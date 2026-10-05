from agents.multi_layer_automission import (
    LANES,
    build_cycle,
    build_result_outcome,
    choose_next_action,
    review_result_outcome,
)

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

def test_invalid_control_signal_is_reported_and_blocks_execution():
    decision = choose_next_action({"ml": float("nan"), "nlp": "not-a-number"})
    assert decision["control_input_valid"] is False
    assert decision["invalid_control_signals"] == ["ml", "nlp"]
    assert decision["governance"]["orchestration_execution_allowed"] is False

def test_valid_control_signals_allow_orchestration():
    decision = choose_next_action({"ml": 0.5, "nlp": 1.0})
    assert decision["control_input_valid"] is True
    assert decision["invalid_control_signals"] == []
    assert decision["governance"]["orchestration_execution_allowed"] is True

def test_result_outcome_review_is_distinct_from_verification():
    expected = {"status": "PASS", "score": 0.91, "test_count": 12}
    observed = {"status": "PASS", "score": 0.91, "test_count": 12}
    review = review_result_outcome(expected, observed)
    assert review["status"] == "RESULT_OUTCOME_MATCH"
    assert review["matched"] is True
    assert review["verification_status"] == "RESULT_OUTCOME_CHECKED"
    assert review["independent_verification_established"] is False
    assert review["scientific_truth_established"] is False

def test_result_outcome_mismatch_is_explicit():
    review = review_result_outcome({"status": "PASS"}, {"status": "FAIL"})
    assert review["status"] == "RESULT_OUTCOME_MISMATCH"
    assert review["matched"] is False
    assert review["independent_verification_established"] is False

def test_result_outcome_rejects_non_mapping_inputs():
    try:
        review_result_outcome({"status": "PASS"}, ["PASS"])
    except ValueError:
        pass
    else:
        raise AssertionError("result outcome review must reject non-mapping inputs")

def test_actual_lane_result_record_is_explicit():
    record = build_result_outcome("ml", "tests/test_supreme_ai_ml_nlp.py", "pytest", 0)
    assert record["status"] == "PASS"
    assert record["exit_code"] == 0
    assert record["verification_status"] == "RESULT_OUTCOME_CHECKED"
    assert record["independent_verification_established"] is False
    assert record["scientific_truth_established"] is False
    assert len(record["outcome_fingerprint"]) == 64

def test_failed_lane_result_record_never_looks_verified():
    record = build_result_outcome("nlp", "tests/test_supreme_nlp_end_to_end.py", "pytest", 1)
    assert record["status"] == "FAIL"
    assert record["exit_code"] == 1
    assert record["verification_status"] == "RESULT_OUTCOME_CHECKED"
    assert record["independent_verification_established"] is False

def test_result_record_rejects_invalid_runner():
    try:
        build_result_outcome("ml", "tests/test.py", "shell", 0)
    except ValueError:
        pass
    else:
        raise AssertionError("unknown test runner must be rejected")
