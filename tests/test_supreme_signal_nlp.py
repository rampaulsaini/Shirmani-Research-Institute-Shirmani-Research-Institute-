import unittest

from factory.supreme_signal_nlp import (
    SCHEMA_VERSION,
    interpret_signal,
    summarize_signal,
    translate_signal,
)


class SupremeSignalNlpTests(unittest.TestCase):
    def test_empty_signal_fails_closed(self):
        result = translate_signal([])
        self.assertEqual(result["summary"]["status"], "INSUFFICIENT_DATA")
        self.assertEqual(result["interpretation"]["confidence"], 0.0)

    def test_signal_features_are_deterministic(self):
        result = summarize_signal([1, 2, 3, 4], sample_rate_hz=2, baseline=[1, 1, 1, 1], channel="plant")
        self.assertEqual(result["schema_version"], SCHEMA_VERSION)
        self.assertEqual(result["sample_count"], 4)
        self.assertEqual(result["features"]["delta_from_baseline"], 1.5)
        self.assertEqual(result["features"]["duration_seconds"], 2.0)

    def test_interpretation_is_observable_not_mind_reading(self):
        result = interpret_signal(
            summarize_signal([1, 2, 3, 4], baseline=[1, 1, 1, 1]),
            context="controlled observation",
        )
        text = result["plain_language"]
        self.assertIn("मापित", text)
        self.assertIn("चेतना", text)
        self.assertNotIn("भावना सिद्ध", text)

    def test_translation_has_evidence_and_confidence(self):
        result = translate_signal([1, 1, 2, 2, 3], baseline=[1, 1, 1, 1, 1], channel="bioelectric")
        self.assertEqual(result["pipeline"], "observe->clean->summarize->interpret->explain")
        self.assertGreater(result["interpretation"]["confidence"], 0.0)
        self.assertTrue(result["interpretation"]["evidence"])


if __name__ == "__main__":
    unittest.main()
