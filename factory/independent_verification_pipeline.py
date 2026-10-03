#!/usr/bin/env python3
"""Fail-closed independent-verification conveyor.

This tool NEVER promotes a claim to VERIFIED. It validates the conveyor state,
checks reproducibility/audit prerequisites when review records exist, and emits
a machine-readable report describing what is still required.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
STATUS = OUT / "independent-verification-status-2026-09-29.json"
QUEUE = OUT / "independent-verification-queue.jsonl"
REGISTRY = OUT / "independent-verification-registry.jsonl"
REPORT = OUT / "independent-verification-conveyor-report.json"

STAGES = ["EVIDENCE_COLLECTION", "INDEPENDENT_TEST", "REPRODUCIBLE_RESULT", "AUDIT", "VERIFIED"]

def load_jsonl(path: Path):
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        return []
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            raise ValueError(f"{path.name}: invalid JSONL line {n}: {exc}")
    return rows

def sha256_obj(obj):
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def main():
    if not STATUS.exists():
        raise SystemExit("missing independent verification status registry")
    errors = []

    queue = load_jsonl(QUEUE)
    registry = load_jsonl(REGISTRY)
    queue_ids = {str(x.get("task_id")) for x in queue if x.get("task_id")}
    registry_ids = {str(x.get("task_id")) for x in registry if x.get("task_id")}

    stage_counts = {s: 0 for s in STAGES}
    blockers = []
    verified = 0
    for r in registry:
        stage = r.get("stage")
        if stage in stage_counts:
            stage_counts[stage] += 1
        if stage == "VERIFIED":
            required = (
                r.get("independent") is True,
                bool(r.get("reviewer")),
                bool(r.get("reviewer_role")),
                bool(r.get("reviewed_at")),
                bool(r.get("evidence_references")),
                (r.get("countercase_review") or {}).get("status") == "REVIEWED",
                (r.get("reproduction_or_test") or {}).get("status") in {"PASSED", "SUPPORTED"},
                bool((r.get("audit") or {}).get("recorded_at")),
                bool((r.get("audit") or {}).get("record_hash")),
            )
            if not all(required):
                blockers.append({"task_id": r.get("task_id"), "reason": "incomplete_verified_record"})
            else:
                verified += 1

    missing_registry_tasks = sorted(queue_ids - registry_ids)
    report = {
        "schema_version": "2.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": "EVIDENCE_COLLECTION -> INDEPENDENT_TEST -> REPRODUCIBLE_RESULT -> AUDIT -> VERIFIED",
        "policy": {
            "fail_closed": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "accuracy_is_measured_not_declared": True,
            "workflow_success_is_not_independent_verification": True,
        },
        "baseline": {
            "queue_records": summary.get("queue_records", len(records)),
            "evidence_supported_records": summary.get("evidence_supported_records", 0),
            "independently_verified_records": verified,
            "independent_verified_percent": round((verified / len(queue)) * 100, 4) if queue else 0.0,
        },
        "conveyor": {
            "queue_records": len(queue),
            "review_registry_records": len(registry),
            "missing_registry_tasks": len(missing_registry_tasks),
            "stage_counts": stage_counts,
            "blocked_verified_records": len(blockers),
        },
        "next_actions": [
            "Attach an operational definition to each testable claim.",
            "Collect independent evidence and record provenance.",
            "Run an independent test or observation with reproducible inputs.",
            "Record counter-evidence and failure cases.",
            "Record reviewer identity/role, timestamp and immutable task hash.",
            "Only then allow an independent reviewer to record a VERIFIED decision.",
        ],
        "errors": errors,
        "blockers": blockers,
        "missing_registry_tasks_sample": missing_registry_tasks[:20],
        "queue_sha256": sha256_obj(queue),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS" if not errors else "BLOCK", "verified": report["baseline"]["independently_verified_records"], "queue": report["conveyor"]["queue_records"], "registry": report["conveyor"]["review_registry_records"], "stage_counts": stage_counts, "report": str(REPORT.relative_to(ROOT))}, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
