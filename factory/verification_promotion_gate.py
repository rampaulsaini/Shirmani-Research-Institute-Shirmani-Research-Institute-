#!/usr/bin/env python3
"""Fail-closed gate for promotion from review record to VERIFIED.

The factory may create review slots, but only a complete human/audit record
can promote a claim. Missing or fabricated reviewer/evidence data is blocked.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

REQUIRED = (
    "review_id", "task_id", "claim_id", "status", "verification_status",
    "independent", "reviewer", "reviewed_at", "evidence_references",
    "countercase_review", "reproduction_or_test", "audit", "created_at", "generator"
)

def promotable(r):
    return (
        r.get("status") == "REVIEWED"
        and r.get("verification_status") == "VERIFIED"
        and r.get("independent") is True
        and isinstance(r.get("reviewer"), str) and bool(r["reviewer"].strip())
        and bool(r.get("reviewed_at"))
        and isinstance(r.get("evidence_references"), list) and bool(r["evidence_references"])
        and (r.get("countercase_review") or {}).get("status") == "REVIEWED"
        and bool((r.get("countercase_review") or {}).get("references"))
        and (r.get("reproduction_or_test") or {}).get("status") in {"PASSED", "SUPPORTED"}
        and bool((r.get("reproduction_or_test") or {}).get("references"))
        and bool((r.get("audit") or {}).get("recorded_at"))
        and bool((r.get("audit") or {}).get("record_hash"))
    )

def main():
    path = OUT / "independent-verification-registry.jsonl"
    if not path.exists():
        raise SystemExit("independent-verification-registry.jsonl is missing")
    errors, seen, records, verified, eligible = [], set(), 0, 0, 0
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        records += 1
        try:
            r = json.loads(line)
        except Exception as exc:
            errors.append({"line": line_no, "error": "invalid_json:" + str(exc)})
            continue
        rid = r.get("review_id")
        if not rid or rid in seen:
            errors.append({"line": line_no, "error": "missing_or_duplicate_review_id"})
        seen.add(rid)
        for key in REQUIRED:
            if key not in r:
                errors.append({"line": line_no, "error": "missing:" + key})
        if r.get("verification_status") == "VERIFIED":
            verified += 1
            if not promotable(r):
                errors.append({"line": line_no, "error": "unearned_verified_status"})
        if promotable(r):
            eligible += 1
    report = {
        "version": 1,
        "records": records,
        "verified_records": verified,
        "promotion_eligible": eligible,
        "error_count": len(errors),
        "publication_gate": "BLOCK" if errors else ("PASS" if records == eligible else "CHECK"),
        "policy": "Only complete independent review, evidence, countercase, reproduction/test and audit records may reach VERIFIED."
    }
    (OUT / "VERIFICATION-PROMOTION-QC.json").write_text(
        json.dumps({**report, "errors": errors}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
