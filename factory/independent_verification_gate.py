#!/usr/bin/env python3
"""Fail-closed counter for independently VERIFIED claim/evidence records."""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "generated" / "claim-evidence.jsonl"
OUT = ROOT / "generated" / "independent-verification-status.json"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    if path.exists():
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
    return h.hexdigest()

def main() -> int:
    counts = {"total": 0, "verified": 0, "unverified": 0, "review": 0, "blocked": 0}
    if SOURCE.exists():
        with SOURCE.open("r", encoding="utf-8") as f:
            for raw in f:
                if not raw.strip():
                    continue
                counts["total"] += 1
                try:
                    state = str(json.loads(raw).get("verification_state", "UNVERIFIED")).upper()
                except (json.JSONDecodeError, TypeError):
                    state = "BLOCKED"
                if state == "VERIFIED":
                    counts["verified"] += 1
                elif state == "REVIEW":
                    counts["review"] += 1
                elif state == "BLOCKED":
                    counts["blocked"] += 1
                else:
                    counts["unverified"] += 1

    total = counts["total"]
    pct = round(100 * counts["verified"] / total, 4) if total else 0.0
    status = "NO_RECORDS" if total == 0 else ("VERIFIED_DATA_PRESENT" if counts["verified"] else "PARTIAL")
    report = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {"path": "generated/claim-evidence.jsonl", "sha256": sha256_file(SOURCE)},
        "records_total": total,
        "verified_records": counts["verified"],
        "unverified_records": counts["unverified"],
        "review_records": counts["review"],
        "blocked_records": counts["blocked"],
        "verification_percent": pct,
        "status": status,
        "integrity": {
            "fail_closed": True,
            "workflow_success_is_not_verification": True,
            "empty_source_is_zero_verified": True
        }
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
