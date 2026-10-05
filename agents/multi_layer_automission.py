"""Bounded multi-layer AI/ML/NLP practitioner Automission controller.

"Quantum" means quantum-inspired deterministic selection only; no quantum hardware
or quantum advantage is claimed. Automation never promotes records to VERIFIED.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib, json
from pathlib import Path
from math import isfinite

@dataclass(frozen=True)
class Lane:
    name: str
    layer: str
    priority: float
    checks: tuple[str, ...]

LANES = (
    Lane("practitioner", "AI/ML/NLP practitioner", 1.00, ("compile core agents","run deterministic smoke tests","preserve provenance and limitations")),
    Lane("ml", "ML evaluation", 0.96, ("check calibration inputs","reject NaN/Inf","measure drift and compatibility")),
    Lane("nlp", "NLP reasoning", 0.94, ("validate abstention","validate heterogeneous modalities","keep confidence calibrated only when evaluated")),
    Lane("evidence", "independent evidence", 1.10, ("separate prepared packets from reviewed records","require counter-evidence","keep VERIFIED fail-closed")),
    Lane("automission", "Automission operations", 0.92, ("audit workflow health","emit bounded improvement actions","block scheduled code mutation")),
    Lane("quantum-mechanism", "quantum-inspired orchestration", 0.88, ("score candidate lanes","select a deterministic next action","record that no quantum hardware is used")),
)

def _score(lane, signals):
    try:
        raw = float(signals.get(lane.name, 0.0))
    except (TypeError, ValueError):
        raw = 0.0
    pressure = max(0.0, min(1.0, raw)) if isfinite(raw) else 0.0
    return round(lane.priority*(0.5+0.5*pressure),6)

def choose_next_action(signals=None):
    signals=signals or {}
    invalid_signals=[]
    for name, value in signals.items():
        try:
            numeric=float(value)
        except (TypeError, ValueError):
            invalid_signals.append(name)
            continue
        if not isfinite(numeric):
            invalid_signals.append(name)
    scored=[{"lane":l.name,"layer":l.layer,"score":_score(l,signals),"checks":list(l.checks)} for l in LANES]
    scored.sort(key=lambda x:(-x["score"],x["lane"]))
    return {"selection_mode":"quantum-inspired-deterministic","quantum_hardware_used":False,"quantum_advantage_claimed":False,
            "winner":scored[0],"ranked_lanes":scored,
            "control_input_valid":not invalid_signals,"invalid_control_signals":sorted(invalid_signals),
            "governance":{"fail_closed":True,"independent_verification_required":True,
                          "scheduled_code_mutation_allowed":False,"automated_verified_promotion_allowed":False,
                          "verification_basis":"verified_result_record_only",
                          "verification_mode":"result_outcome_review_not_direct_automation",
                          "orchestration_execution_allowed":not invalid_signals}}

def _fingerprint_payload(cycle):
    return {k: v for k, v in cycle.items() if k != "cycle_fingerprint"}

def fingerprint_cycle(cycle):
    return hashlib.sha256(
        json.dumps(_fingerprint_payload(cycle), sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()

def constant_time_compare(left, right):
    import hmac
    return hmac.compare_digest(str(left), str(right))

def verify_cycle_fingerprint(cycle):
    expected = cycle.get("cycle_fingerprint") if isinstance(cycle, dict) else None
    return bool(expected) and constant_time_compare(expected, fingerprint_cycle(cycle))

def result_outcome_fingerprint(result):
    """Hash an observed result without converting it into a scientific verdict."""
    return hashlib.sha256(
        json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()

def review_result_outcome(expected_result, observed_result):
    """Check whether an observed result matches an explicit expected result.

    This verifies the outcome record only. It never establishes scientific truth,
    independent replication, or VERIFIED status.
    """
    if not isinstance(expected_result, dict) or not isinstance(observed_result, dict):
        raise ValueError("expected_result and observed_result must be mappings")
    expected_hash = result_outcome_fingerprint(expected_result)
    observed_hash = result_outcome_fingerprint(observed_result)
    if not all(key in observed_result and observed_result[key] == value for key, value in expected_result.items()):
        matched = False
    else:
        matched = True
    return {
        "status": "RESULT_OUTCOME_MATCH" if matched else "RESULT_OUTCOME_MISMATCH",
        "matched": matched,
        "expected_result_fingerprint": expected_hash,
        "observed_result_fingerprint": observed_hash,
        "verification_status": "RESULT_OUTCOME_CHECKED",
        "independent_verification_established": False,
        "scientific_truth_established": False,
    }

LANE_CONTRACTS = {
    "practitioner": {"focus": "practitioner-core", "runner": "pytest"},
    "ml": {"focus": "ml-validation", "runner": "pytest"},
    "nlp": {"focus": "nlp-end-to-end", "runner": "pytest"},
    "evidence": {"focus": "independent-evidence-ledger", "runner": "python"},
    "automission": {"focus": "automission-hardening", "runner": "python"},
    "quantum-mechanism": {"focus": "deterministic-orchestration", "runner": "pytest"},
}

def validate_lane_contract(lane, focus, test_path, runner):
    """Validate that an executed lane matches its declared contract."""
    if lane not in LANE_CONTRACTS:
        raise ValueError("unknown lane")
    if not isinstance(focus, str) or not focus:
        raise ValueError("focus must be a non-empty string")
    if not isinstance(test_path, str) or not test_path:
        raise ValueError("test_path must be a non-empty string")
    if runner not in {"pytest", "python"}:
        raise ValueError("runner must be pytest or python")
    expected = LANE_CONTRACTS[lane]
    if focus != expected["focus"] or runner != expected["runner"]:
        raise ValueError("lane contract mismatch")
    return True

def build_result_outcome(lane, test_path, runner, exit_code):
    """Create a result record from the actual lane test process outcome."""
    if not isinstance(lane, str) or not lane:
        raise ValueError("lane must be a non-empty string")
    if not isinstance(test_path, str) or not test_path:
        raise ValueError("test_path must be a non-empty string")
    if runner not in {"pytest", "python"}:
        raise ValueError("runner must be pytest or python")
    if not isinstance(exit_code, int):
        raise ValueError("exit_code must be an integer")
    status = "PASS" if exit_code == 0 else "FAIL"
    return {
        "lane": lane,
        "test_path": test_path,
        "runner": runner,
        "exit_code": exit_code,
        "status": status,
        "outcome_fingerprint": result_outcome_fingerprint({
            "lane": lane, "test_path": test_path, "runner": runner,
            "exit_code": exit_code, "status": status,
        }),
        "verification_status": "RESULT_OUTCOME_CHECKED",
        "independent_verification_established": False,
        "scientific_truth_established": False,
    }

def build_cycle(signals=None, executed_lane=None):
    decision=choose_next_action(signals)
    cycle={"controller":"SHIRMANI Multi-Layer AI ML NLP Practitioner Automission","version":3,
           "generated_at_utc":datetime.now(timezone.utc).isoformat(),
           "architecture":["Observe","Collect","Clean","AI/ML/NLP Evaluate","Reason","Evidence","Independent Verify","QC","Automission","Continuous Improve"],
           "decision":decision}
    if executed_lane is not None:
        cycle["executed_lane"] = str(executed_lane)
    cycle["cycle_fingerprint"]=fingerprint_cycle(cycle)
    return cycle

def write_cycle(path="generated/multi-layer-automission/cycle.json"):
    result=build_cycle(); target=Path(path); target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+ "\n",encoding="utf-8"); return result

if __name__=="__main__":
    print(json.dumps(write_cycle(),ensure_ascii=False,indent=2))
