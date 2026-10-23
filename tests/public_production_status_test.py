#!/usr/bin/env python3
"""Regression tests for the public production status contract."""
import json
import tempfile
import unittest
from pathlib import Path

from factory.public_production_materializer import materialize_concrete_asset_status
from factory.qc_state_contract import qc_passed, sync_public_qc_state
from factory.supreme_public_production_sync import build_product_row, has_approved_price


class ConcreteAssetStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "generated").mkdir()
        (self.root / "products" / "production").mkdir(parents=True)
        (self.root / "products" / "production" / "a.html").write_text("A", encoding="utf-8")
        (self.root / "products" / "production" / "b.html").write_text("B", encoding="utf-8")
        catalog = {
            "product_count": 2,
            "products": [
                {"id": "a", "asset": "products/production/a.html"},
                {"id": "b", "asset": "products/production/b.html"},
            ],
        }
        (self.root / "generated" / "1000-digital-products.json").write_text(
            json.dumps(catalog), encoding="utf-8"
        )
        # Reproduce the legacy persisted status that caused the production gate to fail.
        (self.root / "generated" / "concrete-product-asset-status.json").write_text(
            json.dumps({"product_assets": 2, "dispatch": "NO"}), encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_refreshes_timestamp_and_counts_real_assets(self):
        timestamp = "2026-10-16T00:00:00+00:00"
        status = materialize_concrete_asset_status(self.root, generated_at=timestamp)
        self.assertEqual(status["generated_at"], timestamp)
        self.assertEqual(status["product_assets"], 2)
        self.assertEqual(status["concrete_product_assets"], 2)
        self.assertEqual(status["catalog_products"], 2)
        self.assertEqual(status["materialization_percent"], 100.0)
        self.assertEqual(status["state"], "READY_FOR_QC")
        self.assertEqual(status["dispatch"], "NO")

    def test_matching_qc_gate_promotes_only_qc_state_not_dispatch(self):
        (self.root / "generated" / "product-qc-gate.json").write_text(json.dumps({
            "catalog_count": 2, "produced_count": 2, "qc_passed": 2,
            "qc_failed": 0, "release_state": "QC_PASS_READY_FOR_DISPATCH"
        }), encoding="utf-8")
        status = materialize_concrete_asset_status(self.root, generated_at="2026-10-16T00:00:00+00:00")
        self.assertEqual(status["state"], "QC_PASSED_AWAITING_DISPATCH")
        self.assertEqual(status["qc_state"], "QC_PASSED")
        self.assertEqual(status["dispatch"], "NO")

    def test_stale_or_mismatched_qc_does_not_promote_status(self):
        (self.root / "generated" / "product-qc-gate.json").write_text(json.dumps({
            "catalog_count": 2, "produced_count": 2, "qc_passed": 1,
            "qc_failed": 0, "release_state": "QC_PASS_READY_FOR_DISPATCH"
        }), encoding="utf-8")
        status = materialize_concrete_asset_status(self.root, generated_at="2026-10-16T00:00:00+00:00")
        self.assertEqual(status["state"], "READY_FOR_QC")
        self.assertEqual(status["qc_state"], "READY_FOR_QC")
        self.assertEqual(status["dispatch"], "NO")

    def test_missing_asset_is_not_counted_as_produced(self):
        (self.root / "products" / "production" / "b.html").unlink()
        status = materialize_concrete_asset_status(self.root, generated_at="2026-10-16T00:00:00+00:00")
        self.assertEqual(status["product_assets"], 1)
        self.assertEqual(status["materialization_percent"], 50.0)
        self.assertEqual(status["state"], "IN_PROGRESS")

    def test_path_traversal_asset_is_not_counted(self):
        catalog_path = self.root / "generated" / "1000-digital-products.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["products"][0]["asset"] = "../outside.html"
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
        status = materialize_concrete_asset_status(self.root, generated_at="2026-10-16T00:00:00+00:00")
        self.assertEqual(status["product_assets"], 1)



class QCStateContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "generated").mkdir()
        (self.root / "generated" / "concrete-product-asset-status.json").write_text(
            json.dumps({"state": "READY_FOR_QC", "dispatch": "NO"}), encoding="utf-8"
        )
        (self.root / "generated" / "live-production-state.json").write_text(
            json.dumps({
                "current_catalog_pending": 0,
                "dispatch_released": 0,
                "sales_claimed": 0,
                "payment_claimed": 0,
                "independent_verification_claimed": 0,
            }), encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_qc_pass_promotes_only_qc_state_not_dispatch_or_revenue(self):
        qc = {
            "catalog_count": 2, "produced_count": 2, "qc_passed": 2, "qc_failed": 0,
            "release_state": "QC_PASS_READY_FOR_DISPATCH", "dispatch_default": "NO",
            "generated_at": "2026-10-23T00:00:00+00:00",
            "integrity": {"deterministic_qc": True, "sale_claim": False},
        }
        self.assertTrue(qc_passed(qc, 2))
        (self.root / "generated" / "product-qc-gate.json").write_text(
            json.dumps(qc), encoding="utf-8"
        )
        self.assertTrue(sync_public_qc_state(self.root, 2))
        status = json.loads((self.root / "generated" / "concrete-product-asset-status.json").read_text())
        live = json.loads((self.root / "generated" / "live-production-state.json").read_text())
        self.assertEqual(status["state"], "QC_PASSED")
        self.assertEqual(live["qc_state"], "QC_PASSED")
        self.assertEqual(live["state"], "QC_PASSED_AWAITING_DISPATCH")
        self.assertEqual(live["dispatch_released"], 0)
        self.assertEqual(live["sales_claimed"], 0)
        self.assertEqual(live["payment_claimed"], 0)
        self.assertEqual(live["independent_verification_claimed"], 0)

    def test_incomplete_or_failed_qc_never_promotes_public_state(self):
        qc = {
            "catalog_count": 2, "produced_count": 2, "qc_passed": 1, "qc_failed": 1,
            "release_state": "QC_REVIEW_REQUIRED", "dispatch_default": "NO",
            "integrity": {"deterministic_qc": True, "sale_claim": False},
        }
        self.assertFalse(qc_passed(qc, 2))
        (self.root / "generated" / "product-qc-gate.json").write_text(
            json.dumps(qc), encoding="utf-8"
        )
        self.assertFalse(sync_public_qc_state(self.root, 2))
        status = json.loads((self.root / "generated" / "concrete-product-asset-status.json").read_text())
        live = json.loads((self.root / "generated" / "live-production-state.json").read_text())
        self.assertEqual(status["state"], "QC_REVIEW_REQUIRED")
        self.assertEqual(live["qc_state"], "QC_REVIEW_REQUIRED")
        self.assertEqual(live["dispatch_released"], 0)
        self.assertEqual(live["sales_claimed"], 0)
        self.assertEqual(live["payment_claimed"], 0)


    def test_integrity_repair_reconciles_qc_after_placeholder_write(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github" / "workflows" / "production-state-integrity-repair.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            'cp "$GITHUB_WORKSPACE/factory/qc_state_contract.py" factory/qc_state_contract.py',
            workflow,
        )
        self.assertLess(
            workflow.index('(gen/"four-stage-production-status.json")'),
            workflow.index("sync_public_qc_state"),
        )
        self.assertIn("PUBLIC_STATE_FAIL", workflow)


class CommercialReadinessTests(unittest.TestCase):
    def test_unapproved_price_is_quote_required(self):
        product = {"id": "SP-0001", "name": "Starter Tool", "price_inr": 99}
        row = build_product_row(product, "products/production/sp-0001.html", "2026-10-21T00:00:00+00:00")
        self.assertEqual(row["name"], "Starter Tool")
        self.assertEqual(row["sale_state"], "QUOTE_REQUIRED")
        self.assertEqual(row["commercial_status"], "QUOTE_REQUIRED")
        self.assertFalse(row["payment_enabled"])
        self.assertFalse(has_approved_price(product))

    def test_approved_price_requires_explicit_flag_and_positive_amount(self):
        approved = {"id": "SP-0002", "name": "Research Tool", "price_inr": 199, "commercial_status": "PRICE_APPROVED"}
        row = build_product_row(approved, "products/production/sp-0002.html", "2026-10-21T00:00:00+00:00")
        self.assertEqual(row["sale_state"], "READY_FOR_ORDER")
        self.assertEqual(row["commercial_status"], "PRICE_APPROVED")
        self.assertTrue(row["payment_enabled"])
        self.assertTrue(has_approved_price(approved))

    def test_zero_or_invalid_price_cannot_be_approved(self):
        for amount in (0, -1, None, "not-a-price", float("nan"), float("inf")):
            product = {"id": "SP-0003", "commercial_status": "PRICE_APPROVED", "price_inr": amount}
            self.assertFalse(has_approved_price(product), msg=f"unexpectedly approved price: {amount!r}")
            row = build_product_row(product, "products/production/sp-0003.html", "2026-10-21T00:00:00+00:00")
            self.assertEqual(row["sale_state"], "QUOTE_REQUIRED")
            self.assertFalse(row["payment_enabled"])


if __name__ == "__main__":
    unittest.main()
