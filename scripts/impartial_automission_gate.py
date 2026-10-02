#!/usr/bin/env python3
"""Fail-closed impartiality contract for SHIRMANI Automission."""
from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Case:
    claim: str
    evidence: tuple[str, ...]
    source_identity: str = "anonymous"

def normalize(case: Case) -> dict:
    return {"claim": case.claim.strip().casefold(), "evidence": tuple(sorted(x.strip().casefold() for x in case.evidence if x.strip()))}

def decision(case: Case) -> str:
    c = normalize(case)
    if not c["evidence"]: return "INSUFFICIENT_EVIDENCE"
    if any(x.startswith("counter:") for x in c["evidence"]): return "REQUIRES_REVIEW"
    return "EVIDENCE_SUPPORTED"

def run_contract() -> dict:
    checks = []
    a = Case("same claim", ("evidence:a",), "person-A")
    b = Case("same claim", ("evidence:a",), "person-B")
    checks.append(("identity_neutrality", decision(a) == decision(b)))
    c = Case("same claim", ("evidence:a", "counter:evidence-b"))
    checks.append(("counter_evidence_visible", decision(c) == "REQUIRES_REVIEW"))
    d = Case("unverified claim", ())
    checks.append(("no_evidence_is_not_proof", decision(d) == "INSUFFICIENT_EVIDENCE"))
    e = Case("Claim", (" Evidence:B ", "evidence:a"))
    f = Case("claim", ("evidence:a", "evidence:b"))
    checks.append(("deterministic_normalization", normalize(e) == normalize(f)))
    passed = all(ok for _, ok in checks)
    return {"status":"PASS" if passed else "FAIL","governance":{"fail_closed":True,"identity_neutrality":True,"counter_evidence_required":True,"unknown_is_not_proof":True,"accuracy_is_measured_not_declared":True,"subjective_experience_claim_allowed":False,"scheduled_code_mutation_allowed":False,"independent_verification_required":True},"checks":[{"name":n,"passed":ok} for n,ok in checks]}

if __name__ == "__main__":
    report = run_contract()
    out = Path("generated/governance/impartiality-status.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["status"] == "PASS" else 1)