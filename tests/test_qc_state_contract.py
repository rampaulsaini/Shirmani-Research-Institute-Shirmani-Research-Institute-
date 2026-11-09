from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from factory.qc_state_contract import sync_public_qc_state


class PublicQCStateContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.generated = self.root / "generated"
        self.generated.mkdir()
        (self.generated / "concrete-product-asset-status.json").write_text(
            json.dumps({"dispatch": "NO"}), encoding="utf-8"
        )
        (self.generated / "live-production-state.json").write_text(
            json.dumps({
                "current_catalog_pending": 0,
                "dispatch_released": 0,
                "sales_claimed": 0,
                "payment_claimed": 0,
            }),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def write_qc(self, **overrides):
        qc = {
            "generated_at": "2026-11-09T00:00:00+00:00",
            "catalog_count": 2,
            "produced_count": 2,
            "qc_passed": 2,
            "qc_failed": 0,
            "release_state": "QC_PASS_READY_FOR_DISPATCH",
            "integrity": {"deterministic_qc": True, "sale_claim": False},
        }
        qc.update(overrides)
        (self.generated / "product-qc-gate.json").write_text(
            json.dumps(qc), encoding="utf-8"
        )

    def read_json(self, name):
        return json.loads((self.generated / name).read_text(encoding="utf-8"))

    def test_passed_qc_counters_reach_public_live_state_without_commercial_claims(self):
        self.write_qc()
        self.assertTrue(sync_public_qc_state(self.root, 2))

        live = self.read_json("live-production-state.json")
        status = self.read_json("concrete-product-asset-status.json")
        self.assertEqual(live["qc_state"], "QC_PASSED")
        self.assertEqual(live["state"], "QC_PASSED_AWAITING_DISPATCH")
        self.assertEqual(live["qc_catalog_count"], 2)
        self.assertEqual(live["qc_produced_count"], 2)
        self.assertEqual(live["qc_passed"], 2)
        self.assertEqual(live["qc_failed"], 0)
        self.assertEqual(status["qc_passed"], 2)
        self.assertEqual(status["dispatch"], "NO")
        self.assertEqual(live["dispatch_released"], 0)
        self.assertEqual(live["sales_claimed"], 0)
        self.assertEqual(live["payment_claimed"], 0)

    def test_failed_qc_never_promotes_public_pass_count(self):
        self.write_qc(
            produced_count=1,
            qc_passed=1,
            qc_failed=1,
            release_state="QC_REVIEW_REQUIRED",
        )
        self.assertFalse(sync_public_qc_state(self.root, 2))

        live = self.read_json("live-production-state.json")
        self.assertEqual(live["qc_state"], "QC_REVIEW_REQUIRED")
        self.assertEqual(live["qc_passed"], 0)
        self.assertEqual(live["qc_failed"], 1)
        self.assertEqual(live["dispatch_released"], 0)
        self.assertEqual(live["sales_claimed"], 0)
        self.assertEqual(live["payment_claimed"], 0)

    def test_malformed_pending_count_does_not_crash_or_claim_completion(self):
        self.write_qc()
        live_path = self.generated / "live-production-state.json"
        for invalid_value in ("unknown", -1, False, 0.0):
            with self.subTest(pending=invalid_value):
                live = json.loads(live_path.read_text(encoding="utf-8"))
                live["current_catalog_pending"] = invalid_value
                live_path.write_text(json.dumps(live), encoding="utf-8")

                self.assertTrue(sync_public_qc_state(self.root, 2))
                updated = self.read_json("live-production-state.json")
                self.assertEqual(updated["state"], "PRODUCTION_STATE_UNAVAILABLE")
                self.assertEqual(updated["dispatch_released"], 0)
                self.assertEqual(updated["sales_claimed"], 0)
                self.assertEqual(updated["payment_claimed"], 0)

    def test_boolean_and_invalid_qc_counts_fail_closed(self):
        for overrides in (
            {"catalog_count": True},
            {"produced_count": True},
            {"qc_passed": True},
            {"qc_failed": False},
            {"qc_failed": -1},
        ):
            with self.subTest(overrides=overrides):
                self.write_qc(**overrides)
                self.assertFalse(sync_public_qc_state(self.root, 2))
                live = self.read_json("live-production-state.json")
                self.assertEqual(live["qc_state"], "READY_FOR_QC")
                self.assertEqual(live["qc_passed"], 0)
                self.assertEqual(live["dispatch_released"], 0)
                self.assertEqual(live["sales_claimed"], 0)
                self.assertEqual(live["payment_claimed"], 0)

    def test_missing_qc_fails_closed(self):
        self.assertFalse(sync_public_qc_state(self.root, 2))
        live = self.read_json("live-production-state.json")
        self.assertEqual(live["qc_state"], "READY_FOR_QC")
        self.assertEqual(live["qc_passed"], 0)
        self.assertEqual(live["qc_failed"], 0)


if __name__ == "__main__":
    unittest.main()
