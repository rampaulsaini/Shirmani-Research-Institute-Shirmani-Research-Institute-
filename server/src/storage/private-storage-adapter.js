import { createHash } from "node:crypto";

export const DEFAULT_MAX_OBJECT_BYTES = 10 * 1024 * 1024;
export const DEFAULT_MAX_READ_GRANT_SECONDS = 300;

const ALLOWED_MIME_TYPES = new Set([
  "image/jpeg",
  "image/png",
  "image/webp",
  "audio/mpeg",
  "audio/wav",
  "video/mp4",
  "application/pdf",
  "text/plain"
]);

const REQUIRED_PROVIDER_METHODS = [
  "putObject",
  "headObject",
  "getObject",
  "deleteObject",
  "createReadGrant"
];

function validateKey(key) {
  if (typeof key !== "string" || key.length < 1 || key.length > 500 ||
      key.startsWith("/") || key.includes("\\") ||
      !/^[A-Za-z0-9][A-Za-z0-9/_-]*$/.test(key) ||
      key.split("/").some(segment => !segment || segment === "." || segment === "..")) {
    throw new TypeError("INVALID_STORAGE_KEY");
  }
}

function validateBody(body, maxBytes) {
  if (!Buffer.isBuffer(body) && !(body instanceof Uint8Array)) {
    throw new TypeError("INVALID_OBJECT_BODY");
  }
  if (body.byteLength < 1 || body.byteLength > maxBytes) {
    throw new RangeError("OBJECT_SIZE_OUT_OF_RANGE");
  }
  return Buffer.from(body);
}

function validateMimeType(mimeType) {
  if (typeof mimeType !== "string" || !ALLOWED_MIME_TYPES.has(mimeType)) {
    throw new TypeError("UNSUPPORTED_MIME_TYPE");
  }
}

export function createPrivateStorageAdapter({
  provider,
  authorize,
  maxObjectBytes = DEFAULT_MAX_OBJECT_BYTES,
  maxReadGrantSeconds = DEFAULT_MAX_READ_GRANT_SECONDS,
  now = () => Date.now()
} = {}) {
  if (!provider || REQUIRED_PROVIDER_METHODS.some(method => typeof provider[method] !== "function")) {
    throw new TypeError("INVALID_STORAGE_PROVIDER");
  }
  if (typeof authorize !== "function") throw new TypeError("AUTHORIZATION_CALLBACK_REQUIRED");
  if (!Number.isSafeInteger(maxObjectBytes) || maxObjectBytes < 1) throw new RangeError("INVALID_MAX_OBJECT_BYTES");
  if (!Number.isSafeInteger(maxReadGrantSeconds) || maxReadGrantSeconds < 1 || maxReadGrantSeconds > 3600) {
    throw new RangeError("INVALID_MAX_READ_GRANT_SECONDS");
  }

  const assertAuthorized = async (actorId, key, action) => {
    validateKey(key);
    if (typeof actorId !== "string" || !actorId.trim() ||
        await authorize({ actorId, key, action }) !== true) {
      const error = new Error("STORAGE_ACCESS_DENIED");
      error.code = "STORAGE_ACCESS_DENIED";
      throw error;
    }
  };

  return Object.freeze({
    async putObject({ key, body, mimeType, ownerId } = {}) {
      await assertAuthorized(ownerId, key, "write");
      validateMimeType(mimeType);
      if (typeof ownerId !== "string" || !ownerId.trim()) throw new TypeError("OWNER_ID_REQUIRED");
      const bytes = validateBody(body, maxObjectBytes);
      const metadata = Object.freeze({
        ownerId,
        mimeType,
        byteSize: bytes.byteLength,
        sha256: createHash("sha256").update(bytes).digest("hex")
      });
      await provider.putObject({ key, body: bytes, mimeType, metadata, private: true, ifAbsent: true });
      return Object.freeze({ key, ...metadata, storage: "private" });
    },

    async headObject({ key, actorId } = {}) {
      await assertAuthorized(actorId, key, "read_metadata");
      return provider.headObject({ key });
    },

    async getObject({ key, actorId } = {}) {
      await assertAuthorized(actorId, key, "read");
      return provider.getObject({ key });
    },

    async deleteObject({ key, actorId } = {}) {
      await assertAuthorized(actorId, key, "delete");
      return provider.deleteObject({ key });
    },

    async createReadGrant({ key, actorId, expiresInSeconds = 60 } = {}) {
      await assertAuthorized(actorId, key, "create_read_grant");
      if (!Number.isSafeInteger(expiresInSeconds) || expiresInSeconds < 1 ||
          expiresInSeconds > maxReadGrantSeconds) {
        throw new RangeError("READ_GRANT_TTL_OUT_OF_RANGE");
      }
      const grant = await provider.createReadGrant({ key, expiresInSeconds });
      const nowSeconds = Math.floor(now() / 1000);
      if (!grant || typeof grant.url !== "string" || !grant.url.startsWith("https://") ||
          !Number.isSafeInteger(grant.expiresAt) ||
          grant.expiresAt <= nowSeconds ||
          grant.expiresAt > nowSeconds + expiresInSeconds) {
        throw new Error("INVALID_PROVIDER_READ_GRANT");
      }
      return Object.freeze({ url: grant.url, expiresAt: grant.expiresAt, access: "temporary_bearer_grant" });
    }
  });
}
