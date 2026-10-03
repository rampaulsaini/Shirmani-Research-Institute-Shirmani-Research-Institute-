#!/usr/bin/env python3
"""Generate the authoritative fail-closed SHIRMANI verification dashboard."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "generated/independent-verification-records.json"
QUEUE = ROOT / "generated/independent-verification-queue.jsonl"
REGISTRY = ROOT / "generated/independent-verification-registry.jsonl"
OUT = ROOT / "generated/verification-progress-dashboard.json"
OUT_MD = ROOT / "generated/verification-progress-dashboard.md"
TARGET = 100200

def read_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing required status file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows

def bar(percent: float, width: int = 30) -> str:
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)

def main() -> int:
    data = read_json(RECORDS)
    records = data.get("records", [])
    if not isinstance(records, list):
        raise SystemExit("records must be a list")

    queue = read_jsonl(QUEUE)
    registry = read_jsonl(REGISTRY)

    prepared = len(records)
    queued = len(queue)
    reviewed = sum(
        1 for r in registry
        if r.get("status") == "REVIEWED"
        and r.get("verification_status") in {"VERIFIED", "NOT_VERIFIED", "CONTRADICTED", "INCONCLUSIVE"}
    )
    verified = sum(
        1 for r in records
        if r.get("reviewer_decision", {}).get("decision") == "VERIFIED"
        and r.get("status") == "VERIFIED"
    )
    registry_verified = sum(1 for r in registry if r.get("verification_status") == "VERIFIED")
    evidence_supported = sum(1 for r in records if r.get("status") == "EVIDENCE-SUPPORTED")

    # Fail closed on any disagreement between independent ledgers.
    if registry_verified != verified:
        raise SystemExit(
            f"Verification ledger mismatch: source VERIFIED={verified}, registry VERIFIED={registry_verified}"
        )
    if queued > TARGET or prepared > TARGET or reviewed > queued or verified > reviewed:
        raise SystemExit("Verification counters violate monotonic invariants.")

    remaining = TARGET - verified
    prepared_pct = round(prepared / TARGET * 100, 6)
    queued_pct = round(queued / TARGET * 100, 6)
    reviewed_pct = round(reviewed / TARGET * 100, 6)
    verified_pct = round(verified / TARGET * 100, 6)
    remaining_pct = round(remaining / TARGET * 100, 6)
    generated = datetime.now(timezone.utc).isoformat()

    dashboard = {
        "generated_at": generated,
        "method": "authoritative verification records + queue + review registry; fail-closed",
        "target": TARGET,
        "records": {
            "target": TARGET,
            "prepared": prepared,
            "queued": queued,
            "reviewed": reviewed,
            "verified": verified,
            "remaining_to_verified_target": remaining,
            "evidence_supported": evidence_supported,
        },
        "percent": {
            "prepared_of_target": prepared_pct,
            "queued_of_target": queued_pct,
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
        "integrity": {
            "source_records_count": prepared,
            "queue_count": queued,
            "review_registry_count": len(registry),
            "verified_ledger_match": registry_verified == verified,
        },
        "next_gate": (
            "Complete independent review for queued records; each VERIFIED "
            "promotion requires evidence, counter-evidence, reproducible test, "
            "reviewer provenance, timestamp, and audit."
            if verified < TARGET else "Target reached."
        ),
    }
    OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = f"""# ꙰ SHIRMANI Verification Progress Dashboard

Generated: {generated}

## Authoritative target

**{verified:,} / {TARGET:,} independently VERIFIED ({verified_pct:g}%)**

### Graph map

- Concrete source records: **{prepared:,}/{TARGET:,} ({prepared_pct:g}%)**  {bar(prepared_pct)}
- Queued review tasks: **{queued:,}/{TARGET:,} ({queued_pct:g}%)**  {bar(queued_pct)}
- Independently reviewed: **{reviewed:,}/{TARGET:,} ({reviewed_pct:g}%)**  {bar(reviewed_pct)}
- Independently VERIFIED: **{verified:,}/{TARGET:,} ({verified_pct:g}%)**  {bar(verified_pct)}
- Remaining to VERIFIED target: **{remaining:,}/{TARGET:,} ({remaining_pct:g}%)**  {bar(remaining_pct)}

## Control state

- Automation may prepare: **YES**
- Automation may declare VERIFIED: **NO**
- Independent review required: **YES**
- Fail-closed promotion: **ENFORCED**

## Integrity

The dashboard is regenerated from the concrete source-record file, verification
queue and review registry. A disagreement in VERIFIED counts blocks publication.
A target of {TARGET:,} is a target, not evidence that {TARGET:,} concrete review
tasks currently exist.

## Next gate

{dashboard["next_gate"]}
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
