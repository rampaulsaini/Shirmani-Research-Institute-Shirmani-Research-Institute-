#!/usr/bin/env python3
"""Fail-safe stop gate for the 5,000-item production target.

This gate skips generation only when the catalog, concrete assets, QR assets,
and deterministic QC all meet the published target. Missing/incomplete counts
do not qualify as complete, so production can continue to fill real gaps.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

STATE_PATH = Path("generated/live-production-state.json")


def target_complete(state: dict[str, Any]) -> bool:
    target = int(state.get("five_thousand_scale_target", 5000))
    catalog = int(state.get("catalog_identities", state.get("module_products_generated", 0)))
    concrete = int(state.get("concrete_repository_assets", 0))
    qr_assets = int(state.get("product_qr_assets", 0))
    return (
        target > 0
        and catalog >= target
        and concrete >= target
        and qr_assets >= target
        and state.get("qc_state") == "QC_PASSED"
        and int(state.get("qc_passed", 0)) >= target
        and int(state.get("qc_failed", 0)) == 0
    )


def main() -> int:
    if not STATE_PATH.is_file():
        raise SystemExit(f"Required production state is missing: {STATE_PATH}")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    complete = target_complete(state)
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"complete={'true' if complete else 'false'}\n")
    if complete:
        print("Production target already complete; skipping duplicate generation.")
    else:
        print("Production target has a validated gap; bounded production may continue.")
    print(json.dumps({
        "complete": complete,
        "target": int(state.get("five_thousand_scale_target", 5000)),
        "catalog_identities": int(state.get("catalog_identities", state.get("module_products_generated", 0))),
        "concrete_repository_assets": int(state.get("concrete_repository_assets", 0)),
        "product_qr_assets": int(state.get("product_qr_assets", 0)),
        "qc_state": state.get("qc_state"),
        "qc_passed": int(state.get("qc_passed", 0)),
        "qc_failed": int(state.get("qc_failed", 0)),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
