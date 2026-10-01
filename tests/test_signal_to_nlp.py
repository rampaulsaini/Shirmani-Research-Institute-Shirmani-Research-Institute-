import unittest

from factory.signal_to_nlp import interpret_observations, normalize_observation


class SignalToNlpTests(unittest.TestCase):
    def test_observable_signal_becomes_plain_language(self):
        result = interpret_observations([{
            "source": "plant-sensor-01",
            "feature": "electrical_signal",
            "value": 12.5,
            "unit": "mV",
            "baseline": 10,
            "direction": "rising",
        }])
        self.assertIn("plant-sensor-01", result["plain_language"])
        self.assertIn("12.5mV", result["plain_language"])
        self.assertIn("do not by themselves establish", result["interpretation_boundary"])

    def test_invalid_signal_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_observation({"source": "x", "feature": "y", "value": "unknown"})

    def test_no_observations_is_explicit(self):
        result = interpret_observations([])
        self.assertEqual(result["confidence"], 0.0)
        self.assertIn("No valid observations", result["plain_language"])


if __name__ == "__main__":
    unittest.main()
