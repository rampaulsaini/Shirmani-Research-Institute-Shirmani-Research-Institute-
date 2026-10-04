import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "factory" / "independent_verification_gate.py"
INPUT = ROOT / "generated" / "claim-evidence.jsonl"
OUTPUT = ROOT / "generated" / "independent-verification-status.json"


def test_registry_is_not_promoted_without_independent_review():
    ns = runpy.run_path(str(SCRIPT))
    assert ns["main"]() == 0

    report = json.loads(OUTPUT.read_text(encoding="utf-8"))
    records = [
        json.loads(line)
        for line in INPUT.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    assert report["records"] == len(records) == 10
    assert report["verified"] == 0
    assert report["verification_completion_percent"] == 0.0
    assert report["remaining_percent"] == 100.0
    assert report["errors"] == []
    assert "independent verification" in report["integrity_boundary"].lower()

    for record in records:
        verification = record.get("verification", {})
        assert verification.get("status") == "NOT_VERIFIED"
        assert verification.get("independent") is False


if __name__ == "__main__":
    test_registry_is_not_promoted_without_independent_review()
    print("independent verification gate regression: PASS")
