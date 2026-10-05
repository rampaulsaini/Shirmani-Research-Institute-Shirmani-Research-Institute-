import json
import subprocess
import sys
from factory.supreme_independent_verification_ledger import load_schema, validate_record
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    result = subprocess.run(
        [sys.executable, str(ROOT / "factory/supreme_independent_verification_ledger.py")],
        cwd=ROOT, text=True, capture_output=True, check=False
    )
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads((ROOT / "generated/supreme-independent-verification-ledger.json").read_text(encoding="utf-8"))
    assert report["target_verified_records"] == 100_200
    assert report["verified_count"] >= 0
    assert report["remaining_to_target"] == max(100_200 - report["verified_count"], 0)
    assert 0 <= report["verification_completion_percent"] <= 100
    assert report["independence_boundary"].startswith("Automation validates")
    assert report["result_first_boundary"].startswith("VERIFIED is reserved for reviewed result artifacts")

    base = {
        "record_id": "VR-TEST",
        "source_record_id": "RESULT-001",
        "claim_or_result": "A concrete produced result",
        "verification_scope": "Result reproducibility and evidence review",
        "evidence_refs": ["evidence://test-001"],
        "independent_verifier": "reviewer-A",
        "verification_method": "independent reproduction",
        "reviewed_at": "2026-10-05T00:00:00Z",
        "verification_state": "VERIFIED",
        "limitations": ["test fixture"],
    }
    errors = validate_record(base, load_schema())
    assert "VERIFIED record requires result_artifact_ref" in errors

    base["result_artifact_ref"] = "generated/results/RESULT-001.json"
    assert validate_record(base, load_schema()) == []

    # Pre-verification states may remain queued/reviewable without a result
    # artifact; the new boundary applies only when promotion to VERIFIED occurs.
    queued = dict(base)
    queued.pop("result_artifact_ref")
    queued["verification_state"] = "REVIEW"
    assert validate_record(queued, load_schema()) == []
    print("SHIRMANI Supreme Independent Verification Ledger: PASS")

if __name__ == "__main__":
    main()
