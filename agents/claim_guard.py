"""Claim governance guard for Heart-View / Yatharth-Yug source material.

The user's framework is preserved as source material. This guard prevents the
language layer from silently upgrading a source statement into a verified fact.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Literal
import hashlib, json

Kind = Literal["SOURCE", "OBSERVATION", "HYPOTHESIS", "EVIDENCE_SUPPORTED",
               "INDEPENDENTLY_VERIFIED", "REJECTED"]

@dataclass(frozen=True)
class GovernedClaim:
    claim_id: str
    text: str
    kind: Kind
    source_ref: str
    evidence_refs: tuple[str, ...] = ()
    counter_evidence_refs: tuple[str, ...] = ()
    generator: str = ""
    verifier: str = ""

def claim_id(text: str, source_ref: str) -> str:
    return hashlib.sha256(f"{source_ref}\n{text}".encode("utf-8")).hexdigest()[:24]

def can_publish_as_verified(c: GovernedClaim) -> bool:
    return (
        c.kind == "INDEPENDENTLY_VERIFIED"
        and bool(c.evidence_refs)
        and bool(c.verifier)
        and c.verifier != c.generator
    )

def govern_source(text: str, source_ref: str, generator: str) -> GovernedClaim:
    return GovernedClaim(
        claim_id=claim_id(text, source_ref),
        text=text,
        kind="SOURCE",
        source_ref=source_ref,
        generator=generator,
    )

def attach_evidence(c: GovernedClaim, evidence_refs: list[str],
                    counter_evidence_refs: list[str] | None = None) -> GovernedClaim:
    if c.kind == "REJECTED":
        raise ValueError("Rejected claims cannot be promoted by this function.")
    return GovernedClaim(
        **{**asdict(c),
           "kind": "EVIDENCE_SUPPORTED",
           "evidence_refs": tuple(evidence_refs),
           "counter_evidence_refs": tuple(counter_evidence_refs or [])}
    )

def independently_verify(c: GovernedClaim, verifier: str) -> GovernedClaim:
    if c.kind != "EVIDENCE_SUPPORTED":
        raise ValueError("Only evidence-supported claims may enter independent verification.")
    if not c.evidence_refs:
        raise ValueError("Evidence is required.")
    if not verifier or verifier == c.generator:
        raise ValueError("Independent verifier must be distinct from generator.")
    return GovernedClaim(
        **{**asdict(c), "kind": "INDEPENDENTLY_VERIFIED", "verifier": verifier}
    )

def to_machine_record(c: GovernedClaim) -> dict:
    d = asdict(c)
    d["publishable_as_verified"] = can_publish_as_verified(c)
    return d

if __name__ == "__main__":
    c = govern_source(
        "Heart-View / Yatharth-Yug user-authored proposition",
        "source/user-directives/2026-09-20-shirmani-heart-view-request.md",
        "source-intake",
    )
    c = attach_evidence(c, ["example-evidence"], ["example-counter-evidence"])
    c = independently_verify(c, "independent-verifier")
    print(json.dumps(to_machine_record(c), ensure_ascii=False, indent=2))
