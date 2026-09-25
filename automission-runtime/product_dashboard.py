import sqlite3
from pathlib import Path


def _ensure_tables(db):
    db.execute("""CREATE TABLE IF NOT EXISTS products (
        id TEXT PRIMARY KEY, stage TEXT NOT NULL
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS publishing_channels (
        id TEXT PRIMARY KEY, status TEXT NOT NULL
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS product_sales (
        id TEXT PRIMARY KEY, product_id TEXT NOT NULL, amount REAL NOT NULL,
        currency TEXT NOT NULL, evidence_url TEXT NOT NULL,
        channel TEXT NOT NULL, recorded_at TEXT NOT NULL
    )""")


def snapshot(db_path: Path):
    with sqlite3.connect(db_path) as db:
        _ensure_tables(db)
        products = db.execute(
            "SELECT stage, COUNT(*) FROM products GROUP BY stage ORDER BY stage"
        ).fetchall()
        channels = db.execute(
            "SELECT status, COUNT(*) FROM publishing_channels GROUP BY status ORDER BY status"
        ).fetchall()
        sales = db.execute(
            """SELECT currency, SUM(amount), COUNT(*)
               FROM product_sales
               WHERE amount > 0 AND evidence_url IS NOT NULL
                 AND TRIM(evidence_url) <> ''
               GROUP BY currency ORDER BY currency"""
        ).fetchall()
    return {
        "products_by_stage": {stage: count for stage, count in products},
        "channels_by_status": {status: count for status, count in channels},
        "verified_sales_by_currency": {
            currency: {"verified_income": float(amount), "verified_sales": int(count)}
            for currency, amount, count in sales
        },
    }
