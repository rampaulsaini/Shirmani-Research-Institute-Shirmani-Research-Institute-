import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-benchmark-record.schema.json"
RECORD_DIR = ROOT / "generated" / "supreme-nlp-benchmark-records"

STATES = ["REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED", "PROPOSED_IMPROVEMENT"]
EXPECTED_KEYS = {
    "record_id", "task", "population_scope", "dataset_fingerprint", "model",
    "metric", "direction", "baseline", "candidate", "delta",
    "uncertainty", "provenance", "limitations", "verification_state"
}

def fail(message):
    raise SystemExit(message)

def validate_schema():
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    if set(data.get("required", [])) != EXPECTED_KEYS:
        fail("Benchmark schema required keys changed unexpectedly.")
    if data["properties"]["verification_state"]["enum"] != STATES:
        fail("Benchmark verification-state contract changed unexpectedly.")

def validate_record(record, source):
    if set(record) != EXPECTED_KEYS:
        fail(f"{source}: undeclared or missing record keys.")
    if record["direction"] not in {"higher_is_better", "lower_is_better"}:
        fail(f"{source}: invalid direction.")
    for key in ("baseline", "candidate", "delta"):
        value = record[key]
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
            fail(f"{source}: {key} must be a finite number.")
    expected_delta = (
        record["candidate"] - record["baseline"]
        if record["direction"] == "higher_is_better"
        else record["baseline"] - record["candidate"]
    )
    if not math.isclose(record["delta"], expected_delta, rel_tol=1e-12, abs_tol=1e-12):
        fail(f"{source}: delta does not match baseline/candidate/direction.")
    if not isinstance(record["provenance"], list) or not record["provenance"]:
        fail(f"{source}: provenance must be non-empty.")
    if record["verification_state"] not in STATES:
        fail(f"{source}: invalid verification_state.")
    if record["verification_state"] == "VERIFIED":
        joined = " ".join(str(x).lower() for x in record["provenance"])
        if "independent verification" not in joined:
            fail(f"{source}: VERIFIED requires explicit independent verification provenance.")

def main():
    validate_schema()
    checked = 0
    if RECORD_DIR.exists():
        for path in sorted(RECORD_DIR.glob("*.json")):
            validate_record(json.loads(path.read_text(encoding="utf-8")), str(path.relative_to(ROOT)))
            checked += 1
    print(json.dumps({
        "status": "PASS",
        "records_checked": checked,
        "record_directory": str(RECORD_DIR.relative_to(ROOT)),
        "promotion_policy": "fail-closed",
        "verified_requires_independent_verification": True
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
