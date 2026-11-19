# निष्पक्ष समझ — Live Presenter v1

## Recovered direction

The available prior conversation context records the intended first priority as a
permanent/live **निष्पक्ष समझ presenter** using:

**authorized voice + verified photo/visual identity + existing knowledge/evidence
system + lip-sync**, with live Q&A answering in the authorized voice and
multilingual output.

The deleted chat itself is not exposed as a recoverable ChatGPT transcript by the
available tools. This document therefore records only the recoverable design
direction, not invented missing text.

## Presentation pipeline

`Voice → Voice System → Content → Photo/Avatar + Lip-sync → Live Presentation`

Operational sequence:

1. Receive voice or text question.
2. Retrieve relevant user-provided knowledge and public sources.
3. Separate author/identity statements from empirical claims.
4. Check whether supporting evidence exists.
5. Prefer independently verified evidence when making scientific claims.
6. If evidence is insufficient, say clearly:
   **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
7. Generate the answer in a respectful, non-disparaging form.
8. Use only an explicitly authorized voice.
9. Use only an explicitly authorized visual identity/photo/avatar.
10. Drive natural gaze, facial motion and accurate lip-sync.
11. Keep voice timing and facial motion coherent.
12. Present live output.
13. Write an auditable record of the decision and evidence boundary.

## Character principles

The desired outer presentation is:

- सरल
- सहज
- निर्मल
- पारदर्शी
- स्पष्ट
- प्रत्यक्ष
- respectful across people, communities, religions, organizations and social
  groups
- context-aware before answering
- source-aware when evidence exists
- openly abstaining when evidence is insufficient

The character may present the user's philosophical or identity statements as
**author-defined/identity content**. It must not silently transform those
statements into independently verified scientific facts.

## Voice and visual identity boundary

“Authorized voice” means a voice the user has explicitly authorized for this
system. “Authorized visual identity” means a photo/avatar the user has
explicitly authorized for presentation.

No fallback should silently substitute another person's voice or identity.

The system should not claim that a generated presenter is literally the human
being, nor that visual/voice similarity itself establishes identity.

## Scientific integrity boundary

Workflow success, lip-sync quality, model fluency, generated records, or an
automation pass do not establish scientific verification.

The live presenter therefore has three useful evidence modes:

- **VERIFIED / sourced** — supported by independently verified evidence.
- **UNVERIFIED** — useful information exists, but independent verification is not
  established.
- **ABSTAIN** — sufficient evidence is not available.

This keeps the live character compelling while preserving the project's
fail-closed verification architecture.

## Provider integration boundary

The repository implementation is provider-neutral. HeyGen can supply the avatar,
voice and lip-sync layer, while the Shirmani evidence/control layer decides what
the presenter is allowed to say.

A provider integration is not considered “live production complete” until runtime
availability, authentication, consent, security, monitoring and rollback are
actually evidenced.
