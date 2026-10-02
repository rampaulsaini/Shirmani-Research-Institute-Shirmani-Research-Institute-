import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp-supervisory-control.json"
SCHEMA = ROOT / "schemas" / "supreme-nlp-supervisory-control.schema.json"

CONTROLLERS = [
    ("health", ROOT / "factory/supreme_nlp_automission_health.py"),
    ("benchmark", ROOT / "factory/supreme_nlp_benchmark_controller.py"),
    ("orchestrator", ROOT / "factory/ultra_mega_infinity_quantum_automission.py"),
]

def run_controller(path):
    r = subprocess.run([sys.executable, str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
    output = (r.stdout + r.stderr).strip()
    declared = "UNKNOWN"
    try:
        data = json.loads(r.stdout)
        declared = data.get("verification_state", data.get("status", "UNKNOWN"))
    except (json.JSONDecodeError, TypeError):
        pass
    return r.returncode, declared, output[-2500:]

def validate_schema():
    if not SCHEMA.is_file():
        return ["supervisory schema is missing"]
    try:
        data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ["supervisory schema is invalid JSON"]
    expected = {"cycle_id","timestamp","repository","status","verification_state","controllers","blockers","warnings","provenance","metrics"}
    blockers = []
    if set(data.get("required", [])) != expected:
        blockers.append("supervisory schema required keys do not match contract")
    if data.get("additionalProperties") is not False:
        blockers.append("supervisory schema must reject undeclared properties")
    return blockers

def main():
    started = time.monotonic()
    blockers = validate_schema()
    warnings = []
    results = {}

    for name, path in CONTROLLERS:
        if not path.is_file():
            blockers.append("missing controller: " + str(path))
            results[name] = {"exit_code":127,"declared_state":"BLOCKED","output_tail":"missing"}
            continue
        code, declared, output = run_controller(path)
        results[name] = {"exit_code":code,"declared_state":declared,"output_tail":output}
        if code != 0:
            blockers.append(f"{name} controller failed with exit code {code}")
        if declared == "BLOCKED":
            blockers.append(f"{name} controller declared BLOCKED")
        if declared == "REVIEW":
            warnings.append(f"{name} controller declared REVIEW")

    if any(v["declared_state"] == "VERIFIED" for v in results.values()):
        warnings.append("A controller reported VERIFIED; independent verification must still be checked explicitly.")

    failed = sum(1 for v in results.values() if v["exit_code"] != 0)
    status = "BLOCKED" if blockers else ("REVIEW" if warnings else "PASS")
    verification_state = "BLOCKED" if blockers else ("REVIEW" if warnings else "UNVERIFIED")

    record = {
        "cycle_id":"supervisor-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp":datetime.now(timezone.utc).isoformat(),
        "repository":"rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
        "status":status,
        "verification_state":verification_state,
        "controllers":results,
        "blockers":blockers,
        "warnings":warnings,
        "provenance":["repository supervisory contract","deterministic controller exit codes","controller-declared states"],
        "metrics":{"cycle_duration_seconds":round(time.monotonic()-started,4),"controller_count":len(CONTROLLERS),"failed_controller_count":failed}
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))
    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
