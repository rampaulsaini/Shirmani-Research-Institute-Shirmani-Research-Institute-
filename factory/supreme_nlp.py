"""Supreme NLP quality gate.

Dependency-free control-plane validation for multimodal signal -> language
pipelines. It separates observations from interpretations and requires
provenance, uncertainty and verification metadata.
"""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

REQUIRED_FIELDS = {"event_id","source_type","observations","interpretation","confidence","evidence","verification","provenance"}

def _bounded_confidence(value: Any) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    return value

def validate_record(record: Dict[str, Any]) -> Dict[str, Any]:
    missing = sorted(REQUIRED_FIELDS - record.keys())
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))
    confidence = _bounded_confidence(record["confidence"])
    observations = record["observations"]
    evidence = record["evidence"]
    verification = record["verification"]
    provenance = record["provenance"]
    if not isinstance(observations, list) or not observations:
        raise ValueError("observations must be a non-empty list")
    if not isinstance(evidence, list):
        raise ValueError("evidence must be a list")
    if not isinstance(verification, dict):
        raise ValueError("verification must be an object")
    if not isinstance(provenance, dict):
        raise ValueError("provenance must be an object")
    verified = bool(verification.get("independent_check", False))
    return {"event_id":str(record["event_id"]),"status":"verified" if verified else "unverified","confidence":confidence,"observation_count":len(observations),"evidence_count":len(evidence),"independent_check":verified}

def run_self_test() -> Dict[str, Any]:
    sample = {
        "event_id":"synthetic-self-test-001","source_type":"synthetic_multimodal",
        "observations":[{"modality":"signal","feature":"pattern_A","value":0.72},{"modality":"environment","feature":"temperature","value":24.1}],
        "interpretation":{"plain_language":"A measurable signal pattern was detected.","claim_type":"data_interpretation"},
        "confidence":0.72,"evidence":["synthetic_fixture"],
        "verification":{"independent_check":True,"method":"deterministic_fixture"},
        "provenance":{"source":"self_test","timestamp":"synthetic"}
    }
    return {"ok":True,"record":validate_record(sample)}

def main() -> None:
    result=run_self_test()
    result["generated_at"]=datetime.now(timezone.utc).isoformat()
    result["engine_hash"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out=Path("generated/supreme-nlp-status.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
