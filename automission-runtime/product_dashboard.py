import sqlite3
from pathlib import Path


def _table_exists(db, name):
    return db.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def snapshot(db_path: Path):
    with sqlite3.connect(db_path) as db:
        products = (
            db.execute("SELECT stage, COUNT(*) FROM products GROUP BY stage ORDER BY stage").fetchall()
            if _table_exists(db, "products") else []
        )
        channels = (
            db.execute("SELECT status, COUNT(*) FROM publishing_channels GROUP BY status ORDER BY status").fetchall()
            if _table_exists(db, "publishing_channels") else []
        )
        sales = (
            db.execute(
                """SELECT currency, SUM(amount), COUNT(*)
                   FROM product_sales
                   WHERE amount > 0 AND evidence_url IS NOT NULL
                     AND TRIM(evidence_url) <> ''
                   GROUP BY currency ORDER BY currency"""
            ).fetchall()
            if _table_exists(db, "product_sales") else []
        )
    return {
        "products_by_stage": {stage: count for stage, count in products},
        "channels_by_status": {status: count for status, count in channels},
        "verified_sales_by_currency": {
            currency: {"verified_income": float(amount), "verified_sales": int(count)}
            for currency, amount, count in sales
        },
    }
