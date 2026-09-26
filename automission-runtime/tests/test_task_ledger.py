import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from master_automission import AgentTask
from task_ledger import AgentTaskLedger


def test_task_ledger_is_idempotent_and_persistent(tmp_path):
    db = tmp_path / "ledger.db"
    ledger = AgentTaskLedger(db)
    task = AgentTask("product-cycle", "products", "product-orchestrator", "create_blueprint")

    key1 = ledger.record(task, {"title": "demo"})
    key2 = ledger.record(task, {"title": "demo"})
    assert key1 == key2
    assert ledger.snapshot() == {"DISCOVERED": 1}

    ledger.set_status(key1, "RUNNING")
    ledger.set_status(key1, "COMPLETED", output={"product_id": "p1"}, evidence_url="evidence://p1")
    assert ledger.snapshot() == {"COMPLETED": 1}

    reopened = AgentTaskLedger(db)
    assert reopened.snapshot() == {"COMPLETED": 1}
