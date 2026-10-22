"""Shared fail-closed contract for publishing deterministic product QC state."""
from __future__ import annotations
import json
from pathlib import Path

PASS_STATE = "QC_PASS_READY_FOR_DISPATCH"


def qc_passed(qc: object, catalog_count: int) -> bool:
    if not isinstance(qc, dict) or catalog_count <= 0:
        return False
    return (
        qc.get("catalog_count") == catalog_count
        and qc.get("produced_count") == catalog_count
        and qc.get("qc_passed") == catalog_count
        and qc.get("qc_failed") == 0
        and qc.get("release_state") == PASS_STATE
        and qc.get("integrity", {}).get("deterministic_qc") is True
        and qc.get("integrity", {}).get("sale_claim") is False
    )


def read_qc(root: Path, catalog_count: int) -> tuple[dict, bool]:
    path = Path(root) / "generated" / "product-qc-gate.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {}, False
    return payload, qc_passed(payload, catalog_count)


def sync_public_qc_state(root: Path, catalog_count: int) -> bool:
    """Update existing public status files only; never claim dispatch, sales, or payment."""
    root = Path(root)
    qc, passed = read_qc(root, catalog_count)
    state = "QC_PASSED" if passed else "READY_FOR_QC"
    gen = root / "generated"
    status_path = gen / "concrete-product-asset-status.json"
    if status_path.is_file():
        status = json.loads(status_path.read_text(encoding="utf-8"))
        status.update({
            "state": state,
            "qc_passed": qc.get("qc_passed", 0) if passed else 0,
            "qc_failed": qc.get("qc_failed", 0) if passed else qc.get("qc_failed", 0),
            "qc_generated_at": qc.get("generated_at"),
            "dispatch": "NO",
        })
        status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    live_path = gen / "live-production-state.json"
    if live_path.is_file():
        live = json.loads(live_path.read_text(encoding="utf-8"))
        live.update({
            "qc_state": state,
            "state": "QC_PASSED_AWAITING_DISPATCH" if passed else (
                "PRODUCTION_COMPLETE_CURRENT_CATALOG"
                if int(live.get("current_catalog_pending", 0)) == 0
                else "PRODUCTION_IN_PROGRESS"
            ),
            "dispatch_released": 0,
            "sales_claimed": 0,
            "payment_claimed": 0,
            "independent_verification_claimed": 0,
        })
        live_path.write_text(json.dumps(live, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return passed
