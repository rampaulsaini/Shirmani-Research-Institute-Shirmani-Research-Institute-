import json
import sqlite3
from pathlib import Path


def _table_exists(db, name):
    return db.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def _verified_income(db):
    if not _table_exists(db, "outcomes"):
        return []
    columns = {row[1] for row in db.execute("PRAGMA table_info(outcomes)").fetchall()}
    required = {"amount", "currency", "evidence_url"}
    if not required.issubset(columns):
        return []
    return db.execute(
        """SELECT channel, currency, SUM(amount), COUNT(*)
           FROM outcomes
           WHERE amount > 0
             AND currency IS NOT NULL AND TRIM(currency) <> ''
             AND evidence_url IS NOT NULL AND TRIM(evidence_url) <> ''
           GROUP BY channel, currency
           ORDER BY channel, currency"""
    ).fetchall()


def capture_master_intelligence(
    runtime_db: Path,
    ledger_db: Path,
    product_db: Path | None = None,
):
    """Build evidence-backed cross-domain intelligence without inventing outcomes."""
    result = {
        "verified_income_by_channel_currency": {},
        "task_status": {},
        "product_learning": {},
    }

    with sqlite3.connect(runtime_db) as db:
        for channel, currency, amount, count in _verified_income(db):
            result["verified_income_by_channel_currency"].setdefault(channel, {})[currency] = {
                "verified_income": float(amount),
                "verified_outcomes": int(count),
            }

    with sqlite3.connect(ledger_db) as db:
        if _table_exists(db, "agent_tasks"):
            rows = db.execute(
                "SELECT status, COUNT(*) FROM agent_tasks GROUP BY status ORDER BY status"
            ).fetchall()
            result["task_status"] = {status: int(count) for status, count in rows}

    if product_db and Path(product_db).exists():
        with sqlite3.connect(product_db) as db:
            if _table_exists(db, "product_sales"):
                columns = {row[1] for row in db.execute("PRAGMA table_info(product_sales)").fetchall()}
                if {"amount", "currency", "evidence_url"}.issubset(columns):
                    rows = db.execute(
                        """SELECT currency, SUM(amount), COUNT(*)
                           FROM product_sales
                           WHERE amount > 0
                             AND currency IS NOT NULL AND TRIM(currency) <> ''
                             AND evidence_url IS NOT NULL AND TRIM(evidence_url) <> ''
                           GROUP BY currency ORDER BY currency"""
                    ).fetchall()
                    result["product_learning"] = {
                        currency: {"verified_income": float(amount), "verified_sales": int(count)}
                        for currency, amount, count in rows
                    }
    return result


def write_intelligence(db_path: Path, intelligence):
    db_path = Path(db_path)
    with sqlite3.connect(db_path) as db:
        db.execute(
            """CREATE TABLE IF NOT EXISTS master_learning (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                captured_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                intelligence_json TEXT NOT NULL
            )"""
        )
        db.execute(
            "INSERT INTO master_learning(intelligence_json) VALUES(?)",
            (json.dumps(intelligence, sort_keys=True),),
        )



def _verified_deliveries(fulfillment_db):
    if not fulfillment_db or not Path(fulfillment_db).exists():
        return {}
    with sqlite3.connect(fulfillment_db) as db:
        if not _table_exists(db, "deliveries"):
            return {}
        columns = {row[1] for row in db.execute("PRAGMA table_info(deliveries)").fetchall()}
        required = {"state", "delivery_evidence_url", "product_id"}
        if not required.issubset(columns):
            return {}
        rows = db.execute(
            """SELECT product_id, COUNT(*)
               FROM deliveries
               WHERE state='VERIFIED'
                 AND delivery_evidence_url IS NOT NULL
                 AND TRIM(delivery_evidence_url) <> ''
               GROUP BY product_id ORDER BY product_id"""
        ).fetchall()
    return {product_id: {"verified_deliveries": int(count)} for product_id, count in rows}


def capture_fulfillment_intelligence(fulfillment_db):
    """Return only evidence-backed verified delivery signals."""
    return {"verified_deliveries_by_product": _verified_deliveries(fulfillment_db)}
