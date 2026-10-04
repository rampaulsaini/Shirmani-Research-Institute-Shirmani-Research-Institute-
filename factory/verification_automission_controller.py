#!/usr/bin/env python3
"""SHIRMANI 100% Automission verification controller.

Automates the complete verification workflow mechanics: discovery, structural
checks, evidence/readiness classification, progress accounting and fail-closed
promotion. It NEVER fabricates an independent reviewer decision and NEVER
promotes a record to VERIFIED without the required independent decision.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "generated" / "independent-verification-records.json"
TARGET = ROOT / "config" / "independent-verification-target.json"
OUT = ROOT / "generated" / "verification-automission-report.json"

VERIFIED = {"VERIFIED", "INDEPENDENTLY_VERIFIED"}
DECISIONS = {"VERIFIED", "NOT_VERIFIED", "CONTRADICTED", "INCONCLUSIVE"}

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    if not REGISTRY.exists() or not TARGET.exists():
        raise SystemExit("AUTOMISSION_VERIFICATION_FAIL: required registry/config missing")

    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    cfg = json.loads(TARGET.read_text(encoding="utf-8"))
    records = data.get("records")
    target = int(cfg["verification_target"])

    if not isinstance(records, list) or target <= 0:
        raise SystemExit("AUTOMISSION_VERIFICATION_FAIL: invalid registry or target")

    seen = set()
    ready = []
    blocked = []
    verified = []

    for r in records:
        rid = r.get("id")
        if not rid or rid in seen:
            raise SystemExit(f"AUTOMISSION_VERIFICATION_FAIL: duplicate/missing id: {rid}")
        seen.add(rid)

        status = str(r.get("status", "")).upper()
        decision = str(r.get("reviewer_decision", {}).get("decision", "")).upper()

        if status in VERIFIED and decision == "VERIFIED":
            verified.append(rid)
            continue

        reasons = []
        if not r.get("operational_definition"):
            reasons.append("missing operational definition")
        if not r.get("evidence", {}).get("sources"):
            reasons.append("no independent/source evidence listed")
        if r.get("independent_test", {}).get("result") in (None, "", "PENDING"):
            reasons.append("independent test pending")
        if not r.get("counter_evidence", {}).get("reviewed"):
            reasons.append("counter-evidence review pending")
        if decision not in DECISIONS:
            reasons.append("independent reviewer decision pending")

        if not reasons:
            ready.append(rid)
        else:
            blocked.append({"id": rid, "reasons": reasons})

    if len(verified) > target or len(records) > target:
        raise SystemExit("AUTOMISSION_VERIFICATION_FAIL: target invariant violated")

    remaining = max(target - len(verified), 0)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "100_PERCENT_AUTOMISSION_WORKFLOW_MECHANICS",
        "fail_closed": True,
        "automation_coverage_percent": 100,
        "verification_target": target,
        "registry_records": len(records),
        "verified_records": len(verified),
        "ready_for_independent_decision": len(ready),
        "blocked_pending_independent_work": len(blocked),
        "remaining_to_target": remaining,
        "verified_percent_of_target": round(len(verified) / target * 100, 6),
        "remaining_percent_of_target": round(remaining / target * 100, 6),
        "verified_ids": verified,
        "ready_ids": ready,
        "blocked": blocked,
        "registry_sha256": sha256(REGISTRY),
        "promotion_rule": "Automation may prepare, validate and route; only an explicit independent reviewer decision may promote VERIFIED.",
        "status": "TARGET_REACHED" if len(verified) >= target else "AUTOMISSION_ACTIVE",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
