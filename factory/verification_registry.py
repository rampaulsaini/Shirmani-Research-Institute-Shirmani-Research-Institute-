#!/usr/bin/env python3
"""Build durable human-review records from the independent verification queue.

Review records are append/update durable state: existing human/audit fields are
preserved when the underlying verification task is unchanged. The factory
never fabricates a reviewer, evidence, or VERIFIED status.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def sha(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def load_existing(path):
    existing = {}
    if not path.exists():
        return existing
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
            key = record.get("task_id")
            if key:
                existing[str(key)] = record
        except Exception:
            # The promotion gate will fail closed on malformed persisted state.
            continue
    return existing

def new_record(task, now):
    task_id = str(task["task_id"])
    return {
        "review_id": "review:" + sha(task_id)[:24],
        "task_id": task_id,
        "claim_id": str(task["claim_id"]),
        "status": "QUEUED",
        "verification_status": "NOT_VERIFIED",
        "independent": False,
        "reviewer": None,
        "reviewer_role": None,
        "reviewed_at": None,
        "evidence_references": [],
        "countercase_review": {"status": "NOT_REVIEWED", "references": []},
        "reproduction_or_test": {"status": "NOT_RUN", "references": []},
        "audit": {
            "recorded_at": now,
            "record_hash": sha(json.dumps(task, ensure_ascii=False, sort_keys=True)),
        },
        "created_at": now,
        "generator": "factory/verification_registry.py",
    }

def main():
    queue = OUT / "independent-verification-queue.jsonl"
    if not queue.exists():
        raise SystemExit("independent-verification-queue.jsonl is missing")

    now = datetime.now(timezone.utc).isoformat()
    out = OUT / "independent-verification-registry.jsonl"
    existing = load_existing(out)
    records = []
    preserved = 0
    reset_for_changed_task = 0

    for line in queue.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        task_id = str(task["task_id"])
        task_hash = sha(json.dumps(task, ensure_ascii=False, sort_keys=True))
        prior = existing.get(task_id)

        if prior and (prior.get("audit") or {}).get("record_hash") == task_hash:
            record = prior
            preserved += 1
            # Keep the immutable identity tied to the current task.
            record["review_id"] = "review:" + sha(task_id)[:24]
            record["task_id"] = task_id
            record["claim_id"] = str(task["claim_id"])
            record["generator"] = "factory/verification_registry.py"
        else:
            record = new_record(task, now)
            if prior:
                reset_for_changed_task += 1

        records.append(record)

    out.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in records)
        + ("\n" if records else ""),
        encoding="utf-8",
    )

    verified = sum(r.get("verification_status") == "VERIFIED" for r in records)
    summary = {
        "version": 2,
        "records": len(records),
        "queued": sum(r.get("status") == "QUEUED" for r in records),
        "reviewed": sum(r.get("status") == "REVIEWED" for r in records),
        "verified": verified,
        "preserved_existing_reviews": preserved,
        "reset_for_changed_task": reset_for_changed_task,
        "promotion_gate": "CHECK" if records else "BLOCK",
        "policy": (
            "Persisted review records are preserved when task provenance is unchanged; "
            "changed tasks receive fresh review slots. No reviewer/evidence/verification is invented."
        ),
    }
    (OUT / "VERIFICATION-REGISTRY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    main()
