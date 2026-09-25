import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def capture_cycle_features(db_path: Path, accepted, routed, approval_required):
    features = {
        "accepted": int(accepted),
        "routed": int(routed),
        "approval_required": int(approval_required),
        "captured_at": utc_now(),
    }
    with sqlite3.connect(db_path) as db:
        db.execute("""CREATE TABLE IF NOT EXISTS learning_features (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            captured_at TEXT NOT NULL, features TEXT NOT NULL
        )""")
        db.execute("INSERT INTO learning_features(captured_at,features) VALUES(?,?)",
                   (features["captured_at"], json.dumps(features, sort_keys=True)))
    return features
