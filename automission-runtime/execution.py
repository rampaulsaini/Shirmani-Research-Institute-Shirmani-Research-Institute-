from connectors import load
from datetime import datetime, timezone

IRREVERSIBLE = {"apply","submit","accept_contract","publish","payment"}

def run(item):
    action = item.get("action", "review")
    if action in IRREVERSIBLE:
        return {"status":"APPROVAL_REQUIRED","action":action,
                "reason":"irreversible action requires authorization"}
    channel = item.get("channel")
    adapter = load(channel)
    if adapter is None:
        return {"status":"PLANNED","channel":channel,
                "action":action,"reason":"adapter_not_configured"}
    prepared = adapter.prepare(item)
    if not isinstance(prepared, dict):
        return {"status":"REJECTED","channel":channel,"reason":"invalid_adapter_prepare_result"}
    if prepared.get("status") in {"APPROVAL_REQUIRED","REJECTED"}:
        return prepared
    result = adapter.execute(prepared)
    if not isinstance(result, dict):
        return {"status":"REJECTED","channel":channel,"reason":"invalid_adapter_execute_result"}
    result.setdefault("channel", channel)
    result.setdefault("action", action)
    result["executed_at"] = datetime.now(timezone.utc).isoformat()
    return result
