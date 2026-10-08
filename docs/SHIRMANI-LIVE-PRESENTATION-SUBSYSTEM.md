# SHIRMANI Live Presentation Subsystem

## Flow
**Voice → Authorized Voice Integration → Test Q&A → Lip-Sync → Live Presentation**

### Implemented in this repository
- Static live-presentation interface.
- User-selectable portrait and audio for local preview.
- Browser speech-synthesis fallback for Q&A testing.
- Evidence-gated response rule with the exact insufficient-evidence phrase:
  **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है”**
- Audio-reactive mouth timing demo.
- Explicit boundary between user-authored identity/philosophy and independently verified factual/scientific claims.
- Provider adapter boundary: no external voice cloning is enabled merely by opening the page.
- Production lip-sync is intentionally not claimed until phoneme/viseme timestamps are available.

## Authorization model
External voice-provider integration requires explicit authorization and provider credentials. The repository must not manufacture consent, credentials, provider connection state, or verification.

## User-provided source asset fingerprints
- Photo SHA-256: `562f03564d1c1f5f90b9aaab5ecc9fecce471345d9dbfbdd8c34ba18e2110631`
- Audio SHA-256: `2d7bbdee9338dcc87217ba40aecf72a2a2abd455f4a4bd9cdee8e084730dc0ba`
- Audio: mono, 48 kHz, 176.485 seconds.

These fingerprints identify the files supplied in the current work session; the binary assets are not silently uploaded to GitHub by this change.

## Next production gate
1. Put the authorized portrait/audio assets in the repository's designated live-assets path.
2. Select an explicitly authorized voice provider, if dynamic same-voice synthesis is required.
3. Store provider credentials only in GitHub Actions secrets or the provider's approved secret store.
4. Generate phoneme/viseme timestamps for accurate lip-sync.
5. Run test Q&A and evidence gate.
6. Publish only after QC passes.
