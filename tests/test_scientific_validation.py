import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))

from supreme_nlp.scientific_validation import calibration_error, independent_gate

def test_calibration_error_perfect():
    assert calibration_error([1.0,0.0,1.0,0.0],[True,False,True,False]) == 0.0

def test_gate_fails_without_independent_replication():
    r=independent_gate(repeated_trials=10, independent_sources=1, preregistered=True,
                       blinded=True, negative_controls=True, reproducible=True,
                       effect_replicated=True)
    assert r.status=="NOT_VERIFIED"

def test_gate_requires_full_protocol():
    r=independent_gate(repeated_trials=3, independent_sources=2, preregistered=True,
                       blinded=True, negative_controls=True, reproducible=True,
                       effect_replicated=True)
    assert r.status=="VERIFIED_CANDIDATE"
