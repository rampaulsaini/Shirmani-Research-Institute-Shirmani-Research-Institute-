from master_learning import capture_fulfillment_intelligence
from master_dashboard import snapshot
from fulfillment_ledger import FulfillmentLedger


def test_fulfillment_learning_counts_only_verified(tmp_path):
    db = tmp_path / "fulfillment.db"
    ledger = FulfillmentLedger(db)
    key = ledger.create("order-1", "product-1")
    ledger.transition(key, "PREPARING")
    ledger.transition(key, "READY")
    ledger.transition(key, "DELIVERED", evidence_url="https://example.invalid/delivery")
    assert capture_fulfillment_intelligence(db)["verified_deliveries_by_product"] == {}
    ledger.transition(key, "VERIFIED", evidence_url="https://example.invalid/verified")
    result = capture_fulfillment_intelligence(db)
    assert result["verified_deliveries_by_product"]["product-1"]["verified_deliveries"] == 1


def test_dashboard_accepts_fulfillment_database(tmp_path):
    runtime = tmp_path / "runtime.db"
    ledger = tmp_path / "ledger.db"
    fulfillment = tmp_path / "fulfillment.db"
    FulfillmentLedger(fulfillment)
    result = snapshot(runtime, ledger, fulfillment_db=fulfillment)
    assert "fulfillment_learning" in result
