import { createHash } from "node:crypto";

const DEFAULT_MAX_BYTES = 10 * 1024 * 1024;
const ALLOWED_CONTENT_TYPES = new Set([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "text/plain"
]);
const ALLOWED_PURPOSES = new Set([
  "written_acceptance",
  "payment_proof",
  "customer_consent",
  "delivery",
  "customer_acceptance"
]);

const sha256 = value => createHash("sha256").update(value).digest("hex");

export class EvidenceStore {
  constructor(adapter, { maxBytes = DEFAULT_MAX_BYTES } = {}) {
    for (const method of ["put", "head", "get", "delete"]) {
      if (typeof adapter?.[method] !== "function") {
        throw new TypeError(`Evidence storage adapter must implement ${method}()`);
      }
    }
    if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) {
      throw new TypeError("maxBytes must be a positive safe integer");
    }
    this.adapter = adapter;
    this.maxBytes = maxBytes;
  }

  async put({ body, contentType, purpose, uploaderId }) {
    if (!Buffer.isBuffer(body) && !(body instanceof Uint8Array)) {
      throw new TypeError("Evidence body must be a Buffer or Uint8Array");
    }
    const bytes = Buffer.from(body);
    if (!bytes.length || bytes.length > this.maxBytes) {
      throw new RangeError("Evidence size is outside the configured limit");
    }
    if (!ALLOWED_CONTENT_TYPES.has(contentType)) {
      throw new TypeError("Evidence content type is not allowed");
    }
    if (!ALLOWED_PURPOSES.has(purpose)) {
      throw new TypeError("Evidence purpose is not allowed");
    }
    if (typeof uploaderId !== "string" || !uploaderId.trim() || uploaderId.length > 200) {
      throw new TypeError("A valid uploaderId is required");
    }

    const metadata = Object.freeze({
      contentType,
      purpose,
      uploaderId,
      sizeBytes: bytes.length,
      checksumSha256: sha256(bytes)
    });
    const key = await this.adapter.put({ body: bytes, metadata });
    if (typeof key !== "string" || !key.trim() || key.length > 512) {
      throw new TypeError("Storage adapter did not return a valid opaque key");
    }
    return Object.freeze({ key, ...metadata });
  }

  async head(key) {
    this.#assertKey(key);
    const metadata = await this.adapter.head(key);
    if (!metadata) return null;
    return Object.freeze({ ...metadata });
  }

  async get(key) {
    this.#assertKey(key);
    const [metadata, body] = await Promise.all([
      this.adapter.head(key),
      this.adapter.get(key)
    ]);
    if (!metadata || body == null) return null;
    const bytes = Buffer.from(body);
    if (bytes.length !== metadata.sizeBytes || sha256(bytes) !== metadata.checksumSha256) {
      throw new Error("Evidence integrity check failed");
    }
    return Object.freeze({ body: bytes, metadata: Object.freeze({ ...metadata }) });
  }

  async delete(key) {
    this.#assertKey(key);
    return this.adapter.delete(key);
  }

  #assertKey(key) {
    if (typeof key !== "string" || !key.trim() || key.length > 512) {
      throw new TypeError("A valid opaque storage key is required");
    }
  }
}

// Deliberately no production adapter is supplied. A deployment must select,
// review, configure, and test a durable private object store separately.
