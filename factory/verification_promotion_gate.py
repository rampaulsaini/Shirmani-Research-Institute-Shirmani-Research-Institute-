#!/usr/bin/env python3
"""Build a durable independent-review registry and fail-closed promotion gate.

The factory may queue verification work, but it may not manufacture a verified
result. Human/audited review records are accepted only when every required
field is present and the review is explicitly independent.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
REVIEWS = OUT / "verification-reviews.jsonl"
QUEUE = OUT / "independent-verification-queue.jsonl"
REGISTRY = OUT / "verification-registry.jsonl"
REPORT = OUT / "VERIFICATION-PROMOTION-GATE.json"

REQUIRED_REVIEW = (
    "task_id", "claim_id", "decision", "reviewer_id", "reviewed_at",
    "evidence_refs", "countercase_reviewed", "independent", "audit_ref"
)
ALLOWED_DECISIONS = {"VERIFIED", "REJECTED", "NEEDS_REVIEW"}

def load_jsonl(path):
    if not path.exists():
        return []
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            rows.append((n, json.loads(line)))
    return rows

def main():
    if not QUEUE.exists():
        raise SystemExit("independent-verification-queue.jsonl is missing")

    queue_rows = load_jsonl(QUEUE)
    queue = {str(r.get("task_id")): r for _, r in queue_rows}
    reviews = {}
    errors = []

    for line_no, review in load_jsonl(REVIEWS):
        missing = [k for k in REQUIRED_REVIEW if k not in review]
        if missing:
            errors.append({"line": line_no, "error": "review_missing:" + ",".join(missing)})
            continue
        task_id = str(review["task_id"])
        if task_id in reviews:
            errors.append({"line": line_no, "error": "duplicate_review_task_id"})
            continue
        if task_id not in queue:
            errors.append({"line": line_no, "error": "review_task_not_in_queue"})
            continue
        if review["decision"] not in ALLOWED_DECISIONS:
            errors.append({"line": line_no, "error": "invalid_review_decision"})
        if not isinstance(review["evidence_refs"], list) or not review["evidence_refs"]:
            errors.append({"line": line_no, "error": "missing_evidence_refs"})
        if review["countercase_reviewed"] is not True:
            errors.append({"line": line_no, "error": "countercase_review_required"})
        if review["independent"] is not True:
            errors.append({"line": line_no, "error": "independent_review_required"})
        if not str(review["reviewer_id"]).strip():
            errors.append({"line": line_no, "error": "reviewer_id_required"})
        if not str(review["audit_ref"]).strip():
            errors.append({"line": line_no, "error": "audit_ref_required"})
        reviews[task_id] = review

    now = datetime.now(timezone.utc).isoformat()
    registry_rows = []
    promoted = 0
    pending = 0
    rejected = 0

    for task_id, task in queue.items():
        review = reviews.get(task_id)
        status = "NOT_VERIFIED"
        independent = False
        if review and not any(e.get("line") == task_id for e in errors):
            if review["decision"] == "VERIFIED":
                status = "VERIFIED"
                independent = True
                promoted += 1
            elif review["decision"] == "REJECTED":
                status = "REJECTED"
                rejected += 1
            else:
                status = "NEEDS_REVIEW"
                pending += 1
        else:
            pending += 1
        registry_rows.append({
            "task_id": task_id,
            "claim_id": task.get("claim_id"),
            "verification_status": status,
            "independent": independent,
            "review_ref": review.get("audit_ref") if review else None,
            "reviewed_at": review.get("reviewed_at") if review else None,
            "generated_at": now,
            "policy": "Only an explicit independent review with evidence, countercase review and audit reference may promote a claim."
        })

    REGISTRY.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in registry_rows) +
        ("\n" if registry_rows else ""), encoding="utf-8"
    )
    report = {
        "version": 1,
        "queue_records": len(queue_rows),
        "review_records": len(reviews),
        "promoted_verified": promoted,
        "rejected": rejected,
        "pending_or_needs_review": pending,
        "error_count": len(errors),
        "verification_completion": "COMPLETE" if pending == 0 and not errors else "CHECK",
        "publication_gate": "PASS" if not errors else "BLOCK",
        "policy": "Verification promotion is fail-closed; the factory cannot self-verify claims."
    }
    REPORT.write_text(json.dumps({**report, "errors": errors}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
