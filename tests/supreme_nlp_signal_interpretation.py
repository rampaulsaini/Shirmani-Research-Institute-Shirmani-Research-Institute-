import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    qc = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_nlp_signal_interpretation_qc.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert qc.returncode == 0, qc.stdout + qc.stderr

    schema = json.loads(
        (ROOT / "schemas/supreme-nlp-signal-interpretation.schema.json").read_text(encoding="utf-8")
    )
    assert schema["additionalProperties"] is False
    assert "subjective_experience_claim" in schema["properties"]
    assert schema["properties"]["verification_state"]["enum"] == ["REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED"]
    assert "biopotential" in schema["properties"]["signal_modality"]["enum"]
    assert "multimodal" in schema["properties"]["signal_modality"]["enum"]
    print("SHIRMANI Supreme NLP Signal Interpretation hardening: PASS")

if __name__ == "__main__":
    main()
