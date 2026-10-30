import hashlib
import json
import sqlite3
from datetime import datetime, timezone


STATUSES = (
    "DISCOVERED",
    "QUEUED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "APPROVAL_REQUIRED",
)


def utc_now():
    return datetime.now(timezone.utc).isoformat()


class AgentTaskLedger:
    """Persistent, idempotent task state for the master automission control plane."""

    def __init__(self, db_path):
        self.db_path = str(db_path)
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as db:
            db.execute(
                """CREATE TABLE IF NOT EXISTS agent_tasks (
                    task_key TEXT PRIMARY KEY,
                    task_id TEXT NOT NULL,
                    domain TEXT NOT NULL,
                    role TEXT NOT NULL,
                    action TEXT NOT NULL,
                    status TEXT NOT NULL,
                    input_hash TEXT,
                    output_hash TEXT,
                    evidence_url TEXT,
                    error TEXT,
                    created_at TEXT NOT NULL,
                    started_at TEXT,
                    finished_at TEXT
                )"""
            )

    @staticmethod
    def task_key(task_id, domain, action):
        raw = f"{task_id}|{domain}|{action}".encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    @staticmethod
    def _hash(value):
        if value is None:
            return None
        raw = value if isinstance(value, str) else json.dumps(value, sort_keys=True)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def record(self, task, input_payload=None):
        key = self.task_key(task.task_id, task.domain, task.action)
        with self._connect() as db:
            db.execute(
                """INSERT OR IGNORE INTO agent_tasks
                   (task_key, task_id, domain, role, action, status, input_hash, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    key, task.task_id, task.domain, task.role, task.action,
                    "DISCOVERED", self._hash(input_payload), utc_now(),
                ),
            )
        return key

    def set_status(self, task_key, status, output=None, evidence_url=None, error=None):
        if status not in STATUSES:
            raise ValueError("invalid_task_status")
        now = utc_now()
        started = now if status == "RUNNING" else None
        finished = now if status in {"COMPLETED", "FAILED", "APPROVAL_REQUIRED"} else None
        with self._connect() as db:
            row = db.execute(
                "SELECT task_key FROM agent_tasks WHERE task_key=?", (task_key,)
            ).fetchone()
            if not row:
                raise KeyError("unknown_task")
            db.execute(
                """UPDATE agent_tasks
                   SET status=?,
                       output_hash=COALESCE(?, output_hash),
                       evidence_url=COALESCE(?, evidence_url),
                       error=COALESCE(?, error),
                       started_at=COALESCE(?, started_at),
                       finished_at=COALESCE(?, finished_at)
                   WHERE task_key=?""",
                (
                    status, self._hash(output), evidence_url, error,
                    started, finished, task_key,
                ),
            )

    def snapshot(self):
        with self._connect() as db:
            rows = db.execute(
                """SELECT status, COUNT(*) FROM agent_tasks GROUP BY status ORDER BY status"""
            ).fetchall()
        return {status: count for status, count in rows}
