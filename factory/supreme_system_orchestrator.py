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
("neutrality_contract","scripts/validate_neutrality_contract.py"),
("nlp_qc","factory/supreme_nlp_qc.py"),("quality_gate","factory/supreme_quality_gate.py"),
("verification_queue_qc","factory/verification_queue_qc.py"),
("verification_promotion_gate","factory/verification_promotion_gate.py"),
("publication_gate","factory/publication_gate.py"),("nlp_benchmark","factory/supreme_nlp_benchmark.py"),
]
REQUIRED=[
"agents/automission_supervisor.py","agents/supreme_nlp_practitioner.py",
"schemas/supreme-nlp-signal-record.schema.json","schemas/neutrality-evidence-record.schema.json",
"docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
"docs/SHIRMANI-NEUTRALITY-EVIDENCE-CONTRACT.md","factory/supreme_nlp_benchmark.py",
"research/independent-verification-protocol-2026-09-29.md",
]
def seed_nlp_status()->None:
 from agents.supreme_nlp import build_record
 source=ROOT/"generated"/"signal-input.jsonl"
 rows=([json.loads(x) for x in source.read_text(encoding="utf-8").splitlines() if x.strip()] if source.exists() else [])
 if not rows: rows=[{"modality":"synthetic","feature":"baseline_a","value":1.0,"quality":1.0,"source":"supreme-orchestrator-smoke"},{"modality":"synthetic","feature":"baseline_b","value":1.0,"quality":1.0,"source":"supreme-orchestrator-smoke"}]
 target=ROOT/"generated"/"supreme-nlp"/"status.json"; target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(build_record(rows,"supreme-orchestrator-cycle"),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def ensure_empty_verification_ledgers()->None:
 for name in ("claim-evidence.jsonl","independent-verification-queue.jsonl","independent-verification-registry.jsonl"):
  p=ROOT/"generated"/name; p.parent.mkdir(parents=True,exist_ok=True)
  if not p.exists(): p.write_text("",encoding="utf-8")
def run_gate(name:str,rel:str)->dict[str,Any]:
 p=ROOT/rel
 if not p.exists(): return {"name":name,"status":"BLOCK","reason":f"missing:{rel}"}
 try:
  x=subprocess.run(["python",str(p)],cwd=ROOT,text=True,capture_output=True,timeout=180)
  return {"name":name,"status":"PASS" if x.returncode==0 else "BLOCK","returncode":x.returncode,"stdout_tail":x.stdout[-2000:],"stderr_tail":x.stderr[-2000:]}
 except Exception as e: return {"name":name,"status":"BLOCK","reason":str(e)}
def main()->int:
 missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
 seed_nlp_status(); ensure_empty_verification_ledgers(); gates=[run_gate(n,p) for n,p in GATES]
 ok=not missing and all(g["status"]=="PASS" for g in gates)
 d={"schema_version":"1.2","generated_at":datetime.now(timezone.utc).isoformat(),
 "system":"SHIRMANI_SUPREME_TOTAL_AI_ML_NLP_AUTOMISSION","cycle":"5-minute",
 "pipeline":["Observe","Collect","Normalize","Analyze","Reason","Execute","Test","Verify","Audit","Learn","Improve"],
 "status":"PASS" if ok else "BLOCK","missing_required_files":missing,"gates":gates,
 "verification_state":{"claim_records":0,"queued_records":0,"verified_records":0,"note":"Empty ledgers are intentional until evidence-backed claims are submitted; no verification is fabricated."},
 "governance":{"fail_closed":True,"scheduled_code_mutation_allowed":False,"subjective_experience_claim_allowed":False,
 "independent_verification_required":True,"human_review_for_high_impact_actions":True,"accuracy_is_measured_not_declared":True,
 "synthetic_regression_benchmark_required":True,"neutrality_contract_required":True,"symmetric_evidence_standards":True,
 "counter_evidence_required":True,"authority_based_promotion_allowed":False}}
 d["fingerprint"]=hashlib.sha256(json.dumps(d,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 (OUT/"status.json").write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(d,ensure_ascii=False,indent=2)); return 0 if ok else 1
if __name__=="__main__": raise SystemExit(main())
