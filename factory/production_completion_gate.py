#!/usr/bin/env python3
"""Fail-safe stop gate: do not regenerate the completed 5,000-item catalogue."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

STATE_PATH = Path("generated/live-production-state.json")
QC_PATH = Path("generated/product-qc-gate.json")
PASS_STATE = "QC_PASS_READY_FOR_DISPATCH"


def qc_evidence_complete(qc: dict[str, Any], target: int) -> bool:
    integrity = qc.get("integrity")
    return (
        target > 0
        and isinstance(integrity, dict)
        and qc.get("catalog_count") == target
        and qc.get("produced_count") == target
        and qc.get("qc_passed") == target
        and qc.get("qc_failed") == 0
        and qc.get("release_state") == PASS_STATE
        and integrity.get("deterministic_qc") is True
        and integrity.get("sale_claim") is False
    )


def target_complete(state: dict[str, Any], qc: dict[str, Any]) -> bool:
    try:
        target = int(state.get("five_thousand_scale_target", 5000))
        catalog = int(state.get("catalog_identities", state.get("module_products_generated", 0)))
        concrete = int(state.get("concrete_repository_assets", 0))
        qr_assets = int(state.get("product_qr_assets", 0))
    except (TypeError, ValueError):
        return False
    return (
        target > 0
        and catalog >= target
        and concrete >= target
        and qr_assets >= target
        and qc_evidence_complete(qc, target)
    )


def main() -> int:
    if not STATE_PATH.is_file() or not QC_PATH.is_file():
        raise SystemExit("Required canonical production state or QC evidence is missing; fail closed.")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    qc = json.loads(QC_PATH.read_text(encoding="utf-8"))
    complete = target_complete(state, qc)
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"complete={'true' if complete else 'false'}\n")
    print(json.dumps({
        "complete": complete,
        "target": state.get("five_thousand_scale_target", 5000),
        "catalog_identities": state.get("catalog_identities", 0),
        "concrete_repository_assets": state.get("concrete_repository_assets", 0),
        "product_qr_assets": state.get("product_qr_assets", 0),
        "canonical_qc_state": qc.get("release_state"),
        "qc_passed": qc.get("qc_passed", 0),
        "qc_failed": qc.get("qc_failed", 0),
        "dispatch_released": state.get("dispatch_released", 0),
        "sales_claimed": state.get("sales_claimed", 0),
        "payment_claimed": state.get("payment_claimed", 0),
    }, ensure_ascii=False))
    print("Target complete: skip duplicate production." if complete else "Validated gap: bounded production may continue.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
