"""Deterministic claim/evidence protocol.

This module does not prove arbitrary claims. It creates an auditable
structure in which a claim can be defined, formulated, compared and
assigned a conservative status.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any
import hashlib

VALID_TYPES={"empirical","mathematical","historical","textual","philosophical","computational"}
VALID_STATUSES={"supported","contradicted","unresolved","hypothesis","not_testable"}

@dataclass
class ClaimAssessment:
    claim:str
    claim_type:str="philosophical"
    definitions:list[str]|None=None
    formulation:dict[str,list[str]]|None=None
    evidence:list[dict[str,Any]]|None=None
    computation:list[dict[str,Any]]|None=None
    comparison:list[dict[str,Any]]|None=None
    status:str="unresolved"
    reason:str="No independent verification supplied."
    limitations:list[str]|None=None
    provenance:list[str]|None=None
    def to_dict(self)->dict[str,Any]:
        return asdict(self)

def claim_id(claim:str)->str:
    return "claim-"+hashlib.sha256(claim.strip().encode("utf-8")).hexdigest()[:20]

def assess(claim:str, *, claim_type:str="philosophical",
           definitions:list[str]|None=None,
           formulation:dict[str,list[str]]|None=None,
           evidence:list[dict[str,Any]]|None=None,
           computation:list[dict[str,Any]]|None=None,
           comparison:list[dict[str,Any]]|None=None,
           status:str="unresolved",
           reason:str="No independent verification supplied.",
           limitations:list[str]|None=None,
           provenance:list[str]|None=None)->dict[str,Any]:
    if claim_type not in VALID_TYPES: raise ValueError(f"Unsupported claim_type: {claim_type}")
    if status not in VALID_STATUSES: raise ValueError(f"Unsupported status: {status}")
    if not claim.strip(): raise ValueError("claim must not be empty")
    result=ClaimAssessment(claim=claim.strip(),claim_type=claim_type,
        definitions=definitions or [],
        formulation=formulation or {"logic":[],"equations":[],"algorithm":[]},
        evidence=evidence or [],computation=computation or [],comparison=comparison or [],
        status=status,reason=reason,limitations=limitations or [],provenance=provenance or []).to_dict()
    result["claim_id"]=claim_id(claim)
    return result

def conservative_status(*, independent_evidence:bool, reproducible_test:bool,
                        contradiction:bool=False)->str:
    """Absence of evidence never becomes proof."""
    if contradiction: return "contradicted"
    if independent_evidence and reproducible_test: return "supported"
    return "unresolved"
