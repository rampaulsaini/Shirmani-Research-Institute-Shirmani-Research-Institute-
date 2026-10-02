import json
from pathlib import Path
from agents.supreme_nlp_evidence_v2 import build_record, ENGINE_VERSION

def main():
    schema=json.loads(Path("schemas/supreme-nlp-evidence-record.schema.json").read_text())
    assert schema["title"]=="Supreme NLP Evidence Record V2"
    r=build_record([
      {"modality":"synthetic","feature":"baseline","value":1.0,"quality":1.0,"source":"validator"}
    ],"validator")
    assert r["interpretation"]["status"]=="INFERENCE"
    assert r["verification"]["state"]=="UNVERIFIED"
    assert r["verification"]["independent_required"] is True
    assert r["provenance"]["engine_version"]==ENGINE_VERSION
    assert r["fingerprint"]
    print("SUPREME_NLP_EVIDENCE_V2=PASS")

if __name__=="__main__":
    main()
