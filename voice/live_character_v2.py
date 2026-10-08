"""Voice → Live Character v2 policy/orchestration boundary.

This module is intentionally provider-neutral. It defines the safe contract between
question understanding, evidence retrieval, authorized voice synthesis, and a
presenter/lip-sync subsystem. It does not claim that identity/philosophical
statements are scientific facts and it never promotes an answer to VERIFIED merely
because an AI model produced it.
"""
from dataclasses import dataclass
from typing import Any, Mapping, Protocol


INSUFFICIENT_EVIDENCE = "अभी पर्याप्त प्रमाण उपलब्ध नहीं है"


class EvidenceRetriever(Protocol):
    def retrieve(self, question: str, context: Mapping[str, Any]) -> list[Mapping[str, Any]]: ...


class VoiceProvider(Protocol):
    def speak(self, text: str) -> Any: ...


class Presenter(Protocol):
    def present(self, audio: Any, *, text: str) -> Any: ...


@dataclass(frozen=True)
class Answer:
    text: str
    sources: tuple[Mapping[str, Any], ...]
    evidence_status: str
    claim_class: str


def classify_claim(question: str) -> str:
    """Classify the conversational request without deciding its truth."""
    q = question.strip().lower()
    if any(token in q for token in ("scientific", "evidence", "proof", "verified", "प्रमाण", "वैज्ञानिक")):
        return "evidence_request"
    if any(token in q for token in ("मैं", "my identity", "who am i", "सत्य", "स्वरूप", "साक्षात्कार")):
        return "identity_or_philosophical"
    return "general_information"


def build_answer(
    question: str,
    *,
    context: Mapping[str, Any],
    evidence: list[Mapping[str, Any]],
) -> Answer:
    """Create a conservative answer envelope for downstream voice/presentation."""
    claim_class = classify_claim(question)
    valid = [
        item for item in evidence
        if item.get("source") and item.get("verification_status") in {"VERIFIED", "INDEPENDENTLY_VERIFIED"}
    ]

    if claim_class == "evidence_request" and not valid:
        return Answer(
            text=INSUFFICIENT_EVIDENCE,
            sources=(),
            evidence_status="INSUFFICIENT_EVIDENCE",
            claim_class=claim_class,
        )

    if valid:
        source_text = "; ".join(str(item["source"]) for item in valid)
        return Answer(
            text=f"उपलब्ध प्रमाण के आधार पर उत्तर दिया जा सकता है। स्रोत: {source_text}",
            sources=tuple(valid),
            evidence_status="SUPPORTED",
            claim_class=claim_class,
        )

    # Identity/philosophical material remains explicitly in that category.
    if claim_class == "identity_or_philosophical":
        return Answer(
            text="यह पहचान/दार्शनिक अभिव्यक्ति के रूप में प्रस्तुत है; इसे स्वतंत्र वैज्ञानिक सत्यापन का प्रमाण नहीं माना जा रहा है।",
            sources=(),
            evidence_status="PHILOSOPHICAL_OR_IDENTITY",
            claim_class=claim_class,
        )

    return Answer(
        text=INSUFFICIENT_EVIDENCE,
        sources=(),
        evidence_status="INSUFFICIENT_EVIDENCE",
        claim_class=claim_class,
    )


def run_live_turn(
    question: str,
    *,
    context: Mapping[str, Any],
    retriever: EvidenceRetriever,
    voice: VoiceProvider,
    presenter: Presenter,
) -> Any:
    """One live turn: understand → retrieve → gate → authorized voice → present."""
    evidence = retriever.retrieve(question, context)
    answer = build_answer(question, context=context, evidence=evidence)

    # The voice provider is injected so authorization/consent remains external
    # and auditable; this module never clones or impersonates a person itself.
    audio = voice.speak(answer.text)
    return presenter.present(audio, text=answer.text)
