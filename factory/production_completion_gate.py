#!/usr/bin/env python3
"""Fail-safe stop gate for the 5,000-item production target.

The public summary can lag or regress during concurrent scheduled workflows.
Use the canonical product QC gate as the authority; never regenerate the
catalog solely because the summary's qc_state is stale.
"""
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
    target = int(state.get("five_thousand_scale_target", 5000))
    catalog = int(state.get("catalog_identities", state.get("module_products_generated", 0)))
    concrete = int(state.get("concrete_repository_assets", 0))
    qr_assets = int(state.get("product_qr_assets", 0))
    return (
        target > 0
        and catalog >= target
        and concrete >= target
        and qr_assets >= target
        and qc_evidence_complete(qc, target)
    )


def main() -> int:
    if not STATE_PATH.is_file():
        raise SystemExit(f"Required production state is missing: {STATE_PATH}")
    if not QC_PATH.is_file():
        raise SystemExit(f"Required canonical QC evidence is missing: {QC_PATH}")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    qc = json.loads(QC_PATH.read_text(encoding="utf-8"))
    complete = target_complete(state, qc)
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"complete={'true' if complete else 'false'}\\n")
    if complete:
        print("Production target already complete from canonical QC evidence; skipping duplicate generation.")
    else:
        print("Production target/QC evidence has a validated gap; bounded production may continue.")
    print(json.dumps({
        "complete": complete,
        "target": int(state.get("five_thousand_scale_target", 5000)),
        "catalog_identities": int(state.get("catalog_identities", state.get("module_products_generated", 0))),
        "concrete_repository_assets": int(state.get("concrete_repository_assets", 0)),
        "product_qr_assets": int(state.get("product_qr_assets", 0)),
        "summary_qc_state": state.get("qc_state"),
        "canonical_qc_state": qc.get("release_state"),
        "qc_passed": qc.get("qc_passed", 0),
        "qc_failed": qc.get("qc_failed", 0),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
