# Hindi Story Automission — MVP

## First production item
- Story: `HI-STORY-0001` — **निष्पक्षता का दीपक**
- Language: Hindi
- Includes: original script, six scene breakdowns, narration text, on-screen captions, short social caption and hashtags.
- Current state: script package ready; rendered video/audio/thumbnail not yet created.

## Pipeline boundaries
1. Author and review the story package.
2. Produce visual scenes, narration, subtitles and platform-specific edits.
3. Run content and rights/safety checks.
4. Route only to accounts whose platform authorization and publishing permissions have been independently confirmed.
5. Record platform post URL/ID and provider receipt as publication evidence.
6. Record analytics, customer enquiries, sales and payments in separate evidence records.

## What this MVP automation does
- Validates the manifest and story package.
- Runs on manual trigger, relevant file changes and a daily schedule.
- Does not call a generative media service, render video/audio, log into social accounts, or publish anything.
- Keeps `publication.state=NOT_PUBLISHED` until external platform evidence is reviewed.

## Why publishing is separate
A GitHub commit or green Actions run proves only that repository content was committed or validated. A saved social URL does not prove account authorization. A dispatch request does not prove a platform post. Do not report reach, sales or payment without platform/provider evidence.

## Run locally
```sh
node scripts/validate-social-stories.js
```

## Next activation gates
- Approve story wording and visual treatment.
- Connect an authorized media-generation/rendering service.
- Verify the specific social account and official publishing API permissions.
- Test against a private destination first; keep external publishing disabled until reviewed.
