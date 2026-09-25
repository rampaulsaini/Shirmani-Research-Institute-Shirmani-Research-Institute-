import pytest
from fulfillment_ledger import FulfillmentLedger


def test_delivery_requires_evidence():
    ledger = FulfillmentLedger(":memory:")
    key = ledger.create("order-1", "product-1")
    ledger.transition(key, "PREPARING")
    ledger.transition(key, "READY")
    with pytest.raises(ValueError, match="delivery_evidence_required"):
        ledger.transition(key, "DELIVERED")


def test_delivery_is_auditable_and_verified_only_after_delivery():
    ledger = FulfillmentLedger(":memory:")
    key = ledger.create("order-2", "product-2")
    ledger.transition(key, "PREPARING")
    ledger.transition(key, "READY")
    ledger.transition(key, "DELIVERED", evidence_url="https://example.invalid/delivery/2")
    assert ledger.get(key)["state"] == "DELIVERED"
    ledger.transition(key, "VERIFIED", evidence_url="https://example.invalid/verified/2")
    assert ledger.get(key)["state"] == "VERIFIED"


def test_invalid_transition_is_rejected():
    ledger = FulfillmentLedger(":memory:")
    key = ledger.create("order-3", "product-3")
    with pytest.raises(ValueError, match="invalid_delivery_transition"):
        ledger.transition(key, "VERIFIED", evidence_url="https://example.invalid/x")
