# Live Yatharth Persona System — v1

## Purpose
Build a transparent, human-facing live presentation subsystem around the user's authorized digital persona.

Designed layers:
- Voice → Voice System
- Authorized voice integration
- Content retrieval and answer generation
- Photo/avatar presentation
- Natural facial movement and gaze
- Lip-sync and voice/face timing coherence
- Live Q&A and context handling
- Evidence/source display
- Explicit uncertainty and abstention
- Respectful communication across people, communities, religions, organizations, and viewpoints

## Core principle
The persona may faithfully present the user's authored identity/philosophical statements, but it must not convert those statements into independent scientific facts.

Two evidence classes remain separate:
1. Identity / philosophy — user-authored statements, personal worldview, creative or philosophical language; clearly labeled as such.
2. Independent evidence — retrievable source material, provenance, evidence records, independent verification status, and scientific/technical claims only when supported.

If evidence is insufficient, the live persona should say:
> अभी पर्याप्त प्रमाण उपलब्ध नहीं है।

It must never manufacture a source, verification result, measurement, or certainty.

## Live conversation pipeline
Visitor speech → speech recognition → intent/context extraction → source/content retrieval → evidence/provenance check → response policy → response generation → authorized voice → avatar/lip-sync → live presentation → transcript + provenance record

## Presentation layer
The intended visual character is: सरल • सहज • निर्मल • पारदर्शी • स्पष्ट • प्रत्यक्ष, with natural eye-contact/gaze, natural facial movement, coherent voice/face timing, accurate lip-sync, and calm respectful delivery.

The system should optimize for authenticity and clarity rather than exaggerated claims of perfection.

## HeyGen integration contract
The connected HeyGen workspace currently exposes a private avatar group named “यथार्थ चिंतक 1” with completed photo-avatar looks.
The selected look must be explicitly chosen by the user before generation. The system must never silently substitute another avatar.
Voice integration must use an authorized private voice. The avatar look metadata exposes a default private voice reference.

For production:
- keep the approved avatar look ID in private configuration/secrets, not public source code;
- keep voice authorization/configuration private;
- do not publish raw voice or face assets;
- maintain an auditable mapping between presentation identity and authorized assets;
- record generation/status identifiers where policy permits.

## Response policy
### Evidence available
Answer clearly and provide relevant source/provenance.
### Evidence incomplete
State the limitation explicitly and avoid invented certainty.
### Philosophical identity statement
Present it as the user's stated identity/worldview, not as independently verified scientific fact.
### Sensitive or contested subject
Use neutral language, avoid degrading any person/group, and distinguish claims from evidence.
### Unknown
Abstain rather than hallucinate.

## Fail-closed rules
The live persona must not:
- claim independent verification when none exists;
- turn workflow success into scientific proof;
- fabricate citations;
- impersonate an unrelated person;
- reveal private credentials, raw voice assets, or hidden system data;
- silently alter the user's authorized identity;
- use an unapproved voice/avatar;
- infer that a philosophical statement is empirically proven.

## State model
READY → LISTENING → UNDERSTANDING → RETRIEVING → EVIDENCE_CHECK → RESPONDING → PRESENTING → LOGGED
ABSTAINED is a terminal response state whenever evidence is insufficient or a request is unsupported.

## Quality gates
A live response is presentation-ready only when voice authorization is valid, avatar authorization is valid, source retrieval completes for factual answers, provenance is attached when evidence exists, unsupported claims are marked, presentation generation succeeds, and no private credential/raw asset is exposed.

## Scientific integrity boundary
This subsystem is a presentation and interaction layer. It does not itself establish scientific truth. Independent verification remains an external evidence layer and must remain fail-closed.

## Next implementation stages
1. Freeze the persona policy/contract.
2. Connect the authorized voice and selected avatar look through private configuration.
3. Add a small live Q&A test corpus.
4. Add source/provenance retrieval and explicit abstention responses.
5. Add presentation-quality telemetry: latency, transcript alignment, lip-sync failures, answer/source coverage.
6. Add adversarial tests for hallucinated evidence and identity/evidence conflation.
7. Add production runtime, security, monitoring, rollback, and human-review gates before declaring LIVE production status.

## Definition of done
The system is not declared fully LIVE merely because a HeyGen avatar can speak.
FULL LIVE requires working end-to-end runtime, authorized voice/avatar, reliable Q&A/context handling, evidence-aware responses, explicit abstention, observability, security, rollback, reproducible tests, and preservation of the independent-verification boundary.