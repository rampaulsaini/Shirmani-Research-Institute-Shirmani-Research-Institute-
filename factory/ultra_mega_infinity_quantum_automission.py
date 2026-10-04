import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "ultra-mega-infinity-quantum-automission.json"

REQUIRED = [
    "docs/ultra-mega-infinity-quantum-ai-ml-nlp-automission.md",
    "schemas/ultra-mega-infinity-quantum-orchestrator.schema.json",
    "schemas/agent-governance.json",
    "factory/supreme_nlp_contract_qc.py",
    "factory/supreme_nlp_evaluation_qc.py",
    "factory/supreme_nlp_automission_health.py",
]

STAGES = ["observe","collect","normalize","analyze","reason","execute","test","verify","audit","learn","improve"]

def fingerprint(paths):
    h = hashlib.sha256()
    for rel in paths:
        p = ROOT / rel
        h.update(rel.encode())
        h.update(p.read_bytes())
    return h.hexdigest()

def gate(path):
    env = dict(__import__("os").environ)
    env["PYTHONPATH"] = str(ROOT) + (":" + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
    r = subprocess.run([sys.executable, str(ROOT / path)], cwd=ROOT, env=env, text=True, capture_output=True, check=False)
    return {"exit_code": r.returncode, "output": (r.stdout + r.stderr)[-1200:]}

def main():
    started = time.monotonic()
    blockers = [p for p in REQUIRED if not (ROOT / p).is_file()]
    contract = ROOT / REQUIRED[0]
    governance = ROOT / "schemas/agent-governance.json"

    if contract.exists():
        text = contract.read_text(encoding="utf-8").lower()
        for term in ["measured signal", "model inference", "confidence", "provenance", "fail-closed"]:
            if term not in text:
                blockers.append("contract-missing:" + term)

    if governance.exists():
        g = json.loads(governance.read_text(encoding="utf-8"))
        for key in ("fail_closed", "provenance_required_for_claims", "fabrication_prohibited"):
            if g.get(key) is not True:
                blockers.append("governance-not-fail-closed:" + key)

    gates = {}
    for name, path in [
        ("contract_qc", "factory/supreme_nlp_contract_qc.py"),
        ("evaluation_qc", "factory/supreme_nlp_evaluation_qc.py"),
        ("health_qc", "factory/supreme_nlp_automission_health.py"),
    ]:
        if Path(path).exists():
            gates[name] = gate(path)
            if gates[name]["exit_code"] != 0:
                blockers.append(name + "-failed")

    state = "BLOCKED" if blockers else "UNVERIFIED"
    record = {
        "cycle_id": "umiaq-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "architecture": "ultra-mega-infinity-quantum",
        "stages": STAGES,
        "verification_state": state,
        "provenance": ["repository files", "deterministic QC gates", "governance contract"],
        "blockers": blockers,
        "metrics": {"cycle_duration_seconds": round(time.monotonic() - started, 4)},
        "input_fingerprint": fingerprint(REQUIRED) if not blockers else None,
        "gates": gates,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))
    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
