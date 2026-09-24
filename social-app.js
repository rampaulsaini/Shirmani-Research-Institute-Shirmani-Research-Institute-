(() => {
"use strict";
const KEY="shirmani_social_mvp_v1";
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
$("postForm").addEventListener("submit",e=>{e.preventDefault();const text=$("postText").value.trim();if(!text)return;state.posts.push({id:crypto.randomUUID(),text,type:$("postType").value,createdAt:new Date().toISOString()});$("postText").value="";save();showTab("home");status("Post local feed में प्रकाशित हो गया।")});
$("clearDraft").addEventListener("click",()=>{$("postText").value="";status("Draft साफ़ किया गया।")});
$("profileForm").addEventListener("submit",e=>{e.preventDefault();state.profile={name:$("displayName").value.trim(),bio:$("bio").value.trim(),language:$("language").value};save();status("Profile local device पर सहेजा गया।")});
$("nextQuestion").addEventListener("click",()=>{state.questionIndex=(state.questionIndex+1)%QUESTIONS.length;save()});
$("saveInterview").addEventListener("click",()=>{const answer=$("answer").value.trim();if(!answer){status("पहले अपना उत्तर लिखें।");return}state.interviews.push({id:crypto.randomUUID(),question:QUESTIONS[state.questionIndex%QUESTIONS.length],answer,createdAt:new Date().toISOString()});$("answer").value="";save();status("आपका self-interview उत्तर सहेज लिया गया।")});
$("exportData").addEventListener("click",()=>{const blob=new Blob([JSON.stringify(state,null,2)],{type:"application/json"});const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download="shirmani-social-data.json";a.click();URL.revokeObjectURL(a.href);status("JSON export तैयार है।")});
$("deleteData").addEventListener("click",()=>{if(!confirm("इस browser का पूरा local MVP data मिटाएँ?"))return;localStorage.removeItem(KEY);state=load();renderAll();status("Local data मिटा दिया गया।")});
$("seedDemo").addEventListener("click",()=>{state.posts.push({id:crypto.randomUUID(),text:"यह केवल local demo है — यहाँ कोई वास्तविक follower, view, payment या व्यक्ति का दावा नहीं किया गया है।",type:"Demo",createdAt:new Date().toISOString()});save();status("Demo post जोड़ा गया।")});
renderAll();const initial=location.hash.slice(1);if(["home","create","learn","profile","data"].includes(initial))showTab(initial);
})();