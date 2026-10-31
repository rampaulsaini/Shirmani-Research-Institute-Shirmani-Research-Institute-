import unittest

from factory.production_completion_gate import target_complete


class ProductionCompletionGateTests(unittest.TestCase):
    def complete_state(self):
        return {
            "five_thousand_scale_target": 5000,
            "catalog_identities": 5000,
            "concrete_repository_assets": 5000,
            "product_qr_assets": 5000,
        }

    def complete_qc(self):
        return {
            "catalog_count": 5000,
            "produced_count": 5000,
            "qc_passed": 5000,
            "qc_failed": 0,
            "release_state": "QC_PASS_READY_FOR_DISPATCH",
            "integrity": {"deterministic_qc": True, "sale_claim": False},
        }

    def test_complete_target_skips_duplicate_production(self):
        self.assertTrue(target_complete(self.complete_state(), self.complete_qc()))

    def test_stale_summary_qc_fields_do_not_override_canonical_qc(self):
        state = self.complete_state()
        state["qc_state"] = "READY_FOR_QC"
        state["qc_passed"] = 0
        self.assertTrue(target_complete(state, self.complete_qc()))

    def test_missing_concrete_assets_does_not_skip(self):
        state = self.complete_state()
        state["concrete_repository_assets"] = 4999
        self.assertFalse(target_complete(state, self.complete_qc()))

    def test_missing_qr_assets_does_not_skip(self):
        state = self.complete_state()
        state["product_qr_assets"] = 4999
        self.assertFalse(target_complete(state, self.complete_qc()))

    def test_qc_not_passed_does_not_skip(self):
        qc = self.complete_qc()
        qc["release_state"] = "QC_REVIEW_REQUIRED"
        self.assertFalse(target_complete(self.complete_state(), qc))

    def test_qc_failure_does_not_skip(self):
        qc = self.complete_qc()
        qc["qc_failed"] = 1
        self.assertFalse(target_complete(self.complete_state(), qc))

    def test_missing_integrity_does_not_skip(self):
        qc = self.complete_qc()
        qc.pop("integrity")
        self.assertFalse(target_complete(self.complete_state(), qc))

    def test_bad_counter_does_not_skip(self):
        state = self.complete_state()
        state["catalog_identities"] = "not-a-number"
        self.assertFalse(target_complete(state, self.complete_qc()))


if __name__ == "__main__":
    unittest.main()
