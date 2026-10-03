#!/usr/bin/env python3
"""Generate a non-deceptive independent-verification progress map."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "generated/independent-verification-status-2026-09-29.json"
QUEUE = ROOT / "generated/independent-verification-queue.jsonl"
REGISTRY = ROOT / "generated/independent-verification-registry.jsonl"
OUT_JSON = ROOT / "generated/independent-verification-progress.json"
OUT_MD = ROOT / "generated/independent-verification-progress-map.md"

def jsonl_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())

def bar(pct: float, width: int = 20) -> str:
    filled = round(width * pct / 100)
    return "█" * filled + "░" * (width - filled)

def main() -> None:
    data = json.loads(STATUS.read_text(encoding="utf-8"))
    s = data["verification_summary"]

    # Prefer the live canonical registry over the historical 2026-09-29
    # status snapshot. The snapshot must not cap a live queue that has
    # subsequently expanded (for example, to 100,200 records).
    live_records = ROOT / "generated/independent-verification-records.json"
    live = json.loads(live_records.read_text(encoding="utf-8")) if live_records.exists() else {}
    live_rows = live.get("records", []) if isinstance(live, dict) else []
    queue = jsonl_count(QUEUE)
    registry = jsonl_count(REGISTRY)
    total = queue or len(live_rows) or int(s["queue_records"])
    evidence = sum(
        1 for r in live_rows
        if str(r.get("source_status", r.get("status", ""))).upper() == "EVIDENCE-SUPPORTED"
    )
    readiness = 100.0 if total else float(s["verification_readiness_percent"])

    # The live review registry is authoritative for progress after bootstrap.
    # Never infer VERIFIED from workflow success or the historical status file.
    verified = 0
    if REGISTRY.exists():
        for line in REGISTRY.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            if (
                str(record.get("status", "")).upper() == "REVIEWED"
                and str(record.get("verification_status", "")).upper() == "VERIFIED"
                and record.get("independent") is True
            ):
                verified += 1
    evidence_pct = round((evidence / total) * 100, 2) if total else 0
    verified_pct = round((verified / total) * 100, 2) if total else 0
    registry_coverage = round((registry / queue) * 100, 2) if queue else 0

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "live queue + generated/independent-verification-records.json; historical status retained for provenance",
        "queue_records": total,
        "evidence_supported_records": evidence,
        "evidence_supported_percent": evidence_pct,
        "review_readiness_percent": readiness,
        "queue_records_generated": queue,
        "review_registry_records": registry,
        "review_registry_coverage_percent": registry_coverage,
        "independently_verified_records": verified,
        "independent_verified_percent": verified_pct,
        "policy": {
            "workflow_activity_is_not_verification": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "human_or_independent_reviewer_decision_required": True
        }
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = """# ꙰ SHIRMANI Independent Verification Progress Map

Generated: {generated}

## Current measurable state

| Measure | Progress |
|---|---:|
| Verification readiness | **{readiness:g}%** |
| Evidence-supported records | **{evidence}/{total} ({evidence_pct:g}%)** |
| Queue generated | **{queue}/{total} ({queue_pct:g}%)** |
| Review registry coverage | **{registry}/{queue} ({registry_coverage:g}%)** |
| Independently VERIFIED | **{verified}/{total} ({verified_pct:g}%)** |

## Graph

- Readiness: {readiness_bar} {readiness:g}%
- Evidence-supported: {evidence_bar} {evidence_pct:g}%
- Review registry coverage: {registry_bar} {registry_coverage:g}%
- Independent VERIFIED: {verified_bar} {verified_pct:g}%

## Critical distinction

**Prepared/ready is not the same as independently VERIFIED.**

A workflow succeeding, a queue being generated, or evidence being collected does not create an independent verification decision. VERIFIED remains fail-closed until an independent reviewer records the required evidence, counter-evidence review, reproducible test/observation, reviewer identity/role, timestamp, and audit record.

## Next measurable gate

EVIDENCE -> INDEPENDENT TEST -> REPRODUCIBLE RESULT -> COUNTER-EVIDENCE -> AUDIT -> VERIFIED

The system may automate preparation and auditing, but it must not manufacture an independent reviewer decision.
""".format(
        generated=report["generated_at"], readiness=readiness, evidence=evidence, total=total,
        evidence_pct=evidence_pct, queue=queue, queue_pct=round(queue/total*100,2) if total else 0,
        registry=registry, registry_coverage=registry_coverage, verified=verified,
        verified_pct=verified_pct, readiness_bar=bar(readiness), evidence_bar=bar(evidence_pct),
        registry_bar=bar(registry_coverage), verified_bar=bar(verified_pct)
    )
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
