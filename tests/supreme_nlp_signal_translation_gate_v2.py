import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-signal-translation-v2.schema.json"

def main():
    data=json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert "uncertainty" in data["required"]
    assert "alternatives" in data["required"]
    assert "provenance" in data["properties"]["source"]["required"]
    assert "ABSTAIN" in data["properties"]["verification_state"]["enum"]
    r=subprocess.run([sys.executable,str(ROOT/"factory"/"supreme_nlp_signal_translation_gate_v2.py")],cwd=ROOT,text=True,capture_output=True)
    assert r.returncode==0, r.stdout+r.stderr
    print("Supreme NLP Signal Translation Gate v2 tests: PASS")

if __name__=="__main__":
    main()
