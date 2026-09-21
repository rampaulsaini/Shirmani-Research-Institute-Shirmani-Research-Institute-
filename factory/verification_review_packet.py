#!/usr/bin/env python3
"""Build a deterministic, hash-bound human verification review packet.

This tool prepares review work; it never fabricates evidence, reviewers, tests,
or VERIFIED status. It reads the current verification queue and registry and
emits a small review packet whose task identity is bound to the exact queue
record hash.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"


def task_hash(task: dict) -> str:
    payload = json.dumps(task, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")
    records = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSON at {path}:{line_no}: {exc}") from exc
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--offset", type=int, default=0)
    args = parser.parse_args()

    if args.batch_size < 1 or args.batch_size > 1000:
        raise SystemExit("--batch-size must be between 1 and 1000")
    if args.offset < 0:
        raise SystemExit("--offset must be non-negative")

    queue = load_jsonl(GENERATED / "independent-verification-queue.jsonl")
    registry = load_jsonl(GENERATED / "independent-verification-registry.jsonl")
    registry_by_task = {str(r.get("task_id")): r for r in registry}

    selected = queue[args.offset : args.offset + args.batch_size]
    if not selected:
        raise SystemExit("requested review packet is empty")

    packet = []
    for ordinal, task in enumerate(selected, start=args.offset + 1):
        task_id = str(task.get("task_id", ""))
        if not task_id:
            raise SystemExit(f"queue record {ordinal} has no task_id")
        registry_record = registry_by_task.get(task_id)
        if registry_record is None:
            raise SystemExit(f"no registry record for {task_id}")

        packet.append(
            {
                "packet_ordinal": ordinal,
                "task_id": task_id,
                "task_hash": task_hash(task),
                "claim_id": str(task.get("claim_id", "")),
                "source_ids": list(task.get("source_ids") or []),
                "verification_questions": list(task.get("verification_questions") or []),
                "current_status": registry_record.get("status", "UNKNOWN"),
                "current_verification_status": registry_record.get(
                    "verification_status", "UNKNOWN"
                ),
                "review_template": {
                    "exact_claim": None,
                    "definitions": [],
                    "evidence_references": [],
                    "countercase_review": {
                        "status": "NOT_REVIEWED",
                        "references": [],
                    },
                    "reproduction_or_test": {
                        "status": "NOT_RUN",
                        "references": [],
                    },
                    "uncertainty": [],
                    "reviewer": None,
                    "reviewer_role": None,
                    "reviewed_at": None,
                    "reviewer_conclusion": None,
                    "audit_notes": [],
                },
                "policy": (
                    "Packet preparation is not verification. Do not populate "
                    "review fields from inference or invention."
                ),
            }
        )

    packet_path = GENERATED / (
        f"verification-review-packet-{args.offset + 1:06d}-"
        f"{args.offset + len(selected):06d}.json"
    )
    packet_path.write_text(
        json.dumps(
            {
                "version": 1,
                "packet_range": [args.offset + 1, args.offset + len(selected)],
                "records": len(packet),
                "source": "generated/independent-verification-queue.jsonl",
                "registry": "generated/independent-verification-registry.jsonl",
                "status": "READY_FOR_HUMAN_REVIEW",
                "verified_records": 0,
                "items": packet,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "packet": packet_path.relative_to(ROOT).as_posix(),
                "records": len(packet),
                "range": [args.offset + 1, args.offset + len(selected)],
                "status": "READY_FOR_HUMAN_REVIEW",
                "verification_status": "NOT_PERFORMED",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
