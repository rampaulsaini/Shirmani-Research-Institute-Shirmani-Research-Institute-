import unittest
from factory.signal_to_nlp import Observation, observation_to_nlp, translate_batch

class SignalToNlpTests(unittest.TestCase):
    def test_above_baseline_is_translated_without_claiming_feeling(self):
        result = observation_to_nlp(Observation(
            "plant-sensor", "electrical", "amplitude", 2.0, "mV", 1.0, 0.2, ("sensor:1",)
        ))
        self.assertEqual(result["status"], "above-baseline")
        self.assertIn("signal change", result["interpretation"])
        self.assertTrue(result["confidence"]["not_probability_of_feeling"])

    def test_missing_baseline_remains_observation(self):
        result = observation_to_nlp(Observation("object-sensor", "vibration", "frequency", 12.5, "Hz"))
        self.assertEqual(result["status"], "observed")
        self.assertEqual(result["confidence"]["score"], 0.0)

    def test_batch_is_deterministic(self):
        row = Observation("s", "sound", "level", 3.0, "dB")
        self.assertEqual(translate_batch([row]), translate_batch([row]))

if __name__ == "__main__":
    unittest.main()
