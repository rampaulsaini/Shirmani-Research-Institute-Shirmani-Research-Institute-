#!/usr/bin/env python3
"""Synchronize concrete product assets without overstating commercial readiness."""
from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
CAT = GEN / "1000-digital-products.json"
PROD = ROOT / "products" / "production"


def qc(pid: str) -> str:
    return "QC-PROD-" + hashlib.sha256((pid + "|SHIRMANI").encode()).hexdigest()[:12].upper()


def has_approved_price(product: dict) -> bool:
    """Only an explicit approval plus a positive finite price enables ordering."""
    if product.get("commercial_status") != "PRICE_APPROVED":
        return False
    try:
        amount = float(product.get("price_inr"))
    except (TypeError, ValueError):
        return False
    return math.isfinite(amount) and amount > 0


def build_product_row(product: dict, artifact_url: str, produced_at: str | None = None) -> dict:
    """Build a public row with clear identity and a fail-closed commercial state."""
    pid = product["id"]
    approved = has_approved_price(product)
    name = product.get("name") or product.get("title") or product.get("product_name") or product.get("label") or pid
    row = {
        "id": pid,
        "name": name,
        "description": product.get("description") or product.get("summary") or "",
        "family": product.get("family") or product.get("category") or "Unclassified",
        "engine": product.get("engine") or "Not recorded",
        "production_state": "PRODUCED",
        "sale_state": "READY_FOR_ORDER" if approved else "QUOTE_REQUIRED",
        "commercial_status": "PRICE_APPROVED" if approved else "QUOTE_REQUIRED",
        "payment_enabled": approved,
        "artifact_url": artifact_url,
        "production_batch": "PUBLIC-PRODUCTION-SYNC",
        "produced_at": produced_at or datetime.now(timezone.utc).isoformat(),
        "qc_code": product.get("qc_code") or qc(pid),
        "gate_no": product.get("gate_no") or f"GATE-{int(pid.split('-')[-1]):04d}",
        "dispatch_no": "NO",
        "price_inr": product.get("price_inr"),
        "offer_price_inr": product.get("offer_price_inr"),
        "offer": product.get("offer"),
        "guarantee": product.get("guarantee"),
        "packing": product.get("packing"),
    }
    return row


def main():
    data = json.loads(CAT.read_text(encoding="utf-8"))
    products = data.get("products", [])
    rows = []
    missing = []
    stamp = datetime.now(timezone.utc).isoformat()

    for product in products:
        pid = product["id"]
        asset = ROOT / (product.get("asset") or f"products/production/{pid.lower()}.html")
        if not asset.is_file():
            missing.append(pid)
            continue
        rows.append(build_product_row(product, str(asset.relative_to(ROOT)), stamp))

    overlay = {
        "schema_version": 2,
        "generated_at": stamp,
        "architecture": ["INSTITUTE", "FACTORY", "QC", "SHOWROOM_SALE"],
        "production_first": True,
        "verification_is_downstream": True,
        "product_count": len(products),
        "produced_count": len(rows),
        "remaining_count": len(products) - len(rows),
        "missing_asset_count": len(missing),
        "products": rows,
    }
    (GEN / "concrete-production-overlay.json").write_text(
        json.dumps(overlay, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    registry = {
        "schema_version": 4,
        "generated_at": stamp,
        "architecture": ["INSTITUTE", "FACTORY", "QC", "SHOWROOM_SALE"],
        "production_first": True,
        "verification_is_downstream": True,
        "catalog_count": len(products),
        "produced_count": len(rows),
        "remaining_count": len(products) - len(rows),
        "engine_count": data.get("engine_count", 0),
        "family_count": len(data.get("family_definitions", [])),
        "products": rows,
    }
    (GEN / "production-registry.json").write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    status = {
        "generated_at": stamp,
        "catalog_count": len(products),
        "produced": len(rows),
        "remaining": len(products) - len(rows),
        "qc_ready": len(rows),
        "offered": sum(row["sale_state"] == "READY_FOR_ORDER" for row in rows),
        "quote_required": sum(row["sale_state"] == "QUOTE_REQUIRED" for row in rows),
        "dispatch_no": len(rows),
        "dispatch_yes": 0,
        "production_first": True,
        "verification_scope": "DOWNSTREAM_PRODUCT_RESULT",
        "missing_assets": missing[:1000],
    }
    (GEN / "production-status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "catalog": len(products),
        "produced": len(rows),
        "ready_for_order": status["offered"],
        "quote_required": status["quote_required"],
        "remaining": len(products) - len(rows),
        "missing_assets": len(missing),
    }))


if __name__ == "__main__":
    main()
