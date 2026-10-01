import unittest

from factory.supreme_multimodal_nlp import (
    SCHEMA_VERSION,
    classify_pattern,
    extract_features,
    signal_to_nlp,
)


class SupremeMultimodalNlpTests(unittest.TestCase):
    def test_schema_is_stable(self):
        self.assertEqual(SCHEMA_VERSION, "1.1")

    def test_constant_signal_is_stable(self):
        signal = {
            "channel": "electrical",
            "values": [2, 2, 2],
            "unit": "mV",
            "source_id": "s1",
            "timestamp": "2026-10-01T00:00:00Z",
        }
        features = extract_features(signal)
        self.assertEqual(features["stddev"], 0.0)
        self.assertEqual(classify_pattern(features)["pattern"], "stable")

    def test_high_variation_and_direction_are_detected(self):
        signal = {
            "channel": "vibration",
            "values": [1, 10, 1, 10],
            "unit": "a.u.",
            "source_id": "s2",
            "timestamp": "2026-10-01T00:00:00Z",
        }
        result = signal_to_nlp(signal, ["experiment-1"])
        self.assertEqual(result["pattern"]["pattern"], "high_variation")
        self.assertEqual(result["pattern"]["direction"], "rising")
        self.assertEqual(result["verification_status"], "UNVERIFIED")
        self.assertIn("subjective feeling", result["claim_boundary"])

    def test_invalid_channel_fails_closed(self):
        with self.assertRaises(ValueError):
            extract_features({"channel": "imaginary", "values": [1, 2]})

    def test_nonfinite_samples_are_tracked(self):
        result = signal_to_nlp({
            "channel": "temperature",
            "values": [20, float("nan"), 20, 21],
            "unit": "C",
            "source_id": "s3",
            "timestamp": "2026-10-01T00:00:00Z",
        })
        self.assertEqual(result["quality"]["sample_count"], 3)
        self.assertIn("NONFINITE_SAMPLES_DROPPED", result["quality"]["flags"])

    def test_missing_metadata_is_explicit(self):
        result = signal_to_nlp({
            "channel": "light",
            "values": [1, 1, 1],
        })
        self.assertIn("MISSING_TIMESTAMP", result["quality"]["flags"])
        self.assertIn("MISSING_SOURCE_ID", result["quality"]["flags"])
        self.assertFalse(result["quality"]["quality_pass"])

    def test_output_is_deterministic(self):
        signal = {
            "channel": "temperature",
            "values": [20, 21, 20],
            "unit": "C",
            "source_id": "s4",
            "timestamp": "2026-10-01T00:00:00Z",
        }
        self.assertEqual(signal_to_nlp(signal), signal_to_nlp(signal))


if __name__ == "__main__":
    unittest.main()
