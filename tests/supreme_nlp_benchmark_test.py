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
    data = json.loads((ROOT / "generated/supreme-nlp/benchmark.json").read_text(encoding="utf-8"))
    assert data["benchmark"] == "supreme-nlp-synthetic-v1"
    assert data["status"] == "PASS"
    assert data["classification_accuracy"] == 1.0
    assert data["uncertainty_language_contract"] is True
    assert data["deterministic_fingerprints"] is True
    assert data["limitations"]
    print("SHIRMANI Supreme NLP benchmark regression: PASS")

if __name__ == "__main__":
    main()
