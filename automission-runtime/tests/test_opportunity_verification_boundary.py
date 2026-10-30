import sys
import unittest
from pathlib import Path

RUNTIME_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNTIME_ROOT))

from agents import prepare, score


class OpportunityVerificationBoundaryTests(unittest.TestCase):
    def test_urls_only_create_review_candidate_not_verified_record(self):
        item = {
            "title": "Freelance writing project",
            "description": "Freelance content writing",
            "channel": "freelancing",
            "url": "https://example.com/opportunity",
            "evidence_url": "https://example.com/source",
        }

        result = prepare(item)

        self.assertIsNotNone(result)
        self.assertEqual(result["status"], "REVIEW_REQUIRED")
        self.assertEqual(result["evidence_status"], "PRESENT_UNVERIFIED")
        self.assertNotEqual(result["status"], "VERIFIED")

    def test_missing_evidence_url_is_not_accepted_as_review_ready(self):
        item = {
            "title": "Freelance writing project",
            "channel": "freelancing",
            "url": "https://example.com/opportunity",
        }
        self.assertIsNone(prepare(item))

    def test_score_is_triage_only_and_does_not_change_verification_state(self):
        item = {
            "title": "Freelance content writing project",
            "channel": "freelancing",
            "url": "https://example.com/opportunity",
            "evidence_url": "https://example.com/source",
            "score": 0,
        }
        result = prepare(item)
        self.assertGreater(result["score"], 0)
        self.assertEqual(result["status"], "REVIEW_REQUIRED")

    def test_unknown_channel_is_rejected(self):
        self.assertIsNone(prepare({
            "title": "Unknown",
            "channel": "unknown",
            "url": "https://example.com/opportunity",
            "evidence_url": "https://example.com/source",
        }))


if __name__ == "__main__":
    unittest.main()
