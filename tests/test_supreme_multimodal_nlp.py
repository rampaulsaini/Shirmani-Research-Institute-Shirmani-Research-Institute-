import unittest
from factory.supreme_multimodal_nlp import SCHEMA_VERSION, classify_pattern, extract_features, signal_to_nlp

class SupremeMultimodalNlpTests(unittest.TestCase):
    def test_schema_is_stable(self):
        self.assertEqual(SCHEMA_VERSION, "1.0")

    def test_constant_signal_is_stable(self):
        signal = {"channel": "electrical", "values": [2, 2, 2], "unit": "mV", "source_id": "s1"}
        features = extract_features(signal)
        self.assertEqual(features["stddev"], 0.0)
        self.assertEqual(classify_pattern(features)["pattern"], "stable")

    def test_high_variation_is_detected(self):
        signal = {"channel": "vibration", "values": [1, 10, 1, 10], "unit": "a.u.", "source_id": "s2"}
        result = signal_to_nlp(signal, ["experiment-1"])
        self.assertEqual(result["pattern"]["pattern"], "high_variation")
        self.assertEqual(result["verification_status"], "UNVERIFIED")
        self.assertIn("subjective feeling", result["claim_boundary"])

    def test_invalid_channel_fails_closed(self):
        with self.assertRaises(ValueError):
            extract_features({"channel": "imaginary", "values": [1, 2]})

    def test_output_is_deterministic(self):
        signal = {"channel": "temperature", "values": [20, 21, 20], "unit": "C", "source_id": "s3"}
        self.assertEqual(signal_to_nlp(signal), signal_to_nlp(signal))

if __name__ == "__main__":
    unittest.main()
