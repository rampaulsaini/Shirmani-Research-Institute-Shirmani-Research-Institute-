import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    r = subprocess.run(
        [sys.executable, str(ROOT / "factory" / "scientific_validation_gate.py")],
        cwd=ROOT, text=True, capture_output=True
    )
    assert r.returncode == 0, r.stdout + r.stderr
    print("SHIRMANI Scientific Validation Gate tests: PASS")

if __name__ == "__main__":
    main()
