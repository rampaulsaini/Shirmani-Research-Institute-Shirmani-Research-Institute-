'use strict';
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'social-content-manifest.json'), 'utf8'));
if (!Array.isArray(manifest.stories)) throw new Error('stories must be an array');
const errors = [];
for (const item of manifest.stories) {
  const file = path.join(root, item.path);
  if (!fs.existsSync(file)) { errors.push(item.story_id + ': story file missing'); continue; }
  const story = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (story.story_id !== item.story_id) errors.push(item.story_id + ': ID mismatch');
  if (story.language !== 'hi') errors.push(item.story_id + ': first MVP requires Hindi');
  if (!story.title || !Array.isArray(story.scenes) || story.scenes.length < 1) errors.push(item.story_id + ': title/scenes missing');
  for (const scene of story.scenes || []) {
    if (!scene.visual || !scene.narration || !scene.onscreen_caption) errors.push(item.story_id + ': incomplete scene ' + scene.scene);
  }
  if (!story.publication || story.publication.state !== 'NOT_PUBLISHED') errors.push(item.story_id + ': publication state must remain NOT_PUBLISHED until platform proof is supplied');
  if ((story.publication.proof_urls || []).length || (story.publication.provider_receipts || []).length) {
    if (!story.publication.verified_by_human) errors.push(item.story_id + ': publication proof requires human verification');
  }
}
if (errors.length) { console.error(errors.join('\\n')); process.exit(1); }
console.log(JSON.stringify({mode:'VALIDATION_ONLY',stories:manifest.stories.length,valid:true,external_publication:'NOT_ATTEMPTED'}, null, 2));
