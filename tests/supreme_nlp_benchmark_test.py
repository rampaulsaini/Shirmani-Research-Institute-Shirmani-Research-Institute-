import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    result = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_nlp_benchmark.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert result.returncode == 0, result.stdout + result.stderr
    data = json.loads((ROOT / "generated/supreme-nlp-benchmark.json").read_text(encoding="utf-8"))
    assert data["benchmark_id"] == "supreme-nlp-reference-v1"
    assert data["metric"] == "accuracy"
    assert data["sample_count"] == 12
    assert data["correct_count"] == 12
    assert data["result"] == 1.0
    assert data["verification_state"] == "UNVERIFIED"
    assert data["limitations"]
    print("SHIRMANI Supreme NLP benchmark regression: PASS")

if __name__ == "__main__":
    main()
