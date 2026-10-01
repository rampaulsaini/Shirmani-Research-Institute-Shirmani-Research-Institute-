#!/usr/bin/env python3
"""Unified fail-closed control plane for the SHIRMANI AI/ML/NLP Automission stack."""
from __future__ import annotations
import hashlib,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"supreme-orchestrator"; OUT.mkdir(parents=True,exist_ok=True)
GATES=[
("architecture_qc","factory/supreme_architecture_qc.py"),
("nlp_qc","factory/supreme_nlp_qc.py"),
("quality_gate","factory/supreme_quality_gate.py"),
("verification_queue_qc","factory/verification_queue_qc.py"),
("verification_promotion_gate","factory/verification_promotion_gate.py"),
("publication_gate","factory/publication_gate.py"),
("nlp_benchmark","factory/supreme_nlp_benchmark.py"),
]
REQUIRED=[
"agents/automission_supervisor.py",
"agents/supreme_nlp_practitioner.py",
"schemas/supreme-nlp-signal-record.schema.json",
"docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
"factory/supreme_nlp_benchmark.py",
"research/independent-verification-protocol-2026-09-29.md",
]
def run_gate(name:str,rel:str)->dict[str,Any]:
    p=ROOT/rel
    if not p.exists(): return {"name":name,"status":"BLOCK","reason":f"missing:{rel}"}
    try:
        x=subprocess.run(["python",str(p)],cwd=ROOT,text=True,capture_output=True,timeout=180)
        return {"name":name,"status":"PASS" if x.returncode==0 else "BLOCK",
                "returncode":x.returncode,"stdout_tail":x.stdout[-2000:],"stderr_tail":x.stderr[-2000:]}
    except Exception as e: return {"name":name,"status":"BLOCK","reason":str(e)}
def main()->int:
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    gates=[run_gate(n,p) for n,p in GATES]
    ok=not missing and all(g["status"]=="PASS" for g in gates)
    d={"schema_version":"1.0","generated_at":datetime.now(timezone.utc).isoformat(),
       "system":"SHIRMANI_SUPREME_TOTAL_AI_ML_NLP_AUTOMISSION","cycle":"5-minute",
       "pipeline":["Observe","Collect","Normalize","Analyze","Reason","Execute","Test","Verify","Audit","Learn","Improve"],
       "status":"PASS" if ok else "BLOCK","missing_required_files":missing,"gates":gates,
       "governance":{"fail_closed":True,"scheduled_code_mutation_allowed":False,
       "subjective_experience_claim_allowed":False,"independent_verification_required":True,
       "human_review_for_high_impact_actions":True,"accuracy_is_measured_not_declared":True,
       "synthetic_regression_benchmark_required":True}}
    d["fingerprint"]=hashlib.sha256(json.dumps(d,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    (OUT/"status.json").write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(d,ensure_ascii=False,indent=2)); return 0 if ok else 1
if __name__=="__main__": raise SystemExit(main())
