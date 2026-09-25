import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

IRREVERSIBLE_ACTIONS = {"publish", "payment", "submit", "accept_contract"}

def utc_now():
    return datetime.now(timezone.utc).isoformat()

class PublishingRegistry:
    """Evidence-first registry for channel adapters.

    Adapters are intentionally declarative here: an external platform is not
    treated as connected until a configured adapter reports it explicitly.
    """

    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _init(self):
        with sqlite3.connect(self.db_path) as db:
            db.execute("""CREATE TABLE IF NOT EXISTS publishing_channels (
                channel TEXT PRIMARY KEY, adapter TEXT NOT NULL,
                enabled INTEGER NOT NULL DEFAULT 0,
                actions TEXT NOT NULL, status TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS publishing_plans (
                id TEXT PRIMARY KEY, product_id TEXT NOT NULL, channel TEXT NOT NULL,
                action TEXT NOT NULL, status TEXT NOT NULL, details TEXT NOT NULL,
                created_at TEXT NOT NULL
            )""")

    def register(self, channel, adapter, actions=(), enabled=False, status="PLANNED"):
        if not channel or not adapter:
            raise ValueError("channel and adapter are required")
        actions = sorted({str(x) for x in actions})
        with sqlite3.connect(self.db_path) as db:
            db.execute("""INSERT INTO publishing_channels
                (channel,adapter,enabled,actions,status,updated_at)
                VALUES(?,?,?,?,?,?)
                ON CONFLICT(channel) DO UPDATE SET
                adapter=excluded.adapter, enabled=excluded.enabled,
                actions=excluded.actions, status=excluded.status,
                updated_at=excluded.updated_at""",
                (channel, adapter, int(bool(enabled)), json.dumps(actions),
                 status, utc_now()))

    def channels(self):
        with sqlite3.connect(self.db_path) as db:
            rows = db.execute("""SELECT channel,adapter,enabled,actions,status,updated_at
                                 FROM publishing_channels ORDER BY channel""").fetchall()
        return [
            {"channel": r[0], "adapter": r[1], "enabled": bool(r[2]),
             "actions": json.loads(r[3]), "status": r[4], "updated_at": r[5]}
            for r in rows
        ]

    def plan(self, product_id, channel, action="publish", details=None):
        if action not in IRREVERSIBLE_ACTIONS:
            raise ValueError("unsupported publication action")
        with sqlite3.connect(self.db_path) as db:
            row = db.execute(
                "SELECT enabled,actions,status FROM publishing_channels WHERE channel=?",
                (channel,)).fetchone()
            if not row:
                state = "PLANNED_NO_ADAPTER"
            elif not row[0] or action not in json.loads(row[1]):
                state = "PLANNED_NOT_ENABLED"
            else:
                state = "APPROVAL_REQUIRED"
            db.execute("""INSERT INTO publishing_plans
                (id,product_id,channel,action,status,details,created_at)
                VALUES(lower(hex(randomblob(16))),?,?,?,?,?,?)""",
                (product_id, channel, action, state,
                 json.dumps(details or {}, sort_keys=True), utc_now()))
        return state
