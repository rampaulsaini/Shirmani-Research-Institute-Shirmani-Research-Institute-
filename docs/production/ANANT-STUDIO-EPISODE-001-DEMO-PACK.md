# Anant Studio — Episode 001 Demo Pack

**Episode:** 001  
**Working title:** हृदय से हृदय संवाद  
**Theme:** सत्य • प्रेम • शांति  
**Language:** Hindi  
**Format target:** 9:16 vertical short, 1080 × 1920, 30 fps  
**Status:** Script and production specification only. Original voice sync, rendered media, playback QA, publication, and revenue are pending.

## 1. Release boundary

This pack is a production brief, not proof that an audio/video asset exists. The source MP3 referenced in the conversation was not available to inspect in the current work session. Do not synthesize a substitute and label it as the user's original voice. Do not use another person's face or photo as the user's identity. Use only source assets supplied or explicitly approved by the user.

## 2. 15-second short — narration draft

> जब मन शांत होता है, तब सत्य को देखने की दृष्टि निर्मल होती है।  
> जहाँ सत्य है, वहाँ विश्वास जन्म लेता है।  
> जहाँ प्रेम है, वहाँ भेद मिटते हैं।  
> और जहाँ शांति है, वहाँ जीवन को नई दिशा मिलती है।  
> **सत्य • प्रेम • शांति**

This is editorial draft copy. Revise it against the user's actual recording before locking captions or timings.

## 3. 30-second podcast — narration draft

> क्या सत्य केवल विचार है, या उसे जीवन में प्रत्यक्ष अनुभव भी किया जा सकता है?  
> जब हम बिना पक्षपात के देखते हैं, तो समझ विकसित होती है।  
> जब समझ में प्रेम जुड़ता है, तो संबंधों में विश्वास आता है।  
> और जब जीवन में विश्वास तथा संवेदनशीलता होती है, तब शांति की संभावना बढ़ती है।  
> आइए, प्रकृति, पृथ्वी और समस्त जीवन के प्रति उत्तरदायी बनें।  
> **सत्य • प्रेम • शांति।**

This is a draft, not a transcript of the user's recording.

## 4. Visual storyboard

| Time target | Visual direction | On-screen text |
|---|---|---|
| 00–04 s | Sunrise and quiet natural landscape | सत्य |
| 04–09 s | Respectful human connection and listening | प्रेम |
| 09–15 s | Earth, water, forests and living systems | शांति |
| 15–22 s | Nature and people caring for their surroundings | जीवन का सम्मान |
| 22–27 s | Calm wide landscape; visual breathing room | निष्पक्ष समझ |
| 27–30 s | Anant Studio title card | सत्य • प्रेम • शांति |

Timing is provisional until the approved voice track is measured. Do not speed up or cut the user's words merely to fit the target duration; adjust the edit or duration instead.

## 5. Asset and identity rules

- Preserve the original recording as an untouched source asset.
- Keep an edited working copy separate from the source.
- Do not clone, imitate, or synthesize the user's voice unless the user separately authorizes a specific voice-generation workflow.
- Use the user's own photo only when the user supplies or clearly approves that exact image.
- Any stock or generated visuals must be clearly treated as illustrative visuals, not as documentary evidence.
- Add background music only when its licence and use are cleared; keep narration intelligible.
- Captions must be checked against the actual audio, not merely copied from this draft.

## 6. Production checklist

- [ ] Original MP3 received and playable.
- [ ] Source file name, duration, format, and checksum recorded.
- [ ] User's actual words transcribed and reviewed.
- [ ] Final narration wording approved.
- [ ] Voice edit preserves meaning, pauses, and identity.
- [ ] Visual assets and licences/permissions recorded.
- [ ] Captions timed against the final audio.
- [ ] Export rendered at the agreed dimensions and frame rate.
- [ ] Full playback checked on a mobile-sized screen.
- [ ] Audio clipping, sync, caption spelling, safe margins, and black frames checked.
- [ ] Final file checksum and reviewer/date recorded.
- [ ] User approves the final master before any public release.

## 7. Evidence record template

Record actual values only. Leave unknown fields null; never infer a successful render, test, upload, or publication.

```json
{
  "episode_id": "ANANT-EP-001",
  "title": "हृदय से हृदय संवाद",
  "language": "hi",
  "status": "draft",
  "source_audio": {
    "received": false,
    "filename": null,
    "duration_seconds": null,
    "sha256": null
  },
  "voice_sync": {
    "status": "blocked_pending_source_audio",
    "reviewed_by": null,
    "reviewed_at": null
  },
  "video_master": {
    "rendered": false,
    "path": null,
    "sha256": null,
    "dimensions": "1080x1920",
    "fps": 30
  },
  "quality_assurance": {
    "playback_test": "not_run",
    "audio_sync": "not_run",
    "caption_review": "not_run",
    "visual_review": "not_run"
  },
  "publication": {
    "status": "not_published",
    "platform": null,
    "url": null,
    "published_at": null
  },
  "revenue": {
    "payment_received": false,
    "amount": null,
    "currency": null,
    "evidence_reference": null
  }
}
```

## 8. Completion criteria

The demo may be labelled **rendered** only after a real video file exists. It may be labelled **QA-passed** only after the listed checks have been performed and recorded. It may be labelled **published** only after a public platform URL and publication timestamp are captured. Payment and revenue require separate transaction evidence. A merged documentation PR does not satisfy any of these media, publication, or revenue gates.
