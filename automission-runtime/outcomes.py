import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def record(db_path: Path, opportunity_id, result):
    status = str(result.get("status", "UNKNOWN"))
    income = float(result.get("verified_income", 0) or 0)
    evidence = result.get("evidence_url")
    if income > 0 and not evidence:
        status = "REJECTED_NO_INCOME_EVIDENCE"
        income = 0
    with sqlite3.connect(db_path) as db:
        db.execute("""INSERT INTO outcomes
            (id, opportunity_id, status, verified_income, currency, evidence_url, notes, recorded_at)
            VALUES (lower(hex(randomblob(16))), ?, ?, ?, ?, ?, ?, ?)""",
            (opportunity_id, status, income, result.get("currency"),
             evidence, json.dumps(result, sort_keys=True), utc_now()))
    return status
