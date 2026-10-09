#!/usr/bin/env python3
"""Validate catalogue integrity and showroom anchors; emit an honest cycle report."""
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "products" / "catalog.json"
SHOWROOM = ROOT / "showroom" / "index.html"
OUT = ROOT / "generated" / "production" / "production-report.json"
REQUIRED = {"id", "slug", "name", "category", "status", "price", "deliverables", "qc_gate", "demo"}
ALLOWED_STATUSES = {"preview", "production-ready", "blocked"}


def main():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    html = SHOWROOM.read_text(encoding="utf-8")
    products = data.get("products", [])
    ids, slugs, anchors, errors = set(), set(), set(), []
    for i, product in enumerate(products):
        prefix = f"products[{i}]"
        missing = REQUIRED - product.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
        pid, slug = product.get("id"), product.get("slug")
        if not pid or pid in ids:
            errors.append(f"{prefix} missing or duplicate product id: {pid!r}")
        if not slug or slug in slugs:
            errors.append(f"{prefix} missing or duplicate slug: {slug!r}")
        ids.add(pid)
        slugs.add(slug)
        if product.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{pid}: unsupported status {product.get('status')!r}")
        if not isinstance(product.get("deliverables"), list) or not product.get("deliverables"):
            errors.append(f"{pid}: deliverables must be a non-empty list")
        if not product.get("qc_gate"):
            errors.append(f"{pid}: no QC gate")
        price = product.get("price", {})
        if not isinstance(price, dict) or not {"amount", "currency", "label"} <= price.keys():
            errors.append(f"{pid}: price must include amount, currency and label")
        demo = product.get("demo", "")
        anchor = demo.split("#", 1)[1] if "#" in demo else ""
        if not anchor:
            errors.append(f"{pid}: demo URL must include a product anchor")
        elif anchor in anchors:
            errors.append(f"{pid}: duplicate demo anchor #{anchor}")
        else:
            anchors.add(anchor)
            if f'id="{anchor}"' not in html and f"id='{anchor}'" not in html:
                errors.append(f"{pid}: showroom anchor #{anchor} not found in showroom/index.html")

    report = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "cycle": "catalogue-and-showroom-production-readiness",
        "catalogue_count": len(products),
        "unique_ids": len(ids),
        "unique_slugs": len(slugs),
        "showroom_anchor_count": len(anchors),
        "preview_count": sum(p.get("status") == "preview" for p in products),
        "production_ready_count": sum(p.get("status") == "production-ready" for p in products),
        "errors": errors,
        "result": "PASS" if not errors else "FAIL",
        "limitations": [
            "This cycle validates catalogue structure and showroom anchors; it does not create new product code.",
            "A PASS is a metadata/link-integrity result, not independent product certification or commercial release approval.",
            "Production-ready status requires product-specific executable tests, evidence artifacts and release-owner approval.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
