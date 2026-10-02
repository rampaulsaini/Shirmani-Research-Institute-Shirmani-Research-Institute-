"""Regression coverage for numerically extreme but finite signal values."""
import math
import unittest

from agents.supreme_nlp import build_record, summarize


class SupremeNLPNumericalRobustnessTests(unittest.TestCase):
    def test_extreme_values_do_not_overflow(self):
        rows = [
            {"modality": "sensor", "feature": "x", "value": 1e308, "quality": 1.0, "source": "a"},
            {"modality": "sensor", "feature": "x", "value": -1e308, "quality": 1.0, "source": "b"},
            {"modality": "audio", "feature": "x", "value": 1e307, "quality": 1.0, "source": "c"},
        ]
        record = build_record(rows, "robustness-extreme")
        features = record["result"]["features"]
        for key in ("mean", "spread", "anomaly_score", "agreement", "quality", "drift_score"):
            self.assertTrue(math.isfinite(features[key]), key)
        self.assertTrue(math.isfinite(record["result"]["interpretation"]["confidence"]))

    def test_zero_scale_remains_deterministic(self):
        result = summarize([
            {"modality": "sensor", "feature": "x", "value": 0.0, "quality": 1.0, "source": "a"},
            {"modality": "audio", "feature": "x", "value": 0.0, "quality": 1.0, "source": "b"},
        ])
        self.assertEqual(result["features"]["mean"], 0.0)
        self.assertEqual(result["features"]["spread"], 0.0)
        self.assertTrue(math.isfinite(result["interpretation"]["confidence"]))


if __name__ == "__main__":
    unittest.main()
