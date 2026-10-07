/* SHIRMANI Supreme Showroom Visual Identity Layer v4 */
(function(){
"use strict";
const esc=s=>String(s??"").replace(/[&<>"]/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m]));
const LOGO="assets/shirmani-perspective-photo.png";
const IDENTITY="Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present";
const qr=id=>"https://api.qrserver.com/v1/create-qr-code/?size=420x420&margin=10&data="+encodeURIComponent(location.origin+location.pathname.replace(/[^/]*$/,"")+"product-passport.html?id="+encodeURIComponent(id));
async function boot(){
 let catalog;
 try{catalog=await fetch("generated/1000-digital-products.json?ts="+Date.now(),{cache:"no-store"}).then(r=>r.json())}catch(e){return}
 const map=new Map((catalog.products||[]).map(p=>[p.id,p]));
 const style=document.createElement("style");
 style.textContent=".shirmani-poster{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:14px;border:1px solid #e7c85b}.shirmani-poster>img{display:block;width:100%;height:100%;object-fit:cover}.shirmani-brand{position:absolute;left:1.2%;top:1.2%;display:flex;gap:8px;align-items:center;max-width:58%;padding:7px 9px;border-radius:10px;background:#04110cdd;border:1px solid #e7c85b;color:#fff}.shirmani-brand img{width:44px;height:44px;border-radius:50%;object-fit:cover;border:2px solid #e7c85b}.shirmani-brand b{display:block;color:#f6d35f;font-size:12px}.shirmani-brand span{display:block;font-size:8px;line-height:1.2}.shirmani-qr{position:absolute;right:1.2%;top:1.2%;width:86px;padding:6px;background:#061016ed;border:1px solid #e7c85b;border-radius:10px;text-align:center}.shirmani-qr img{width:72px;height:72px;background:#fff}.shirmani-qr small{display:block;color:#66ddff;font-size:7px;font-weight:900}.shirmani-short{position:absolute;left:1.2%;right:22%;bottom:2%;padding:6px 9px;background:#050910dc;border-left:3px solid #66ddff;color:#fff;font-size:9px}.shirmani-short b{color:#f6d35f}.shirmani-id{position:absolute;right:1.2%;bottom:2%;padding:6px 9px;background:#050910ee;border:1px solid #e7c85b;border-radius:9px;color:#f6d35f;font-weight:900;font-size:9px}";
 document.head.appendChild(style);
 const decorate=()=>document.querySelectorAll("#grid .card").forEach(card=>{
  if(card.dataset.identityVisualV3==="1")return;
  const img=card.querySelector("img");if(!img)return;
  const m=(card.textContent||"").match(/\bSP-\d{4,}\b/i);if(!m)return;
  const p=map.get(m[0].toUpperCase())||{id:m[0].toUpperCase(),name:"SHIRMANI Digital Product"};
  const id=String(p.id).toUpperCase();
  const desc=String(p.short_description||p.description||"Unique customer-facing digital product.").replace(/\s+/g," ").slice(0,170);
  const poster=document.createElement("div");poster.className="shirmani-poster";
  poster.innerHTML='<img src="'+img.src+'" alt="'+esc(p.name)+' — 4K product visual" loading="lazy"><div class="shirmani-brand"><img src="'+LOGO+'" alt="SHIRMANI logo"><div><b>SHIRMANI SUPREME DIGITAL PRODUCT</b><span>'+esc(IDENTITY)+'</span></div></div><div class="shirmani-qr"><img src="'+qr(id)+'" alt="QR for long description"><small>SCAN FOR LONG DESCRIPTION</small></div><div class="shirmani-short"><b>SHORT DESCRIPTION · </b>'+esc(desc)+'</div><div class="shirmani-id">'+esc(id)+'</div>';
  img.parentElement.replaceWith(poster);
  card.dataset.identityVisualV3="1";
 });
 decorate();
 const grid=document.getElementById("grid");if(grid)new MutationObserver(decorate).observe(grid,{childList:true,subtree:true});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",boot);else boot();
})();