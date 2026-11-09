import "dotenv/config";
import express from "express";
import cors from "cors";
import rateLimit from "express-rate-limit";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import pg from "pg";
import { governancePolicy } from "./governance-policy.js";

const { Pool } = pg;
const app = express();
const port = Number(process.env.PORT || 8787);
const isProduction = process.env.NODE_ENV === "production";
const origin = process.env.CORS_ORIGIN;
const allowedOrigins = new Set((origin || "").split(",").map(value => value.trim()).filter(value => value && value !== "*"));
const secret = process.env.JWT_SECRET;
const ownerEmail = (process.env.OWNER_EMAIL || "").trim().toLowerCase();
const pool = process.env.DATABASE_URL ? new Pool({ connectionString: process.env.DATABASE_URL, max: 10 }) : null;

const missingProductionConfig = [
  !allowedOrigins.size ? "CORS_ORIGIN" : null,
  !secret ? "JWT_SECRET" : null,
  !process.env.DATABASE_URL ? "DATABASE_URL" : null
].filter(Boolean);

if (isProduction && missingProductionConfig.length) {
  // Keep the process available for diagnostics; protected routes remain fail-closed.
  // Never invent credentials or database connection strings.
  console.error("Production configuration incomplete:", missingProductionConfig.join(", "));
}

// In production, only explicitly configured origins receive CORS access.
// A missing or wildcard production origin never opens cross-origin access.
app.use(cors({
  origin: (requestOrigin, callback) => {
    if (!requestOrigin) return callback(null, true);
    if (allowedOrigins.has(requestOrigin)) return callback(null, true);
    if (!isProduction && !origin) return callback(null, true);
    return callback(null, false);
  }
}));
// Render terminates TLS and forwards one trusted proxy hop to this web service.
app.set("trust proxy", 1);
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

// Private lead access is restricted to one explicitly configured owner account.
// Fail closed when the owner identity has not been configured by the deployment.
const ownerOnly = async (req, res, next) => {
  const ownerAccountId = process.env.OWNER_ACCOUNT_ID;
  if (ownerAccountId && req.user?.sub === ownerAccountId) return next();
  if (!ownerEmail) {
    return res.status(ownerAccountId ? 403 : 503).json({ error: ownerAccountId ? "OWNER_ACCESS_REQUIRED" : "OWNER_IDENTITY_NOT_CONFIGURED" });
  }
  try {
    const { rows } = await pool.query("select lower(email) as email from accounts where id=$1", [req.user.sub]);
    if (rows[0]?.email !== ownerEmail) return res.status(403).json({ error: "OWNER_ACCESS_REQUIRED" });
    return next();
  } catch {
    return res.status(503).json({ error: "OWNER_IDENTITY_LOOKUP_FAILED" });
  }
};

app.get("/health", async (_req, res) => {
  let database = "NOT_CONFIGURED";
  if (pool) { try { await pool.query("select 1"); database = "READY"; } catch { database = "ERROR"; } }
  const status = database === "READY" && secret ? "READY" : "DEGRADED";
  res.status(status === "READY" ? 200 : 503).json({ service: "shirmani-social-api", status, database, auth: secret ? "CONFIGURED" : "NOT_CONFIGURED", generated_at: new Date().toISOString() });
});

// Public client enquiries are leads only: they do not create orders or payment records.
const enquiryLimiter = rateLimit({ windowMs: 15 * 60_000, limit: 8, standardHeaders: true, legacyHeaders: false });
app.post("/v1/enquiries", dbRequired, enquiryLimiter, async (req, res) => {
  const body = req.body || {};
  const clean = (value, max) => typeof value === "string" ? value.trim().slice(0, max) : "";
  const name = clean(body.name, 120);
  const email = clean(body.email, 254).toLowerCase();
  const phone = clean(body.phone, 32);
  const service = clean(body.service, 80);
  const language = clean(body.language, 32);
  const topic = clean(body.topic, 180);
  const goal = clean(body.goal, 500);
  const wordCount = clean(body.word_count, 40);
  const deadline = clean(body.deadline, 100);
  const budget = clean(body.budget, 80);
  const sources = clean(body.sources, 1500);
  const notes = clean(body.notes, 1500);
  const honeypot = clean(body.website, 200);

  if (honeypot) return res.status(400).json({ error: "INVALID_ENQUIRY" });
  if (!service || !topic || !["Hindi", "English", "Hindi + English", "To be agreed"].includes(language)) {
    return res.status(400).json({ error: "INVALID_ENQUIRY" });
  }
  if (body.consent !== true) return res.status(400).json({ error: "CONSENT_REQUIRED" });
  if ((!email && !phone) || (email && !/^\S+@\S+\.\S+$/.test(email)) ||
      (phone && !/^[+0-9() .-]{7,32}$/.test(phone))) {
    return res.status(400).json({ error: "VALID_CONTACT_REQUIRED" });
  }
  if (typeof body.name !== "undefined" && typeof body.name !== "string" ||
      typeof body.service !== "string" || body.service.length > 80 ||
      typeof body.topic !== "string" || body.topic.length > 180 ||
      typeof body.goal !== "undefined" && typeof body.goal !== "string" ||
      typeof body.sources !== "undefined" && typeof body.sources !== "string" ||
      typeof body.notes !== "undefined" && typeof body.notes !== "string") {
    return res.status(400).json({ error: "INVALID_ENQUIRY" });
  }

  try {
    const { rows } = await pool.query(
      "insert into client_enquiries(name,email,phone,service,language,topic,goal,word_count,deadline,budget,sources,notes,consent_at) values($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,now()) returning id,status,created_at",
      [name, email || null, phone || null, service, language, topic, goal, wordCount, deadline, budget, sources, notes]
    );
    res.status(201).json({ ...rows[0], message: "Enquiry received for human review. No order or payment has been created." });
  } catch {
    res.status(500).json({ error: "ENQUIRY_SAVE_FAILED" });
  }
});

