import unittest

from factory.production_completion_gate import target_complete


class ProductionCompletionGateTests(unittest.TestCase):
    def complete_state(self):
        return {
            "five_thousand_scale_target": 5000,
            "catalog_identities": 5000,
            "concrete_repository_assets": 5000,
            "product_qr_assets": 5000,
            "qc_state": "QC_PASSED",
            "qc_passed": 5000,
            "qc_failed": 0,
        }

    def test_complete_target_skips_duplicate_production(self):
        self.assertTrue(target_complete(self.complete_state()))

    def test_missing_concrete_assets_do_not_skip_production(self):
        state = self.complete_state()
        state["concrete_repository_assets"] = 4999
        self.assertFalse(target_complete(state))

    def test_missing_qr_assets_do_not_skip_production(self):
        state = self.complete_state()
        state["product_qr_assets"] = 4999
        self.assertFalse(target_complete(state))

    def test_qc_not_passed_does_not_skip_production(self):
        state = self.complete_state()
        state["qc_state"] = "READY_FOR_QC"
        self.assertFalse(target_complete(state))

    def test_any_qc_failure_does_not_skip_production(self):
        state = self.complete_state()
        state["qc_failed"] = 1
        self.assertFalse(target_complete(state))

    def test_catalog_below_target_does_not_skip_production(self):
        state = self.complete_state()
        state["catalog_identities"] = 4999
        self.assertFalse(target_complete(state))


if __name__ == "__main__":
    unittest.main()
