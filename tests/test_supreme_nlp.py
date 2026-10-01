import math
import unittest

from factory.supreme_nlp import canonical_hash, interpret, observe


class SupremeNLPTests(unittest.TestCase):
    def test_canonical_hash_is_stable(self):
        self.assertEqual(
            canonical_hash({"b": 2, "a": 1}),
            canonical_hash({"a": 1, "b": 2}),
        )

    def test_observation_has_traceable_evidence(self):
        obs = observe(
            "test-001", "PLANT", "ELECTRICAL",
            {"signal": 1.0}, "relative-unit", "synthetic",
            {"test": True},
        )
        self.assertEqual(len(obs.evidence_hash), 64)
        self.assertTrue(obs.evidence_hash.isalnum())
        self.assertTrue(obs.context["test"])

    def test_interpretation_defaults_to_unverified(self):
        obs = observe(
            "test-002", "DEVICE", "TEMPERATURE",
            {"celsius": 21.5}, "C", "synthetic",
        )
        result = interpret(
            obs,
            "Measured temperature pattern detected.",
            ["environmental change may be present"],
            0.5,
        )
        self.assertEqual(result.verification_status, "UNVERIFIED")

    def test_non_finite_signals_are_rejected(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    observe(
                        "bad-signal", "PLANT", "ELECTRICAL",
                        {"signal": value}, "unit", "synthetic",
                    )

    def test_invalid_confidence_is_rejected(self):
        obs = observe(
            "test-003", "ANIMAL", "MOTION",
            {"velocity": 1.0}, "m/s", "synthetic",
        )
        with self.assertRaises(ValueError):
            interpret(obs, "x", ["y"], 1.01)


if __name__ == "__main__":
    unittest.main()
