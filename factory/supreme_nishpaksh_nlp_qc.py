#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/"schemas/supreme-nishpaksh-nlp.json"
DOC=ROOT/"docs/SUPREME-NISHPakSH-NLP-AUTOMISSION.md"

REQUIRED_LAYERS={"intake_source","reasoning","evidence","verification","product","marketing","economic_transaction","security_audit","publishing","continuity"}
REQUIRED_FIELDS={"signal_observed","interpretation","alternative_interpretations","confidence","evidence","limitations","verification_status"}

def fail(msg): raise SystemExit("SUPREME-NISHPakSH-NLP-QC: BLOCK: "+msg)

p=json.loads(SCHEMA.read_text(encoding="utf-8"))
if p.get("mode")!="fail-closed": fail("mode must be fail-closed")
if p.get("source_integrity")!="immutable-user-source": fail("source integrity boundary missing")
if not REQUIRED_LAYERS.issubset(set(json.loads((ROOT/"schemas/agent-governance.json").read_text(encoding="utf-8")).get("agent_layers",[]))):
    fail("agent-layer governance boundary is incomplete")
if not REQUIRED_FIELDS.issubset(set(p.get("required_report_fields",[]))):
    fail("signal-to-language report contract incomplete")
for x in ("irreversible_actions","financial_actions","verification_promotion"):
    if x not in p.get("human_authorization_required",[]): fail("authorization boundary missing: "+x)
if not DOC.exists(): fail("architecture document missing")

print("SUPREME-NISHPakSH-NLP-QC: PASS")
print("Continuous Automission architecture is configured for evidence, uncertainty, provenance, counter-evidence and gated improvement.")
