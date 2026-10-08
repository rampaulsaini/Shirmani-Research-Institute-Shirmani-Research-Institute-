# SHIRMANI Live Voice → Voice System → Content → Photo/Lip-sync → Live Presentation

## Purpose

A controlled multimodal presentation subsystem for the Shirmani Research Institute.

Pipeline:

**Voice → Authorized Voice Integration → Test Q&A → Content → Photo/Lip-sync → Live Presentation**

## Integrity boundary

- Voice identity must be explicitly authorized by the owner of the voice.
- The browser demo uses the device's speech synthesis where available; it does not clone a person's voice.
- A supplied photograph is treated as presentation media, not proof of identity.
- Philosophical/identity statements remain author statements unless independently verified.
- Scientific or factual claims require evidence; insufficient evidence must be reported as: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
- No person, caste, religion, faith, organization or community is to be demeaned.
- Live publication requires human approval and applicable platform/rights checks.
- Lip-sync in this foundation is a visual timing prototype; production-grade phoneme-level lip-sync requires a selected authorized media provider or an owned rendering stack.

## Runtime stages

1. **Voice input** — microphone or text-to-speech test.
2. **Authorization gate** — explicit owner authorization record.
3. **Q&A context** — question → grounded response.
4. **Evidence gate** — source/evidence/uncertainty separation.
5. **Content renderer** — concise answer, caption, and source state.
6. **Photo presentation** — selected authorized image.
7. **Lip-sync timing prototype** — mouth animation synchronized to audio activity.
8. **Live presentation** — browser presentation surface.
9. **Audit** — timestamp, source state, authorization state, output state.

## Verification states

- READY
- AUTHORIZATION_REQUIRED
- EVIDENCE_REQUIRED
- TEST_ONLY
- HUMAN_REVIEW
- LIVE_READY
- NOT_VERIFIED

The system must never convert a workflow success into an independent scientific verification claim.

## Next production integrations

- Replace browser speech synthesis with an explicitly authorized voice provider.
- Add consent/authorization artifact storage and revocation.
- Add server-side Q&A with source retrieval and evidence citations.
- Add phoneme/viseme lip-sync renderer after provider selection.
- Add WebRTC/live-stream output only after rights, moderation, security and human approval gates.
