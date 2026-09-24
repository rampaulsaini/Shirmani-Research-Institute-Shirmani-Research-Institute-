import "dotenv/config";
import express from "express";
import cors from "cors";
import rateLimit from "express-rate-limit";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import pg from "pg";

const { Pool } = pg;
const app = express();
const port = Number(process.env.PORT || 8787);
const origin = process.env.CORS_ORIGIN || "*";
const secret = process.env.JWT_SECRET;
const pool = process.env.DATABASE_URL ? new Pool({ connectionString: process.env.DATABASE_URL }) : null;

app.use(cors({ origin }));
app.use(express.json({ limit: "1mb" }));
app.use(rateLimit({ windowMs: 60_000, limit: 120, standardHeaders: true, legacyHeaders: false }));
app.use((_req, res, next) => { res.setHeader("Cache-Control", "no-store"); next(); });

const dbRequired = (_req, res, next) => {
  if (!pool) return res.status(503).json({ error: "DATABASE_NOT_CONFIGURED" });
  next();
};
const auth = (req, res, next) => {
  if (!secret) return res.status(503).json({ error: "JWT_SECRET_NOT_CONFIGURED" });
  const header = req.headers.authorization || "";
  if (!header.startsWith("Bearer ")) return res.status(401).json({ error: "AUTH_REQUIRED" });
  try { req.user = jwt.verify(header.slice(7), secret); next(); }
  catch { res.status(401).json({ error: "INVALID_TOKEN" }); }
};

app.get("/health", async (_req, res) => {
  let database = "NOT_CONFIGURED";
  if (pool) { try { await pool.query("select 1"); database = "READY"; } catch { database = "ERROR"; } }
  res.json({ service: "shirmani-social-api", status: "READY", database, auth: secret ? "CONFIGURED" : "NOT_CONFIGURED", generated_at: new Date().toISOString() });
});

app.post("/v1/auth/register", dbRequired, async (req, res) => {
  const { email, password, display_name = "", bio = "", language = "हिंदी" } = req.body || {};
  if (typeof email !== "string" || !/^\S+@\S+\.\S+$/.test(email) || typeof password !== "string" || password.length < 12 || password.length > 200) return res.status(400).json({ error: "INVALID_REGISTRATION" });
  if (!secret) return res.status(503).json({ error: "JWT_SECRET_NOT_CONFIGURED" });
  const normalized = email.trim().toLowerCase();
  const hash = await bcrypt.hash(password, 12);
  try {
    const client = await pool.connect();
    try {
      await client.query("begin");
      const account = await client.query("insert into accounts(email, password_hash) values($1,$2) returning id,email,created_at", [normalized, hash]);
      const profile = await client.query("insert into profiles(id,display_name,bio,language) values($1,$2,$3,$4) returning id,display_name,bio,language,created_at,updated_at", [account.rows[0].id, String(display_name).slice(0,80), String(bio).slice(0,1000), String(language).slice(0,32)]);
      await client.query("commit");
      const token = jwt.sign({ sub: account.rows[0].id }, secret, { expiresIn: "7d", issuer: "shirmani-social-api" });
      res.status(201).json({ token, account: account.rows[0], profile: profile.rows[0] });
    } catch (e) { await client.query("rollback"); if (e.code === "23505") return res.status(409).json({ error: "EMAIL_ALREADY_REGISTERED" }); throw e; }
    finally { client.release(); }
  } catch { res.status(500).json({ error: "REGISTRATION_FAILED" }); }
});

app.post("/v1/auth/login", dbRequired, async (req, res) => {
  const { email, password } = req.body || {};
  if (typeof email !== "string" || typeof password !== "string") return res.status(400).json({ error: "INVALID_LOGIN" });
  if (!secret) return res.status(503).json({ error: "JWT_SECRET_NOT_CONFIGURED" });
  const { rows } = await pool.query("select id,email,password_hash from accounts where email=$1", [email.trim().toLowerCase()]);
  if (!rows[0] || !(await bcrypt.compare(password, rows[0].password_hash))) return res.status(401).json({ error: "INVALID_CREDENTIALS" });
  const token = jwt.sign({ sub: rows[0].id }, secret, { expiresIn: "7d", issuer: "shirmani-social-api" });
  res.json({ token, account: { id: rows[0].id, email: rows[0].email } });
});

app.get("/v1/profile/:id", dbRequired, async (req, res) => {
  const { rows } = await pool.query("select id, display_name, bio, language, created_at, updated_at from profiles where id=$1", [req.params.id]);
  if (!rows[0]) return res.status(404).json({ error: "PROFILE_NOT_FOUND" });
  res.json(rows[0]);
});

app.get("/v1/feed", dbRequired, async (_req, res) => {
  const { rows } = await pool.query("select p.id,p.author_id,pr.display_name,p.text,p.type,p.created_at from posts p join profiles pr on pr.id=p.author_id order by p.created_at desc limit 50");
  res.json({ items: rows });
});

app.post("/v1/posts", dbRequired, auth, async (req, res) => {
  const { text, type = "विचार" } = req.body || {};
  if (typeof text !== "string" || !text.trim() || text.length > 5000) return res.status(400).json({ error: "INVALID_POST" });
  const { rows } = await pool.query("insert into posts(author_id,text,type) values($1,$2,$3) returning id,author_id,text,type,created_at", [req.user.sub, text.trim(), String(type).slice(0,32)]);
  res.status(201).json(rows[0]);
});

app.post("/v1/self-interviews", dbRequired, auth, async (req, res) => {
  const { question, answer } = req.body || {};
  if (typeof question !== "string" || !question.trim() || typeof answer !== "string" || !answer.trim() || answer.length > 5000) return res.status(400).json({ error: "INVALID_SELF_INTERVIEW" });
  const { rows } = await pool.query("insert into self_interviews(profile_id,question,answer) values($1,$2,$3) returning id,profile_id,question,answer,created_at", [req.user.sub, question.trim(), answer.trim()]);
  res.status(201).json(rows[0]);
});

app.use((_req, res) => res.status(404).json({ error: "NOT_FOUND" }));
app.listen(port, () => console.log(`shirmani-social-api listening on :${port}`));
