import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"supreme-nlp"))
from quality_gate import gate

def base():
    return {"observed_signal":{"record_count":6,"independent_sources":["a","b"],
            "modalities":["plant-electric","temperature"]},"inference":{"confidence":0.88},
            "uncertainty":["calibration not established"],"verification_state":"UNVERIFIED",
            "governance":{"subjective_experience_claim_allowed":False}}

def test_confidence_never_promotes_verification():
    r=gate(base()); assert r["publishable"] is False
    assert r["verification_state"]=="UNVERIFIED"; assert r["status"]=="PASS"

def test_missing_evidence_fails_closed():
    x=base(); x["observed_signal"]["record_count"]=1; r=gate(x)
    assert r["status"]=="REVIEW"; assert "insufficient_samples" in r["failures"]

def test_verified_requires_explicit_independent_state():
    x=base(); x["verification_state"]="INDEPENDENTLY_VERIFIED"
    assert gate(x)["publishable"] is True

if __name__=="__main__":
    test_confidence_never_promotes_verification()
    test_missing_evidence_fails_closed()
    test_verified_requires_explicit_independent_state()
    print("Supreme NLP quality gate tests: PASS")
