#!/usr/bin/env python3
"""Sequential hash-bound Heart-View review conveyor.

Prepares the first missing 25-record review packet, validates it, and records
a durable continuation state. It never performs or fabricates human review.
"""
from __future__ import annotations
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
TOTAL = 100200
BATCH = 25
PATTERN = re.compile(r"verification-review-packet-(\d{6})-(\d{6})\.json$")

def existing_ranges():
    ranges = []
    for p in GENERATED.glob("verification-review-packet-*.json"):
        m = PATTERN.match(p.name)
        if m:
            ranges.append((int(m.group(1)), int(m.group(2))))
    return sorted(ranges)

def first_missing_offset():
    covered = set()
    for start, end in existing_ranges():
        covered.update(range(start, end + 1))
    for position in range(1, TOTAL + 1):
        if position not in covered:
            return position - 1
    return None

def main():
    GENERATED.mkdir(parents=True, exist_ok=True)
    offset = first_missing_offset()
    now = datetime.now(timezone.utc).isoformat()

    if offset is None:
        state = {
            "version": 1,
            "generated_at": now,
            "status": "COMPLETE",
            "queue_total": TOTAL,
            "prepared_records": TOTAL,
            "next_offset": None,
            "human_verification": "NOT_PERFORMED",
            "policy": "Packet preparation is not verification."
        }
        (GENERATED / "auto-review-state.json").write_text(
            json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(json.dumps(state, ensure_ascii=False))
        return

    end = min(offset + BATCH, TOTAL)
    subprocess.run(
        ["python3", str(ROOT / "factory" / "verification_review_packet.py"),
         "--batch-size", str(end - offset), "--offset", str(offset)],
        cwd=ROOT, check=True
    )
    packet = GENERATED / f"verification-review-packet-{offset+1:06d}-{end:06d}.json"
    subprocess.run(
        ["python3", str(ROOT / "factory" / "verification_review_packet_qc.py"),
         "--packet", str(packet)],
        cwd=ROOT, check=True
    )

    state = {
        "version": 1,
        "generated_at": now,
        "status": "READY_FOR_HUMAN_REVIEW",
        "queue_total": TOTAL,
        "prepared_through": end,
        "prepared_percentage": round(end / TOTAL * 100, 5),
        "packet": str(packet.relative_to(ROOT)),
        "packet_range": [offset + 1, end],
        "packet_records": end - offset,
        "human_verification": "NOT_PERFORMED",
        "verified_records": 0,
        "next_offset": end,
        "policy": "Preserve first. Reason second. Verify third. Transform only as a traceable derivative."
    }
    (GENERATED / "auto-review-state.json").write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    qc = ROOT / f"CONTINUATION-REVIEW-SLICE-{offset+1:06d}-{end:06d}-QC.md"
    qc.write_text(
        f"# SHIRMANI HEART-VIEW — REVIEW SLICE {offset+1}–{end}\n\n"
        f"- Packet: {packet.relative_to(ROOT).as_posix()}\n"
        f"- Records: {end-offset}\n"
        f"- Prepared through: {end} / {TOTAL} = {end/TOTAL*100:.5f}%\n"
        f"- Packet status: READY_FOR_HUMAN_REVIEW\n"
        f"- Packet QC: PASS\n"
        f"- Human verification: NOT PERFORMED\n"
        f"- VERIFIED promotion: 0\n\n"
        "**Preserve first. Reason second. Verify third. Transform only as a traceable derivative.**\n",
        encoding="utf-8"
    )
    print(json.dumps(state, ensure_ascii=False))

if __name__ == "__main__":
    main()
