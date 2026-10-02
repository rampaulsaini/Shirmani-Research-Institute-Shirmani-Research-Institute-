from pathlib import Path
import json
from agents.supreme_nlp_automission_v2 import build_record

def main():
    json.loads(Path("schemas/supreme-nlp-automission-v2.schema.json").read_text(encoding="utf-8"))
    r=build_record([{"modality":"synthetic","feature":"a","value":1.0,"quality":1.0,"source":"validator"},{"modality":"synthetic","feature":"b","value":0.25,"quality":0.8,"source":"validator"}],"validator")
    g=r["governance"]
    assert g["fail_closed"] and g["independent_verification_required"]
    assert not g["subjective_experience_claim_allowed"]
    assert g["accuracy_is_measured_not_declared"] and not g["scheduled_code_mutation_allowed"]
    assert not r["interpretation"]["state"]["subjective_experience_inferred"]
    assert len(r["fingerprint"])==64
    print("SUPREME_NLP_AUTOMISSION_V2_VALIDATION: PASS")

if __name__=="__main__": main()
