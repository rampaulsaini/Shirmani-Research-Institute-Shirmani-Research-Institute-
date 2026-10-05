from agents.supreme_nlp_v3 import build_record, calibration_report, validate_result_boundary

def main():
    signals=[
        {"modality":"electrical","feature":"potential","value":1.0,"quality":.95,"source":"sensor-a","baseline_mean":0.5,"baseline_std":.1},
        {"modality":"vibration","feature":"rms","value":.8,"quality":.90,"source":"sensor-b","baseline_mean":0.5,"baseline_std":.1},
    ]
    r=build_record(signals,"v3-qc")
    assert r["schema_version"]=="supreme-nlp-v3"
    assert r["result"]["status"]=="interpreted"
    assert r["result"]["interpretation"]["verification_status"]=="UNVERIFIED"
    assert r["result"]["interpretation"]["confidence_status"]=="UNCALIBRATED"
    assert r["result"]["features"]["source_count"]==2
    assert "cross_modal_disagreement" in r["result"]["features"]
    boundary = validate_result_boundary(r)
    assert boundary["status"] == "PASS"
    assert boundary["scientific_verification_granted"] is False
    c=calibration_report([.1,.9,.8,.2],[0,1,1,0])
    assert c["sample_count"]==4 and c["status"]=="CALIBRATED_EVALUATION"
    print("SUPREME_NLP_V3_QC=PASS")

if __name__=="__main__":
    main()
