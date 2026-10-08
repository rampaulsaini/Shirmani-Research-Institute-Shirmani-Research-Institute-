"""Fail-closed live presentation controller for the Nishpaksh character.

This module orchestrates question understanding, evidence gating, bounded
answering, authorized voice, and presentation timing. It deliberately does
not claim scientific verification, consciousness, or identity equivalence.
Provider-specific voice/avatar/lip-sync adapters can be attached later.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class EvidenceItem:
    title: str
    source: str
    verified: bool
    excerpt: str = ""


@dataclass(frozen=True)
class QuestionContext:
    question: str
    topic: str = ""
    evidence: tuple[EvidenceItem, ...] = ()


@dataclass(frozen=True)
class PresentationPlan:
    answer: str
    evidence_sources: tuple[str, ...]
    voice_authorized: bool
    lip_sync_ready: bool
    gaze_mode: str
    facial_expression_mode: str
    status: str
    abstained: bool


ABSTENTION = "अभी पर्याप्त प्रमाण उपलब्ध नहीं है。"


def understand_question(question: str, topic: str = "") -> QuestionContext:
    text = " ".join(str(question or "").split())
    if not text:
        raise ValueError("question must not be empty")
    return QuestionContext(question=text, topic=" ".join(str(topic or "").split()))


def evidence_gate(
    context: QuestionContext,
    retriever: Callable[[QuestionContext], Iterable[EvidenceItem]] | None = None,
) -> QuestionContext:
    if retriever is None:
        return context
    items = tuple(x for x in retriever(context) if isinstance(x, EvidenceItem))
    return QuestionContext(context.question, context.topic, items)


def bounded_answer(context: QuestionContext) -> tuple[str, tuple[str, ...], bool]:
    """Return only source-backed content; abstain when evidence is insufficient."""
    verified = tuple(item for item in context.evidence if item.verified and item.source.strip())
    if not verified:
        return ABSTENTION, (), True

    sources = tuple(dict.fromkeys(item.source.strip() for item in verified))
    excerpts = tuple(item.excerpt.strip() for item in verified if item.excerpt.strip())
    if not excerpts:
        return ABSTENTION, sources, True

    answer = " ".join(excerpts)
    return answer, sources, False


def build_presentation_plan(
    context: QuestionContext,
    *,
    voice_authorized: bool,
    answer: str | None = None,
) -> PresentationPlan:
    if answer is None:
        generated, sources, abstained = bounded_answer(context)
    else:
        generated = " ".join(str(answer).split())
        sources = tuple(
            dict.fromkeys(
                item.source.strip()
                for item in context.evidence
                if item.verified and item.source.strip()
            )
        )
        abstained = not bool(generated) or not bool(sources)
        if abstained:
            generated = ABSTENTION
            sources = ()

    ready = bool(voice_authorized and generated)
    return PresentationPlan(
        answer=generated,
        evidence_sources=sources,
        voice_authorized=bool(voice_authorized),
        lip_sync_ready=ready,
        gaze_mode="natural-eye-contact",
        facial_expression_mode="natural-bounded",
        status="ABSTAIN" if abstained else "READY",
        abstained=abstained,
    )


def identity_statement_is_philosophical(statement: str) -> bool:
    """Keep identity/philosophical declarations outside scientific evidence."""
    return bool(str(statement or "").strip())


def scientific_verification_granted(plan: PresentationPlan) -> bool:
    """Presentation readiness can never grant scientific verification."""
    return False
