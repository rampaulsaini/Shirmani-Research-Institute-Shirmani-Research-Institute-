#!/usr/bin/env python3
"""Validate and normalize source-backed income opportunities.

No ranking, scoring, scraping, financial action, or approval is performed here.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "income" / "opportunity-sources.json"
OUT = ROOT / "generated" / "income-opportunities.json"

CHANNELS = (
    "employment",
    "freelancing",
    "ai_marketing",
    "digital_store",
    "yatharth_music",
    "economic_vision",
)
REQUIRED = {
    "id", "channel", "opportunity", "source_url", "discovered_at",
    "fit_reason", "estimated_effort", "estimated_value", "risk",
    "next_action",
}
HTTP_SCHEMES = {"http", "https"}


def is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in HTTP_SCHEMES and bool(parsed.netloc)


def validate(record: dict) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED - record.keys())
    if missing:
        errors.append("missing:" + ",".join(missing))
    if record.get("channel") not in CHANNELS:
        errors.append("invalid_channel")
    if not is_http_url(record.get("source_url")):
        errors.append("invalid_source_url")
    return errors


def main() -> int:
    if not SEED.exists():
        raise SystemExit("source file missing; no opportunity records will be fabricated")
    raw = json.loads(SEED.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise SystemExit("source file must contain a JSON array")

    accepted: list[dict] = []
    rejected: list[dict] = []
    seen: set[str] = set()
    checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    for record in raw:
        if not isinstance(record, dict):
            rejected.append({"record": record, "errors": ["record_not_object"]})
            continue
        item = dict(record)
        errors = validate(item)
        if item.get("id") in seen:
            errors.append("duplicate_id")
        if item.get("id"):
            seen.add(str(item["id"]))
        if errors:
            rejected.append({"record": item, "errors": errors})
            continue

        item["verification_status"] = "UNVERIFIED"
        item["owner_approval"] = "PENDING"
        item["intake_checked_at"] = checked_at
        accepted.append(item)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "schema": "shirmani.income-opportunity-queue.v1",
                "generated_at": checked_at,
                "source_policy": "source-backed-only",
                "opportunities": accepted,
                "rejected_records": rejected,
                "counts": {
                    "accepted": len(accepted),
                    "rejected": len(rejected),
                    "total": len(raw),
                },
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print("INCOME_OPPORTUNITY_INTAKE=PASS")
    print(f"ACCEPTED={len(accepted)}")
    print(f"REJECTED={len(rejected)}")
    print("STATUS_POLICY=UNVERIFIED_PENDING")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
