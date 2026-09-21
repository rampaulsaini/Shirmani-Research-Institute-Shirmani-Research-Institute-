#!/usr/bin/env python3
"""Fail-closed QC for generated independent-review packets.

This validator checks that every packet item is bound to the exact current
verification-queue task and that packet preparation has not been presented as
human verification. It never creates reviewer evidence or VERIFIED status.
"""
from __future__ import annotations
import argparse
import hashlib, json
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
    parser.add_argument("--packet", action="append", default=None, help="Validate only these packet paths; repeatable.")
    args = parser.parse_args()

    queue = load_jsonl(GENERATED / "independent-verification-queue.jsonl")
    registry = load_jsonl(GENERATED / "independent-verification-registry.jsonl")
    if args.packet:
        packets = [Path(p) if Path(p).is_absolute() else ROOT / p for p in args.packet]
    else:
        packets = sorted(GENERATED.glob("verification-review-packet-*.json"))
    queue_by_id = {str(r.get("task_id")): r for r in queue}
    registry_by_id = {str(r.get("task_id")): r for r in registry}
    errors, checked_items = [], 0

    if not packets:
        raise SystemExit("no generated verification review packet found")

    for packet_path in packets:
        try:
            packet = json.loads(packet_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append({"packet": packet_path.name, "error": "invalid_json:" + str(exc)})
            continue

        if packet.get("status") != "READY_FOR_HUMAN_REVIEW":
            errors.append({"packet": packet_path.name, "error": "invalid_packet_status"})
        if packet.get("verification_status") not in (None, "NOT_PERFORMED"):
            errors.append({"packet": packet_path.name, "error": "packet_claims_verification"})
        items = packet.get("items")
        if not isinstance(items, list) or not items:
            errors.append({"packet": packet_path.name, "error": "missing_items"})
            continue

        for item in items:
            checked_items += 1
            task_id = str(item.get("task_id", ""))
            task = queue_by_id.get(task_id)
            registry_record = registry_by_id.get(task_id)
            if task is None:
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "task_not_in_current_queue"})
                continue
            if registry_record is None:
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "task_not_in_current_registry"})
                continue
            if item.get("task_hash") != task_hash(task):
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "task_hash_mismatch"})
            if item.get("claim_id") != str(task.get("claim_id", "")):
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "claim_id_mismatch"})
            if item.get("current_status") != registry_record.get("status"):
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "registry_status_mismatch"})
            if item.get("current_verification_status") != registry_record.get("verification_status"):
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "registry_verification_status_mismatch"})
            template = item.get("review_template") or {}
            if template.get("reviewer") is not None or template.get("reviewer_role") is not None:
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "invented_reviewer_state"})
            if template.get("reviewed_at") is not None or template.get("reviewer_conclusion") is not None:
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "invented_review_state"})
            if (template.get("countercase_review") or {}).get("status") != "NOT_REVIEWED":
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "countercase_not_fail_closed"})
            if (template.get("reproduction_or_test") or {}).get("status") != "NOT_RUN":
                errors.append({"packet": packet_path.name, "task_id": task_id, "error": "reproduction_not_fail_closed"})

    report = {
        "version": 1,
        "packets": len(packets),
        "scope": "explicit" if args.packet else "all",
        "checked_items": checked_items,
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK",
        "status": "PACKET_INTEGRITY_PASS" if not errors else "PACKET_INTEGRITY_BLOCKED",
        "policy": "Packet integrity is not human verification; all missing review evidence remains fail-closed."
    }
    (GENERATED / "VERIFICATION-PACKET-QC.json").write_text(
        json.dumps({**report, "errors": errors}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
