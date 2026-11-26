import { createHash, randomUUID } from "node:crypto";

const DEFAULT_ALLOWED_MIME_TYPES = Object.freeze([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "text/plain"
]);
const KEY_PATTERN = /^evidence\/[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

export class PrivateObjectStoreError extends Error {
  constructor(code, message) {
    super(message);
    this.name = "PrivateObjectStoreError";
    this.code = code;
  }
}

const sha256 = bytes => createHash("sha256").update(bytes).digest("hex");

function assertAdapter(adapter) {
  for (const method of ["put", "head", "get", "delete"]) {
    if (typeof adapter?.[method] !== "function") {
      throw new TypeError(`Storage adapter must implement ${method}()`);
    }
  }
}

function assertKey(key) {
  if (typeof key !== "string" || !KEY_PATTERN.test(key)) {
    throw new PrivateObjectStoreError("INVALID_STORAGE_KEY", "Storage key is invalid");
  }
}

function asBytes(value) {
  if (!(Buffer.isBuffer(value) || value instanceof Uint8Array)) {
    throw new PrivateObjectStoreError("INVALID_OBJECT_BODY", "Object body must be bytes");
  }
  return Buffer.from(value);
}

async function requireAuthorization(authorize, metadata, action) {
  if (typeof authorize !== "function") {
    throw new PrivateObjectStoreError("AUTHORIZATION_REQUIRED", "A per-object authorization check is required");
  }
  if (await authorize({ action, metadata }) !== true) {
    throw new PrivateObjectStoreError("FORBIDDEN", "Private object access denied");
  }
}

/**
 * Provider-neutral private object contract.
 *
 * The adapter is deliberately injected. This module does not create buckets,
 * credentials, public URLs, signed URLs, or network connections.
 */
export function createPrivateObjectStore({
  adapter,
  maxBytes = 5 * 1024 * 1024,
  allowedMimeTypes = DEFAULT_ALLOWED_MIME_TYPES
} = {}) {
  assertAdapter(adapter);
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) {
    throw new TypeError("maxBytes must be a positive safe integer");
  }
  const mimeTypes = new Set(allowedMimeTypes);
  if (!mimeTypes.size || [...mimeTypes].some(type => typeof type !== "string" || !/^[\w.+-]+\/[\w.+-]+$/.test(type))) {
    throw new TypeError("allowedMimeTypes must contain valid MIME types");
  }

  async function head(key) {
    assertKey(key);
    const metadata = await adapter.head(key);
    if (!metadata) return null;
    return Object.freeze({
      key,
      contentType: metadata.contentType,
      size: metadata.size,
      sha256: metadata.sha256
    });
  }

  return Object.freeze({
    async put({ body, contentType } = {}) {
      const bytes = asBytes(body);
      if (!mimeTypes.has(contentType)) {
        throw new PrivateObjectStoreError("UNSUPPORTED_CONTENT_TYPE", "Content type is not allowed");
      }
      if (bytes.length < 1 || bytes.length > maxBytes) {
        throw new PrivateObjectStoreError("OBJECT_SIZE_OUT_OF_RANGE", "Object size is outside the allowed range");
      }
      const key = `evidence/${randomUUID()}`;
      const metadata = {
        contentType,
        size: bytes.length,
        sha256: sha256(bytes)
      };
      await adapter.put({ key, body: bytes, ...metadata });
      return Object.freeze({
        locator: `private://${key}`,
        ...metadata
      });
    },

    async head(key) {
      return head(key);
    },

    async get({ key, authorize } = {}) {
      const metadata = await head(key);
      if (!metadata) throw new PrivateObjectStoreError("OBJECT_NOT_FOUND", "Private object not found");
      await requireAuthorization(authorize, metadata, "read");
      const body = asBytes(await adapter.get(key));
      if (body.length !== metadata.size || sha256(body) !== metadata.sha256) {
        throw new PrivateObjectStoreError("OBJECT_INTEGRITY_FAILURE", "Stored object failed integrity verification");
      }
      return Object.freeze({ metadata, body });
    },

    async delete({ key, authorize } = {}) {
      const metadata = await head(key);
      if (!metadata) return false;
      await requireAuthorization(authorize, metadata, "delete");
      await adapter.delete(key);
      return true;
    }
  });
}

/**
 * Process-local fake adapter for tests only. It is not durable storage and
 * must never be selected as a production evidence provider.
 */
export function createMemoryObjectAdapter() {
  const objects = new Map();
  return Object.freeze({
    async put({ key, body, contentType, size, sha256: digest }) {
      if (objects.has(key)) throw new PrivateObjectStoreError("OBJECT_ALREADY_EXISTS", "Object key already exists");
      objects.set(key, {
        body: Buffer.from(body),
        contentType,
        size,
        sha256: digest
      });
    },
    async head(key) {
      const value = objects.get(key);
      if (!value) return null;
      return {
        contentType: value.contentType,
        size: value.size,
        sha256: value.sha256
      };
    },
    async get(key) {
      const value = objects.get(key);
      if (!value) throw new PrivateObjectStoreError("OBJECT_NOT_FOUND", "Private object not found");
      return Buffer.from(value.body);
    },
    async delete(key) {
      objects.delete(key);
    }
  });
}
