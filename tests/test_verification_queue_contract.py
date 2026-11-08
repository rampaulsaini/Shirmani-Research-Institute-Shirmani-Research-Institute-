import json
import tempfile
import unittest
from pathlib import Path

from factory.verification_queue_qc import validate


class VerificationQueueContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.records_path = self.root / "records.json"
        self.queue_path = self.root / "queue.jsonl"
        self.source = {
            "schema_version": "1.1.0",
            "records": [
                {
                    "id": "IV-001",
                    "status": "EVIDENCE-SUPPORTED",
                    "source_status": "EVIDENCE-SUPPORTED",
                    "evidence": {"sources": ["https://example.org/source-a"]},
                },
                {
                    "id": "IV-002",
                    "status": "NOT_VERIFIED",
                    "source_status": "NOT_VERIFIED",
                    "evidence": {"sources": []},
                },
            ],
        }
        self.queue = [
            self.task("IV-001", ["https://example.org/source-a"], "EVIDENCE-SUPPORTED"),
            self.task("IV-002", [], "NOT_VERIFIED"),
        ]
        self.write()

    def tearDown(self):
        self.tmp.cleanup()

    @staticmethod
    def task(claim_id, source_ids, source_status):
        return {
            "task_id": f"{claim_id}-independent-review-v1",
            "claim_id": claim_id,
            "source_ids": source_ids,
            "source_status": source_status,
            "verification_questions": ["Can an independent reviewer reproduce this?"],
            "required_evidence": ["Independent source or reproducible test"],
            "status": "QUEUED",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "created_at": "2026-11-08T00:00:00+00:00",
            "generator": "factory/bootstrap_independent_verification_queue.py",
        }

    def write(self):
        self.records_path.write_text(json.dumps(self.source), encoding="utf-8")
        self.queue_path.write_text(
            "".join(json.dumps(row) + "\n" for row in self.queue),
            encoding="utf-8",
        )

    def test_valid_dedicated_queue_passes_without_claim_evidence_file(self):
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "PASS")
        self.assertEqual(report["records"], 2)
        self.assertEqual(report["queue_records"], 2)
        self.assertEqual(errors, [])

    def test_missing_authoritative_claim_blocks(self):
        self.queue.pop()
        self.write()
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "BLOCK")
        self.assertTrue(any(e.get("error") == "authoritative_claims_missing_from_queue" for e in errors))

    def test_duplicate_claim_blocks(self):
        self.queue[1] = self.task("IV-001", ["https://example.org/source-a"], "EVIDENCE-SUPPORTED")
        self.write()
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "BLOCK")
        self.assertTrue(any(e.get("error") == "duplicate_claim_id" for e in errors))

    def test_unearned_verified_status_blocks(self):
        self.queue[0]["verification_status"] = "VERIFIED"
        self.write()
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "BLOCK")
        self.assertTrue(any(e.get("error") == "verified_task_missing_independent_review_state" for e in errors))


    def test_human_reviewed_state_is_preserved(self):
        self.queue[0]["status"] = "REVIEWED"
        self.queue[0]["verification_status"] = "NOT_VERIFIED"
        self.queue[0]["independent"] = False
        self.write()
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "PASS")
        self.assertEqual(errors, [])

    def test_verified_state_requires_independent_review(self):
        self.queue[0]["status"] = "VERIFIED"
        self.queue[0]["verification_status"] = "VERIFIED"
        self.queue[0]["independent"] = False
        self.write()
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "BLOCK")
        self.assertTrue(any(e.get("error") == "verified_task_missing_independent_review_state" for e in errors))

    def test_verified_state_with_independent_review_flag_is_structurally_allowed(self):
        self.queue[0]["status"] = "REVIEWED"
        self.queue[0]["verification_status"] = "VERIFIED"
        self.queue[0]["independent"] = True
        self.write()
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "PASS")
        self.assertEqual(errors, [])

    def test_source_mismatch_blocks(self):
        self.queue[0]["source_ids"] = ["https://wrong.example/evidence"]
        self.write()
        report, errors = validate(self.records_path, self.queue_path)
        self.assertEqual(report["publication_gate"], "BLOCK")
        self.assertTrue(any(e.get("error") == "source_ids_do_not_match_authoritative_record" for e in errors))


if __name__ == "__main__":
    unittest.main()
