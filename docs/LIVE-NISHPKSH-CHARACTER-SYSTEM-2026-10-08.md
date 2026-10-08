# Live Nishpaksh Character System — 2026-10-08

## उद्देश्य

यह subsystem **शिरोमणि रामपॉल सैनी** की public digital presentation को research/evidence platform से जोड़ता है।

लक्ष्य केवल एक talking avatar बनाना नहीं है। लक्ष्य है:

**Voice → authorized voice integration → question/context understanding → evidence-aware answer → voice → face/lip-sync → live presentation**

यह presentation layer user-declared identity/creative presentation को independently verified scientific evidence से अलग रखती है।

## मुख्य platform पर स्थान

Public entry point:

- live-character.html — Live Character / Presentation Console
- index.html — मुख्य platform landing page पर “Live Nishpaksh Character” entry
- Research/evidence dashboards — factual claims और verification state के लिए
- Production Command Center — runtime/output telemetry के लिए

Visitor path:

**Main Platform → Live Character → Question → Evidence-aware Response → Voice/Presentation**

## Character contract

### Presentation qualities

- सरल
- सहज
- निर्मल
- पारदर्शी
- स्पष्ट
- प्रत्यक्ष communication
- context-sensitive dress/presentation
- natural eye-contact/gaze where the rendering system supports it
- natural facial movement
- accurate lip-sync
- voice/face timing coherence
- respectful communication across people, communities and organizations
- concise explanation before unnecessary long storytelling

### Context-aware presentation

Dress, posture, tone and visual presentation may depend on context (for example: research, public explanation, education, creative presentation, formal interaction).

Context changes **presentation**, not evidence standards.

## Answer contract

1. Understand the question and context.
2. Retrieve relevant source/evidence when available.
3. Separate:
   - author-declared / philosophical / identity statement;
   - interpretation or hypothesis;
   - independently verified evidence.
4. If evidence is adequate, answer with source/provenance.
5. If evidence is inadequate, say clearly:

> अभी पर्याप्त प्रमाण उपलब्ध नहीं है।

6. Never manufacture verification, credentials, scientific proof, revenue, testimonials, users or external authorization.
7. Do not demean a person, caste, religion, faith, community or organization.
8. Comparative facts may be presented when relevant and sourced.
9. The system must not convert a philosophical identity statement into a scientific finding.

## Presentation state machine

- IDLE
- LISTENING
- UNDERSTANDING
- EVIDENCE_LOOKUP
- ANSWER_READY
- SPEAKING
- LIP_SYNC
- PRESENTING
- ABSTAIN
- ERROR

The visual layer must follow the answer/voice state. It must never simulate speech when there is no authorized active voice output.

## Voice → presentation pipeline

1. Voice input / text input
2. Speech recognition where enabled
3. NLP/context understanding
4. Evidence retrieval and provenance
5. Answer contract / abstention gate
6. Authorized voice generation
7. Audio timing metadata
8. Avatar/facial rendering
9. Lip-sync
10. Public presentation
11. Traceable interaction/result record

## Evidence boundary

A successful workflow, a fluent answer, a convincing avatar, eye contact, facial expression, lip-sync, or voice similarity is **not** evidence that a scientific or identity claim is independently verified.

The platform keeps:

**DESIGNED → AUTOMATED → INTEGRATED → OPERATIONAL → VERIFIED**

as distinct states.

VERIFIED requires independent evidence for the specific claim and cannot be created merely by automation.

## Human authorization boundary

High-impact, irreversible, financial, legal, identity, account, or external-publication actions remain human-authorized.

Self-improvement is versioned and test-gated; it must not silently mutate the public character.

## “Permanent” behavior

The intended product behavior is continuous availability through the deployed runtime, durable configuration, monitoring and recovery—not an unsupported claim that an AI process is literally permanent or conscious.

## Acceptance gates

### Presentation

- [ ] authorized avatar/voice asset
- [ ] consent/authorization recorded where required
- [ ] natural facial movement
- [ ] lip-sync timing check
- [ ] audio/video synchronization check
- [ ] mobile-responsive public route

### Intelligence

- [ ] context-aware Q&A
- [ ] source/provenance retrieval
- [ ] explicit insufficient-evidence response
- [ ] comparative analysis with sources
- [ ] no unsupported verification

### Operations

- [ ] runtime endpoint
- [ ] persistence
- [ ] monitoring
- [ ] rollback/recovery
- [ ] bounded automation
- [ ] audit trail

### Quality

- [ ] adversarial tests
- [ ] evidence-boundary tests
- [ ] identity/presentation separation tests
- [ ] privacy/safety review
- [ ] independent verification remains fail-closed

## Current implementation status

The public presentation contract and main-platform entry are being added as a first-class subsystem.

The visual/voice experience is **not declared fully live merely because the public page exists**. Actual live avatar/voice operation requires the authorized HeyGen/voice runtime connection and successful end-to-end runtime evidence.

That distinction is intentional and matches the Shirmani evidence architecture.
