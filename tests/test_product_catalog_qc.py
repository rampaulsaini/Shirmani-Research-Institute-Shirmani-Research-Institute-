import copy
import json
from pathlib import Path

import pytest

from factory.product_catalog_qc import validate_catalog

CATALOG = Path(__file__).resolve().parents[1] / "products" / "product-catalog.json"


def load_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def test_public_catalog_passes_validation():
    assert validate_catalog(load_catalog()) is True


@pytest.mark.parametrize("field", ["product_id", "title_hi", "type", "price_inr", "currency",
                                   "listing_state", "verification_state", "delivery", "source_reference"])
def test_required_product_fields_are_enforced(field):
    data = load_catalog()
    data["products"][0].pop(field)
    with pytest.raises(ValueError, match="PRODUCT_MISSING_FIELD"):
        validate_catalog(data)


def test_duplicate_product_ids_are_blocked():
    data = load_catalog()
    data["products"][1]["product_id"] = data["products"][0]["product_id"]
    with pytest.raises(ValueError, match="DUPLICATE_PRODUCT_ID"):
        validate_catalog(data)


@pytest.mark.parametrize("price", [True, float("nan"), float("inf"), -1])
def test_invalid_prices_fail_closed(price):
    data = load_catalog()
    data["products"][0]["price_inr"] = price
    with pytest.raises(ValueError, match="INVALID_PRICE"):
        validate_catalog(data)


def test_invalid_currency_is_blocked():
    data = load_catalog()
    data["products"][0]["currency"] = "USD"
    with pytest.raises(ValueError, match="INVALID_CURRENCY"):
        validate_catalog(data)


def test_unknown_listing_state_is_blocked():
    data = load_catalog()
    data["products"][0]["listing_state"] = "SOLD"
    with pytest.raises(ValueError, match="INVALID_LISTING_STATE"):
        validate_catalog(data)


def test_automission_cannot_invent_transaction_outcomes():
    data = load_catalog()
    data["products"][0]["sales"] = 1
    with pytest.raises(ValueError, match="FORBIDDEN_TRANSACTION_FIELD"):
        validate_catalog(data)


def test_verification_state_is_explicit_and_bounded():
    data = load_catalog()
    data["products"][0]["verification_state"] = "AUTO_VERIFIED"
    with pytest.raises(ValueError, match="INVALID_VERIFICATION_STATE"):
        validate_catalog(data)


def test_catalog_validation_does_not_mutate_input():
    data = load_catalog()
    snapshot = copy.deepcopy(data)
    validate_catalog(data)
    assert data == snapshot
