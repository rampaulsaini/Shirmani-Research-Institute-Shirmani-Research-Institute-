#!/usr/bin/env python3
"""Continuous runtime gate for the SHIRMANI Supreme NLP architecture."""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"supreme-nlp-runtime-status.json"
REQUIRED_FILES=[
 "docs/supreme-nlp-practitioner-contract.md",
 "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
 "schemas/agent-governance.json",
 "schemas/supreme-nlp-practitioner.schema.json",
 "schemas/supreme-nlp-quality-gate.schema.json",
 "schemas/supreme-nlp-record.schema.json",
 "schemas/supreme-nlp-signal-record.schema.json",
 "factory/supreme_nlp_contract_qc.py",
]
CONTRACT_TERMS=["Measured signal","Model inference","Interpretation","Confidence","Unresolved uncertainty","Independent verification","Fail-closed rules","Continuous improvement"]
def sha256_file(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
 return h.hexdigest()
def check_json(path):
 try: json.loads(path.read_text(encoding="utf-8")); return []
 except Exception as exc: return [f"{path}: invalid_json:{exc}"]
def main():
 errors=[]; warnings=[]; files={}; governance={}
 for rel in REQUIRED_FILES:
  p=ROOT/rel
  if not p.exists(): errors.append(f"missing_required_file:{rel}"); continue
  files[rel]={"sha256":sha256_file(p),"bytes":p.stat().st_size}
 contract=ROOT/"docs/supreme-nlp-practitioner-contract.md"
 if contract.exists():
  text=contract.read_text(encoding="utf-8")
  for term in CONTRACT_TERMS:
   if term not in text: errors.append(f"contract_missing:{term}")
 gp=ROOT/"schemas/agent-governance.json"
 if gp.exists():
  errors.extend(check_json(gp))
  try: governance=json.loads(gp.read_text(encoding="utf-8"))
  except Exception: governance={}
 for rel in REQUIRED_FILES:
  if rel.endswith(".json") and (ROOT/rel).exists(): errors.extend(check_json(ROOT/rel))
 if governance.get("fail_closed") is not True: errors.append("governance_fail_closed_required")
 if governance.get("provenance_required_for_claims") is not True: errors.append("governance_provenance_required")
 if governance.get("fabrication_prohibited") is not True: errors.append("governance_fabrication_prohibited")
 if (ROOT/"generated"/"worker-status.json").exists():
  try: json.loads((ROOT/"generated"/"worker-status.json").read_text(encoding="utf-8"))
  except Exception as exc: errors.append(f"worker-status_invalid_json:{exc}")
 else: warnings.append("worker-status_not_present")
 result={"schema_version":"supreme-nlp-runtime-v3","generated_at":datetime.now(timezone.utc).isoformat(),"status":"BLOCKED" if errors else ("READY_WITH_WARNINGS" if warnings else "READY"),"promotion_allowed":False,"runtime_model_execution":"not_claimed","independent_verification":"required","errors":errors,"warnings":warnings,"governance":{"fail_closed":governance.get("fail_closed"),"provenance_required_for_claims":governance.get("provenance_required_for_claims"),"fabrication_prohibited":governance.get("fabrication_prohibited"),"subjective_experience_claim_allowed":False,"scheduled_code_mutation_allowed":False},"artifacts":files,"next_loop":["Observe","Collect","Normalize","Analyze","Reason","Translate","Test","Verify","Audit","Learn","Improve"]}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,ensure_ascii=False,indent=2)); return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())