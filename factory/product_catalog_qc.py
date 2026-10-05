"""Deterministic, fail-closed QC for the public product catalog.

Catalog readiness is not sales, payment, delivery, or independent verification.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "products" / "product-catalog.json"

REQUIRED_CATALOG_FIELDS = ("schema_version", "catalog_id", "status", "products", "pipeline")
REQUIRED_PRODUCT_FIELDS = (
    "product_id",
    "title_hi",
    "type",
    "price_inr",
    "currency",
    "listing_state",
    "verification_state",
    "delivery",
    "source_reference",
)
ALLOWED_LISTING_STATES = {"READY_FOR_LISTING", "LISTED", "NOT_READY"}
ALLOWED_VERIFICATION_STATES = {"NOT_VERIFIED", "VERIFIED"}
FORBIDDEN_TRANSACTION_FIELDS = {"sales", "orders", "customers", "payments", "revenue", "profit"}


def validate_catalog(data):
    if not isinstance(data, dict):
        raise ValueError("PRODUCT_CATALOG_NOT_OBJECT")
    for key in REQUIRED_CATALOG_FIELDS:
        if key not in data:
            raise ValueError("PRODUCT_CATALOG_MISSING_FIELD:" + key)

    if not isinstance(data["schema_version"], str) or not data["schema_version"].strip():
        raise ValueError("INVALID_SCHEMA_VERSION")
    if not isinstance(data["catalog_id"], str) or not data["catalog_id"].strip():
        raise ValueError("INVALID_CATALOG_ID")
    if data["status"] != "CATALOG_READY":
        raise ValueError("INVALID_CATALOG_STATUS")
    if not isinstance(data["products"], list) or not data["products"]:
        raise ValueError("PRODUCT_CATALOG_EMPTY")
    if not isinstance(data["pipeline"], list) or not data["pipeline"]:
        raise ValueError("PRODUCT_PIPELINE_EMPTY")

    ids = set()
    for product in data["products"]:
        if not isinstance(product, dict):
            raise ValueError("PRODUCT_NOT_OBJECT")
        product_id = product.get("product_id", "unknown")
        for key in REQUIRED_PRODUCT_FIELDS:
            if key not in product:
                raise ValueError(f"PRODUCT_MISSING_FIELD:{product_id}:{key}")
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError("INVALID_PRODUCT_ID")
        if product_id in ids:
            raise ValueError("DUPLICATE_PRODUCT_ID:" + product_id)
        ids.add(product_id)

        if not isinstance(product["title_hi"], str) or not product["title_hi"].strip():
            raise ValueError("INVALID_PRODUCT_TITLE:" + product_id)
        if not isinstance(product["type"], str) or not product["type"].strip():
            raise ValueError("INVALID_PRODUCT_TYPE:" + product_id)
        if isinstance(product["price_inr"], bool) or not isinstance(product["price_inr"], (int, float)):
            raise ValueError("INVALID_PRICE:" + product_id)
        if not math.isfinite(float(product["price_inr"])) or product["price_inr"] < 0:
            raise ValueError("INVALID_PRICE:" + product_id)
        if product["currency"] != "INR":
            raise ValueError("INVALID_CURRENCY:" + product_id)
        if product["listing_state"] not in ALLOWED_LISTING_STATES:
            raise ValueError("INVALID_LISTING_STATE:" + product_id)
        if product["verification_state"] not in ALLOWED_VERIFICATION_STATES:
            raise ValueError("INVALID_VERIFICATION_STATE:" + product_id)
        if not isinstance(product["delivery"], str) or not product["delivery"].strip():
            raise ValueError("INVALID_DELIVERY:" + product_id)
        if not isinstance(product["source_reference"], str) or not product["source_reference"].strip():
            raise ValueError("INVALID_SOURCE_REFERENCE:" + product_id)

        forbidden = sorted(FORBIDDEN_TRANSACTION_FIELDS.intersection(product))
        if forbidden:
            raise ValueError(f"FORBIDDEN_TRANSACTION_FIELD:{product_id}:{','.join(forbidden)}")

    return True


def main():
    if not CATALOG.is_file():
        raise SystemExit("PRODUCT_CATALOG_MISSING")
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        validate_catalog(data)
    except (json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc

    print(json.dumps({
        "status": "PASS",
        "catalog_id": data["catalog_id"],
        "product_count": len(data["products"]),
        "rule": "catalog readiness is not sales, payment, delivery or independent verification",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
