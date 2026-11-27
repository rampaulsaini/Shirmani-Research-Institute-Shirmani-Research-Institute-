import { createHash, randomUUID } from "node:crypto";

const DEFAULT_MAX_BYTES = 5 * 1024 * 1024;
const DEFAULT_CONTENT_TYPES = new Set([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "image/webp",
  "text/plain"
]);
const ALLOWED_PURPOSES = new Set([
  "written_acceptance",
  "payment_proof",
  "customer_consent",
  "delivery",
  "customer_acceptance"
]);

const digest = bytes => createHash("sha256").update(bytes).digest("hex");
const validKey = key => typeof key === "string" &&
  /^evidence\/[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/.test(key);

/**
 * Provider-neutral private evidence-store boundary.
 *
 * The injected driver is deliberately not implemented here. A production driver
 * must enforce private access at the storage provider and implement put/head/get/delete.
 * This module never accepts a caller-selected object key and never treats a URI
 * string as evidence that an object exists.
 */
export function createEvidenceStore(driver, {
  maxBytes = DEFAULT_MAX_BYTES,
  allowedContentTypes = DEFAULT_CONTENT_TYPES
} = {}) {
  for (const method of ["put", "head", "get", "delete"]) {
    if (typeof driver?.[method] !== "function") {
      throw new TypeError(`Evidence driver must implement ${method}()`);
    }
  }
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) {
    throw new TypeError("maxBytes must be a positive safe integer");
  }

  return Object.freeze({
    async put(bytes, { contentType, purpose } = {}) {
      if (!Buffer.isBuffer(bytes)) throw new TypeError("Evidence must be supplied as a Buffer");
      if (bytes.length < 1 || bytes.length > maxBytes) throw new RangeError("Evidence size is outside the permitted limit");
      if (!allowedContentTypes.has(contentType)) throw new TypeError("Evidence content type is not allowed");
      if (!ALLOWED_PURPOSES.has(purpose)) throw new TypeError("Evidence purpose is not allowed");

      const key = `evidence/${randomUUID()}`;
      const metadata = Object.freeze({
        key,
        contentType,
        purpose,
        byteSize: bytes.length,
        sha256: digest(bytes),
        createdAt: new Date().toISOString()
      });
      await driver.put(key, Buffer.from(bytes), metadata);
      const stored = await driver.head(key);
      if (!stored || stored.sha256 !== metadata.sha256 || stored.byteSize !== metadata.byteSize) {
        await driver.delete(key).catch(() => {});
        throw new Error("Evidence storage write could not be verified");
      }
      return metadata;
    },

    async head(key) {
      if (!validKey(key)) throw new TypeError("Invalid evidence key");
      const metadata = await driver.head(key);
      if (!metadata) return null;
      if (metadata.key !== key || !Number.isSafeInteger(metadata.byteSize) ||
          typeof metadata.sha256 !== "string" || !/^[a-f0-9]{64}$/.test(metadata.sha256)) {
        throw new Error("Evidence storage metadata is invalid");
      }
      return Object.freeze({ ...metadata });
    },

    async get(key) {
      if (!validKey(key)) throw new TypeError("Invalid evidence key");
      const metadata = await driver.head(key);
      if (!metadata) return null;
      const bytes = await driver.get(key);
      if (!Buffer.isBuffer(bytes) || bytes.length !== metadata.byteSize || digest(bytes) !== metadata.sha256) {
        throw new Error("Evidence checksum or size verification failed");
      }
      return Buffer.from(bytes);
    },

    async delete(key) {
      if (!validKey(key)) throw new TypeError("Invalid evidence key");
      return driver.delete(key);
    }
  });
}
