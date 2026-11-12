from shirmani_supreme_nlp.result_contract import AgentResult


def test_valid_result_contract():
    r = AgentResult(
        task_id="demo-1",
        source_type="measurement",
        claim="A measurable signal pattern was detected.",
        confidence=0.92,
        plain_language="A signal pattern was detected; its interpretation is provisional.",
    )
    r.validate()


def test_invalid_confidence_is_rejected():
    r = AgentResult(task_id="x", source_type="measurement", claim="x", confidence=1.2)
    try:
        r.validate()
    except ValueError:
        return
    raise AssertionError("invalid confidence was accepted")
