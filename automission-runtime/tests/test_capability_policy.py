from capability_policy import CapabilityPolicy
from execution import run


def test_permission_matrix_requires_authorization_for_publish():
    policy = CapabilityPolicy()
    assert policy.allows_planning("publish")
    assert policy.requires_authorization("publish")
    assert not policy.allows_execution("publish")


def test_unknown_capability_fails_closed():
    result = run({"channel": "digital-store", "action": "unknown_action"})
    assert result["status"] == "REJECTED"
    assert result["reason"] == "capability_not_in_permission_matrix"


def test_reversible_capability_can_reach_adapter_gate():
    result = run({"channel": "digital_store", "action": "create"})
    assert result["status"] in {"PLANNED", "APPROVAL_REQUIRED"}
