#!/usr/bin/env python3
"""Conservative inventory of explicit verification states."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "independent-verification-audit.json"
SCAN_DIRS = ("generated", "evidence", "federation", "research")
TARGET = 100_200
STATES = ("REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED")

def iter_json_files():
    seen = set()
    for name in SCAN_DIRS:
        base = ROOT / name
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix.lower() in {".json", ".jsonl", ".ndjson"}:
                rp = p.resolve()
                if rp not in seen:
                    seen.add(rp)
                    yield p

def records_from(path: Path):
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return
    if path.suffix.lower() in {".jsonl", ".ndjson"}:
        for line in raw.splitlines():
            if line.strip():
                try: obj = json.loads(line)
                except json.JSONDecodeError: continue
                if isinstance(obj, dict): yield obj
        return
    try: obj = json.loads(raw)
    except json.JSONDecodeError: return
    if isinstance(obj, dict): yield obj
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict): yield item

def main():
    counts = {s: 0 for s in STATES}
    explicit_independent_verified = 0
    matched_files = 0
    total_records = 0
    samples = []
    for path in iter_json_files():
        file_matched = False
        for record in records_from(path):
            state = record.get("verification_state")
            if state in counts:
                counts[state] += 1
                total_records += 1
                file_matched = True
                if state == "VERIFIED" and record.get("independent_verification") is True:
                    explicit_independent_verified += 1
                if len(samples) < 20 and state == "VERIFIED":
                    samples.append(str(path.relative_to(ROOT)))
        if file_matched: matched_files += 1
    remaining = max(TARGET - explicit_independent_verified, 0)
    report = {
        "event_id": "independent-verification-audit-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repository": "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
        "audit_scope": list(SCAN_DIRS),
        "target_independent_verified_records": TARGET,
        "counts_by_verification_state": counts,
        "explicit_independent_verified_records": explicit_independent_verified,
        "remaining_to_target": remaining,
        "target_progress_percent": round((explicit_independent_verified / TARGET) * 100, 6),
        "matched_files": matched_files,
        "records_with_verification_state": total_records,
        "verified_sample_files": samples,
        "integrity_rule": "Explicit states only; no promotion and no workflow-success-as-verification.",
        "status": "MEASURED",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
