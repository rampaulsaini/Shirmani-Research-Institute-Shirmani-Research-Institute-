#!/usr/bin/env python3
"""Fail-closed verification readiness audit.

This tool NEVER promotes a record to independently verified by itself.
It audits claim-evidence records and only counts VERIFIED when an explicit
independent verification record satisfies the required fields.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
INPUT = GENERATED / "claim-evidence.jsonl"
OUT = GENERATED / "automission" / "verification-readiness.json"

REQUIRED = ("id", "claim", "source", "evidence", "verification", "provenance")

def sha(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode()).hexdigest()

def independently_verified(r):
    v = r.get("verification") or {}
    return (
        v.get("status") == "VERIFIED"
        and v.get("independent") is True
        and isinstance(v.get("method"), str) and bool(v["method"].strip())
        and isinstance(v.get("verifier"), str) and bool(v["verifier"].strip())
        and isinstance(v.get("verification_ref"), str) and bool(v["verification_ref"].strip())
        and isinstance(v.get("verified_at"), str) and bool(v["verified_at"].strip())
    )

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    records, errors = [], []
    if INPUT.exists():
        for line_no, line in enumerate(INPUT.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except Exception as exc:
                errors.append({"line": line_no, "error": "invalid_json", "detail": str(exc)})
                continue
            missing = [k for k in REQUIRED if k not in r]
            if missing:
                errors.append({"line": line_no, "error": "missing_fields", "fields": missing})
                continue
            records.append(r)

    verified = [r for r in records if independently_verified(r)]
    report = {
        "schema_version": "verification-readiness-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input": str(INPUT.relative_to(ROOT)),
        "records_scanned": len(records),
        "independently_verified_records": len(verified),
        "not_independently_verified_records": len(records) - len(verified),
        "malformed_records": len(errors),
        "verification_status": "VERIFIED_RECORDS_PRESENT" if verified else "NO_INDEPENDENTLY_VERIFIED_RECORDS",
        "publication_gate": "PASS" if not errors else "BLOCK",
        "promotion_rule": "Workflow run, QC PASS, source trace, or model output alone can never promote a record to VERIFIED.",
        "integrity": "fail-closed",
        "report_hash": sha({"records": len(records), "verified": len(verified), "errors": errors}),
        "errors": errors[:100],
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
