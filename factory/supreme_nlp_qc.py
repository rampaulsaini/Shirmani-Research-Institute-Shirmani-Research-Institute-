"""Quality gate for the Supreme NLP v2 control layer."""
from pathlib import Path
import sys

# Direct execution places factory/ on sys.path rather than the repository root.
# Add the root explicitly so the canonical agents package resolves identically
# in local runs and GitHub Actions.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agents.supreme_nlp import build_record

def main():
    signals = [
        {"modality":"sensor","feature":"electrical","value":1.0,"quality":0.95,"source":"qc-a"},
        {"modality":"vibration","feature":"rms","value":0.5,"quality":0.90,"source":"qc-b"},
    ]
    out = build_record(signals, "qc-smoke")
    required = {"schema_version","task_id","generated_at","pipeline",
                "result","simple_language","fingerprint","provenance"}
    assert required <= set(out), f"missing={sorted(required-set(out))}"
    assert out["schema_version"] == "supreme-nlp-v2"
    assert out["result"]["status"] == "interpreted"
    assert out["result"]["verification"]["status"] == "UNVERIFIED"
    assert out["provenance"]["verification_status"] == "UNVERIFIED"
    assert out["result"]["interpretation"]["confidence_status"] == "UNCALIBRATED"
    assert out["result"]["features"]["independent_sources"] == 2
    assert out["result"]["features"]["sample_count"] == 2
    print("SUPREME_NLP_QC_V2=PASS")

if __name__=="__main__":
    main()
