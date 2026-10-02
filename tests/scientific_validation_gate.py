import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "scientific-validation-record.schema.json"

def main():
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert data["properties"]["dataset"]["properties"]["train_eval_separation"]["const"] is True
    assert data["properties"]["result"]["properties"]["held_out"]["const"] is True
    assert data["properties"]["replication"]["properties"]["independent"]["type"] == "boolean"
    assert data["properties"]["replication"]["properties"]["status"]["enum"][-1] == "SUCCESS"
    assert "verification" in data["required"]
    text = "\n".join(json.dumps(x) for x in data["allOf"])
    assert "VERIFIED" in text and "independence_attestation" in text
    r = subprocess.run([sys.executable, str(ROOT / "factory" / "scientific_validation_gate.py")], cwd=ROOT, text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print("SHIRMANI Scientific Validation Gate tests: PASS")

if __name__ == "__main__":
    main()
