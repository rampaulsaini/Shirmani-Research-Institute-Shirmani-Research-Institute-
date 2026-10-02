import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    r = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_nlp_benchmark_controller.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert r.returncode == 0, r.stdout + r.stderr
    data = json.loads((ROOT / "generated/supreme-nlp-benchmark-controller.json").read_text())
    assert data["promotion_policy"] == "fail-closed"
    assert data["self_improvement"]["mode"] == "proposal-only"
    assert data["self_improvement"]["production_self_modification"] is False
    assert data["self_improvement"]["human_authorization_required"] is True
    print("SHIRMANI Supreme NLP Benchmark Controller: PASS")

if __name__ == "__main__":
    main()
