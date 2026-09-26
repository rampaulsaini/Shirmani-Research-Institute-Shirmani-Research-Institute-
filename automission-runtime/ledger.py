import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def record_verified_income(db_path: Path, opportunity_id, amount, currency, evidence_url, notes=""):
    if amount is None or float(amount) <= 0:
        raise ValueError("verified income must be positive")
    if not currency or not str(currency).strip():
        raise ValueError("income currency is required")
    if not evidence_url or not str(evidence_url).strip():
        raise ValueError("income evidence URL is required")
    with sqlite3.connect(db_path) as db:
        db.execute("""INSERT INTO outcomes
            (id, opportunity_id, status, verified_income, currency, evidence_url, notes, recorded_at)
            VALUES (lower(hex(randomblob(16))), ?, 'VERIFIED_INCOME', ?, ?, ?, ?, ?)""",
            (opportunity_id, float(amount), str(currency).strip().upper(),
             str(evidence_url).strip(), notes, utc_now()))
