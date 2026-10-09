#!/usr/bin/env python3
"""Validate the starter product catalogue and create a production-cycle report."""
import json, pathlib, datetime, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "products" / "catalog.json"
OUT = ROOT / "generated" / "production" / "production-report.json"
REQUIRED = {"id", "slug", "name", "category", "status", "price", "deliverables", "qc_gate", "demo"}
def main():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    products = data.get("products", [])
    ids, slugs, errors = set(), set(), []
    for i, p in enumerate(products):
        missing = REQUIRED - p.keys()
        if missing: errors.append(f"products[{i}] missing fields: {sorted(missing)}")
        if p.get("id") in ids: errors.append(f"duplicate product id: {p.get('id')}")
        if p.get("slug") in slugs: errors.append(f"duplicate slug: {p.get('slug')}")
        ids.add(p.get("id")); slugs.add(p.get("slug"))
        if not p.get("deliverables"): errors.append(f"{p.get('id')}: no deliverables")
        if not p.get("qc_gate"): errors.append(f"{p.get('id')}: no QC gate")
    report = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "cycle": "catalogue-validation-and-production-readiness",
        "catalogue_count": len(products), "unique_ids": len(ids),
        "preview_count": sum(p.get("status") == "preview" for p in products),
        "production_ready_count": sum(p.get("status") == "production-ready" for p in products),
        "errors": errors, "result": "PASS" if not errors else "FAIL",
        "limitations": ["This cycle validates catalogue metadata; it does not create new product code or independently certify products.", "Production-ready status requires product-specific tests and artifacts."]
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if errors else 0
if __name__ == "__main__":
    sys.exit(main())
