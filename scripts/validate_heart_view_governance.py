import json
from pathlib import Path
from agents.claim_guard import govern_source, attach_evidence, independently_verify, can_publish_as_verified

policy=json.loads(Path("automation/supreme-nlp-policy.json").read_text(encoding="utf-8"))
profile=json.loads(Path("automation/heart-view-source-profile.json").read_text(encoding="utf-8"))

assert policy["verification"]["fail_closed"] is True
assert policy["verification"]["independent_verifier_must_differ_from_generator"] is True
assert profile["status"] == "USER_AUTHORED_SOURCE"
assert profile["preservation"]["do_not_promote_to_scientific_fact"] is True

c=govern_source("source proposition", "source/user-directives/example.md", "generator")
assert c.kind == "SOURCE"
c=attach_evidence(c, ["e1"], ["counter1"])
assert c.kind == "EVIDENCE_SUPPORTED"
assert can_publish_as_verified(c) is False
c=independently_verify(c, "independent-verifier")
assert can_publish_as_verified(c) is True

try:
    independently_verify(
        govern_source("x", "source", "same-agent"),
        "same-agent",
    )
except ValueError:
    pass
else:
    raise AssertionError("Self-verification must fail closed")

print("HEART_VIEW_GOVERNANCE_OK")
