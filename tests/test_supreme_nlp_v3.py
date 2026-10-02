from agents.supreme_nlp_v3 import build_record, calibration_report

def main():
    good={"modality":"sensor","feature":"signal","value":1.0,"quality":1.0,"source":"a"}
    r=build_record([good],"test")
    assert r["result"]["interpretation"]["abstention"] is False
    assert r["result"]["interpretation"]["verification_status"]=="UNVERIFIED"
    noisy=[
      {"modality":"a","feature":"x","value":1e9,"quality":1.0,"source":"a"},
      {"modality":"b","feature":"x","value":-1e9,"quality":1.0,"source":"b"}]
    n=build_record(noisy,"abstain")
    assert n["result"]["interpretation"]["abstention"] is True
    c=calibration_report([0,.25,.75,1],[0,0,1,1])
    assert 0 <= c["brier_score"] <= 1
    assert 0 <= c["expected_calibration_error"] <= 1
    print("SUPREME_NLP_V3_CONTRACT=PASS")

if __name__=="__main__":
    main()
