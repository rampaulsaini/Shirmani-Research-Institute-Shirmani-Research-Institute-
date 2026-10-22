#!/usr/bin/env python3
"""Reconcile the public production state from the concrete production overlay.

The concrete overlay is the source-derived production surface. This script never
turns workflow execution into a product and never changes downstream QC,
dispatch, sales, payment, or independent-verification claims.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
overlay_path = ROOT / "generated" / "concrete-production-overlay.json"
state_path = ROOT / "generated" / "live-production-state.json"

overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
catalog = int(overlay.get("product_count", 0))
overlay_rows = len(overlay.get("products", []))
# Count actual files in this checkout; do not trust stale generated totals as filesystem evidence.
concrete_assets = len(list((ROOT / "products" / "concrete").glob("*.html")))
browser_assets = len(list((ROOT / "products" / "production").glob("*.html")))
visual_assets = len(list((ROOT / "products" / "visuals").glob("*.svg")))
qr_assets = len(list((ROOT / "products" / "visuals" / "qr").glob("*.svg")))
pending = max(0, catalog - concrete_assets)
scale_target = 5000
state = {
    "schema_version": 3,
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "production_first": True,
    "catalog_identities": catalog,
    "concrete_repository_assets": concrete_assets,
    "production_browser_assets": browser_assets,
    "public_4k_visual_assets": visual_assets,
    "product_qr_assets": qr_assets,
    "overlay_product_records": overlay_rows,
    "current_catalog_pending": pending,
    "five_thousand_scale_target": scale_target,
    "remaining_to_scale_target": max(0, scale_target - concrete_assets),
    "concrete_materialization_percent_of_catalog": round((concrete_assets / catalog) * 100, 2) if catalog else 0,
    "concrete_materialization_percent_of_scale_target": round((concrete_assets / scale_target) * 100, 2),
    "module_products_generated": browser_assets,
    "dispatch_released": 0,
    "sales_claimed": 0,
    "payment_claimed": 0,
    "independent_verification_claimed": 0,
    "state": "PRODUCTION_COMPLETE_CURRENT_CATALOG" if pending == 0 else "PRODUCTION_IN_PROGRESS",
    "qc_state": "READY_FOR_QC",
    "truth_boundary": "Concrete assets, overlay rows, visual assets, QC, dispatch, sales, payment and independent verification are separate states.",
    "rule": "Filesystem counts are measured from repository files; overlay rows are reported separately and workflow execution is not counted as a product.",
}
existing = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else None
# Do not create a commit when the production-derived values have not changed.
if existing:
    comparable_existing = dict(existing)
    comparable_state = dict(state)
    comparable_existing.pop("generated_at", None)
    comparable_state.pop("generated_at", None)
    if comparable_existing == comparable_state:
        state = existing
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
from factory.qc_state_contract import sync_public_qc_state
sync_public_qc_state(ROOT, catalog)
state = json.loads(state_path.read_text(encoding="utf-8"))
print(json.dumps(state, ensure_ascii=False))
