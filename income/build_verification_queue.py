#!/usr/bin/env python3
"""Build a human-reviewable verification queue from the income opportunity intake."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "generated" / "income-opportunities.json"
OUTPUT = ROOT / "generated" / "income-verification-queue.json"

ALLOWED = {"UNVERIFIED", "SOURCE_CHECKED", "VERIFIED", "REJECTED"}


def main() -> int:
    if not INPUT.exists():
        raise SystemExit("income opportunity intake artifact is missing")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    opportunities = payload.get("opportunities", [])
    if not isinstance(opportunities, list):
        raise SystemExit("opportunities must be an array")

    checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    queue = []
    for item in opportunities:
        status = item.get("verification_status", "UNVERIFIED")
        approval = item.get("owner_approval", "PENDING")
        if status not in ALLOWED:
            raise SystemExit(f"invalid verification status: {status}")
        queue.append({
            "opportunity_id": item["id"],
            "channel": item["channel"],
            "opportunity": item["opportunity"],
            "source_url": item["source_url"],
            "discovered_at": item["discovered_at"],
            "verification_status": status,
            "owner_approval": approval,
            "verification_actions": [
                "Open and inspect the source URL.",
                "Confirm the opportunity is current and materially matches the record.",
                "Record evidence before changing verification status.",
                "Obtain owner approval before execution or commitment.",
            ],
            "evidence": [],
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "schema": "shirmani.income-verification-queue.v1",
        "generated_at": checked_at,
        "execution_policy": "verification-and-owner-approval-required",
        "items": queue,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("INCOME_VERIFICATION_QUEUE=PASS")
    print(f"ITEMS={len(queue)}")
    print("EXECUTION_GATE=OWNER_APPROVAL_REQUIRED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
