#!/usr/bin/env python3
"""Generate a non-deceptive independent-verification progress map."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "generated/independent-verification-status-2026-09-29.json"
QUEUE_SUMMARY = ROOT / "generated/VERIFICATION-QUEUE.json"
REGISTRY_SUMMARY = ROOT / "generated/VERIFICATION-REGISTRY.json"
OUT_JSON = ROOT / "generated/independent-verification-progress.json"
OUT_MD = ROOT / "generated/independent-verification-progress-map.md"

def jsonl_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())

def bar(pct: float, width: int = 20) -> str:
    filled = round(width * pct / 100)
    return "█" * filled + "░" * (width - filled)

def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> None:
    data = read_json(STATUS)
    s = data.get("verification_summary", {})

    # The authoritative 100,200-record queue is distinct from the small
    # prepared/source set. Never collapse these into one denominator.
    queue_data = read_json(QUEUE_SUMMARY)
    registry_data = read_json(REGISTRY_SUMMARY)
    target = int(queue_data.get("records", 100_200))
    queued = int(queue_data.get("queued", 0))
    reviewed = int(registry_data.get("reviewed", 0))
    verified = int(registry_data.get("verified", 0))

    prepared = int(s.get("queue_records", 0))
    evidence = int(s.get("evidence_supported_records", 0))
    readiness = float(s.get("verification_readiness_percent", 0))

    # Cross-check the authoritative registry rather than inferring VERIFIED
    # from workflow activity or the historical status file.
    registry_jsonl = ROOT / "generated/independent-verification-registry.jsonl"
    registry_records = jsonl_count(registry_jsonl)
    if registry_jsonl.exists():
        actual_verified = 0
        for line in registry_jsonl.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            if (
                str(record.get("status", "")).upper() == "REVIEWED"
                and str(record.get("verification_status", "")).upper() == "VERIFIED"
                and record.get("independent") is True
            ):
                actual_verified += 1
        if actual_verified != verified:
            raise SystemExit(
                f"Authoritative verification mismatch: registry summary={verified}, "
                f"registry records={actual_verified}"
            )

    if not (0 <= verified <= reviewed <= queued <= target):
        raise SystemExit("Authoritative verification counters violate monotonic invariants.")

    prepared_pct = round((prepared / target) * 100, 6) if target else 0
    queued_pct = round((queued / target) * 100, 6) if target else 0
    evidence_pct = round((evidence / target) * 100, 6) if target else 0
    verified_pct = round((verified / target) * 100, 6) if target else 0
    remaining = target - verified
    registry_coverage = round((registry_records / queued) * 100, 6) if queued else 0

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "historical_prepared_status": str(STATUS),
            "authoritative_queue": str(QUEUE_SUMMARY),
            "authoritative_registry": str(REGISTRY_SUMMARY),
        },
        "target_records": target,
        "prepared_records": prepared,
        "prepared_percent_of_target": prepared_pct,
        "queued_records": queued,
        "queued_percent_of_target": queued_pct,
        "evidence_supported_records": evidence,
        "evidence_supported_percent_of_target": evidence_pct,
        "reviewed_records": reviewed,
        "independently_verified_records": verified,
        "independent_verified_percent": verified_pct,
        "remaining_to_target": remaining,
        "review_registry_records_observed": registry_records,
        "review_registry_coverage_percent": registry_coverage,
        "review_readiness_percent": readiness,
        "policy": {
            "workflow_activity_is_not_verification": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "human_or_independent_reviewer_decision_required": True,
        },
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = """# ꙰ SHIRMANI Independent Verification Progress Map

Generated: {generated}

## Authoritative current state

| Measure | Count | Progress of 100,200 target |
|---|---:|---:|
| Prepared/source set | **{prepared}** | **{prepared_pct:g}%** |
| Authoritative queue | **{queued}** | **{queued_pct:g}%** |
| Evidence-supported | **{evidence}** | **{evidence_pct:g}%** |
| Reviewed | **{reviewed}** | **{reviewed_pct:g}%** |
| Independently VERIFIED | **{verified}** | **{verified_pct:g}%** |
| Remaining to target | **{remaining}** | **{remaining_pct:g}%** |

## Graph

- Prepared/source set: {prepared_bar} {prepared_pct:g}%
- Authoritative queue: {queued_bar} {queued_pct:g}%
- Evidence-supported: {evidence_bar} {evidence_pct:g}%
- Reviewed: {reviewed_bar} {reviewed_pct:g}%
- Independent VERIFIED: {verified_bar} {verified_pct:g}%

## Critical distinction

**Prepared, queued, evidence-supported, reviewed, and independently VERIFIED are separate states.**

Workflow success, queue generation, evidence collection, or review-slot creation does not create an independent verification decision. VERIFIED remains fail-closed until an independent reviewer records the required evidence, counter-evidence review, reproducible test/observation, reviewer provenance, timestamp, and audit record.

## Next measurable gate

EVIDENCE -> INDEPENDENT TEST -> REPRODUCIBLE RESULT -> COUNTER-EVIDENCE -> AUDIT -> VERIFIED

Automation may prepare and audit the process, but it must not manufacture an independent reviewer decision.
""".format(
        generated=report["generated_at"],
        prepared=prepared, prepared_pct=prepared_pct,
        queued=queued, queued_pct=queued_pct,
        evidence=evidence, evidence_pct=evidence_pct,
        reviewed=reviewed, reviewed_pct=round(reviewed / target * 100, 6) if target else 0,
        verified=verified, verified_pct=verified_pct,
        remaining=remaining, remaining_pct=round(remaining / target * 100, 6) if target else 0,
        prepared_bar=bar(prepared_pct), queued_bar=bar(queued_pct),
        evidence_bar=bar(evidence_pct), verified_bar=bar(verified_pct)
    )
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
