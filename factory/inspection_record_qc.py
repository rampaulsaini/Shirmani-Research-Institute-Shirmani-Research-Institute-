"""Deterministic QC for Nishpaksh Inspection records."""
from pathlib import Path
import json
def validate(r):
    errors=[]
    required={"schema","created_at","purpose","level","evidence_input_present","claim_method","time_context","conflict_declaration","biometric_mode","storage","status","failures","verification","certificate","notes"}
    errors += [f"missing:{k}" for k in sorted(required-set(r))]
    if r.get("schema")!="nishpaksh-inspection-record/v1": errors.append("schema_mismatch")
    if r.get("status") not in {"DEFERRED","READY_FOR_REVIEW","VERIFIED"}: errors.append("invalid_status")
    if r.get("verification") not in {"NOT_VERIFIED","PENDING","INDEPENDENTLY_VERIFIED"}: errors.append("invalid_verification")
    if r.get("certificate")!="PROCESS_ONLY": errors.append("certificate_must_be_process_only")
    if r.get("verification")=="INDEPENDENTLY_VERIFIED" and r.get("status")!="VERIFIED": errors.append("verification_status_inconsistent")
    if r.get("status")=="READY_FOR_REVIEW" and not r.get("evidence_input_present"): errors.append("ready_without_input")
    if r.get("biometric_mode")!="Disabled" and "Biometrics do not establish truth" not in " ".join(r.get("notes",[])): errors.append("biometric_boundary_missing")
    return errors
def main():
    paths=list(Path("generated").glob("inspection-record*.json"))
    if not paths:
        print("Inspection record QC: NO_RECORDS")
        return 0
    failed=0
    for p in paths:
        errors=validate(json.loads(p.read_text(encoding="utf-8")));print(f"{p}: {'PASS' if not errors else 'FAIL'}")
        if errors: print("  "+"; ".join(errors));failed+=1
    return 1 if failed else 0
if __name__=="__main__": raise SystemExit(main())
