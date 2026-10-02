import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    r = subprocess.run([sys.executable, str(ROOT / "factory/supreme_nlp_supervisory_control.py")], cwd=ROOT, text=True, capture_output=True, check=False)
    assert r.returncode == 0, r.stdout + r.stderr
    data = json.loads((ROOT / "generated/supreme-nlp-supervisory-control.json").read_text())
    assert data["status"] == "PASS"
    assert data["verification_state"] == "UNVERIFIED"
    assert data["blockers"] == []
    assert data["metrics"]["controller_count"] == 3
    assert data["metrics"]["failed_controller_count"] == 0
    assert all(v["exit_code"] == 0 for v in data["controllers"].values())
    print("SHIRMANI Supreme NLP Supervisory Control: PASS")

if __name__ == "__main__":
    main()
