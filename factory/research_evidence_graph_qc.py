#!/usr/bin/env python3
"""Deterministic QC for the research/evidence traceability graph."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "generated"
NODE_TYPES = {"SOURCE","ARTIFACT","CLAIM","EVIDENCE","FORMULATION","VERIFICATION_TASK","REVIEW_RECORD"}
RELATIONS = {"TRACEABLE_TO","DERIVED_FROM","SUPPORTED_BY","REFERENCES_SOURCE","TESTS","REVIEWS","FULFILLS"}

def main():
    path = OUT / "research-evidence-graph.json"
    if not path.exists():
        raise SystemExit("research-evidence-graph.json is missing")
    graph = json.loads(path.read_text(encoding="utf-8"))
    errors, ids = [], [n.get("id") for n in graph.get("nodes", [])]
    if len(ids) != len(set(ids)): errors.append("duplicate_node_id")
    node_ids = set(ids)
    for n in graph.get("nodes", []):
        if n.get("type") not in NODE_TYPES: errors.append("invalid_node_type:" + str(n.get("id")))
    seen = set()
    for e in graph.get("edges", []):
        key = (e.get("from"), e.get("to"), e.get("relation"))
        if key in seen: errors.append("duplicate_edge")
        seen.add(key)
        if e.get("from") not in node_ids or e.get("to") not in node_ids: errors.append("dangling_edge")
        if e.get("relation") not in RELATIONS: errors.append("invalid_relation")
    claims = {n["id"] for n in graph.get("nodes", []) if n.get("type") == "CLAIM"}
    evidence_by_claim = set()
    for e in graph.get("edges", []):
        if e.get("relation") == "SUPPORTED_BY" and e.get("from") in claims:
            evidence_by_claim.add(e["from"])
    missing_evidence = sorted(claims - evidence_by_claim)
    if missing_evidence:
        errors.append({"missing_evidence_for_claim_count": len(missing_evidence), "sample": missing_evidence[:10]})
    summary = {
        "version": 2, "nodes": len(graph.get("nodes", [])), "edges": len(graph.get("edges", [])),
        "claim_nodes": len(claims), "claims_with_explicit_evidence_nodes": len(evidence_by_claim),
        "error_count": len(errors), "publication_gate": "BLOCK" if errors or not graph.get("nodes") else "PASS",
        "policy": "Graph integrity is deterministic traceability QC; evidence nodes do not establish truth or independent verification.",
        "errors": errors
    }
    (OUT / "RESEARCH-EVIDENCE-GRAPH-QC.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("nodes","edges","claim_nodes","claims_with_explicit_evidence_nodes","error_count","publication_gate")}, ensure_ascii=False))
    if errors or not graph.get("nodes"): raise SystemExit(1)

if __name__ == "__main__":
    main()
