import os
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

DB = Path(os.getenv("AUTOMISSION_DB", "/app/automission-runtime/state/automission.db"))
MAX_AGE = int(os.getenv("AUTOMISSION_MAX_HEARTBEAT_AGE_SECONDS", "900"))

def now():
    return datetime.now(timezone.utc)

def check():
    if not DB.exists():
        return False, "database_missing"
    with sqlite3.connect(DB) as db:
        row = db.execute("select ts,status from heartbeats order by id desc limit 1").fetchone()
    if not row or row[1] != "HEARTBEAT_OK":
        return False, "heartbeat_missing_or_not_ok"
    ts = datetime.fromisoformat(row[0])
    age = (now() - ts).total_seconds()
    return age <= MAX_AGE, f"heartbeat_age_seconds={int(age)}"

if __name__ == "__main__":
    ok, reason = check()
    print(reason, flush=True)
    raise SystemExit(0 if ok else 1)
