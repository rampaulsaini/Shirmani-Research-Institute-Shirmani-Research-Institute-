import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-signal-translation-v2.schema.json"
REQUIRED = ["record_id","timestamp","domain","source","signal","quality","features","context","model","inference","translation","confidence","calibration","ood","evidence","alternatives","uncertainty","verification_state","audit"]
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
    if props["confidence"]["properties"]["calibrated"].get("type") != "boolean":
        raise SystemExit("Confidence calibration flag missing")
    if props["calibration"]["properties"]["status"]["enum"] != ["MEASURED","UNMEASURED","INSUFFICIENT"]:
        raise SystemExit("Calibration state taxonomy drift detected")
    if props["ood"]["properties"]["status"]["enum"] != ["IN_DISTRIBUTION","OUT_OF_DISTRIBUTION","UNKNOWN"]:
        raise SystemExit("OOD state taxonomy drift detected")
    if props["evidence"].get("minItems") != 1 or props["alternatives"].get("minItems") != 1:
        raise SystemExit("Evidence and alternative-hypothesis requirements missing")
    if "provenance" not in props["source"]["required"]:
        raise SystemExit("Provenance must be required")
    if "ABSTAIN" not in STATES or "uncertainty" not in schema["required"]:
        raise SystemExit("Abstention/uncertainty gate missing")
    verification = props["verification"]
    required_verification = {"verifier_id","method","artifact_ref","outcome","independence_attestation"}
    if not required_verification.issubset(set(verification["required"])):
        raise SystemExit("Independent verification contract incomplete")
    print("SHIRMANI Supreme NLP Signal Translation Gate v2: PASS")
    print("Policy: VERIFIED requires measured calibration, explicit uncertainty, independent verification, and non-OOD evidence.")

if __name__ == "__main__":
    main()
