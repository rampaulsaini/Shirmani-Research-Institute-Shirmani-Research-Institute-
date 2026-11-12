import unittest
from src.supreme_nlp.core import Signal, interpret_signal, audit_record, normalize_text


class SupremeNLPTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_text("  hello\nworld  "), "hello world")

    def test_conservative_interpretation(self):
        result = interpret_signal(
            Signal("fixture", "bioelectric", {"delta": 0.1}, provenance="test")
        )
        self.assertEqual(result.status, "hypothesis")
        self.assertGreaterEqual(result.confidence, 0.0)
        self.assertLessEqual(result.confidence, 1.0)
        self.assertIn("does not establish subjective experience", result.statement)

    def test_fingerprint_is_stable(self):
        signal = Signal("fixture", "vibration", 42.0, provenance="test")
        a = audit_record(signal, interpret_signal(signal))
        b = audit_record(signal, interpret_signal(signal))
        self.assertEqual(a["fingerprint"], b["fingerprint"])


if __name__ == "__main__":
    unittest.main()
