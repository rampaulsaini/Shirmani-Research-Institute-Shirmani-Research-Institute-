import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    r = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_nlp_benchmark_integrity.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert r.returncode == 0, r.stdout + r.stderr
    print("SHIRMANI Supreme NLP Benchmark Integrity Gate: PASS")

if __name__ == "__main__":
    main()
