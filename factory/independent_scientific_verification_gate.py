#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/"schemas/independent-scientific-verification.schema.json"
REGISTRY=ROOT/"generated/independent-verification-registry.jsonl"
REQUIRED=["verification_id","claim_id","claim_type","candidate_system","verifier_identity","independence_statement","evidence_refs","method","dataset_or_material_fingerprint","analysis_fingerprint","replication_status","result","limitations","verification_state"]
STATES=["BLOCKED","REGISTERED","REVIEW","UNVERIFIED","VERIFIED"]
REPLICATION=["INDEPENDENT_REPLICATION","MULTI_SITE_REPLICATION","NOT_REPLICATED","PARTIAL"]
def validate_schema():
 s=json.loads(SCHEMA.read_text())
 if any(k not in s["required"] for k in REQUIRED): raise SystemExit("schema incomplete")
 if s["properties"]["verification_state"]["enum"]!=STATES: raise SystemExit("states not fail-closed")
 if s["properties"]["replication_status"]["enum"]!=REPLICATION: raise SystemExit("replication states changed")
def validate_record(r):
 missing=[k for k in REQUIRED if k not in r]
 if missing:return "MISSING:"+",".join(missing)
 if r["verification_state"]=="VERIFIED":
  if len(r["evidence_refs"])<2:return "VERIFIED_REQUIRES_TWO_EVIDENCE_REFS"
  if r["replication_status"] not in {"INDEPENDENT_REPLICATION","MULTI_SITE_REPLICATION"}:return "VERIFIED_REQUIRES_INDEPENDENT_REPLICATION"
  if r["candidate_system"]["name"].strip().lower()==r["verifier_identity"]["name"].strip().lower():return "CANDIDATE_AND_VERIFIER_MUST_BE_INDEPENDENT"
  if len(r["independence_statement"])<20 or len(r["method"])<20:return "VERIFIED_REQUIRES_INDEPENDENCE_AND_METHOD"
  if not r.get("dataset_or_material_fingerprint") or not r.get("analysis_fingerprint"):return "VERIFIED_REQUIRES_FINGERPRINTS"
  if not r.get("raw_data_ref") or not r.get("pre_registration_ref"):return "VERIFIED_REQUIRES_RAW_DATA_AND_PREREGISTRATION"
 return "OK"
def main():
 validate_schema(); records=[]
 if REGISTRY.exists():
  for line in REGISTRY.read_text().splitlines():
   if line.strip():records.append(json.loads(line))
 bad=[e for e in (validate_record(r) for r in records) if e!="OK"]
 if bad:raise SystemExit("BLOCKED: "+" | ".join(bad))
 print(json.dumps({"status":"PASS","registry_records":len(records),"verified_records":sum(r.get("verification_state")=="VERIFIED" for r in records),"note":"PASS means registry integrity, not scientific proof."},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
