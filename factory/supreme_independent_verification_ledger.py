import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-independent-verification-record.schema.json"
RECORD_DIR = ROOT / "generated" / "independent-verification-records"
OUT = ROOT / "generated" / "supreme-independent-verification-ledger.json"
TARGET_CONFIG = ROOT / "config" / "independent-verification-target.json"


def target_value():
    data = json.loads(TARGET_CONFIG.read_text(encoding="utf-8"))
    target = int(data["verification_target"])
    if target <= 0:
        raise RuntimeError("verification_target must be positive")
    return target
STATES = {"REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"}

REQUIRED = [
    "record_id", "source_record_id", "claim_or_result", "verification_scope",
    "evidence_refs", "independent_verifier", "verification_method",
    "reviewed_at", "verification_state", "limitations"
]

def load_schema():
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    if data.get("required") != REQUIRED:
        raise RuntimeError("Verification schema required keys changed unexpectedly.")
    if set(data.get("properties", {}).get("verification_state", {}).get("enum", [])) != STATES:
        raise RuntimeError("Verification state contract changed unexpectedly.")
    return data

def validate_record(record, schema):
    errors = []
    allowed_keys = set(schema["required"]) | {"result_artifact_ref"}
    if not set(record).issubset(allowed_keys):
        errors.append("record contains keys outside the verification schema")
    for key in REQUIRED:
        if key not in record:
            continue
        if key == "evidence_refs" and (not isinstance(record[key], list) or not record[key]):
            errors.append("evidence_refs must be a non-empty array")
        if key == "limitations" and not isinstance(record[key], list):
            errors.append("limitations must be an array")
    state = record.get("verification_state")
    if state not in STATES:
        errors.append("invalid verification_state: " + repr(state))
    if state == "VERIFIED":
        for key in ["source_record_id", "verification_scope", "independent_verifier", "verification_method", "reviewed_at"]:
            if not record.get(key):
                errors.append("VERIFIED record missing " + key)
        if not record.get("evidence_refs"):
            errors.append("VERIFIED record requires evidence_refs")
        if not record.get("result_artifact_ref"):
            errors.append("VERIFIED record requires result_artifact_ref")
    return errors

def main():
    started = datetime.now(timezone.utc)
    schema = load_schema()
    target = target_value()
    RECORD_DIR.mkdir(parents=True, exist_ok=True)

    counts = {state: 0 for state in sorted(STATES)}
    blockers = []
    records_seen = 0

    for path in sorted(RECORD_DIR.glob("*.json")):
        records_seen += 1
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            blockers.append(path.name + ": invalid JSON: " + str(exc))
            continue
        errors = validate_record(record, schema)
        if errors:
            blockers.extend(path.name + ": " + error for error in errors)
            continue
        counts[record["verification_state"]] += 1

    verified = counts["VERIFIED"]
    completion = round((verified / target) * 100, 6)
    status = "PASS" if not blockers else "BLOCKED"
    if not blockers and verified == 0:
        status = "AWAITING_INDEPENDENT_EVIDENCE"

    report = {
        "event_id": "supreme-independent-verification-" + started.strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": started.isoformat(),
        "repository": "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
        "status": status,
        "target_verified_records": target,
        "records_seen": records_seen,
        "state_counts": counts,
        "verified_count": verified,
        "verification_completion_percent": completion,
        "remaining_to_target": max(target - verified, 0),
        "blockers": blockers,
        "provenance": ["verification-record directory", "supreme-independent-verification-record.schema.json", "deterministic ledger audit"],
        "independence_boundary": "Automation validates declared evidence and structure; it does not self-attest independent verification.",
        "result_first_boundary": "VERIFIED is reserved for reviewed result artifacts; workflow execution, queue presence, or direct verification flags cannot create VERIFIED."
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
