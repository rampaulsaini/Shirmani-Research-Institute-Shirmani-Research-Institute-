"""Shared fail-closed contract for publishing deterministic product QC state."""
from __future__ import annotations

import json
from pathlib import Path

PASS_STATE = "QC_PASS_READY_FOR_DISPATCH"


def qc_passed(qc: object, catalog_count: int) -> bool:
    if (
        not isinstance(qc, dict)
        or type(catalog_count) is not int
        or catalog_count <= 0
    ):
        return False
    integrity = qc.get("integrity")
    if not isinstance(integrity, dict):
        return False
    counts = (qc.get("catalog_count"), qc.get("produced_count"), qc.get("qc_passed"))
    if any(type(value) is not int or value < 0 for value in counts):
        return False
    if type(qc.get("qc_failed")) is not int or qc.get("qc_failed") < 0:
        return False
    return (
        qc.get("catalog_count") == catalog_count
        and qc.get("produced_count") == catalog_count
        and qc.get("qc_passed") == catalog_count
        and qc.get("qc_failed") == 0
        and qc.get("release_state") == PASS_STATE
        and integrity.get("deterministic_qc") is True
        and integrity.get("sale_claim") is False
    )


def read_qc(root: Path, catalog_count: int) -> tuple[dict, bool]:
    path = Path(root) / "generated" / "product-qc-gate.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {}, False
    return payload, qc_passed(payload, catalog_count)


def _nonnegative_int_or_none(value: object) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) and value >= 0 else None


def sync_public_qc_state(root: Path, catalog_count: int) -> bool:
    """Publish QC counters to existing status files; never claim dispatch, sales, or payment."""
    root = Path(root)
    qc, passed = read_qc(root, catalog_count)
    qc_failed = _nonnegative_int_or_none(qc.get("qc_failed"))
    qc_passed_count = _nonnegative_int_or_none(qc.get("qc_passed")) if passed else 0
    produced_count = _nonnegative_int_or_none(qc.get("produced_count"))
    state = (
        "QC_PASSED" if passed
        else "QC_REVIEW_REQUIRED" if qc.get("release_state") == "QC_REVIEW_REQUIRED"
        else "READY_FOR_QC"
    )
    gen = root / "generated"

    status_path = gen / "concrete-product-asset-status.json"
    if status_path.is_file():
        status = json.loads(status_path.read_text(encoding="utf-8"))
        status.update({
            "state": state,
            "qc_state": state,
            "qc_catalog_count": catalog_count,
            "qc_produced_count": produced_count,
            "qc_passed": qc_passed_count,
            "qc_failed": qc_failed,
            "qc_generated_at": qc.get("generated_at"),
            "dispatch": "NO",
        })
        status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    live_path = gen / "live-production-state.json"
    if live_path.is_file():
        live = json.loads(live_path.read_text(encoding="utf-8"))
        pending_raw = live.get("current_catalog_pending", 0)
        pending_valid = (
            isinstance(pending_raw, int)
            and not isinstance(pending_raw, bool)
            and pending_raw >= 0
        )
        live.update({
            "qc_state": state,
            "qc_catalog_count": catalog_count,
            "qc_produced_count": produced_count,
            "qc_passed": qc_passed_count,
            "qc_failed": qc_failed,
            "qc_state_source": "generated/product-qc-gate.json",
            "state": (
                "QC_PASSED_AWAITING_DISPATCH" if passed
                else "QC_REVIEW_REQUIRED" if qc.get("release_state") == "QC_REVIEW_REQUIRED"
                else "PRODUCTION_COMPLETE_CURRENT_CATALOG" if pending_valid and pending_raw == 0
                else "PRODUCTION_IN_PROGRESS" if pending_valid
                else "PRODUCTION_STATE_UNAVAILABLE"
            ),
        })
        live_path.write_text(json.dumps(live, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return passed
