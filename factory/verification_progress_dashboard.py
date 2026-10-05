#!/usr/bin/env python3
"""Generate the authoritative fail-closed SHIRMANI verification dashboard."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "generated/independent-verification-records.json"
PREPARATION_STATUS = ROOT / "generated/independent-verification-status.json"
TARGET_CONFIG = ROOT / "config/independent-verification-target.json"
OUT = ROOT / "generated/verification-progress-dashboard.json"
OUT_MD = ROOT / "generated/verification-progress-dashboard.md"

def target_value() -> int:
    data = read_json(TARGET_CONFIG)
    target = int(data["verification_target"])
    if target <= 0:
        raise SystemExit("verification_target must be positive")
    return target

def read_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing required status file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def bar(percent: float, width: int = 30) -> str:
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)

def validate_preparation_status(prep: dict, target: int) -> int:
    if prep.get("version") != 1:
        raise SystemExit("PREPARATION_STATUS_SCHEMA_VERSION_UNSUPPORTED")
    if prep.get("state") != "NOT_VERIFIED":
        raise SystemExit("PREPARATION_STATUS_STATE_MUST_REMAIN_NOT_VERIFIED")
    if prep.get("promotion_eligible") != 0:
        raise SystemExit("PREPARATION_STATUS_PROMOTION_ELIGIBLE_MUST_BE_ZERO")

    integer_fields = (
        "queue_total", "queued_records", "prepared_review_records",
        "reviewed_records", "verified_records", "packet_qc_checked_items",
        "queue_qc_error_count", "registry_qc_error_count",
        "promotion_qc_error_count"
    )
    for field in integer_fields:
        value = prep.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise SystemExit(f"PREPARATION_STATUS_INVALID_{field.upper()}")

    queue_total = prep["queue_total"]
    queued = prep["queued_records"]
    prepared = prep["prepared_review_records"]
    reviewed = prep["reviewed_records"]
    verified = prep["verified_records"]

    if not (prepared <= queued <= queue_total <= target):
        raise SystemExit("PREPARATION_STATUS_QUEUE_INVARIANT_FAILED")
    if not (verified <= reviewed <= prepared):
        raise SystemExit("PREPARATION_STATUS_REVIEW_INVARIANT_FAILED")
    if prep.get("prepared_percent") != round(prepared / target * 100, 6):
        raise SystemExit("PREPARATION_STATUS_PREPARED_PERCENT_MISMATCH")
    expected_verified_pct = round(verified / queue_total * 100, 6) if queue_total else 0
    if prep.get("verified_percent_of_queue") != expected_verified_pct:
        raise SystemExit("PREPARATION_STATUS_VERIFIED_PERCENT_MISMATCH")
    return prepared

def main() -> int:
    data = read_json(RECORDS)
    prep = read_json(PREPARATION_STATUS)
    TARGET = target_value()
    records = data.get("records", [])
    prepared = validate_preparation_status(prep, TARGET)
    if not isinstance(records, list):
        raise SystemExit("records must be a list")

    if prepared < 0 or prepared > TARGET:
        raise SystemExit("PREPARED_PACKET_COUNT_OUT_OF_RANGE")
    verified = sum(1 for r in records
                   if r.get("reviewer_decision", {}).get("decision") == "VERIFIED"
                   and r.get("status") == "VERIFIED")
    reviewed = sum(1 for r in records
                   if r.get("reviewer_decision", {}).get("decision")
                   in {"VERIFIED", "NOT_VERIFIED", "CONTRADICTED", "INCONCLUSIVE"})
    evidence_supported = sum(1 for r in records if r.get("status") == "EVIDENCE-SUPPORTED")

    # The authoritative source is the records list. Never report a synthetic
    # queued/prepared count that is larger than the actual record registry.
    if verified > reviewed or reviewed > prepared or prepared > TARGET:
        raise SystemExit("Verification counters violate monotonic invariants.")
    if len(records) > prepared:
        raise SystemExit("REVIEW_RECORDS_EXCEED_PREPARED_PACKETS")

    remaining = TARGET - verified
    prepared_pct = round(prepared / TARGET * 100, 6)
    reviewed_pct = round(reviewed / TARGET * 100, 6)
    verified_pct = round(verified / TARGET * 100, 6)
    remaining_pct = round(remaining / TARGET * 100, 6)
    generated = datetime.now(timezone.utc).isoformat()

    dashboard = {
        "generated_at": generated,
        "method": "authoritative independent-verification records; fail-closed",
        "target": TARGET,
        "records": {
            "target": TARGET, "prepared": prepared, "reviewed": reviewed,
            "verified": verified, "remaining_to_verified_target": remaining,
            "evidence_supported": evidence_supported,
            "source_registry_records": len(records),
            "prepared_review_packets": prepared
        },
        "percent": {
            "prepared_of_target": prepared_pct, "reviewed_of_target": reviewed_pct,
            "independently_verified_of_target": verified_pct,
            "remaining_of_target": remaining_pct
        },
        "automation_state": {
            "independent_verification_required": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "independent_reviewer_decision_required": True
        },
        "next_gate": (
            "Complete independent review for prepared records; each VERIFIED "
            "promotion requires evidence, counter-evidence, reproducible test, "
            "reviewer provenance, timestamp, and audit."
            if verified < TARGET else "Target reached."
        )
    }
    OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = f"""# ꙰ SHIRMANI Verification Progress Dashboard

Generated: {generated}

## Authoritative target

**{verified:,} / {TARGET:,} independently VERIFIED ({verified_pct:g}%)**

### Graph map

- Prepared records: **{prepared:,}/{TARGET:,} ({prepared_pct:g}%)**  {bar(prepared_pct)}
- Reviewed records: **{reviewed:,}/{TARGET:,} ({reviewed_pct:g}%)**  {bar(reviewed_pct)}
- Independently VERIFIED: **{verified:,}/{TARGET:,} ({verified_pct:g}%)**  {bar(verified_pct)}
- Remaining to target: **{remaining:,}/{TARGET:,} ({remaining_pct:g}%)**  {bar(remaining_pct)}

## Current prepared set

- Source registry records (actual review records): **{len(records):,}**
- Prepared review-packet records: **{prepared:,}**
- Evidence-supported: **{evidence_supported:,}**
- Reviewed: **{reviewed:,}**
- Independently VERIFIED: **{verified:,}**

## Control state

- Automation may prepare: **YES**
- Automation may declare VERIFIED: **NO**
- Independent review required: **YES**
- Fail-closed promotion: **ENFORCED**

## Integrity rule

Workflow success, queue generation, evidence collection, generated packets,
or review-slot creation do not by themselves constitute independent
verification. VERIFIED requires an explicit independent-review decision with
the defined evidence, counter-evidence, reproducible test/observation,
reviewer provenance, timestamp, and audit record.

## Next gate

{dashboard["next_gate"]}
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
