import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def _ensure_tables(db):
    db.execute("""CREATE TABLE IF NOT EXISTS learning_features (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        captured_at TEXT NOT NULL, features TEXT NOT NULL
    )""")
    columns = {row[1] for row in db.execute("PRAGMA table_info(channel_performance)")}
    if columns and "currency" not in columns:
        db.execute("ALTER TABLE channel_performance RENAME TO channel_performance_legacy")
        columns = set()
    if not columns:
        db.execute("""CREATE TABLE IF NOT EXISTS channel_performance (
            channel TEXT NOT NULL,
            currency TEXT NOT NULL,
            verified_income REAL NOT NULL DEFAULT 0,
            verified_outcomes INTEGER NOT NULL DEFAULT 0,
            evidence_count INTEGER NOT NULL DEFAULT 0,
            last_verified_at TEXT,
            PRIMARY KEY (channel, currency)
        )""")
    db.execute("""CREATE TABLE IF NOT EXISTS opportunities (
        id TEXT PRIMARY KEY,
        channel TEXT NOT NULL
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS outcomes (
        id TEXT PRIMARY KEY,
        opportunity_id TEXT NOT NULL,
        status TEXT NOT NULL,
        verified_income REAL DEFAULT 0,
        currency TEXT,
        evidence_url TEXT,
        notes TEXT,
        recorded_at TEXT NOT NULL
    )""")


def _verified_outcome_rows(db):
    return db.execute(
        """SELECT o.opportunity_id, o.verified_income, UPPER(TRIM(o.currency)),
                  o.evidence_url, o.recorded_at, COALESCE(p.channel, 'unknown')
           FROM outcomes o
           LEFT JOIN opportunities p ON p.id = o.opportunity_id
           WHERE o.verified_income > 0
             AND o.evidence_url IS NOT NULL
             AND TRIM(o.evidence_url) <> ''
             AND o.currency IS NOT NULL
             AND TRIM(o.currency) <> ''"""
    ).fetchall()


def capture_revenue_intelligence(db_path: Path):
    """Aggregate only evidence-backed positive income, separated by currency."""
    with sqlite3.connect(db_path) as db:
        _ensure_tables(db)
        rows = _verified_outcome_rows(db)
        channels = {}

        for _, amount, currency, evidence_url, recorded_at, channel in rows:
            channel = channel or "unknown"
            currency = currency or "UNKNOWN"
            bucket = channels.setdefault(channel, {}).setdefault(
                currency,
                {"verified_income": 0.0, "verified_outcomes": 0,
                 "evidence_count": 0, "last_verified_at": None},
            )
            bucket["verified_income"] += float(amount)
            bucket["verified_outcomes"] += 1
            bucket["evidence_count"] += 1
            if bucket["last_verified_at"] is None or recorded_at > bucket["last_verified_at"]:
                bucket["last_verified_at"] = recorded_at

        db.execute("DELETE FROM channel_performance")
        for channel, currencies in channels.items():
            for currency, bucket in currencies.items():
                db.execute(
                    """INSERT INTO channel_performance
                       (channel, currency, verified_income, verified_outcomes,
                        evidence_count, last_verified_at)
                       VALUES (?, ?, ?, ?, ?, ?)""",
                    (channel, currency, bucket["verified_income"],
                     bucket["verified_outcomes"], bucket["evidence_count"],
                     bucket["last_verified_at"]),
                )

        total_income_by_currency = {}
        for channel_data in channels.values():
            for currency, bucket in channel_data.items():
                total_income_by_currency[currency] = (
                    total_income_by_currency.get(currency, 0.0)
                    + bucket["verified_income"]
                )

        return {
            "verified_income_by_currency": total_income_by_currency,
            "verified_outcomes": len(rows),
            "evidence_backed": len(rows),
            "channels": channels,
        }


def prioritize_score(base_score, channel, performance, currency=None):
    score = float(base_score or 0)
    bucket = performance.get("channels", {}).get(channel, {})
    if not currency:
        return score
    bucket = bucket.get(str(currency).upper(), {})
    verified_income = float(bucket.get("verified_income", 0) or 0)
    verified_outcomes = int(bucket.get("verified_outcomes", 0) or 0)
    if verified_outcomes:
        return score + min(verified_income / verified_outcomes, 1000.0) * 0.01
    return score


def capture_cycle_features(db_path: Path, accepted, routed, approval_required):
    revenue = capture_revenue_intelligence(db_path)
    features = {
        "accepted": int(accepted),
        "routed": int(routed),
        "approval_required": int(approval_required),
        "verified_income_by_currency": revenue["verified_income_by_currency"],
        "verified_outcomes": revenue["verified_outcomes"],
        "evidence_backed": revenue["evidence_backed"],
        "channels": revenue["channels"],
        "captured_at": utc_now(),
    }
    with sqlite3.connect(db_path) as db:
        _ensure_tables(db)
        db.execute(
            "INSERT INTO learning_features(captured_at,features) VALUES(?,?)",
            (features["captured_at"], json.dumps(features, sort_keys=True)),
        )
    return features
