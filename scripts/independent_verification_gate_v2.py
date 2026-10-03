#!/usr/bin/env python3
"""Fail-closed gate for the repository's nested independent-verification registry."""
import argparse,json,hashlib
from pathlib import Path

def fail(msg): raise SystemExit("VERIFICATION_GATE_FAIL: "+msg)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--registry",required=True); a=ap.parse_args()
    p=Path(a.registry); d=json.loads(p.read_text(encoding="utf-8")); rs=d["records"]; s=d["verification_summary"]
    if s["queue_records"]!=len(rs): fail("queue_records mismatch")
    ids=[r.get("id") for r in rs]
    if len(ids)!=len(set(ids)): fail("duplicate record id")
    verified=[r for r in rs if r.get("status")=="VERIFIED"]
    evidence=[r for r in rs if r.get("status")=="EVIDENCE-SUPPORTED"]
    if s["independently_verified_records"]!=len(verified): fail("verified count mismatch")
    expected=round(len(verified)/len(rs)*100,6) if rs else 0
    if s["independent_verified_percent"]!=expected: fail("verified percent mismatch")
    if s["evidence_supported_records"]!=len(evidence): fail("evidence count mismatch")
    for r in rs:
        d=r.get("reviewer_decision",{}); decision=d.get("decision")
        if decision not in {"PENDING","VERIFIED","NOT_VERIFIED","CONTRADICTED","INCONCLUSIVE"}: fail(f'{r.get("id")}: invalid decision')
        if r.get("status")!="VERIFIED": continue
        if decision!="VERIFIED": fail(f'{r["id"]}: status/decision mismatch')
        e,t,p,c,a=r["evidence"],r["independent_test"],r["reproducibility"],r["counter_evidence"],r["audit"]
        if not e.get("sources") or len(str(e.get("evidence_hash","")))!=64: fail(f'{r["id"]}: evidence incomplete')
        if not t.get("protocol") or not t.get("result") or len(str(t.get("test_hash","")))!=64: fail(f'{r["id"]}: test incomplete')
        if not p.get("environment") or not p.get("reproduction_steps") or p.get("result_match") is not True: fail(f'{r["id"]}: reproducibility incomplete')
        if c.get("reviewed") is not True: fail(f'{r["id"]}: counter-evidence incomplete')
        if a.get("passed") is not True or not a.get("audit_id") or not a.get("timestamp"): fail(f'{r["id"]}: audit incomplete')
        if not d.get("reviewer_identity") or not d.get("reviewer_role") or not d.get("timestamp"): fail(f'{r["id"]}: reviewer provenance incomplete')
    print("Independent verification gate v2: PASS")
    print(f"queue={len(rs)} evidence_supported={len(evidence)} verified={len(verified)}")
    print("No workflow success is treated as independent verification.")
    print("registry_sha256="+hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=="__main__": main()
