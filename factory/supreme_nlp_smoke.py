from agents.supreme_nlp_practitioner import build_practitioner_record,calibration_metrics,compare_practitioner_records
def main():
    obs=[{"modality":"electrical","feature":"signal","value":0.42,"quality":0.95,"source":"synthetic","timestamp":"2026-10-01T00:00:00Z"},{"modality":"acoustic","feature":"signal","value":0.44,"quality":0.94,"source":"synthetic-b","timestamp":"2026-10-01T00:00:01Z"}]
    a=build_practitioner_record(obs,"भाव/अनुभव को signal-based hypothesis के रूप में समझाएं")
    b=build_practitioner_record([{**x,"value":x["value"]+2} for x in obs],"same test")
    assert a["governance"]["subjective_experience_claim_allowed"] is False
    assert 0 <= a["result"]["features"]["confidence"] <= 1
    assert calibration_metrics([.1,.8,.9,.2],[0,1,1,0])["sample_count"]==4
    assert compare_practitioner_records(a,b)["disagreement"] is True
    print("SUPREME-NLP-SMOKE: PASS")
if __name__=="__main__": main()
