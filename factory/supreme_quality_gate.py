#!/usr/bin/env python3
"""Deterministic integrity gate for the AI/ML/NLP/Automission pipeline.
Measures engineering integrity only; it never claims scientific truth.
"""
from __future__ import annotations
import hashlib,json,py_compile
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; REPORT=GEN/"supreme-quality-status.json"
REQUIRED=["generated/claim-evidence.jsonl","generated/continuity-manifest.json"]
def sha256(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
 return h.hexdigest()
def pycheck():
 files=[p for r in (ROOT/"agents",ROOT/"factory") for p in r.rglob("*.py") if "_sources" not in p.parts and "__pycache__" not in p.parts]
 e=[]
 for p in files:
  try: py_compile.compile(str(p),doraise=True)
  except Exception as x:e.append(f"{p.relative_to(ROOT)}: {x}")
 return {"passed":not e,"files":len(files),"errors":e[:20]}
def jsoncheck():
 files=list((ROOT/"schemas").glob("*.json"))+list(GEN.glob("*.json"));e=[]
 for p in files:
  try: json.loads(p.read_text(encoding="utf-8"))
  except Exception as x:e.append(f"{p.relative_to(ROOT)}: {x}")
 return {"passed":not e,"files":len(files),"errors":e[:20]}
def claimcheck():
 p=ROOT/"generated/claim-evidence.jsonl"
 if not p.exists(): return {"passed":False,"records":0,"errors":["missing claim-evidence.jsonl"]}
 req={"claim_id","claim","claim_class","evidence_state","verification_state","provenance"};ids=set();nrec=0;e=[]
 for n,line in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
  if not line.strip():continue
  nrec+=1
  try:o=json.loads(line)
  except Exception as x:e.append(f"line {n}: invalid JSON: {x}");continue
  m=sorted(req-set(o))
  if m:e.append(f"line {n}: missing {m}")
  cid=o.get("claim_id")
  if cid in ids:e.append(f"line {n}: duplicate claim_id {cid}")
  ids.add(cid)
  if o.get("verification_state")=="INDEPENDENTLY_VERIFIED" and not o.get("independent_verification"):
   e.append(f"line {n}: unbacked independent verification promotion")
 return {"passed":not e,"records":nrec,"errors":e[:50]}
def main():
 checks={}
 missing=[x for x in REQUIRED if not (ROOT/x).exists() or (ROOT/x).stat().st_size==0]
 checks["required_artifacts"]={"passed":not missing,"missing":missing}
 checks["python_compile"]=pycheck();checks["json_integrity"]=jsoncheck();checks["claim_evidence_contract"]=claimcheck()
 passed=all(v.get("passed",True) for k,v in checks.items())
 report={"schema_version":"1.0","gate":"SHIRMANI_SUPREME_QUALITY_GATE","timestamp_utc":datetime.now(timezone.utc).isoformat(),"status":"PASS" if passed else "FAIL","accuracy_claim":"NOT_MEASURED","independent_verification":"NOT_GRANTED_BY_AUTOMATION","principle":"Workflow success is not scientific truth.","checks":checks}
 GEN.mkdir(exist_ok=True);REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(report,ensure_ascii=False,indent=2));return 0 if passed else 1
if __name__=="__main__": raise SystemExit(main())
