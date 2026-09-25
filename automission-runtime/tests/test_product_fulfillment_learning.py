from product_learning import capture_fulfillment_signal, prioritize_with_fulfillment
from fulfillment_ledger import FulfillmentLedger


def test_verified_fulfillment_signal_is_evidence_backed(tmp_path):
    db = tmp_path / "fulfillment.db"
    ledger = FulfillmentLedger(db)
    key = ledger.create("o1", "p1")
    ledger.transition(key, "PREPARING")
    ledger.transition(key, "READY")
    ledger.transition(key, "DELIVERED", evidence_url="https://example.invalid/d")
    assert capture_fulfillment_signal(db) == {}
    ledger.transition(key, "VERIFIED", evidence_url="https://example.invalid/v")
    assert capture_fulfillment_signal(db) == {"p1": 1}


def test_fulfillment_score_is_bounded():
    assert prioritize_with_fulfillment(10, "p1", {"p1": 1000}) == 11
