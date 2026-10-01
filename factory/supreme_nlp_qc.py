"""Quality gate for the Supreme NLP control layer."""
from agents.supreme_nlp_agent import interpret

def main():
    out=interpret({"context":"controlled signal observation",
                   "signals":[{"type":"electrical","value":1.0},{"type":"vibration","value":0.5}]})
    required={"schema_version","status","input_sha256","natural_language",
              "evidence_boundary","confidence","verification","next_actions"}
    assert required <= set(out), f"missing={sorted(required-set(out))}"
    assert out["status"]=="UNVERIFIED"
    assert out["confidence"]==0.0
    assert out["verification"]["independent_reviewer_required"] is True
    assert out["evidence_boundary"]=="observable_signal_only"
    print("SUPREME_NLP_QC=PASS")

if __name__=="__main__":
    main()
