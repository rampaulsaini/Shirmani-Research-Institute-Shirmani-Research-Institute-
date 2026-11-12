#!/usr/bin/env python3
"""Product-first multi-layer Automission coordinator."""
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"
CFG=json.loads((ROOT/"factory/agent_config.json").read_text(encoding="utf-8")); TARGETS=CFG.get("products",{})
TYPES=[("digital_books","Digital Mahagranth","generated/book-*.md"),("verses","Traceable Sutra/Verse Records","generated/verse-corpus.jsonl"),("research_papers","Research Paper Drafts","generated/research-paper-draft-*.md"),("certificates","Archival Certificates","generated/certificates/certificate-*.md"),("audio_prompts","Audio / Music AI Prompts","generated/audio-prompts.jsonl")]
def n(key,pat):
 p=ROOT/(pat if key not in {"verses","audio_prompts"} else ("generated/verse-corpus.jsonl" if key=="verses" else "generated/audio-prompts.jsonl"))
 if key in {"verses","audio_prompts"}: return sum(1 for x in p.open(encoding="utf-8",errors="ignore") if x.strip()) if p.exists() else 0
 return len(list(ROOT.glob(pat)))
def main():
 out=[]; tt=tc=0
 for k,label,pat in TYPES:
  target=int(TARGETS.get(k,0)); cur=n(k,pat); tt+=target; tc+=min(cur,target)
  out.append({"id":k,"label":label,"target":target,"current":cur,"completion_pct":round(min(100,cur/target*100) if target else 0,2),"state":"ready_for_catalog" if cur else "empty","verification":"downstream_quality_gate"})
 payload={"schema_version":"1.0","generated_at":datetime.now(timezone.utc).isoformat(),"mode":"product-first","principle":"product/output first; verification promotes quality and trust","execution_layers":["intake_source","reasoning","AI_ML","NLP","practitioner","deep_learning","product","marketing","economic_transaction","security_audit","publishing","continuity","verification"],"quantum_mode":{"state":"quantum-ready-adapter","actual_quantum_backend_used":False,"reason":"No quantum provider is assumed; deterministic execution remains the safe baseline."},"products":out,"aggregate_product_completion_pct":round(min(100,tc/tt*100) if tt else 0,2),"next_priority":["activate product surfaces","connect product metadata to catalog/store links","run NLP/ML practitioner enrichment where configured","route completed outputs to evidence/QC","use independent verification for promotion, not as a substitute for product generation"]}
 OUT.mkdir(exist_ok=True); (OUT/"PRODUCT-FIRST-AUTOMISSION.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(payload,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
