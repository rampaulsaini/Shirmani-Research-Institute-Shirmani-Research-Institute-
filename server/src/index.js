import "dotenv/config";
import express from "express";
import cors from "cors";
import pg from "pg";

const { Pool } = pg;
const app = express();
const port = Number(process.env.PORT || 8787);
const origin = process.env.CORS_ORIGIN || "*";
const pool = process.env.DATABASE_URL ? new Pool({ connectionString: process.env.DATABASE_URL }) : null;

app.use(cors({ origin }));
app.use(express.json({ limit: "1mb" }));

const noStore = (_req, res, next) => { res.setHeader("Cache-Control", "no-store"); next(); };
app.use(noStore);

app.get("/health", async (_req, res) => {
  let database = "NOT_CONFIGURED";
  if (pool) {
    try { await pool.query("select 1"); database = "READY"; }
    catch { database = "ERROR"; }
  }
  res.json({ service: "shirmani-social-api", status: "READY", database, generated_at: new Date().toISOString() });
});

app.get("/v1/profile/:id", async (req, res) => {
  if (!pool) return res.status(503).json({ error: "DATABASE_NOT_CONFIGURED" });
  const { rows } = await pool.query("select id, display_name, bio, language, created_at, updated_at from profiles where id=$1", [req.params.id]);
  if (!rows[0]) return res.status(404).json({ error: "PROFILE_NOT_FOUND" });
  res.json(rows[0]);
});

app.post("/v1/posts", async (req, res) => {
  if (!pool) return res.status(503).json({ error: "DATABASE_NOT_CONFIGURED" });
  const { author_id, text, type = "विचार" } = req.body || {};
  if (!author_id || typeof text !== "string" || !text.trim() || text.length > 5000) return res.status(400).json({ error: "INVALID_POST" });
  const { rows } = await pool.query("insert into posts(author_id, text, type) values($1,$2,$3) returning id, author_id, text, type, created_at", [author_id, text.trim(), type]);
  res.status(201).json(rows[0]);
});

app.get("/v1/feed", async (_req, res) => {
  if (!pool) return res.status(503).json({ error: "DATABASE_NOT_CONFIGURED" });
  const { rows } = await pool.query("select id, author_id, text, type, created_at from posts order by created_at desc limit 50");
  res.json({ items: rows });
});

app.post("/v1/self-interviews", async (req, res) => {
  if (!pool) return res.status(503).json({ error: "DATABASE_NOT_CONFIGURED" });
  const { profile_id, question, answer } = req.body || {};
  if (!profile_id || typeof question !== "string" || !question.trim() || typeof answer !== "string" || !answer.trim() || answer.length > 5000) return res.status(400).json({ error: "INVALID_SELF_INTERVIEW" });
  const { rows } = await pool.query("insert into self_interviews(profile_id, question, answer) values($1,$2,$3) returning id, profile_id, question, answer, created_at", [profile_id, question.trim(), answer.trim()]);
  res.status(201).json(rows[0]);
});

app.use((_req, res) => res.status(404).json({ error: "NOT_FOUND" }));
app.listen(port, () => console.log(`shirmani-social-api listening on :${port}`));
