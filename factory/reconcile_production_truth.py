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
produced = int(overlay.get("produced_count", 0))
pending = max(0, catalog - produced)
scale_target = 5000
state = {
    "schema_version": 1,
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "production_first": True,
    "catalog_identities": catalog,
    "concrete_repository_assets": produced,
    "current_catalog_pending": pending,
    "five_thousand_scale_target": scale_target,
    "remaining_to_scale_target": max(0, scale_target - produced),
    "concrete_materialization_percent_of_catalog": round((produced / catalog) * 100, 2) if catalog else 0,
    "concrete_materialization_percent_of_scale_target": round((produced / scale_target) * 100, 2),
    "module_products_generated": produced,
    "dispatch_released": 0,
    "sales_claimed": 0,
    "payment_claimed": 0,
    "independent_verification_claimed": 0,
    "state": "PRODUCTION_COMPLETE_CURRENT_CATALOG" if pending == 0 else "PRODUCTION_IN_PROGRESS",
    "rule": "Concrete repository-bound artifacts are production evidence; workflow execution is not counted as a product.",
    "next_work": [
        "continue expansion toward 5,000 concrete products",
        "deepen product-specific modules and demos",
        "feed public customer reviews into the quality backlog",
        "keep QC, dispatch, sales and research verification as separate downstream states",
    ],
}
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(state, ensure_ascii=False))
