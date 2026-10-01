"""Contract tests for Supreme evidence evaluation/calibration."""
from agents.supreme_evaluation import build_record

def main():
    rows=[
        {"label":1,"probability":0.90},{"label":1,"probability":0.80},
        {"label":0,"probability":0.10},{"label":0,"probability":0.20},
        {"label":1,"probability":0.55},{"label":0,"probability":0.51},
    ]
    rec=build_record(rows,0.60); m=rec["metrics"]
    assert rec["schema_version"]=="supreme-eval-v1"
    assert m["status"]=="OK" and m["count"]==6
    assert all(0<=m[k]<=1 for k in ("accuracy","precision","recall","f1","brier_score","ece"))
    assert m["abstentions"]==2 and m["evaluated"]==4 and m["coverage"]==0.666667
    assert rec["calibration"]["status"]=="NOT_CALIBRATED"
    assert rec["governance"]["accuracy_is_measured_not_declared"] is True
    assert len(rec["fingerprint"])==64
    empty=build_record([])
    assert empty["metrics"]["status"]=="NO_LABELLED_DATA" and empty["metrics"]["count"]==0
    print("SUPREME_EVALUATION_CONTRACT_OK")

if __name__=="__main__": main()
