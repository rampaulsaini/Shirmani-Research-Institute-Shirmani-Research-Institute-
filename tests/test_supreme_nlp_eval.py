import unittest

from factory.supreme_nlp_eval import (
    classification_metrics,
    expected_calibration_error,
    quality_gate,
    robustness_consistency,
)


class SupremeNLPEvalTests(unittest.TestCase):
    def setUp(self):
        self.true = ["stable", "stable", "change", "change", "stable", "change"]
        self.pred = ["stable", "stable", "change", "stable", "change", "change"]
        self.conf = [0.90, 0.80, 0.85, 0.70, 0.60, 0.95]

    def test_metrics_are_deterministic_and_bounded(self):
        metrics = classification_metrics(self.true, self.pred, self.conf, [False] * 6)
        self.assertAlmostEqual(metrics["accuracy"], 4 / 6)
        self.assertGreaterEqual(metrics["macro_f1"], 0.0)
        self.assertLessEqual(metrics["macro_f1"], 1.0)
        self.assertGreaterEqual(metrics["expected_calibration_error"], 0.0)
        self.assertLessEqual(metrics["expected_calibration_error"], 1.0)

    def test_calibration_matches_direct_function(self):
        metrics = classification_metrics(self.true, self.pred, self.conf)
        self.assertAlmostEqual(
            metrics["expected_calibration_error"],
            expected_calibration_error(self.true, self.pred, self.conf),
        )

    def test_robustness_is_bounded(self):
        score = robustness_consistency(
            ["stable", "change", "stable"],
            ["stable", "stable", "stable"],
        )
        self.assertAlmostEqual(score, 2 / 3)

    def test_quality_gate_fails_closed_on_bad_metrics(self):
        result = quality_gate(
            {
                "accuracy": 0.99,
                "macro_f1": 0.99,
                "expected_calibration_error": 0.01,
                "robustness": 0.20,
            }
        )
        self.assertEqual(result["status"], "FAIL")
        self.assertFalse(result["checks"]["robustness"])

    def test_quality_gate_requires_complete_metrics(self):
        result = quality_gate({"accuracy": 1.0})
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(result["reason"], "missing_metrics")


if __name__ == "__main__":
    unittest.main()
