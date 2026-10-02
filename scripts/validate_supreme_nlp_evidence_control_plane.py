"""Contract checks for the unified Supreme NLP evidence control plane."""
from factory.supreme_nlp_evidence_control_plane import run

d=run()
g=d["governance"]
assert g["fail_closed"] and not g["subjective_experience_claim_allowed"]
assert not g["scheduled_code_mutation_allowed"] and g["independent_verification_required"]
assert g["accuracy_is_measured_not_declared"]
assert d["promotion"]["production_promotion_allowed"] is False
assert len(d["quality_gate"]["fingerprint"]) == 64
assert isinstance(d["multimodal"]["limitations"],list)
print("SUPREME_NLP_EVIDENCE_CONTROL_PLANE: PASS")
