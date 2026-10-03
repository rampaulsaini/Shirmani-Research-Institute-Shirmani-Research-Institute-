import unittest

from factory.supreme_ai_ml_nlp_engine import (
    SCHEMA_VERSION,
    _near_duplicate_pairs,
    evaluate,
    jaccard,
    lexical_profile,
    robust_anomaly_scores,
)


class SupremeAiMlNlpTests(unittest.TestCase):
    def test_schema_and_lexical_profile_are_deterministic(self):
        text = "Heart view truth is transparent and observable."
        self.assertEqual(lexical_profile(text), lexical_profile(text))
        self.assertEqual(SCHEMA_VERSION, "2.0")

    def test_jaccard_identical_text_is_one(self):
        self.assertEqual(jaccard("a b c d", "a b c d"), 1.0)

    def test_anomaly_detector_is_stable(self):
        values = [10, 10, 10, 10, 100]
        first = robust_anomaly_scores(values)
        second = robust_anomaly_scores(values)
        self.assertEqual(first, second)
        self.assertGreater(first[-1], first[0])

    def test_near_duplicate_search_is_bounded_and_deterministic(self):
        rows = [{"text": "a b c d e"}, {"text": "a b c d e"}, {"text": "x y z"}]
        self.assertEqual(_near_duplicate_pairs(rows), 1)

    def test_consensus_requires_observable_worker(self):
        rows = [{
            "id": "1",
            "text": "independent evidence method trace",
            "source_ids": ["s1"],
            "method_trace": "m1",
            "content_hash": "h",
        }]
        verification = {"fail_closed": True}
        good_worker = {"worker_observable": True}
        bad_worker = {"worker_observable": False}

        good = evaluate(rows, verification, good_worker)
        bad = evaluate(rows, verification, bad_worker)

        self.assertTrue(good["consensus_pass"])
        self.assertEqual(good["next_action"], "CONTINUE_AUTOMISSION")
        self.assertFalse(bad["consensus_pass"])
        self.assertEqual(bad["next_action"], "STOP_AND_REPAIR")


if __name__ == "__main__":
    unittest.main()
