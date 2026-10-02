from __future__ import annotations
import json
from pathlib import Path
from agents.supreme_nlp_multimodal import analyze, fingerprint, to_simple_language

ROOT=Path(__file__).resolve().parents[1]

def main():
    schema=json.loads((ROOT/"schemas/supreme-nlp-adapter-contract.schema.json").read_text(encoding="utf-8"))
    p=schema["properties"]["governance"]["properties"]
    assert p["abstention_supported"]["const"] is True
    assert p["subjective_experience_claim_allowed"]["const"] is False
    assert p["independent_verification_required"]["const"] is True

    rows=[
      {"modality":"electrical","feature":"signal","value":1.0,"quality":1.0,"source":"a"},
      {"modality":"audio","feature":"signal","value":1.02,"quality":1.0,"source":"b"}
    ]
    r=analyze(rows,request="भाव/एहसास interpretation",source_type="plant")
    assert r["evidence_class"]=="INFERRED"
    assert r["status"]=="CANDIDATE"
    assert 0<=r["confidence"]<=1
    assert r["verification"]["promotion_allowed"] is False
    assert r["uncertainty"]["abstention_available"] is True
    assert r["provenance"]["fingerprint"]==fingerprint(r)
    assert "प्रत्यक्ष भाव" in to_simple_language(r)

    empty=analyze([])
    assert empty["status"]=="NO_CLAIM"
    assert empty["evidence_class"]=="UNKNOWN"
    print("SUPREME_NLP_MULTIMODAL_VALIDATION: PASS")

if __name__=="__main__":
    main()
