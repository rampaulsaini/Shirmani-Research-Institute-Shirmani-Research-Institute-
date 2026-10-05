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

    # Abstention flags must be explicit booleans; strings such as "false" are ambiguous.
    for bad in ("false", "true", "yes", 0, 1):
        try:
            selective_risk([1], [1], [bad])
        except ValueError:
            pass
        else:
            raise AssertionError("ambiguous abstention flags must be rejected")

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
    # Missing feature groups are insufficient evidence, not positive drift proof.
    assert missing["drift_detected"] is False
    assert missing["status"] == "INSUFFICIENT_EVIDENCE"
    assert missing["features"]["latency|ms"]["status"] == "INSUFFICIENT_EVIDENCE"

    # Missing/blank units must never be treated as a comparable scale.
    missing_unit_drift = drift_report(
        [{"feature":"latency","value":10.0}],
        [{"feature":"latency","value":20.0}],
    )
    assert missing_unit_drift["status"] == "INSUFFICIENT_EVIDENCE"
    assert missing_unit_drift["reason"] == "MISSING_UNIT"
    assert missing_unit_drift["drift_detected"] is False

    # Empty reference/current observations are insufficient evidence, not no-drift.
    for ref, cur in (([], reference), (reference, []), ([], [])):
        empty_drift = drift_report(ref, cur)
        assert empty_drift["status"] == "INSUFFICIENT_EVIDENCE"
        assert empty_drift["reason"] == "EMPTY_REFERENCE_OR_CURRENT"
        assert empty_drift["drift_detected"] is False

    # Invalid drift thresholds must fail closed instead of accepting NaN/zero.
    for bad in (0, -1, float("nan"), float("inf")):
        try:
            drift_report(reference,current,bad)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid drift thresholds must be rejected")


    # Adversarial numeric inputs must fail closed rather than become trusted zeros.
    bad_numeric = build_record([
        {"modality":"sensor","feature":"signal","value":float("nan"),"quality":1.0,"source":"nan"},
        {"modality":"sensor","feature":"signal","value":float("inf"),"quality":1.0,"source":"inf"},
    ],"invalid-numeric")
    assert bad_numeric["result"]["status"] == "insufficient_quality"

    # Cross-modal disagreement must not compare incomparable feature/unit groups.
    incomparable = build_record([
        {"modality":"camera","feature":"intensity","value":100.0,"quality":1.0,"source":"cam","unit":"lux","baseline_mean":90.0,"baseline_std":5.0},
        {"modality":"microphone","feature":"intensity","value":0.01,"quality":1.0,"source":"mic","unit":"normalized","baseline_mean":0.01,"baseline_std":0.001},
    ],"incomparable")
    assert incomparable["result"]["features"]["cross_modal_disagreement"] == 0.0
    assert incomparable["result"]["interpretation"]["verification_status"] == "UNVERIFIED"

    # Distinct source strings and declared experiment IDs are not independent replication proof.
    provenance = build_record([
        {"modality":"sensor","feature":"signal","value":1.0,"quality":1.0,"source":"lab-A","experiment_id":"exp-1","unit":"u"},
        {"modality":"sensor","feature":"signal","value":1.1,"quality":1.0,"source":"lab-B","experiment_id":"exp-1","unit":"u"},
    ],"provenance-boundary")
    assert provenance["result"]["features"]["source_count"] == 2
    assert provenance["result"]["features"]["declared_unique_experiment_count"] == 1
    assert provenance["result"]["features"]["independence_status"] == "NOT_ESTABLISHED"
    assert provenance["provenance"]["independent_replication_verified"] is False

    # Missing-unit multi-signal inputs must abstain on comparability.
    missing_units = build_record([
        {"modality":"camera","feature":"signal","value":10.0,"quality":1.0,"source":"cam"},
        {"modality":"microphone","feature":"signal","value":0.1,"quality":1.0,"source":"mic"},
    ],"missing-units")
    assert missing_units["result"]["features"]["anomaly_comparability_status"] == "INSUFFICIENT_EVIDENCE"
    assert missing_units["result"]["interpretation"]["abstention"] is True

    # Calibration contracts reject empty data, invalid bins, and invalid probabilities.
    for bad_bins in (0, -1, 1.5, True):
        try:
            calibration_report([0.5], [1], bad_bins)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid calibration bins must be rejected")
    try:
        calibration_report([], [], 10)
    except ValueError:
        pass
    else:
        raise AssertionError("empty calibration data must be rejected")
    for bad_probability in (-0.1, 1.1, float("nan"), float("inf")):
        try:
            calibration_report([bad_probability], [1])
        except ValueError:
            pass
        else:
            raise AssertionError("invalid probabilities must be rejected")

    # Fingerprint integrity is distinct from scientific verification.
    assert r["provenance"]["independent_replication_verified"] is False
    from agents.supreme_nlp_v3 import verify_record_integrity
    assert verify_record_integrity(r) is True
    tampered = dict(r)
    tampered["result"] = dict(r["result"])
    tampered["result"]["features"] = dict(r["result"]["features"])
    tampered["result"]["features"]["sample_count"] = 999
    assert verify_record_integrity(tampered) is False

    print("SUPREME_NLP_V3_CONTRACT=PASS")


if __name__=="__main__":
    main()
