import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "independent_verification_gate.py"
TMP = ROOT / "generated" / ".verification-gate-test.json"

BASE = {
    "operational_definition": "Defined test",
    "independent_sources": ["independent-source"],
    "test_or_observation": "Reproducible test",
    "counter_evidence_review": "Reviewed",
    "result": "Pass",
    "reviewer": {"identity": "independent-reviewer", "role": "reviewer"},
    "reviewed_at": "2026-10-04T00:00:00Z",
    "decision": "VERIFIED",
}


def run(records, expected):
    data = {
        "verification_summary": {
            "queue_records": len(records),
            "independently_verified_records": expected,
            "independent_verified_percent": round(expected / len(records) * 100, 6),
            "evidence_supported_records": 0,
        },
        "records": records,
    }
    TMP.write_text(json.dumps(data), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(GATE), "--registry", str(TMP)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr or result.stdout)


def expect_failure(records, expected):
    data = {
        "verification_summary": {
            "queue_records": len(records),
            "independently_verified_records": expected,
            "independent_verified_percent": round(expected / len(records) * 100, 6),
            "evidence_supported_records": 0,
        },
        "records": records,
    }
    TMP.write_text(json.dumps(data), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(GATE), "--registry", str(TMP)],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        raise AssertionError("expected verification gate failure")


try:
    run([{"id": "IV-TEST-001", "status": "UNVERIFIED"}], 0)
    run([{"id": "IV-TEST-001", "status": "INDEPENDENTLY_VERIFIED", **BASE}], 1)

    pending_result = {
        "id": "IV-TEST-002",
        "status": "INDEPENDENTLY_VERIFIED",
        **BASE,
        "result": "PENDING",
    }
    expect_failure([pending_result], 1)

    pending_observation = {
        "id": "IV-TEST-003",
        "status": "INDEPENDENTLY_VERIFIED",
        **BASE,
        "test_or_observation": "PENDING_REVIEW",
    }
    expect_failure([pending_observation], 1)

    print("independent_verification_gate tests: PASS")
finally:
    TMP.unlink(missing_ok=True)
