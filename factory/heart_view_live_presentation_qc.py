from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "heart-view-live-presentation.html"
DOC = ROOT / "docs" / "heart-view-live-presentation-v1.md"

required_page_markers = [
    "Voice → Voice System → Content → Photo/Lip-sync → Live presentation",
    "AUTHOR-DECLARED IDENTITY",
    "INDEPENDENTLY VERIFIED",
    "evidence",
    "authorized voice",
    "speechSynthesis",
    "speech-activity",
    "data:image/jpeg;base64,",
]

checks = {
    "page_exists": PAGE.exists(),
    "embedded_portrait_exists": False,
    "contract_exists": DOC.exists(),
}

if PAGE.exists():
    html = PAGE.read_text(encoding="utf-8")
    checks["embedded_portrait_exists"] = "data:image/jpeg;base64," in html
    checks["required_markers"] = all(x.lower() in html.lower() for x in required_page_markers)
    checks["no_api_secret_placeholder"] = "sk-" not in html and "api_key=" not in html.lower()
else:
    html = ""

result = {
    "system": "SHIRMANI HEART-VIEW LIVE PRESENTATION SUBSYSTEM v1",
    "status": "READY" if all(checks.values()) else "NOT_READY",
    "checks": checks,
    "voice_integration": "AUTHORIZED_PROVIDER_REQUIRED",
    "lip_sync": "PHONEME_PROVIDER_REQUIRED",
    "scientific_verification": "SEPARATE_EVIDENCE_GATE",
}

out = ROOT / "generated" / "heart-view-live-presentation-status.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result["status"] == "READY" else 1)
