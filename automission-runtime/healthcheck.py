"""Container healthcheck: fail when the worker stops refreshing its durable heartbeat."""
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

state_dir = Path(os.getenv("AUTOMISSION_STATE_DIR", "/app/automission-runtime/state"))
db_path = state_dir / "automission.db"
max_age = int(os.getenv("AUTOMISSION_HEARTBEAT_MAX_AGE_SECONDS", "900"))

try:
    with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=3) as db:
        row = db.execute(
            "SELECT ts, status FROM heartbeats ORDER BY id DESC LIMIT 1"
        ).fetchone()
    if not row or row[1] != "HEARTBEAT_OK":
        raise RuntimeError("no successful heartbeat")
    timestamp = datetime.fromisoformat(row[0].replace("Z", "+00:00"))
    age = (datetime.now(timezone.utc) - timestamp).total_seconds()
    if age < -60 or age > max_age:
        raise RuntimeError(f"heartbeat stale or clock-skewed: age={age:.0f}s")
except Exception as exc:
    print(f"AUTOMISSION_UNHEALTHY: {exc}", file=sys.stderr)
    raise SystemExit(1)

print(f"AUTOMISSION_HEALTHY: heartbeat_age_seconds={age:.0f}")
