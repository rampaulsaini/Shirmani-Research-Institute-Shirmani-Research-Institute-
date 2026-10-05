from agents.multi_layer_automission import LANES, build_cycle, choose_next_action

def test_all_layers_present():
    assert {"practitioner","ml","nlp","evidence","automission","quantum-mechanism"} <= {x.name for x in LANES}

def test_selection_deterministic():
    a=choose_next_action({"evidence":1.0,"nlp":0.5}); b=choose_next_action({"evidence":1.0,"nlp":0.5})
    assert a["winner"]==b["winner"]

def test_fail_closed():
    g=build_cycle()["decision"]["governance"]
    assert g["fail_closed"] and g["independent_verification_required"]
    assert not g["scheduled_code_mutation_allowed"]
    assert not g["automated_verified_promotion_allowed"]

def test_no_quantum_claim():
    d=build_cycle()["decision"]
    assert d["quantum_hardware_used"] is False
    assert d["quantum_advantage_claimed"] is False

def test_cycle_fingerprint_covers_executed_lane():
    from agents.multi_layer_automission import verify_cycle_fingerprint
    cycle = build_cycle({"evidence": 1.0}, executed_lane="evidence")
    assert verify_cycle_fingerprint(cycle) is True
    cycle["executed_lane"] = "nlp"
    assert verify_cycle_fingerprint(cycle) is False


def test_invalid_signal_fails_closed_to_bounded_range():
    for value in (float("nan"), float("inf"), -float("inf")):
        decision = choose_next_action({"ml": value})
        assert 0.0 <= decision["winner"]["score"] <= 1.1
        assert decision["governance"]["fail_closed"] is True


def test_verification_is_result_outcome_review_not_direct_automation():
    d = build_cycle()["decision"]
    g = d["governance"]
    assert g["verification_basis"] == "verified_result_record_only"
    assert g["verification_mode"] == "result_outcome_review_not_direct_automation"
    assert g["automated_verified_promotion_allowed"] is False
