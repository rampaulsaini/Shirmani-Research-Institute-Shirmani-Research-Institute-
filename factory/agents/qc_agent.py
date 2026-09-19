import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
out=ROOT/"generated"/"qc-report.json"
checks={
"canonical_corpus_exists":(ROOT/"generated"/"canonical-corpus.jsonl").exists(),
"evidence_index_exists":(ROOT/"generated"/"evidence-index.jsonl").exists(),
"verification_report_exists":(ROOT/"generated"/"verification-report.json").exists(),
"research_queue_exists":(ROOT/"generated"/"research-queue.jsonl").exists(),
"product_queue_exists":(ROOT/"generated"/"product-queue.jsonl").exists()
}
out.write_text(json.dumps({"status":"PASS" if all(checks.values()) else "BLOCKED","checks":checks},ensure_ascii=False,indent=2),encoding="utf-8")
print("qc-agent:",out.read_text())
