import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))

import sqlite3
import tempfile
import unittest
from pathlib import Path

from execution import run
from outcomes import record
from ledger import record_verified_income
from learning import capture_revenue_intelligence, prioritize_score


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
        result = run({"id": "op-1", "channel": "employment", "action": "apply"})
        self.assertEqual(result["status"], "APPROVAL_REQUIRED")
        self.assertEqual(result["action"], "apply")

    def test_unconfigured_adapter_is_planned_not_executed(self):
        result = run({"id": "op-2", "channel": "freelancing", "action": "review"})
        self.assertEqual(result["status"], "PLANNED")
        self.assertEqual(result["reason"], "adapter_not_configured")

    def test_income_without_evidence_is_rejected(self):
        result = record(
            self.db, "op-3",
            {"status": "EXECUTED", "verified_income": 100, "currency": "INR"},
        )
        self.assertEqual(result, "REJECTED_NO_INCOME_EVIDENCE")
        with sqlite3.connect(self.db) as db:
            row = db.execute(
                "select status, verified_income from outcomes where opportunity_id=?",
                ("op-3",),
            ).fetchone()
        self.assertEqual(row, ("REJECTED_NO_INCOME_EVIDENCE", 0.0))

    def test_ledger_rejects_missing_evidence_or_currency(self):
        with self.assertRaises(ValueError):
            record_verified_income(self.db, "op-ledger", 100, "INR", "")
        with self.assertRaises(ValueError):
            record_verified_income(self.db, "op-ledger-2", 100, "", "https://example.test/evidence")

    def test_revenue_intelligence_ignores_unverified_or_currencyless_income(self):
        record(self.db, "op-unverified", {
            "status": "EXECUTED", "verified_income": 500, "currency": "INR",
        })
        record(self.db, "op-currencyless", {
            "status": "EXECUTED", "verified_income": 700,
            "evidence_url": "https://example.test/currencyless",
        })
        revenue = capture_revenue_intelligence(self.db)
        self.assertEqual(revenue["verified_income_by_currency"], {})
        self.assertEqual(revenue["verified_outcomes"], 0)

    def test_revenue_intelligence_aggregates_by_channel_and_currency(self):
        with sqlite3.connect(self.db) as db:
            db.execute("""CREATE TABLE opportunities (
                id TEXT PRIMARY KEY, channel TEXT NOT NULL
            )""")
            db.executemany(
                "INSERT INTO opportunities(id, channel) VALUES(?, ?)",
                [("op-a", "freelancing"), ("op-b", "freelancing"),
                 ("op-c", "freelancing")],
            )
        record(self.db, "op-a", {
            "status": "EXECUTED", "verified_income": 200, "currency": "INR",
            "evidence_url": "https://example.test/a",
        })
        record(self.db, "op-b", {
            "status": "EXECUTED", "verified_income": 300, "currency": "INR",
            "evidence_url": "https://example.test/b",
        })
        record(self.db, "op-c", {
            "status": "EXECUTED", "verified_income": 50, "currency": "USD",
            "evidence_url": "https://example.test/c",
        })
        revenue = capture_revenue_intelligence(self.db)
        self.assertEqual(revenue["verified_income_by_currency"], {"INR": 500.0, "USD": 50.0})
        self.assertEqual(revenue["verified_outcomes"], 3)
        self.assertEqual(
            revenue["channels"]["freelancing"]["INR"]["verified_income"], 500.0
        )
        self.assertEqual(
            revenue["channels"]["freelancing"]["USD"]["verified_income"], 50.0
        )

    def test_learning_migrates_legacy_channel_performance_schema(self):
        with sqlite3.connect(self.db) as db:
            db.execute("""CREATE TABLE channel_performance (
                channel TEXT PRIMARY KEY,
                verified_income REAL NOT NULL DEFAULT 0,
                verified_outcomes INTEGER NOT NULL DEFAULT 0,
                evidence_count INTEGER NOT NULL DEFAULT 0,
                last_verified_at TEXT
            )""")
        revenue = capture_revenue_intelligence(self.db)
        self.assertEqual(revenue["verified_income_by_currency"], {})
        with sqlite3.connect(self.db) as db:
            columns = {row[1] for row in db.execute("PRAGMA table_info(channel_performance)")}
            self.assertIn("currency", columns)
            self.assertEqual(
                db.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='channel_performance_legacy'"
                ).fetchone()[0],
                "channel_performance_legacy",
            )

    def test_prioritization_requires_matching_currency_history(self):
        performance = {
            "channels": {
                "freelancing": {
                    "INR": {"verified_income": 500, "verified_outcomes": 2}
                }
            }
        }
        self.assertGreater(prioritize_score(10, "freelancing", performance, "INR"), 10)
        self.assertEqual(prioritize_score(10, "freelancing", performance, "USD"), 10)
        self.assertEqual(prioritize_score(10, "freelancing", performance), 10)

    def test_verified_income_requires_positive_amount_and_evidence(self):
        result = record(
            self.db, "op-4",
            {
                "status": "EXECUTED", "verified_income": 250, "currency": "INR",
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
