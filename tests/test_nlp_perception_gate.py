import unittest
from factory.nlp_perception_gate import validate


def base(status="OBSERVED"):
    return {
        "record_id": "test-001",
        "timestamp": "2026-10-01T00:00:00Z",
        "status": status,
        "modality": "sensor",
        "subject_type": "plant",
        "content": "Observed sensor response.",
        "features": [{"name": "response_signal", "value": 1}],
        "evidence_refs": [],
        "uncertainty": 0.0,
        "model": None,
        "model_version": None,
        "provenance": {"source_id": "test-fixture"},
        "human_review": False,
    }


class GateContractTests(unittest.TestCase):
    def test_observed_record_passes_without_inference_claim(self):
        self.assertEqual(validate(base()), [])

    def test_inferred_record_requires_evidence(self):
        record = base("INFERRED")
        record["model"] = "baseline"
        record["model_version"] = "1"
        self.assertIn("inferred_requires_evidence_refs", validate(record))

    def test_inferred_record_requires_model_identity(self):
        record = base("INFERRED")
        record["evidence_refs"] = ["study:test"]
        errors = validate(record)
        self.assertIn("model_derived_requires_model_identity", errors)

    def test_inferred_record_with_evidence_and_model_passes(self):
        record = base("INFERRED")
        record["evidence_refs"] = ["study:test"]
        record["model"] = "baseline"
        record["model_version"] = "1"
        self.assertEqual(validate(record), [])

    def test_uncertainty_is_bounded(self):
        record = base()
        record["uncertainty"] = 1.1
        self.assertIn("invalid:uncertainty", validate(record))

    def test_invalid_subject_type_is_rejected(self):
        record = base()
        record["subject_type"] = "fictional_consciousness"
        self.assertIn("invalid:subject_type", validate(record))


if __name__ == "__main__":
    unittest.main()
