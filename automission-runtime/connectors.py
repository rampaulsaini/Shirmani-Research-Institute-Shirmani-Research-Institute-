import importlib
import os

ALLOWED_ADAPTERS = tuple(x.strip() for x in os.getenv("AUTOMISSION_ADAPTER_ALLOWLIST", "").split(",") if x.strip())

CHANNELS = ("employment","freelancing","ai_marketing","digital_store","yatharth_ai_music","economic_vision")

def module_for(channel):
    if channel not in CHANNELS:
        raise ValueError("unsupported channel")
    return os.getenv("AUTOMISSION_" + channel.upper() + "_ADAPTER", "").strip()

def load(channel):
    name = module_for(channel)
    if not name:
        return None
    if ALLOWED_ADAPTERS and name not in ALLOWED_ADAPTERS:
        raise RuntimeError("adapter is not allowlisted: " + name)
    if not (name.startswith("adapters.") or (ALLOWED_ADAPTERS and name in ALLOWED_ADAPTERS)):
        raise RuntimeError("adapter must use the adapters namespace")
    module = importlib.import_module(name)
    for fn in ("health","discover","prepare","execute"):
        if not callable(getattr(module, fn, None)):
            raise RuntimeError("adapter " + name + " missing " + fn)
    return module

def health_all():
    result = {}
    for channel in CHANNELS:
        try:
            adapter = load(channel)
            result[channel] = "READY" if adapter and bool(adapter.health()) else "NOT_READY"
        except Exception as exc:
            result[channel] = "ERROR:" + str(exc)
    return result
