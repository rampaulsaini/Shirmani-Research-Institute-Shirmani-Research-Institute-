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
    db.execute("""CREATE TABLE IF NOT EXISTS channel_performance (
        channel TEXT NOT NULL,
        currency TEXT NOT NULL,
        verified_income REAL NOT NULL DEFAULT 0,
        verified_outcomes INTEGER NOT NULL DEFAULT 0,
        evidence_count INTEGER NOT NULL DEFAULT 0,
        last_verified_at TEXT,
        PRIMARY KEY (channel, currency)
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
            bucket = channels.setdefault(channel, {})
            currency_bucket = bucket.setdefault(
                currency,
                {"verified_income": 0.0, "verified_outcomes": 0, "evidence_count": 0,
                 "last_verified_at": None},
            )
            currency_bucket["verified_income"] += float(amount)
            currency_bucket["verified_outcomes"] += 1
            currency_bucket["evidence_count"] += 1
            if (currency_bucket["last_verified_at"] is None
                    or recorded_at > currency_bucket["last_verified_at"]):
                currency_bucket["last_verified_at"] = recorded_at

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
        verified_outcomes = len(rows)
        for channel_data in channels.values():
            for currency, bucket in channel_data.items():
                total_income_by_currency[currency] = (
                    total_income_by_currency.get(currency, 0.0)
                    + bucket["verified_income"]
                )

        return {
            "verified_income_by_currency": total_income_by_currency,
            "verified_outcomes": verified_outcomes,
            "evidence_backed": verified_outcomes,
            "channels": channels,
        }


def prioritize_score(base_score, channel, performance, currency=None):
    """Return a deterministic score boost using only verified history in one currency."""
    score = float(base_score or 0)
    bucket = performance.get("channels", {}).get(channel, {})
    if currency:
        bucket = bucket.get(str(currency).upper(), {})
    else:
        return score

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
