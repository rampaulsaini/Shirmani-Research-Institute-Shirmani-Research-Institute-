/* SHIRMANI Supreme Showroom Visual Identity Layer v5
 * Product-first visual contract:
 * - product-specific visual remains the main artwork
 * - SHIRMANI Heart-View photo/logo at upper-left
 * - exact English identity line below the logo
 * - QR at upper-right routes to the product's long passport/details
 * - short description is rendered on the artwork
 * - no claim of sale, QC or scientific verification is implied by the visual
 */
(function(){
"use strict";
const esc=s=>String(s??"").replace(/[&<>"]/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m]));
const LOGO="assets/shirmani-perspective-logo.svg";
const IDENTITY="Shiromani Rampal Saini · Impartial Understanding · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present";
const qr=id=>"https://api.qrserver.com/v1/create-qr-code/?size=420x420&margin=10&data="+encodeURIComponent(new URL("product-passport.html?id="+encodeURIComponent(id),location.href).href);

async function boot(){
 let catalog={products:[]};
 try{catalog=await fetch("generated/1000-digital-products.json?ts="+Date.now(),{cache:"no-store"}).then(r=>r.ok?r.json():{products:[]})}catch(e){}
 const map=new Map((catalog.products||[]).map(p=>[String(p.id||"").toUpperCase(),p]));
 const style=document.createElement("style");
 style.textContent=`
 .shirmani-poster{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:14px;border:2px solid #e7c85b;background:#050910}
 .shirmani-poster>img.shirmani-art{display:block;width:100%;height:100%;object-fit:cover}
 .shirmani-brand{position:absolute;left:1.2%;top:1.2%;display:flex;gap:8px;align-items:flex-start;max-width:57%;padding:7px 9px;border-radius:10px;background:#04110cee;border:1px solid #e7c85b;color:#fff;z-index:5;box-shadow:0 5px 18px #0008}
 .shirmani-brand img{width:52px;height:52px;flex:0 0 52px;border-radius:50%;object-fit:cover;border:2px solid #e7c85b;background:#061016}
 .shirmani-brand b{display:block;color:#f6d35f;font-size:12px;line-height:1.15}
 .shirmani-brand span{display:block;font-size:8px;line-height:1.22;margin-top:3px;color:#f4f7fb}
 .shirmani-qr{position:absolute;right:1.2%;top:1.2%;width:96px;padding:6px;background:#061016ee;border:1px solid #e7c85b;border-radius:10px;text-align:center;z-index:5;box-shadow:0 5px 18px #0008}
 .shirmani-qr img{width:82px;height:82px;background:#fff;display:block}
 .shirmani-qr small{display:block;color:#66ddff;font-size:7px;font-weight:900;line-height:1.1;margin-top:4px}
 .shirmani-short{position:absolute;left:1.2%;right:22%;bottom:2%;padding:7px 10px;background:#050910e8;border-left:3px solid #66ddff;color:#fff;font-size:10px;line-height:1.25;z-index:5;box-shadow:0 3px 12px #0007}
 .shirmani-short b{color:#f6d35f}
 .shirmani-id{position:absolute;right:1.2%;bottom:2%;padding:7px 10px;background:#050910ee;border:1px solid #e7c85b;border-radius:9px;color:#f6d35f;font-weight:900;font-size:10px;z-index:5}
 @media(max-width:650px){.shirmani-brand{max-width:66%}.shirmani-brand span{font-size:7px}.shirmani-qr{width:78px}.shirmani-qr img{width:64px;height:64px}.shirmani-short{right:27%;font-size:8px}.shirmani-id{font-size:8px}}
 `;
 document.head.appendChild(style);

 const decorate=()=>{
   document.querySelectorAll("#grid .card").forEach(card=>{
     if(card.dataset.identityVisualV5==="1")return;
     const img=card.querySelector("img");
     if(!img)return;
     const m=(card.textContent||"").match(/\bSP-\d{4,}\b/i);
     if(!m)return;
     const id=m[0].toUpperCase();
     const p=map.get(id)||{id,name:"SHIRMANI Digital Product"};
     const desc=String(p.short_description||p.description||"Unique customer-facing digital product.").replace(/\s+/g," ").slice(0,190);
     const poster=document.createElement("div");
     poster.className="shirmani-poster";
     poster.innerHTML='<img class="shirmani-art" src="'+esc(img.currentSrc||img.src)+'" alt="'+esc(p.name)+' — unique 4K product visual" loading="lazy">'+
       '<div class="shirmani-brand"><img src="'+LOGO+'" alt="SHIRMANI Heart-View logo"><div><b>SHIRMANI SUPREME DIGITAL PRODUCT</b><span>'+esc(IDENTITY)+'</span></div></div>'+
       '<div class="shirmani-qr"><img src="'+qr(id)+'" alt="QR for long product description"><small>SCAN FOR LONG DESCRIPTION</small></div>'+
       '<div class="shirmani-short"><b>SHORT DESCRIPTION · </b>'+esc(desc)+'</div>'+
       '<div class="shirmani-id">'+esc(id)+'</div>';
     img.parentElement.replaceWith(poster);
     card.dataset.identityVisualV5="1";
   });
 };
 decorate();
 const grid=document.getElementById("grid");
 if(grid)new MutationObserver(decorate).observe(grid,{childList:true,subtree:true});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",boot);else boot();
})();