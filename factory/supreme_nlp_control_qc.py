#!/usr/bin/env python3
"""Deterministic readiness QC for the SHIRMANI Supreme NLP control plane."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/"docs/supreme-nlp-practitioner-contract.md"
EVAL=ROOT/"docs/supreme-nlp-evaluation-standard.md"
GRAPH=ROOT/"docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"
SCHEMA=ROOT/"schemas/multimodal-signal-record.schema.json"
GOV=ROOT/"schemas/agent-governance.json"

def require(path, terms):
    text=path.read_text(encoding="utf-8")
    missing=[t for t in terms if t not in text]
    if missing:
        raise SystemExit(f"{path}: missing required terms: {', '.join(missing)}")

def main():
    require(CONTRACT,["Measured signal","Model inference","Interpretation","Confidence","Unresolved uncertainty","Fail-closed rules"])
    require(EVAL,["Evaluation dimensions","Accuracy gate","Continuous improvement","Biological and environmental interpretation"])
    require(GRAPH,["Multimodal Perception","ML Models","NLP","Independent Verification","Continuous Improvement"])
    schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
    for key in ["record_id","timestamp","source_type","measurement","provenance","interpretation_boundary"]:
        if key not in schema.get("required",[]):
            raise SystemExit(f"Signal schema missing required field: {key}")
    gov=json.loads(GOV.read_text(encoding="utf-8"))
    if gov.get("fail_closed") is not True or gov.get("fabrication_prohibited") is not True:
        raise SystemExit("Governance is not fail-closed/fabrication-safe")
    if gov.get("authorization",{}).get("verification_promotion")!="independent_verification_required":
        raise SystemExit("Independent verification promotion gate missing")
    print("SHIRMANI Supreme NLP Control Plane: READY_FOR_EVALUATION")

if __name__=="__main__":
    main()
