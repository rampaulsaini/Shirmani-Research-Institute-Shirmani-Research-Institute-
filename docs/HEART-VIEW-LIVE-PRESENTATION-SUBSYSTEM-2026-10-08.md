# ꙰ SHIRMANI HEART-VIEW Live Presentation Subsystem — 2026-10-08

## Objective

Create a truthful, provider-neutral live presentation path:

`voice source → authorized voice adapter → Q&A/context → audio output → photo/avatar → lip-sync → live presentation`

The subsystem must distinguish **source assets**, **browser demo capability**, **connected provider capability**, and **verified external operation**.

## Supplied source assets

- Photo: `1769318638154.jpg`
  - SHA-256: `562f03564d1c1f5f90b9aaab5ecc9fecce471345d9dbfbdd8c34ba18e2110631`
  - 600 × 525 RGB
- Voice: `शिरोमणि रामपॉल सैनी (1).mp3`
  - SHA-256: `2d7bbdee9338dcc87217ba40aecf72a2a2abd455f4a4bd9cdee8e084730dc0ba`
  - 176.485 seconds, 48 kHz, mono

These hashes identify the supplied inputs; they do not by themselves establish legal ownership or third-party authorization.

## Runtime states

- **SOURCE_READY** — supplied photo/voice assets are available.
- **BROWSER_DEMO** — local photo + audio playback + amplitude lip-sync are working.
- **ADAPTER_CONNECTED** — an explicitly authorized provider endpoint is configured.
- **INTEGRATED** — Q&A, provider speech output, avatar rendering and playback exchange real artifacts end-to-end.
- **OPERATIONAL** — an external runtime can be demonstrated repeatedly.
- **VERIFIED** — an independent reviewer confirms the specific claim. Automation must never manufacture this state.

## Q&A behavior

1. Receive the user's question.
2. Preserve conversational context.
3. Prefer evidence-backed answers when evidence is available.
4. If evidence is insufficient, explicitly abstain rather than inventing.
5. Keep philosophical/identity statements separate from independently verified scientific claims.
6. Do not demean a person, caste, religion, organization or community.
7. Never claim an external organization was contacted unless an actual authorized outbound channel produced evidence.

## Voice boundary

The repository contains an adapter contract, not a hidden voice-cloning service.

A connected voice provider must be:
- explicitly authorized;
- configured outside committed secrets;
- auditable by request/response IDs;
- capable of returning an audio artifact;
- subject to provider terms and consent requirements.

The supplied MP3 can be played as a source sample in the browser demo. It is not silently transformed into a synthetic voice.

## Lip-sync boundary

The browser MVP uses audio amplitude to drive a natural mouth-open/mouth-close animation. This is a **visual synchronization demo**, not phoneme-level lip-sync.

Production phoneme-accurate lip-sync requires a provider/runtime that returns timing or viseme data. The UI must report the actual mode.

## Acceptance gates

- [ ] photo upload/display works
- [ ] supplied voice sample playback works
- [ ] amplitude lip-sync works
- [ ] test Q&A context is visible
- [ ] evidence/abstention rule is visible
- [ ] adapter configuration is explicit
- [ ] no credentials committed
- [ ] no fabricated outbound/contact/sale/verification claims
- [ ] connected-provider runtime evidence is captured before calling the system OPERATIONAL
