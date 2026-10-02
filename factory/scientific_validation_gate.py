import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "scientific-validation-record.schema.json"
STATES = {"REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED","ABSTAIN"}
CLAIM_CLASSES = {"OBSERVATION","ASSOCIATION","PREDICTION","CAUSAL","SUBJECTIVE-EXPERIENCE"}

def require(mapping, key, label):
    if key not in mapping:
        raise SystemExit(f"Missing {label}: {key}")
    return mapping[key]

def main():
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(data.get("required", []))
    expected = {"record_id","claim_class","hypothesis","operational_definition","dataset","controls","metrics","result","uncertainty","replication","verification_state","provenance"}
    missing = expected - required
    if missing:
        raise SystemExit("Missing required validation fields: " + ", ".join(sorted(missing)))
    props = data["properties"]
    if set(props["verification_state"]["enum"]) != STATES:
        raise SystemExit("Unsafe/incomplete verification states")
    if set(props["claim_class"]["enum"]) != CLAIM_CLASSES:
        raise SystemExit("Claim-class taxonomy drift detected")
    dataset = props["dataset"]
    if dataset["properties"]["train_eval_separation"].get("const") is not True:
        raise SystemExit("Training/evaluation separation must be a hard gate")
    if dataset["properties"]["test_protection"].get("type") != "boolean":
        raise SystemExit("Protected test-set field missing")
    replication = props["replication"]
    if "independent" not in replication["required"] or "replication_id" not in replication["required"]:
        raise SystemExit("Independent replication identity is required")
    verification = props["verification"]
    for key in ("verifier_id","method","artifact_ref","outcome","independence_attestation"):
        require(verification["required"], key, "verification field")
    if verification["properties"]["outcome"]["enum"] != ["PASS","FAIL","INCONCLUSIVE"]:
        raise SystemExit("Verification outcome taxonomy drift detected")
    print("SHIRMANI Scientific Validation Gate: PASS")
    print("Policy: VERIFIED requires held-out evidence, protected testing, independent SUCCESS replication, and an independent PASS artifact.")

if __name__ == "__main__":
    main()
