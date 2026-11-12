import unittest

from factory.signal_nlp_translator import (
    SCHEMA_VERSION,
    SignalObservation,
    classify_signal,
    translate,
)


class SignalNlpTranslatorTests(unittest.TestCase):
    def test_schema_version_and_determinism(self):
        payload = {
            "source_id": "plant-1",
            "domain": "plant",
            "signal_type": "electrical",
            "window_seconds": 30,
            "baseline": 100,
            "value": 120,
            "trend": "rising",
            "quality": 0.9,
            "features": ["spike"],
        }
        self.assertEqual(SCHEMA_VERSION, "1.0")
        self.assertEqual(translate(payload), translate(payload))

    def test_output_does_not_claim_subjective_feeling(self):
        result = translate({
            "source_id": "s1",
            "domain": "plant",
            "signal_type": "electrical",
            "window_seconds": 10,
            "baseline": 100,
            "value": 160,
            "trend": "rising",
            "quality": 1.0,
        })
        self.assertIn("observable signal pattern", result["evidence_boundary"])
        self.assertNotIn("feels", result["simple_language"].lower())

    def test_low_quality_is_not_overinterpreted(self):
        result = classify_signal(SignalObservation(
            source_id="s2",
            domain="environment",
            signal_type="temperature",
            window_seconds=5,
            baseline=20,
            value=40,
            quality=0.2,
        ))
        self.assertEqual(result["claim_level"], "LOW_QUALITY")

    def test_invalid_signal_fails_closed(self):
        result = translate({
            "source_id": "",
            "signal_type": "x",
            "window_seconds": 0,
            "baseline": float("nan"),
            "value": 1,
            "quality": 2,
        })
        self.assertEqual(result["status"], "INVALID")
        self.assertTrue(result["errors"])


if __name__ == "__main__":
    unittest.main()
