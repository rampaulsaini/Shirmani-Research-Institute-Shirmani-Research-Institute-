import sqlite3
from pathlib import Path

def snapshot(db_path: Path):
    with sqlite3.connect(db_path) as db:
        products = db.execute("""SELECT stage, COUNT(*) FROM products
                                 GROUP BY stage ORDER BY stage""").fetchall()
        channels = db.execute("""SELECT status, COUNT(*) FROM publishing_channels
                                 GROUP BY status ORDER BY status""").fetchall()
        sales = db.execute("""SELECT currency, SUM(amount), COUNT(*)
                              FROM product_sales
                              WHERE amount > 0 AND evidence_url IS NOT NULL
                              AND TRIM(evidence_url) <> ''
                              GROUP BY currency ORDER BY currency""").fetchall()
    return {
        "products_by_stage": {stage: count for stage, count in products},
        "channels_by_status": {status: count for status, count in channels},
        "verified_sales_by_currency": {
            currency: {"verified_income": float(amount), "verified_sales": int(count)}
            for currency, amount, count in sales
        },
    }
