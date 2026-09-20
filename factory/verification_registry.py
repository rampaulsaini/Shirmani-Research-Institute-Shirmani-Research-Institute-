#!/usr/bin/env python3
"""Build a durable independent-verification review registry.

The registry records review state separately from the verification queue.
It never invents a reviewer, evidence, or verification result. Existing
review records are preserved when the factory reruns.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def read_jsonl(path):
    if not path.exists():
        raise SystemExit(f"{path.name} is missing")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def main():
    queue = read_jsonl(OUT / "independent-verification-queue.jsonl")
    existing_path = OUT / "independent-verification-registry.jsonl"
    existing = {}
    if existing_path.exists():
        for row in read_jsonl(existing_path):
            if row.get("task_id"):
                existing[str(row["task_id"])] = row

    now = datetime.now(timezone.utc).isoformat()
    records = []
    for task in queue:
        tid = str(task["task_id"])
        cid = str(task["claim_id"])
        old = existing.get(tid, {})
        record = {
            "review_id": str(old.get("review_id") or "review:" + digest(tid)[:24]),
            "task_id": tid,
            "claim_id": cid,
            "source_ids": [str(x) for x in task.get("source_ids", [])],
            "status": str(old.get("status") or "UNREVIEWED"),
            "verification_status": str(old.get("verification_status") or "NOT_VERIFIED"),
            "independent": bool(old.get("independent", False)),
            "reviewer": old.get("reviewer"),
            "reviewer_role": old.get("reviewer_role"),
            "audit_reference": old.get("audit_reference"),
            "evidence_references": old.get("evidence_references") or [],
            "countercase_review": old.get("countercase_review"),
            "notes": old.get("notes"),
            "created_at": old.get("created_at") or now,
            "updated_at": now,
            "generator": "factory/verification_registry.py",
        }
        records.append(record)

    out = OUT / "independent-verification-registry.jsonl"
    out.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in records) +
        ("\n" if records else ""), encoding="utf-8"
    )
    summary = {
        "version": 1,
        "records": len(records),
        "unreviewed": sum(r["status"] == "UNREVIEWED" for r in records),
        "verified": sum(r["verification_status"] == "VERIFIED" for r in records),
        "independent_records": sum(r["independent"] is True for r in records),
        "publication_gate": "CHECK" if records else "BLOCK",
        "policy": "Registry records human/auditable review state; it does not auto-verify claims.",
    }
    (OUT / "VERIFICATION-REGISTRY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    main()
