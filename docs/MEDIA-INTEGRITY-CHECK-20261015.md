# Media Integrity Check — 2026-10-15

**Scope:** local source-file fingerprint comparison only. This is not proof of ownership, consent, provider acceptance, avatar generation, or lip-sync.

## Results

| Asset | Actual file inspected | SHA-256 computed from file | Comparison | Status |
|---|---|---|---|---|
| Reference MP4 | `Video.Guru_20261013-080950532.mp4` | `a9f7872659ff6f7ceded7624b0f41c04163a395ae1dfb96fd03c209f32566f99` | Matches the value supplied with the file in this conversation | HASH MATCH — supplied value |
| Authorized voice candidate | `शिरोमणि रामपॉल सैनी _073114 (1).mp3` | `2d7bbdee9338dcc87217ba40aecf72a2a2abd455f4a4bd9cdee8e084730dc0ba` | Exact match to the repository's expected audio SHA-256 in `docs/SHIRMANI-LIVE-PRESENTATION-SUBSYSTEM.md` | HASH MATCH — repository expected value |
| Original portrait | No matching original image file was present in the inspected local files | Not computed for an original portrait | Repository expected value is `562f03564d1c1f5f90b9aaab5ecc9fecce471345d9dbfbdd8c34ba18e2110631` | BLOCKED — actual source photo unavailable |

## Observed media properties

- MP4: H.264 video, 888 × 1920; AAC audio, 44.1 kHz stereo; duration 35.982993 seconds; file size 52,076,438 bytes.
- Audio candidate: MP3 stream, mono, 48 kHz; duration 176.496 seconds; file size 1,007,109 bytes.

## Interpretation and remaining gates

1. The audio candidate's actual SHA-256 exactly matches the repository's expected audio hash. This establishes byte-for-byte file equality with that recorded expected fingerprint, not the speaker's identity or authorization by itself.
2. The MP4 fingerprint matches the value supplied with the file. The recording is a reference/setup recording; it does not independently prove that HeyGen accepted the voice, generated an avatar, or passed lip-sync.
3. The expected portrait hash cannot be checked until the actual original portrait file is available in the working session.
4. HeyGen import/provider project status is not verified. The attachment-import call did not accept the supplied file reference; the HeyGen asset-library interface was opened as a supported alternative. No successful import is claimed.
5. No generated avatar output, 20-case Q&A run, face/gaze review, lip-sync timing measurements, or end-to-end latency measurements were produced in this check.

**Release decision: BLOCKED.** Keep the verified audio hash result, but do not mark the whole presentation system production-ready.
