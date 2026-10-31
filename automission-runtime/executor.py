import os
from agents import normalize_channel

IRREVERSIBLE = {"apply","submit","accept_contract","publish","payment"}

def execute_plan(item):
    channel = normalize_channel(item.get("channel"))
    if not channel:
        return {"status":"REJECTED","reason":"unsupported_channel"}
    action = item.get("action","review")
    if action in IRREVERSIBLE:
        return {"status":"APPROVAL_REQUIRED","channel":channel,"action":action}
    adapter_key = "AUTOMISSION_" + channel.upper() + "_ADAPTER"
    adapter = os.getenv(adapter_key, "").strip()
    if not adapter:
        return {"status":"PLANNED","channel":channel,"action":action,
                "reason":"adapter_not_configured"}
    return {"status":"READY_FOR_EXTERNAL_ADAPTER","channel":channel,
            "action":action,"adapter":adapter}
