import unittest
from factory.signal_to_language import SignalObservation, plain_language_interpretation, signal_features

class SignalToLanguageTests(unittest.TestCase):
    def test_signal_features_are_deterministic(self):
        rows = [
            SignalObservation("electrical", 12.0, 10.0, "mV"),
            SignalObservation("vibration", 8.0, 10.0, "Hz"),
        ]
        self.assertEqual(signal_features(rows), signal_features(rows))

    def test_plain_language_separates_measurement_from_feeling(self):
        result = plain_language_interpretation(
            [SignalObservation("temperature", 30.0, 25.0, "C")],
            context="plant",
            model_confidence=0.8,
        )
        self.assertEqual(result["epistemic_status"], "measurement_plus_model_interpretation")
        self.assertIn("not a direct reading of subjective feeling", result["simple_language"])
        self.assertEqual(result["confidence"], 0.8)

    def test_invalid_confidence_fails_closed(self):
        with self.assertRaises(ValueError):
            plain_language_interpretation(
                [SignalObservation("x", 1.0, 0.0)], model_confidence=1.1
            )

if __name__ == "__main__":
    unittest.main()
