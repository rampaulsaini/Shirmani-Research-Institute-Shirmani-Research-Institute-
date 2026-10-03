#!/usr/bin/env python3
"""Generate the authoritative fail-closed SHIRMANI verification dashboard.

The 100,200-record target is sourced from the authoritative queue/registry.
Concrete claim/review records are reported separately and are never conflated
with the full target scale.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORITATIVE_QUEUE = ROOT / "generated/VERIFICATION-QUEUE.json"
AUTHORITATIVE_REGISTRY = ROOT / "generated/VERIFICATION-REGISTRY.json"
CONCRETE_RECORDS = ROOT / "generated/independent-verification-records.json"
OUT = ROOT / "generated/verification-progress-dashboard.json"
OUT_MD = ROOT / "generated/verification-progress-dashboard.md"
TARGET = 100200

def read_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing required status file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def bar(percent: float, width: int = 30) -> str:
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)

def pct(n: int, d: int) -> float:
    return round(100.0 * n / d, 6) if d else 0.0

def main() -> int:
    queue = read_json(AUTHORITATIVE_QUEUE)
    registry = read_json(AUTHORITATIVE_REGISTRY)
    concrete = read_json(CONCRETE_RECORDS)

    target = int(queue.get("records", 0))
    queued = int(registry.get("queued", 0))
    reviewed = int(registry.get("reviewed", 0))
    verified = int(registry.get("verified", 0))
    concrete_records = concrete.get("records", [])
    concrete_prepared = len(concrete_records)
    concrete_reviewed = sum(
        1 for r in concrete_records
        if r.get("reviewer_decision", {}).get("decision")
        in {"VERIFIED", "NOT_VERIFIED", "CONTRADICTED", "INCONCLUSIVE"}
    )
    concrete_verified = sum(
        1 for r in concrete_records
        if r.get("reviewer_decision", {}).get("decision") == "VERIFIED"
        and r.get("status") == "VERIFIED"
    )

    if target != TARGET:
        raise SystemExit(f"Authoritative target mismatch: expected {TARGET}, got {target}")
    if not (0 <= verified <= reviewed <= queued <= target):
        raise SystemExit("Authoritative verification counters violate monotonic invariants.")
    if concrete_verified > concrete_reviewed or concrete_reviewed > concrete_prepared:
        raise SystemExit("Concrete review counters violate monotonic invariants.")

    remaining = target - verified
    generated = datetime.now(timezone.utc).isoformat()

    dashboard = {
        "generated_at": generated,
        "method": "authoritative queue + fail-closed promotion registry; concrete review layer reported separately",
        "records": {
            "target": target,
            "queued": queued,
            "reviewed": reviewed,
            "verified": verified,
            "remaining_to_verified_target": remaining,
            "concrete_prepared": concrete_prepared,
            "concrete_reviewed": concrete_reviewed,
            "concrete_verified": concrete_verified,
        },
        "percent": {
            "queued_of_target": pct(queued, target),
            "reviewed_of_target": pct(reviewed, target),
            "independently_verified_of_target": pct(verified, target),
            "remaining_of_target": pct(remaining, target),
            "concrete_prepared_of_target": pct(concrete_prepared, target),
            "concrete_reviewed_of_prepared": pct(concrete_reviewed, concrete_prepared),
            "concrete_verified_of_prepared": pct(concrete_verified, concrete_prepared),
        },
        "automation_state": {
            "independent_verification_required": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "independent_reviewer_decision_required": True,
            "scales_must_not_be_conflated": True,
        },
        "next_gate": (
            "Complete independent review for queued records; each VERIFIED "
            "promotion requires evidence, counter-evidence, reproducible "
            "test/observation, reviewer provenance, timestamp and audit."
            if verified < target else "Target reached."
        ),
    }

    OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tv = dashboard["percent"]["independently_verified_of_target"]
    tr = dashboard["percent"]["remaining_of_target"]
    md = f"""# ꙰ SHIRMANI Verification Progress Dashboard

Generated: {generated}

## Authoritative 100,200-record target

**{verified:,} / {target:,} independently VERIFIED ({tv:g}%)**

### Target graph

- Queued: **{queued:,}/{target:,} ({dashboard["percent"]["queued_of_target"]:g}%)**  {bar(dashboard["percent"]["queued_of_target"])}
- Reviewed: **{reviewed:,}/{target:,} ({dashboard["percent"]["reviewed_of_target"]:g}%)**  {bar(dashboard["percent"]["reviewed_of_target"])}
- Independently VERIFIED: **{verified:,}/{target:,} ({tv:g}%)**  {bar(tv)}
- Remaining to target: **{remaining:,}/{target:,} ({tr:g}%)**  {bar(tr)}

## Concrete instantiated review layer

- Concrete claim records: **{concrete_prepared:,}**
- Concrete reviewed: **{concrete_reviewed:,}**
- Concrete independently VERIFIED: **{concrete_verified:,}**
- Concrete review completion: **{dashboard["percent"]["concrete_reviewed_of_prepared"]:g}%**
- Concrete VERIFIED completion: **{dashboard["percent"]["concrete_verified_of_prepared"]:g}%**

## Control state

- Automation may prepare: **YES**
- Automation may declare VERIFIED: **NO**
- Independent review required: **YES**
- Fail-closed promotion: **ENFORCED**
- Target and concrete review scales: **KEPT SEPARATE**

## Integrity rule

Workflow success, queue generation, evidence collection, generated packets,
or review-slot creation do not by themselves constitute independent
verification. VERIFIED requires an explicit independent-review decision with
the defined evidence, counter-evidence, reproducible test/observation,
reviewer provenance, timestamp and audit record.

## Operational path

**Source → Claims → Evidence → Independent Test → Reproducible Result → Counter-Evidence → Audit → VERIFIED → QC → Publication/Archive**

## Next gate

{dashboard["next_gate"]}
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
