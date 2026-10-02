import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-signal-translation-v2.schema.json"

def main():
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(data["required"])
    for field in ("uncertainty","alternatives","evidence","calibration","ood"):
        assert field in required
    assert "provenance" in data["properties"]["source"]["required"]
    assert "ABSTAIN" in data["properties"]["verification_state"]["enum"]
    assert data["properties"]["confidence"]["properties"]["value"]["minimum"] == 0
    assert data["properties"]["confidence"]["properties"]["value"]["maximum"] == 1
    assert "verification" in data["properties"]
    text = "\n".join(json.dumps(x) for x in data["allOf"])
    assert "VERIFIED" in text and "independence_attestation" in text
    r = subprocess.run([sys.executable, str(ROOT / "factory" / "supreme_nlp_signal_translation_gate_v2.py")], cwd=ROOT, text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print("Supreme NLP Signal Translation Gate v2 tests: PASS")

if __name__ == "__main__":
    main()
