import unittest
from agents.supreme_nlp_engine import Signal, interpret


class SupremeNLPTests(unittest.TestCase):
    def test_empty_input_fails_closed(self):
        result = interpret([])
        self.assertEqual(result["status"], "insufficient_data")
        self.assertEqual(result["interpretation"]["confidence"], 0.0)

    def test_multimodal_output_is_bounded(self):
        result = interpret(
            [
                Signal("bioelectric", 1.8, 1.0, 1.0, "u", "a"),
                Signal("vibration", 1.5, 1.0, 1.0, "u", "b"),
                Signal("thermal", 0.8, 1.0, 1.0, "u", "c"),
            ],
            labelled_evaluation=True,
        )
        self.assertEqual(result["status"], "interpreted")
        self.assertGreaterEqual(result["interpretation"]["confidence"], 0.0)
        self.assertLessEqual(result["interpretation"]["confidence"], 1.0)
        self.assertEqual(result["features"]["modalities"], 3)
        self.assertIn(result["interpretation"]["evidence_grade"], {"A", "B", "C", "D"})
        self.assertIn("subjective", result["interpretation"]["statement"].lower())

    def test_invalid_scale_is_rejected(self):
        with self.assertRaises(ValueError):
            interpret([Signal("x", 1.0, 0.0, 0.0)])


if __name__ == "__main__":
    unittest.main()
