#!/usr/bin/env python3
"""Fail-closed gate for promotion from review record to VERIFIED.

The factory may create review slots, but only a complete human/audit record
can promote a claim. Missing or fabricated reviewer/evidence data is blocked.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

REQUIRED = (
    "review_id", "task_id", "claim_id", "status", "verification_status",
    "independent", "reviewer", "reviewed_at", "evidence_references",
    "countercase_review", "reproduction_or_test", "audit", "created_at", "generator"
)

def promotable(r):
    return (
        r.get("status") == "REVIEWED"
        and r.get("verification_status") == "VERIFIED"
        and r.get("independent") is True
        and isinstance(r.get("reviewer"), str) and bool(r["reviewer"].strip())
        and isinstance(r.get("reviewer_role"), str) and bool(r["reviewer_role"].strip())
        and bool(r.get("reviewed_at"))
        and isinstance(r.get("evidence_references"), list) and all(isinstance(x, str) and x.strip() for x in r["evidence_references"]) and bool(r["evidence_references"])
        and (r.get("countercase_review") or {}).get("status") == "REVIEWED"
        and isinstance((r.get("countercase_review") or {}).get("references"), list)
        and all(isinstance(x, str) and x.strip() for x in (r.get("countercase_review") or {}).get("references", []))
        and bool((r.get("countercase_review") or {}).get("references"))
        and (r.get("reproduction_or_test") or {}).get("status") in {"PASSED", "SUPPORTED"}
        and isinstance((r.get("reproduction_or_test") or {}).get("references"), list)
        and all(isinstance(x, str) and x.strip() for x in (r.get("reproduction_or_test") or {}).get("references", []))
        and bool((r.get("reproduction_or_test") or {}).get("references"))
        and bool((r.get("audit") or {}).get("recorded_at"))
        and bool((r.get("audit") or {}).get("record_hash"))
    )

def main():
    path = OUT / "independent-verification-registry.jsonl"
    queue_path = OUT / "independent-verification-queue.jsonl"
    if not path.exists():
        raise SystemExit("independent-verification-registry.jsonl is missing")
    if not queue_path.exists():
        raise SystemExit("independent-verification-queue.jsonl is missing")

    # Bind every review slot to the exact current queue task. A review record
    # for an obsolete/mutated task must never survive as valid verification.
    queue_tasks = {}
    for line_no, line in enumerate(queue_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            task = json.loads(line)
        except Exception as exc:
            raise SystemExit(f"invalid verification queue JSON at line {line_no}: {exc}")
        task_id = str(task.get("task_id", ""))
        if not task_id or task_id in queue_tasks:
            raise SystemExit("verification queue has missing or duplicate task_id")
        queue_tasks[task_id] = task

    errors, seen, records, verified, eligible = [], set(), 0, 0, 0
    registry_task_ids = set()
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        records += 1
        try:
            r = json.loads(line)
        except Exception as exc:
            errors.append({"line": line_no, "error": "invalid_json:" + str(exc)})
            continue
        task_id = str(r.get("task_id", ""))
        registry_task_ids.add(task_id)
        if task_id not in queue_tasks:
            errors.append({"line": line_no, "error": "task_id_not_in_current_queue"})
        else:
            expected_hash = __import__("hashlib").sha256(json.dumps(queue_tasks[task_id], ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
            actual_hash = (r.get("audit") or {}).get("record_hash")
            if actual_hash != expected_hash:
                errors.append({"line": line_no, "error": "review_task_hash_mismatch"})
        rid = r.get("review_id")
        if not rid or rid in seen:
            errors.append({"line": line_no, "error": "missing_or_duplicate_review_id"})
        seen.add(rid)
        for key in REQUIRED:
            if key not in r:
                errors.append({"line": line_no, "error": "missing:" + key})
        if r.get("verification_status") == "VERIFIED":
            verified += 1
            if not promotable(r):
                errors.append({"line": line_no, "error": "unearned_verified_status"})
        if promotable(r):
            eligible += 1
    orphan_tasks = sorted(set(queue_tasks) - registry_task_ids)
    if orphan_tasks:
        errors.append({"error": "queue_tasks_missing_registry_records", "count": len(orphan_tasks), "task_ids_sample": orphan_tasks[:10]})

    report = {
        "version": 1,
        "records": records,
        "verified_records": verified,
        "promotion_eligible": eligible,
        "error_count": len(errors),
        "publication_gate": "BLOCK" if errors else ("PASS" if records == eligible else "CHECK"),
        "queue_records": len(queue_tasks),
        "orphan_queue_tasks": len(orphan_tasks),
        "policy": "Only complete independent review, evidence, countercase, reproduction/test and audit records may reach VERIFIED; every review must match the exact current queue task hash."
    }
    (OUT / "VERIFICATION-PROMOTION-QC.json").write_text(
        json.dumps({**report, "errors": errors}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
