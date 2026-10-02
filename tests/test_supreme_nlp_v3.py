from agents.supreme_nlp_v3 import (
    build_record,
    calibration_report,
    classification_report,
    selective_risk,
    drift_report,
)


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

    # Ambiguous truthy strings must not silently become positive labels.
    for bad in ("false", "true", "yes"):
        try:
            calibration_report([0.5], [bad])
        except ValueError:
            pass
        else:
            raise AssertionError("ambiguous string labels must be rejected")

    c=calibration_report([0,.25,.75,1],[0,0,1,1])
    assert 0 <= c["brier_score"] <= 1
    assert 0 <= c["expected_calibration_error"] <= 1

    m=classification_report([1,1,0,0],[1,0,1,0])
    assert m["precision"] == .5
    assert m["recall"] == .5
    assert m["f1"] == .5
    assert m["tp"] == 1 and m["fp"] == 1 and m["fn"] == 1 and m["tn"] == 1

    # Strict binary validation must apply consistently to predictions/labels.
    for bad in ("false", "true", "yes"):
        try:
            classification_report([1], [bad])
        except ValueError:
            pass
        else:
            raise AssertionError("ambiguous classification labels must be rejected")
        try:
            selective_risk([1], [bad], [False])
        except ValueError:
            pass
        else:
            raise AssertionError("ambiguous selective-risk labels must be rejected")

    s=selective_risk([1,1,0,0],[1,0,1,0],[False,True,False,False])
    assert s["coverage"] == .75
    assert s["abstention_rate"] == .25
    assert s["selective_risk"] == round(1/3,6)

    reference=[
      {"feature":"latency","unit":"ms","value":10},
      {"feature":"latency","unit":"ms","value":12},
      {"feature":"latency","unit":"ms","value":8},
    ]
    current=[
      {"feature":"latency","unit":"ms","value":10},
      {"feature":"latency","unit":"ms","value":11},
      {"feature":"latency","unit":"ms","value":9},
    ]
    d=drift_report(reference,current)
    assert d["status"] == "NO_DRIFT_DETECTED"
    missing=drift_report(reference,[{"feature":"other","unit":"ms","value":10}])
    assert missing["drift_detected"] is True
    assert missing["features"]["latency|ms"]["status"] == "INSUFFICIENT_EVIDENCE"

    # Invalid drift thresholds must fail closed instead of accepting NaN/zero.
    for bad in (0, -1, float("nan"), float("inf")):
        try:
            drift_report(reference,current,bad)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid drift thresholds must be rejected")

    print("SUPREME_NLP_V3_CONTRACT=PASS")


if __name__=="__main__":
    main()
