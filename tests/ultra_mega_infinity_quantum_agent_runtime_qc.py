import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = ROOT / "factory/ultra_mega_infinity_quantum_agent_runtime.py"
    r = subprocess.run([sys.executable, str(p)], cwd=ROOT, text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr
    record = json.loads((ROOT / "generated/ultra-mega-infinity-quantum-agent-runtime.json").read_text(encoding="utf-8"))
    assert record["runtime_status"] == "READY"
    assert record["verification_state"] == "UNVERIFIED"
    assert len(record["agents"]) == 10
    assert record["blockers"] == []
    print("Ultra Mega Infinity Quantum Agent Runtime QC: PASS")

if __name__ == "__main__":
    main()
