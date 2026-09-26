import sqlite3

from master_dashboard import snapshot
from master_learning import capture_master_intelligence


def test_master_learning_uses_only_verified_income(tmp_path):
    runtime = tmp_path / "runtime.db"
    ledger = tmp_path / "ledger.db"
    with sqlite3.connect(runtime) as db:
        db.execute("""CREATE TABLE outcomes(
            id INTEGER, channel TEXT, amount REAL, currency TEXT, evidence_url TEXT
        )""")
        db.executemany(
            "INSERT INTO outcomes VALUES(?,?,?,?,?)",
            [
                (1, "freelancing", 100, "USD", "https://evidence.example/1"),
                (2, "freelancing", 900, "USD", ""),
                (3, "freelancing", 500, None, "https://evidence.example/3"),
            ],
        )
    with sqlite3.connect(ledger) as db:
        db.execute("""CREATE TABLE agent_tasks(
            task_key TEXT, status TEXT
        )""")
        db.executemany(
            "INSERT INTO agent_tasks VALUES(?,?)",
            [("a", "QUEUED"), ("b", "COMPLETED")],
        )

    intelligence = capture_master_intelligence(runtime, ledger)
    assert intelligence["verified_income_by_channel_currency"]["freelancing"]["USD"]["verified_income"] == 100.0
    assert intelligence["task_status"] == {"COMPLETED": 1, "QUEUED": 1}


def test_dashboard_is_safe_on_fresh_databases(tmp_path):
    runtime = tmp_path / "runtime.db"
    ledger = tmp_path / "ledger.db"
    with sqlite3.connect(runtime):
        pass
    with sqlite3.connect(ledger):
        pass

    result = snapshot(runtime, ledger)
    assert result["queue_by_status"] == {}
    assert result["approval_by_status"] == {}
    assert result["outcome_by_status"] == {}
    assert result["products_by_stage"] == {}
    assert result["master_learning"]["task_status"] == {}
