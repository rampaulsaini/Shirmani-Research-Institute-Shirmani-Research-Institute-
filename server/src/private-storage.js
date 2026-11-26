import { createHash } from "node:crypto";

const DEFAULT_CONTENT_TYPES = new Set([
  "application/pdf",
  "audio/mp4",
  "audio/mpeg",
  "image/jpeg",
  "image/png",
  "text/plain",
  "video/mp4"
]);

const SHA256_PATTERN = /^[a-f0-9]{64}$/;

function storageError(code) {
  const error = new Error(code);
  error.code = code;
  return error;
}

function validateKey(key) {
  if (typeof key !== "string" || key.length < 1 || key.length > 200 ||
      !/^[a-z0-9][a-z0-9/_-]*$/.test(key) ||
      key.split("/").some(part => !part || part === "." || part === "..")) {
    throw storageError("INVALID_PRIVATE_STORAGE_KEY");
  }
  return key;
}

function toBytes(body, maxBytes) {
  if (!Buffer.isBuffer(body) && !(body instanceof Uint8Array)) {
    throw storageError("INVALID_PRIVATE_STORAGE_BODY");
  }
  const bytes = Buffer.from(body);
  if (bytes.length < 1 || bytes.length > maxBytes) {
    throw storageError("PRIVATE_STORAGE_SIZE_OUT_OF_RANGE");
  }
  return bytes;
}

function digest(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

function validateMetadata(metadata, key, allowedContentTypes, maxBytes) {
  if (!metadata || metadata.key !== key ||
      !Number.isSafeInteger(metadata.byteSize) ||
      metadata.byteSize < 1 || metadata.byteSize > maxBytes ||
      !allowedContentTypes.has(metadata.contentType) ||
      typeof metadata.sha256 !== "string" ||
      !SHA256_PATTERN.test(metadata.sha256)) {
    throw storageError("PRIVATE_STORAGE_METADATA_INVALID");
  }
  return {
    key,
    contentType: metadata.contentType,
    byteSize: metadata.byteSize,
    sha256: metadata.sha256
  };
}

/**
 * Provider-neutral private object storage boundary.
 *
 * Adapters implement putObject({ key, body, contentType, sha256 }),
 * headObject(key), getObject(key), and deleteObject(key).
 * Adapter methods must use private storage only and must never return public
 * object URLs. Authentication/authorization belongs in the calling service;
 * this module deliberately exposes no public URL or signed-link operation.
 */
export function createPrivateStorage({
  adapter,
  maxBytes = 10 * 1024 * 1024,
  allowedContentTypes = DEFAULT_CONTENT_TYPES
} = {}) {
  if (!adapter || ["putObject", "headObject", "getObject", "deleteObject"]
    .some(method => typeof adapter[method] !== "function")) {
    throw storageError("PRIVATE_STORAGE_ADAPTER_INCOMPLETE");
  }
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) {
    throw storageError("INVALID_PRIVATE_STORAGE_MAX_BYTES");
  }

  const allowed = new Set(allowedContentTypes);
  if (!allowed.size || [...allowed].some(type => typeof type !== "string" || !/^[a-z0-9.+-]+\/[a-z0-9.+-]+$/.test(type))) {
    throw storageError("INVALID_PRIVATE_STORAGE_CONTENT_TYPES");
  }

  return Object.freeze({
    async put({ key, body, contentType, expectedSha256 } = {}) {
      validateKey(key);
      if (!allowed.has(contentType)) throw storageError("PRIVATE_STORAGE_CONTENT_TYPE_NOT_ALLOWED");
      const bytes = toBytes(body, maxBytes);
      const sha256 = digest(bytes);
      if (expectedSha256 !== undefined &&
          (typeof expectedSha256 !== "string" ||
           !SHA256_PATTERN.test(expectedSha256) ||
           expectedSha256 !== sha256)) {
        throw storageError("PRIVATE_STORAGE_CHECKSUM_MISMATCH");
      }

      await adapter.putObject({ key, body: Buffer.from(bytes), contentType, sha256 });
      const stored = validateMetadata(await adapter.headObject(key), key, allowed, maxBytes);
      if (stored.byteSize !== bytes.length ||
          stored.contentType !== contentType ||
          stored.sha256 !== sha256) {
        throw storageError("PRIVATE_STORAGE_WRITE_VERIFICATION_FAILED");
      }
      return stored;
    },

    async head(key) {
      validateKey(key);
      const metadata = await adapter.headObject(key);
      return metadata === null ? null : validateMetadata(metadata, key, allowed, maxBytes);
    },

    async get(key) {
      validateKey(key);
      const metadata = await this.head(key);
      if (!metadata) return null;
      const object = await adapter.getObject(key);
      if (!object || object.contentType !== metadata.contentType) {
        throw storageError("PRIVATE_STORAGE_READ_METADATA_MISMATCH");
      }
      const body = toBytes(object.body, maxBytes);
      if (body.length !== metadata.byteSize || digest(body) !== metadata.sha256) {
        throw storageError("PRIVATE_STORAGE_READ_CHECKSUM_MISMATCH");
      }
      return { ...metadata, body: Buffer.from(body) };
    },

    async delete(key) {
      validateKey(key);
      const existed = await adapter.headObject(key) !== null;
      if (!existed) return false;
      await adapter.deleteObject(key);
      if (await adapter.headObject(key) !== null) {
        throw storageError("PRIVATE_STORAGE_DELETE_VERIFICATION_FAILED");
      }
      return true;
    }
  });
}
