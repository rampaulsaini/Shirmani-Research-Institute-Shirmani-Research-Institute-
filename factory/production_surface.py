#!/usr/bin/env python3
"""Build a truthful production-first platform status surface.

This is telemetry, not a verification gate. It counts production capability and
visible outputs while keeping independent verification as a downstream status.
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
REG = ROOT / "docs/yatharth-system/public-module-registry.json"

def count_lines(p):
    if not p.exists(): return 0
    with p.open(encoding="utf-8", errors="replace") as f:
        return sum(1 for x in f if x.strip())

def count_glob(pattern):
    return len(list(OUT.glob(pattern)))

def main():
    reg = json.loads(REG.read_text(encoding="utf-8"))
    nav = reg.get("navigation", [])
    statuses = {}
    for m in nav:
        statuses[m["status"]] = statuses.get(m["status"], 0) + 1

    metrics = {
        "source_units": count_lines(OUT/"source-units.jsonl"),
        "research_queue": count_lines(OUT/"research-queue.jsonl"),
        "verse_records": count_lines(OUT/"verse-corpus.jsonl"),
        "reasoning_records": count_lines(OUT/"reasoning-manifest.jsonl"),
        "claim_evidence_records": count_lines(OUT/"claim-evidence.jsonl"),
        "provenance_records": count_lines(OUT/"provenance-ledger.jsonl"),
        "audio_prompts": count_lines(OUT/"audio-prompts.jsonl"),
        "research_paper_drafts": count_glob("research-paper-draft-*.md"),
        "digital_books": count_glob("book-*.md"),
        "certificates": count_glob("certificates/certificate-*.md"),
        "product_records": count_lines(OUT/"product-queue.jsonl"),
        "evidence_graph_nodes": None,
        "evidence_graph_edges": None,
    }
    graph = OUT/"RESEARCH-EVIDENCE-GRAPH-QC.json"
    if graph.exists():
        g=json.loads(graph.read_text(encoding="utf-8"))
        metrics["evidence_graph_nodes"]=g.get("nodes")
        metrics["evidence_graph_edges"]=g.get("edges")

    workflows = len(list((ROOT/".github/workflows").glob("*.y*ml")))
    agents = len(json.loads((OUT/"agent-status.json").read_text(encoding="utf-8")).get("agents", [])) if (OUT/"agent-status.json").exists() else 0

    payload = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "purpose": "production-first automission telemetry",
        "principle": "Produce broadly first; quality/QC gates protect outputs; independent verification is downstream and never replaced by automation.",
        "public_modules": {"total": len(nav), "status_counts": statuses},
        "automation": {"workflow_files": workflows, "registered_agent_layers": agents},
        "production_metrics": metrics,
        "independent_verification": reg.get("verification", {}),
        "truth_boundary": "Counts prove generated/implemented artifacts exist; they do not prove scientific, historical, philosophical or metaphysical truth.",
        "next_work": [
            "continue multi-lane production",
            "expand architecture-only public modules into executable bounded modules",
            "publish machine-readable production telemetry",
            "keep verification as downstream quality/promotion, not the production bottleneck"
        ]
    }
    OUT.mkdir(exist_ok=True)
    (OUT/"PRODUCTION-SURFACE.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=["# SHIRMANI Production Surface","",f"Updated: {payload['generated_at']}","",
           "Production-first telemetry. Verification is downstream and does not block generation.",
           "", "## Public modules"]
    for k,v in statuses.items(): lines.append(f"- {k}: {v}")
    lines += ["","## Production outputs"]
    for k,v in metrics.items(): lines.append(f"- {k}: {v}")
    lines += ["","## Automation",f"- workflow files: {workflows}",f"- registered agent layers: {agents}",
              "","## Boundary","Generated output and workflow success are not independent proof."]
    (OUT/"PRODUCTION-SURFACE.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps(payload,ensure_ascii=False))

if __name__ == "__main__":
    main()
