#!/usr/bin/env python3
"""Generate a non-deceptive independent-verification progress map.

The repository currently has two deliberately distinct scales:
1. The authoritative 100,200-record target registry.
2. The instantiated claim/review registry currently materialized for actual review.

They must never be conflated. Workflow activity and review-slot creation are
preparation telemetry, not independent verification.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORITATIVE_QUEUE = ROOT / "generated/VERIFICATION-QUEUE.json"
AUTHORITATIVE_REGISTRY = ROOT / "generated/VERIFICATION-REGISTRY.json"
PROMOTION_QC = ROOT / "generated/VERIFICATION-PROMOTION-QC.json"
STATUS = ROOT / "generated/independent-verification-status-2026-09-29.json"
QUEUE = ROOT / "generated/independent-verification-queue.jsonl"
REGISTRY = ROOT / "generated/independent-verification-registry.jsonl"
OUT_JSON = ROOT / "generated/independent-verification-progress.json"
OUT_MD = ROOT / "generated/independent-verification-progress-map.md"

def jsonl_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())

def jsonl_verified(path: Path) -> int:
    if not path.exists():
        return 0
    n = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if (str(r.get("status","")).upper() == "REVIEWED"
            and str(r.get("verification_status","")).upper() == "VERIFIED"
            and r.get("independent") is True):
            n += 1
    return n

def pct(n: int, d: int) -> float:
    return round(100.0*n/d, 4) if d else 0.0

def bar(value: float, width: int = 20) -> str:
    filled = round(width*value/100)
    return "█"*filled + "░"*(width-filled)

def main() -> None:
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    summary = status["verification_summary"]
    aq = json.loads(AUTHORITATIVE_QUEUE.read_text(encoding="utf-8"))
    ar = json.loads(AUTHORITATIVE_REGISTRY.read_text(encoding="utf-8"))
    promotion = json.loads(PROMOTION_QC.read_text(encoding="utf-8"))

    target = int(aq["records"])
    queued = int(ar["queued"])
    reviewed = int(ar["reviewed"])
    verified = int(ar["verified"])

    instantiated = jsonl_count(QUEUE)
    review_slots = jsonl_count(REGISTRY)
    instantiated_verified = jsonl_verified(REGISTRY)
    historical_queue = int(summary["queue_records"])
    evidence_supported = int(summary["evidence_supported_records"])

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "independent-verification",
        "authoritative_target": target,
        "authoritative": {
            "registered_target_capacity": target,
            "target_capacity_is_not_instantiated_queue": True,
            "queued": queued, "reviewed": reviewed, "verified": verified,
            "remaining_to_target": max(target-verified,0),
            "queued_percent": pct(queued,target),
            "registered_target_capacity_percent": 100.0,
            "reviewed_percent": pct(reviewed,target),
            "verified_percent": pct(verified,target),
            "remaining_percent": pct(max(target-verified,0),target),
            "promotion_eligible": int(promotion.get("promotion_eligible",0)),
            "publication_gate": promotion.get("publication_gate"),
        },
        "instantiated_review_layer": {
            "claim_records": instantiated,
            "instantiated_queue_records": instantiated,
            "review_slots": review_slots,
            "verified": instantiated_verified,
            "review_slot_coverage_percent": pct(review_slots,instantiated),
            "verified_percent_of_instantiated": pct(instantiated_verified,instantiated),
            "evidence_supported_records": evidence_supported,
            "evidence_supported_percent_of_historical_queue": pct(evidence_supported,historical_queue),
        },
        "legacy_status_reference": {
            "historical_queue_records": historical_queue,
            "historical_verified_records": int(summary["independently_verified_records"]),
            "historical_verified_percent": float(summary["independent_verified_percent"]),
        },
        "policy": {
            "workflow_activity_is_not_verification": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "independent_reviewer_decision_required": True,
            "scales_must_not_be_conflated": True,
        },
    }
    OUT_JSON.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    tv = report["authoritative"]["verified_percent"]
    tr = report["authoritative"]["remaining_percent"]
    rc = report["instantiated_review_layer"]["review_slot_coverage_percent"]
    iv = report["instantiated_review_layer"]["verified_percent_of_instantiated"]

    md = f"""# ꙰ SHIRMANI Independent Verification Progress Map

Generated: {report["generated_at"]}

## Authoritative target scale

| Measure | Current |
|---|---:|
| Target | **{target:,} records** |
| Registered target capacity | **{target:,} (100%)** |
| Instantiated review queue | **{instantiated:,} ({pct(instantiated,target):g}% of target)** |
| Legacy/authoritative queue metadata | **{queued:,} ({report["authoritative"]["queued_percent"]:g}% of target)** |
| Reviewed | **{reviewed:,} ({report["authoritative"]["reviewed_percent"]:g}%)** |
| Independently VERIFIED | **{verified:,} ({tv:g}%)** |
| Remaining to target | **{target-verified:,} ({tr:g}%)** |
| Promotion eligible | **{promotion.get("promotion_eligible",0):,}** |
| Publication gate | **{promotion.get("publication_gate")}** |

### Target graph
- VERIFIED: {bar(tv)} {tv:g}%
- Remaining: {bar(tr)} {tr:g}%

## Instantiated review layer

The repository currently materializes a smaller set of concrete claim/review records.
The 100,200 figure is a target/registry-capacity declaration; it must not be presented as 100,200 completed or instantiated review tasks. The machine-readable report explicitly marks target capacity as distinct from the instantiated queue.

| Measure | Current |
|---|---:|
| Concrete claim records | **{instantiated:,}** |
| Target coverage by concrete records | **{pct(instantiated,target):g}%** |
| Review slots | **{review_slots:,} ({rc:g}% coverage)** |
| Independently VERIFIED | **{instantiated_verified:,} ({iv:g}%)** |
| Evidence-supported in historical 10-record status | **{evidence_supported}/{historical_queue} ({report["instantiated_review_layer"]["evidence_supported_percent_of_historical_queue"]:g}%)** |

### Review-layer graph
- Review-slot coverage: {bar(rc)} {rc:g}%
- Independently VERIFIED: {bar(iv)} {iv:g}%

## Critical distinction

**Preparation, queue generation, review-slot generation, evidence collection and workflow success are not independent verification.**

A record reaches VERIFIED only after the required independent review decision, evidence, counter-evidence review, reproducible test/observation, reviewer identity/role, timestamp and audit record satisfy the fail-closed promotion controls.

## Operational path

**Source → Normalize → Claims → Evidence → Independent Test → Reproducible Result → Counter-Evidence → Audit → VERIFIED → QC → Publication/Archive**

The system may automate preparation and auditing, but it must not manufacture an independent reviewer decision.

## Integrity note

The 100,200-record target and the currently instantiated concrete review records are intentionally reported as separate scales. This prevents a 10/10 review-slot coverage figure from being mistaken for 100% completion of the 100,200 VERIFIED target.
"""
    OUT_MD.write_text(md,encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__ == "__main__":
    main()
