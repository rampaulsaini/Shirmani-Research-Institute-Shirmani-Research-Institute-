# Hindi Stories Automission — MVP

## First production unit
- Story: `SRI-STORY-001` — **पारदर्शी तराज़ू**
- Language: Hindi (`hi`)
- Source: `content/stories/hi/SRI-STORY-001-paradarshi-tarazu.md`
- Current state: text draft created; editorial review required.
- Images, narration, video, captions and animation have **not** been created.

## Existing integration boundary
`config/social-accounts.json` is a directory of owner-supplied URLs. Its entries are not authenticated platform connections. The existing `supreme-dispatch.yml` and `scripts/auto-dispatch.js` are product-dispatch infrastructure, not a story-media publishing pipeline. Do not route story content through the product dispatch bridge.

## MVP stages
1. Create an original Hindi story draft.
2. Human editorial review and approval.
3. Produce each media asset as a separate artifact with its own QC state.
4. Generate platform-specific captions and accessibility text.
5. Require an explicitly authorized platform connection and destination allow-list.
6. Publish only after explicit approval and successful platform API response.
7. Record the canonical post URL, platform receipt/post ID, timestamp and content hash.

## Evidence states
- `DRAFT_REVIEW_REQUIRED`: story text exists, not approved.
- `ASSET_NOT_CREATED`: media output does not exist.
- `READY_FOR_REVIEW`: content and required assets are present but awaiting human review.
- `APPROVED_FOR_PUBLISH`: human approval recorded for the exact content hash and destination.
- `PUBLISH_ATTEMPTED`: API call attempted; not proof of publication.
- `PUBLISHED`: only with a verifiable platform post URL and platform receipt/post ID.
- `PUBLISH_FAILED`: platform rejected or request failed.

A GitHub Actions green check, generated file, account URL, webhook acceptance, or screenshot of a workflow is not by itself publication evidence. Sales and payment evidence must remain separate.

## Current safeguards
- `config/social-content-manifest.json` starts with `publishing_enabled: false`.
- The first workflow validates metadata only; it does not contact social platforms.
- No credentials, access tokens, passwords or private customer data belong in Git.
- Do not claim that the 16 social accounts are connected. The current registry contains URLs with link-only / not-connected states and includes non-profile links.

## Next implementation gate
After story approval, add media-generation jobs and their artifact QC. Add a publishing adapter only for a platform whose official API, authorization, destination and test receipt have been verified. Keep every platform's publication evidence separate.
