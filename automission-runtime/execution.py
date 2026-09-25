from connectors import load
from adapter_registry import AdapterRegistry, adapter_key
from datetime import datetime, timezone
from pathlib import Path
import os

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
    state_dir = Path(os.getenv("AUTOMISSION_STATE_DIR", str(Path(__file__).parent / "state")))
    registry = AdapterRegistry(state_dir / "adapter-registry.db")
    key = adapter_key(channel or "unknown", action)
    if not registry.can_execute(key):
        return {"status":"APPROVAL_REQUIRED","channel":channel,"action":action,
                "reason":"adapter_not_ready_or_authorized"}
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
