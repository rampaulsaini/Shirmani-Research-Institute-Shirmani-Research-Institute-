import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

def utc_now():
    return datetime.now(timezone.utc).isoformat()

class QueueStore:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init(self):
        with self._connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS opportunities (
                id TEXT PRIMARY KEY, source TEXT NOT NULL, channel TEXT NOT NULL,
                title TEXT NOT NULL, description TEXT NOT NULL, url TEXT,
                evidence_url TEXT, status TEXT NOT NULL, score REAL DEFAULT 0,
                payload TEXT NOT NULL, discovered_at TEXT NOT NULL,
                updated_at TEXT NOT NULL, UNIQUE(source, url, title)
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS outcomes (
                id TEXT PRIMARY KEY, opportunity_id TEXT NOT NULL,
                status TEXT NOT NULL, verified_income REAL DEFAULT 0,
                currency TEXT, evidence_url TEXT, notes TEXT,
                recorded_at TEXT NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS approvals (
                id TEXT PRIMARY KEY, opportunity_id TEXT NOT NULL,
                action TEXT NOT NULL, status TEXT NOT NULL,
                decided_at TEXT, notes TEXT
            )""")

    def upsert_opportunity(self, item):
        now = utc_now()
        oid = item.get("id") or str(uuid.uuid4())
        payload = json.dumps(item, sort_keys=True)
        with self._connect() as db:
            db.execute("""INSERT INTO opportunities
                (id,source,channel,title,description,url,evidence_url,status,score,payload,discovered_at,updated_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(source,url,title) DO UPDATE SET
                description=excluded.description, evidence_url=excluded.evidence_url,
                payload=excluded.payload, updated_at=excluded.updated_at""",
                (oid, item["source"], item["channel"], item["title"],
                 item.get("description",""), item.get("url"), item.get("evidence_url"),
                 item.get("status","DISCOVERED"), float(item.get("score",0)),
                 payload, now, now))
        return oid

    def pending(self, limit=25):
        with self._connect() as db:
            rows = db.execute("""SELECT id,source,channel,title,description,url,evidence_url,status,score,payload
                                 FROM opportunities
                                 WHERE status IN ('DISCOVERED','VERIFIED','QUEUED')
                                 ORDER BY score DESC, updated_at ASC LIMIT ?""",(limit,)).fetchall()
        return [dict(zip(["id","source","channel","title","description","url","evidence_url","status","score","payload"], r)) for r in rows]
