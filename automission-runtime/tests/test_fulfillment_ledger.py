import pytest
from pathlib import Path
from fulfillment_ledger import FulfillmentLedger


def make_ledger(tmp_path):
    return FulfillmentLedger(tmp_path / "fulfillment.db")


def test_delivery_requires_evidence(tmp_path):
    ledger = make_ledger(tmp_path)
    key = ledger.create("order-1", "product-1")
    ledger.transition(key, "PREPARING")
    ledger.transition(key, "READY")
    with pytest.raises(ValueError, match="delivery_evidence_required"):
        ledger.transition(key, "DELIVERED")


def test_delivery_is_auditable_and_verified_only_after_delivery(tmp_path):
    ledger = ledger(tmp_path)
    key = ledger.create("order-2", "product-2")
    ledger.transition(key, "PREPARING")
    ledger.transition(key, "READY")
    ledger.transition(key, "DELIVERED", evidence_url="https://example.invalid/delivery/2")
    assert ledger.get(key)["state"] == "DELIVERED"
    ledger.transition(key, "VERIFIED", evidence_url="https://example.invalid/verified/2")
    assert ledger.get(key)["state"] == "VERIFIED"


def test_invalid_transition_is_rejected(tmp_path):
    ledger = ledger(tmp_path)
    key = ledger.create("order-3", "product-3")
    with pytest.raises(ValueError, match="invalid_delivery_transition"):
        ledger.transition(key, "VERIFIED", evidence_url="https://example.invalid/x")
