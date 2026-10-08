from live.nishpaksh_character_v2 import (
    ABSTENTION,
    EvidenceItem,
    build_presentation_plan,
    scientific_verification_granted,
    understand_question,
)


def main():
    q = understand_question("What does the evidence show?", "evidence")

    no_evidence = build_presentation_plan(q, voice_authorized=True)
    assert no_evidence.status == "ABSTAIN"
    assert no_evidence.answer == ABSTENTION
    assert no_evidence.abstained is True
    assert no_evidence.lip_sync_ready is True
    assert scientific_verification_granted(no_evidence) is False

    supported = q.__class__(
        q.question,
        q.topic,
        (
            EvidenceItem(
                title="verified record",
                source="record-001",
                verified=True,
                excerpt="The measured result is available in the record.",
            ),
        ),
    )
    plan = build_presentation_plan(supported, voice_authorized=True)
    assert plan.status == "READY"
    assert plan.evidence_sources == ("record-001",)
    assert plan.voice_authorized is True
    assert plan.lip_sync_ready is True
    assert scientific_verification_granted(plan) is False

    print("NISHPAKSH_LIVE_CHARACTER_V2_CONTRACT=PASS")


if __name__ == "__main__":
    main()
