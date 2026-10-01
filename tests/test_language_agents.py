from agents.language_agents import detect, route

def test_multilingual_script_detection():
    assert detect("निष्पक्ष समझ") == "hi"
    assert detect("ਸਤ ਸ੍ਰੀ ਅਕਾਲ") == "pa"
    assert detect("বাংলা ভাষা") == "bn"
    assert detect("ગુજરાતી") == "gu"
    assert detect("தமிழ்") == "ta"
    assert detect("తెలుగు") == "te"
    assert detect("ಕನ್ನಡ") == "kn"
    assert detect("മലയാളം") == "ml"
    assert detect("Русский") == "ru"

def test_latin_defaults_to_english():
    assert detect("Supreme NLP") == "en"

def test_route_is_verification_aware():
    result = route("hi")
    assert result["agent"] == "hindi-agent"
    assert result["verification_required"] is True
    assert result["subjective_state_inference_from_script"] is False
