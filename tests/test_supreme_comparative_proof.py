import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_comparative_proof():
    r = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_comparative_proof.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert r.returncode == 0, r.stdout + r.stderr
    p = ROOT / "generated/supreme-nlp/comparative-proof.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    assert data["comparison_metrics"]["case_count"] == 3
    assert data["comparison_metrics"]["governance_contract_all_cases"] is True
    assert data["comparison_metrics"]["conflict_abstention"] is True
    assert data["comparison_metrics"]["no_signal_abstention"] is True
    assert data["governance"]["accuracy_is_measured_not_declared"] is True
    assert len(data["fingerprint"]) == 64
