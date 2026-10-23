#!/usr/bin/env python3
"""Validate starter product metadata and report registered offers without conflating the two."""
import json
import pathlib
import datetime
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "products" / "catalog.json"
OFFER_REGISTRY = ROOT / "factory" / "product-catalog.json"
OUT = ROOT / "generated" / "production" / "production-report.json"
REQUIRED = {"id", "slug", "name", "category", "status", "price", "deliverables", "qc_gate", "demo"}


def main():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    products = data.get("products", [])
    ids, slugs, errors = set(), set(), []
    for i, p in enumerate(products):
        missing = REQUIRED - p.keys()
        if missing:
            errors.append(f"products[{i}] missing fields: {sorted(missing)}")
        if p.get("id") in ids:
            errors.append(f"duplicate product id: {p.get('id')}")
        if p.get("slug") in slugs:
            errors.append(f"duplicate slug: {p.get('slug')}")
        ids.add(p.get("id"))
        slugs.add(p.get("slug"))
        if not p.get("deliverables"):
            errors.append(f"{p.get('id')}: no deliverables")
        if not p.get("qc_gate"):
            errors.append(f"{p.get('id')}: no QC gate")

    # The starter prototype catalogue and the commercial offer registry are different
    # sources. Report both so a passing metadata check cannot imply product readiness.
    registry = json.loads(OFFER_REGISTRY.read_text(encoding="utf-8"))
    offers = [
        offer
        for lane in registry.get("lanes", [])
        for offer in lane.get("offers", [])
    ]
    offers_with_asset_path = [o for o in offers if o.get("asset_path")]
    present_asset_paths = [
        o for o in offers_with_asset_path
        if (ROOT / o["asset_path"]).is_file()
    ]
    missing_asset_paths = [
        o["id"] for o in offers_with_asset_path
        if not (ROOT / o["asset_path"]).is_file()
    ]
    external_paths = [
        o["id"] for o in offers
        if o.get("store") or o.get("destination")
    ]
    service_offers = [
        o["id"] for o in offers
        if "service" in str(o.get("delivery", "")).lower()
    ]

    report = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "cycle": "catalogue-validation-and-production-readiness",
        "starter_catalogue_count": len(products),
        "unique_starter_ids": len(ids),
        "preview_count": sum(p.get("status") == "preview" for p in products),
        "production_ready_count": sum(p.get("status") == "production-ready" for p in products),
        "registered_offer_count": len(offers),
        "registered_offers_with_declared_repository_asset_path": len(offers_with_asset_path),
        "registered_offers_with_present_repository_asset": len(present_asset_paths),
        "registered_offers_with_missing_repository_asset": len(missing_asset_paths),
        "registered_offers_missing_asset_ids": missing_asset_paths,
        "registered_offers_with_external_checkout_or_destination": len(external_paths),
        "registered_external_path_ids": external_paths,
        "registered_service_offer_count": len(service_offers),
        "registered_service_offer_ids": service_offers,
        "errors": errors,
        "result": "PASS" if not errors else "FAIL",
        "limitations": [
            "PASS validates starter catalogue metadata only; it does not create product code or independently certify products.",
            "The registered offer count is separate from the starter catalogue count.",
            "A repository asset path being present does not prove product quality, customer delivery, or independent verification.",
            "An external checkout/destination URL is recorded, not independently tested for checkout completion.",
            "Production-ready status requires product-specific tests and artifacts."
        ]
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
