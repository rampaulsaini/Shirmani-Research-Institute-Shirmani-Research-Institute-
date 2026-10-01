import unittest

from factory.supreme_accuracy_v3 import audit


class SupremeAccuracyV3Tests(unittest.TestCase):
    def base_row(self):
        return {
            "id": "1",
            "text": "independent evidence trace",
            "content_hash": "7d2e1f8d8c6f8a0f5f1b8b2f8b1d3e8a7e8e4d2b8e7e7d6f8b5d2d8c8a8a8c8",
            "source_ids": ["source-1"],
            "method_trace": ["source_provenance"],
            "claim_class": "unverified_claim",
            "evidence_status": "requires_independent_verification",
        }

    def test_integrity_gate_is_fail_closed(self):
        row = self.base_row()
        import hashlib
        row["content_hash"] = hashlib.sha256(row["text"].encode()).hexdigest()
        good = audit([row], {"generated_at": "now"}, {
            "independently_verified_records": 0
        })
        self.assertEqual(good["execution_gate"], "PASS")
        self.assertEqual(good["publication_gate"], "HOLD")
        self.assertEqual(good["accuracy_measurement"], "NOT_MEASURED")

    def test_duplicate_ids_stop_execution(self):
        row = self.base_row()
        import hashlib
        row["content_hash"] = hashlib.sha256(row["text"].encode()).hexdigest()
        bad = audit([row, dict(row)], {"generated_at": "now"}, {
            "independently_verified_records": 0
        })
        self.assertEqual(bad["execution_gate"], "HOLD")
        self.assertEqual(bad["next_action"], "STOP_AND_REPAIR")

    def test_independent_verification_is_required_for_publication(self):
        row = self.base_row()
        import hashlib
        row["content_hash"] = hashlib.sha256(row["text"].encode()).hexdigest()
        verified = audit([row], {"generated_at": "now"}, {
            "independently_verified_records": 1
        })
        self.assertEqual(verified["publication_gate"], "PASS")


if __name__ == "__main__":
    unittest.main()
