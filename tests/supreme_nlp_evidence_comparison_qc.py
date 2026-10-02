import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    r = subprocess.run(
        [sys.executable, str(ROOT / "factory" / "supreme_nlp_evidence_comparison_qc.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    print("SHIRMANI Supreme NLP Evidence & Comparative Reasoning Gate test: PASS")

if __name__ == "__main__":
    main()
