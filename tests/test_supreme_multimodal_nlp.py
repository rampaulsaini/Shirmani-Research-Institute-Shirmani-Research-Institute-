import unittest

from agents.supreme_multimodal_nlp import analyze, build_record, explain_simple


class SupremeMultimodalNLPTests(unittest.TestCase):
    def test_no_quality_means_fail_closed(self):
        result = analyze([
            {"modality": "plant", "feature": "signal", "value": 1, "quality": 0}
        ])
        self.assertEqual(result["status"], "insufficient_quality")
        self.assertIsNone(result["interpretation"])

    def test_multimodal_record_is_deterministic(self):
        rows = [
            {"modality": "plant", "feature": "voltage", "value": 1.0,
             "quality": 1.0, "source": "sensor-a", "baseline": 0.9},
            {"modality": "audio", "feature": "vibration", "value": 1.1,
             "quality": 0.95, "source": "sensor-b", "baseline": 1.0},
            {"modality": "environment", "feature": "temperature", "value": 25,
             "quality": 0.9, "source": "sensor-c", "baseline": 24},
        ]
        a = analyze(rows, "इन संकेतों का सरल अर्थ बताओ")
        b = analyze(rows, "इन संकेतों का सरल अर्थ बताओ")
        self.assertEqual(a["fingerprint"], b["fingerprint"])
        self.assertGreaterEqual(a["features"]["confidence"], 0)
        self.assertLessEqual(a["features"]["confidence"], 1)
        self.assertEqual(a["features"]["modalities"], 3)

    def test_counter_evidence_is_explicit(self):
        result = analyze([
            {"modality": "plant", "feature": "signal", "value": 1,
             "quality": 1, "source": "one"},
            {"modality": "plant", "feature": "signal", "value": 2,
             "quality": 1, "source": "one"},
        ])
        self.assertTrue(result["counter_evidence"])

    def test_simple_language_preserves_boundary(self):
        result = analyze([
            {"modality": "plant", "feature": "signal", "value": 1,
             "quality": 1, "source": "sensor-a"},
            {"modality": "audio", "feature": "vibration", "value": 1,
             "quality": 1, "source": "sensor-b"},
        ])
        text = explain_simple(result)
        self.assertIn("प्रमाण", text)

    def test_record_governance_is_fail_closed(self):
        record = build_record([
            {"modality": "machine", "feature": "load", "value": 1,
             "quality": 1, "source": "test"}
        ])
        self.assertTrue(record["governance"]["fail_closed"])
        self.assertFalse(record["governance"]["subjective_experience_claim_allowed"])
        self.assertTrue(record["governance"]["independent_verification_required"])


if __name__ == "__main__":
    unittest.main()
