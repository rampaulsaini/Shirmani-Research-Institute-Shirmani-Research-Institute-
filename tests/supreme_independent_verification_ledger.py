import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    result = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_independent_verification_ledger.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads((ROOT / "generated/supreme-independent-verification-ledger.json").read_text(encoding="utf-8"))
    target = json.loads(
        (ROOT / "config" / "independent-verification-target.json").read_text(encoding="utf-8")
    )["verification_target"]
    assert report["target_verified_records"] == target
    assert report["verified_count"] >= 0
    assert report["remaining_to_target"] == max(target - report["verified_count"], 0)
    assert 0 <= report["verification_completion_percent"] <= 100
    assert report["independence_boundary"].startswith("Automation validates")
    print("SHIRMANI Supreme Independent Verification Ledger: PASS")

if __name__ == "__main__":
    main()
