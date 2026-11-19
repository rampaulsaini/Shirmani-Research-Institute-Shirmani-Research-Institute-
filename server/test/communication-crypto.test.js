import assert from "node:assert/strict";
import test from "node:test";
import { randomBytes } from "node:crypto";
import { decryptMessageContent, encryptMessageContent } from "../src/communication-crypto.js";

const key = randomBytes(32);
const keyVersion = "test-v1";

test("message content is encrypted and round-trips with matching key version", () => {
  const source = "Confidential customer email — नमस्ते";
  const encrypted = encryptMessageContent(source, { key, keyVersion });
  assert.notEqual(encrypted.encryptedContent.toString("utf8"), source);
  assert.equal(encrypted.contentKeyVersion, keyVersion);
  assert.match(encrypted.contentSha256, /^[0-9a-f]{64}$/);
  const decrypted = decryptMessageContent(encrypted.encryptedContent, { key, keyVersion });
  assert.equal(decrypted.plaintext, source);
  assert.equal(decrypted.contentSha256, encrypted.contentSha256);
});

test("different random nonces produce different ciphertext envelopes", () => {
  const a = encryptMessageContent("same content", { key, keyVersion });
  const b = encryptMessageContent("same content", { key, keyVersion });
  assert.notDeepEqual(a.encryptedContent, b.encryptedContent);
});

test("tampering with ciphertext or authentication tag is rejected", () => {
  const encrypted = encryptMessageContent("do not alter", { key, keyVersion });
  const envelope = JSON.parse(encrypted.encryptedContent.toString("utf8"));
  const data = Buffer.from(envelope.data, "base64");
  data[0] ^= 1;
  envelope.data = data.toString("base64");
  assert.throws(() => decryptMessageContent(Buffer.from(JSON.stringify(envelope)), { key, keyVersion }));
});

test("wrong key and invalid key configuration fail closed", () => {
  const encrypted = encryptMessageContent("private", { key, keyVersion });
  assert.throws(() => decryptMessageContent(encrypted.encryptedContent, { key: randomBytes(32), keyVersion }));
  assert.throws(() => encryptMessageContent("private", { key: Buffer.alloc(16), keyVersion }));
  assert.throws(() => encryptMessageContent("private", { key, keyVersion: "../bad" }));
});

test("invalid envelope and input types are rejected", () => {
  assert.throws(() => encryptMessageContent(Buffer.from("not text"), { key, keyVersion }));
  assert.throws(() => decryptMessageContent(Buffer.from("{broken"), { key, keyVersion }));
  assert.throws(() => decryptMessageContent("not a buffer", { key, keyVersion }));
});
