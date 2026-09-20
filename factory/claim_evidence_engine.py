#!/usr/bin/env python3
"""Deterministic claim/evidence normalization aligned to claim-record.schema.json.

The engine never upgrades evidence or verification. Missing information remains
explicitly unverified.
"""
import json
from pathlib import Path

CLAIM_TYPES={"FACT","INTERPRETATION","HYPOTHESIS","PHILOSOPHICAL_PROPOSITION",
             "MATHEMATICAL","COMPUTATIONAL","HISTORICAL","SCIENTIFIC","COMPARATIVE"}
STATUSES={"DRAFT","SUPPORTED","PARTIALLY_SUPPORTED","NOT_VERIFIED","REFUTED","DEFERRED"}
VERIFY={"UNVERIFIED","INDEPENDENTLY_CHECKED","AUTOMATED_CHECK","CONFLICTING","NOT_APPLICABLE"}

def normalize_claim(raw):
    r=dict(raw)
    r.setdefault("id","")
    r.setdefault("claim","")
    r.setdefault("claim_type","HYPOTHESIS")
    r.setdefault("status","NOT_VERIFIED")
    r.setdefault("definitions",[])
    r.setdefault("evidence",[])
    r.setdefault("formulation",[])
    r.setdefault("countercases",[])
    r.setdefault("verification",{"status":"UNVERIFIED","method":"NOT_RUN"})
    r.setdefault("provenance",{"recorded_at":None})

    if r["claim_type"] not in CLAIM_TYPES: r["claim_type"]="HYPOTHESIS"
    if r["status"] not in STATUSES: r["status"]="NOT_VERIFIED"
    v=r["verification"]
    if v.get("status") not in VERIFY: v["status"]="UNVERIFIED"
    # A PASS-like claim status is never inferred from missing/unclear verification.
    if r["status"]=="SUPPORTED" and v["status"] not in {"INDEPENDENTLY_CHECKED","AUTOMATED_CHECK"}:
        r["status"]="NOT_VERIFIED"
    for ev in r["evidence"]:
        if not isinstance(ev,dict):
            continue
        ev.setdefault("description","")
        ev.setdefault("source","")
    return r

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
    p.add_argument("input"); p.add_argument("output")
    a=p.parse_args()
    print("NORMALIZED_CLAIMS:",process_jsonl(a.input,a.output))