// Private owner inbox: never expose customer contact details to ordinary accounts.
app.get("/v1/owner/enquiries", dbRequired, auth, ownerOnly, async (req, res) => {
  const requestedLimit = Number.parseInt(req.query.limit, 10);
  const limit = Number.isInteger(requestedLimit) ? Math.min(100, Math.max(1, requestedLimit)) : 50;
  try {
    const { rows } = await pool.query(
      "select id,name,email,phone,service,language,topic,goal,word_count,deadline,budget,sources,notes,status,consent_at,created_at,updated_at from client_enquiries order by created_at desc limit $1",
      [limit]
    );
    res.json({ items: rows, count: rows.length, access: "owner_only" });
  } catch {
    res.status(500).json({ error: "ENQUIRY_INBOX_READ_FAILED" });
  }
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

app.get("/v1/capabilities/status", (_req, res) => {
  res.json({
    status_model: ["PLANNED","ARCHITECTURE","MVP","TESTED","DEPLOYMENT_GATED","LIVE","AUTOMATED","INDEPENDENTLY_VERIFIED"],
    capabilities: [
      { id: "identity", status: "ARCHITECTURE" },
      { id: "social", status: "MVP" },
      { id: "research", status: "MVP" },
      { id: "education", status: "ARCHITECTURE" },
      { id: "ai", status: "ARCHITECTURE" },
      { id: "ai-music", status: "ARCHITECTURE" },
      { id: "digital-store", status: "MVP" },
      { id: "freelancing", status: "MVP" },
      { id: "employment", status: "ARCHITECTURE" },
      { id: "business", status: "ARCHITECTURE" },
      { id: "economy", status: "ARCHITECTURE" },
      { id: "yatharth-mudra", status: "ARCHITECTURE" },
      { id: "yatharth-justice", status: "ARCHITECTURE" },
      { id: "trust", status: "MVP" },
      { id: "verification", status: "DEPLOYMENT_GATED" },
      { id: "nature-humanity", status: "ARCHITECTURE" },
      { id: "platform-operations", status: "TESTED" }
    ],
    truth_boundary: {
      ci_success_is_not_production_availability: true,
      workflow_completion_is_not_truth_verification: true,
      author_testimony_is_not_independent_verification: true,
      conceptual_currency_design_is_not_legal_currency: true
    },
    generated_at: new Date().toISOString()
  });
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



// Public-platform social/work/learning primitives.
// These endpoints operate only on records represented by the database schema.
app.post("/v1/users/:id/follow", dbRequired, auth, async (req,res)=>{
  if(req.params.id===req.user.sub) return res.status(400).json({error:"SELF_FOLLOW_NOT_ALLOWED"});
  const {rows}=await pool.query("insert into follows(follower_id,followed_id) values($1,$2) on conflict do nothing returning follower_id,followed_id,created_at",[req.user.sub,req.params.id]);
  if(!rows[0]) return res.status(200).json({following:true});
  res.status(201).json({following:true,...rows[0]});
});
app.delete("/v1/users/:id/follow", dbRequired, auth, async (req,res)=>{
  await pool.query("delete from follows where follower_id=$1 and followed_id=$2",[req.user.sub,req.params.id]);
  res.status(204).end();
});
app.get("/v1/users/:id/followers", dbRequired, async (req,res)=>{
  const {rows}=await pool.query("select f.follower_id as id,p.display_name from follows f join profiles p on p.id=f.follower_id where f.followed_id=$1 order by f.created_at desc limit 100",[req.params.id]);
  res.json({items:rows});
});
app.get("/v1/users/:id/following", dbRequired, async (req,res)=>{
  const {rows}=await pool.query("select f.followed_id as id,p.display_name from follows f join profiles p on p.id=f.followed_id where f.follower_id=$1 order by f.created_at desc limit 100",[req.params.id]);
  res.json({items:rows});
});

app.get("/v1/posts/:id/comments", dbRequired, async (req,res)=>{
  const {rows}=await pool.query("select c.id,c.author_id,p.display_name,c.text,c.created_at from comments c join profiles p on p.id=c.author_id where c.post_id=$1 order by c.created_at asc limit 200",[req.params.id]);
  res.json({items:rows});
});
app.post("/v1/posts/:id/comments", dbRequired, auth, async (req,res)=>{
  const {text}=req.body||{};
  if(typeof text!=="string"||!text.trim()||text.length>2000) return res.status(400).json({error:"INVALID_COMMENT"});
  const {rows}=await pool.query("insert into comments(post_id,author_id,text) values($1,$2,$3) returning id,post_id,author_id,text,created_at",[req.params.id,req.user.sub,text.trim()]);
  res.status(201).json(rows[0]);
});
app.put("/v1/posts/:id/reaction", dbRequired, auth, async (req,res)=>{
  const {reaction="like"}=req.body||{};
  if(typeof reaction!=="string"||!/^[a-z0-9_-]{1,32}$/i.test(reaction)) return res.status(400).json({error:"INVALID_REACTION"});
  const {rows}=await pool.query("insert into reactions(post_id,user_id,reaction) values($1,$2,$3) on conflict(post_id,user_id) do update set reaction=excluded.reaction returning post_id,user_id,reaction,created_at",[req.params.id,req.user.sub,reaction]);
  res.json(rows[0]);
});
app.delete("/v1/posts/:id/reaction", dbRequired, auth, async (req,res)=>{
  await pool.query("delete from reactions where post_id=$1 and user_id=$2",[req.params.id,req.user.sub]);
  res.status(204).end();
});

app.get("/v1/notifications", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,actor_id,kind,target_type,target_id,payload,read_at,created_at from notifications where recipient_id=$1 order by created_at desc limit 100",[req.user.sub]);
  res.json({items:rows});
});
app.post("/v1/notifications/:id/read", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("update notifications set read_at=coalesce(read_at,now()) where id=$1 and recipient_id=$2 returning id,read_at",[req.params.id,req.user.sub]);
  if(!rows[0]) return res.status(404).json({error:"NOTIFICATION_NOT_FOUND"});
  res.json(rows[0]);
});

app.post("/v1/courses/:listingId/enroll", dbRequired, auth, async (req,res)=>{
  const listing=await pool.query("select id,owner_id,kind,status from marketplace_listings where id=$1",[req.params.listingId]);
  if(!listing.rows[0]||listing.rows[0].kind!=="course"||listing.rows[0].status!=="published") return res.status(404).json({error:"COURSE_NOT_AVAILABLE"});
  if(listing.rows[0].owner_id===req.user.sub) return res.status(400).json({error:"OWNER_ENROLLMENT_NOT_ALLOWED"});
  const {rows}=await pool.query("insert into course_enrollments(course_listing_id,learner_id) values($1,$2) on conflict do nothing returning id,course_listing_id,learner_id,status,created_at",[req.params.listingId,req.user.sub]);
  if(!rows[0]) return res.status(200).json({enrolled:true});
  res.status(201).json({enrolled:true,...rows[0]});
});
app.get("/v1/courses/enrollments", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select e.id,e.course_listing_id,l.title,e.status,e.created_at from course_enrollments e join marketplace_listings l on l.id=e.course_listing_id where e.learner_id=$1 order by e.created_at desc limit 100",[req.user.sub]);
  res.json({items:rows});
});

app.post("/v1/work-orders", dbRequired, auth, async (req,res)=>{
  const {listing_id,worker_id=null}=req.body||{};
  if(typeof listing_id!=="string") return res.status(400).json({error:"INVALID_WORK_ORDER"});
  const listing=await pool.query("select id,owner_id,kind,status from marketplace_listings where id=$1",[listing_id]);
  if(!listing.rows[0]||!["service","job"].includes(listing.rows[0].kind)||listing.rows[0].status!=="published") return res.status(404).json({error:"WORK_LISTING_NOT_AVAILABLE"});
  if(listing.rows[0].owner_id===req.user.sub) return res.status(400).json({error:"OWNER_WORK_ORDER_NOT_ALLOWED"});
  const {rows}=await pool.query("insert into work_orders(listing_id,client_id,worker_id) values($1,$2,$3) returning id,listing_id,client_id,worker_id,status,created_at,updated_at",[listing_id,req.user.sub,worker_id]);
  res.status(201).json(rows[0]);
});
app.get("/v1/work-orders", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,listing_id,client_id,worker_id,status,created_at,updated_at from work_orders where client_id=$1 or worker_id=$1 order by created_at desc limit 100",[req.user.sub]);
  res.json({items:rows});
});
app.post("/v1/work-orders/:id/status", dbRequired, auth, async (req,res)=>{
  const allowed=new Set(["accepted","in_progress","delivered","completed","cancelled","disputed"]);
  const {status}=req.body||{};
  if(!allowed.has(status)) return res.status(400).json({error:"INVALID_WORK_STATUS"});
  const {rows}=await pool.query("update work_orders set status=$1,updated_at=now() where id=$2 and (client_id=$3 or worker_id=$3) returning id,status,updated_at",[status,req.params.id,req.user.sub]);
  if(!rows[0]) return res.status(404).json({error:"WORK_ORDER_NOT_FOUND"});
  res.json(rows[0]);
});

