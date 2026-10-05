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
