import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-evaluation.schema.json"

REQUIRED_SCHEMA_KEYS = [
    "record_id","task","dataset_fingerprint","model","metric","baseline",
    "result","confidence","provenance","verification_state"
]

def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_SCHEMA_KEYS if key not in schema.get("required", [])]
    if missing:
        raise SystemExit("Evaluation schema missing required keys: " + ", ".join(missing))
    states = schema.get("properties", {}).get("verification_state", {}).get("enum", [])
    if states != ["REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED"]:
        raise SystemExit("Verification states are not fail-closed")
    if schema.get("properties", {}).get("baseline", {}).get("type") != "number":
        raise SystemExit("Baseline must be numeric")
    if schema.get("properties", {}).get("result", {}).get("type") != "number":
        raise SystemExit("Result must be numeric")
    print("SHIRMANI Supreme NLP Evaluation Gate: PASS")

if __name__ == "__main__":
    main()
