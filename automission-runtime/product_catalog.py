import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

STAGES = (
    "IDEA", "RESEARCHED", "CREATED", "QC_PASSED", "PACKAGED",
    "PRICED", "READY_TO_PUBLISH", "PUBLISH_APPROVAL_REQUIRED",
    "PUBLISHED", "VERIFIED_SALE", "LEARNING",
)
PRODUCT_TYPES = (
    "software", "website", "ai_tool", "book", "course",
    "animation", "cartoon", "film", "music", "painting",
    "research", "service_package", "other",
)
IRREVERSIBLE_STAGES = {"PUBLISH_APPROVAL_REQUIRED", "PUBLISHED", "VERIFIED_SALE"}

def utc_now():
    return datetime.now(timezone.utc).isoformat()

class ProductCatalog:
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
            db.execute("""CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY, slug TEXT NOT NULL UNIQUE, title TEXT NOT NULL,
                product_type TEXT NOT NULL, description TEXT NOT NULL DEFAULT '',
                stage TEXT NOT NULL, price REAL, currency TEXT, evidence_url TEXT,
                quality_score REAL DEFAULT 0, payload TEXT NOT NULL,
                created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS product_events (
                id TEXT PRIMARY KEY, product_id TEXT NOT NULL, from_stage TEXT,
                to_stage TEXT NOT NULL, actor TEXT NOT NULL, notes TEXT,
                created_at TEXT NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS product_sales (
                id TEXT PRIMARY KEY, product_id TEXT NOT NULL, amount REAL NOT NULL,
                currency TEXT NOT NULL, evidence_url TEXT NOT NULL,
                channel TEXT NOT NULL, recorded_at TEXT NOT NULL
            )""")

    def create(self, title, product_type, description="", slug=None, payload=None):
        if product_type not in PRODUCT_TYPES:
            raise ValueError("unsupported product type")
        if not title or not title.strip():
            raise ValueError("product title is required")
        slug = slug or "-".join(title.lower().split())[:80]
        now = utc_now()
        pid = str(uuid.uuid4())
        with self._connect() as db:
            db.execute("""INSERT INTO products
                (id,slug,title,product_type,description,stage,payload,created_at,updated_at)
                VALUES(?,?,?,?,?,?,?,?,?)""",
                (pid, slug, title.strip(), product_type, description.strip(),
                 "IDEA", json.dumps(payload or {}, sort_keys=True), now, now))
            db.execute("""INSERT INTO product_events
                (id,product_id,from_stage,to_stage,actor,notes,created_at)
                VALUES(?,?,?,?,?,?,?)""",
                (str(uuid.uuid4()), pid, None, "IDEA", "automission", "created", now))
        return pid

    def get(self, product_id):
        with self._connect() as db:
            row = db.execute("SELECT * FROM products WHERE id=?", (product_id,)).fetchone()
            if not row:
                return None
            cols = [x[1] for x in db.execute("PRAGMA table_info(products)")]
            return dict(zip(cols, row))

    def transition(self, product_id, to_stage, actor="automission", notes=""):
        if to_stage not in STAGES:
            raise ValueError("unknown product stage")
        product = self.get(product_id)
        if not product:
            raise KeyError(product_id)
        current = product["stage"]
        if current == to_stage:
            return False
        if STAGES.index(to_stage) < STAGES.index(current):
            raise ValueError("product stage cannot move backwards")
        if current == "READY_TO_PUBLISH" and to_stage == "PUBLISHED":
            raise PermissionError("publishing requires explicit approval")
        if to_stage == "PUBLISHED" and current != "PUBLISH_APPROVAL_REQUIRED":
            raise PermissionError("product must enter approval stage before publishing")
        now = utc_now()
        with self._connect() as db:
            db.execute("UPDATE products SET stage=?,updated_at=? WHERE id=?",
                       (to_stage, now, product_id))
            db.execute("""INSERT INTO product_events
                (id,product_id,from_stage,to_stage,actor,notes,created_at)
                VALUES(?,?,?,?,?,?,?)""",
                (str(uuid.uuid4()), product_id, current, to_stage, actor, notes, now))
        return True

    def approve_publish(self, product_id, actor="human"):
        product = self.get(product_id)
        if not product:
            raise KeyError(product_id)
        if product["stage"] != "PUBLISH_APPROVAL_REQUIRED":
            raise ValueError("publish approval is not pending")
        return self.transition(product_id, "PUBLISHED", actor=actor, notes="explicit publish approval")

    def set_quality(self, product_id, quality_score, evidence_url=None):
        score = float(quality_score)
        if score < 0 or score > 100:
            raise ValueError("quality score must be 0..100")
        if score < 80:
            raise ValueError("quality gate requires score >= 80")
        with self._connect() as db:
            db.execute("""UPDATE products SET quality_score=?,evidence_url=?,updated_at=?
                         WHERE id=?""",
                       (score, evidence_url, utc_now(), product_id))

    def set_price(self, product_id, price, currency):
        if price is None or float(price) < 0:
            raise ValueError("price must be non-negative")
        if not currency or not currency.strip():
            raise ValueError("currency is required")
        with self._connect() as db:
            db.execute("""UPDATE products SET price=?,currency=?,updated_at=? WHERE id=?""",
                       (float(price), currency.strip().upper(), utc_now(), product_id))

    def record_sale(self, product_id, amount, currency, evidence_url, channel):
        if amount is None or float(amount) <= 0:
            raise ValueError("sale amount must be positive")
        if not currency or not currency.strip():
            raise ValueError("sale currency is required")
        if not evidence_url or not evidence_url.strip():
            raise ValueError("sale evidence URL is required")
        if not channel or not channel.strip():
            raise ValueError("sale channel is required")
        product = self.get(product_id)
        if not product:
            raise KeyError(product_id)
        if product["stage"] not in {"PUBLISHED", "VERIFIED_SALE", "LEARNING"}:
            raise ValueError("sale requires a published product")
        now = utc_now()
        with self._connect() as db:
            db.execute("""INSERT INTO product_sales
                (id,product_id,amount,currency,evidence_url,channel,recorded_at)
                VALUES(?,?,?,?,?,?,?)""",
                (str(uuid.uuid4()), product_id, float(amount),
                 currency.strip().upper(), evidence_url.strip(), channel.strip(), now))
        if product["stage"] == "PUBLISHED":
            self.transition(product_id, "VERIFIED_SALE", notes="evidence-backed sale recorded")
        return True

    def verified_sales(self):
        with self._connect() as db:
            rows = db.execute("""SELECT product_id,currency,SUM(amount),COUNT(*)
                                 FROM product_sales
                                 WHERE amount>0 AND evidence_url IS NOT NULL
                                 AND TRIM(evidence_url)<>'' GROUP BY product_id,currency""").fetchall()
        return rows
