import sqlite3
from pathlib import Path

def capture_product_intelligence(db_path: Path):
    """Aggregate only evidence-backed product sales; never infer revenue."""
    with sqlite3.connect(db_path) as db:
        rows = db.execute("""SELECT p.product_type, s.currency,
                                    SUM(s.amount), COUNT(*)
                             FROM product_sales s
                             JOIN products p ON p.id=s.product_id
                             WHERE s.amount > 0
                               AND s.evidence_url IS NOT NULL
                               AND TRIM(s.evidence_url) <> ''
                               AND s.currency IS NOT NULL
                               AND TRIM(s.currency) <> ''
                             GROUP BY p.product_type, s.currency""").fetchall()
    by_type = {}
    for product_type, currency, amount, count in rows:
        by_type.setdefault(product_type, {})[currency.upper()] = {
            "verified_sales": int(count),
            "verified_income": float(amount),
        }
    return {"product_types": by_type, "evidence_backed_sales": sum(r[3] for r in rows)}

def prioritize_product(base_score, product_type, currency, intelligence):
    score = float(base_score or 0)
    bucket = intelligence.get("product_types", {}).get(product_type, {})
    history = bucket.get(str(currency or "").upper())
    if not history or not history["verified_sales"]:
        return score
    return score + min(
        history["verified_income"] / history["verified_sales"], 1000.0
    ) * 0.01


def capture_fulfillment_signal(db_path: Path):
    """Return verified delivery counts only; no revenue inference."""
    db_path = Path(db_path)
    if not db_path.exists():
        return {}
    with sqlite3.connect(db_path) as db:
        exists = db.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='deliveries'"
        ).fetchone()
        if not exists:
            return {}
        rows = db.execute(
            """SELECT product_id, COUNT(*)
               FROM deliveries
               WHERE state='VERIFIED'
                 AND delivery_evidence_url IS NOT NULL
                 AND TRIM(delivery_evidence_url) <> ''
               GROUP BY product_id ORDER BY product_id"""
        ).fetchall()
    return {product_id: int(count) for product_id, count in rows}


def prioritize_with_fulfillment(base_score, product_id, fulfillment_signal):
    """Bounded score adjustment from verified fulfillment only."""
    score = float(base_score or 0)
    verified = int(fulfillment_signal.get(product_id, 0) or 0)
    return score + min(verified, 100) * 0.01
