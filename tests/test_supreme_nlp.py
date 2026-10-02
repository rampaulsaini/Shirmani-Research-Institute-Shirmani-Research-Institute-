import unittest

from agents.supreme_nlp import build_record, summarize, to_simple_language
from agents.supreme_nlp_quality import QualityThresholds, evaluate, expected_calibration_error


class SupremeNlpCoreTests(unittest.TestCase):
    def test_empty_input_abstains(self):
        self.assertEqual(summarize([])["status"], "no_data")

    def test_zero_quality_abstains(self):
        result = summarize([{
            "modality": "sensor", "feature": "x", "value": 1.0,
            "quality": 0.0, "source": "bad"
        }])
        self.assertEqual(result["status"], "insufficient_quality")

    def test_stable_pattern_is_deterministic(self):
        rows = [
            {"modality": "sensor", "feature": "x", "value": 1.00, "quality": 1.0, "source": "a"},
            {"modality": "sensor", "feature": "x", "value": 1.01, "quality": 1.0, "source": "b"},
            {"modality": "audio", "feature": "x", "value": 0.99, "quality": 1.0, "source": "c"},
            {"modality": "thermal", "feature": "x", "value": 1.00, "quality": 1.0, "source": "d"},
        ]
        a = build_record(rows, "test")
        b = build_record(rows, "test")
        self.assertEqual(a["result"], b["result"])
        self.assertEqual(len(a["fingerprint"]), 64)
        self.assertIn("प्रत्यक्ष भाव", to_simple_language(a["result"]))

    def test_quality_gate_is_fail_closed(self):
        rows = [
            {"modality": "sensor", "feature": "x", "value": 1.0, "quality": 1.0, "source": "a"},
            {"modality": "audio", "feature": "x", "value": 1.01, "quality": 1.0, "source": "b"},
        ]
        report = evaluate(build_record(rows, "quality"))
        self.assertFalse(report["promotion_allowed"])
        self.assertTrue(report["governance"]["fail_closed"])
        self.assertTrue(report["governance"]["independent_verification_required"])

    def test_quality_gate_blocks_insufficient_samples(self):
        rows = [
            {"modality": "sensor", "feature": "x", "value": 1.0,
             "quality": 1.0, "source": "a"}
            for _ in range(2)
        ]
        report = evaluate(
            build_record(rows, "insufficient"),
            thresholds=QualityThresholds(min_samples=10)
        )
        self.assertIn("sample_count", report["failed_checks"])
        self.assertFalse(report["promotion_allowed"])

    def test_calibration_metric_is_bounded(self):
        ece = expected_calibration_error(
            [0.0, 0.25, 0.75, 1.0],
            [0, 0, 1, 1],
        )
        self.assertGreaterEqual(ece, 0.0)
        self.assertLessEqual(ece, 1.0)


if __name__ == "__main__":
    unittest.main()
