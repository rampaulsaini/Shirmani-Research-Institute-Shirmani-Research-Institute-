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
    assert report["target_verified_records"] == 100_200
    assert report["verified_count"] >= 0
    assert report["remaining_to_target"] == max(100_200 - report["verified_count"], 0)
    assert 0 <= report["verification_completion_percent"] <= 100
    assert report["independence_boundary"].startswith("Automation validates result artifacts")

    from factory.supreme_independent_verification_ledger import load_schema, validate_record

    base = {
        "record_id": "synthetic-result-001",
        "source_record_id": "result-001",
        "claim_or_result": "A concrete measured result artifact.",
        "verification_scope": "Verify the recorded result against its evidence and reproducibility protocol.",
        "evidence_refs": ["evidence/result-001.json"],
        "independent_verifier": "independent-reviewer-1",
        "verification_method": "blind re-analysis",
        "reviewed_at": "2026-10-06T00:00:00Z",
        "verification_state": "VERIFIED",
        "limitations": ["Synthetic contract test only."],
    }

    missing_artifact = validate_record(base, load_schema())
    assert any("result_artifact_ref" in error for error in missing_artifact)
    assert any("result_artifact_sha256" in error for error in missing_artifact)

    valid = dict(base)
    valid["result_artifact_ref"] = "generated/results/result-001.json"
    valid["result_artifact_sha256"] = "a" * 64
    assert validate_record(valid, load_schema()) == []

    bad_hash = dict(valid, result_artifact_sha256="not-a-sha")
    assert any("result_artifact_sha256" in error for error in validate_record(bad_hash, load_schema()))

    # Non-VERIFIED states may be prepared before a concrete result artifact exists.
    pending = dict(base)
    pending["verification_state"] = "REVIEW"
    pending.pop("result_artifact_ref", None)
    pending.pop("result_artifact_sha256", None)
    assert validate_record(pending, load_schema()) == []

    print("SHIRMANI Supreme Independent Verification Ledger: PASS")
    print("RESULT_ARTIFACT_BOUNDARY=PASS")


if __name__ == "__main__":
    main()
