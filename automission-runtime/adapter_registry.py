import hashlib
import json
import sqlite3
from datetime import datetime, timezone


STATES = ("DISCOVERED", "CONFIGURED", "HEALTH_CHECKED", "AUTHORIZED", "READY", "DISABLED")


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def adapter_key(channel, action):
    return hashlib.sha256(f"{channel}|{action}".encode("utf-8")).hexdigest()


class AdapterRegistry:
    """Persistent capability registry; registration never grants external authorization."""

    def __init__(self, db_path):
        self.db_path = str(db_path)
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS adapters (
                adapter_key TEXT PRIMARY KEY,
                channel TEXT NOT NULL,
                action TEXT NOT NULL,
                state TEXT NOT NULL,
                capabilities_json TEXT NOT NULL,
                authorization_required INTEGER NOT NULL DEFAULT 1,
                health_json TEXT,
                updated_at TEXT NOT NULL
            )""")

    def register(self, channel, action, capabilities=None):
        key = adapter_key(channel, action)
        capabilities = capabilities or []
        with self._connect() as db:
            db.execute(
                """INSERT INTO adapters
                   (adapter_key, channel, action, state, capabilities_json,
                    authorization_required, updated_at)
                   VALUES (?, ?, ?, 'DISCOVERED', ?, 1, ?)
                   ON CONFLICT(adapter_key) DO UPDATE SET
                     capabilities_json=excluded.capabilities_json,
                     updated_at=excluded.updated_at""",
                (key, channel, action, json.dumps(sorted(set(capabilities))), utc_now()),
            )
        return key

    def set_state(self, key, state, health=None):
        if state not in STATES:
            raise ValueError("invalid_adapter_state")
        with self._connect() as db:
            row = db.execute(
                "SELECT authorization_required FROM adapters WHERE adapter_key=?", (key,)
            ).fetchone()
            if not row:
                raise KeyError("unknown_adapter")
            if state in {"AUTHORIZED", "READY"} and row[0] != 1:
                raise ValueError("authorization_policy_corrupt")
            db.execute(
                "UPDATE adapters SET state=?, health_json=?, updated_at=? WHERE adapter_key=?",
                (state, json.dumps(health, sort_keys=True) if health is not None else None, utc_now(), key),
            )

    def can_execute(self, key):
        with self._connect() as db:
            row = db.execute(
                "SELECT state, authorization_required FROM adapters WHERE adapter_key=?", (key,)
            ).fetchone()
        return bool(row and row[0] == "READY" and row[1] == 1)

    def snapshot(self):
        with self._connect() as db:
            rows = db.execute(
                "SELECT state, COUNT(*) FROM adapters GROUP BY state ORDER BY state"
            ).fetchall()
        return {state: count for state, count in rows}
