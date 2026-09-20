import json
import tempfile
import unittest
from datetime import datetime, timezone, timedelta
from pathlib import Path

from factory.queue_worker import claim, enqueue, finish


class QueueWorkerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "queue.jsonl"

    def tearDown(self):
        self.tmp.cleanup()

    def rows(self):
        return [
            json.loads(line)
            for line in self.path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def test_enqueue_is_idempotent(self):
        job = {"job_id": "verse-000001", "kind": "verse", "number": 1}
        enqueue(self.path, [job, job])
        enqueue(self.path, [job])
        self.assertEqual(len(self.rows()), 1)

    def test_claim_assigns_lease_token(self):
        enqueue(self.path, [{"job_id": "verse-000001"}])
        claimed = claim(self.path, limit=1, lease_seconds=60)
        self.assertEqual(len(claimed), 1)
        self.assertEqual(claimed[0]["status"], "running")
        self.assertTrue(claimed[0]["lease_token"])
        self.assertTrue(claimed[0]["lease_expires_at"])

    def test_running_job_requires_matching_lease_token(self):
        enqueue(self.path, [{"job_id": "verse-000001"}])
        claimed = claim(self.path, limit=1)
        self.assertFalse(finish(self.path, "verse-000001", True))
        self.assertTrue(
            finish(
                self.path,
                "verse-000001",
                True,
                lease_token=claimed[0]["lease_token"],
            )
        )
        self.assertEqual(self.rows()[0]["status"], "succeeded")

    def test_retry_then_dead_letter(self):
        enqueue(self.path, [{"job_id": "verse-000001"}])
        for attempt in range(2):
            claimed = claim(self.path, limit=1)
            self.assertEqual(len(claimed), 1)
            self.assertTrue(
                finish(
                    self.path,
                    "verse-000001",
                    False,
                    error=f"error-{attempt}",
                    lease_token=claimed[0]["lease_token"],
                )
            )
            row = self.rows()[0]
            self.assertEqual(row["status"], "retrying")
            row["retry_at"] = datetime.now(timezone.utc).isoformat()
            self.path.write_text(
                json.dumps(row, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

        claimed = claim(self.path, limit=1)
        self.assertEqual(len(claimed), 1)
        self.assertTrue(
            finish(
                self.path,
                "verse-000001",
                False,
                error="final-error",
                lease_token=claimed[0]["lease_token"],
            )
        )
        row = self.rows()[0]
        self.assertEqual(row["status"], "failed")
        self.assertTrue(row["dead_letter"])
        self.assertEqual(row["attempts"], 3)

    def test_expired_lease_is_recovered(self):
        enqueue(self.path, [{"job_id": "verse-000001"}])
        claimed = claim(self.path, limit=1, lease_seconds=1)
        row = self.rows()[0]
        row["lease_expires_at"] = (
            datetime.now(timezone.utc) - timedelta(seconds=1)
        ).isoformat()
        self.path.write_text(
            json.dumps(row, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        recovered = claim(self.path, limit=1)
        self.assertEqual(len(recovered), 1)
        self.assertNotEqual(
            recovered[0]["lease_token"], claimed[0]["lease_token"]
        )
        self.assertEqual(recovered[0]["status"], "running")


if __name__ == "__main__":
    unittest.main()
