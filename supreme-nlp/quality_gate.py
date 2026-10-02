"""Fail-closed quality gate for multimodal signal -> language outputs.
Provider/model agnostic. Confidence is not verification.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from typing import Any

SCHEMA_VERSION="2.0.0"
ALLOWED_VERIFICATION={"UNVERIFIED","REVIEW","INDEPENDENTLY_VERIFIED"}

def _hash(value: Any)->str:
    raw=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def assess(result: dict[str,Any])->dict[str,Any]:
    if not isinstance(result,dict):
        return {"schema_version":SCHEMA_VERSION,"status":"REJECT","reason":"result_not_object"}
    observed=result.get("observed_signal",{})
    inference=result.get("inference",{})
    uncertainty=result.get("uncertainty",[])
    verification=result.get("verification_state","UNVERIFIED")
    count=int(observed.get("record_count",0) or 0)
    sources=observed.get("independent_sources",[]) or []
    modalities=observed.get("modalities",[]) or []
    confidence=float(inference.get("confidence",0) or 0)
    failures=[]
    if count < 3: failures.append("insufficient_samples")
    if len(sources) < 2: failures.append("insufficient_independent_sources")
    if len(modalities) < 2: failures.append("insufficient_modalities")
    if not 0 <= confidence <= 1: failures.append("invalid_confidence")
    if not uncertainty: failures.append("missing_uncertainty")
    if verification not in ALLOWED_VERIFICATION: failures.append("invalid_verification_state")
    if result.get("governance",{}).get("subjective_experience_claim_allowed",True):
        failures.append("subjective_experience_claim_policy_violation")
    publishable=(not failures and verification=="INDEPENDENTLY_VERIFIED")
    return {"schema_version":SCHEMA_VERSION,"status":"PASS" if not failures else "REVIEW",
            "publishable":publishable,"verification_state":verification,
            "confidence":round(confidence,6),
            "quality":{"sample_count":count,"independent_sources":len(sources),"modalities":len(modalities)},
            "failures":failures,"rule":"confidence_never_equals_verification",
            "generated_at":datetime.now(timezone.utc).isoformat()}

def gate(result:dict[str,Any])->dict[str,Any]:
    report=assess(result)
    report["input_fingerprint"]=_hash(result)
    report["fingerprint"]=_hash(report)
    return report
