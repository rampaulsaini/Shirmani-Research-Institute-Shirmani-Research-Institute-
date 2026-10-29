import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))

import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import worker


class EndToEndLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.state = Path(self.tmp.name)
        self.db = self.state / "automission.db"

    def tearDown(self):
        self.tmp.cleanup()

    def test_unverified_opportunity_is_not_executed_before_review(self):
        item = {
            "id": "e2e-1",
            "source": "test-feed",
            "channel": "freelancing",
            "title": "Freelance project requiring review",
            "description": "contract project",
            "url": "https://example.test/project/1",
            "evidence_url": "https://example.test/evidence/1",
            "action": "review",
            "score": 80,
            "status": "DISCOVERED",
        }

        old_db, old_state = worker.DB, worker.STATE_DIR
        worker.DB, worker.STATE_DIR = self.db, self.state
        try:
            worker.init_db()
            with patch.object(worker, "discover", return_value=[item]), \
                 patch.object(worker, "health_all", return_value={"freelancing": "NOT_READY"}):
                worker.cycle()

            with sqlite3.connect(self.db) as db:
                heartbeat = db.execute(
                    "select status from heartbeats order by id desc limit 1"
                ).fetchone()
                outcome = db.execute(
                    "select status from outcomes where opportunity_id=? order by recorded_at desc limit 1",
                    ("e2e-1",),
                ).fetchone()
                learning = db.execute(
                    "select count(*) from learning_features"
                ).fetchone()[0]
                receipt = db.execute(
                    "select status from execution_receipts order by id desc limit 1"
                ).fetchone()

            self.assertEqual(heartbeat, ("HEARTBEAT_OK",))
            self.assertIsNone(outcome, "Unverified opportunity must not create a planned outcome")
            self.assertEqual(learning, 1)
            self.assertIsNone(receipt, "Unverified opportunity must not create an execution receipt")
        finally:
            worker.DB, worker.STATE_DIR = old_db, old_state


if __name__ == "__main__":
    unittest.main()
