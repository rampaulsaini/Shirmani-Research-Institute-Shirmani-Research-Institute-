import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "generated" / "independent-verification-status-2026-09-29.json"
SCHEMA = ROOT / "schemas" / "independent-verification-record.schema.json"

def main():
    data = json.loads(STATUS.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    records = data["records"]
    summary = data["verification_summary"]

    assert len(records) == summary["queue_records"]
    assert summary["independently_verified_records"] == 0
    assert summary["independent_verified_percent"] == 0
    assert all(r["status"] != "VERIFIED" for r in records)

    required = set(schema["required"])
    for r in records:
        assert required.issubset(r), f"Missing schema fields: {r.get('id')}"
        assert r["independent_test"]["result"] == "PENDING"
        assert r["reproducibility"]["result_match"] is False
        assert r["counter_evidence"]["reviewed"] is False
        assert r["audit"]["passed"] is False
        assert r["reviewer_decision"]["decision"] == "PENDING"

    print(f"Queue records: {len(records)}")
    print("Independent VERIFIED records: 0")
    print("Gate result: FAIL-CLOSED / UNVERIFIED")
    print("No workflow success is promoted to independent verification.")

if __name__ == "__main__":
    main()
