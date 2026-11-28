/**
 * Storage adapter contract for private service evidence.
 *
 * Production implementations must be server-side, private by default, durable,
 * and independently tested for provider ACLs and retention. This module only
 * validates the adapter shape; it does not make an adapter production-safe.
 *
 * @typedef {Object} EvidenceStorageAdapter
 * @property {(input: {bytes: Buffer|Uint8Array, contentType: string, ownerId: string, orderId: string}) => Promise<{key: string, sha256: string, byteLength: number, contentType: string}>} put
 * @property {(input: {key: string, ownerId: string, orderId: string}) => Promise<{bytes: Buffer, sha256: string, byteLength: number, contentType: string, ownerId: string, orderId: string}>} get
 * @property {(input: {key: string, ownerId: string, orderId: string}) => Promise<{deleted: true}>} delete
 * @property {() => Promise<void>} close
 */

/**
 * Fail fast when an adapter does not implement the minimum storage interface.
 * This is deliberately a shape check, not a security or durability certification.
 * @param {unknown} adapter
 * @returns {EvidenceStorageAdapter}
 */
export function assertEvidenceStorageAdapter(adapter) {
  const methods = ["put", "get", "delete", "close"];
  if (!adapter || typeof adapter !== "object" ||
      methods.some(method => typeof adapter[method] !== "function")) {
    throw new TypeError("EVIDENCE_STORAGE_ADAPTER_INVALID");
  }
  return adapter;
}
