#!/usr/bin/env python3
"""Product-first orchestration layer.

Build useful product records from existing generated assets first. Independent
verification remains a downstream quality outcome, not the product itself.
The quantum profile is quantum-inspired/deterministic unless a real backend is
explicitly configured and exercised.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
CFG=json.loads((ROOT/"factory"/"agent_config.json").read_text(encoding="utf-8"))

def count_jsonl(p): return sum(1 for x in p.open(encoding="utf-8") if x.strip()) if p.exists() else 0
def count_glob(pattern): return len(list(OUT.glob(pattern)))

def product_lines():
    cert=OUT/"certificates"
    return [
      {"id":"digital-mahagranth","name":"Digital Mahagranth","type":"digital-book","artifact":"generated/book-*.md","count":count_glob("book-*.md"),"target":int(CFG["products"]["digital_books"]),"next_action":"package, catalog, preview and publish approved editions"},
      {"id":"research-paper-drafts","name":"Research Paper Draft Series","type":"research-draft","artifact":"generated/research-paper-draft-*.md","count":count_glob("research-paper-draft-*.md"),"target":int(CFG["products"]["research_papers"]),"next_action":"editorial review, evidence review and publication packaging"},
      {"id":"verse-corpus","name":"Heart-View Verse / Sutra Corpus","type":"digital-corpus","artifact":"generated/verse-corpus.jsonl","count":count_jsonl(OUT/"verse-corpus.jsonl"),"target":int(CFG["products"]["verses"]),"next_action":"create themed collections, previews and distribution packages"},
      {"id":"audio-prompt-library","name":"AI Music / Audio Prompt Library","type":"audio-ready-digital-product","artifact":"generated/audio-prompts.jsonl","count":count_jsonl(OUT/"audio-prompts.jsonl"),"target":int(CFG["products"]["audio_prompts"]),"next_action":"render audio variants, attach licensing metadata and catalog"},
      {"id":"digital-certificates","name":"Digital Research Certificates","type":"archival-digital-product","artifact":"generated/certificates/certificate-*.md","count":len(list(cert.glob("certificate-*.md"))) if cert.exists() else 0,"target":int(CFG["products"]["certificates"]),"next_action":"template design, issue metadata and delivery packaging"},
      {"id":"evidence-graph","name":"Research Evidence Graph Export","type":"research-data-product","artifact":"generated/research-evidence-graph.json","count":1 if (OUT/"research-evidence-graph.json").exists() else 0,"target":1,"next_action":"create public explorer/export views"},
      {"id":"research-intelligence-catalog","name":"Research Intelligence Catalog","type":"information-product","artifact":"generated/repository-intelligence.json","count":1 if (OUT/"repository-intelligence.json").exists() else 0,"target":1,"next_action":"publish searchable catalog and capability pages"}
    ]

def main():
    lines=product_lines()
    for p in lines:
        p["completion_pct"]=round(min(100,p["count"]/p["target"]*100),2) if p["target"] else 0
        p["asset_state"]="AVAILABLE" if p["count"] else "MISSING"
        p["product_state"]="READY_FOR_PACKAGING" if p["count"] else "BACKLOG"
        p["verification_state"]="UNVERIFIED"
        p["commercial_state"]="NOT_CONFIGURED"
        p["independent_verification_required"]=True
    total_target=sum(p["target"] for p in lines)
    total_count=sum(min(p["count"],p["target"]) for p in lines)
    c={"version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"strategy":"PRODUCT_FIRST",
       "principle":"Build useful products first; verification is a downstream quality outcome.",
       "quantum_execution":{"mode":"quantum-inspired-deterministic","purpose":"queue prioritization, decomposition and scheduling","real_quantum_backend":False,"future_backend_allowed":True},
       "product_count":len(lines),"target_units":total_target,"available_units":total_count,
       "completion_pct":round(total_count/total_target*100,2) if total_target else 0,"lines":lines,
       "safety":{"generated_output_is_not_automatic_truth":True,"verification_does_not_create_the_product":True,"financial_actions_require_owner_authorization":True}}
    (OUT/"PRODUCT-CATALOG.json").write_text(json.dumps(c,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    md=["# SHIRMANI PRODUCT-FIRST AUTOMISSION","",f"Generated: {c['generated_at']}","",
        "**Rule:** Product creation and packaging proceed independently of verification; verification is a downstream quality outcome.","",
        "| Product | Available | Target | Completion | State |","|---|---:|---:|---:|---|"]
    for p in lines: md.append(f"| {p['name']} | {p['count']} | {p['target']} | {p['completion_pct']}% | {p['product_state']} |")
    md += ["","## Multi-layer execution","Source → Research → Reasoning → Product → Packaging → Marketing Draft → QC → Independent Verification → Publication.",
           "","## Quantum mechanism boundary","The current repository uses a deterministic/quantum-inspired orchestration profile. No real quantum hardware or quantum advantage is claimed until an actual backend is configured and exercised.",
           "","## Commercial boundary","Catalog generation is enabled. Payments, financial transactions and irreversible commercial actions remain disabled until explicitly authorized and integrated."]
    (OUT/"PRODUCT-PIPELINE.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps({"strategy":c["strategy"],"product_lines":len(lines),"available_units":total_count,"target_units":total_target,"completion_pct":c["completion_pct"]},ensure_ascii=False))
if __name__=="__main__": main()
