import os

CHANNELS = (
    "employment",
    "freelancing",
    "ai_marketing",
    "digital_store",
    "yatharth_ai_music",
    "economic_vision",
)

def configured(channel):
    key = "AUTOMISSION_" + channel.upper() + "_ADAPTER"
    return os.getenv(key, "").strip()

def plan(channel, opportunity):
    if channel not in CHANNELS:
        raise ValueError("unsupported channel")
    adapter = configured(channel)
    action = opportunity.get("action", "review")
    if action in {"apply","submit","accept_contract","publish","payment"}:
        return {"channel":channel,"adapter":adapter or None,
                "status":"APPROVAL_REQUIRED","action":action,
                "reason":"irreversible action requires authorization"}
    return {"channel":channel,"adapter":adapter or None,
            "status":"READY_FOR_EXECUTION" if adapter else "PLANNED",
            "action":action}
