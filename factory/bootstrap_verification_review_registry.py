"""Create and maintain pending review slots bound to the exact current verification queue.

This is deliberately additive: existing review decisions are preserved.
Pending slots are not verification decisions, and this script never promotes a claim.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "generated/independent-verification-queue.jsonl"
OUT = ROOT / "generated/independent-verification-registry.jsonl"

def task_hash(task):
    return hashlib.sha256(
        json.dumps(task, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()

def load_jsonl(path: Path):
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        return []
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            raise SystemExit(f"invalid JSONL at {path}:{line_no}: {exc}")
    return rows

def main():
    queue = load_jsonl(QUEUE)
    existing = load_jsonl(OUT)
    existing_by_task = {}
    for row in existing:
        task_id = str(row.get("task_id", ""))
        if not task_id:
            raise SystemExit("review registry contains a record without task_id")
        if task_id in existing_by_task:
            raise SystemExit(f"duplicate task_id in review registry: {task_id}")
        existing_by_task[task_id] = row

    now = datetime.now(timezone.utc).isoformat()
    result = []
    preserved = 0
    created = 0

    for task in queue:
        task_id = str(task.get("task_id", ""))
        if not task_id:
            raise SystemExit("verification queue contains a task without task_id")

        prior = existing_by_task.get(task_id)
        expected_hash = task_hash(task)

        if prior is not None:
            # Preserve reviewer work. The promotion gate will reject stale hashes.
            prior_hash = (prior.get("audit") or {}).get("record_hash")
            if prior_hash != expected_hash:
                # Do not silently rewrite a reviewed record. Keep it visible and
                # let the promotion QC report it as stale.
                prior = dict(prior)
                prior["stale_against_current_queue"] = True
                prior["stale_detected_at"] = now
            result.append(prior)
            preserved += 1
            continue

        result.append({
            "review_id": "REVIEW-" + task_id,
            "task_id": task_id,
            "claim_id": task["claim_id"],
            "status": "PENDING_REVIEW",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "reviewer": "",
            "reviewer_role": "",
            "reviewed_at": "",
            "evidence_references": list(task.get("source_ids") or []),
            "countercase_review": {"status": "PENDING", "references": []},
            "reproduction_or_test": {"status": "PENDING", "references": []},
            "audit": {"recorded_at": "", "record_hash": expected_hash},
            "created_at": now,
            "generator": "factory/bootstrap_verification_review_registry.py"
        })
        created += 1

    # Never silently retain records for tasks no longer in the authoritative queue.
    current_ids = {str(t.get("task_id", "")) for t in queue}
    orphaned = sorted(set(existing_by_task) - current_ids)
    if orphaned:
        raise SystemExit(
            "review registry contains orphaned tasks; reconciliation required: "
            + ", ".join(orphaned[:10])
        )

    OUT.write_text(
        "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in result),
        encoding="utf-8"
    )
    print(json.dumps({
        "review_slots": len(result),
        "created": created,
        "preserved": preserved,
        "verified_records": sum(
            1 for x in result if x.get("verification_status") == "VERIFIED"
        ),
        "fail_closed": True,
        "review_decisions_preserved": True
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