app.post("/v1/disputes", dbRequired, auth, async (req,res)=>{
  const {target_type,target_id,reason}=req.body||{};
  if(typeof target_type!=="string"||!target_type.trim()||typeof target_id!=="string"||!target_id.trim()||typeof reason!=="string"||!reason.trim()||reason.length>3000) return res.status(400).json({error:"INVALID_DISPUTE"});
  const {rows}=await pool.query("insert into disputes(opened_by,target_type,target_id,reason) values($1,$2,$3,$4) returning id,target_type,target_id,reason,status,created_at",[req.user.sub,target_type.trim().slice(0,64),target_id.trim(),reason.trim()]);
  res.status(201).json(rows[0]);
});
app.get("/v1/disputes", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,target_type,target_id,reason,status,resolution,created_at,updated_at from disputes where opened_by=$1 order by created_at desc limit 100",[req.user.sub]);
  res.json({items:rows});
});

app.get("/v1/verification-reviews/:claimId", dbRequired, async (req,res)=>{
  const {rows}=await pool.query("select id,claim_id,reviewer_type,reviewer_reference,evidence,decision,notes,created_at from verification_reviews where claim_id=$1 order by created_at desc limit 100",[req.params.claimId]);
  res.json({items:rows});
});



// Marketplace checkout/order lifecycle (record-only until a real payment provider is configured).
app.post("/v1/marketplace/orders", dbRequired, auth, async (req,res)=>{
  const {listing_id, quantity=1}=req.body||{};
  if(typeof listing_id!=="string"||!Number.isInteger(quantity)||quantity<1||quantity>100) return res.status(400).json({error:"INVALID_ORDER"});
  const {rows}=await pool.query("select id,owner_id,kind,title,price_minor,currency,status from marketplace_listings where id=$1",[listing_id]);
  const listing=rows[0];
  if(!listing||listing.status!=="published") return res.status(404).json({error:"LISTING_NOT_AVAILABLE"});
  if(listing.owner_id===req.user.sub) return res.status(400).json({error:"OWNER_ORDER_NOT_ALLOWED"});
  const total=listing.price_minor*quantity;
  if(!Number.isSafeInteger(total)) return res.status(400).json({error:"ORDER_TOTAL_TOO_LARGE"});
  const order=await pool.query("insert into orders(buyer_id,seller_id,listing_id,quantity,unit_amount_minor,total_amount_minor,currency,status) values($1,$2,$3,$4,$5,$6,$7,'intent') returning id,buyer_id,seller_id,listing_id,quantity,unit_amount_minor,total_amount_minor,currency,status,created_at,updated_at",[req.user.sub,listing.owner_id,listing.id,quantity,listing.price_minor,total,listing.currency]);
  await pool.query("insert into audit_events(actor_id,event_type,target_type,target_id,metadata) values($1,'marketplace_order_created','order',$2,$3)",[req.user.sub,order.rows[0].id,{listing_id,quantity}]);
  res.status(201).json({...order.rows[0],listing_title:listing.title,listing_kind:listing.kind,payment_state:"NOT_PAID"});
});

