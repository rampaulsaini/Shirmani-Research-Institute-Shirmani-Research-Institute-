import unittest

from agents.supreme_nlp import build_record, summarize, to_simple_language


class SupremeNLPRobustnessTests(unittest.TestCase):
    def test_empty_and_zero_quality_are_fail_closed(self):
        self.assertEqual(summarize([])["status"], "no_data")
        self.assertEqual(
            summarize([{"modality": "sensor", "feature": "x", "value": 1, "quality": 0}])["status"],
            "insufficient_quality",
        )

    def test_multimodal_translation_preserves_verification_boundary(self):
        rows = [
            {"modality": "audio", "feature": "vibration", "value": 1.0, "quality": 1.0, "source": "s1"},
            {"modality": "electrical", "feature": "signal", "value": 1.1, "quality": 0.95, "source": "s2"},
            {"modality": "environment", "feature": "temperature", "value": 0.9, "quality": 0.9, "source": "s3"},
        ]
        record = build_record(rows, "robustness-multimodal")
        result = record["result"]
        self.assertEqual(result["status"], "interpreted")
        self.assertEqual(result["verification"]["status"], "UNVERIFIED")
        self.assertTrue(result["verification"]["independent_required"])
        self.assertTrue(result["verification"]["replication_required"])
        self.assertEqual(result["interpretation"]["confidence_status"], "UNCALIBRATED")
        simple = to_simple_language(result)
        self.assertIn("प्रत्यक्ष भाव", simple)
        self.assertIn("प्रमाण", simple)

    def test_extreme_values_are_normalized_without_nan_or_infinity(self):
        rows = [
            {"modality": "sensor", "feature": "a", "value": "nan", "quality": 1.0},
            {"modality": "sensor", "feature": "b", "value": "inf", "quality": 1.0},
            {"modality": "sensor", "feature": "c", "value": -1e300, "quality": 1.0},
        ]
        record = build_record(rows, "robustness-extreme")
        self.assertEqual(record["result"]["status"], "interpreted")
        self.assertNotIn("nan", record["simple_language"].lower())
        self.assertNotIn("inf", record["simple_language"].lower())

    def test_baseline_drift_is_exposed_as_feature_not_hidden_claim(self):
        rows = [
            {
                "modality": "plant-signal",
                "feature": "electrical",
                "value": 2.0,
                "baseline_mean": 1.0,
                "baseline_std": 0.2,
                "quality": 1.0,
                "source": "calibrated-sensor",
            },
            {
                "modality": "plant-signal",
                "feature": "vibration",
                "value": 1.0,
                "baseline_mean": 1.0,
                "baseline_std": 0.2,
                "quality": 1.0,
                "source": "calibrated-sensor-2",
            },
        ]
        result = summarize(rows)
        self.assertGreater(result["features"]["drift_score"], 0.0)
        self.assertIn("drift_score", result["features"])
        self.assertEqual(result["verification"]["status"], "UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
