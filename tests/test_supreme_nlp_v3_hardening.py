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

    # Calibration rejects an invalid bin count instead of silently accepting it.
    try:
        calibration_report([0.2], [0], bins=0)
    except ValueError:
        pass
    else:
        raise AssertionError("bins=0 must be rejected")

    # Non-finite signal values are normalized into a safe finite representation.
    safe = build_record([{"modality":"sensor","feature":"x","value":float("nan")}], "nan")
    assert safe["result"]["signals"][0]["value"] == 0.0

    print("SUPREME_NLP_V3_HARDENING=PASS")

if __name__ == "__main__":
    main()