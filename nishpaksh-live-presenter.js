(function(){
  const q=document.getElementById("question"), ev=document.getElementById("evidence"), es=document.getElementById("evidenceStatus");
  const answer=document.getElementById("answer"), badges=document.getElementById("evidenceBadges"), speak=document.getElementById("speakBtn");
  function render(){
    const text=q.value.trim(), source=ev.value.trim(), state=es.value;
    if(!text){answer.textContent="कृपया पहले प्रश्न लिखें।";badges.innerHTML="";return;}
    let response;
    if(state==="available" && source){
      response="मैंने प्रश्न को उपलब्ध संदर्भ के आधार पर सीमित उत्तर में रखा है।\n\nप्रश्न: "+text+"\n\nउत्तर: उपलब्ध source/evidence के दायरे में ही निष्कर्ष रखा जाएगा। Source की स्वतंत्रता और वैज्ञानिक validity अलग verification चरण हैं।";
    }else{
      response="प्रश्न: "+text+"\n\nउत्तर: अभी पर्याप्त प्रमाण उपलब्ध नहीं है। उपलब्ध जानकारी को observation / claim / hypothesis के रूप में अलग रखा जाएगा; बिना पर्याप्त independent evidence के इसे VERIFIED तथ्य नहीं माना जाएगा।";
    }
    answer.textContent=response;
    badges.innerHTML="";
    const add=(t,c)=>{const s=document.createElement("span");s.className="badge "+c;s.textContent=t;badges.appendChild(s)};
    add(state==="available"&&source?"SOURCE PROVIDED":"EVIDENCE LIMITED",state==="available"&&source?"good":"warn");
    add("UNVERIFIED BOUNDARY","lock");
    if(source)add("Source: "+source,"good");
  }
  document.getElementById("answerBtn").addEventListener("click",render);
  speak.addEventListener("click",function(){
    const text=answer.textContent.trim();
    if(!text || text==="उत्तर यहाँ दिखाई देगा।"){render();}
    const utter=new SpeechSynthesisUtterance(answer.textContent);
    utter.lang="hi-IN"; utter.rate=.95; utter.pitch=1;
    if("speechSynthesis" in window) window.speechSynthesis.speak(utter);
  });
})();