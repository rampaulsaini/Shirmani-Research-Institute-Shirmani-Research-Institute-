from presentation.nishpaksh_presenter import (
    EvidenceItem,
    PresenterPolicy,
    INSUFFICIENT_EVIDENCE,
    build_answer_policy,
    build_live_presentation_plan,
    render_answer,
)


def main():
    base = PresenterPolicy(
        authorized_voice=True,
        authorized_visual_identity=True,
        evidence_available=True,
        evidence_independently_verified=True,
    )

    verified = [EvidenceItem("Study", "source://study", independently_verified=True)]
    plan = build_live_presentation_plan("वैज्ञानिक प्रमाण क्या है?", verified, base)
    assert plan["runtime_status"] == "READY_FOR_PROVIDER"
    assert plan["answer"]["answer_mode"] == "ANSWER_WITH_SOURCES"
    assert plan["audit"]["scientific_verification_granted"] is False
    assert plan["pipeline"][-1] == "AUDIT_RECORD"

    no_evidence = build_answer_policy("क्या यह वैज्ञानिक रूप से सिद्ध है?", [], base)
    assert no_evidence["answer_mode"] == "ABSTAIN_INSUFFICIENT_EVIDENCE"
    assert no_evidence["abstention_text"] == INSUFFICIENT_EVIDENCE

    unverified = build_answer_policy(
        "इस दावे का प्रमाण क्या है?",
        [EvidenceItem("Author statement", "source://author", independently_verified=False)],
        base,
    )
    assert unverified["answer_mode"] == "ANSWER_WITH_UNVERIFIED_LABEL"
    assert unverified["verification_status"] == "UNVERIFIED"

    identity = build_answer_policy(
        "मैं कौन हूं?",
        [],
        base,
    )
    assert identity["answer_mode"] == "ATTRIBUTE_AS_IDENTITY_OR_AUTHOR_CLAIM"

    blocked = build_live_presentation_plan(
        "प्रश्न",
        verified,
        PresenterPolicy(
            authorized_voice=False,
            authorized_visual_identity=True,
            evidence_available=True,
            evidence_independently_verified=True,
        ),
    )
    assert blocked["runtime_status"] == "BLOCKED_AUTHORIZATION"

    rendered = render_answer(
        unverified,
        "प्रारंभिक व्याख्या उपलब्ध है।",
        [EvidenceItem("Author statement", "source://author")],
    )
    assert "UNVERIFIED" in rendered
    assert "स्वतंत्र सत्यापन" in rendered

    print("NISHPAKSH_PRESENTER_CONTRACT=PASS")


if __name__ == "__main__":
    main()
