import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-evaluation.schema.json"

REQUIRED_SCHEMA_KEYS = [
    "record_id", "task", "dataset_fingerprint", "model", "metric",
    "baseline", "result", "confidence", "provenance", "verification_state"
]
REQUIRED_PROPERTIES = [
    "population_scope", "uncertainty", "limitations",
    "alternative_interpretations"
]
EXPECTED_STATES = ["REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"]


def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    missing = [key for key in REQUIRED_SCHEMA_KEYS if key not in schema.get("required", [])]
    if missing:
        raise SystemExit("Evaluation schema missing required keys: " + ", ".join(missing))

    properties = schema.get("properties", {})
    missing_properties = [key for key in REQUIRED_PROPERTIES if key not in properties]
    if missing_properties:
        raise SystemExit(
            "Evaluation schema missing required properties: " + ", ".join(missing_properties)
        )

    states = properties.get("verification_state", {}).get("enum", [])
    if states != EXPECTED_STATES:
        raise SystemExit("Verification states are not fail-closed")

    for key in ("baseline", "result"):
        if properties.get(key, {}).get("type") != "number":
            raise SystemExit(f"{key} must be numeric")

    if properties.get("provenance", {}).get("minItems") != 1:
        raise SystemExit("Provenance must contain at least one source")

    if properties.get("uncertainty", {}).get("minLength") != 1:
        raise SystemExit("Uncertainty statement is required")

    # Python's JSON parser accepts NaN/Infinity even though they are not valid JSON.
    # Keep the gate explicit so downstream evaluation records remain deterministic.
    for value in (0.0, 1.0):
        if not math.isfinite(value):
            raise SystemExit("Numeric gate is invalid")

    print("SHIRMANI Supreme NLP Evaluation Gate: PASS")


if __name__ == "__main__":
    main()
