import unittest
from agents.supreme_nlp import build_record, validate_record_contract

class SupremeNLPContractTests(unittest.TestCase):
    def test_multimodal_record_is_auditable(self):
        record = build_record([
            {"modality":"bioelectric","feature":"signal","value":0.42,"unit":"mV","quality":0.95,"source":"synthetic-a"},
            {"modality":"vibration","feature":"frequency","value":12.4,"unit":"Hz","quality":0.90,"source":"synthetic-b"},
        ], "test-001")
        self.assertEqual(record["provenance"]["verification_status"], "UNVERIFIED")
        self.assertEqual(validate_record_contract(record), [])
        self.assertGreaterEqual(record["result"]["features"]["modalities"], 2)
        self.assertIn("subjective", " ".join(record["result"]["interpretation"]["limitations"]))

    def test_empty_input_fail_closed(self):
        record = build_record([], "empty")
        self.assertEqual(record["result"]["status"], "no_data")
        self.assertEqual(validate_record_contract(record), [])

if __name__ == "__main__":
    unittest.main()