app.get("/v1/marketplace/orders", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select o.id,o.buyer_id,o.seller_id,o.listing_id,o.quantity,o.unit_amount_minor,o.total_amount_minor,o.currency,o.status,o.provider,o.provider_reference,o.created_at,o.updated_at from orders o where o.buyer_id=$1 or o.seller_id=$1 order by o.created_at desc limit 100",[req.user.sub]);
  res.json({items:rows});
});

app.post("/v1/marketplace/orders/:id/cancel", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("update orders set status='cancelled',updated_at=now() where id=$1 and (buyer_id=$2 or seller_id=$2) and status in ('intent','pending') returning id,status,updated_at",[req.params.id,req.user.sub]);
  if(!rows[0]) return res.status(404).json({error:"ORDER_NOT_CANCELLABLE"});
  res.json(rows[0]);
});

// Seller/creator dashboard aggregates owned listings, orders and work.
app.get("/v1/dashboard", dbRequired, auth, async (req,res)=>{
  const [listings,orders,work,learning,ai,reports]=await Promise.all([
    pool.query("select count(*)::int as total,count(*) filter(where status='published')::int as published from marketplace_listings where owner_id=$1",[req.user.sub]),
    pool.query("select count(*)::int as total,count(*) filter(where status in ('paid','fulfilled','completed'))::int as completed,sum(case when status='paid' then total_amount_minor else 0 end)::bigint as paid_amount_minor from orders where buyer_id=$1 or seller_id=$1",[req.user.sub]),
    pool.query("select count(*)::int as total,count(*) filter(where status='completed')::int as completed from work_orders where client_id=$1 or worker_id=$1",[req.user.sub]),
    pool.query("select count(*)::int as total,count(*) filter(where status='completed')::int as completed from course_enrollments where learner_id=$1",[req.user.sub]),
    pool.query("select count(*)::int as total,count(*) filter(where status='completed')::int as completed,count(*) filter(where status='failed')::int as failed from ai_tasks where owner_id=$1",[req.user.sub]),
    pool.query("select count(*)::int as total,count(*) filter(where status='open')::int as open from reports where reporter_id=$1",[req.user.sub])
  ]);
  res.json({listings:listings.rows[0],orders:orders.rows[0],work_orders:work.rows[0],learning:learning.rows[0],ai_tasks:ai.rows[0],reports:reports.rows[0],income_note:"Recorded order/payment fields are not proof of real payment, income, delivery or customer satisfaction."});
});

