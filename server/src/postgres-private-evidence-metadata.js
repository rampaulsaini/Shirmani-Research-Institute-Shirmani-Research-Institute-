/**
 * PostgreSQL-backed durable metadata adapter for private evidence.
 * Object bytes remain in a separate private object-storage adapter.
 */
export function createPostgresPrivateMetadataStore(pool) {
  if (!pool || typeof pool.query !== "function") {
    throw new TypeError("POSTGRES_POOL_WITH_QUERY_REQUIRED");
  }

  function mapRow(row) {
    if (!row) return null;
    const byteSize = Number(row.byte_size);
    if (!Number.isSafeInteger(byteSize)) throw new Error("PRIVATE_EVIDENCE_BYTE_SIZE_INVALID");
    return {
      key: row.object_key,
      ownerId: row.owner_id,
      mimeType: row.mime_type,
      byteSize,
      sha256: row.sha256,
      createdAt: new Date(row.created_at).getTime()
    };
  }

  return Object.freeze({
    async get(key) {
      const result = await pool.query(
        `select object_key, owner_id, mime_type, byte_size, sha256, created_at
           from private_evidence_objects where object_key = $1`,
        [key]
      );
      return mapRow(result.rows[0]);
    },

    async put(record) {
      await pool.query(
        `insert into private_evidence_objects
           (object_key, owner_id, mime_type, byte_size, sha256, created_at)
         values ($1, $2, $3, $4, $5, to_timestamp($6 / 1000.0))`,
        [record.key, record.ownerId, record.mimeType, record.byteSize, record.sha256, record.createdAt]
      );
    },

    async delete(key) {
      await pool.query("delete from private_evidence_objects where object_key = $1", [key]);
    },

    async listByOwner(ownerId) {
      const result = await pool.query(
        `select object_key, owner_id, mime_type, byte_size, sha256, created_at
           from private_evidence_objects
          where owner_id = $1
          order by created_at asc, object_key asc`,
        [ownerId]
      );
      return result.rows.map(mapRow);
    }
  });
}
