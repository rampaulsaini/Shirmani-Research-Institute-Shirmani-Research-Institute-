import importlib
import os

CHANNELS = ("employment","freelancing","ai_marketing","digital_store","yatharth_ai_music","economic_vision")

def module_for(channel):
    if channel not in CHANNELS:
        raise ValueError("unsupported channel")
    return os.getenv("AUTOMISSION_" + channel.upper() + "_ADAPTER", "").strip()

def load(channel):
    name = module_for(channel)
    if not name:
        return None
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
