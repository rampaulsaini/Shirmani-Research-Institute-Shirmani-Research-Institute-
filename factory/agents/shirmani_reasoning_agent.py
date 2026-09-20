#!/usr/bin/env python3
"""Deterministic epistemic reasoning layer for the Shirmani Research Institute.

This agent does not prove claims. It records classification, evidence needs,
provenance and independent-review requirements using the institute framework.
"""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_PATH = ROOT / "factory" / "shirmani-framework.json"

def load_framework():
    return json.loads(FRAMEWORK_PATH.read_text(encoding="utf-8"))

def classify(claim, policy):
    """Classify using framework vocabulary while preserving a safe fallback."""
    c = claim.lower()
    classes = set(policy.get("claim_classes", []))
    if policy.get("epistemic_safety", {}).get("philosophical_claims_must_be_labeled", True) and any(
        x in c for x in ("यथार्थ युग", "शिरोमणि", "निष्पक्ष समझ", "हृदय दृष्टिकोण", "संपूर्ण संतुष्टि")
    ) and "user_philosophy" in classes:
        return "user_philosophy"
    if any(x in c for x in ("प्रमाण", "सिद्ध", "वैज्ञानिक", "empirical", "science")) and "unverified_claim" in classes:
        return "unverified_claim"
    if "creative_expression" in classes:
        return "creative_expression"
    return next(iter(sorted(classes)), "unverified_claim")

def reason(claim, source_ids=None):
    policy = load_framework()
    claim_class = classify(claim, policy)
    return {
        "id": "reason-" + hashlib.sha256(claim.encode("utf-8")).hexdigest()[:16],
        "claim": claim,
        "claim_class": claim_class,
        "framework_id": policy["framework_id"],
        "source_ids": [str(x) for x in (source_ids or [])],
        "method_trace": list(policy.get("method_stack", [])),
        "verification_questions": [
            "क्या दावा स्पष्ट रूप से परिभाषित और परीक्षण योग्य है?",
            "क्या प्राथमिक/विश्वसनीय स्रोत उपलब्ध हैं?",
            "क्या विरोधी साक्ष्य या वैकल्पिक व्याख्याएँ दर्ज की गई हैं?",
            "क्या गणना/कोड/प्रयोग पुनरुत्पादित किया जा सकता है?"
        ],
        "evidence_status": "requires_independent_verification",
        "human_review_required": True,
        "unsupported_claim_action": "label_or_abstain",
        "note": "स्रोत-ट्रेस स्वयं स्वतंत्र प्रमाण नहीं है; user philosophy को वैज्ञानिक तथ्य के रूप में स्वतः परिवर्तित नहीं किया जाता।"
    }
