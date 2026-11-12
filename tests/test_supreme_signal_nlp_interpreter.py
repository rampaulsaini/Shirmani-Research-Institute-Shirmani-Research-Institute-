import unittest

from factory.supreme_signal_nlp_interpreter import (
    Signal,
    interpret,
    interpret_batch,
    normalize_signals,
)


class SupremeSignalNlpTests(unittest.TestCase):
    def test_empty_input_is_explicitly_unknown(self):
        result = interpret("plant-1", "plant", [])
        self.assertEqual(result.state, "unknown")
        self.assertEqual(result.confidence, 0.0)
        self.assertIn("No observable signal", result.plain_language)

    def test_normalization_clips_bounded_values(self):
        result = normalize_signals([
            {"name": "temperature", "value": 2.0, "quality": -1.0},
            {"name": "moisture", "value": -2.0, "quality": 2.0},
        ])
        self.assertEqual(result[0].value, 1.0)
        self.assertEqual(result[0].quality, 0.0)
        self.assertEqual(result[1].value, 0.0)
        self.assertEqual(result[1].quality, 1.0)

    def test_evidence_and_multiple_sources_raise_confidence(self):
        result = interpret(
            "tree-1",
            "plant",
            [
                Signal("leaf-response", 0.8, source="camera", quality=1.0, evidence_ids=("e1",)),
                Signal("moisture-stress", 0.7, source="sensor", quality=1.0, evidence_ids=("e2",)),
                Signal("growth-rate", 0.6, source="history", quality=1.0, evidence_ids=("e3",)),
            ],
        )
        self.assertEqual(result.state, "elevated")
        self.assertGreaterEqual(result.confidence, 0.9)
        self.assertLessEqual(result.uncertainty, 0.1)
        self.assertEqual(result.evidence_ids, ("e1", "e2", "e3"))

    def test_output_does_not_claim_literal_feeling(self):
        result = interpret(
            "machine-1",
            "machine",
            [{"name": "vibration", "value": 0.9, "source": "sensor"}],
        )
        self.assertEqual(result.consciousness_claim, "not_inferred")
        self.assertIn("not a proof of subjective feeling", result.plain_language)

    def test_batch_is_deterministic(self):
        record = {
            "entity_id": "environment-1",
            "entity_type": "environment",
            "signals": [
                {"name": "noise", "value": 0.2, "source": "meter", "evidence_ids": ["n1"]},
                {"name": "heat", "value": 0.3, "source": "meter", "evidence_ids": ["h1"]},
            ],
        }
        self.assertEqual(interpret_batch([record]), interpret_batch([record]))


if __name__ == "__main__":
    unittest.main()
