import hashlib
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
        db = sqlite3.connect(self.db_path, timeout=30)
        db.execute("PRAGMA busy_timeout=30000")
        return db

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
            db.execute("""CREATE TABLE IF NOT EXISTS execution_keys (
                idempotency_key TEXT PRIMARY KEY, opportunity_id TEXT NOT NULL,
                action TEXT NOT NULL, created_at TEXT NOT NULL,
                status TEXT NOT NULL
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
                payload=excluded.payload, updated_at=excluded.updated_at
                WHERE opportunities.status NOT IN ('EXECUTED','APPROVAL_REQUIRED')""",
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

    @staticmethod
    def idempotency_key(item):
        raw = f"{item['id']}|{item.get('action','review')}|{item.get('channel','')}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def claim(self, item, status="PROCESSING"):
        """Atomically claim a pending opportunity and create its idempotency key."""
        key = self.idempotency_key(item)
        now = utc_now()
        with self._connect() as db:
            try:
                db.execute("BEGIN IMMEDIATE")
                cur = db.execute(
                    """UPDATE opportunities SET status=?, updated_at=?
                       WHERE id=? AND status IN ('DISCOVERED','VERIFIED','QUEUED')""",
                    (status, now, item["id"]),
                )
                if cur.rowcount != 1:
                    db.rollback()
                    return False
                db.execute(
                    """INSERT INTO execution_keys
                       (idempotency_key, opportunity_id, action, created_at, status)
                       VALUES(?,?,?,?,?)
                       ON CONFLICT(idempotency_key) DO UPDATE SET
                       status=excluded.status""",
                    (key, item["id"], item.get("action","review"), now, status),
                )
                db.commit()
                return True
            except sqlite3.IntegrityError:
                db.rollback()
                return False
            except Exception:
                db.rollback()
                raise

    def set_status(self, opportunity_id, status):
        with self._connect() as db:
            db.execute("UPDATE opportunities SET status=?, updated_at=? WHERE id=?",
                       (status, utc_now(), opportunity_id))

    def release_for_retry(self, opportunity_id):
        self.set_status(opportunity_id, "QUEUED")

    def recover_stale_processing(self, max_age_seconds=1800):
        cutoff = datetime.fromtimestamp(
            datetime.now(timezone.utc).timestamp() - max_age_seconds, timezone.utc
        ).isoformat()
        with self._connect() as db:
            cur = db.execute(
                """UPDATE opportunities SET status='QUEUED', updated_at=?
                   WHERE status='PROCESSING' AND updated_at < ?""",
                (utc_now(), cutoff),
            )
        return cur.rowcount

    def mark_idempotency(self, item, status):
        with self._connect() as db:
            db.execute("UPDATE execution_keys SET status=? WHERE idempotency_key=?",
                       (status, self.idempotency_key(item)))
