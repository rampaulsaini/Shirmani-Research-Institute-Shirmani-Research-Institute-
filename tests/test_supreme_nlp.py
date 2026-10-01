import math
import unittest

from factory.supreme_nlp import canonical_hash, independent_verify, interpret, observe


class SupremeNLPTests(unittest.TestCase):
    def test_canonical_hash_is_stable(self):
        self.assertEqual(canonical_hash({"b": 2, "a": 1}), canonical_hash({"a": 1, "b": 2}))

    def test_observation_has_traceable_evidence(self):
        obs = observe("test-001", "PLANT", "ELECTRICAL", {"signal": 1.0}, "relative-unit", "synthetic", {"test": True})
        self.assertEqual(len(obs.evidence_hash), 64)
        self.assertTrue(obs.context["test"])

    def test_interpretation_defaults_to_unverified(self):
        obs = observe("test-002", "DEVICE", "TEMPERATURE", {"celsius": 21.5}, "C", "synthetic")
        result = interpret(obs, "Measured temperature pattern detected.", ["environmental change may be present"], 0.5)
        self.assertEqual(result.verification_status, "UNVERIFIED")

    def test_non_finite_signals_are_rejected(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    observe("bad-signal", "PLANT", "ELECTRICAL", {"signal": value}, "unit", "synthetic")

    def test_invalid_confidence_is_rejected(self):
        obs = observe("test-003", "ANIMAL", "MOTION", {"velocity": 1.0}, "m/s", "synthetic")
        with self.assertRaises(ValueError):
            interpret(obs, "x", ["y"], 1.01)

    def test_verified_status_cannot_be_forged_at_generation(self):
        obs = observe("test-004", "PLANT", "ELECTRICAL", {"signal": 1.0}, "u", "synthetic")
        with self.assertRaises(ValueError):
            interpret(obs, "pattern", ["hypothesis"], 0.8, "validated", verification_status="INDEPENDENTLY_VERIFIED")

    def test_independent_verification_requires_two_distinct_passes(self):
        obs = observe("test-005", "PLANT", "ELECTRICAL", {"signal": 1.0}, "u", "synthetic")
        result = interpret(obs, "validated pattern", ["hypothesis"], 0.8, "validated")
        one = independent_verify(result, [{"verifier_id": "A", "observation_hash": obs.evidence_hash, "decision": "PASS"}])
        self.assertEqual(one["status"], "UNVERIFIED")
        two = independent_verify(result, [
            {"verifier_id": "A", "observation_hash": obs.evidence_hash, "decision": "PASS"},
            {"verifier_id": "B", "observation_hash": obs.evidence_hash, "decision": "PASS"},
        ])
        self.assertEqual(two["status"], "INDEPENDENTLY_VERIFIED")
        self.assertEqual(two["verifier_count"], 2)

    def test_wrong_observation_hash_cannot_verify(self):
        obs = observe("test-006", "DEVICE", "TEMPERATURE", {"celsius": 21.5}, "C", "synthetic")
        result = interpret(obs, "validated pattern", ["hypothesis"], 0.8, "validated")
        check = independent_verify(result, [
            {"verifier_id": "A", "observation_hash": "0" * 64, "decision": "PASS"},
            {"verifier_id": "B", "observation_hash": obs.evidence_hash, "decision": "PASS"},
        ])
        self.assertEqual(check["status"], "UNVERIFIED")

    def test_non_pass_attestation_cannot_verify(self):
        obs = observe("test-007", "PLANT", "ELECTRICAL", {"signal": 1.0}, "u", "synthetic")
        result = interpret(obs, "validated pattern", ["hypothesis"], 0.8, "validated")
        check = independent_verify(result, [
            {"verifier_id": "A", "observation_hash": obs.evidence_hash, "decision": "FAIL"},
            {"verifier_id": "B", "observation_hash": obs.evidence_hash, "decision": "PASS"},
        ])
        self.assertEqual(check["status"], "UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
