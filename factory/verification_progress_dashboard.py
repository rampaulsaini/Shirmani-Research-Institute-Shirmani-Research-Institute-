#!/usr/bin/env python3
"""Generate the authoritative fail-closed SHIRMANI verification dashboard."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD_DIR = ROOT / "generated" / "independent-verification-records"
SCHEMA_PATH = ROOT / "schemas" / "supreme-independent-verification-record.schema.json"
TARGET_CONFIG = ROOT / "config" / "independent-verification-target.json"
OUT = ROOT / "generated" / "verification-progress-dashboard.json"
OUT_MD = ROOT / "generated" / "verification-progress-dashboard.md"
STATES = {"REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"}

def read_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing required status file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def target_value() -> int:
    target = int(read_json(TARGET_CONFIG)["verification_target"])
    if target <= 0:
        raise SystemExit("verification_target must be positive")
    return target

def bar(percent: float, width: int = 30) -> str:
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)

def load_records() -> tuple[list[dict], list[str]]:
    schema = read_json(SCHEMA_PATH)
    required = set(schema["required"])
    records = []
    errors = []
    RECORD_DIR.mkdir(parents=True, exist_ok=True)
    for path in sorted(RECORD_DIR.glob("*.json")):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        if set(record) != required:
            errors.append(f"{path.name}: record keys do not exactly match schema")
            continue
        if record.get("verification_state") not in STATES:
            errors.append(f"{path.name}: invalid verification_state")
            continue
        if not isinstance(record.get("evidence_refs"), list) or not record["evidence_refs"]:
            errors.append(f"{path.name}: evidence_refs must be non-empty")
            continue
        records.append(record)
    return records, errors

def main() -> int:
    target = target_value()
    records, errors = load_records()
    if errors:
        raise SystemExit("Verification dashboard BLOCKED:\n" + "\n".join(errors))

    prepared = len(records)
    counts = {state: sum(r["verification_state"] == state for r in records) for state in STATES}
    reviewed = counts["REVIEW"] + counts["VERIFIED"]
    verified = counts["VERIFIED"]
    evidence_backed = sum(bool(r["evidence_refs"]) for r in records)

    if verified > reviewed or reviewed > prepared:
        raise SystemExit("Verification counters violate monotonic invariants.")
    if prepared > target:
        raise SystemExit(
            "Prepared canonical verification records exceed the configured milestone; "
            "the milestone target is not the same thing as the upstream queue size."
        )

    remaining = target - verified
    prepared_pct = round(prepared / target * 100, 6)
    reviewed_pct = round(reviewed / target * 100, 6)
    verified_pct = round(verified / target * 100, 6)
    remaining_pct = round(remaining / target * 100, 6)
    generated = datetime.now(timezone.utc).isoformat()

    dashboard = {
        "generated_at": generated,
        "method": "canonical independent-verification-record directory; fail-closed",
        "target": target,
        "records": {
            "target": target,
            "prepared": prepared,
            "reviewed": reviewed,
            "verified": verified,
            "remaining_to_verified_target": remaining,
            "evidence_supported": evidence_backed,
            "source_registry_records": prepared,
            "state_counts": counts,
        },
        "percent": {
            "prepared_of_target": prepared_pct,
            "reviewed_of_target": reviewed_pct,
            "independently_verified_of_target": verified_pct,
            "remaining_of_target": remaining_pct,
        },
        "automation_state": {
            "independent_verification_required": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "independent_reviewer_decision_required": True,
            "fail_closed": True,
        },
        "next_gate": (
            "Complete independent review for REVIEW records; VERIFIED promotion requires "
            "evidence, counter-evidence, reproducible test/observation, reviewer provenance, "
            "timestamp and audit."
            if verified < target else "Target reached."
        ),
    }
    OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = f"""# ꙰ SHIRMANI Verification Progress Dashboard

Generated: {generated}

## Authoritative target

**{verified:,} / {target:,} independently VERIFIED ({verified_pct:g}%)**

### Graph map

- Canonical prepared records: **{prepared:,}/{target:,} ({prepared_pct:g}%)**  {bar(prepared_pct)}
- Reviewed records: **{reviewed:,}/{target:,} ({reviewed_pct:g}%)**  {bar(reviewed_pct)}
- Independently VERIFIED: **{verified:,}/{target:,} ({verified_pct:g}%)**  {bar(verified_pct)}
- Remaining to target: **{remaining:,}/{target:,} ({remaining_pct:g}%)**  {bar(remaining_pct)}

## Canonical verification states

- REGISTERED: **{counts["REGISTERED"]}**
- UNVERIFIED: **{counts["UNVERIFIED"]}**
- REVIEW: **{counts["REVIEW"]}**
- VERIFIED: **{counts["VERIFIED"]}**
- BLOCKED: **{counts["BLOCKED"]}**

## Control state

- Automation may prepare: **YES**
- Automation may declare VERIFIED: **NO**
- Independent review required: **YES**
- Fail-closed promotion: **ENFORCED**

## Integrity rule

Workflow success, upstream queue size, generated packets, evidence collection,
or review-slot creation do not by themselves constitute independent verification.
VERIFIED requires the repository's independent-review decision and its complete
promotion controls.

## Next gate

{dashboard["next_gate"]}
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
