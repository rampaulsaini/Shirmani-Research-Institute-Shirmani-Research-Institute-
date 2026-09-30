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
const isProduction = process.env.NODE_ENV === "production";
const origin = process.env.CORS_ORIGIN;
const secret = process.env.JWT_SECRET;
const pool = process.env.DATABASE_URL ? new Pool({ connectionString: process.env.DATABASE_URL, max: 10 }) : null;

if (isProduction && (!origin || origin === "*" || !secret || !process.env.DATABASE_URL)) {
  console.error("Production startup requires CORS_ORIGIN, JWT_SECRET and DATABASE_URL.");
  process.exit(1);
}

app.use(cors({ origin: origin || "*" }));
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
  try { req.user = jwt.verify(header.slice(7), secret, { issuer: "shirmani-social-api" }); next(); }
  catch { res.status(401).json({ error: "INVALID_TOKEN" }); }
};

app.get("/health", async (_req, res) => {
  let database = "NOT_CONFIGURED";
  if (pool) { try { await pool.query("select 1"); database = "READY"; } catch { database = "ERROR"; } }
  const status = database === "READY" && secret ? "READY" : "DEGRADED";
  res.status(status === "READY" ? 200 : 503).json({ service: "shirmani-social-api", status, database, auth: secret ? "CONFIGURED" : "NOT_CONFIGURED", generated_at: new Date().toISOString() });
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

app.patch("/v1/profile/:id", dbRequired, auth, async (req, res) => {
  if (req.params.id !== req.user.sub) return res.status(403).json({ error: "PROFILE_OWNERSHIP_REQUIRED" });
  const { display_name = "", bio = "", language = "हिंदी" } = req.body || {};
  if (typeof display_name !== "string" || display_name.length > 80 || typeof bio !== "string" || bio.length > 1000 || typeof language !== "string" || language.length > 32) return res.status(400).json({ error: "INVALID_PROFILE" });
  const { rows } = await pool.query("update profiles set display_name=$1,bio=$2,language=$3,updated_at=now() where id=$4 returning id,display_name,bio,language,created_at,updated_at", [display_name.trim(), bio.trim(), language.trim(), req.user.sub]);
  if (!rows[0]) return res.status(404).json({ error: "PROFILE_NOT_FOUND" });
  res.json(rows[0]);
});

app.get("/v1/self-interviews", dbRequired, auth, async (req, res) => {
  const { rows } = await pool.query("select id,profile_id,question,answer,created_at from self_interviews where profile_id=$1 order by created_at desc limit 100", [req.user.sub]);
  res.json({ items: rows });
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

app.get("/v1/account/export", dbRequired, auth, async (req, res) => {
  const account = await pool.query("select id,email,created_at from accounts where id=$1", [req.user.sub]);
  if (!account.rows[0]) return res.status(404).json({ error: "ACCOUNT_NOT_FOUND" });
  const profile = await pool.query("select id,display_name,bio,language,created_at,updated_at from profiles where id=$1", [req.user.sub]);
  const posts = await pool.query("select id,text,type,created_at from posts where author_id=$1 order by created_at desc", [req.user.sub]);
  const interviews = await pool.query("select id,question,answer,created_at from self_interviews where profile_id=$1 order by created_at desc", [req.user.sub]);
  const listings = await pool.query("select id,kind,title,description,price_minor,currency,status,created_at from marketplace_listings where owner_id=$1 order by created_at desc", [req.user.sub]);
  res.json({ account: account.rows[0], profile: profile.rows[0] || null, posts: posts.rows, self_interviews: interviews.rows, marketplace_listings: listings.rows, exported_at: new Date().toISOString() });
});

app.delete("/v1/account", dbRequired, auth, async (req, res) => {
  const { password } = req.body || {};
  if (typeof password !== "string" || !password) return res.status(400).json({ error: "PASSWORD_CONFIRMATION_REQUIRED" });
  const { rows } = await pool.query("select id,password_hash from accounts where id=$1", [req.user.sub]);
  if (!rows[0]) return res.status(404).json({ error: "ACCOUNT_NOT_FOUND" });
  if (!(await bcrypt.compare(password, rows[0].password_hash))) return res.status(401).json({ error: "INVALID_PASSWORD" });
  await pool.query("delete from accounts where id=$1", [req.user.sub]);
  res.status(204).end();
});

app.get("/v1/marketplace/listings", dbRequired, async (req, res) => {
  const kind = typeof req.query.kind === "string" ? req.query.kind.slice(0,32) : null;
  const params = []; let where = "";
  if (kind) { params.push(kind); where = " where l.kind=$1"; }
  const { rows } = await pool.query(`select l.id,l.owner_id,p.display_name,l.kind,l.title,l.description,l.price_minor,l.currency,l.status,l.created_at from marketplace_listings l join profiles p on p.id=l.owner_id${where} order by l.created_at desc limit 100`, params);
  res.json({items: rows});
});

app.post("/v1/marketplace/listings", dbRequired, auth, async (req, res) => {
  const { kind, title, description = "", price_minor = 0, currency = "INR" } = req.body || {};
  const allowed = new Set(["product","service","course","music","audio","job"]);
  if (!allowed.has(kind) || typeof title !== "string" || !title.trim() || title.length > 160 || typeof description !== "string" || description.length > 5000 || !Number.isInteger(price_minor) || price_minor < 0 || price_minor > 1000000000 || typeof currency !== "string" || !/^[A-Z]{3}$/.test(currency)) return res.status(400).json({error:"INVALID_LISTING"});
  const { rows } = await pool.query("insert into marketplace_listings(owner_id,kind,title,description,price_minor,currency) values($1,$2,$3,$4,$5,$6) returning id,owner_id,kind,title,description,price_minor,currency,status,created_at", [req.user.sub,kind,title.trim(),description,price_minor,currency]);
  res.status(201).json(rows[0]);
});

app.post("/v1/ai-tasks", dbRequired, auth, async (req, res) => {
  const { task_type, input = {} } = req.body || {};
  if (typeof task_type !== "string" || !task_type.trim() || task_type.length > 64 || typeof input !== "object" || input === null || Array.isArray(input)) return res.status(400).json({ error: "INVALID_AI_TASK" });
  const { rows } = await pool.query("insert into ai_tasks(owner_id,task_type,input) values($1,$2,$3) returning id,task_type,status,created_at,updated_at", [req.user.sub, task_type.trim(), input]);
  res.status(202).json(rows[0]);
});

app.post("/v1/reports", dbRequired, auth, async (req, res) => {
  const { target_type, target_id, reason, details = "" } = req.body || {};
  if (typeof target_type !== "string" || !target_type.trim() || typeof target_id !== "string" || !target_id.trim() || typeof reason !== "string" || !reason.trim() || reason.length > 100 || typeof details !== "string" || details.length > 3000) return res.status(400).json({ error: "INVALID_REPORT" });
  const { rows } = await pool.query("insert into reports(reporter_id,target_type,target_id,reason,details) values($1,$2,$3,$4,$5) returning id,target_type,target_id,reason,details,status,created_at", [req.user.sub, target_type.trim().slice(0,32), target_id, reason.trim(), details]);
  res.status(201).json(rows[0]);
});

app.get("/v1/ai-tasks/:id", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,task_type,status,result,created_at,updated_at from ai_tasks where id=$1 and owner_id=$2",[req.params.id,req.user.sub]);
  if(!rows[0]) return res.status(404).json({error:"AI_TASK_NOT_FOUND"});
  res.json(rows[0]);
});

app.post("/v1/marketplace/listings/:id/publish", dbRequired, auth, async (req, res) => {
  const { rows } = await pool.query("update marketplace_listings set status='published' where id=$1 and owner_id=$2 returning id,status,created_at", [req.params.id, req.user.sub]);
  if (!rows[0]) return res.status(404).json({ error: "LISTING_NOT_FOUND" });
  res.json(rows[0]);
});

app.post("/v1/marketplace/listings/:id/pause", dbRequired, auth, async (req, res) => {
  const { rows } = await pool.query("update marketplace_listings set status='paused' where id=$1 and owner_id=$2 returning id,status", [req.params.id, req.user.sub]);
  if (!rows[0]) return res.status(404).json({ error: "LISTING_NOT_FOUND" });
  res.json(rows[0]);
});

app.post("/v1/marketplace/listings/:id/archive", dbRequired, auth, async (req, res) => {
  const { rows } = await pool.query("update marketplace_listings set status='archived' where id=$1 and owner_id=$2 returning id,status", [req.params.id, req.user.sub]);
  if (!rows[0]) return res.status(404).json({ error: "LISTING_NOT_FOUND" });
  res.json(rows[0]);
});

app.get("/v1/audit-events", dbRequired, auth, async (req, res) => {
  const { rows } = await pool.query("select id,event_type,target_type,target_id,metadata,created_at from audit_events where actor_id=$1 order by created_at desc limit 100", [req.user.sub]);
  res.json({ items: rows });
});

app.get("/v1/marketplace/transactions", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,buyer_id,seller_id,listing_id,amount_minor,currency,status,provider,provider_reference,created_at,updated_at from transactions where buyer_id=$1 or seller_id=$1 order by created_at desc limit 100",[req.user.sub]);
  res.json({items:rows});
});

app.use((_req, res) => res.status(404).json({ error: "NOT_FOUND" }));
app.listen(port, () => console.log(`shirmani-social-api listening on :${port}`));
