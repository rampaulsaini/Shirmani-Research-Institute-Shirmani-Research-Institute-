"""Shared fail-closed contract for publishing deterministic product QC state."""
from __future__ import annotations

import json
from pathlib import Path

PASS_STATE = "QC_PASS_READY_FOR_DISPATCH"

PARTIAL_PASS_STATE = "QC_PARTIAL_PASS"
PENDING_PRODUCTION_STATE = "QC_PENDING_PRODUCTION"
REVIEW_REQUIRED_STATE = "QC_REVIEW_REQUIRED"


def qc_release_state(
    catalog_count: object,
    produced_count: object,
    passed_count: object,
    failed_count: object,
    has_errors: bool = False,
) -> str:
    """Never mistake partial coverage for full-catalog QC."""
    counts = (catalog_count, produced_count, passed_count, failed_count)
    if any(type(value) is not int or value < 0 for value in counts):
        return REVIEW_REQUIRED_STATE
    catalog_total, produced_total, passed_total, failed_total = counts
    if (
        has_errors
        or failed_total > 0
        or catalog_total <= 0
        or produced_total > catalog_total
        or passed_total > produced_total
    ):
        return REVIEW_REQUIRED_STATE
    if produced_total == catalog_total and passed_total == catalog_total:
        return PASS_STATE
    if produced_total > 0 and passed_total == produced_total:
        return PARTIAL_PASS_STATE
    return PENDING_PRODUCTION_STATE


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
    if not isinstance(payload, dict):
        return {}, False
    return payload, qc_passed(payload, catalog_count)


def _nonnegative_int_or_none(value: object) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) and value >= 0 else None


def sync_public_qc_state(root: Path, catalog_count: int) -> bool:
    """Publish QC counters to existing status files; never claim dispatch, sales, or payment."""
    root = Path(root)
    qc, passed = read_qc(root, catalog_count)
    qc_failed = _nonnegative_int_or_none(qc.get("qc_failed"))
    qc_passed_count = _nonnegative_int_or_none(qc.get("qc_passed"))
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
                "PRODUCTION_STATE_UNAVAILABLE" if not pending_valid
                else "QC_PASSED_AWAITING_DISPATCH" if passed
                else "QC_REVIEW_REQUIRED" if qc.get("release_state") == "QC_REVIEW_REQUIRED"
                else "PRODUCTION_COMPLETE_CURRENT_CATALOG" if pending_raw == 0
                else "PRODUCTION_IN_PROGRESS"
            ),
        })
        live_path.write_text(json.dumps(live, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return passed
