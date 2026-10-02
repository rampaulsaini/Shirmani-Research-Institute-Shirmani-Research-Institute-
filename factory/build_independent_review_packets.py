#!/usr/bin/env python3
"""Build deterministic independent-review packets without declaring verification.

The packet separates:
- evidence already present,
- what an independent reviewer must test,
- counter-evidence requirements,
- explicit reviewer decision fields.

It never changes a claim to VERIFIED.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "generated/independent-verification-records.json"
OUT = ROOT / "generated/independent-review-packets.json"

TEST_PLANS = {
    "IV-001": {
        "operational_definition": "A claim passes only if authoritative astronomical sources independently document stellar life-cycle change and galaxy evolution over time.",
        "test": "Triangulate at least two authoritative sources; record the exact passages supporting stellar change and galaxy evolution; check whether any source materially contradicts the claim.",
        "reproduction": "Reviewer independently opens the cited NASA sources, records source version/access date, and reproduces the evidence mapping.",
        "counterevidence": "Search for authoritative evidence that would limit, qualify, or contradict the general evolution claim; preserve negative findings as well.",
    },
    "IV-002": {
        "operational_definition": "A claim passes only if authoritative observations document galaxy collisions/mergers and measurable structural change associated with them.",
        "test": "Independently inspect NASA/Hubble material for documented collisions, mergers, deformation, star-formation effects, or resulting structures.",
        "reproduction": "Reviewer independently maps each cited source to one or more observable features and records the source access/version metadata.",
        "counterevidence": "Check whether the wording overstates collision frequency, mechanism, certainty, or timescale; record any qualification.",
    },
    "IV-003": {
        "operational_definition": "A claim passes only if a major scientific assessment documents measurable links between human activity and climate, ecosystems, or biodiversity.",
        "test": "Independently inspect the IPCC assessment and identify the specific assessed findings supporting human influence and effects on natural systems.",
        "reproduction": "Reviewer records report version, chapter/section/page references and reproduces the evidence-to-claim mapping.",
        "counterevidence": "Record uncertainties, attribution limits, regional variation, alternative explanations, and confidence levels stated by the assessment.",
    },
    "IV-004": {
        "operational_definition": "The claim is limited to whether first-person self-knowledge and prereflective self-consciousness are established subjects of philosophical analysis, not whether a particular theory is scientifically proven.",
        "test": "Independently inspect multiple scholarly reference sources and determine whether they explicitly discuss self-knowledge and prereflective self-consciousness as philosophical objects of analysis.",
        "reproduction": "Reviewer records the exact source entries and verifies that the claim does not silently exceed their scope.",
        "counterevidence": "Record competing philosophical accounts and disagreements about the nature, epistemic status, or scope of self-knowledge/self-consciousness.",
    },
}

def sha256_obj(obj):
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    packets = []
    for record in data.get("records", []):
        rid = record["id"]
        plan = TEST_PLANS.get(rid)
        packet = {
            "packet_version": "1.0.0",
            "claim_id": rid,
            "claim": record["claim"],
            "source_status": record.get("source_status", record.get("status")),
            "source_evidence": record.get("evidence", {}),
            "readiness": "REVIEW_READY" if plan else "NEEDS_OPERATIONALIZATION",
            "independence": {
                "author_material_is_not_independent": True,
                "automated_workflow_success_is_not_verification": True,
                "external_reviewer_required": True,
            },
            "review_plan": plan or {
                "operational_definition": "",
                "test": "Define a falsifiable/observable test before review.",
                "reproduction": "Define reproducible inputs, environment, procedure and expected output.",
                "counterevidence": "Identify credible counter-evidence and record it before any decision.",
            },
            "reviewer_decision_template": {
                "reviewer_identity": "",
                "reviewer_role": "",
                "reviewed_at": "",
                "decision": "PENDING",
                "reasoning_summary": "",
                "evidence_references": [],
                "counterevidence_references": [],
                "reproduction_artifacts": [],
            },
        }
        packet["packet_sha256"] = sha256_obj(packet)
        packets.append(packet)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "queue_records": len(packets),
        "review_ready_records": sum(p["readiness"] == "REVIEW_READY" for p in packets),
        "needs_operationalization_records": sum(p["readiness"] == "NEEDS_OPERATIONALIZATION" for p in packets),
        "verified_records": 0,
        "fail_closed": True,
        "packets": packets,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "queue_records": len(packets),
        "review_ready": report["review_ready_records"],
        "needs_operationalization": report["needs_operationalization_records"],
        "verified": 0,
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
