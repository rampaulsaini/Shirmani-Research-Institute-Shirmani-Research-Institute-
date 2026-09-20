#!/usr/bin/env python3
"""Deterministic claim/evidence normalization.

No web/API calls are made here. Input records are normalized, missing evidence
stays missing, and no verification status is upgraded automatically.
"""
import json
from pathlib import Path

ALLOWED_EVIDENCE={"SUPPORTED","PARTIAL","UNAVAILABLE","CONTRADICTED","NOT_VERIFIED"}
ALLOWED_VERIFY={"PASS","CHECK","FAIL","NOT_VERIFIED"}

def normalize_claim(raw):
    claim=dict(raw)
    claim.setdefault("definitions",[])
    claim.setdefault("source",[])
    claim.setdefault("evidence",[])
    claim.setdefault("formulation",{"method":"NOT_PROVIDED","result_status":"NOT_VERIFIED"})
    claim.setdefault("countercases",[])
    claim.setdefault("verification",{"status":"NOT_VERIFIED","method":"NOT_RUN","independent":False})
    claim.setdefault("conclusion","NOT_VERIFIED")
    claim.setdefault("provenance",{"created_at":None,"generator":"claim_evidence_engine"})
    claim.setdefault("status","DRAFT")

    for ev in claim["evidence"]:
        if ev.get("status") not in ALLOWED_EVIDENCE:
            ev["status"]="NOT_VERIFIED"
    if claim["verification"].get("status") not in ALLOWED_VERIFY:
        claim["verification"]["status"]="NOT_VERIFIED"
    if claim["verification"].get("status")=="PASS" and not claim["verification"].get("independent",False):
        claim["verification"]["status"]="CHECK"
    return claim

def process_jsonl(input_path, output_path):
    src=Path(input_path); dst=Path(output_path)
    rows=[]
    if src.exists():
        for line in src.read_text(encoding="utf-8").splitlines():
            if line.strip(): rows.append(normalize_claim(json.loads(line)))
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text("".join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding="utf-8")
    return len(rows)

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    a=p.parse_args()
    print("NORMALIZED_CLAIMS:",process_jsonl(a.input,a.output))
