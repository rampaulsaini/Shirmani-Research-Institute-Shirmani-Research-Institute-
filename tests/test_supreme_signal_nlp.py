import unittest

from factory.supreme_signal_nlp import SCHEMA_VERSION, summarize_signal


class SupremeSignalNlpTests(unittest.TestCase):
    def test_empty_signal_fails_closed(self):
        r = summarize_signal("plant_signal", [])
        self.assertEqual(r["status"], "NO_VALID_SIGNAL")
        self.assertEqual(r["confidence"], 0.0)

    def test_signal_translation_is_deterministic(self):
        values = [1.0, 1.2, 1.4, 1.5, 1.7]
        a = summarize_signal("electrical_activity", values, unit=" mV", baseline=1.0)
        b = summarize_signal("electrical_activity", values, unit=" mV", baseline=1.0)
        self.assertEqual(a, b)
        self.assertEqual(a["schema_version"], SCHEMA_VERSION)
        self.assertEqual(a["direction"], "increasing")
        self.assertGreaterEqual(a["confidence"], 0.0)
        self.assertLessEqual(a["confidence"], 1.0)

    def test_interpretation_does_not_claim_subjective_feeling(self):
        r = summarize_signal("vibration", [2, 2, 2, 2], unit=" Hz")
        self.assertIn("measurable signal", r["interpretation"])
        self.assertIn("भावना", r["plain_language"])


if __name__ == "__main__":
    unittest.main()
