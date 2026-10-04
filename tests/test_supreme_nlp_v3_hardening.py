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

    # Non-finite signal values are normalized into a safe finite representation.
    safe = build_record([{"modality":"sensor","feature":"x","value":float("nan")}], "nan")
    assert safe["result"]["signals"][0]["value"] == 0.0

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

    # Missing units are never treated as compatible for cross-modal comparison.
    missing_units = build_record([
        {"modality":"a","feature":"x","value":1.0,"baseline_mean":0.0,"baseline_std":1.0},
        {"modality":"b","feature":"x","value":100.0,"baseline_mean":0.0,"baseline_std":1.0},
    ], "missing-unit")
    assert missing_units["result"]["features"]["cross_modal_disagreement"] == 0.0

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

    print("SUPREME_NLP_V3_HARDENING=PASS")

if __name__ == "__main__":
    main()
