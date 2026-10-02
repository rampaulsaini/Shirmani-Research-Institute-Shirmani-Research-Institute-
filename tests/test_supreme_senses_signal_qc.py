import unittest
from factory.supreme_senses_signal_qc import validate

BASE = {
    "record_id": "smoke-001",
    "timestamp": "2026-10-02T00:00:00Z",
    "source_type": "sensor",
    "modality": "multimodal",
    "raw_reference": "synthetic://smoke-001",
    "measurement": "electrical and audio features recorded",
    "detected_pattern": "repeatable cross-modal pattern",
    "model_inference": "pattern is compatible with the labelled baseline",
    "plain_language": "The measured signals show a repeatable pattern; the cause is not established.",
    "confidence": 0.82,
    "uncertainty": ["synthetic data", "no causal conclusion"],
    "evidence": ["synthetic baseline v1"],
    "alternative_interpretations": ["instrument noise", "environmental variation"],
    "verification_state": "UNVERIFIED",
}

class SupremeSensesQCTests(unittest.TestCase):
    def test_valid_record_passes(self):
        self.assertEqual(validate(BASE), [])

    def test_subjective_claim_is_blocked(self):
        record = dict(BASE)
        record["plain_language"] = "This proves consciousness."
        errors = validate(record)
        self.assertTrue(any("unsupported subjective-state claim" in e for e in errors))

    def test_missing_evidence_blocks(self):
        record = dict(BASE)
        record["evidence"] = []
        self.assertTrue(any("evidence is required" in e for e in validate(record)))

if __name__ == "__main__":
    unittest.main()
