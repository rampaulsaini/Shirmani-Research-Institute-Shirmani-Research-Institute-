#!/usr/bin/env python3
"""Regression tests for the public production status contract."""
import json
import tempfile
import unittest
from pathlib import Path

from factory.public_production_materializer import materialize_concrete_asset_status
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
