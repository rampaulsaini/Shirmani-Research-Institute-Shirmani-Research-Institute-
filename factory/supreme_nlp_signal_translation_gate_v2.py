import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-signal-translation-v2.schema.json"
REQUIRED = ["record_id","timestamp","domain","source","signal","quality","features","context","model","inference","translation","confidence","evidence","alternatives","uncertainty","verification_state","audit"]
STATES = {"REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED","ABSTAIN"}

def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED if k not in schema.get("required", [])]
    if missing:
        raise SystemExit("Missing required fields: " + ", ".join(missing))
    props = schema["properties"]
    if set(props["verification_state"]["enum"]) != STATES:
        raise SystemExit("Unsafe/incomplete verification state set")
    conf = props["confidence"]["properties"]["value"]
    if conf.get("minimum") != 0 or conf.get("maximum") != 1:
        raise SystemExit("Confidence must be bounded [0,1]")
    if "provenance" not in props["source"]["required"]:
        raise SystemExit("Provenance must be required")
    if "uncertainty" not in schema["required"] or "ABSTAIN" not in STATES:
        raise SystemExit("Abstention/uncertainty gate missing")
    print("SHIRMANI Supreme NLP Signal Translation Gate v2: PASS")

if __name__ == "__main__":
    main()
