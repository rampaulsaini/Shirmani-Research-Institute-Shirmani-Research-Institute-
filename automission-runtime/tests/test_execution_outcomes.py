import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))

import sqlite3
import tempfile
import unittest
from pathlib import Path

from execution import run
from outcomes import record


class ExecutionOutcomeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "automission.db"
        with sqlite3.connect(self.db) as db:
            db.execute("""CREATE TABLE outcomes (
                id TEXT PRIMARY KEY, opportunity_id TEXT NOT NULL,
                status TEXT NOT NULL, verified_income REAL DEFAULT 0,
                currency TEXT, evidence_url TEXT, notes TEXT,
                recorded_at TEXT NOT NULL
            )""")

    def tearDown(self):
        self.tmp.cleanup()

    def test_irreversible_actions_stop_for_human_approval(self):
        result = run({
            "id": "op-1",
            "channel": "employment",
            "action": "apply",
        })
        self.assertEqual(result["status"], "APPROVAL_REQUIRED")
        self.assertEqual(result["action"], "apply")

    def test_unconfigured_adapter_is_planned_not_executed(self):
        result = run({
            "id": "op-2",
            "channel": "freelancing",
            "action": "review",
        })
        self.assertEqual(result["status"], "PLANNED")
        self.assertEqual(result["reason"], "adapter_not_configured")

    def test_income_without_evidence_is_rejected(self):
        result = record(
            self.db,
            "op-3",
            {"status": "EXECUTED", "verified_income": 100, "currency": "INR"},
        )
        self.assertEqual(result, "REJECTED_NO_INCOME_EVIDENCE")

        with sqlite3.connect(self.db) as db:
            row = db.execute(
                "select status, verified_income from outcomes where opportunity_id=?",
                ("op-3",),
            ).fetchone()
        self.assertEqual(row, ("REJECTED_NO_INCOME_EVIDENCE", 0.0))

    def test_verified_income_requires_positive_amount_and_evidence(self):
        result = record(
            self.db,
            "op-4",
            {
                "status": "EXECUTED",
                "verified_income": 250,
                "currency": "INR",
                "evidence_url": "https://example.test/payment/4",
            },
        )
        self.assertEqual(result, "EXECUTED")

        with sqlite3.connect(self.db) as db:
            row = db.execute(
                "select verified_income, currency, evidence_url from outcomes where opportunity_id=?",
                ("op-4",),
            ).fetchone()
        self.assertEqual(row, (250.0, "INR", "https://example.test/payment/4"))


if __name__ == "__main__":
    unittest.main()
