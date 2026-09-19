"""Deterministic language routing layer; optional model enrichment can plug in later."""
LANGUAGE_AGENTS={"hi":"hindi-agent","pa":"punjabi-agent","en":"english-agent"}
def detect(text):
    if any("\u0900"<=c<="\u097f" for c in text): return "hi"
    if any("\u0a00"<=c<="\u0a7f" for c in text): return "pa"
    return "en"
def route(language): return {"language":language,"agent":LANGUAGE_AGENTS.get(language,"english-agent"),"queue":f"language.{language}"}
