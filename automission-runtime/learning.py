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
        channel TEXT PRIMARY KEY,
        verified_income REAL NOT NULL DEFAULT 0,
        verified_outcomes INTEGER NOT NULL DEFAULT 0,
        evidence_count INTEGER NOT NULL DEFAULT 0,
        last_verified_at TEXT
    )""")


def _verified_outcome_rows(db):
    return db.execute(
        """SELECT o.opportunity_id, o.verified_income, o.currency, o.evidence_url,
                  o.recorded_at, COALESCE(p.channel, 'unknown')
           FROM outcomes o
           LEFT JOIN opportunities p ON p.id = o.opportunity_id
           WHERE o.verified_income > 0 AND o.evidence_url IS NOT NULL
             AND TRIM(o.evidence_url) <> ''"""
    ).fetchall()


def capture_revenue_intelligence(db_path: Path):
    """Aggregate only evidence-backed positive income into the learning signal."""
    with sqlite3.connect(db_path) as db:
        _ensure_tables(db)
        rows = _verified_outcome_rows(db)
        total_income = sum(float(row[1]) for row in rows)
        verified_outcomes = len(rows)
        channels = {}

        for _, amount, _, evidence_url, recorded_at, channel in rows:
            channel = channel or "unknown"
            bucket = channels.setdefault(
                channel,
                {"verified_income": 0.0, "verified_outcomes": 0, "evidence_count": 0,
                 "last_verified_at": None},
            )
            bucket["verified_income"] += float(amount)
            bucket["verified_outcomes"] += 1
            bucket["evidence_count"] += 1
            if bucket["last_verified_at"] is None or recorded_at > bucket["last_verified_at"]:
                bucket["last_verified_at"] = recorded_at

        db.execute("DELETE FROM channel_performance")
        for channel, bucket in channels.items():
            db.execute(
                """INSERT INTO channel_performance
                   (channel, verified_income, verified_outcomes, evidence_count, last_verified_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (channel, bucket["verified_income"], bucket["verified_outcomes"],
                 bucket["evidence_count"], bucket["last_verified_at"]),
            )

        return {
            "verified_income": total_income,
            "verified_outcomes": verified_outcomes,
            "evidence_backed": verified_outcomes,
            "channels": channels,
        }


def prioritize_score(base_score, channel, performance):
    """Return a deterministic score boost from verified income only."""
    score = float(base_score or 0)
    bucket = performance.get("channels", {}).get(channel, {})
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
        "verified_income": revenue["verified_income"],
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
