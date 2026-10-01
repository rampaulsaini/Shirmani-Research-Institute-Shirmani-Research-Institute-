import unittest

from agents.supreme_nlp import Signal, translate, make_record
from agents.automission_engine import run_cycle, publish_gate


class SupremeNLPTests(unittest.TestCase):
    def test_signal_translation_is_conservative(self):
        r = translate([Signal("voltage", 1.0, "mV"), Signal("voltage", 1.05, "mV")])
        self.assertGreaterEqual(r.confidence, 0)
        self.assertLessEqual(r.confidence, 1)
        self.assertIn("प्रत्यक्ष प्रमाण", " ".join(r.limitations))

    def test_record_is_hashed(self):
        r = make_record([Signal("temperature", 25.0, "C")])
        self.assertEqual(len(r["record_sha256"]), 64)

    def test_publish_requires_independent_verification(self):
        r = run_cycle({"evidence": ["sensor:001"]})
        ok, errors = publish_gate(r)
        self.assertFalse(ok)
        self.assertIn("NOT_INDEPENDENTLY_VERIFIED", errors)


if __name__ == "__main__":
    unittest.main()
