"""Deterministic contract tests for Supreme NLP Practitioner."""
from agents.supreme_nlp_practitioner import build_practitioner_record, detect_language, semantic_intent, fuse

def main():
    rows=[
        {"modality":"sensor","feature":"voltage","value":1.0,"quality":.95,"source":"s1"},
        {"modality":"audio","feature":"vibration","value":1.1,"quality":.90,"source":"s2"},
        {"modality":"environment","feature":"temperature","value":1.05,"quality":.92,"source":"s3"},
        {"modality":"sensor","feature":"voltage","value":1.02,"quality":.96,"source":"s1"},
    ]
    rec=build_practitioner_record(rows,"वनस्पति संकेत क्या बताते हैं?")
    assert rec["schema_version"]=="1.0"
    assert rec["result"]["status"]=="interpreted"
    f=rec["result"]["features"]
    assert 0<=f["confidence"]<=1 and 0<=f["agreement"]<=1
    assert f["modalities"]==3 and f["sources"]==3
    assert f["sample_count"]==4 and f["independent_sources"]==3
    assert f["evidence_grade"] in {"A","B","C","D"}
    assert len(rec["fingerprint"])==64
    assert rec["governance"]["fail_closed"] is True
    assert rec["governance"]["subjective_experience_claim_allowed"] is False
    assert detect_language("यह क्या है?")=="hi"
    assert detect_language("ਇਹ ਕੀ ਹੈ?")=="pa"
    assert semantic_intent("what is the cause?")=="causal_question"
    assert semantic_intent("इसका एहसास क्या है?")=="experience_interpretation"
    assert fuse([])["status"]=="insufficient_quality"
    print("SUPREME_NLP_PRACTITIONER_CONTRACT_OK")
    print(rec["simple_language"])

if __name__=="__main__":
    main()
