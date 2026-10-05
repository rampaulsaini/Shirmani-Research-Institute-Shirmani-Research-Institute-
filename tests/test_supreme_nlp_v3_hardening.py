from agents.supreme_nlp_v3 import build_record, calibration_report

def main():
    # Different units/scales without baselines must not create a false
    # cross-modal disagreement from raw numeric magnitudes.
    heterogeneous = [
        {"modality":"electrical","feature":"potential","value":1000,"unit":"mV","source":"a"},
        {"modality":"vibration","feature":"rms","value":0.001,"unit":"m/s2","source":"b"},
    ]
    r = build_record(heterogeneous, "heterogeneous-units")
    assert r["result"]["features"]["cross_modal_disagreement"] == 0.0
    assert r["result"]["features"]["anomaly_comparability_status"] == "INSUFFICIENT_EVIDENCE"
    assert r["result"]["interpretation"]["abstention"] is True
    assert r["result"]["features"]["anomaly_score"] == 0.0

    # Comparable signals retain anomaly detection; high within-group
    # variability must still trigger abstention.
    comparable = build_record([
        {"modality":"sensor-a","feature":"signal","value":100.0,"unit":"u","source":"a"},
        {"modality":"sensor-b","feature":"signal","value":-100.0,"unit":"u","source":"b"},
    ], "comparable-high-variance")
    assert comparable["result"]["features"]["anomaly_comparability_status"] == "COMPARABLE_GROUPS"
    assert comparable["result"]["features"]["anomaly_score"] >= 0.90
    assert comparable["result"]["interpretation"]["abstention"] is True

    # Cross-modal disagreement must use standardized values rather than raw
    # magnitudes, so equal z-scores agree even when baseline means differ.
    standardized_agreement = build_record([
        {"modality":"a","feature":"signal","value":11.0,"unit":"u","source":"a","baseline_mean":10.0,"baseline_std":1.0},
        {"modality":"b","feature":"signal","value":102.0,"unit":"u","source":"b","baseline_mean":100.0,"baseline_std":2.0},
    ], "standardized-agreement")
    assert standardized_agreement["result"]["features"]["cross_modal_disagreement"] == 0.0

    # Opposite standardized effects in a comparable feature/unit group must
    # trigger strong disagreement and therefore fail closed.
    standardized_disagreement = build_record([
        {"modality":"a","feature":"signal","value":11.0,"unit":"u","source":"a","baseline_mean":10.0,"baseline_std":1.0},
        {"modality":"b","feature":"signal","value":98.0,"unit":"u","source":"b","baseline_mean":100.0,"baseline_std":1.0},
    ], "standardized-disagreement")
    assert standardized_disagreement["result"]["features"]["cross_modal_disagreement"] >= 0.85
    assert standardized_disagreement["result"]["interpretation"]["abstention"] is True

    # Same feature with different units is not silently compared as if the
    # units were interchangeable; the result must remain fail-closed.
    mixed_units = build_record([
        {"modality":"a","feature":"signal","value":1.0,"unit":"m","source":"a","baseline_mean":0.0,"baseline_std":1.0},
        {"modality":"b","feature":"signal","value":100.0,"unit":"cm","source":"b","baseline_mean":0.0,"baseline_std":1.0},
    ], "mixed-units")
    assert mixed_units["result"]["features"]["cross_modal_disagreement"] == 0.0
    assert mixed_units["result"]["features"]["anomaly_comparability_status"] == "INSUFFICIENT_EVIDENCE"
    assert mixed_units["result"]["interpretation"]["abstention"] is True

    # Calibration rejects an invalid bin count instead of silently accepting it.
    try:
        calibration_report([0.2], [0], bins=0)
    except ValueError:
        pass
    else:
        raise AssertionError("bins=0 must be rejected")

    # Calibration rejects non-finite and out-of-range probabilities.
    for bad in ([float("nan")], [float("inf")], [-0.1], [1.1]):
        try:
            calibration_report(bad, [0])
        except ValueError:
            pass
        else:
            raise AssertionError("invalid probabilities must be rejected")

    # Non-finite/invalid signal values are normalized for auditability but
    # must become unusable rather than trusted zero-valued observations.
    for bad in (float("nan"), float("inf"), "not-a-number"):
        safe = build_record([{"modality":"sensor","feature":"x","value":bad}], "invalid-value")
        assert safe["result"]["signals"][0]["value"] == 0.0
        assert safe["result"]["signals"][0]["quality"] == 0.0
        assert safe["result"]["status"] == "insufficient_quality"

    # Non-finite quality must fail closed instead of becoming a perfect-quality signal.
    quality_safe = build_record([
        {"modality":"sensor","feature":"x","value":1.0,"quality":float("nan")}
    ], "nan-quality")
    assert quality_safe["result"]["status"] == "insufficient_quality"

    # Non-mapping signal inputs are rejected instead of being coerced unpredictably.
    try:
        build_record([None], "invalid-signal")
    except ValueError:
        pass
    else:
        raise AssertionError("non-mapping signals must be rejected")

    # Invalid baseline statistics must not leak NaN/Inf into z-score diagnostics.
    baseline_safe = build_record([
        {"modality":"a","feature":"x","value":1.0,"unit":"u","baseline_mean":float("nan"),"baseline_std":float("inf")},
        {"modality":"b","feature":"x","value":2.0,"unit":"u","baseline_mean":1.0,"baseline_std":1.0},
    ], "baseline-nonfinite")
    features = baseline_safe["result"]["features"]
    assert features["baseline_z_score_max_abs"] == 1.0
    assert features["cross_modal_disagreement"] == 0.0

    # Missing units are never treated as comparable anomaly groups.
    missing_units = build_record([
        {"modality":"a","feature":"x","value":1.0,"baseline_mean":0.0,"baseline_std":1.0},
        {"modality":"b","feature":"x","value":100.0,"baseline_mean":0.0,"baseline_std":1.0},
    ], "missing-unit")
    assert missing_units["result"]["features"]["cross_modal_disagreement"] == 0.0
    assert missing_units["result"]["features"]["anomaly_comparability_status"] == "INSUFFICIENT_EVIDENCE"
    assert missing_units["result"]["interpretation"]["abstention"] is True

    # Repeated source IDs are a source count, not evidence of independent experiments.
    duplicate_sources = build_record([
        {"modality":"a","feature":"x","value":1.0,"source":"same","experiment_id":"exp-1"},
        {"modality":"b","feature":"y","value":1.1,"source":"same","experiment_id":"exp-1"},
    ], "duplicate-source")
    assert duplicate_sources["result"]["features"]["source_count"] == 1
    assert duplicate_sources["result"]["features"]["declared_unique_experiment_count"] == 1
    assert duplicate_sources["result"]["features"]["experiment_provenance_status"] == "DECLARED_IDENTIFIERS_ONLY"
    assert duplicate_sources["result"]["features"]["independence_status"] == "NOT_ESTABLISHED"
    assert duplicate_sources["provenance"]["independent_replication_verified"] is False

    # Distinct experiment identifiers are the explicit provenance signal.
    independent = build_record([
        {"modality":"a","feature":"x","value":1.0,"source":"same","experiment_id":"exp-1"},
        {"modality":"b","feature":"x","value":1.1,"source":"same","experiment_id":"exp-2"},
    ], "independent-experiments")
    assert independent["result"]["features"]["source_count"] == 1
    assert independent["result"]["features"]["declared_unique_experiment_count"] == 2
    assert independent["result"]["features"]["experiment_provenance_status"] == "DECLARED_IDENTIFIERS_ONLY"
    assert independent["result"]["features"]["independence_status"] == "NOT_ESTABLISHED"
    assert independent["provenance"]["independent_replication_verified"] is False

    # Drift must fail closed when the feature unit is missing instead of
    # silently comparing values in the empty-string unit bucket.
    from agents.supreme_nlp_v3 import drift_report
    missing_unit_drift = drift_report(
        [{"feature":"signal","value":1.0}],
        [{"feature":"signal","value":2.0}],
    )
    assert missing_unit_drift["status"] == "INSUFFICIENT_EVIDENCE"
    assert missing_unit_drift["drift_detected"] is False
    assert missing_unit_drift["insufficient_evidence"] is True
    assert missing_unit_drift["features"]["signal|<MISSING_UNIT>"]["status"] == "INSUFFICIENT_EVIDENCE"

    # Drift must fail closed on malformed observed values rather than
    # allowing normalize() to turn them into trusted zeros.
    for bad in (float("nan"), float("inf"), "not-a-number"):
        invalid_drift = drift_report(
            [{"feature":"x","unit":"u","value":bad}],
            [{"feature":"x","unit":"u","value":1.0}],
        )
        assert invalid_drift["status"] == "INSUFFICIENT_EVIDENCE"
        assert invalid_drift["drift_detected"] is False
        assert invalid_drift["insufficient_evidence"] is True
        reverse_invalid_drift = drift_report(
            [{"feature":"x","unit":"u","value":1.0}],
            [{"feature":"x","unit":"u","value":bad}],
        )
        assert reverse_invalid_drift["status"] == "INSUFFICIENT_EVIDENCE"
        assert reverse_invalid_drift["drift_detected"] is False

    # Numeric thresholds supplied as strings are normalized before comparison.
    numeric_string_threshold = drift_report(
        [{"feature":"x","unit":"u","value":0.0}],
        [{"feature":"x","unit":"u","value":3.0}],
        "2.0",
    )
    assert numeric_string_threshold["drift_detected"] is True
    assert numeric_string_threshold["threshold"] == 2.0

    # Drift thresholds must reject type-confused values rather than leaking a TypeError.
    try:
        from agents.supreme_nlp_v3 import drift_report
        drift_report([{"feature":"x","unit":"u","value":1}], [{"feature":"x","unit":"u","value":1}], "invalid")
    except ValueError:
        pass
    else:
        raise AssertionError("non-numeric drift thresholds must raise ValueError")

    # Record fingerprints must detect tampering and fail closed on malformed records.
    from agents.supreme_nlp_v3 import verify_record_integrity
    record = build_record([{"modality":"sensor","feature":"x","value":1.0}], "integrity")
    assert verify_record_integrity(record) is True
    tampered = dict(record)
    tampered["result"] = dict(record["result"])
    tampered["result"]["status"] = "tampered"
    assert verify_record_integrity(tampered) is False
    assert verify_record_integrity({"fingerprint": ""}) is False


    # Calibration labels must be explicit binary values; truthy strings and
    # non-binary numerics are ambiguous and must fail closed.
    for bad_label in ("1", 2, -1, 0.5, None):
        try:
            calibration_report([0.5], [bad_label])
        except ValueError:
            pass
        else:
            raise AssertionError("ambiguous labels must be rejected")

    # Calibration also rejects an empty evaluation set and mismatched lengths.
    for probabilities, labels in (([], []), ([0.5], []), ([], [0])):
        try:
            calibration_report(probabilities, labels)
        except ValueError:
            pass
        else:
            raise AssertionError("empty or mismatched calibration inputs must be rejected")

    # A feature present in only one population is not a valid drift comparison.
    from agents.supreme_nlp_v3 import drift_report
    missing_feature = drift_report(
        [{"feature":"x","unit":"u","value":1.0}],
        [{"feature":"y","unit":"u","value":2.0}],
    )
    assert missing_feature["status"] == "INSUFFICIENT_EVIDENCE"
    assert missing_feature["drift_detected"] is False
    assert missing_feature["insufficient_evidence"] is True
    assert missing_feature["features"]["x|u"]["status"] == "INSUFFICIENT_EVIDENCE"
    assert missing_feature["features"]["y|u"]["status"] == "INSUFFICIENT_EVIDENCE"

    # Non-finite thresholds must be rejected just like non-numeric thresholds.
    for bad_threshold in (float("nan"), float("inf"), 0, -1):
        try:
            drift_report(
                [{"feature":"x","unit":"u","value":1.0}],
                [{"feature":"x","unit":"u","value":2.0}],
                bad_threshold,
            )
        except ValueError:
            pass
        else:
            raise AssertionError("invalid drift thresholds must be rejected")

    print("SUPREME_NLP_V3_HARDENING=PASS")

if __name__ == "__main__":
    main()
