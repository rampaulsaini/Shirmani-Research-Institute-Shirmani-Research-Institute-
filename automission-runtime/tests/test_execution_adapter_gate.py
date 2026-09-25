from execution import run

def test_irreversible_action_still_requires_approval():
    result = run({"channel": "digital-store", "action": "publish"})
    assert result["status"] == "APPROVAL_REQUIRED"
