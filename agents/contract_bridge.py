"""Deterministic bridge from legacy orchestrator rows to Research Factory contracts.

This module does not infer truth. It only normalizes traceability fields and assigns
conservative statuses when independent evidence is absent.
"""
import hashlib
from datetime import datetime, timezone

CLAIM_TYPES={"FACT","INTERPRETATION","HYPOTHESIS","PHILOSOPHICAL_PROPOSITION","MATHEMATICAL","COMPUTATIONAL","HISTORICAL","SCIENTIFIC","COMPARATIVE"}

def _hash(text):
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()

def source_record(row, recorded_at=None):
    text=row.get("text","")
    source=str(row.get("source") or row.get("repository") or "unknown")
    return {
        "id":"source-"+_hash(source+"|"+str(row.get("id"))+"|"+text)[:20],
        "source_type":"REPOSITORY" if "/" in source else "OTHER",
        "title":source,
        "language":row.get("language",""),
        "locator":source,
        "content_hash":_hash(text),
        "availability":"AVAILABLE" if source!="unknown" else "UNAVAILABLE",
        "provenance":{
            "recorded_at":recorded_at or datetime.now(timezone.utc).isoformat(),
            "repository":row.get("repository",source),
            "path":row.get("path",""),
            "commit":row.get("commit","")
        }
    }

def concept_records(row):
    return [{
        "id":"concept-"+_hash(str(topic))[:20],
        "label":str(topic),
        "aliases":[],
        "definition":"",
        "status":"DRAFT",
        "relations":[],
        "source_refs":[str(row.get("id"))]
    } for topic in row.get("topics",["general"])]

def claim_record(row, verification_status="UNVERIFIED", source_ref="unknown"):
    text=row.get("text","").strip()
    claim_type=row.get("claim_type","PHILOSOPHICAL_PROPOSITION")
    if claim_type not in CLAIM_TYPES:
        claim_type="PHILOSOPHICAL_PROPOSITION"
    return {
        "id":"claim-"+_hash(str(row.get("id"))+"|"+text)[:20],
        "claim":text,
        "claim_type":claim_type,
        "status":"DRAFT",
        "definitions":[],
        "evidence":[{
            "type":"PRIMARY_SOURCE",
            "description":"Traceable source text supplied to the orchestrator; source presence is not independent proof.",
            "source":source_ref
        }],
        "formulation":[{
            "method":"SOURCE_NORMALIZATION",
            "result":"Normalized for structured research processing; no truth inference performed.",
            "reproducible":True
        }],
        "verification":{
            "status":verification_status,
            "method":"Deterministic provenance check only; independent verification not performed.",
            "checked_by":"research-factory-contract-bridge"
        },
        "countercases":[],
        "provenance":{
            "recorded_at":datetime.now(timezone.utc).isoformat(),
            "repository":row.get("repository",source_ref),
            "path":row.get("path",""),
            "commit":row.get("commit",""),
            "content_hash":_hash(text)
        }
    }

def verification_report(claim, verification_status="NOT_VERIFIED"):
    rid=claim["id"]
    return {
        "record_id":rid,
        "verification_status":verification_status,
        "checks":[{
            "name":"source_trace",
            "status":"PASS" if claim["provenance"].get("repository") else "NOT_VERIFIED",
            "details":"A provenance locator is present; this does not establish external truth."
        },{
            "name":"independent_evidence",
            "status":"NOT_VERIFIED",
            "details":"No independent evidence was supplied by this deterministic bridge."
        }],
        "limitations":["No scientific, historical, medical, mathematical, or empirical proof is inferred."],
        "generated_at":datetime.now(timezone.utc).isoformat()
    }
