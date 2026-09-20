#!/usr/bin/env python3
"""Fail-closed promotion gate for independently verified claims.

VERIFIED is allowed only when all reviewer, evidence, countercase, test and
audit requirements are explicitly present. Missing work yields CHECK, never PASS.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"

def main():
    p=OUT/"independent-verification-registry.jsonl"
    if not p.exists(): raise SystemExit("independent-verification-registry.jsonl is missing")
    errors=[]; eligible=0; promoted=0; count=0
    for n,line in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        count+=1
        try: r=json.loads(line)
        except Exception as e:
            errors.append({"line":n,"error":"invalid_json:"+str(e)}); continue
        if r.get("verification_status")=="VERIFIED":
            eligible += 1
            required = [
                r.get("independent") is True,
                bool(r.get("reviewer")),
                bool(r.get("reviewed_at")),
                isinstance(r.get("evidence_references"),list) and bool(r["evidence_references"]),
                (r.get("countercase_review") or {}).get("status")=="REVIEWED",
                isinstance((r.get("countercase_review") or {}).get("references"),list) and bool((r.get("countercase_review") or {}).get("references")),
                (r.get("reproduction_or_test") or {}).get("status") in {"PASSED","NOT_APPLICABLE_WITH_REASON"},
                bool((r.get("reproduction_or_test") or {}).get("references")),
                bool((r.get("audit") or {}).get("recorded_at")),
                bool((r.get("audit") or {}).get("record_hash"))
            ]
            if all(required):
                promoted += 1
            else:
                errors.append({"line":n,"error":"verified_record_missing_promotion_requirements"})
    gate = "PASS" if count == 0 else ("PASS" if promoted == count else "CHECK")
    report={"version":1,"records":count,"verified_records":eligible,
            "promotion_ready":promoted,"error_count":len(errors),
            "promotion_gate":gate,"errors":errors,
            "policy":"The factory never changes NOT_VERIFIED records to VERIFIED."}
    (OUT/"VERIFICATION-PROMOTION-QC.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if errors: raise SystemExit(1)

if __name__=="__main__": main()
