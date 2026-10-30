import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))

import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from queue import QueueStore


class QueueClaimTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "automission.db"
        self.store = QueueStore(self.db)
        self.item = {
            "id": "op-1",
            "source": "test",
            "channel": "employment",
            "title": "Test opportunity",
            "description": "queue test",
            "url": "https://example.test/op-1",
            "action": "review",
            "status": "DISCOVERED",
        }

    def tearDown(self):
        self.tmp.cleanup()

    def test_claim_is_single_use_for_concurrent_workers(self):
        self.store.upsert_opportunity(self.item)
        first = self.store.claim(self.item)
        second = QueueStore(self.db).claim(self.item)

        self.assertTrue(first)
        self.assertFalse(second)

        with sqlite3.connect(self.db) as db:
            self.assertEqual(
                db.execute("select count(*) from execution_keys").fetchone()[0],
                1,
            )

    def test_stale_processing_recovers_and_can_be_claimed_again(self):
        self.store.upsert_opportunity(self.item)
        self.assertTrue(self.store.claim(self.item))

        stale = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        with sqlite3.connect(self.db) as db:
            db.execute(
                "update opportunities set updated_at=? where id=?",
                (stale, self.item["id"]),
            )

        self.assertEqual(self.store.recover_stale_processing(max_age_seconds=60), 1)
        self.assertEqual(self.store.pending()[0]["status"], "QUEUED")
        self.assertTrue(self.store.claim(self.item))

        key = self.store.idempotency_key(self.item)
        with sqlite3.connect(self.db) as db:
            row = db.execute(
                "select idempotency_key, status from execution_keys where idempotency_key=?",
                (key,),
            ).fetchone()
        self.assertEqual(row, (key, "PROCESSING"))

    def test_retry_after_failure_reuses_same_idempotency_record(self):
        self.store.upsert_opportunity(self.item)
        self.assertTrue(self.store.claim(self.item))
        self.store.mark_idempotency(self.item, "FAILED")
        self.store.release_for_retry(self.item["id"])

        self.assertTrue(self.store.claim(self.item))

        with sqlite3.connect(self.db) as db:
            count, status = db.execute(
                "select count(*), max(status) from execution_keys"
            ).fetchone()
        self.assertEqual(count, 1)
        self.assertEqual(status, "PROCESSING")


if __name__ == "__main__":
    unittest.main()