// Privacy, media metadata and bounded Automission control-plane endpoints.
app.get("/v1/ai-agents", dbRequired, auth, async (_req,res)=>{
  const {rows}=await pool.query("select id,agent_key,display_name,scope,status,requires_human_review,created_at,updated_at from ai_agents order by agent_key");
  res.json({items:rows});
});
// Bounded Automission lifecycle: queue/dispatch/retry/cancel are auditable state transitions.
// These routes never mark research claims as verified and do not execute arbitrary code.
app.post("/v1/ai-tasks/:id/dispatch", dbRequired, auth, async (req,res)=>{
  const {agent_key}=req.body||{};
  if(typeof agent_key!=="string"||!agent_key.trim()) return res.status(400).json({error:"AGENT_REQUIRED"});
  const agent=await pool.query("select id,agent_key,status,requires_human_review from ai_agents where agent_key=$1",[agent_key.trim()]);
  if(!agent.rows[0]||agent.rows[0].status!=="enabled") return res.status(404).json({error:"AGENT_NOT_AVAILABLE"});
  const client=await pool.connect();
  try{
    await client.query("begin");
    const task=await client.query("select id,status from ai_tasks where id=$1 and owner_id=$2 for update",[req.params.id,req.user.sub]);
    if(!task.rows[0]){await client.query("rollback");return res.status(404).json({error:"AI_TASK_NOT_FOUND"});}
    if(!["queued","failed"].includes(task.rows[0].status)){await client.query("rollback");return res.status(409).json({error:"AI_TASK_NOT_DISPATCHABLE"});}
    await client.query("update ai_tasks set status='running',updated_at=now() where id=$1",[req.params.id]);
    await client.query("insert into ai_task_events(task_id,agent_id,event_type,payload) values($1,$2,'dispatched',$3)",[req.params.id,agent.rows[0].id,{agent_key:agent.rows[0].agent_key,requires_human_review:agent.rows[0].requires_human_review}]);
    await client.query("commit");
    res.status(202).json({id:req.params.id,status:"running",agent_key:agent.rows[0].agent_key,requires_human_review:agent.rows[0].requires_human_review});
  }catch(e){await client.query("rollback");res.status(500).json({error:"AI_TASK_DISPATCH_FAILED"});}finally{client.release();}
});
app.post("/v1/ai-tasks/:id/retry", dbRequired, auth, async (req,res)=>{
  const client=await pool.connect();
  try{
    await client.query("begin");
    const task=await client.query("select id,status from ai_tasks where id=$1 and owner_id=$2 for update",[req.params.id,req.user.sub]);
    if(!task.rows[0]){await client.query("rollback");return res.status(404).json({error:"AI_TASK_NOT_FOUND"});}
    if(task.rows[0].status!=="failed"){await client.query("rollback");return res.status(409).json({error:"AI_TASK_NOT_RETRYABLE"});}
    await client.query("update ai_tasks set status='queued',result=null,updated_at=now() where id=$1",[req.params.id]);
    await client.query("insert into ai_task_events(task_id,event_type,payload) values($1,'retry_requested',$2)",[req.params.id,{requested_by:req.user.sub}]);
    await client.query("commit");
    res.status(202).json({id:req.params.id,status:"queued"});
  }catch(e){await client.query("rollback");res.status(500).json({error:"AI_TASK_RETRY_FAILED"});}finally{client.release();}
});
app.post("/v1/ai-tasks/:id/cancel", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("update ai_tasks set status='cancelled',updated_at=now() where id=$1 and owner_id=$2 and status in ('queued','running') returning id,status,updated_at",[req.params.id,req.user.sub]);
  if(!rows[0]) return res.status(404).json({error:"AI_TASK_NOT_CANCELLABLE"});
  await pool.query("insert into ai_task_events(task_id,event_type,payload) values($1,'cancelled',$2)",[req.params.id,{requested_by:req.user.sub}]);
  res.json(rows[0]);
});

app.get("/v1/ai-tasks/:id/events", dbRequired, auth, async (req,res)=>{
  const task=await pool.query("select id from ai_tasks where id=$1 and owner_id=$2",[req.params.id,req.user.sub]);
  if(!task.rows[0]) return res.status(404).json({error:"AI_TASK_NOT_FOUND"});
  const {rows}=await pool.query("select e.id,e.event_type,e.payload,e.created_at,a.agent_key from ai_task_events e left join ai_agents a on a.id=e.agent_id where e.task_id=$1 order by e.created_at asc",[req.params.id]);
  res.json({items:rows});
});
app.post("/v1/privacy-requests", dbRequired, auth, async (req,res)=>{
  const {request_type,details=""}=req.body||{};
  if(!["export","delete","correction"].includes(request_type)||typeof details!=="string"||details.length>3000) return res.status(400).json({error:"INVALID_PRIVACY_REQUEST"});
  const {rows}=await pool.query("insert into privacy_requests(account_id,request_type,details) values($1,$2,$3) returning id,request_type,status,details,created_at",[req.user.sub,request_type,details]);
  res.status(202).json(rows[0]);
});
app.get("/v1/privacy-requests/:id", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,request_type,status,details,created_at,completed_at from privacy_requests where id=$1 and account_id=$2",[req.params.id,req.user.sub]);
  if(!rows[0]) return res.status(404).json({error:"PRIVACY_REQUEST_NOT_FOUND"});
  res.json(rows[0]);
});
app.get("/v1/privacy-requests", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,request_type,status,details,created_at,completed_at from privacy_requests where account_id=$1 order by created_at desc limit 50",[req.user.sub]);
  res.json({items:rows});
});
app.post("/v1/media-assets", dbRequired, auth, async (req,res)=>{
  const {media_type,storage_key,mime_type,byte_size}=req.body||{};
  if(!["image","video","audio","document"].includes(media_type)||typeof storage_key!=="string"||!storage_key.trim()||storage_key.length>500||typeof mime_type!=="string"||mime_type.length>120||!Number.isInteger(byte_size)||byte_size<0) return res.status(400).json({error:"INVALID_MEDIA_METADATA"});
  const {rows}=await pool.query("insert into media_assets(owner_id,media_type,storage_key,mime_type,byte_size) values($1,$2,$3,$4,$5) returning id,media_type,mime_type,byte_size,status,created_at",[req.user.sub,media_type,storage_key.trim(),mime_type.trim(),byte_size]);
  res.status(201).json({...rows[0],storage_note:"Binary storage is external; metadata does not imply a publicly accessible file."});
});
app.get("/v1/media-assets", dbRequired, auth, async (req,res)=>{
  const {rows}=await pool.query("select id,media_type,mime_type,byte_size,status,created_at from media_assets where owner_id=$1 order by created_at desc limit 100",[req.user.sub]);
  res.json({items:rows});
});

