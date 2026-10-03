#!/usr/bin/env python3
"""Build an exact, fail-closed verification progress map.

This is a measurement layer only. It never promotes a record to VERIFIED.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
TARGET = 100200

def main():
    registry_path = OUT / "VERIFICATION-REGISTRY.json"
    promotion_path = OUT / "VERIFICATION-PROMOTION-QC.json"
    if not registry_path.exists() or not promotion_path.exists():
        raise SystemExit("verification registry/QC artifacts are missing")

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    promotion = json.loads(promotion_path.read_text(encoding="utf-8"))

    total = int(registry.get("records", 0))
    queued = int(registry.get("queued", 0))
    reviewed = int(registry.get("reviewed", 0))
    verified = int(registry.get("verified", 0))

    if total < 0 or any(x < 0 for x in (queued, reviewed, verified)):
        raise SystemExit("negative verification counts are invalid")
    if reviewed + queued > total or verified > reviewed:
        raise SystemExit("verification counts are internally inconsistent")
    if int(promotion.get("verified_records", -1)) != verified:
        raise SystemExit("promotion QC verified count does not match registry")

    progress = round(verified / TARGET * 100, 4)
    reviewed_progress = round(reviewed / TARGET * 100, 4)
    remaining = max(TARGET - verified, 0)

    report = {
        "version": 1,
        "target_verified_records": TARGET,
        "current_total_review_tasks": total,
        "queued_records": queued,
        "reviewed_records": reviewed,
        "verified_records": verified,
        "remaining_to_target": remaining,
        "verified_progress_percent": progress,
        "reviewed_progress_percent": reviewed_progress,
        "status": "COMPLETE" if verified >= TARGET else "HUMAN_REVIEW_REQUIRED",
        "independent_verification_is_not_automated": True,
        "promotion_gate": promotion.get("publication_gate"),
        "integrity_rule": "Workflow success, QC PASS, provenance and queue creation do not equal independent verification.",
    }

    (OUT / "VERIFICATION-PROGRESS.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
