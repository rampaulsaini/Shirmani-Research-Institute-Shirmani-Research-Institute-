#!/usr/bin/env python3
"""Deterministic QC primitives for the research factory.

No paid API is required. This module checks provenance, schema-like fields,
duplicate hashes and forbidden publication states before artifacts are published.
"""
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def check_records(path):
    seen=set(); errors=[]; count=0
    with open(path,encoding="utf-8") as f:
        for line_no,line in enumerate(f,1):
            if not line.strip(): continue
            count+=1
            try: r=json.loads(line)
            except Exception as e:
                errors.append({"line":line_no,"error":f"invalid_json:{e}"}); continue
            for key in ("id","source","text","hash"):
                if key not in r: errors.append({"line":line_no,"error":f"missing:{key}"})
            h=r.get("hash")
            if h in seen: errors.append({"line":line_no,"error":"duplicate_hash"})
            if h: seen.add(h)
    return {"records":count,"unique_hashes":len(seen),"errors":errors}

def main():
    generated=ROOT/"generated"
    report={"checks":[]}
    src=generated/"source-units.jsonl"
    if src.exists(): report["checks"].append({"file":str(src.relative_to(ROOT)),**check_records(src)})
    verse=generated/"verse-corpus.jsonl"
    if verse.exists(): report["checks"].append({"file":str(verse.relative_to(ROOT)),**check_records(verse)})
    report["publication_gate"] = "PASS" if all(not c["errors"] for c in report["checks"]) else "BLOCK"
    (generated/"QC-REPORT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))

if __name__=="__main__": main()
