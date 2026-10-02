import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEALTH = ROOT / "generated" / "supreme-nlp-automission-health.json"

CHECKS = [
    "factory/supreme_nlp_contract_qc.py",
    "factory/supreme_nlp_evaluation_qc.py",
    "factory/supreme_nlp_automission_health.py",
]

def run_check(script):
    proc = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, text=True, capture_output=True, timeout=120)
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise SystemExit(f"REGRESSION BLOCKED: {script}")
    print(proc.stdout)

def main():
    for script in CHECKS:
        run_check(script)
    data = json.loads(HEALTH.read_text(encoding="utf-8"))
    required = {"event_id","timestamp","repository","contract_status","schema_status","governance_status","graph_status","regression_status","verification_state","blockers","warnings","provenance","cycle_duration_seconds"}
    missing = sorted(required - data.keys())
    if missing: raise SystemExit("REGRESSION BLOCKED: health record missing " + ", ".join(missing))
    if data["blockers"]: raise SystemExit("REGRESSION BLOCKED: deterministic blockers remain: " + " | ".join(data["blockers"]))
    for key in ["contract_status","schema_status","governance_status","graph_status","regression_status"]:
        if data.get(key) != "PASS": raise SystemExit(f"REGRESSION BLOCKED: {key}={data.get(key)!r}")
    if data.get("verification_state") != "UNVERIFIED":
        raise SystemExit("REGRESSION BLOCKED: operational health must remain distinct from independent scientific verification.")
    print("SHIRMANI Supreme NLP deterministic regression gate: PASS")
    print("Operational health PASS; scientific/model verification remains separate.")

if __name__ == "__main__":
    main()
