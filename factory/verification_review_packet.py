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
    parser.add_argument(
        "--pending-first",
        action="store_true",
        help="Select the first batch of review slots that are not yet REVIEWED.",
    )
    args = parser.parse_args()

    if args.batch_size < 1 or args.batch_size > 1000:
        raise SystemExit("--batch-size must be between 1 and 1000")
    if args.offset < 0:
        raise SystemExit("--offset must be non-negative")

    queue = load_jsonl(GENERATED / "independent-verification-queue.jsonl")
    registry = load_jsonl(GENERATED / "independent-verification-registry.jsonl")
    registry_by_task = {str(r.get("task_id")): r for r in registry}

    if args.pending_first:
        pending = [
            (ordinal, task)
            for ordinal, task in enumerate(queue, start=1)
            if registry_by_task[str(task.get("task_id", ""))].get("status") != "REVIEWED"
        ]
        selected_pairs = pending[: args.batch_size]
    else:
        selected_pairs = [
            (ordinal, task)
            for ordinal, task in enumerate(
                queue[args.offset : args.offset + args.batch_size],
                start=args.offset + 1,
            )
        ]

    if not selected_pairs:
        raise SystemExit("no pending review slots remain")

    selected = [task for _, task in selected_pairs]
    packet = []
    for ordinal, task in selected_pairs:
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

    first_ordinal = selected_pairs[0][0]
    last_ordinal = selected_pairs[-1][0]
    packet_path = GENERATED / (
        f"verification-review-packet-{first_ordinal:06d}-"
        f"{last_ordinal:06d}.json"
    )
    packet_path.write_text(
        json.dumps(
            {
                "version": 1,
                "packet_range": [first_ordinal, last_ordinal],
                "records": len(packet),
                "selection_mode": "PENDING_FIRST" if args.pending_first else "OFFSET",
                "pending_slots_before_packet": sum(
                    1 for r in registry if r.get("status") != "REVIEWED"
                ),
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
                "range": [first_ordinal, last_ordinal],
                "selection_mode": "PENDING_FIRST" if args.pending_first else "OFFSET",
                "status": "READY_FOR_HUMAN_REVIEW",
                "verification_status": "NOT_PERFORMED",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
