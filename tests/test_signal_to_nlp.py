import unittest

from factory.signal_to_nlp import (
    SCHEMA_VERSION,
    interpret_observation,
    normalize_observation,
    to_plain_language,
)


class SignalToNlpTests(unittest.TestCase):
    def test_normalization_is_deterministic(self):
        obs = {
            "modality": "BioElectrical",
            "source_id": "plant-001",
            "features": {"voltage": 0.42, "noise": "low"},
        }
        self.assertEqual(normalize_observation(obs), normalize_observation(obs))
        self.assertEqual(normalize_observation(obs)["schema_version"], SCHEMA_VERSION)

    def test_unknown_modality_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_observation({"modality": "telepathy", "features": {}})

    def test_output_preserves_uncertainty_boundary(self):
        result = interpret_observation({
            "modality": "electrical",
            "source_id": "sensor-1",
            "features": {"voltage": 0.42},
        })
        self.assertEqual(result["verification_status"], "UNVERIFIED")
        self.assertIn("No subjective feeling is asserted", result["inference"])
        self.assertIn("प्रत्यक्ष अनुभव का प्रमाण नहीं", to_plain_language(result))


if __name__ == "__main__":
    unittest.main()
