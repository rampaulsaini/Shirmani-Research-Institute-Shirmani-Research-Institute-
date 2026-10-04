#!/usr/bin/env python3
"""Deterministic Research Paper claim intake; preserves UNVERIFIED status."""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
PREFIX="claim:research-paper-claim:"

def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main():
    reg=json.loads((OUT/"research-paper-claims.json").read_text(encoding="utf-8"))
    now=datetime.now(timezone.utc).isoformat()
    claims=[json.loads(x) for x in (OUT/"claim-evidence.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    claims=[x for x in claims if not str(x.get("id","")).startswith(PREFIX)]
    for c in reg["claims"]:
        cid=str(c["id"]); text=str(c["claim"])
        claims.append({
            "id":PREFIX+cid,
            "claim":text,
            "definitions":["Author proposition; requires human review."],
            "source":[{"type":"RESEARCH_PAPER","locator":"rampaulsaini/Shirmani-Research-Paper:index.html","source_id":"srp:"+cid}],
            "evidence":[{"kind":"AUTHOR_DECLARATION","status":"NOT_VERIFIED","detail":"Provenance is not independent proof."}],
            "formulation":{"method":"Research Paper intake","result_status":"NOT_VERIFIED"},
            "source_traceability":{"status":"DECLARED","source_ids":["srp:"+cid],"resolved":False},
            "verification":{"status":"NOT_VERIFIED","method":"Independent verification required.","independent":False},
            "verification_questions":c.get("evidence_required",[]),
            "conclusion":"No independently verified conclusion is asserted.",
            "provenance":{"created_at":now,"generator":"factory/research_paper_claim_intake.py","content_hash":sha(text)}
        })
    (OUT/"claim-evidence.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in claims)+"\n",encoding="utf-8")
    print(json.dumps({"intaken":len(reg["claims"]),"status":"UNVERIFIED"}))

if __name__=="__main__": main()
