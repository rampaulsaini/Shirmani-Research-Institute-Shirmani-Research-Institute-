#!/usr/bin/env python3
"""Fail the public production build when its published truth files disagree."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"


def read_json(name: str) -> dict:
    path = GEN / name
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"PUBLIC_PRODUCTION_GATE_FAIL: missing/empty generated/{name}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"PUBLIC_PRODUCTION_GATE_FAIL: invalid JSON generated/{name}: {exc}")
    if not isinstance(value, dict):
        raise SystemExit(f"PUBLIC_PRODUCTION_GATE_FAIL: generated/{name} must be a JSON object")
    return value


def fresh_timestamp(value: object, name: str) -> None:
    if not isinstance(value, str) or not value:
        raise SystemExit(f"PUBLIC_PRODUCTION_GATE_FAIL: generated/{name} has no generated_at")
    try:
        timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError("timestamp must include timezone")
    except ValueError as exc:
        raise SystemExit(f"PUBLIC_PRODUCTION_GATE_FAIL: invalid generated_at in {name}: {exc}")
    age = (datetime.now(timezone.utc) - timestamp.astimezone(timezone.utc)).total_seconds()
    if age < -300 or age > 1800:
        raise SystemExit(
            f"PUBLIC_PRODUCTION_GATE_FAIL: {name} is stale/future-dated "
            f"(age_seconds={int(age)})"
        )


def main() -> None:
    target = int(os.environ.get("PRODUCT_TARGET", "5000"))
    catalog = read_json("1000-digital-products.json")
    status = read_json("concrete-product-asset-status.json")
    live = read_json("live-production-state.json")
    overlay = read_json("public-production-asset-overlay.json")
    qc = read_json("product-qc-gate.json")
    import sys
    sys.path.insert(0, str(ROOT))
    from factory.qc_state_contract import qc_passed
    expected_qc_state = "QC_PASSED" if qc_passed(qc, target) else ("QC_REVIEW_REQUIRED" if qc.get("release_state") == "QC_REVIEW_REQUIRED" else "READY_FOR_QC")
    if status.get("state") != expected_qc_state:
        raise SystemExit(f"PUBLIC_PRODUCTION_GATE_FAIL: concrete status state={status.get('state')!r} expected {expected_qc_state}")
    if live.get("qc_state") != expected_qc_state:
        raise SystemExit(f"PUBLIC_PRODUCTION_GATE_FAIL: live qc_state={live.get('qc_state')!r} expected {expected_qc_state}")
    if qc.get("dispatch_default") != "NO" or live.get("dispatch_released", 0) != 0:
        raise SystemExit("PUBLIC_PRODUCTION_GATE_FAIL: QC must not imply dispatch release")

    products = catalog.get("products")
    if not isinstance(products, list) or catalog.get("product_count") != target or len(products) != target:
        raise SystemExit(
            f"PUBLIC_PRODUCTION_GATE_FAIL: catalog count mismatch "
            f"(declared={catalog.get('product_count')}, rows={len(products) if isinstance(products, list) else 'invalid'}, target={target})"
        )

    ids = [p.get("id") for p in products if isinstance(p, dict)]
    if len(ids) != target or any(not isinstance(pid, str) or not pid for pid in ids) or len(set(ids)) != target:
        raise SystemExit("PUBLIC_PRODUCTION_GATE_FAIL: product IDs missing, invalid, or duplicated")

    asset_paths = []
    missing = []
    for product in products:
        asset = product.get("asset")
        if not isinstance(asset, str) or not asset:
            missing.append(str(product.get("id", "<unknown>")) + ":missing asset path")
            continue
        path = (ROOT / asset).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file() or path.stat().st_size == 0:
            missing.append(f"{product.get('id', '<unknown>')}:{asset}")
        else:
            asset_paths.append(asset)

    if missing:
        sample = ", ".join(missing[:10])
        raise SystemExit(
            f"PUBLIC_PRODUCTION_GATE_FAIL: {len(missing)} catalog assets missing/invalid; sample={sample}"
        )

    overlay_products = overlay.get("products")
    if not isinstance(overlay_products, list):
        raise SystemExit("PUBLIC_PRODUCTION_GATE_FAIL: overlay products must be a list")
    overlay_ids = [p.get("id") for p in overlay_products if isinstance(p, dict)]
    if len(overlay_ids) != len(set(overlay_ids)):
        raise SystemExit("PUBLIC_PRODUCTION_GATE_FAIL: duplicate IDs in production overlay")
    overlay_count = len(overlay_products)
    actual_count = len(asset_paths)
    declared_counts = {
        "concrete-product-asset-status.product_assets": status.get("product_assets"),
        "live-production-state.concrete_repository_assets": live.get("concrete_repository_assets"),
        "live-production-state.public_production_assets": live.get("public_production_assets"),
        "public-production-asset-overlay.produced_count": overlay.get("produced_count"),
    }
    expected = {
        "concrete-product-asset-status.product_assets": actual_count,
        "live-production-state.concrete_repository_assets": actual_count,
        "live-production-state.public_production_assets": overlay_count,
        "public-production-asset-overlay.produced_count": overlay_count,
    }
    mismatches = [
        f"{key}={value!r} expected {expected[key]}"
        for key, value in declared_counts.items()
        if value != expected[key]
    ]
    if overlay_count != actual_count:
        mismatches.append(f"overlay rows={overlay_count} expected {actual_count}")
    if overlay.get("product_count") != target:
        mismatches.append(f"overlay product_count={overlay.get('product_count')!r} expected {target}")
    if live.get("catalog_identities") != target:
        mismatches.append(f"live catalog_identities={live.get('catalog_identities')!r} expected {target}")
    if live.get("current_catalog_pending") != max(0, target - actual_count):
        mismatches.append("live current_catalog_pending does not match concrete asset count")
    if live.get("remaining_to_scale_target") != max(0, target - actual_count):
        mismatches.append("live remaining_to_scale_target does not match concrete asset count")
    if mismatches:
        raise SystemExit("PUBLIC_PRODUCTION_GATE_FAIL: " + "; ".join(mismatches))

    for filename, payload in (
        ("1000-digital-products.json", catalog),
        ("concrete-product-asset-status.json", status),
        ("live-production-state.json", live),
        ("public-production-asset-overlay.json", overlay),
        ("product-qc-gate.json", qc),
    ):
        fresh_timestamp(payload.get("generated_at"), filename)

    print(json.dumps({
        "gate": "PUBLIC_PRODUCTION_TRUTH_SMOKE",
        "result": "PASS",
        "catalog_target": target,
        "unique_product_ids": len(set(ids)),
        "concrete_product_files": actual_count,
        "overlay_product_rows": overlay_count,
        "dispatch_released": live.get("dispatch_released", 0),
        "sales_claimed": live.get("sales_claimed", 0),
        "payment_claimed": live.get("payment_claimed", 0),
        "independent_verification_claimed": live.get("independent_verification_claimed", 0),
        "truth_boundary": "asset existence is not QC, dispatch, payment, or independent verification",
    }, ensure_ascii=False))
    

if __name__ == "__main__":
    main()
