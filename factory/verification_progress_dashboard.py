#!/usr/bin/env python3
"""Generate the authoritative fail-closed SHIRMANI verification dashboard."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "generated/VERIFICATION-QUEUE.json"
REGISTRY = ROOT / "generated/VERIFICATION-REGISTRY.json"
PROMOTION = ROOT / "generated/VERIFICATION-PROMOTION-QC.json"
OUT = ROOT / "generated/verification-progress-dashboard.json"
OUT_MD = ROOT / "generated/verification-progress-dashboard.md"

def read_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing required authoritative status file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def bar(percent: float, width: int = 30) -> str:
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)

def main() -> int:
    queue = read_json(QUEUE)
    registry = read_json(REGISTRY)
    promotion = read_json(PROMOTION)

    target = int(queue.get("records", 0))
    queued = int(queue.get("queued", 0))
    reviewed = int(registry.get("reviewed", 0))
    verified = int(registry.get("verified", 0))
    promotion_verified = int(promotion.get("verified_records", 0))

    if target < 0 or queued < 0 or reviewed < 0 or verified < 0:
        raise SystemExit("Negative verification counters are invalid.")
    if queued > target or reviewed > target or verified > reviewed:
        raise SystemExit("Verification counters violate monotonic invariants.")
    if verified != promotion_verified:
        raise SystemExit(
            f"Registry/promotion mismatch: registry verified={verified}, "
            f"promotion verified={promotion_verified}"
        )

    remaining = target - verified
    queued_pct = round(queued / target * 100, 6) if target else 0.0
    reviewed_pct = round(reviewed / target * 100, 6) if target else 0.0
    verified_pct = round(verified / target * 100, 6) if target else 0.0
    remaining_pct = round(remaining / target * 100, 6) if target else 0.0
    generated = datetime.now(timezone.utc).isoformat()

    dashboard = {
        "generated_at": generated,
        "method": "authoritative verification queue, review registry and promotion QC; fail-closed",
        "target": target,
        "records": {
            "target": target,
            "queued": queued,
            "reviewed": reviewed,
            "verified": verified,
            "remaining_to_verified_target": remaining,
            "promotion_verified": promotion_verified
        },
        "percent": {
            "queued_of_target": queued_pct,
            "reviewed_of_target": reviewed_pct,
            "independently_verified_of_target": verified_pct,
            "remaining_of_target": remaining_pct
        },
        "automation_state": {
            "independent_verification_required": True,
            "automission_may_prepare": True,
            "automission_may_declare_verified": False,
            "independent_reviewer_decision_required": True
        },
        "next_gate": (
            "Complete independent review for queued records; each VERIFIED "
            "promotion requires evidence, counter-evidence, reproducible test, "
            "reviewer provenance, timestamp, and audit."
            if verified < target else "Target reached."
        )
    }
    OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = f"""# ꙰ SHIRMANI Verification Progress Dashboard

Generated: {generated}

## Authoritative target

**{verified:,} / {target:,} independently VERIFIED ({verified_pct:g}%)**

### Graph map

- Verification queue: **{queued:,}/{target:,} ({queued_pct:g}%)**  {bar(queued_pct)}
- Reviewed records: **{reviewed:,}/{target:,} ({reviewed_pct:g}%)**  {bar(reviewed_pct)}
- Independently VERIFIED: **{verified:,}/{target:,} ({verified_pct:g}%)**  {bar(verified_pct)}
- Remaining to target: **{remaining:,}/{target:,} ({remaining_pct:g}%)**  {bar(remaining_pct)}

## Authoritative current state

- Queue records: **{target:,}**
- Queued: **{queued:,}**
- Reviewed: **{reviewed:,}**
- Independently VERIFIED: **{verified:,}**
- Promotion-QC verified: **{promotion_verified:,}**

## Control state

- Automation may prepare: **YES**
- Automation may declare VERIFIED: **NO**
- Independent review required: **YES**
- Fail-closed promotion: **ENFORCED**

## Integrity rule

Workflow success, queue generation, evidence collection, generated packets,
or review-slot creation do not by themselves constitute independent
verification. VERIFIED requires an explicit independent-review decision with
the defined evidence, counter-evidence, reproducible test/observation,
reviewer provenance, timestamp, and audit record.

## Next gate

{dashboard["next_gate"]}
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
