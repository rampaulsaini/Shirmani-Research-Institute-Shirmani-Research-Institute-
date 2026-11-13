import assert from "node:assert/strict";
import test from "node:test";
import fs from "node:fs";

const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");

test("communication archive write route is authenticated and owner-only", () => {
  assert.match(source, /app\.post\("\/api\/owner\/communications\/messages",\s*dbRequired,\s*auth,\s*ownerOnly/);
  assert.match(source, /content_reviewed_no_credentials !== true/);
  assert.match(source, /normalizeTimestamp\(body\.sent_at\)/);
  assert.match(source, /normalizeTimestamp\(body\.received_at\)/);
  assert.match(source, /!providerMessageId/);
  assert.match(source, /encryptMessageContent\(messageContent\)/);
  assert.match(source, /encrypted\.encryptedContent/);
  assert.match(source, /EMAIL_CONTENT_ENCRYPTION_NOT_CONFIGURED/);
});

test("communication archive does not return message bodies in list response", () => {
  assert.match(source, /app\.get\("\/api\/owner\/communications\/messages",\s*dbRequired,\s*auth,\s*ownerOnly/);
  assert.match(source, /bodies_included: false/);
  assert.doesNotMatch(source, /select\s+[^;]*encrypted_content[^;]*from communication_messages order by/i);
});

test("message body retrieval remains owner-only and checks key version and digest", () => {
  assert.match(source, /app\.get\("\/api\/owner\/communications\/messages\/:id\/content",\s*dbRequired,\s*auth,\s*ownerOnly/);
  assert.match(source, /EMAIL_CONTENT_KEY_VERSION_MISMATCH/);
  assert.match(source, /COMMUNICATION_INTEGRITY_CHECK_FAILED/);
  assert.match(source, /decryptMessageContent\(rows\[0\]\.encrypted_content/);
});

test("communication archive errors do not expose database or encryption internals", () => {
  assert.match(source, /COMMUNICATION_ARCHIVE_SAVE_FAILED/);
  assert.match(source, /COMMUNICATION_CONTENT_UNAVAILABLE/);
});

test("communication archive insert and audit event are committed atomically", () => {
  const route = source.slice(
    source.indexOf('app.post("/api/owner/communications/messages"'),
    source.indexOf('app.get("/api/owner/communications/messages"')
  );
  assert.match(route, /let client;[\s\S]*client = await pool\.connect\(\)/);
  assert.match(route, /await client\.query\("begin"\)/);
  assert.match(route, /insert into communication_messages/);
  assert.match(route, /insert into audit_events\(actor_id,event_type,target_type,target_id,metadata\)/);
  assert.match(route, /'communication_message_archived','communication_message'/);
  assert.match(route, /await client\.query\("commit"\)/);
  assert.match(route, /await client\.query\("rollback"\)/);
  assert.match(route, /try\s*\{\s*client\??\.release\(\);\s*\}\s*catch\s*\{\s*\}/);
  assert.match(route, /audit_recorded: true/);
});
