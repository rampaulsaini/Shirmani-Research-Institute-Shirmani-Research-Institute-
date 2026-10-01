import unittest

from factory.supreme_nlp_practitioner import (
    SCHEMA_VERSION,
    normalize_signals,
    practitioner_report,
)


class SupremeNlpPractitionerTests(unittest.TestCase):
    def test_schema_and_plain_language_are_deterministic(self):
        report = practitioner_report(
            "plant",
            [{"name": "soil_moisture", "value": 21, "unit": "%", "quality": 0.9}],
        )
        self.assertEqual(report["schema_version"], SCHEMA_VERSION)
        self.assertIn("soil moisture", report["plain_language_hi"].lower())
        self.assertEqual(report["observation_quality"], 0.9)
        self.assertEqual(report["observation_quality_label"], "high")
        self.assertEqual(report["signals"][0]["modality"], "other")
        self.assertEqual(report["nlp_modes"], ["Natural Language Processing", "Nispak Learning Programs"])

    def test_invalid_numbers_are_finite(self):
        signals = normalize_signals([{"name": "x", "value": "not-a-number"}])
        self.assertEqual(signals[0].value, 0.0)

    def test_consciousness_is_not_claimed(self):
        report = practitioner_report(
            "human",
            [{"name": "heart_rate", "value": 72, "unit": "bpm", "modality": "other"}],
        )
        boundary = report["interpretation"]["claim_boundary"]
        self.assertIn("do not", boundary)
        self.assertIn("consciousness", boundary)

    def test_baseline_change_is_explicit(self):
        report = practitioner_report(
            "environment",
            [{"name": "temperature", "value": 31, "unit": "C"}],
            baseline={"temperature": 28},
        )
        self.assertEqual(report["changes"][0]["direction"], "up")
        self.assertEqual(report["changes"][0]["delta"], 3.0)


if __name__ == "__main__":
    unittest.main()
