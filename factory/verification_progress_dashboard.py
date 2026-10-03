#!/usr/bin/env python3
"""Generate the authoritative, quantitative, fail-closed verification dashboard."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "generated/VERIFICATION-QUEUE.json"
REGISTRY = ROOT / "generated/VERIFICATION-REGISTRY.json"
PROMOTION = ROOT / "generated/VERIFICATION-PROMOTION-QC.json"
SAMPLE = ROOT / "generated/independent-verification-status-2026-09-29.json"
OUT = ROOT / "generated/verification-progress-dashboard.json"
OUT_MD = ROOT / "generated/verification-progress-dashboard.md"

def read_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing required status file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def bar(percent: float, width: int = 30) -> str:
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)

def main() -> int:
    target = read_json(TARGET)
    registry = read_json(REGISTRY)
    promotion = read_json(PROMOTION)
    sample = read_json(SAMPLE) if SAMPLE.exists() else {}

    total = int(target.get("records", 0))
    queued = int(target.get("queued", 0))
    reviewed = int(registry.get("reviewed", 0))
    verified = int(registry.get("verified", 0))

    if min(total, queued, reviewed, verified) < 0:
        raise SystemExit("Negative verification counters are invalid.")
    if queued > total or reviewed > total or verified > reviewed:
        raise SystemExit("Verification counters violate monotonic invariants.")
    if int(promotion.get("verified_records", 0)) != verified:
        raise SystemExit("Registry/promotion verified counts do not match.")
    if int(promotion.get("queue_records", total)) != total:
        raise SystemExit("Promotion/queue record counts do not match.")

    remaining = max(total - verified, 0)
    queued_pct = round(queued / total * 100, 4) if total else 0.0
    reviewed_pct = round(reviewed / total * 100, 4) if total else 0.0
    verified_pct = round(verified / total * 100, 4) if total else 0.0
    remaining_pct = round(remaining / total * 100, 4) if total else 0.0
    generated = datetime.now(timezone.utc).isoformat()

    # Keep the persisted dashboard deterministic when the authoritative state
    # has not changed. This prevents the five-minute workflow from creating a
    # new commit solely because generated_at changed.
    previous_generated = None
    if OUT.exists():
        try:
            previous = json.loads(OUT.read_text(encoding="utf-8"))
            previous_generated = previous.get("generated_at")
        except (OSError, ValueError, TypeError):
            previous_generated = None

    dashboard = {
        "generated_at": generated,
        "method": "authoritative aggregate queue + fail-closed promotion state",
        "records": {"target": total, "queued": queued, "reviewed": reviewed,
                    "verified": verified, "remaining_to_verified_target": remaining},
        "percent": {"queued_of_target": queued_pct, "reviewed_of_target": reviewed_pct,
                    "independently_verified_of_target": verified_pct,
                    "remaining_of_target": remaining_pct},
        "automation_state": {
            "independent_verification_required": True,
            "automission_may_declare_verified": False,
            "promotion_gate": promotion.get("promotion_gate", promotion.get("publication_gate")),
            "publication_gate": target.get("publication_gate"),
        },
        "sample_reference": {
            "sample_records": int((sample.get("verification_summary") or {}).get("queue_records", 0)),
            "sample_verified": int((sample.get("verification_summary") or {}).get("independently_verified_records", 0)),
            "note": "Legacy 10-record sample is informational only and is not the authoritative denominator.",
        },
        "next_gate": (
            "Independent review records with evidence, counter-evidence, reproducible test and audit "
            "must be completed before VERIFIED promotion."
            if verified < total else "Target reached."
        ),
    }
    if previous_generated:
        previous = json.loads(OUT.read_text(encoding="utf-8"))
        current_state = dict(dashboard)
        previous_state = dict(previous)
        current_state.pop("generated_at", None)
        previous_state.pop("generated_at", None)
        if current_state == previous_state:
            dashboard["generated_at"] = previous_generated

    OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = f"""# ꙰ SHIRMANI Verification Progress Dashboard

Generated: {generated}

## Authoritative target

**{verified:,} / {total:,} independently VERIFIED ({verified_pct:g}%)**

### Graph map

- Queue prepared: **{queued:,}/{total:,} ({queued_pct:g}%)**  {bar(queued_pct)}
- Reviews completed: **{reviewed:,}/{total:,} ({reviewed_pct:g}%)**  {bar(reviewed_pct)}
- Independently VERIFIED: **{verified:,}/{total:,} ({verified_pct:g}%)**  {bar(verified_pct)}
- Remaining to target: **{remaining:,}/{total:,} ({remaining_pct:g}%)**  {bar(remaining_pct)}

## Control state

- Publication gate: **{target.get("publication_gate")}**
- Promotion gate: **{promotion.get("promotion_gate", promotion.get("publication_gate"))}**
- Automation may prepare: **YES**
- Automation may declare VERIFIED: **NO**
- Independent review required: **YES**

## Integrity rule

Workflow success, queue generation, evidence collection, or generated packets do not by themselves constitute independent verification. VERIFIED requires the defined independent-review evidence, counter-evidence, reproducible test/observation, reviewer provenance, timestamp, and audit record.

## Next gate

{dashboard["next_gate"]}
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
