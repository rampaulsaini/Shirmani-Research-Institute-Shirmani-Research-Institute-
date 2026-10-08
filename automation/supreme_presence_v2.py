"""Deterministic, provider-neutral SHIRMANI Supreme Presence v2 contract tests.
No voice provider is called here. Real voice/avatar execution requires explicit authorized credentials.
"""
from __future__ import annotations
import json, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "automation" / "supreme_presence_v2.json"
OUT = ROOT / "generated" / "supreme-presence-v2"
INSUFFICIENT = "अभी पर्याप्त प्रमाण उपलब्ध नहीं है"

def load():
    return json.loads(SPEC.read_text(encoding="utf-8"))

def stable_id(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]

def test_contract(spec):
    required = {
        "voice": "voice",
        "authorized_voice_integration": "authorized_voice_integration",
        "test_qna": "test_qna",
        "content": "content",
        "photo_or_avatar": "photo_or_avatar",
        "lip_sync": "lip_sync",
        "timing_coherence": "timing_coherence",
        "live_presentation": "live_presentation",
        "quality_gate": "quality_gate",
        "independent_verification": "independent_verification",
    }
    pipe = spec["presentation_pipeline"]
    assert pipe == list(required.values()), "presentation pipeline contract changed"
    assert spec["voice_system"]["mode"] == "authorized_voice_only"
    assert spec["voice_system"]["fallback"] == "text_only"
    assert spec["response_policy"]["insufficient_evidence_phrase"] == INSUFFICIENT
    return True

def build_test_qna():
    return [
        {
            "id": stable_id("identity"),
            "question": "आपका presentation principle क्या है?",
            "answer_type": "philosophical_identity",
            "answer": "सरल, सहज, निर्मल, पारदर्शी, स्पष्ट और प्रत्यक्ष संवाद; पहचान को तथ्यात्मक वैज्ञानिक प्रमाण के रूप में प्रस्तुत नहीं किया जाता।",
            "verification": "NOT_APPLICABLE_IDENTITY"
        },
        {
            "id": stable_id("evidence"),
            "question": "यदि किसी तथ्य के पर्याप्त प्रमाण न हों तो?",
            "answer_type": "evidence_policy",
            "answer": INSUFFICIENT,
            "verification": "POLICY_VERIFIED"
        }
    ]

def main():
    spec = load()
    test_contract(spec)
    OUT.mkdir(parents=True, exist_ok=True)
    qna = build_test_qna()
    status = {
        "version": spec["version"],
        "contract_test": "PASS",
        "authorized_voice_ready": False,
        "reason": "Provider credentials and an authorized voice ID are not embedded in source control.",
        "text_qna_ready": True,
        "lip_sync_contract_ready": True,
        "live_presentation_contract_ready": True,
        "independent_verification": "PENDING",
        "insufficient_evidence_phrase": INSUFFICIENT,
        "qna_count": len(qna)
    }
    (OUT / "test-qna.json").write_text(json.dumps(qna, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))

if __name__ == "__main__":
    main()
