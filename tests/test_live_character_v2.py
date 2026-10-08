from voice.live_character_v2 import (
    INSUFFICIENT_EVIDENCE,
    build_answer,
    run_live_turn,
)


class Retriever:
    def __init__(self, evidence):
        self.evidence = evidence
    def retrieve(self, question, context):
        return self.evidence


class Voice:
    def __init__(self):
        self.spoken = []
    def speak(self, text):
        self.spoken.append(text)
        return {"audio": text}


class Presenter:
    def __init__(self):
        self.presented = []
    def present(self, audio, *, text):
        self.presented.append((audio, text))
        return {"presented": text}


def main():
    no_evidence = build_answer("क्या इसका वैज्ञानिक प्रमाण है?", context={}, evidence=[])
    assert no_evidence.text == INSUFFICIENT_EVIDENCE
    assert no_evidence.evidence_status == "INSUFFICIENT_EVIDENCE"

    philosophical = build_answer(
        "मैं कौन हूं?",
        context={},
        evidence=[],
    )
    assert philosophical.evidence_status == "PHILOSOPHICAL_OR_IDENTITY"
    assert "स्वतंत्र वैज्ञानिक सत्यापन" in philosophical.text

    supported = build_answer(
        "इसका evidence क्या है?",
        context={},
        evidence=[{"source": "test-paper", "verification_status": "VERIFIED"}],
    )
    assert supported.evidence_status == "SUPPORTED"
    assert supported.sources[0]["source"] == "test-paper"

    voice = Voice()
    presenter = Presenter()
    result = run_live_turn(
        "क्या इसका वैज्ञानिक प्रमाण है?",
        context={"session": "test"},
        retriever=Retriever([]),
        voice=voice,
        presenter=presenter,
    )
    assert result["presented"] == INSUFFICIENT_EVIDENCE
    assert voice.spoken == [INSUFFICIENT_EVIDENCE]
    assert presenter.presented[0][1] == INSUFFICIENT_EVIDENCE

    print("VOICE_LIVE_CHARACTER_V2_CONTRACT=PASS")


if __name__ == "__main__":
    main()
