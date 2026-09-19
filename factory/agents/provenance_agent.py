#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; G=ROOT/"generated"; G.mkdir(parents=True,exist_ok=True)
src=G/"canonical-corpus.jsonl"; ev=G/"evidence-index.jsonl"; out=G/"provenance-ledger.jsonl"
evidence={}
if ev.exists():
    for line in ev.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r=json.loads(line); evidence[r["canonical_id"]]=r
rows=[]
if src.exists():
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        r=json.loads(line); cid=r["canonical_id"]; e=evidence.get(cid,{})
        rows.append({
            "provenance_id":"PRV-"+hashlib.sha256((cid+"|"+str(r.get("canonical_hash",""))).encode()).hexdigest()[:16],
            "canonical_id":cid,"source":r.get("source"),"source_hash":r.get("canonical_hash"),
            "evidence_status":e.get("evidence_status","unknown"),
            "verification_required":True,"scientific_validation":False,
            "generated_products_are_noncanonical":True,
            "created_at":datetime.now(timezone.utc).isoformat()
        })
out.write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in rows)+("\n" if rows else ""),encoding="utf-8")
print("provenance-agent:",len(rows))
