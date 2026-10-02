import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from factory.supreme_nlp import translate

class SupremeNLPTests(unittest.TestCase):
    def base(self):
        return {
            "observation_id":"demo-001",
            "subject_type":"plant",
            "observations":[
                {"channel":"leaf_temperature","value":24.5,"unit":"C","timestamp":"2026-10-02T00:00:00Z"},
                {"channel":"electrical_signal","value":1.2,"unit":"mV","timestamp":"2026-10-02T00:00:01Z"}
            ],
            "interpretation_policy":{
                "measured_vs_inferred":True,
                "abstain_on_missing_evidence":True
            }
        }

    def test_plain_language_is_generated(self):
        result = translate(self.base())
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["inference_status"], "NOT_ESTABLISHED")
        self.assertIn("leaf_temperature", result["plain_language"])

    def test_missing_policy_blocks(self):
        record = self.base()
        record["interpretation_policy"]["measured_vs_inferred"] = False
        self.assertEqual(translate(record)["status"], "BLOCK")

if __name__ == "__main__":
    unittest.main()
