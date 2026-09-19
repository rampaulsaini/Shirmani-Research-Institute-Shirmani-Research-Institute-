#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; G=ROOT/"generated"; G.mkdir(parents=True,exist_ok=True)
out=G/"qc-report.json"
checks={
"canonical_corpus_exists":(G/"canonical-corpus.jsonl").exists(),
"evidence_index_exists":(G/"evidence-index.jsonl").exists(),
"verification_report_exists":(G/"verification-report.json").exists(),
"research_queue_exists":(G/"research-queue.jsonl").exists(),
"product_queue_exists":(G/"product-queue.jsonl").exists(),
"provenance_ledger_exists":(G/"provenance-ledger.jsonl").exists(),
"ai_output_exists":(G/"ai-output.jsonl").exists()
}
status="PASS" if all(checks.values()) else "BLOCKED"
out.write_text(json.dumps({"status":status,"checks":checks,"policy":{"draft_only":True,"scientific_validation":False,"generated_is_noncanonical":True}},ensure_ascii=False,indent=2),encoding="utf-8")
print("qc-agent:",status)
