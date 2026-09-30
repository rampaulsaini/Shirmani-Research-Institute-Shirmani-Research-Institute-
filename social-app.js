(() => {
"use strict";
const KEY="shirmani_social_mvp_v1";
const API_KEY="shirmani_api_base_v1", TOKEN_KEY="shirmani_api_token_v1";
const apiBase=()=>String(localStorage.getItem(API_KEY)||"").replace(/\\/$/,"");
const token=()=>localStorage.getItem(TOKEN_KEY)||"";
async function api(path,options={}){
  const base=apiBase(); if(!base) throw new Error("API_URL_NOT_CONFIGURED");
  const headers=Object.assign({"Content-Type":"application/json"},options.headers||{});
  if(token()) headers.Authorization="Bearer "+token();
  const r=await fetch(base+path,Object.assign({},options,{headers}));
  const body=await r.json().catch(()=>({}));
  if(!r.ok) throw new Error(body.error||("HTTP_"+r.status));
  return body;
}
function cloudMessage(msg){const el=$("cloudAuth");if(el)el.textContent=msg}
function renderCloud(){const base=apiBase();$("apiBase").value=base;cloudMessage(token()?"Cloud token मौजूद है।":"Local-first mode / cloud login आवश्यक।")}
async function loadCloudFeed(){
  try{const d=await api("/feed");state.posts=(d.items||[]).map(p=>({id:p.id,text:p.text,type:p.type,createdAt:p.created_at,cloud:true,author:p.display_name}));renderFeed();status("Cloud feed लोड हुआ।")}
  catch(e){status("Cloud feed उपलब्ध नहीं: "+e.message)}
}
async function publishCloudPost(text,type){
  try{await api("/posts",{method:"POST",body:JSON.stringify({text,type})});await loadCloudFeed();status("Post cloud feed में प्रकाशित हुआ।")}
  catch(e){status("Cloud publish नहीं हुआ: "+e.message)}
}

const QUESTIONS=["इस क्षण मैं वास्तव में क्या अनुभव कर रहा/रही हूँ?","मेरे उत्तर के पीछे सबसे सरल कारण क्या है?","यदि मैं अपने उत्तर को फिर सुनूँ, तो उसमें क्या स्पष्ट दिखाई देता है?","मेरी बात और किसी दूसरे व्यक्ति की बात में क्या समानता/अंतर है?","आज की मेरी समझ में कौन-सा प्रश्न अभी खुला हुआ है?"];
const defaults={profile:{name:"",bio:"",language:"हिंदी"},posts:[],interviews:[],questionIndex:0};
const load=()=>{try{return Object.assign({},defaults,JSON.parse(localStorage.getItem(KEY)||"{}"))}catch{return JSON.parse(JSON.stringify(defaults))}};
let state=load();
const save=()=>{localStorage.setItem(KEY,JSON.stringify(state));renderAll()};
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const fmt=t=>new Date(t).toLocaleString();
const $=id=>document.getElementById(id);
function status(msg){$("status").textContent=msg;setTimeout(()=>{if($("status").textContent===msg)$("status").textContent=""},2600)}
function renderFeed(){const feed=$("feed");if(!state.posts.length){feed.innerHTML='<p class="small">अभी कोई post नहीं है। Create से पहली बात साझा करें।</p>';return}feed.innerHTML=state.posts.slice().reverse().map(p=>'<article class="post"><div class="meta">'+esc(state.profile.name||"आप")+' · '+esc(p.type)+' · '+esc(fmt(p.createdAt))+'</div><p>'+esc(p.text).replace(/\n/g,"<br>")+'</p></article>').join("")}
function renderProfile(){$("displayName").value=state.profile.name||"";$("bio").value=state.profile.bio||"";$("language").value=state.profile.language||"हिंदी"}
function renderInterviews(){$("question").textContent=QUESTIONS[state.questionIndex%QUESTIONS.length];const h=$("interviewHistory");h.innerHTML=state.interviews.length?'<h3>पिछले उत्तर</h3>'+state.interviews.slice().reverse().map(x=>'<div class="result"><div class="meta">'+esc(fmt(x.createdAt))+'</div><div>'+esc(x.question)+'</div><p>'+esc(x.answer).replace(/\n/g,"<br>")+'</p></div>').join(""):'<p class="small">अभी कोई उत्तर सहेजा नहीं गया।</p>'}
function renderSummary(){$("dataSummary").textContent="Profile: "+(state.profile.name||"—")+" · Posts: "+state.posts.length+" · Interviews: "+state.interviews.length}
function renderAll(){renderFeed();renderProfile();renderInterviews();renderSummary()}
function showTab(id){document.querySelectorAll(".panel").forEach(x=>x.classList.toggle("active",x.id===id));document.querySelectorAll("[data-tab]").forEach(x=>x.classList.toggle("active",x.dataset.tab===id));location.hash=id}
document.querySelectorAll("[data-tab]").forEach(b=>b.addEventListener("click",()=>showTab(b.dataset.tab)));
$("postForm").addEventListener("submit",async e=>{e.preventDefault();const text=$("postText").value.trim();if(!text)return;const type=$("postType").value;if(apiBase()&&token()){await publishCloudPost(text,type)}else{state.posts.push({id:crypto.randomUUID(),text,type,createdAt:new Date().toISOString()});save();status("Post local feed में प्रकाशित हो गया।")}$("postText").value="";showTab("home");});
$("clearDraft").addEventListener("click",()=>{$("postText").value="";status("Draft साफ़ किया गया।")});
$("profileForm").addEventListener("submit",async e=>{e.preventDefault();state.profile={name:$("displayName").value.trim(),bio:$("bio").value.trim(),language:$("language").value};if(apiBase()&&token()){try{await api("/profile/"+JSON.parse(atob(token().split(".")[1])).sub,{method:"PATCH",body:JSON.stringify({display_name:state.profile.name,bio:state.profile.bio,language:state.profile.language})});status("Cloud profile सहेजा गया।")}catch(err){status("Cloud profile नहीं सहेजा: "+err.message)}}else{save();status("Profile local device पर सहेजा गया।")}});
$("nextQuestion").addEventListener("click",()=>{state.questionIndex=(state.questionIndex+1)%QUESTIONS.length;save()});
$("saveInterview").addEventListener("click",()=>{const answer=$("answer").value.trim();if(!answer){status("पहले अपना उत्तर लिखें।");return}state.interviews.push({id:crypto.randomUUID(),question:QUESTIONS[state.questionIndex%QUESTIONS.length],answer,createdAt:new Date().toISOString()});$("answer").value="";save();status("आपका self-interview उत्तर सहेज लिया गया।")});
$("exportData").addEventListener("click",()=>{const blob=new Blob([JSON.stringify(state,null,2)],{type:"application/json"});const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download="shirmani-social-data.json";a.click();URL.revokeObjectURL(a.href);status("JSON export तैयार है।")});
$("deleteData").addEventListener("click",()=>{if(!confirm("इस browser का पूरा local MVP data मिटाएँ?"))return;localStorage.removeItem(KEY);state=load();renderAll();status("Local data मिटा दिया गया।")});
$("saveApi").addEventListener("click",()=>{const v=$("apiBase").value.trim().replace(/\\/$/,"");if(v)localStorage.setItem(API_KEY,v);else localStorage.removeItem(API_KEY);renderCloud();status(v?"API URL सहेजा गया।":"Local-first mode सक्रिय।")});
$("cloudRegister").addEventListener("click",async()=>{try{const email=prompt("Email");const password=prompt("Password (कम से कम 12 characters)");if(!email||!password)return;const d=await api("/auth/register",{method:"POST",body:JSON.stringify({email,password,display_name:$("displayName").value,bio:$("bio").value,language:$("language").value})});localStorage.setItem(TOKEN_KEY,d.token);renderCloud();await loadCloudFeed();status("Cloud account बनाया गया।")}catch(e){cloudMessage("Register error: "+e.message)}});
$("cloudLogin").addEventListener("click",async()=>{try{const email=prompt("Email");const password=prompt("Password");if(!email||!password)return;const d=await api("/auth/login",{method:"POST",body:JSON.stringify({email,password}));localStorage.setItem(TOKEN_KEY,d.token);renderCloud();await loadCloudFeed();status("Cloud login सफल।")}catch(e){cloudMessage("Login error: "+e.message)}});
$("cloudLogout").addEventListener("click",()=>{localStorage.removeItem(TOKEN_KEY);renderCloud();status("Cloud session हटाया गया।")});
$("loadMarket").addEventListener("click",async()=>{try{const d=await api("/marketplace/listings");$("marketResults").innerHTML=(d.items||[]).map(x=>"<div class='post'><b>"+esc(x.title)+"</b><div class='meta'>"+esc(x.kind)+" · "+esc(x.display_name||"")+"</div><p>"+esc(x.description||"")+"</p><strong>"+esc(String(x.price_minor))+" "+esc(x.currency)+"</strong></div>").join("")||"अभी कोई listing नहीं।"}catch(e){$("marketResults").textContent="Marketplace unavailable: "+e.message}});
$("listingForm").addEventListener("submit",async e=>{e.preventDefault();try{if(!token())throw new Error("LOGIN_REQUIRED");await api("/marketplace/listings",{method:"POST",body:JSON.stringify({kind:$("listingKind").value,title:$("listingTitle").value.trim(),description:$("listingDescription").value.trim(),price_minor:Number($("listingPrice").value),currency:$("listingCurrency").value.trim().toUpperCase()})});await $("loadMarket").click();status("Listing cloud marketplace में प्रकाशित हुई।")}catch(err){status("Listing नहीं हुई: "+err.message)}});
$("seedDemo").addEventListener("click",()=>{state.posts.push({id:crypto.randomUUID(),text:"यह केवल local demo है — यहाँ कोई वास्तविक follower, view, payment या व्यक्ति का दावा नहीं किया गया है।",type:"Demo",createdAt:new Date().toISOString()});save();status("Demo post जोड़ा गया।")});
renderAll();renderCloud();const initial=location.hash.slice(1);if(["home","create","learn","profile","data"].includes(initial))showTab(initial);
})();