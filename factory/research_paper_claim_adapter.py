#!/usr/bin/env python3
"""Bridge Research Paper claims into the canonical claim/evidence pipeline.

This adapter is deterministic and idempotent. It preserves the paper's
UNVERIFIED boundary and creates verification questions; it never creates
evidence or promotes a claim.
"""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
INTAKE = ROOT / "federation" / "research-paper-source-intake.json"
REGISTRY = OUT / "research-paper-claims.json"
TARGET = OUT / "claim-evidence.jsonl"
PREFIX = "srp:"

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:24]

def main():
    intake = json.loads(INTAKE.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if intake["verification_status"] != "UNVERIFIED":
        raise SystemExit("Research Paper intake must remain UNVERIFIED")
    rows = [json.loads(x) for x in TARGET.read_text(encoding="utf-8").splitlines() if x.strip()] if TARGET.exists() else []
    rows = [r for r in rows if not str(r.get("id", "")).startswith(PREFIX)]
    for claim in registry["claims"]:
        cid = PREFIX + claim["id"]
        rows.append({
            "id": cid,
            "claim": claim["claim"],
            "claim_category": claim["category"],
            "artifact_type": "RESEARCH_PAPER",
            "artifact_id": claim["id"],
            "source_traceability": {
                "source_ids": [],
                "repository": intake["repository"],
                "ref": intake["ref"],
                "entrypoint": intake["public_entrypoint"]
            },
            "evidence": [],
            "verification": {
                "status": "UNVERIFIED",
                "independent_verification_required": True,
                "independent_replication": False
            },
            "verification_questions": [
                *claim["evidence_required"],
                "Can an independent reviewer reproduce or evaluate the claim without relying on the author's declaration?"
            ],
            "provenance": "AUTHOR_DECLARED_RESEARCH_PAPER",
            "generator": "factory/research_paper_claim_adapter.py"
        })
    rows.sort(key=lambda r: str(r["id"]))
    TARGET.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in rows) + "\n",
        encoding="utf-8"
    )
    print(json.dumps({
        "source": intake["repository"],
        "adapted_claims": len(registry["claims"]),
        "claim_evidence_total": len(rows),
        "verification_status": "UNVERIFIED",
        "promotion": False,
        "fingerprint": digest(json.dumps(registry, ensure_ascii=False, sort_keys=True))
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
