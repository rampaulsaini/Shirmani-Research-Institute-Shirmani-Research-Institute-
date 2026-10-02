import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    result = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_multimodal_signal_qc.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode:
        print(result.stdout + result.stderr)
        raise SystemExit(result.returncode)
    print(result.stdout)

if __name__ == "__main__":
    main()
