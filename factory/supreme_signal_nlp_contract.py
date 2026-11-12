#!/usr/bin/env python3
"""Deterministic contract gate for multimodal signal -> NLP translation.

This module validates that observed signals are translated into human language
with explicit evidence, uncertainty, provenance, and non-overclaiming semantics.
"""
from __future__ import annotations
import json, math
from pathlib import Path

REPORT = Path("generated/supreme-signal-nlp-contract-report.json")
REQUIRED_SIGNAL_FIELDS = {"signal_id","source_type","timestamp","features","context"}
ALLOWED_SOURCE_TYPES = {"text","audio","image","video","sensor","bioelectric","environmental","multimodal","unknown"}
REQUIRED_OUTPUT_FIELDS = {"observation","interpretation","confidence","evidence","limitations","provenance"}

def finite_number(value):
    return isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value)

def validate_signal(signal):
    errors=[]
    missing=REQUIRED_SIGNAL_FIELDS-set(signal)
    if missing: errors.append(f"signal missing fields: {sorted(missing)}")
    if signal.get("source_type") not in ALLOWED_SOURCE_TYPES:
        errors.append("signal source_type is not in the controlled vocabulary")
    if not isinstance(signal.get("features"),dict): errors.append("signal features must be an object")
    if not isinstance(signal.get("context"),dict): errors.append("signal context must be an object")
    return errors

def validate_output(output):
    errors=[]
    missing=REQUIRED_OUTPUT_FIELDS-set(output)
    if missing: errors.append(f"output missing fields: {sorted(missing)}")
    if not finite_number(output.get("confidence")) or not 0 <= output.get("confidence") <= 1:
        errors.append("confidence must be a finite number in [0, 1]")
    for key in ("evidence","limitations","provenance"):
        if not isinstance(output.get(key),list) or not output.get(key):
            errors.append(f"{key} must be a non-empty list")
    text=(str(output.get("observation",""))+" "+str(output.get("interpretation",""))).lower()
    forbidden=("proven to feel","directly feels","consciousness proven")
    if any(term in text for term in forbidden):
        errors.append("output contains an unsupported direct-subjective-experience claim")
    return errors

def main():
    signal={"signal_id":"contract-sample-001","source_type":"multimodal","timestamp":"2026-10-01T00:00:00Z",
            "features":{"spectral_change":0.42,"electrical_variance":0.31},"context":{"environment":"controlled-demo"}}
    output={"observation":"Measured signals changed relative to the baseline.",
            "interpretation":"The pattern is compatible with a changed system state.","confidence":0.82,
            "evidence":["sensor features","baseline comparison"],
            "limitations":["Signal pattern alone does not establish subjective experience."],
            "provenance":["contract-sample-001"]}
    se,oe=validate_signal(signal),validate_output(output)
    checks=[("signal_contract",not se),("translation_contract",not oe),
            ("confidence_bounded",0<=output["confidence"]<=1),("evidence_present",bool(output["evidence"])),
            ("limitations_present",bool(output["limitations"])),("provenance_present",bool(output["provenance"]))]
    passed=sum(ok for _,ok in checks)
    report={"mode":"fail-closed-multimodal-signal-to-nlp-contract","passed_checks":passed,
            "total_checks":len(checks),"checks":[{"name":n,"passed":ok} for n,ok in checks],
            "signal_errors":se,"output_errors":oe,
            "next_action":"CONTINUE_AUTOMISSION" if passed==len(checks) else "STOP_AND_REVIEW",
            "independent_verification_claim":False}
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 0 if passed==len(checks) else 1

if __name__=="__main__":
    raise SystemExit(main())
