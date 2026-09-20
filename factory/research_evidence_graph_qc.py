#!/usr/bin/env python3
"""Deterministic QC for the research/evidence traceability graph."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "generated"
NODE_TYPES = {"SOURCE", "ARTIFACT", "CLAIM", "FORMULATION", "VERIFICATION_TASK", "REVIEW_RECORD"}
RELATIONS = {"TRACEABLE_TO", "DERIVED_FROM", "TESTS", "REVIEWS", "FULFILLS"}

def main():
    path = OUT / "research-evidence-graph.json"
    if not path.exists():
        raise SystemExit("research-evidence-graph.json is missing")
    graph = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    ids = [n.get("id") for n in nodes]
    if len(ids) != len(set(ids)):
        errors.append("duplicate_node_id")
    node_ids = set(ids)
    for n in nodes:
        if n.get("type") not in NODE_TYPES:
            errors.append("invalid_node_type:" + str(n.get("id")))
    seen = set()
    for e in edges:
        key = (e.get("from"), e.get("to"), e.get("relation"))
        if key in seen:
            errors.append("duplicate_edge")
        seen.add(key)
        if e.get("from") not in node_ids or e.get("to") not in node_ids:
            errors.append("dangling_edge")
        if e.get("relation") not in RELATIONS:
            errors.append("invalid_relation")
    summary = {
        "version": 1,
        "nodes": len(nodes),
        "edges": len(edges),
        "error_count": len(errors),
        "publication_gate": "BLOCK" if errors or not nodes else "PASS",
        "policy": "Graph integrity is deterministic traceability QC; it does not establish truth or independent verification.",
        "errors": errors,
    }
    (OUT / "RESEARCH-EVIDENCE-GRAPH-QC.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: summary[k] for k in ("nodes","edges","error_count","publication_gate")}, ensure_ascii=False))
    if errors or not nodes:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
