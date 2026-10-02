import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "ultra-mega-infinity-quantum-agent-runtime.json"

REQUIRED = [
    "docs/ultra-mega-infinity-quantum-agent-runtime.md",
    "schemas/ultra-mega-infinity-quantum-signal.schema.json",
    "docs/supreme-nlp-practitioner-contract.md",
    "docs/supreme-nlp-evaluation-gate.md",
    "schemas/agent-governance.json",
]
AGENTS = ["intake","quality","ml","nlp","reasoning","evidence","verification","security","audit","improvement"]

def fingerprint(paths):
    h = hashlib.sha256()
    for rel in paths:
        p = ROOT / rel
        h.update(rel.encode())
        h.update(p.read_bytes())
    return h.hexdigest()

def main():
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    blockers = []
    if missing:
        blockers.append("Missing runtime dependency: " + ", ".join(missing))

    gov = ROOT / "schemas/agent-governance.json"
    if gov.exists():
        data = json.loads(gov.read_text(encoding="utf-8"))
        for key in ("fail_closed","provenance_required_for_claims","fabrication_prohibited"):
            if data.get(key) is not True:
                blockers.append("Governance requirement failed: " + key)

    status = "BLOCKED" if blockers else "READY"
    record = {
        "event_id":"u-m-i-q-runtime-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp":datetime.now(timezone.utc).isoformat(),
        "runtime":"ultra-mega-infinity-quantum",
        "runtime_status":status,
        "agents":AGENTS,
        "cycle":"Observe → Collect → Normalize → Analyze → Reason → Translate → Test → Verify → Audit → Learn → Improve",
        "dependency_fingerprint":fingerprint(REQUIRED) if not missing else None,
        "blockers":blockers,
        "verification_state":"UNVERIFIED",
        "accuracy_statement":"Task-specific accuracy must be measured; runtime readiness is not model accuracy.",
        "quantum_statement":"Project naming layer only; no quantum hardware or quantum advantage is asserted by this record.",
        "provenance":REQUIRED,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))
    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