// Payment webhooks are deliberately fail-closed until a provider-specific adapter
// verifies the provider's signed raw payload, amount, currency, order mapping and
// event idempotency. A shared static header secret is not sufficient evidence.
app.post("/v1/payments/webhook", dbRequired, async (_req, res) => {
  return res.status(503).json({
    error: "PAYMENT_PROVIDER_ADAPTER_NOT_CONFIGURED",
    message: "No payment event can mark an order as paid until a provider-specific verifier and idempotency ledger are deployed."
  });
});

// Public operational safety endpoints. These expose readiness facts without claiming global availability.
app.get("/v1/governance/policy", (_req, res) => {
  res.json({
    ...governancePolicy(),
    generated_at: new Date().toISOString()
  });
});

app.get("/v1/platform/readiness", async (_req, res) => {
  const databaseConfigured = Boolean(process.env.DATABASE_URL);
  const authConfigured = Boolean(process.env.JWT_SECRET);
  const corsConfigured = Boolean(process.env.CORS_ORIGIN && process.env.CORS_ORIGIN !== "*");
  const ownerInboxConfigured = Boolean(process.env.OWNER_ACCOUNT_ID || ownerEmail);
  let database = databaseConfigured ? "CONFIGURED" : "DATABASE_NOT_CONFIGURED";
  if (pool) {
    try { await pool.query("select 1"); database = "READY"; }
    catch { database = "ERROR"; }
  }
  // A database-backed enquiry form is not operational for the owner until
  // the private inbox identity is configured. Keep this as a readiness gate,
  // not a startup crash, so diagnostics remain available while configuring.
  const ready = database === "READY" && authConfigured && corsConfigured && ownerInboxConfigured;
  res.status(ready ? 200 : 503).json({
    status: ready ? "READY_FOR_DEPLOYMENT_CHECKS" : "BLOCKED",
    checks: {
      database,
      auth: authConfigured ? "CONFIGURED" : "JWT_SECRET_NOT_CONFIGURED",
      cors: corsConfigured ? "CONFIGURED" : "NOT_CONFIGURED_OR_WILDCARD",
      owner_inbox: ownerInboxConfigured ? "CONFIGURED" : "OWNER_ACCOUNT_ID_NOT_CONFIGURED"
    },
    production_live: false,
    independent_verification: false
  });
});

// Backward-compatible enquiry endpoints for the simple public enquiry form.
// The canonical record remains client_enquiries; no payment/order is created here.
app.get("/api/init-db", dbRequired, async (_req, res) => {
  try {
    const { rows } = await pool.query("select to_regclass('public.client_enquiries') is not null as ready");
    if (!rows[0]?.ready) return res.status(503).json({ success: false, message: "Enquiry schema is not installed; apply the versioned database migrations." });
    return res.json({ success: true, message: "Table Ready", table: "client_enquiries", schema_management: "versioned migrations" });
  } catch {
    return res.status(503).json({ success: false, message: "Database unavailable" });
  }
});

app.post("/api/enquiry", dbRequired, enquiryLimiter, async (req, res) => {
  const body = req.body || {};
  const clean = (value, max) => typeof value === "string" ? value.trim().slice(0, max) : "";
  const name = clean(body.name, 120);
  const mobile = clean(body.mobile, 32);
  const service = clean(body.service, 80);
  if (body.consent !== true) return res.status(400).json({ error: "CONSENT_REQUIRED", message: "सहमति अनिवार्य" });
  if (!name || !mobile || !/^[+0-9() .-]{7,32}$/.test(mobile) || !service) {
    return res.status(400).json({ error: "INVALID_ENQUIRY", message: "नाम, वैध मोबाइल और सेवा आवश्यक हैं।" });
  }
  try {
    const { rows } = await pool.query(
      "insert into client_enquiries(name,email,phone,service,language,topic,goal,word_count,deadline,budget,sources,notes,consent_at) values($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,now()) returning id,status,created_at",
      [name, null, mobile, service, "To be agreed", service, "Legacy public enquiry form", "", "", "", "", ""]
    );
    console.info("PUBLIC_ENQUIRY_RECEIVED", JSON.stringify({ id: rows[0].id, notification: "OWNER_INBOX_ONLY_EMAIL_DELIVERY_NOT_CONFIGURED" }));
    return res.status(201).json({ success: true, id: rows[0].id, status: rows[0].status, owner_notification: "NOT_CONFIGURED", payment: "PENDING", income: "₹0", message: "Enquiry saved for owner review. No order or payment was created." });
  } catch {
    return res.status(500).json({ error: "ENQUIRY_SAVE_FAILED" });
  }
});

