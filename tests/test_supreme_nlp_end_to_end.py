"""End-to-end regression tests for the SHIRMANI Supreme NLP stack.

These tests intentionally verify evidence preservation, uncertainty, language
translation, multimodal fusion, calibration metrics, and fail-closed governance.
They do not claim subjective experience from signals.
"""
from __future__ import annotations

import unittest

from agents.supreme_nlp import build_record
from agents.supreme_nlp_multimodal import analyze, to_simple_language
from agents.supreme_nlp_practitioner import build_practitioner_record, detect_language
from agents.supreme_nlp_quality import (
    brier_score,
    evaluate,
    expected_calibration_error,
)


class SupremeNlpEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"modality": "electrical", "feature": "signal", "value": 1.00, "quality": 1, "source": "sensor-a"},
            {"modality": "audio", "feature": "signal", "value": 1.01, "quality": 1, "source": "sensor-b"},
            {"modality": "thermal", "feature": "signal", "value": 1.00, "quality": 1, "source": "sensor-c"},
            {"modality": "electrical", "feature": "signal", "value": 1.02, "quality": 1, "source": "sensor-a"},
            {"modality": "audio", "feature": "signal", "value": 1.00, "quality": 1, "source": "sensor-b"},
            {"modality": "thermal", "feature": "signal", "value": 1.01, "quality": 1, "source": "sensor-c"},
            {"modality": "electrical", "feature": "signal", "value": 1.00, "quality": 1, "source": "sensor-a"},
            {"modality": "audio", "feature": "signal", "value": 1.01, "quality": 1, "source": "sensor-b"},
            {"modality": "thermal", "feature": "signal", "value": 1.00, "quality": 1, "source": "sensor-c"},
            {"modality": "electrical", "feature": "signal", "value": 1.01, "quality": 1, "source": "sensor-a"},
        ]

    def test_multimodal_fusion_is_evidence_preserving(self):
        record = analyze(self.rows, request="वनस्पति संकेत की सरल व्याख्या", source_type="synthetic")
        self.assertEqual(record["status"], "CANDIDATE")
        self.assertEqual(record["evidence_class"], "INFERRED")
        self.assertEqual(record["metrics"]["modalities"], ["audio", "electrical", "thermal"])
        self.assertEqual(record["verification"]["status"], "UNVERIFIED")
        self.assertFalse(record["verification"]["promotion_allowed"])
        self.assertIn("subjective experience", " ".join(record["limitations"]).lower())
        self.assertEqual(len(record["provenance"]["fingerprint"]), 64)

    def test_conflict_causes_abstention(self):
        rows = [
            {"modality": "electrical", "feature": "signal", "value": -100, "quality": 1, "source": "a"},
            {"modality": "audio", "feature": "signal", "value": 100, "quality": 1, "source": "b"},
        ]
        record = analyze(rows)
        self.assertEqual(record["status"], "BLOCKED")
        self.assertEqual(record["uncertainty"]["reason"], "CONFLICTING_OBSERVATIONS")

    def test_practitioner_supports_hindi_punjabi_and_japanese(self):
        self.assertEqual(detect_language("यह एक परीक्षण है"), "hi")
        self.assertEqual(detect_language("ਇਹ ਇੱਕ ਟੈਸਟ ਹੈ"), "pa")
        self.assertEqual(detect_language("これはテストです"), "ja")
        record = build_practitioner_record(self.rows, "जीव संकेत को सरल भाषा में समझाइए")
        self.assertIn("computational", record["simple_language"])

    def test_quality_gate_never_promotes_unverified_data(self):
        record = build_record(self.rows, "e2e-quality")
        report = evaluate(record)
        self.assertTrue(report["governance"]["fail_closed"])
        self.assertFalse(report["promotion_allowed"])
        self.assertTrue(report["governance"]["accuracy_is_measured_not_declared"])

    def test_calibration_metrics_are_bounded(self):
        predictions = [0.05, 0.20, 0.80, 0.95]
        labels = [0, 0, 1, 1]
        ece = expected_calibration_error(predictions, labels)
        brier = brier_score(predictions, labels)
        self.assertGreaterEqual(ece, 0)
        self.assertLessEqual(ece, 1)
        self.assertGreaterEqual(brier, 0)
        self.assertLessEqual(brier, 1)

    def test_simple_language_has_explicit_epistemic_boundary(self):
        record = analyze(self.rows)
        text = to_simple_language(record)
        self.assertIn("प्रत्यक्ष भाव या चेतना का प्रमाण नहीं", text)


if __name__ == "__main__":
    unittest.main()
