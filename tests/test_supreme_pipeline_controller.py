import unittest

from factory.supreme_pipeline_controller import (
    STAGES,
    evaluate_batch,
    evaluate_record,
    lexical_similarity,
    normalize_text,
    stable_fingerprint,
)

class SupremePipelineControllerTests(unittest.TestCase):
    def test_normalization_is_deterministic(self):
        self.assertEqual(normalize_text("Hello, WORLD!"), "hello world")

    def test_similarity_is_bounded(self):
        score = lexical_similarity("alpha beta", "alpha beta")
        self.assertEqual(score, 1.0)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_fingerprint_is_stable(self):
        self.assertEqual(stable_fingerprint({"b": 2, "a": 1}), stable_fingerprint({"a": 1, "b": 2}))

    def test_unverified_record_cannot_publish(self):
        record = {
            "artifact_id": "A1",
            "text": "evidence-backed claim",
            "source": "https://example.invalid/source",
            "confidence": 0.9,
            "verification_status": "UNVERIFIED",
        }
        stages = evaluate_record(record)
        self.assertIn("INDEPENDENT_VERIFY", [x.stage for x in stages])
        self.assertFalse(stages[-1].ok)

    def test_verified_record_can_pass_prerequisites(self):
        record = {
            "artifact_id": "A1",
            "text": "evidence-backed claim",
            "source": "https://example.invalid/source",
            "confidence": 0.9,
            "verification_status": "VERIFIED",
        }
        stages = evaluate_record(record)
        self.assertTrue(all(x.ok for x in stages))

    def test_batch_exposes_duplicate_and_stage_rates(self):
        record = {
            "artifact_id": "A1",
            "text": "evidence-backed claim",
            "source": "https://example.invalid/source",
            "confidence": 0.9,
            "verification_status": "VERIFIED",
        }
        result = evaluate_batch([record, dict(record)])
        self.assertEqual(result["duplicate_record_count"], 1)
        self.assertEqual(set(result["stage_pass_rates"]), set(STAGES))
        self.assertFalse(result["truth_claim"])

if __name__ == "__main__":
    unittest.main()
