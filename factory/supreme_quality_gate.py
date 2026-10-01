#!/usr/bin/env python3
"""Deterministic Supreme AI/ML/NLP/Automission quality gate.

This gate measures repository wiring and evidence discipline. It does not claim
scientific truth, consciousness detection, or 100% model accuracy.
"""
from __future__ import annotations
import hashlib, json, pathlib, time

ROOT = pathlib.Path(".")
REQUIRED = [
    "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
    "PROJECT-CONTINUITY.md",
    "factory",
    "agents",
    "schemas",
    ".github/workflows",
]
SIGNALS = ["provenance","uncertainty","verification","fail-closed","independent","confidence","evidence"]

def sha256(path):
    h=hashlib.sha256()
    if path.is_file(): h.update(path.read_bytes())
    return h.hexdigest()

def main():
    checks=[{"item":x,"present":(ROOT/x).exists()} for x in REQUIRED]
    docs=(ROOT/"docs").rglob("*.md") if (ROOT/"docs").exists() else []
    corpus="\n".join(p.read_text(encoding="utf-8",errors="ignore") for p in docs)
    integrity={s:s.lower() in corpus.lower() for s in SIGNALS}
    workflows=list((ROOT/".github/workflows").glob("*.yml"))+list((ROOT/".github/workflows").glob("*.yaml"))
    scheduled=sum("schedule:" in p.read_text(encoding="utf-8",errors="ignore") for p in workflows)
    result={
      "schema_version":"1.0",
      "generated_at_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
      "status":"PASS" if all(x["present"] for x in checks) and all(integrity.values()) else "CHECK",
      "repository_wiring":{"required_paths":checks,"workflow_count":len(workflows),"scheduled_workflow_count":scheduled},
      "integrity_signals":integrity,
      "accuracy_contract":"measured_not_declared",
      "biological_signal_contract":"signal_to_inference_to_plain_language_with_uncertainty",
      "scientific_claim_boundary":"model output is not automatically proof of subjective feeling or consciousness",
      "artifact_hash":sha256(ROOT/"docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md")
    }
    out=ROOT/"generated/supreme-quality-gate.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__": raise SystemExit(main())
