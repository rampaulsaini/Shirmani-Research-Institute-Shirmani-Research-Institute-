"""Deterministic multilingual script/language routing with safe model-enrichment hooks.

The router identifies likely language from Unicode script evidence. It does not
infer emotion, consciousness, intent, or identity from script alone.
"""

LANGUAGE_AGENTS = {
    "hi": "hindi-agent", "pa": "punjabi-agent", "en": "english-agent",
    "ur": "urdu-agent", "sa": "sanskrit-agent", "bn": "bengali-agent",
    "gu": "gujarati-agent", "mr": "marathi-agent", "ta": "tamil-agent",
    "te": "telugu-agent", "kn": "kannada-agent", "ml": "malayalam-agent",
    "or": "odia-agent", "ar": "arabic-agent", "ru": "cyrillic-agent",
}

SCRIPT_RANGES = (
    ("hi", 0x0900, 0x097F), ("pa", 0x0A00, 0x0A7F),
    ("bn", 0x0980, 0x09FF), ("gu", 0x0A80, 0x0AFF),
    ("or", 0x0B00, 0x0B7F), ("ta", 0x0B80, 0x0BFF),
    ("te", 0x0C00, 0x0C7F), ("kn", 0x0C80, 0x0CFF),
    ("ml", 0x0D00, 0x0D7F), ("ar", 0x0600, 0x06FF),
    ("ru", 0x0400, 0x04FF),
)


def detect(text):
    counts = {}
    for char in str(text):
        code = ord(char)
        for language, start, end in SCRIPT_RANGES:
            if start <= code <= end:
                counts[language] = counts.get(language, 0) + 1
                break
    if not counts:
        return "en"
    # Arabic-script languages need lexical/model confirmation; defaulting to
    # Urdu is explicit and reversible rather than pretending script proves it.
    if counts.get("ar", 0) and not any(
        k in counts for k in ("hi", "pa", "bn", "gu", "or", "ta", "te", "kn", "ml", "ru")
    ):
        return "ur"
    return max(counts, key=counts.get)


def route(language):
    language = str(language).lower()
    return {
        "language": language,
        "agent": LANGUAGE_AGENTS.get(language, "english-agent"),
        "queue": f"language.{language}",
        "verification_required": True,
        "model_enrichment_allowed": True,
        "subjective_state_inference_from_script": False,
    }
