#!/usr/bin/env python3
"""Reconcile private sent-mail/reply CSV exports against the public prospect queue.

This tool is offline-only. It never sends messages, accesses accounts, or proves that
a reply is a qualified enquiry, order, payment, or revenue. Keep source exports private.
The output intentionally excludes names, addresses, subjects, message bodies and phone
numbers so that only the sanitized summary is suitable for controlled reporting.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ALIASES = {
    "prospect_id": ("prospect_id", "prospect id", "lead_id", "lead id"),
    "email": ("email", "contact_email", "recipient_email", "recipient", "to", "to_email", "from", "from_email", "sender_email"),
    "recipient": ("recipient_email", "recipient", "to", "to_email", "email"),
    "sender": ("sender_email", "sender", "from", "from_email", "email"),
    "sent_at": ("sent_at", "sent date", "date_sent", "timestamp", "date", "received_at", "reply_date"),
    "message_id": ("message_id", "message-id", "internet_message_id"),
    "thread_id": ("thread_id", "conversation_id", "conversation id"),
    "in_reply_to": ("in_reply_to", "in-reply-to", "reply_to_message_id"),
    "subject": ("subject", "topic"),
}


def norm_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().casefold()).strip("_")


def email_from_row(row: dict[str, Any]) -> str:
    # Some existing queue records store a published contact address in a notes cell
    # instead of a dedicated email column. Only use a single unambiguous address.
    matches = {
        address.casefold()
        for value in row.values()
        for address in re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+[.][A-Z]{2,}", str(value or ""), re.IGNORECASE)
    }
    return next(iter(matches)) if len(matches) == 1 else ""


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError(f"{path}: CSV header row is missing")
        header_map = {norm_header(name): name for name in reader.fieldnames if name}
        rows = []
        for raw in reader:
            rows.append({
                key: str(raw.get(header_map.get(key, ""), "") or "").strip()
                for key in {alias for aliases in ALIASES.values() for alias in aliases}
            } | {
                "_prospect_id": get_field(raw, header_map, "prospect_id"),
                "_recipient_email": get_field(raw, header_map, "recipient").casefold(),
                "_sender_email": get_field(raw, header_map, "sender").casefold(),
                "_email": get_field(raw, header_map, "email").casefold() or email_from_row(raw),
                "_sent_at": get_field(raw, header_map, "sent_at"),
                "_message_id": get_field(raw, header_map, "message_id").casefold(),
                "_thread_id": get_field(raw, header_map, "thread_id").casefold(),
                "_in_reply_to": get_field(raw, header_map, "in_reply_to").casefold(),
                "_subject": get_field(raw, header_map, "subject").casefold(),
            })
    return rows, list(header_map)


def get_field(row: dict[str, Any], header_map: dict[str, str], field: str) -> str:
    for alias in ALIASES[field]:
        key = norm_header(alias)
        if key in header_map:
            return str(row.get(header_map[key], "") or "").strip()
    return ""


def unique_email_index(queue: list[dict[str, str]]) -> dict[str, str]:
    found: dict[str, set[str]] = defaultdict(set)
    for row in queue:
        if row["_email"] and row["_prospect_id"]:
            found[row["_email"]].add(row["_prospect_id"])
    return {email: next(iter(ids)) for email, ids in found.items() if len(ids) == 1}


def match_prospect(row: dict[str, str], valid_ids: set[str], email_index: dict[str, str]) -> str | None:
    direct = row.get("_prospect_id", "").strip()
    if direct in valid_ids:
        return direct
    email = row.get("_email", "").casefold().strip()
    return email_index.get(email) if email else None


def dedupe_key(row: dict[str, str], prefix: str) -> tuple[str, ...]:
    message_id = row.get("_message_id", "")
    if message_id:
        return (prefix, message_id)
    return (
        prefix,
        row.get("_prospect_id", ""),
        row.get("_email", ""),
        row.get("_sent_at", ""),
        row.get("_thread_id", ""),
        row.get("_in_reply_to", ""),
        row.get("_subject", ""),
    )


def reconcile(queue_path: Path, sent_path: Path, replies_path: Path) -> dict[str, Any]:
    queue, queue_headers = read_csv(queue_path)
    sent, sent_headers = read_csv(sent_path)
    replies, reply_headers = read_csv(replies_path)

    queue_ids = {row["_prospect_id"] for row in queue if row["_prospect_id"]}
    if not queue_ids:
        raise ValueError("Queue must contain a prospect_id column and at least one ID")

    email_index = unique_email_index(queue)
    for row in sent:
        row["_email"] = row["_recipient_email"] or row["_email"]
    for row in replies:
        row["_email"] = row["_sender_email"] or row["_email"]

    sent_seen: set[tuple[str, ...]] = set()
    sent_by_prospect: Counter[str] = Counter()
    sent_by_thread: dict[str, set[str]] = defaultdict(set)
    sent_by_message: dict[str, set[str]] = defaultdict(set)
    unmatched_sent = 0
    invalid_sent = 0

    for row in sent:
        # A sent-mail export must contain a sent timestamp; drafts do not count.
        if not row["_sent_at"]:
            invalid_sent += 1
            continue
        key = dedupe_key(row, "sent")
        if key in sent_seen:
            continue
        sent_seen.add(key)
        prospect = match_prospect(row, queue_ids, email_index)
        if not prospect:
            unmatched_sent += 1
            continue
        sent_by_prospect[prospect] += 1
        if row["_thread_id"]:
            sent_by_thread[row["_thread_id"]].add(prospect)
        if row["_message_id"]:
            sent_by_message[row["_message_id"]].add(prospect)

    reply_seen: set[tuple[str, ...]] = set()
    replies_by_prospect: Counter[str] = Counter()
    unmatched_replies = 0
    invalid_replies = 0
    for row in replies:
        # A received-replies export must contain a received timestamp.
        if not row["_sent_at"]:
            invalid_replies += 1
            continue
        key = dedupe_key(row, "reply")
        if key in reply_seen:
            continue
        reply_seen.add(key)

        candidates: set[str] = set()
        if row["_in_reply_to"]:
            candidates |= sent_by_message.get(row["_in_reply_to"], set())
        if row["_thread_id"]:
            candidates |= sent_by_thread.get(row["_thread_id"], set())
        prospect = next(iter(candidates)) if len(candidates) == 1 else None
        if not prospect:
            prospect = match_prospect(row, queue_ids, email_index)
        if not prospect:
            unmatched_replies += 1
            continue
        replies_by_prospect[prospect] += 1

    per_prospect = []
    for prospect_id in sorted(queue_ids):
        sent_count = sent_by_prospect[prospect_id]
        reply_count = replies_by_prospect[prospect_id]
        if reply_count:
            status = "REPLY_EVIDENCE"
        elif sent_count:
            status = "SENT_EVIDENCE"
        else:
            status = "NO_MATCHED_EVIDENCE"
        per_prospect.append({
            "prospect_id": prospect_id,
            "sent_message_count": sent_count,
            "reply_message_count": reply_count,
            "evidence_status": status,
        })

    return {
        "schema_version": 1,
        "report_type": "private_outreach_export_reconciliation",
        "source_file_roles": ["prospect_queue_csv", "sent_export_csv", "received_replies_csv"],
        "input_rows": {
            "queue": len(queue),
            "sent_export": len(sent),
            "received_replies_export": len(replies),
        },
        "matched_evidence": {
            "unique_sent_messages": sum(sent_by_prospect.values()),
            "prospects_with_sent_evidence": sum(1 for count in sent_by_prospect.values() if count),
            "unique_received_replies": sum(replies_by_prospect.values()),
            "prospects_with_reply_evidence": sum(1 for count in replies_by_prospect.values() if count),
        },
        "unmatched_or_invalid": {
            "unmatched_sent_rows": unmatched_sent,
            "sent_rows_missing_timestamp": invalid_sent,
            "unmatched_reply_rows": unmatched_replies,
            "reply_rows_missing_timestamp": invalid_replies,
        },
        "input_schema": {
            "queue_headers": queue_headers,
            "sent_export_headers": sent_headers,
            "received_replies_headers": reply_headers,
        },
        "prospects": per_prospect,
        "claims_not_established": [
            "qualified enquiry",
            "accepted proposal or order",
            "payment received",
            "delivery or client acceptance",
            "independent verification",
        ],
        "privacy_note": "Raw exports, contact details, subjects and message bodies are not copied into this report. Keep all source exports and this report private; never commit real customer records to a public repository.",
        "matching_note": "Matches use an explicit prospect ID or a unique email address in the queue. Ambiguous or absent matches remain unmatched. Replies are evidence of a received message only, not proof of purchase intent.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", required=True, type=Path, help="Prospect queue CSV")
    parser.add_argument("--sent", required=True, type=Path, help="CSV exported from the Sent folder (not drafts)")
    parser.add_argument("--replies", required=True, type=Path, help="CSV exported from received replies")
    parser.add_argument("--output", required=True, type=Path, help="Private output JSON path; keep outside the public repository")
    args = parser.parse_args()
    for path in (args.queue, args.sent, args.replies):
        if not path.is_file():
            parser.error(f"input file not found: {path}")
    try:
        report = reconcile(args.queue, args.sent, args.replies)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"OUTREACH RECONCILIATION: FAILED — {exc}", file=sys.stderr)
        return 2
    print("OUTREACH RECONCILIATION: COMPLETE")
    print(json.dumps({
        "output": str(args.output),
        "matched_sent_messages": report["matched_evidence"]["unique_sent_messages"],
        "matched_received_replies": report["matched_evidence"]["unique_received_replies"],
        "unmatched_or_invalid": report["unmatched_or_invalid"],
        "income_claimed": False,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
