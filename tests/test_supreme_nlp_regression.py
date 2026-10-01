import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("supreme_nlp_regression", ROOT / "scripts" / "supreme_nlp_regression.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class SupremeNlpRegressionTests(unittest.TestCase):
    def test_observation_passes(self):
        record = {
            "record_id": "obs-1",
            "level": "OBSERVED",
            "input_provenance": {"source_type": "sensor", "timestamp": "2026-10-01T00:00:00Z"},
            "observation": {"signal": "leaf_response", "value": 0.8},
            "uncertainty": 0.0,
        }
        self.assertEqual(MOD.validate_record(record), [])

    def test_inference_requires_evidence(self):
        record = {
            "record_id": "inf-1",
            "level": "INFERRED",
            "input_provenance": {"source_type": "sensor"},
            "observation": {"signal": "response"},
            "uncertainty": 0.2,
            "evidence": [],
        }
        self.assertIn("inferred-without-evidence", MOD.validate_record(record))

    def test_unsupported_subjective_claim_is_rejected(self):
        record = {
            "record_id": "bad-1",
            "level": "INFERRED",
            "input_provenance": {"source_type": "sensor"},
            "observation": {"text": "This proves the organism feels pain."},
            "uncertainty": 0.1,
            "evidence": ["study-1"],
        }
        self.assertIn("integrity:unsupported-certainty-language", MOD.validate_record(record))

    def test_batch_metrics_are_deterministic(self):
        records = [{
            "record_id": "obs-1",
            "level": "OBSERVED",
            "input_provenance": {"source_type": "telemetry"},
            "observation": {"value": 1},
            "uncertainty": 0.0,
        }]
        report = MOD.evaluate(records)
        self.assertEqual(report["pass_rate"], 1.0)
        self.assertTrue(report["all_valid"])

if __name__ == "__main__":
    unittest.main()
