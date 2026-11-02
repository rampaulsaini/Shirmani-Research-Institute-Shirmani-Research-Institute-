'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const manifest = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../showroom-products.json'), 'utf8'));
if (!manifest || !Array.isArray(manifest.products)) throw new Error('showroom-products.json must contain a products array');
const enabled = process.env.DISPATCH_ENABLED === 'true';
const webhook = process.env.MAKE_WEBHOOK_URL || '';
let webhookUrl = null;
if (webhook) {
  try {
    webhookUrl = new URL(webhook);
  } catch {
    throw new Error('MAKE_WEBHOOK_URL must be a valid official Make.com webhook URL.');
  }
  const officialHost = webhookUrl.hostname === 'hook.make.com' ||
    /^hook\.[a-z0-9-]+\.make\.com$/i.test(webhookUrl.hostname);
  if (webhookUrl.protocol !== 'https:' || !officialHost ||
      webhookUrl.username || webhookUrl.password ||
      (webhookUrl.port && webhookUrl.port !== '443')) {
    throw new Error('MAKE_WEBHOOK_URL must use HTTPS and an official hook.make.com host.');
  }
}
const limit = Math.max(1, Math.min(Number.parseInt(process.env.DISPATCH_LIMIT || '1', 10) || 1, 10));
const selected = manifest.products.filter(p => p && p.id && p.name &&
  String(p.dispatch || '').toUpperCase() === 'READY_FOR_DISPATCH' &&
  String(p.artifact_evidence || '').toUpperCase() === 'VERIFIED_IN_REPOSITORY' &&
  Number.isFinite(Number(p.price_inr)) && Number(p.price_inr) >= 0 &&
  typeof (p.artifact_url || p.store_url) === 'string').slice(0, limit);
const events = selected.map(p => {
  const version = String(p.version || 'unversioned');
  const key = crypto.createHash('sha256').update([p.id, version].join(':')).digest('hex');
  return {event_type:'showroom.product.dispatch_requested',idempotency_key:key,product:{
    id:p.id,name:p.name,category:p.category||'uncategorized',price_inr:Number(p.price_inr),
    currency:'INR',url:p.artifact_url||p.store_url,description:String(p.description||'').slice(0,1000),version
  },evidence:{artifact_evidence:p.artifact_evidence,qc_gate:p.qc_gate||'UNSPECIFIED',source_manifest:'showroom-products.json'}};
});
async function main(){
 console.log(JSON.stringify({mode:enabled?'ENABLED':'DRY_RUN',manifest_products:manifest.products.length,eligible_products:selected.length,webhook_configured:Boolean(webhook),events:events.map(e=>({id:e.product.id,idempotency_key:e.idempotency_key,name:e.product.name}))},null,2));
 if(!enabled){console.log('No external messages sent. Enable only after reviewing and testing the receiver.');return;}
 if(!webhook) throw new Error('DISPATCH_ENABLED=true but MAKE_WEBHOOK_URL is missing.');
 for(const event of events){
  const response=await fetch(webhookUrl.toString(),{method:'POST',headers:{'content-type':'application/json','idempotency-key':event.idempotency_key,'user-agent':'Shirmani-Social-Dispatch/1.0'},body:JSON.stringify(event),signal:AbortSignal.timeout(15000)});
  if(!response.ok) throw new Error('Webhook rejected '+event.product.id+': HTTP '+response.status);
  console.log('Webhook accepted event for '+event.product.id+' (HTTP '+response.status+').');
 }
 if(events.length===0) console.log('No eligible products. Nothing sent.');
}
main().catch(err=>{console.error(err.message||err);process.exitCode=1;});
