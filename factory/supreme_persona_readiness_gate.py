#!/usr/bin/env python3
from __future__ import annotations
import json
import pathlib
import re
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "SHIRMANI-SUPREME-PERSONA-V2.md"
OUT = ROOT / "generated" / "supreme-persona-readiness.json"

REQUIRED_SECTIONS = [
    "## Core presentation qualities",
    "## Reasoning and answer policy",
    "## Voice → Voice System → Content → Photo/Lip-sync → Live Presentation",
    "## Test Q&A requirements",
    "## Safety and dignity gate",
    "## Definition of Supreme Ready",
]
REQUIRED_PHRASES = [
    "अभी पर्याप्त प्रमाण उपलब्ध नहीं है",
    "Authorized voice",
    "Accurate lip-sync",
    "fabricated sources",
    "Supreme Ready",
]

def fail(checks, name, detail):
    checks.append({"name": name, "status": "FAIL", "detail": detail})

def ok(checks, name, detail):
    checks.append({"name": name, "status": "PASS", "detail": detail})

text = CONTRACT.read_text(encoding="utf-8") if CONTRACT.exists() else ""
checks = []

if CONTRACT.exists():
    ok(checks, "contract_exists", str(CONTRACT.relative_to(ROOT)))
else:
    fail(checks, "contract_exists", "Contract file is missing.")

for section in REQUIRED_SECTIONS:
    if section in text:
        ok(checks, f"section:{section}", "present")
    else:
        fail(checks, f"section:{section}", "missing")

for phrase in REQUIRED_PHRASES:
    if phrase in text:
        ok(checks, f"phrase:{phrase}", "present")
    else:
        fail(checks, f"phrase:{phrase}", "missing")

secret_patterns = [
    r"(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"(?i)\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b",
    r"(?i)\bsk-[A-Za-z0-9_-]{20,}\b",
]
for pattern in secret_patterns:
    if re.search(pattern, text):
        fail(checks, "secret_scan", "Possible credential/private key detected.")
        break
else:
    ok(checks, "secret_scan", "No obvious credential/private-key pattern detected.")

payload = {
    "contract_version": "2.0",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "status": "SUPREME_READY" if all(x["status"] == "PASS" for x in checks) else "BLOCKED",
    "checks": checks,
    "capabilities": {
        "persona_contract": True,
        "evidence_first_answers": True,
        "insufficient_evidence_gate": True,
        "authorized_voice_gate": True,
        "photo_lipsync_contract": True,
        "live_presentation_contract": True,
        "continuous_improvement": True,
    },
    "important_boundary": "Automated readiness verifies the repository contract only; it does not independently certify scientific truth, human identity, or real-world voice/face authenticity.",
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, ensure_ascii=False, indent=2))
if payload["status"] != "SUPREME_READY":
    raise SystemExit(1)