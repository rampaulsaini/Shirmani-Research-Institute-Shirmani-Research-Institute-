#!/usr/bin/env python3
"""Deterministic, source-backed opportunity intake for the Income Command Center.

This module does not scrape, invent, score, or execute opportunities. It validates
operator-supplied source records and normalizes them into an auditable queue.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "income" / "opportunity-schema.json"
SEED = ROOT / "income" / "opportunity-sources.json"
OUT = ROOT / "generated" / "income-opportunities.json"

REQUIRED = {
    "id", "channel", "opportunity", "source_url", "discovered_at",
    "fit_reason", "estimated_effort", "estimated_value", "risk",
    "next_action", "verification_status", "owner_approval",
}
CHANNELS = {
    "employment", "freelancing", "ai_marketing",
    "digital_store", "yatharth_music", "economic_vision",
}
STATUSES = {"UNVERIFIED", "SOURCE_CHECKED", "VERIFIED", "REJECTED"}
APPROVALS = {"PENDING", "APPROVED", "DECLINED"}


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(item: dict) -> list[str]:
    errors = []
    missing = REQUIRED - item.keys()
    if missing:
        errors.append("missing=" + ",".join(sorted(missing)))
    if item.get("channel") not in CHANNELS:
        errors.append("invalid_channel")
    if not valid_url(str(item.get("source_url", ""))):
        errors.append("invalid_source_url")
    if item.get("verification_status") not in STATUSES:
        errors.append("invalid_verification_status")
    if item.get("owner_approval") not in APPROVALS:
        errors.append("invalid_owner_approval")
    return errors


def main() -> int:
    if not SEED.exists():
        raise SystemExit("income/opportunity-sources.json is required; no opportunities fabricated")
    records = json.loads(SEED.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise SystemExit("opportunity sources must be a JSON array")

    normalized = []
    rejected = []
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    for item in records:
        item = dict(item)
        errors = validate(item)
        if errors:
            rejected.append({"record": item, "errors": errors})
            continue
        # Intake never upgrades verification or approval state.
        item["verification_status"] = "UNVERIFIED"
        item["owner_approval"] = "PENDING"
        item["intake_checked_at"] = now
        normalized.append(item)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "schema": "shirmani.income-opportunity-queue.v1",
        "generated_at": now,
        "opportunities": normalized,
        "rejected_records": rejected,
        "counts": {
            "accepted": len(normalized),
            "rejected": len(rejected),
            "total": len(records),
        },
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"INCOME_OPPORTUNITY_INTAKE=PASS")
    print(f"ACCEPTED={len(normalized)}")
    print(f"REJECTED={len(rejected)}")
    print("VERIFICATION_DEFAULT=UNVERIFIED")
    print("OWNER_APPROVAL_DEFAULT=PENDING")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
