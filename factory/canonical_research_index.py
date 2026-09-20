#!/usr/bin/env python3
"""Publish canonical research/claim indexes from one verified traceable batch.

The index is a traceability view. Draft and UNVERIFIED claims remain unverified.
"""
import json
from pathlib import Path
from datetime import datetime, timezone

def _jsonl(path):
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def build(out_dir):
    out=Path(out_dir)
    contracts=out/"contracts"
    sources=_jsonl(contracts/"source-records.jsonl")
    claims=_jsonl(contracts/"claim-records.jsonl")
    concepts=_jsonl(contracts/"concept-records.jsonl")
    stamp=datetime.now(timezone.utc).isoformat()

    verified=sum(1 for c in claims if c.get("status")=="SUPPORTED" and c.get("verification",{}).get("status") in {"INDEPENDENTLY_CHECKED","AUTOMATED_CHECK"})
    research_index={
        "schema_version":"1.1.0",
        "generated_at":stamp,
        "status":"READY_WITH_UNVERIFIED_RECORDS" if claims else "READY_FOR_INGESTION",
        "source_registry":"generated/source-registry.json",
        "claim_records":claims,
        "artifact_records":[],
        "coverage":{
            "source_records_indexed":len(sources),
            "concept_records_indexed":len(concepts),
            "claim_records_total":len(claims),
            "claim_records_verified":verified,
            "artifact_records_verified":0
        },
        "integrity":{
            "fabricated_records":False,
            "missing_data_preserved":True,
            "verification_required":True
        }
    }
    nodes=[]; edges=[]
    for s in sources:
        nodes.append({"id":str(s.get("id")),"type":"SOURCE","status":s.get("availability","UNKNOWN")})
    for c in concepts:
        nodes.append({"id":str(c.get("id")),"type":"CONCEPT","status":c.get("status","DRAFT")})
    for c in claims:
        cid=str(c.get("id"))
        nodes.append({"id":cid,"type":"CLAIM","status":c.get("status","DRAFT"),
                      "claim_type":c.get("claim_type","")})
        for ev in c.get("evidence",[]):
            ref=ev.get("source")
            if ref:
                edges.append({"from":str(ref),"to":cid,"type":"TRACE"})
    graph={
        "schema_version":"1.1.0","generated_at":stamp,
        "status":"TRACE_GRAPH_ONLY_UNTIL_VERIFICATION" if claims else "READY_FOR_INGESTION",
        "nodes":nodes,"edges":edges,
        "integrity":{
            "fabricated_nodes":False,"fabricated_edges":False,
            "missing_data_preserved":True,"verified_claims_only":False
        }
    }
    root=out.parent.parent if out.name=="agent-run" else out
    (root/"research-index.json").write_text(json.dumps(research_index,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (root/"claim-graph.json").write_text(json.dumps(graph,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return {"source_records":len(sources),"concept_records":len(concepts),
            "claim_records":len(claims),"verified_claims":verified}