// Liveness: a running process returns 200 without querying external dependencies.
app.get("/api/health", (_req, res) => {
  return res.status(200).json({
    live: true,
    service: "shirmani-social-api",
    commit: process.env.RENDER_GIT_COMMIT || "runtime-commit-unavailable",
    generated_at: new Date().toISOString()
  });
});

// Readiness: only return 200 when the real database and required security config work.
app.get("/api/ready", async (_req, res) => {
  const corsConfigured = allowedOrigins.size > 0;
  const checks = {
    database: "NOT_CONFIGURED",
    jwt: secret ? "CONFIGURED" : "JWT_SECRET_NOT_CONFIGURED",
    cors: corsConfigured ? "CONFIGURED" : "NOT_CONFIGURED_OR_WILDCARD"
  };
  if (pool) {
    try { await pool.query("select 1"); checks.database = "READY"; }
    catch { checks.database = "ERROR"; }
  }
  const ready = checks.database === "READY" && checks.jwt === "CONFIGURED" && checks.cors === "CONFIGURED";
  return res.status(ready ? 200 : 503).json({
    ready,
    status: ready ? "READY" : "BLOCKED",
    checks,
    generated_at: new Date().toISOString()
  });
});

// Aggregate public status is separate from process liveness. It exposes counts only;
// verified income requires a consented, verified payment-proof row in INR.
app.get("/api/status", async (_req, res) => {
  let database = "NOT_CONFIGURED";
  const tables = { client_enquiries: "NOT_CHECKED", paid_orders: "NOT_CHECKED" };
  const counters = { enquiries: null, paid_orders: null, income_inr_minor: null };

  if (pool) {
    try {
      await pool.query("select 1");
      database = "READY";
    } catch {
      database = "ERROR";
    }
  }

  if (database === "READY") {
    try {
      const result = await pool.query("select to_regclass('public.client_enquiries') is not null as ready");
      if (result.rows[0]?.ready) {
        tables.client_enquiries = "READY";
        const enquiries = await pool.query("select count(*)::int as count from client_enquiries");
        counters.enquiries = enquiries.rows[0].count;
      } else {
        tables.client_enquiries = "MISSING";
      }
    } catch {
      tables.client_enquiries = "ERROR";
    }

    try {
      const result = await pool.query("select to_regclass('public.paid_orders') is not null as ready");
      if (result.rows[0]?.ready) {
        tables.paid_orders = "READY";
        const paid = await pool.query("select count(*)::int as count, coalesce(sum(amount_minor),0)::bigint as income_inr_minor from paid_orders where verification_status='verified' and customer_consent=true and currency='INR'");
        counters.paid_orders = paid.rows[0].count;
        counters.income_inr_minor = String(paid.rows[0].income_inr_minor);
      } else {
        tables.paid_orders = "MISSING";
      }
    } catch {
      tables.paid_orders = "ERROR";
    }
  }

  const income = counters.income_inr_minor === null
    ? "UNAVAILABLE"
    : "₹" + (Number(counters.income_inr_minor) / 100).toFixed(2);
  return res.status(database === "READY" ? 200 : 503).json({
    service: "shirmani-social-api",
    database,
    tables,
    counters,
    payment: "PENDING_UNLESS_VERIFIED_CONSENTED_PAYMENT_PROOF_EXISTS",
    income,
    generated_at: new Date().toISOString()
  });
});

