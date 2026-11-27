import assert from "node:assert/strict";
import { createHash, randomUUID } from "node:crypto";
import test from "node:test";
import {
  DEFAULT_MAX_EVIDENCE_BYTES,
  EVIDENCE_PURPOSES,
  EvidenceStore,
  validateEvidenceMetadata
} from "../src/evidence-store.js";

// Test-only adapter. It deliberately uses process memory and must never be
// configured as production evidence storage.
class FakeMemoryEvidenceStore extends EvidenceStore {
  #objects = new Map();
  #maxBytes;

  constructor(maxBytes = DEFAULT_MAX_EVIDENCE_BYTES) {
    super();
    this.#maxBytes = maxBytes;
  }

  async put(source, inputMetadata) {
    const metadata = validateEvidenceMetadata(inputMetadata, { maxBytes: this.#maxBytes });
    const chunks = [];
    let byteSize = 0;
    const hash = createHash("sha256");

    for await (const chunk of source) {
      if (!(chunk instanceof Uint8Array)) throw new TypeError("EVIDENCE_CHUNK_INVALID");
      byteSize += chunk.byteLength;
      if (byteSize > metadata.maxBytes) throw new RangeError("EVIDENCE_TOO_LARGE");
      const copy = Buffer.from(chunk);
      chunks.push(copy);
      hash.update(copy);
    }
    if (byteSize === 0) throw new TypeError("EVIDENCE_EMPTY");

    const key = randomUUID();
    const record = {
      bytes: Buffer.concat(chunks),
      metadata: {
        purpose: metadata.purpose,
        contentType: metadata.contentType,
        uploaderId: metadata.uploaderId,
        checksumSha256: hash.digest("hex"),
        byteSize
      }
    };
    this.#objects.set(key, record);
    return Object.freeze({ key, ...record.metadata });
  }

  async head(key) {
    const record = this.#objects.get(key);
    return record ? Object.freeze({ key, ...record.metadata }) : null;
  }

  async get(key) {
    const record = this.#objects.get(key);
    if (!record) return null;
    const bytes = Buffer.from(record.bytes);
    return (async function* () { yield bytes; })();
  }

  async delete(key) {
    this.#objects.delete(key);
    return true;
  }
}

async function* chunks(...values) {
  for (const value of values) yield Buffer.from(value);
}

const metadata = {
  purpose: "payment_proof",
  contentType: "application/pdf",
  uploaderId: "test-owner-1"
};

test("evidence metadata allowlists purpose and content type", () => {
  const result = validateEvidenceMetadata(metadata);
  assert.equal(result.purpose, metadata.purpose);
  assert.equal(result.contentType, metadata.contentType);
  assert.equal(result.uploaderId, metadata.uploaderId);
  assert.equal(result.maxBytes, DEFAULT_MAX_EVIDENCE_BYTES);
  assert.deepEqual(EVIDENCE_PURPOSES.includes(result.purpose), true);
  assert.throws(() => validateEvidenceMetadata({ ...metadata, purpose: "arbitrary" }), /EVIDENCE_PURPOSE_INVALID/);
  assert.throws(() => validateEvidenceMetadata({ ...metadata, contentType: "text/html" }), /EVIDENCE_CONTENT_TYPE_NOT_ALLOWED/);
  assert.throws(() => validateEvidenceMetadata({ ...metadata, uploaderId: " " }), /EVIDENCE_UPLOADER_REQUIRED/);
  assert.throws(() => validateEvidenceMetadata(metadata, { maxBytes: 0 }), /EVIDENCE_MAX_BYTES_INVALID/);
});

test("test adapter stores opaque keys, checksum and exact byte metadata", async () => {
  const store = new FakeMemoryEvidenceStore();
  const bytes = Buffer.from("%PDF-1.7 test evidence");
  const stored = await store.put(chunks("%PDF-1.7 ", "test evidence"), metadata);

  assert.match(stored.key, /^[0-9a-f-]{36}$/i);
  assert.equal(stored.byteSize, bytes.length);
  assert.equal(stored.checksumSha256, createHash("sha256").update(bytes).digest("hex"));
  assert.equal(stored.purpose, metadata.purpose);
  assert.equal(stored.contentType, metadata.contentType);

  const head = await store.head(stored.key);
  assert.equal(head.checksumSha256, stored.checksumSha256);
  const retrieved = [];
  for await (const chunk of await store.get(stored.key)) retrieved.push(chunk);
  assert.deepEqual(Buffer.concat(retrieved), bytes);
});

test("test adapter rejects oversize and empty evidence without persisting an object", async () => {
  const store = new FakeMemoryEvidenceStore(4);
  await assert.rejects(
    store.put(chunks("12345"), metadata),
    /EVIDENCE_TOO_LARGE/
  );
  await assert.rejects(store.put(chunks(), metadata), /EVIDENCE_EMPTY/);
});

test("test adapter delete is idempotent and missing objects stay missing", async () => {
  const store = new FakeMemoryEvidenceStore();
  const stored = await store.put(chunks("evidence"), metadata);
  assert.equal(await store.delete(stored.key), true);
  assert.equal(await store.delete(stored.key), true);
  assert.equal(await store.head(stored.key), null);
  assert.equal(await store.get(stored.key), null);
});
