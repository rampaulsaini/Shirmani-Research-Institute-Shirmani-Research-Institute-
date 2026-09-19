# ꙰ Research Factory — Agent System

यह layer 16 specialized agents को एक Supervisor के अधीन रखती है।

**महत्वपूर्ण:** ये agents अभी orchestration specification हैं; GitHub Actions स्वयं background में 16 independent AI minds नहीं चला रहा। अगले workflow में प्रत्येक agent एक deterministic/free-first stage के रूप में execute होगा और जहाँ external/open model उपलब्ध हो वहीं semantic generation जोड़ी जाएगी।

Flow:
Sources → Librarian → Dedup → Concepts → Research → Products → Evidence → Verification → Languages → Audio → Publishing → Archive

हर artifact में provenance, hash, source repository और verification status रहना चाहिए।