const csvCell = (value) => {
  let text = value === null || value === undefined ? "" : String(value);
  if (/^[\s]*[=+\-@]/.test(text)) text = "'" + text;
  return '"' + text.replace(/"/g, '""') + '"';
};
const sendCsv = (res, filename, columns, rows) => {
  const body = [columns.map(csvCell).join(","), ...rows.map(row => columns.map(key => csvCell(row[key])).join(","))].join("\r\n");
  res.setHeader("Content-Type", "text/csv; charset=utf-8");
  res.setHeader("Content-Disposition", 'attachment; filename="' + filename + '"');
  res.setHeader("Cache-Control", "private, no-store, max-age=0");
  return res.status(200).send("\uFEFF" + body);
};

app.get("/api/export-enquiries", dbRequired, auth, ownerOnly, async (_req, res) => {
  try {
    const { rows } = await pool.query("select id,name,email,phone,service,language,topic,goal,word_count,deadline,budget,sources,notes,status,consent_at,created_at,updated_at from client_enquiries order by created_at asc");
    return sendCsv(res, "enquiries.csv", ["id","name","email","phone","service","language","topic","goal","word_count","deadline","budget","sources","notes","status","consent_at","created_at","updated_at"], rows);
  } catch { return res.status(503).json({ error: "ENQUIRY_EXPORT_UNAVAILABLE" }); }
});

app.get("/api/export-income", dbRequired, auth, ownerOnly, async (req, res) => {
  try {
    const { rows } = await pool.query("select id,order_id,amount_minor,currency,payment_id,upi_ref,screenshot_url,customer_consent,verification_status,verification_method,verified_at,created_at from paid_orders where verification_status='verified' and customer_consent=true order by verified_at asc");
    const totalMinor = rows.reduce((sum, row) => sum + BigInt(row.amount_minor), 0n);
    const totalInr = (totalMinor / 100n).toString() + "." + (totalMinor % 100n).toString().padStart(2, "0");
    const report = { status: rows.length ? "AVAILABLE" : "UNAVAILABLE", currency: "INR", verified_paid_orders: rows.length, total_minor_units: totalMinor.toString(), total_inr: totalInr, verification_basis: "owner_attested_bank_match_or_provider_verified", generated_at: new Date().toISOString(), records: rows };
    res.setHeader("Cache-Control", "private, no-store, max-age=0");
    if (req.query.format === "csv") return sendCsv(res, "income.csv", ["id","order_id","amount_minor","currency","payment_id","upi_ref","screenshot_url","customer_consent","verification_status","verification_method","verified_at","created_at"], rows);
    return res.status(200).json(report);
  } catch { return res.status(503).json({ status: "UNAVAILABLE", error: "INCOME_EXPORT_UNAVAILABLE", records: [] }); }
});

app.post("/api/owner/orders/:orderId/payment-proof", dbRequired, auth, ownerOnly, async (req, res) => {
  const body = req.body || {};
  const clean = value => typeof value === "string" ? value.trim() : "";
  const paymentId = clean(body.payment_id), upiRef = clean(body.upi_ref), screenshotUrl = clean(body.screenshot_url);
  if (!paymentId || paymentId.length > 200 || !upiRef || upiRef.length > 200 ||
      !/^private:\/\/[A-Za-z0-9/_-]{1,960}$/.test(screenshotUrl) || body.customer_consent !== true) {
    return res.status(400).json({ error: "ALL_PAYMENT_PROOFS_AND_CUSTOMER_CONSENT_REQUIRED" });
  }
  try {
    const order = await pool.query("select id,total_amount_minor,currency,status from orders where id=$1", [req.params.orderId]);
    if (!order.rows[0]) return res.status(404).json({ error: "ORDER_NOT_FOUND" });
    if (["refunded","cancelled"].includes(order.rows[0].status)) return res.status(409).json({ error: "ORDER_NOT_ELIGIBLE_FOR_PAYMENT_PROOF" });
    const { rows } = await pool.query("insert into paid_orders(order_id,amount_minor,currency,payment_id,upi_ref,screenshot_url,customer_consent,verification_status) values($1,$2,$3,$4,$5,$6,true,'pending') returning id,order_id,amount_minor,currency,verification_status,created_at", [order.rows[0].id, order.rows[0].total_amount_minor, order.rows[0].currency, paymentId, upiRef, screenshotUrl]);
    return res.status(201).json({ ...rows[0], income: "UNAVAILABLE_PENDING_VERIFICATION", note: "Evidence recorded; this is not yet verified income." });
  } catch (error) {
    if (error?.code === "23505") return res.status(409).json({ error: "PAYMENT_PROOF_ALREADY_RECORDED" });
    return res.status(503).json({ error: "PAYMENT_PROOF_SAVE_FAILED" });
  }
});

app.post("/api/owner/payment-proofs/:proofId/verify", dbRequired, auth, ownerOnly, async (req, res) => {
  if (req.body?.confirm_bank_match !== true) return res.status(400).json({ error: "BANK_MATCH_CONFIRMATION_REQUIRED" });
  try {
    const { rows } = await pool.query("update paid_orders set verification_status='verified',verification_method='owner_bank_statement',verified_by=$1,verified_at=now() where id=$2 and verification_status='pending' and customer_consent=true returning id,order_id,amount_minor,currency,verification_status,verification_method,verified_at", [req.user.sub, req.params.proofId]);
    if (!rows[0]) return res.status(404).json({ error: "PENDING_PAYMENT_PROOF_NOT_FOUND" });
    return res.json({ ...rows[0], verification_scope: "owner_attested_bank_match_not_independent_audit" });
  } catch { return res.status(503).json({ error: "PAYMENT_PROOF_VERIFICATION_FAILED" }); }
});

// Public Yatharth Genesis registry check. This proves only the database reservation row,
// not ownership of a wallet, token issuance, funds, legal-tender status, or exchange operation.
const verifyYatharthAccount = async (req, res) => {
  const accountId = String(req.params.accountId || "").trim();
  if (!/^YTH-[0-9]{10}$/.test(accountId)) {
    return res.status(400).json({ error: "INVALID_YATHARTH_ACCOUNT_ID" });
  }
  try {
    const { rows } = await pool.query(
      "select account_id, status, proof_hash, created_at from yatharth_accounts where account_id=$1",
      [accountId]
    );
    if (!rows[0]) {
      return res.status(404).json({ account_id: accountId, status: "NOT_FOUND", verified: false });
    }
    const verified = rows[0].status === "RESERVED_PERMANENT" &&
      rows[0].proof_hash === "GENESIS-2026-11-06-001";
    return res.status(200).json({
      account_id: rows[0].account_id,
      status: rows[0].status,
      verified,
      verification_scope: "database_reservation_record_only",
      created_at: rows[0].created_at
    });
  } catch (error) {
    if (error?.code === "42P01") {
      return res.status(503).json({ error: "YATHARTH_REGISTRY_NOT_MIGRATED", verified: false });
    }
    return res.status(503).json({ error: "YATHARTH_VERIFICATION_UNAVAILABLE", verified: false });
  }
};

app.get("/api/yatharth/verify/:accountId", dbRequired, verifyYatharthAccount);
app.get("/verify/:accountId", dbRequired, verifyYatharthAccount);

app.use((_req, res) => res.status(404).json({ error: "NOT_FOUND" }));
app.listen(port, () => console.log(`shirmani-social-api listening on :${port}`));
