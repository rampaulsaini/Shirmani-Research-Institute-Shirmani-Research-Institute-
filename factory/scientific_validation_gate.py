import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "scientific-validation-record.schema.json"

REQUIRED = {
    "record_id","claim_class","hypothesis","operational_definition",
    "dataset","controls","metrics","result","uncertainty",
    "replication","verification_state","provenance"
}
STATES = {"REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED","ABSTAIN"}

def main():
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(data.get("required", []))
    missing = REQUIRED - required
    if missing:
        raise SystemExit("Missing required validation fields: " + ", ".join(sorted(missing)))
    if set(data["properties"]["verification_state"]["enum"]) != STATES:
        raise SystemExit("Unsafe/incomplete verification states")
    if data["properties"]["dataset"]["properties"]["train_eval_separation"]["type"] != "boolean":
        raise SystemExit("Train/evaluation separation gate missing")
    if "independent" not in data["properties"]["replication"]["required"]:
        raise SystemExit("Independent replication field missing")
    print("SHIRMANI Scientific Validation Gate: PASS")

if __name__ == "__main__":
    main()
