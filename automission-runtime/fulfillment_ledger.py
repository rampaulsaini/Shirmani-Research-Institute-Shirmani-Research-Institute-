import hashlib
import sqlite3
from datetime import datetime, timezone


DELIVERY_STATES = (
    "ORDER_RECEIVED",
    "PREPARING",
    "AUTHORIZATION_REQUIRED",
    "READY",
    "DELIVERED",
    "VERIFIED",
    "FAILED",
)


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def delivery_key(order_id, product_id):
    return hashlib.sha256(f"{order_id}|{product_id}".encode("utf-8")).hexdigest()


class FulfillmentLedger:
    """Auditable customer-delivery state machine; delivery never implies verified outcome."""

    def __init__(self, db_path):
        self.db_path = str(db_path)
        with sqlite3.connect(self.db_path) as db:
            db.execute("""CREATE TABLE IF NOT EXISTS deliveries (
                delivery_key TEXT PRIMARY KEY,
                order_id TEXT NOT NULL,
                product_id TEXT NOT NULL,
                state TEXT NOT NULL,
                delivery_evidence_url TEXT,
                failure_reason TEXT,
                updated_at TEXT NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS delivery_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                delivery_key TEXT NOT NULL,
                from_state TEXT,
                to_state TEXT NOT NULL,
                evidence_url TEXT,
                created_at TEXT NOT NULL
            )""")

    def create(self, order_id, product_id):
        key = delivery_key(order_id, product_id)
        with sqlite3.connect(self.db_path) as db:
            db.execute(
                """INSERT OR IGNORE INTO deliveries
                   (delivery_key, order_id, product_id, state, updated_at)
                   VALUES (?, ?, ?, 'ORDER_RECEIVED', ?)""",
                (key, order_id, product_id, utc_now()),
            )
        return key

    def transition(self, key, state, evidence_url=None, failure_reason=None):
        if state not in DELIVERY_STATES:
            raise ValueError("invalid_delivery_state")
        with sqlite3.connect(self.db_path) as db:
            row = db.execute(
                "SELECT state FROM deliveries WHERE delivery_key=?", (key,)
            ).fetchone()
            if not row:
                raise KeyError("unknown_delivery")
            current = row[0]
            allowed = {
                "ORDER_RECEIVED": {"PREPARING", "FAILED"},
                "PREPARING": {"AUTHORIZATION_REQUIRED", "READY", "FAILED"},
                "AUTHORIZATION_REQUIRED": {"READY", "FAILED"},
                "READY": {"DELIVERED", "FAILED"},
                "DELIVERED": {"VERIFIED", "FAILED"},
                "VERIFIED": set(),
                "FAILED": {"PREPARING"},
            }
            if state not in allowed[current]:
                raise ValueError("invalid_delivery_transition")
            if state in {"DELIVERED", "VERIFIED"} and not evidence_url:
                raise ValueError("delivery_evidence_required")
            db.execute(
                """UPDATE deliveries
                   SET state=?, delivery_evidence_url=COALESCE(?, delivery_evidence_url),
                       failure_reason=?, updated_at=?
                   WHERE delivery_key=?""",
                (state, evidence_url, failure_reason, utc_now(), key),
            )
            db.execute(
                """INSERT INTO delivery_events
                   (delivery_key, from_state, to_state, evidence_url, created_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (key, current, state, evidence_url, utc_now()),
            )

    def get(self, key):
        with sqlite3.connect(self.db_path) as db:
            row = db.execute(
                """SELECT delivery_key, order_id, product_id, state,
                          delivery_evidence_url, failure_reason, updated_at
                   FROM deliveries WHERE delivery_key=?""", (key,)
            ).fetchone()
        return dict(zip(
            ("delivery_key","order_id","product_id","state",
             "delivery_evidence_url","failure_reason","updated_at"),
            row
        )) if row else None
