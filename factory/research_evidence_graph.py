#!/usr/bin/env python3
"""Build a deterministic research/evidence graph from durable factory artifacts.

The graph is a traceability index, not a truth engine. Edges record provenance,
formulation, review and verification relationships; they never imply that a
claim is scientifically or factually proven.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def read_jsonl(path):
    if not path.exists():
        raise SystemExit(f"{path.name} is missing")
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows

def add_node(nodes, node_id, node_type, **attrs):
    nodes[node_id] = {"id": node_id, "type": node_type, **attrs}

def main():
    sources = read_jsonl(OUT / "source-units.jsonl")
    reasoning = read_jsonl(OUT / "reasoning-manifest.jsonl")
    claims = read_jsonl(OUT / "claim-evidence.jsonl")
    formulations = read_jsonl(OUT / "formulation-records.jsonl")
    tasks = read_jsonl(OUT / "independent-verification-queue.jsonl")
    reviews = read_jsonl(OUT / "independent-verification-registry.jsonl")

    nodes = {}
    edges = []

    for s in sources:
        sid = "source:" + str(s["id"])
        add_node(nodes, sid, "SOURCE", repository=s.get("repository"), path=s.get("path"))

    for r in reasoning:
        aid = "artifact:" + str(r["kind"]) + ":" + str(r["artifact_id"])
        add_node(nodes, aid, "ARTIFACT", kind=r["kind"], artifact_id=str(r["artifact_id"]),
                 content_sha256=r.get("content_sha256"))
        for sid in r.get("source_ids", []):
            source_node = "source:" + str(sid)
            if source_node in nodes:
                edges.append({"from": aid, "to": source_node, "relation": "TRACEABLE_TO"})

    for c in claims:
        cid = str(c["id"])
        add_node(nodes, cid, "CLAIM", verification_status=(c.get("verification") or {}).get("status"))
        kind, artifact_id = cid.split(":", 2)[1:]
        aid = "artifact:" + kind + ":" + artifact_id
        if aid in nodes:
            edges.append({"from": cid, "to": aid, "relation": "DERIVED_FROM"})

    for f in formulations:
        fid = str(f["id"])
        add_node(nodes, fid, "FORMULATION", status=(f.get("result") or {}).get("status"))
        aid = "artifact:" + str(f["kind"]) + ":" + str(f["artifact_id"])
        if aid in nodes:
            edges.append({"from": fid, "to": aid, "relation": "TESTS"})

    for t in tasks:
        tid = str(t["task_id"])
        add_node(nodes, tid, "VERIFICATION_TASK", status=t.get("status"),
                 verification_status=t.get("verification_status"))
        cid = str(t["claim_id"])
        if cid in nodes:
            edges.append({"from": tid, "to": cid, "relation": "REVIEWS"})

    for r in reviews:
        rid = str(r["review_id"])
        add_node(nodes, rid, "REVIEW_RECORD", status=r.get("status"),
                 verification_status=r.get("verification_status"), independent=r.get("independent"))
        tid = str(r["task_id"])
        if tid in nodes:
            edges.append({"from": rid, "to": tid, "relation": "FULFILLS"})

    # Deterministic de-duplication and stable ordering.
    unique = {(e["from"], e["to"], e["relation"]): e for e in edges}
    edges = [unique[k] for k in sorted(unique)]

    payload = {
        "schema_version": 1,
        "graph_type": "research_evidence_traceability_graph",
        "nodes": sorted(nodes.values(), key=lambda x: x["id"]),
        "edges": edges,
        "policy": (
            "Traceability graph only. Provenance, generated reasoning, formulation, "
            "queues and review slots are not independent proof."
        ),
    }
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    payload["graph_sha256"] = digest(canonical)

    (OUT / "research-evidence-graph.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    summary = {
        "version": 1,
        "nodes": len(payload["nodes"]),
        "edges": len(payload["edges"]),
        "graph_sha256": payload["graph_sha256"],
        "publication_gate": "CHECK" if payload["nodes"] else "BLOCK",
        "independent_verification_claimed": False,
    }
    (OUT / "RESEARCH-EVIDENCE-GRAPH.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    main()
