import sqlite3
from pathlib import Path

from master_learning import capture_master_intelligence


def _table_exists(db, name):
    return db.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def _counts(db, table, column):
    if not _table_exists(db, table):
        return {}
    return {
        key: int(value)
        for key, value in db.execute(
            f"SELECT {column}, COUNT(*) FROM {table} GROUP BY {column} ORDER BY {column}"
        ).fetchall()
    }


def snapshot(runtime_db: Path, ledger_db: Path, product_db: Path | None = None):
    with sqlite3.connect(runtime_db) as db:
        queue = _counts(db, "opportunities", "status")
        approvals = _counts(db, "approvals", "status")
        outcomes = _counts(db, "outcomes", "status")

    dashboard = {
        "queue_by_status": queue,
        "approval_by_status": approvals,
        "outcome_by_status": outcomes,
    }

    if product_db and Path(product_db).exists():
        with sqlite3.connect(product_db) as db:
            dashboard["products_by_stage"] = _counts(db, "products", "stage")
    else:
        dashboard["products_by_stage"] = {}

    dashboard["master_learning"] = capture_master_intelligence(
        runtime_db, ledger_db, product_db
    )
    return dashboard
