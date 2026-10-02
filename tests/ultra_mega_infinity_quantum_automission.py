import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    r = subprocess.run(
        [sys.executable, str(ROOT / "factory/ultra_mega_infinity_quantum_automission.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert r.returncode == 0, r.stdout + r.stderr
    data = json.loads((ROOT / "generated/ultra-mega-infinity-quantum-automission.json").read_text())
    assert data["architecture"] == "ultra-mega-infinity-quantum"
    assert len(data["stages"]) >= 8
    assert data["verification_state"] == "UNVERIFIED"
    assert data["blockers"] == []
    print("SHIRMANI Ultra Mega Infinity Quantum Automission: PASS")

if __name__ == "__main__":
    main()
