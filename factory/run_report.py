#!/usr/bin/env python3
import json, subprocess
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"
checks=[("source_units","source-units.jsonl"),("canonical_corpus","canonical-corpus.jsonl"),("evidence_index","evidence-index.jsonl"),("verification_report","verification-report.json"),("research_queue","research-queue.jsonl"),("product_queue","product-queue.jsonl"),("qc_report","qc-report.json"),("cloud_manifest","cloud-sync-manifest.json")]
report={"generated_at":datetime.now(timezone.utc).isoformat(),"status":"PASS","checks":[]}
for name,rel in checks:
    p=OUT/rel; ok=p.exists() and p.stat().st_size>0
    report["checks"].append({"name":name,"path":rel,"ok":ok,"bytes":p.stat().st_size if p.exists() else 0})
    if not ok: report["status"]="FAIL"
try: report["commit"]=subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,text=True,capture_output=True,check=False).stdout.strip()
except Exception: report["commit"]=None
(OUT/"run-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print("factory run:",report["status"])
if report["status"]!="PASS": raise SystemExit(1)
