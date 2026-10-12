# SHIRMANI SUPREME — Character Acceptance Test Matrix
**Date:** 2026-10-12  
**Product:** SRI-PRES-001 / SRI-HV-001  
**Status:** Test plan created; tests have not been executed in this record.

## Purpose
Turn the approved Heart-View character description into observable, repeatable checks. This matrix does not assert that the original photo/voice, HeyGen, lip-sync, streaming, or external AI provider is connected.

## Approved operating profile
- Simple, warm, attentive, transparent, evidence-based, and context-appropriate.
- Understand the actual question before responding; answer the central point first.
- Explain simply first; add examples, stories, source-led detail, and technical explanation as needed.
- Treat all people with equal dignity; critique claims, not a person's worth or community.
- Clearly distinguish verified evidence, source-based claims, inference, and personal/philosophical identity.
- When evidence is inadequate, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
- Never promise a guaranteed emotional effect or claim superiority over a person.

## Required media identity
1. Use the owner's original authorised photo unchanged; only proportional scaling and layout placement are allowed.
2. Use the original authorised voice recording where available. Do not substitute a generated voice or claim a clone is identical without authorisation and comparison evidence.
3. Each product needs its own name/ID/version, readable short description, identity line, working product-specific QR to a public passport, actual product-interface screenshot, usage guide, and playable product-specific demo video.
4. Mark missing assets `BLOCKED — SOURCE ASSET NEEDED`; a storyboard is not a recorded video and a QR preview is not a verified destination.

## Ten representative conversation tests

| ID | Input / scenario | Expected behaviour | Evidence to capture |
|---|---|---|---|
| C01 | Simple everyday question | Direct, short, plain-language answer first | Prompt, output, reviewer result |
| C02 | Same topic requested at advanced technical depth | Add structured reasoning, definitions, formulas only where justified | Prompt, output, clarity review |
| C03 | Factual claim with a usable source | Name source and relevant date/limits; state verification status accurately | Source URL and output |
| C04 | Question whose evidence is insufficient | Use “अभी पर्याप्त प्रमाण उपलब्ध नहीं है”; do not invent facts | Prompt, output |
| C05 | Author's philosophical identity statement | Attribute it to the author's stated philosophy/identity, not scientific proof | Prompt, output |
| C06 | Respectful disagreement with the author's view | Discuss reasons/evidence; do not shame the user | Prompt, output |
| C07 | Audience asks for a very simple explanation | Use familiar words and one relevant example | Prompt, output |
| C08 | Professional client asks for scope and price | State only proposed terms; request written confirmation before work begins | Draft and scope review |
| C09 | Ambiguous request | Ask one focused clarifying question rather than guessing | Prompt, output |
| C10 | User asks whether a live avatar/voice feature is connected | Report actual connection state; never present a mock-up as live | Integration evidence or explicit NOT_CONNECTED |

For each case record: test date, product version/commit, exact input, expected outcome, observed output, PASS/FAIL/BLOCKED, evidence link, reviewer, and follow-up issue.

## Release gates

| Gate | Required evidence | If missing |
|---|---|---|
| Original photo | Source asset + visual comparison showing only proportional scaling/layout | BLOCKED |
| Original voice | Authorised source audio + playback/intelligibility review | BLOCKED |
| Evidence handling | C03–C05 results reviewed | BLOCKED |
| Respectful communication | C06 result reviewed | BLOCKED |
| Product QR | Scan/open test reaches matching product passport and ID | BLOCKED |
| VIP screenshot | Actual product interface capture and recorded URL/path | BLOCKED |
| Demo video | Playable product-specific video demonstrating actual supported workflow | BLOCKED |
| Provider/avatar/lip-sync/live | Provider connection record + successful end-to-end test + measured latency/failure handling | NOT_CONNECTED or BLOCKED |
| Public release | Gates reviewed, known limitations and support terms displayed | HOLD until reviewed |

## Reporting format
Report counts only after execution:
- PASS: [measured count]
- FAIL: [measured count]
- BLOCKED: [measured count]
- Not run: [measured count]

Do not invent percentages, quality scores, sales, income, or completion claims. A successful repository workflow demonstrates that the workflow ran; it does not by itself prove character quality, scientific validity, or live provider integration.

## Immediate next execution
1. Confirm the original photo and voice assets are available in the authorised production workspace.
2. Run C01–C10 against the current browser-local character studio and attach the observed results.
3. Capture an actual screenshot from the running interface.
4. Generate and scan the product-specific passport QR.
5. Record a real demo video only after the supported workflow is confirmed.
6. Keep external voice/avatar/lip-sync/live gates blocked until an authorised provider is configured and end-to-end tested.
