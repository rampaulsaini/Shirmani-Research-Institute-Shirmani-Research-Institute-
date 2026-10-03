#!/usr/bin/env python3
"""Generate the authoritative, quantitative, fail-closed verification dashboard.

The 100,200-record verification queue is the authoritative target. The older
10-record independent-verification sample is retained only as a reference
sample and must never replace the authoritative denominator.
"""
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

def read_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing required status file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

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

    remaining = max(total - verified, 0)
    dashboard = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": "authoritative aggregate queue + fail-closed promotion state",
        "records": {
            "target": total,
            "queued": queued,
            "reviewed": reviewed,
            "verified": verified,
            "remaining_to_verified_target": remaining,
        },
        "percent": {
            "queued_of_target": round(queued / total * 100, 4) if total else 0.0,
            "reviewed_of_target": round(reviewed / total * 100, 4) if total else 0.0,
            "independently_verified_of_target": round(verified / total * 100, 4) if total else 0.0,
            "remaining_of_target": round(remaining / total * 100, 4) if total else 0.0,
        },
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
    OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
