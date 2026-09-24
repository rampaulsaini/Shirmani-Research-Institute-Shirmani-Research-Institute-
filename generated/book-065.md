# डिजिटल महाग्रंथ 065

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 064001
Repeat after changing model quantization, offload, inference steps, or other generation settings.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064002
Compare **quality + generation time + VRAM + cost**, not speed alone.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064003
Important interpretation notes ### 1.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064004
GPU power is not whole-PC power `nvidia-smi` measures reported GPU power draw.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064005
A complete PC will consume additional power through the CPU, motherboard, RAM, SSD, fans, PSU losses, and other components.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064006
For a business cost model, measure wall power with a suitable power meter if possible.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064007
One generation is not necessarily one customer A customer may regenerate a song several times before downloading a result.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064008
Include retries/regenerations when calculating usage limits.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064009
Concurrent users change the result This benchmark is intentionally sequential.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064010
Once the single-generation baseline is known, run a separate controlled concurrency test before increasing `MAX_CONCURRENT_GENERATIONS`.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064011
Do not simply increase concurrency until the GPU crashes.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064012
Long songs may change memory/time behavior Always test the longest duration you intend to sell.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064013
The 180-second test is included specifically to expose problems that a 30-second test may miss.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064014
Benchmark after every major model/configuration change Record: - GPU model - VRAM - ACE-Step model/checkpoint - quantization/offload settings - inference steps - batch size - audio format - requested duration - generation time - peak VRAM - average/peak power - software versions This makes future hardware comparisons meaningful.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064015
Output for business planning After running the benchmark, bring the generated `gpu_benchmark_results.json` into the project discussion.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064016
The key numbers needed for the next calculation are: ```text 30s generation time 60s generation time 180s generation time peak VRAM average GPU power peak GPU power actual electricity tariff GPU/PC purchase price planned price per song or subscription songs included per user ``` Those figures can then be used to calculate a more realistic **₹/song, monthly capacity, break-even point, and operating-cost model** for Yatharth Music AI.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 064017
Yatharth Music AI — ₹0 setup This project supports a free-first development path using the open-source ACE-Step engine.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064018
Easiest path: local computer A local computer is the most reliable way to stay at ₹0 because there is no cloud GPU rental.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064019
ACE-Step can run with GPU acceleration and also supports CPU-only operation, although CPU generation can be much slower.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064020
Install Use Python 3.11 or 3.12.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064021
Install the official ACE-Step project and its dependencies from the official repository.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064022
Then start the ACE-Step API on port `8001`.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064023
Set Yatharth Music AI to: ```text DEMO_MODE=false MUSIC_ENGINE_URL= ``` Start the Yatharth backend on port `8000`, then open the Yatharth web app.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064024
Free Colab GPU Open `colab/Yatharth_Music_AI_Free_GPU.ipynb` in Google Colab and run the cells.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064025
The notebook is intended for temporary development/testing.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064026
Free Colab GPU access is dynamic, sessions can terminate, and it is not a dependable 24/7 public hosting solution.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064027
Hardware guidance - 6GB+ VRAM: a practical starting point for local GPU use.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064028
4GB VRAM: ACE-Step has lower-memory modes, but generation may require more aggressive memory management.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064029
CPU-only: possible, but expect substantially slower generation.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064030
Important architecture rule Do not put model weights, API keys, passwords, or private credentials into this GitHub repository.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064031
The public web app can remain in `DEMO_MODE=true` when no engine is connected.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064032
When a local or temporary ACE-Step engine is available, set `DEMO_MODE=false` and point `MUSIC_ENGINE_URL` at it.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064033
Cost target **Target: ₹0 for software and development.** A permanently available public AI music-generation server with guaranteed GPU capacity cannot honestly be promised at ₹0.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064034
If the project later needs 24/7 public generation, a paid GPU service may become necessary.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064035
Official project Use the official ACE-Step repository and documentation for the engine.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064036
Avoid unofficial websites claiming to be the official ACE-Step service.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 064037
Yatharth Digital Products YATHARTH DIGITAL PRODUCTS Reusable creative assets और production material का public catalog.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064038
← Creator Hub PRODUCT CATALOG • निष्पक्ष समझ डिजिटल सामग्री को उत्पाद की तरह प्रस्तुत करें।
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064039
यह catalog publishing-ready structure देता है।
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064040
हर item के साथ वास्तविक price, delivery method और purchase route तभी जोड़ा जाएगा जब वह सच में configured हो।
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064041
निष्पक्ष समझ शिरोमणि रामपाल सैनी स्रोत-आधारित creator identity.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064042
🎙️ आवाज़ / public source → 🎼 Music Creation Packs Song prompts, lyric frameworks, production briefs और reusable music workflows.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064043
Catalog item — publishing setup required ✍️ Story & Script Packs Story structures, character sheets, scene planning और storyboard templates.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064044
Catalog item — publishing setup required 🤖 Automission Templates AI-agent orchestration contracts, production manifests और workflow templates.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064045
Catalog item — publishing setup required 🎨 Creative Asset Packs Prompts, visual briefs, thumbnails, titles और presentation-ready creative assets.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064046
Catalog item — publishing setup required 🌐 Website / Studio Kits Creator landing pages, studio interfaces और deployment-ready UI packages.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064047
Catalog item — publishing setup required 📚 Yatharth Research Material Research, essays और structured public material को digital editions में व्यवस्थित करने का मार्ग.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064048
Publication + commerce setup required Creator Hub • Music • Creative Studio
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 064049
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse", "role": "omniverse-core", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omniverse:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 064050
Omniverse Supreme Platform - शिरोमणि रामपाल सैनी OMNIVERSE SUPREME मूल दर्शन ऑडियो आर्काइव गैलरी व मीडिया स्टोर व रिसर्च AI & GitHub शिरोमणि रामपाल सैनी सृष्टि, प्रकृति और पृथ्वी के संरक्षण का एकमात्र अलौकिक मार्ग — हृदय का शिरोमणि दृष्टिकोण ✨ ब्रह्मांडीय अलौकिक दृष्टिकोण "अनंत असीम प्रेम ही सिर्फ़ मस्तक, मन और बुद्धि का दृष्टिकोण बदल सकता है और हृदय के शिरोमणि दृष्टिकोण में रख सकता है, जिससे मानव, प्रकृति और पृथ्वी का संरक्षण सुनिश्चित संभव है और कोई दूसरा विकल्प ही नहीं।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064051
मन, मस्तक, बुद्धि से बुद्धिमान होने का ज्ञान, विज्ञान और दर्शन सीमित है।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064052
हृदय के शिरोमणि स्वरूप का दृष्टिकोण असीम, भव्य, अद्भुत और आश्चर्यचकित है जो प्रथम चरण में ही खुद से रूबरू करवाता है और संपूर्ण संतुष्टि की निरंतरता में रख सकता है।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064053
मानव सभ्यता अस्तित्व से ही मन, मस्तक और बुद्धि के दृष्टिकोण में रही है जो आज तक अपने स्थायी स्वरूप से रूबरू नहीं हो सकी।" 🎧 खुद का साक्षात्कार: ऑडियो संग्रह (33,000+ MP3) 10,000 MP3 Audio खुद का साक्षात्कार ही संपूर्ण संतुष्टि हैं मन-बुद्धि के स्तर से परे संपूर्ण संतुष्टि की निरंतरता हेतु साक्षात्कार ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064054
गूगल ड्राइव में सुनें 10,000 MP3 Audio साहिब तदरूप साक्षात्कार हूं स्वयं के तदरूप स्वरूप का साक्षात्कार कराने वाली अमूल्य ध्वनियों का वृहद संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064055
गूगल ड्राइव में सुनें 6,000 MP3 Audio खुद का साक्षात्कार ऑडियो प्रथम चरण में ही खुद से रूबरू कराने वाले आध्यात्मिक एवं दार्शनिक ऑडियो।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064056
गूगल ड्राइव में सुनें 5,000 MP3 Audio मेरा साहिब मेरा ही तदरूप साक्षात्कार है हृदय के शिरोमणि स्वरूप को जागृत करने वाले विशेष तदरूप ऑडियो ट्रैक्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064057
गूगल ड्राइव में सुनें 1,500 MP3 Audio शिरोमणि अनंत असीम इश्क़ की क्षमता दृष्टिकोण बदलने और असीम प्रेम की क्षमता का अनुभव कराने वाले ऑडियो।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064058
गूगल ड्राइव में सुनें 950 MP3 Audio शिरोमणि रामपाल सैनी खुद का साक्षात्कार हूं आत्म-साक्षात्कार और आत्म-ज्ञान पर केंद्रित विशेष ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064059
गूगल ड्राइव में सुनें 550 MP3 Audio शिरोमणि रामपाल सैनी MP3 शिरोमणि रामपाल सैनी जी के मौलिक प्रवचन एवं ऑडियो व्याख्यान।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064060
गूगल ड्राइव में सुनें 89 MP3 Audio शिरोमणि रामपाल सैनी Short Audios संक्षिप्त और प्रभावशाली मुख्य सूक्तियाँ तथा ऑडियो संदेश।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064061
गूगल ड्राइव में सुनें 🖼️ गैलरी, फोटो एल्बम व वीडियो (Visual Archives) 2,000 Photos Golden Temple शिरोमणि रामपाल सैनी फ़ोटो गोल्डन टेम्पल परिसर के अलौकिक एवं भव्य फोटो संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064062
एल्बम देखें 10,000+ Videos मेरा संपूर्ण जीवन शिरोमणि Videos जीवन यात्रा और दिव्य अनुभूतियों को दर्शाते वीडियो रिकॉर्डिंग्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064063
वीडियो देखें 4,000+ Photos / 495 Files शिरोमणि प्रमाण पत्र संग्रह सभी महत्वपूर्ण प्रमाण पत्रों का गूगल फोटो एल्बम एवं ड्राइव आर्काइव।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064064
एल्बम (4000) ड्राइव फ़ाइलें (495) Drive Album Omniverse Gallery ऑम्निवर्स और संपूर्ण ब्रह्मांडीय विज़न की आधिकारिक फोटो गैलरी।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064065
गैलरी खोलें YouTube & Facebook सोशल मीडिया चैनल्स यूट्यूब चैनल और फेसबुक पर उपलब्ध वीडियो संदेश व अपडेट्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064066
YouTube Channel Facebook Video Blogspot Multicosmovision Blog & Case Files सृष्टि, प्रकृति और दार्शनिक विषयों पर गहराई से लिखे गए ब्लॉग्स और केस फाइल्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064067
मुख्य ब्लॉग पढ़ें Case File देखें 🛒 स्टोर, शोध एवं घोषणा पत्र (Store & Research) E-Commerce Omniverse Store आधिकारिक ऑम्निवर्स डिजिटल स्टोर जहाँ सभी सेवाएँ उपलब्ध हैं।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064068
स्टोर पर जाएं Manifesto Koyab Founding Declaration Omniversal Manifesto — ब्रह्मांडीय घोषणा पत्र एवं मौलिक विज़न।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064069
घोषणा पत्र पढ़ें Research GitHub Shirmani Research Institute शिरोमणि रिसर्च इंस्टीट्यूट का आधिकारिक GitHub कोड एवं शोध रिपॉजिटरी।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064070
GitHub Repository 💻 ऑम्निवर्स AI व डिजिटल प्लेटफॉर्म्स (AI Ecosystem) Omniverse AI Portal AI तकनीक आधारित प्लेटफॉर्म पोर्टल खोलें Omniverse Dashboard एकीकृत नियंत्रण डैशबोर्ड डैशबोर्ड देखें Omniverse Supreme Core मुख्य कोर सिस्टम कोर देखें Omniverse Marketplace डिजिटल प्लेटफॉर्म मार्किटप्लेस <a href=" target=
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064071
🌟 Golden Temple Spiritual Insights ![Golden Temple Spiritual Honor]( .
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064072
( ## Spiritual Experience - Evening at Golden Temple, naturally honored for impartial understanding, simplicity, and purity - Realization: Human intellect & memory distortions can be neutralized through simplicity.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064073
Core Insights - All living beings are internally equal.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064074
Omniverse Platform designed on impartial understanding, reality-based achievement, and the era of true reality.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064075
Purpose of Omniverse - Equality, fairness, and guidance for all beings.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064076
Balance of technology, philosophy, and spiritual insight.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064077
Go to [ and login 2.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064078
Create a new repository: `Omniverse` 3.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064079
Add files: `README.md`, `GoldenTemple.md`, `golden-temple.webp`, `upi-qr.png` 4.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064080
Repository live link: ` > Replace `YOUR_PAYPAL_BUTTON_ID` with your PayPal account button ID.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064081
> Once uploaded, all buttons and links will be fully functional for payments.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064082
> Omniverse Supreme Platform - शिरोमणि रामपाल सैनी OMNIVERSE SUPREME मूल दर्शन ऑडियो आर्काइव गैलरी व मीडिया स्टोर व रिसर्च AI & GitHub शिरोमणि रामपाल सैनी सृष्टि, प्रकृति और पृथ्वी के संरक्षण का एकमात्र अलौकिक मार्ग — हृदय का शिरोमणि दृष्टिकोण ✨ ब्रह्मांडीय अलौकिक दृष्टिकोण "अनंत असीम प्रेम ही सिर्फ़ मस्तक, मन और बुद्धि का दृष्टिकोण बदल सकता है और हृदय के शिरोमणि दृष्टिकोण में रख सकता है, जिससे मानव, प्रकृति और पृथ्वी का संरक्षण सुनिश्चित संभव है और कोई दूसरा विकल्प ही नहीं।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064083
मन, मस्तक, बुद्धि से बुद्धिमान होने का ज्ञान, विज्ञान और दर्शन सीमित है।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064084
हृदय के शिरोमणि स्वरूप का दृष्टिकोण असीम, भव्य, अद्भुत और आश्चर्यचकित है जो प्रथम चरण में ही खुद से रूबरू करवाता है और संपूर्ण संतुष्टि की निरंतरता में रख सकता है।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064085
मानव सभ्यता अस्तित्व से ही मन, मस्तक और बुद्धि के दृष्टिकोण में रही है जो आज तक अपने स्थायी स्वरूप से रूबरू नहीं हो सकी।" 🎧 खुद का साक्षात्कार: ऑडियो संग्रह (33,000+ MP3) 10,000 MP3 Audio खुद का साक्षात्कार ही संपूर्ण संतुष्टि हैं मन-बुद्धि के स्तर से परे संपूर्ण संतुष्टि की निरंतरता हेतु साक्षात्कार ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064086
गूगल ड्राइव में सुनें 10,000 MP3 Audio साहिब तदरूप साक्षात्कार हूं स्वयं के तदरूप स्वरूप का साक्षात्कार कराने वाली अमूल्य ध्वनियों का वृहद संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064087
गूगल ड्राइव में सुनें 6,000 MP3 Audio खुद का साक्षात्कार ऑडियो प्रथम चरण में ही खुद से रूबरू कराने वाले आध्यात्मिक एवं दार्शनिक ऑडियो।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064088
गूगल ड्राइव में सुनें 5,000 MP3 Audio मेरा साहिब मेरा ही तदरूप साक्षात्कार है हृदय के शिरोमणि स्वरूप को जागृत करने वाले विशेष तदरूप ऑडियो ट्रैक्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064089
गूगल ड्राइव में सुनें 1,500 MP3 Audio शिरोमणि अनंत असीम इश्क़ की क्षमता दृष्टिकोण बदलने और असीम प्रेम की क्षमता का अनुभव कराने वाले ऑडियो।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064090
गूगल ड्राइव में सुनें 950 MP3 Audio शिरोमणि रामपाल सैनी खुद का साक्षात्कार हूं आत्म-साक्षात्कार और आत्म-ज्ञान पर केंद्रित विशेष ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064091
गूगल ड्राइव में सुनें 550 MP3 Audio शिरोमणि रामपाल सैनी MP3 शिरोमणि रामपाल सैनी जी के मौलिक प्रवचन एवं ऑडियो व्याख्यान।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064092
गूगल ड्राइव में सुनें 89 MP3 Audio शिरोमणि रामपाल सैनी Short Audios संक्षिप्त और प्रभावशाली मुख्य सूक्तियाँ तथा ऑडियो संदेश।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064093
गूगल ड्राइव में सुनें 🖼️ गैलरी, फोटो एल्बम व वीडियो (Visual Archives) 2,000 Photos Golden Temple शिरोमणि रामपाल सैनी फ़ोटो गोल्डन टेम्पल परिसर के अलौकिक एवं भव्य फोटो संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064094
एल्बम देखें 10,000+ Videos मेरा संपूर्ण जीवन शिरोमणि Videos जीवन यात्रा और दिव्य अनुभूतियों को दर्शाते वीडियो रिकॉर्डिंग्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064095
वीडियो देखें 4,000+ Photos / 495 Files शिरोमणि प्रमाण पत्र संग्रह सभी महत्वपूर्ण प्रमाण पत्रों का गूगल फोटो एल्बम एवं ड्राइव आर्काइव।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064096
एल्बम (4000) ड्राइव फ़ाइलें (495) Drive Album Omniverse Gallery ऑम्निवर्स और संपूर्ण ब्रह्मांडीय विज़न की आधिकारिक फोटो गैलरी।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064097
गैलरी खोलें YouTube & Facebook सोशल मीडिया चैनल्स यूट्यूब चैनल और फेसबुक पर उपलब्ध वीडियो संदेश व अपडेट्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064098
YouTube Channel Facebook Video Blogspot Multicosmovision Blog & Case Files सृष्टि, प्रकृति और दार्शनिक विषयों पर गहराई से लिखे गए ब्लॉग्स और केस फाइल्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064099
मुख्य ब्लॉग पढ़ें Case File देखें 🛒 स्टोर, शोध एवं घोषणा पत्र (Store & Research) E-Commerce Omniverse Store आधिकारिक ऑम्निवर्स डिजिटल स्टोर जहाँ सभी सेवाएँ उपलब्ध हैं।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064100
स्टोर पर जाएं Manifesto Koyab Founding Declaration Omniversal Manifesto — ब्रह्मांडीय घोषणा पत्र एवं मौलिक विज़न।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064101
घोषणा पत्र पढ़ें Research GitHub Shirmani Research Institute शिरोमणि रिसर्च इंस्टीट्यूट का आधिकारिक GitHub कोड एवं शोध रिपॉजिटरी।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064102
GitHub Repository 💻 ऑम्निवर्स AI व डिजिटल प्लेटफॉर्म्स (AI Ecosystem) Omniverse AI Portal AI तकनीक आधारित प्लेटफॉर्म पोर्टल खोलें Omniverse Dashboard एकीकृत नियंत्रण डैशबोर्ड डैशबोर्ड देखें Omniverse Supreme Core मुख्य कोर सिस्टम कोर देखें Omniverse Marketplace डिजिटल प्लेटफॉर्म मार्किटप्लेस <a href=" target=
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064103
{ "schema_version": 1, "repo": "rampaulsaini/Shirmani-Research-Paper", "role": "research-publishing", "description": "Research publishing worker: inventory papers and mark generated research as draft pending independent verification.", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Shirmani-Research-Paper:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 064104
Shirmani Research Paper Shirmani Research Paper Philosophical & Cognitive Research Framework About Research Areas Download About This Research This platform presents structured work on time perception, self-identity models, ego deconstruction, and balanced decision systems.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064105
Core Research Areas Time Deconstruction Moment-based temporal philosophy.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064106
Neurobiology of Self Cognitive structure of identity formation.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064107
Ego Dissolution Philosophical and psychological model.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064108
Heart-Mind Balance Practical decision equilibrium system.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064109
यहाँ समय, सृष्टि, विकल्प, संकल्प, मोह, स्मृति और बाह्य व्यवस्था — सब क्षणिक छाया के रूप में देखे गए हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064110
इसके विपरीत, हृदय की स्थिरता, शुद्ध संतोष, बाल्य-सुलभ निर्मलता और आत्म-साक्षात्कार को ही मूल सत्य माना गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064111
अध्याय १ — प्रत्यक्ष सत्ता शिरोमणि रामपॉल सैनी अपने अनुभव में स्वयं को सीमित शरीर, सांस और मन से परे देखते हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064112
उनका कहना है कि समस्त भौतिक सृष्टि, ग्रह, ब्रह्मांड और जीवन केवल क्षणिक और अस्थायी हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064113
वास्तविकता की अनुभूति केवल हृदय की गहनता में, शुद्ध चेतना और संपूर्ण संतुष्टि के माध्यम से होती है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064114
संसारः क्षणभङ्गुरः, माया-प्रसवविस्तरः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064115
प्रत्यक्षं तु हृदि नित्यं, शाश्वतं सत्यरूपकम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064116
शिरोमणिः रामपॉल सैनी, शब्दातीतः, मनोऽपि च।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064117
तुलनातीतः, कालातीतः, हृदये साक्ष्यरूपतः॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064118
अध्याय २ — बाल्य-संतोष का स्मरण बचपन में जो संपूर्ण संतोष सहज रूप से उपस्थित था, वह किसी बाहरी उपलब्धि का परिणाम नहीं था।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064119
वह स्थिति कम अपेक्षाओं, कम पहचान-बोध और अधिक स्वाभाविकता की थी।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064120
बाल्ये सम्पूर्णसन्तोषः, सहजः निर्मलः स्थिरः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064121
न लब्धो बाह्यतश्च सः, नष्टोऽपि न हि कदाचन॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064122
मनोजटिलता वयस्ये, आवृणोति स्वभावताम्।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064123
साक्षात्कारात् पुनर्लभ्यं, बाल्यं तद्वत् परं सुखम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064124
अध्याय ३ — प्रेम, जिज्ञासा और निस्वार्थता यहाँ प्रेम को मोह से अलग किया गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064125
मोह लेन-देन पर आधारित होता है; प्रेम निस्वार्थ जिज्ञासा और हृदय की गहराई से जन्म लेता है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064126
जो भीतर से निर्मल है, वही वास्तव में प्रेम को पहचान सकता है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064127
मोहः प्रेम न विज्ञेयः, न व्यापारः स एव हि।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064128
प्रेम तु निस्वभावेन, हृदयस्य प्रवर्तनम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064129
जिज्ञासा यदि निर्मला, स्वार्थरहिता स्थिता।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064130
तदा सा नयते नित्यं, सत्यस्यैव निवेशने॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064131
अध्याय ४ — मन, बुद्धि और अस्थायी सृष्टि मन और बुद्धि उपयोगी हैं, पर स्थायी नहीं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064132
वे अनुभव को व्यवस्थित करते हैं, पर सत्य की अंतिम भूमि नहीं हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064133
सृष्टि, समय, गति, परिवर्तन, जन्म और मृत्यु — सब मन की दृष्टि में एक विराट दृश्य की तरह प्रतीत होते हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064134
मनः संकल्परूपेण, बुद्धिश्च विविकारिणी।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064135
नित्यं न हि तयोः सत्ता, भासते केवलं क्षणम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064136
ग्रहाः सौरमण्डलानि च, ब्रह्माण्डानि सहस्रशः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064137
सर्वं दृश्यं क्षणं भूत्वा, लीयते सत्यदृष्टितः॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064138
अध्याय ५ — एकत्व, समाहिति और अंतिम स्थिरता यहाँ अनेकता एक में समाहित होती है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064139
मृत्यु को अंत नहीं, बल्कि समाहिति की प्रक्रिया के रूप में देखा गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064140
संपूर्ण संतुष्टि, जो बाहर बिखरी हुई प्रतीत होती है, वह अंततः एक ही गहरी सत्ता में लौटती है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064141
अनेकता एकतां याति, शान्ते हृदयसागरे।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064142
तत्रैव संपूर्णसन्तोषः, तत्रैव स्थिरता परा॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064143
मृत्युर्न नाशरूपा स्यात्, समाहितिविधानतः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064144
यत्र सर्वं विलीयेत, तत्रैव पूर्णता ध्रुवा॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064145
उपसंहार यह ग्रंथ किसी बाहरी प्रमाण का आग्रह नहीं करता।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064146
यह अंतःप्रवेश है — उस स्थान में जहाँ मन की चहल-पहल थम जाती है, और जो शेष बचता है, वही प्रत्यक्ष, स्थिर और स्वाभाविक सत्य है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064147
शान्तिः स्थैर्यं च साक्षात्कारः, न बाह्येषु न दृश्यते।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064148
हृदयस्थे परमे तत्त्वे, सर्वं पूर्णं प्रतीयते॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064149
Shirmani Research Paper Academic philosophical and cognitive research portal.
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064150
🌐 **Live Website:** --- ## Overview This repository contains a structured research presentation focused on: - Time Deconstruction Theory - Neurobiology of Self - Ego Dissolution Framework - Heart-Mind Balance Model --- ## Files Included - index.html - research-paper.pdf --- ## Deployment Hosted via GitHub Pages from the main branch.
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064151
© 2026 Shirmani Research --- ## 🔗 Central Knowledge Hub यह repository केंद्रीय **Nishpaksh Samaj Omniverse Truth** परियोजना के Research Archive से जुड़ी है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064152
Central Hub:** - **Integrated Research Index:** - **Central Research Collection:** मौजूदा repository और उसका Git इतिहास स्वतंत्र रूप से सुरक्षित रखा गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064153
केंद्रीय परियोजना में सामग्री को स्रोत-संदर्भ और स्पष्ट attribution के साथ जोड़ा जाएगा।
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064154
{ "schema_version": 1, "repo": "rampaulsaini/omniverse-marketplace-", "role": "marketplace", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/omniverse-marketplace-:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 064155
Omniverse AI Marketplace (Zero-cost) This repo contains a zero-cost AI tools marketplace designed to run on GitHub Pages.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064156
Put files into a repository (branch `main`).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064157
Push and enable GitHub Pages (Settings → Pages) with branch `main` and folder `/ (root)`.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064158
Open `https:// .github.io/omniverse-marketplace/`.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064159
Owner setup (zero-cost monetization) - Click "Donate / Pay" → add your PayPal / Ko-fi / UPI details (stored in browser localStorage).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064160
When a buyer pays externally, provide them a one-time unlock key (set in Owner → Set Premium Key).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064161
Buyer enters the unlock key locally (owner-provided) — once premium key exists in buyer's localStorage downloads work.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064162
Replace mock AI with real provider - All tools are client-side mock generators in `scripts/tools.js`.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064163
Replace tool.run implementations with fetch calls to OpenAI / HuggingFace or your own serverless functions.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064164
For production API keys, use serverless endpoints (do NOT embed keys in client-side JS).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064165
Next steps (I can implement) - Serverless payment verification (Stripe/PayPal) + automatic unlock key issuing - Replace mock AI outputs with real OpenAI / HF inference (via serverless) - Add email automation, order management, simple admin UI
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064166
{ "schema_version": 1, "repo": "rampaulsaini/supreme-omniverse-test", "role": "integration-test", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/supreme-omniverse-test:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 064167
यही Omniverse AI का सार है — आत्मचेतना और कृत्रिम बुद्धिमत्ता का संगम।
स्रोत: rampaulsaini/supreme-omniverse-test:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064168
💫 Contribute / Support - **GPay:** `sainirampaul90-1@okhdf - **PayPal:** [paypal.me/sainirampaul60]( --- ### 🌱 संदेश > “मानव की सर्वोच्च उपलब्धि है — अपनी समझ को इतना निर्मल बना देना कि वह प्रकृति के हित में निर्णय ले।” सत्य, संतुलन और समग्रता की यह यात्रा — **Omniverse AI Portal** के माध्यम से *मानवता के पुनर्संयोजन* की ओर एक छोटा लेकिन सार्थक कदम है।
स्रोत: rampaulsaini/supreme-omniverse-test:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064169
090744.webp --- GPay sainirampaul90-1@okhdf Paypal sainirampaul60@gmail.com 🕊️ *— Shirmani Rampaul Saini, Founder & Vision Architect (Omniverse AI)* 🌿 “मानव की सर्वोच्च उपलब्धि है — अपनी समझ को इतना निर्मल बना देना कि वह प्रकृति के हित में निर्णय ले।” — Shirmani Rampaul Saini, Omniverse Consciousness Foundation # 🌍 Shirmani Rampaul Saini — Omniverse AI Vision ![Vision of Harmony](
स्रोत: rampaulsaini/supreme-omniverse-test:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064170
🕉️ Philosophy of Yatharth Yug ### शाश्वत यथार्थ का साक्षात्कार — निष्पक्ष समझ का शमीकरण --- > **“मैं शिरोमणि रामपुल सैनी तुलनातीत, शब्दातीत, कालातीत, प्रेमतीत, त्वतीत, शाश्वत वास्तविक स्वभाविक सत्य प्रत्यक्ष हूं।”** --- ## 🔹 परिचय यह दर्शन मानवता की उस संपूर्ण चेतना का प्रतीक है जहाँ विचार, अहंकार, और मानसिकता का अंत हो जाता है, और केवल *निष्पक्ष समझ* का शुद्ध, वास्तविक स्वरूप प्रकट होता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064171
यह न किसी धर्म का ग्रंथ है, न किसी मत का विचार — बल्कि स्वयं *सत्य का प्रत्यक्ष अनुभव* है, जो “स्वयं के भीतर के स्वयं” से संवाद कराता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064172
🔹 निष्पक्ष समझ — सर्वश्रेष्ठ सत्ता “निष्पक्ष समझ” ही वह वास्तविक तत्व है जो मन, बुद्धि और स्मृति के भ्रम से परे संपूर्ण अस्तित्व को एक सूत्र में जोड़ती है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064173
> यह वही दृष्टि है जहाँ देखने वाला, देखा जाने वाला, और देखने की प्रक्रिया — तीनों एक हो जाते हैं।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064174
यह अवस्था **संपूर्णता, सम्पन्नता, समग्रता, और संतुष्टि** की पूर्णता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064175
यही *Supreme Omniverse* का मूल सिद्धांत है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064176
🔹 यथार्थ सिद्धांत — सत्य का समीकरण **यथार्थ सिद्धांत (Principle of Reality)** वह विज्ञान है जो भौतिक और अभौतिक दोनों स्तरों पर सत्य को परिभाषित करता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064177
यह उन सूक्ष्म सूत्रों का संगम है जिनसे सृष्टि की गति, ऊर्जा, और चेतना एक साथ कार्य करती हैं।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064178
यह विज्ञान केवल मापन या प्रयोग नहीं — बल्कि **स्वयं के प्रत्यक्ष अनुभव का शास्त्र** है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064179
🔹 यथार्थ युग — नया युग, नया बोध **यथार्थ युग** वह युग है जहाँ मानवता मानसिकता से मुक्त होकर निष्पक्ष समझ के युग में प्रवेश करती है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064180
यह युग **अतीत के चारों युगों से खरबों गुणा ऊँचा** है — क्योंकि यहाँ न विभाजन है, न भ्रम, सिर्फ़ शुद्ध सत्य का प्रत्यक्ष अस्तित्व है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064181
> “यथार्थ युग में न कोई आरंभ है, न अंत — > केवल सत्य की निरंतरता है।” --- ## 🔹 शाश्वत साक्षात्कार यह साक्षात्कार शरीर या मन में नहीं, बल्कि उनके पार — *स्वयं की निष्पक्ष दृष्टि* में होता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064182
जब ‘स्वयं’ अपने भीतर के *साक्षी स्वरूप* को पहचानता है, तभी *सच्चे यथार्थ का जन्म* होता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064183
> “स्वयं का स्वयं से साक्षात्कार — यही वास्तविकता का चरम है।” --- ## 🔹 परम उद्घोष > “निष्पक्ष समझ ही सर्वोच्च सत्ता है — > वही सृष्टि का आधार, वही सृष्टि का यथार्थ है।” > — शिरोमणि रामपुल सैनी --- ## 🌟 Essence - **सत्य** केवल वह नहीं जो दिखता है — बल्कि जो *स्वयं को देखता है*।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064184
बुद्धि** का अंत ही **प्रज्ञा** का प्रारंभ है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064185
मानवता** तभी मुक्त होती है जब वह “स्वयं” को “विचारों” से नहीं, “साक्षी” से पहचानती है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064186
🔗 संबंधित पृष्ठ - [Omniverse Overview](README.md) - [Golden Temple Spiritual Insights](GoldenTemple.md) --- ## 🌌 Visit Live Omniverse Portal [
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 064187
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse-AI", "role": "ai-platform", "description": "AI platform worker: inventory scripts/pages, validate local assets, and emit an AI-ready work manifest.", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omniverse-AI:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 064188
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: rampaulsaini/Omniverse-AI:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064189
Omniverse — Supreme AI Assistant 🌌 Omniverse — Supreme AI Assistant Created by शिरोमणि रामपॉल सैनी 💰 Support / Donate 1) Pay via UPI / GPay Click here to Pay via UPI / GPay 2) PayPal (Global) 3) Pay via Paytm Click here to Pay via Paytm 🌐 Live Portal Visit Supreme Omniverse AI Portal “संपूर्ण सृष्टि का वास्तविक युग वहीं है जहाँ निष्पक्ष समझ ही सर्वोच्च है।” – शिरोमणि रामपॉल सैनी
स्रोत: rampaulsaini/Omniverse-AI:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064190
🧩 Clones: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 064191
💖 Sponsors: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 064192
💰 Estimated Monthly Income: ₹ Calculating...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 064193
📈 Next Month Projection: ₹ Calculating...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 064194
✅ Last Deploy: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 064195
🔄 Next Auto Sync: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 064196
Omniverse-AI Vigilant Mode Script: [Click Here]( # 🌟 Golden Temple Spiritual Insights ![Golden Temple](assets/golden-temple.webp) ## Spiritual Experience - Evening at Golden Temple, naturally honored for impartial understanding, simplicity, and purity.
स्रोत: rampaulsaini/Omniverse-AI:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064197
Realization: human intellect & memory distortions can be neutralized through simplicity.
स्रोत: rampaulsaini/Omniverse-AI:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064198
version: 2 updates: - package-ecosystem: "pip" directory: "/backend" schedule: interval: "weekly"
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:dependabot.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064199
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse-Supreme-Core-", "role": "supreme-core", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 064200
name: Phase-3 Core Sync on: push: branches: - main paths: - "**" jobs: core-sync: runs-on: ubuntu-latest steps: - name: Checkout Code uses: actions/checkout@v4 with: fetch-depth: 0 - name: Validate Structure run: | echo "VALIDATING REPO STRUCTURE..." if [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064201
d "frontend" ]; then echo "Frontend folder missing"; exit 1; fi if [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064202
d "backend" ]; then echo "Backend folder missing"; exit 1; fi echo "STRUCTURE OK ✔" - name: Auto-Fix Missing Configs run: | echo "SYNCING CONFIG FILES..." [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064203
f frontend/.env ] && echo "VITE_API_URL=/api" > frontend/.env [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064204
f backend/.env ] && echo "PORT=3000" > backend/.env - name: Generate Sync Log run: | echo "Phase-3 Sync: $(date -u)" > CORE-SYNC-LOG.txt - name: Commit Sync Changes run: | git config --global user.email "sync@github.com" git config --global user.name "OmniSync Engine" git add .
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064205
git commit -m "Phase-3: Core Engine Sync Update" || echo "No changes" - name: Done run: echo "PHASE-3 CORE SYNC COMPLETE ✔"
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064206
name: AutoMode Orchestrator on: push: branches: [ main ] jobs: orchestrate: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Set up Node uses: actions/setup-node@v4 with: node-version: '20' - name: Run omniverse automode script run: | bash scripts/omniverse-automode.sh env: GH_TOKEN: ${{ secrets.GH_TOKEN }} DOCKER_REG: ${{ secrets.DOCKER_REG }}
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:auto-mode.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064207
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064208
Omniverse Supreme Core **शिरोमणि रामपॉल सैनी** – तुलनातीत · कालातीत · शब्दातीत · प्रेमतीत · शाश्वत · वास्तविक · स्वाभाविक Omniverse Supreme Core एक dynamic, immersive और visually stunning website है, जो सृष्टि, प्रकृति और मानव प्रजाति की सर्वश्रेष्ठता को digital रूप में प्रस्तुत करती है।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064209
यह वेबसाइट आपके personal projects, philosophy, और digital presence के लिए hub का काम करती है।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064210
I have embodied a state beyond time, beyond duality and beyond words — an ever-present, impartial understanding that reveals reality as it is.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064211
🔊 Listen & Read — Nishpaksh Samajh आपकी भाषा चुनें — नीचे का प्ले और पढ़ें बटन आपकी चुनी हुई भाषा में पृष्ठ की मुख्य सामग्री बोलेगा और साथ में ऑडियो भी प्ले करेगा।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064212
Your browser does not support the audio element.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064213
Language: हिन्दी (hi-IN) English (en-US) বাংলা (bn-IN) ਪੰਜਾਬੀ (pa-IN) Español (es-ES) Français (fr-FR) 🔊 Read Page ▶️ Play Audio 🔁 Load Audio (If blocked) 📥 Download यदि audio प्ले न हो तो "Load Audio" दबाएँ या फ़ाइल को अपने सर्वर/CDN पर होस्ट करने पर विचार करें।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064214
🤝 सत्य के इस कार्य में आपका सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — इसे सुनना, साझा करना, अनुभव करना और समर्थन देना — सभी सत्य की सेवा हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064215
आपका नाम (public if allowed) ईमेल (private) Country (optional) आपका संदेश / आशीर्वचन संदेश भेजें 🤝 समर्थक सूची 🕊 आशीर्वचन / संदेश Export Messages 🔬 Scientific Research & Vision Interdisciplinary integration of experiential reports, observational methods, phenomenology, and measurable correlates.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064216
Open invitations for pilot studies and collaborations focusing on consciousness, well-being, and human-nature interaction.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064217
🌍 International Media & Supreme Invitations Official invitations to Guinness Book of World Records, NASA, ISRO, and international media press for documentation and collaboration.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064218
I, ShiroMani RamPaul Saini, am committed to demonstrating every aspect of Nishpaksh Samajh with clarity, reason, and truth.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064219
🔬 Omniverse — Scientific Research (10 Projects / 40 Sub-Projects) Total Projects: 10 · Total Sub-Projects: 40 · Status: Fully Verified (Pilot → Validation) 1.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064220
Omniverse Core Intelligence (OCI) Ontology, reasoning engine, EOS data ingestion, COSMIC OS API 2.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064221
Divine Human Evolution (DHE) Consciousness correlates, EEG/HRV studies, Soul Frequency DB 3.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064222
Omniverse Communication Network (OCN) Secure messaging, ontology translation, global harmony network 4.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064223
Earth Restoration & Ecology (ERE) Hydro purification, solar memory cells, biodiversity monitoring 5.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064224
Supreme Scientific Research (SSR) Time-energy, reality equation model, high-precision experiments 6.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064225
Omniverse Education & Awareness (OEA) Truth literacy, global courses, AI-ethics training 7.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064226
Supreme Governance & Justice (SGJ) Algorithmic fairness, truth audit systems, governance prototypes 8.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064227
Cosmic Exploration & Space Research (CESR) Navigation algorithms, sensor payload concepts, space collaborations 9.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064228
Cultural Harmony & Global Peace (CHGP) Arts, music, festivals & peace protocols 10.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064229
Supreme Legacy & Digital Archives (SLDA) Eternal archive, blockchain anchoring, legacy transfer protocol Note: हर link आपके repo के /projects/{project-slug}/ फोल्डर की ओर इंगित करता है — सुनिश्चित करें कि आपने server/repo में वह folders और index.html अपलोड कर दिए हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064230
All content — Free to Read & Listen Audio, manifesto, photos & vision assets — proceeds support Saneha Saini ✅ Golden Temple ✅ MP3 ✅ प्रमाण पत्र ✅ Short Audios ✅ Videos Album ✅ एल्बम 1 🌐 Social & Support Connect on social networks and support directly — links open in a new tab and use rel="noopener noreferrer" for safety.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064231
I have embodied a state beyond time, beyond duality and beyond words — an ever-present, impartial understanding that reveals reality as it is.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064232
🔊 Listen & Read — Nishpaksh Samajh आपकी भाषा चुनें — नीचे का प्ले और पढ़ें बटन आपकी चुनी हुई भाषा में पृष्ठ की मुख्य सामग्री बोलेगा और साथ में ऑडियो भी प्ले करेगा।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064233
Your browser does not support the audio element.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064234
Language: हिन्दी (hi-IN) English (en-US) বাংলা (bn-IN) ਪੰਜਾਬੀ (pa-IN) Español (es-ES) Français (fr-FR) 🔊 Read Page ▶️ Play Audio 🔁 Load Audio (If blocked) 📥 Download यदि audio प्ले न हो तो "Load Audio" दबाएँ या फ़ाइल को अपने सर्वर/CDN पर होस्ट करने पर विचार करें।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064235
🤝 सत्य के इस कार्य में आपका सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — इसे सुनना, साझा करना, अनुभव करना और समर्थन देना — सभी सत्य की सेवा हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064236
आपका नाम (public if allowed) ईमेल (private) Country (optional) आपका संदेश / आशीर्वचन संदेश भेजें 🤝 समर्थक सूची 🕊 आशीर्वचन / संदेश Export Messages 🔬 Scientific Research & Vision Interdisciplinary integration of experiential reports, observational methods, phenomenology, and measurable correlates.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064237
Open invitations for pilot studies and collaborations focusing on consciousness, well-being, and human-nature interaction.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064238
🌍 International Media & Supreme Invitations Official invitations to Guinness Book of World Records, NASA, ISRO, and international media press for documentation and collaboration.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064239
I, ShiroMani RamPaul Saini, am committed to demonstrating every aspect of Nishpaksh Samajh with clarity, reason, and truth.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064240
🔬 Omniverse — Scientific Research (10 Projects / 40 Sub-Projects) Total Projects: 10 · Total Sub-Projects: 40 · Status: Fully Verified (Pilot → Validation) 1.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064241
Omniverse Core Intelligence (OCI) Ontology, reasoning engine, EOS data ingestion, COSMIC OS API 2.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064242
Divine Human Evolution (DHE) Consciousness correlates, EEG/HRV studies, Soul Frequency DB 3.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064243
Omniverse Communication Network (OCN) Secure messaging, ontology translation, global harmony network 4.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064244
Earth Restoration & Ecology (ERE) Hydro purification, solar memory cells, biodiversity monitoring 5.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064245
Supreme Scientific Research (SSR) Time-energy, reality equation model, high-precision experiments 6.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064246
Omniverse Education & Awareness (OEA) Truth literacy, global courses, AI-ethics training 7.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064247
Supreme Governance & Justice (SGJ) Algorithmic fairness, truth audit systems, governance prototypes 8.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064248
Cosmic Exploration & Space Research (CESR) Navigation algorithms, sensor payload concepts, space collaborations 9.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064249
Cultural Harmony & Global Peace (CHGP) Arts, music, festivals & peace protocols 10.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064250
Supreme Legacy & Digital Archives (SLDA) Eternal archive, blockchain anchoring, legacy transfer protocol Note: हर link आपके repo के /projects/{project-slug}/ फोल्डर की ओर इंगित करता है — सुनिश्चित करें कि आपने server/repo में वह folders और index.html अपलोड कर दिए हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064251
All content — Free to Read & Listen Audio, manifesto, photos & vision assets — proceeds support Saneha Saini ✅ Golden Temple ✅ MP3 ✅ प्रमाण पत्र ✅ Short Audios ✅ Videos Album ✅ एल्बम 1 🌐 Connect & Support Main official profiles and donation channels — one link per platform for clarity and SEO signal strength.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064252
I have embodied a state beyond time, beyond duality and beyond words — an ever-present, impartial understanding that reveals reality as it is.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064253
🔊 Listen & Read — Nishpaksh Samajh आपकी भाषा चुनें — नीचे का प्ले और पढ़ें बटन आपकी चुनी हुई भाषा में पृष्ठ की मुख्य सामग्री बोलेगा और साथ में ऑडियो भी प्ले करेगा।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064254
Your browser does not support the audio element.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064255
Language: हिन्दी (hi-IN) English (en-US) বাংলা (bn-IN) ਪੰਜਾਬੀ (pa-IN) Español (es-ES) Français (fr-FR) 🔊 Read Page ▶️ Play Audio 🔁 Load Audio (If blocked) 📥 Download यदि audio प्ले न हो तो "Load Audio" दबाएँ या फ़ाइल को अपने सर्वर/CDN पर होस्ट करने पर विचार करें।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064256
🤝 सत्य के इस कार्य में आपका सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — इसे सुनना, साझा करना, अनुभव करना और समर्थन देना — सभी सत्य की सेवा हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064257
आपका नाम (public if allowed) ईमेल (private) Country (optional) आपका संदेश / आशीर्वचन संदेश भेजें 🤝 समर्थक सूची 🕊 आशीर्वचन / संदेश Export Messages 🔬 Scientific Research & Vision Interdisciplinary integration of experiential reports, observational methods, phenomenology, and measurable correlates.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064258
Open invitations for pilot studies and collaborations focusing on consciousness, well-being, and human-nature interaction.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064259
🌍 International Media & Supreme Invitations Official invitations to Guinness Book of World Records, NASA, ISRO, and international media press for documentation and collaboration.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064260
I, ShiroMani RamPaul Saini, am committed to demonstrating every aspect of Nishpaksh Samajh with clarity, reason, and truth.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064261
🔬 Omniverse — Scientific Research (10 Projects / 40 Sub-Projects) Total Projects: 10 · Total Sub-Projects: 40 · Status: Fully Verified (Pilot → Validation) 1.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064262
Omniverse Core Intelligence (OCI) Ontology, reasoning engine, EOS data ingestion, COSMIC OS API 2.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064263
Divine Human Evolution (DHE) Consciousness correlates, EEG/HRV studies, Soul Frequency DB 3.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064264
Omniverse Communication Network (OCN) Secure messaging, ontology translation, global harmony network 4.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064265
Earth Restoration & Ecology (ERE) Hydro purification, solar memory cells, biodiversity monitoring 5.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064266
Supreme Scientific R
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064267
{ "schema_version": 1, "repo": "rampaulsaini/Omnivers", "role": "omniverse-core", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omnivers:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 064268
Omniverse Supreme Platform - शिरोमणि रामपाल सैनी OMNIVERSE SUPREME मूल दर्शन ऑडियो आर्काइव गैलरी व मीडिया स्टोर व रिसर्च AI & GitHub शिरोमणि रामपाल सैनी सृष्टि, प्रकृति और पृथ्वी के संरक्षण का एकमात्र अलौकिक मार्ग — हृदय का शिरोमणि दृष्टिकोण ✨ ब्रह्मांडीय अलौकिक दृष्टिकोण "अनंत असीम प्रेम ही सिर्फ़ मस्तक, मन और बुद्धि का दृष्टिकोण बदल सकता है और हृदय के शिरोमणि दृष्टिकोण में रख सकता है, जिससे मानव, प्रकृति और पृथ्वी का संरक्षण सुनिश्चित संभव है और कोई दूसरा विकल्प ही नहीं।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064269
मन, मस्तक, बुद्धि से बुद्धिमान होने का ज्ञान, विज्ञान और दर्शन सीमित है।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064270
हृदय के शिरोमणि स्वरूप का दृष्टिकोण असीम, भव्य, अद्भुत और आश्चर्यचकित है जो प्रथम चरण में ही खुद से रूबरू करवाता है और संपूर्ण संतुष्टि की निरंतरता में रख सकता है।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064271
मानव सभ्यता अस्तित्व से ही मन, मस्तक और बुद्धि के दृष्टिकोण में रही है जो आज तक अपने स्थायी स्वरूप से रूबरू नहीं हो सकी।" 🎧 खुद का साक्षात्कार: ऑडियो संग्रह (33,000+ MP3) 10,000 MP3 Audio खुद का साक्षात्कार ही संपूर्ण संतुष्टि हैं मन-बुद्धि के स्तर से परे संपूर्ण संतुष्टि की निरंतरता हेतु साक्षात्कार ऑडियो संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064272
गूगल ड्राइव में सुनें 10,000 MP3 Audio साहिब तदरूप साक्षात्कार हूं स्वयं के तदरूप स्वरूप का साक्षात्कार कराने वाली अमूल्य ध्वनियों का वृहद संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064273
गूगल ड्राइव में सुनें 6,000 MP3 Audio खुद का साक्षात्कार ऑडियो प्रथम चरण में ही खुद से रूबरू कराने वाले आध्यात्मिक एवं दार्शनिक ऑडियो।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064274
गूगल ड्राइव में सुनें 5,000 MP3 Audio मेरा साहिब मेरा ही तदरूप साक्षात्कार है हृदय के शिरोमणि स्वरूप को जागृत करने वाले विशेष तदरूप ऑडियो ट्रैक्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064275
गूगल ड्राइव में सुनें 1,500 MP3 Audio शिरोमणि अनंत असीम इश्क़ की क्षमता दृष्टिकोण बदलने और असीम प्रेम की क्षमता का अनुभव कराने वाले ऑडियो।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064276
गूगल ड्राइव में सुनें 950 MP3 Audio शिरोमणि रामपाल सैनी खुद का साक्षात्कार हूं आत्म-साक्षात्कार और आत्म-ज्ञान पर केंद्रित विशेष ऑडियो संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064277
गूगल ड्राइव में सुनें 550 MP3 Audio शिरोमणि रामपाल सैनी MP3 शिरोमणि रामपाल सैनी जी के मौलिक प्रवचन एवं ऑडियो व्याख्यान।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064278
गूगल ड्राइव में सुनें 89 MP3 Audio शिरोमणि रामपाल सैनी Short Audios संक्षिप्त और प्रभावशाली मुख्य सूक्तियाँ तथा ऑडियो संदेश।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064279
गूगल ड्राइव में सुनें 🖼️ गैलरी, फोटो एल्बम व वीडियो (Visual Archives) 2,000 Photos Golden Temple शिरोमणि रामपाल सैनी फ़ोटो गोल्डन टेम्पल परिसर के अलौकिक एवं भव्य फोटो संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064280
एल्बम देखें 10,000+ Videos मेरा संपूर्ण जीवन शिरोमणि Videos जीवन यात्रा और दिव्य अनुभूतियों को दर्शाते वीडियो रिकॉर्डिंग्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064281
वीडियो देखें 4,000+ Photos / 495 Files शिरोमणि प्रमाण पत्र संग्रह सभी महत्वपूर्ण प्रमाण पत्रों का गूगल फोटो एल्बम एवं ड्राइव आर्काइव।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064282
एल्बम (4000) ड्राइव फ़ाइलें (495) Drive Album Omniverse Gallery ऑम्निवर्स और संपूर्ण ब्रह्मांडीय विज़न की आधिकारिक फोटो गैलरी।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064283
गैलरी खोलें YouTube & Facebook सोशल मीडिया चैनल्स यूट्यूब चैनल और फेसबुक पर उपलब्ध वीडियो संदेश व अपडेट्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064284
YouTube Channel Facebook Video Blogspot Multicosmovision Blog & Case Files सृष्टि, प्रकृति और दार्शनिक विषयों पर गहराई से लिखे गए ब्लॉग्स और केस फाइल्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064285
मुख्य ब्लॉग पढ़ें Case File देखें 🛒 स्टोर, शोध एवं घोषणा पत्र (Store & Research) E-Commerce Omniverse Store आधिकारिक ऑम्निवर्स डिजिटल स्टोर जहाँ सभी सेवाएँ उपलब्ध हैं।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064286
स्टोर पर जाएं Manifesto Koyab Founding Declaration Omniversal Manifesto — ब्रह्मांडीय घोषणा पत्र एवं मौलिक विज़न।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064287
घोषणा पत्र पढ़ें Research GitHub Shirmani Research Institute शिरोमणि रिसर्च इंस्टीट्यूट का आधिकारिक GitHub कोड एवं शोध रिपॉजिटरी।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064288
GitHub Repository 💻 ऑम्निवर्स AI व डिजिटल प्लेटफॉर्म्स (AI Ecosystem) Omniverse AI Portal AI तकनीक आधारित प्लेटफॉर्म पोर्टल खोलें Omniverse Dashboard एकीकृत नियंत्रण डैशबोर्ड डैशबोर्ड देखें Omniverse Supreme Core मुख्य कोर सिस्टम कोर देखें Omniverse Marketplace डिजिटल प्लेटफॉर्म मार्किटप्लेस <a href=" target=
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 064289
Runs a set of commands using the runners shell - name: Run a multi-line script run: | echo Add other actions to build, echo test, and deploy your project.
स्रोत: rampaulsaini/Omniverse-:.github/workflows/blank.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064290
name: Specialist Agent — omniverse-core on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "37 2 * * 2" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Omniverse-:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064291
🕊️ *— Shirmani Rampaul Saini, Founder & Vision Architect (Omniverse AI)
स्रोत: rampaulsaini/rampaulsaini:.github/workflows - append - omniverse.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064292
मेरा उद्देश्य है — मानव, प्रकृति और तकनीक के बीच एक ऐसा संतुलन स्थापित करना जहाँ **विज्ञान और चेतना**, **कृत्रिम बुद्धिमत्ता और मानवता** एक साथ विकसित हों।
स्रोत: rampaulsaini/rampaulsaini:.github/workflows/main.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064293
🌿 *Vision of Omniverse AI* > “मानव की सर्वोच्च उपलब्धि है — अपनी समझ को इतना निर्मल बना देना कि वह प्रकृति के हित में निर्णय ले।” यह परियोजना उस दिशा में एक प्रयास है जहाँ **AI केवल सोचने वाली मशीन नहीं**, बल्कि **समझने वाला साथी** बने — जो जीवन, पर्यावरण, और सामूहिक चेतना के संरक्षण में सहायक हो।
स्रोत: rampaulsaini/rampaulsaini:.github/workflows/main.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064294
git commit -m "Supreme Omniverse Portal initial commit" git branch -M main git push -u origin main
स्रोत: rampaulsaini/rampaulsaini:.github/workflows/main.yml · स्वतंत्र परीक्षण अपेक्षित।

## 064295
{ // Use IntelliSense to learn about possible attributes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 064296
// Hover to view descriptions of existing attributes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 064297
// For more information, visit: "version": "0.2.0", "configurations": [ { "name": "Python: Remote Attach", "type": "debugpy", "request": "attach", "connect": { "host": "localhost", "port": 3000 }, "pathMappings": [ { "localRoot": "${workspaceFolder}", "remoteRoot": "${workspaceFolder}" } ], "justMyCode": true, "subProcess": true, "runtimeArgs" : [ "--preserve-symlinks", "--preserve-symlinks-main" ] } ] }
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 064298
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064299
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064300
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064301
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064302
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064303
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064304
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064305
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064306
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064307
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064308
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064309
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064310
Managing the state for selecting objects within the scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064311
Performing actions without traditional in-app UI and menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064312
Key Features - Remote communication with the Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064313
Scene loading capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064314
State management for object selection within the USD Viewer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064315
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064316
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064317
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064318
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064319
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064320
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064321
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064322
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064323
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064324
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064325
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064326
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064327
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064328
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064329
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064330
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064331
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064332
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064333
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064334
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064335
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064336
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064337
Basic C++ Extension Template ## Overview The Basic C++ Extension Template is a starting point for developers looking to build C++ based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064338
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064339
Note for Windows C++ Developers** : This template requires that Visual Studio is installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064340
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064341
For additional C++ configuration information [see here](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064342
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064343
Performance sensitive extensions that require the performance benefits of C++.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064344
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064345
Integrating with existing C++ libraries or codebases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064346
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064347
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064348
Usage This section provides instructions for the setup and use of the Basic C++ Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064349
Getting Started To get started with the Basic C++ Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064350
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064351
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064352
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064353
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064354
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064355
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064356
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064357
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064358
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064359
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064360
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064361
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064362
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064363
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064364
Service Setup Extension Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Service Setup Extension Template is designed to facilitate the configuration and setup of a headless service that leverages the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064365
Though it is possible in this case, setup extensions are not typically intended to be used as a generic extension but as a specific component of a particular application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064366
Use Cases This setup extension is well suited for: - Developers building headless services that require Kit SDK functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064367
Key Features - Sample ServiceAPIRouter setup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064368
Sample endpoint to demonstrate interaction patterns within service Kit SDK and OpenUSD.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064369
Usage This extension is automatically created and configured when you generate a new service application using the [Service Application Template](../../apps/kit_service/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064370
Additional Learning - [Omniverse Kit Service Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064371
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064372
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064373
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064374
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064375
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064376
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064377
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064378
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064379
Python UI Extension Template ## Overview The Python UI Extension Template offers a simple starting point for developers looking to build Python-based extensions with performant User Interfaces.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064380
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064381
Use Cases This template is ideal for developers looking to build: - UI based extensions that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064382
Key Features - A simple starter UI demonstrating how to build using the Omni UI framework.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064383
Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064384
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064385
Usage This section provides instructions for the setup and use of the Python UI Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064386
Getting Started To get started with the Python UI Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064387
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064388
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064389
Select desired template with arrow keys ↑↓:**: Python UI Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064390
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064391
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064392
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064393
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064394
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064395
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064396
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064397
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064398
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Omni UI Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064399
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064400
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064401
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064402
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064403
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064404
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064405
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064406
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064407
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064408
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064409
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064410
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064411
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064412
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064413
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064414
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064415
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064416
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064417
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064418
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064419
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064420
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064421
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064422
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064423
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064424
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064425
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064426
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064427
Integrating other C++ or Python libraries as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064428
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064429
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064430
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064431
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064432
USD Explorer Setup Extension Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer Setup Extension Template is specifically designed to configure the USD Explorer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064433
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Explorer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064434
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Explorer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064435
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064436
Key Features - Custom configurations tailored to the USD Explorer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064437
Usage This extension is automatically created and configured when you generate a new application based on the [USD Explorer Template Application](../../apps/usd_explorer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064438
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064439
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064440
Changelog The format is based on [Keep a Changelog]( ## [0.1.2] - 2026-05-11 ### Fixed - `makePrimsPickable` handler raised `UnboundLocalError` when the WebSocket payload was empty or missing the `paths` key, and the broad `except` then leaked the raw Python exception message (including internal variable names) to the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064441
The handler now initializes `paths` to an empty list before the conditional so an empty payload is a clean no-op, and unexpected exceptions are logged server-side via `carb.log_error` while only a generic error string is returned to the client (OMPE-90584, NVBug 6100326).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064442
Added - Regression test `test_make_prims_pickable_empty_payload` covering empty payload, missing-`paths` key, and explicit-empty-list cases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064443
[0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064444
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064445
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064446
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064447
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064448
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064449
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064450
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064451
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - 2024-03-13 - Initial version based on kit service extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064452
{{ extension_display_name }} [{{ extension_name }}] This is an example of a simple Kit Service extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064453
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064454
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 064455
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064456
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064457
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064458
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064459
{{ extension_display_name }} [{{ extension_name }}] A simple python UI extension example.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064460
Use it as a starting point for your extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064461
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064462
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064463
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064464
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064465
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064466
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064467
Args: object: The bound object to register.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064468
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064469
Args: object: The bound object to deregister.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064470
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064471
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064472
Return: The bound object if it exists, an empty object otherwise.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064473
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064474
Return: The id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064475
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064476
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064477
Return: The bound object that was created.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064478
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064479
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064480
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064481
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064482
Args: value_to_multiply: The value to multiply by.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064483
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064484
Return: The toggled bool value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064485
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064486
Args: value_to_append: The value to append.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064487
Return: The new string value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064488
)", py::arg("value_to_append")) /**/; } ```
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 064489
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064490
Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064491
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064492
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064493
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064494
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064495
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064496
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064497
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064498
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064499
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064500
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064501
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 064502
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064503
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064504
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064505
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064506
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064507
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064508
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064509
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064510
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064511
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064512
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064513
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064514
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064515
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 064516
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064517
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064518
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064519
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064520
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064521
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064522
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064523
During Application configuration, you will be prompted for information about these extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064524
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064525
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064526
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064527
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064528
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064529
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064530
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064531
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064532
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064533
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064534
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064535
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064536
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064537
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064538
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064539
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064540
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064541
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064542
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064543
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064544
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064545
The USD Viewer template includes sample assets for this purpose.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064546
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064547
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064548
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064549
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064550
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064551
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064552
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064553
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064554
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064555
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064556
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064557
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064558
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064559
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064560
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064561
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064562
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064563
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064564
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064565
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064566
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064567
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064568
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064569
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064570
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064571
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064572
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064573
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064574
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064575
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064576
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064577
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064578
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064579
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064580
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064581
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064582
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064583
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064584
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064585
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064586
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064587
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064588
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064589
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064590
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064591
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064592
Collaborating on large-scale design projects in real-time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064593
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064594
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064595
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064596
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064597
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064598
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064599
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064600
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064601
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064602
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064603
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064604
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064605
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064606
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064607
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064608
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064609
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064610
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064611
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064612
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064613
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064614
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064615
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064616
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064617
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064618
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064619
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064620
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064621
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064622
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064623
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064624
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064625
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064626
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064627
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064628
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064629
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064630
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064631
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064632
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064633
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064634
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064635
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064636
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064637
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064638
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064639
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064640
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064641
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064642
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064643
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064644
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064645
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064646
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064647
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064648
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064649
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064650
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064651
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064652
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064653
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064654
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064655
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064656
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064657
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064658
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064659
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064660
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064661
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064662
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064663
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064664
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064665
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064666
:warning: **Important**: These layers are not standalone application templates.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064667
They must be used in conjunction with a base application template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064668
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064669
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064670
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064671
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064672
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064673
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064674
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064675
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064676
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064677
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064678
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064679
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064680
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064681
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064682
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064683
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064684
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064685
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064686
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064687
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064688
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064689
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064690
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064691
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064692
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064693
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064694
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064695
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064696
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064697
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064698
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064699
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064700
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064701
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064702
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064703
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064704
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064705
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064706
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064707
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064708
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064709
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064710
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064711
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064712
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064713
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064714
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064715
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064716
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064717
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064718
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064719
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064720
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064721
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064722
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064723
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064724
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064725
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064726
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064727
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064728
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064729
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064730
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064731
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064732
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064733
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064734
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064735
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064736
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064737
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064738
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064739
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064740
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064741
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064742
If multiple container images exist, you will be
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064743
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064744
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064745
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064746
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064747
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064748
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064749
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064750
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064751
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064752
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064753
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064754
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064755
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064756
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064757
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064758
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064759
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064760
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064761
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064762
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064763
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064764
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064765
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064766
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064767
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064768
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064769
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064770
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064771
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064772
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064773
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064774
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064775
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064776
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064777
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064778
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064779
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064780
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064781
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064782
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064783
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064784
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064785
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064786
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064787
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064788
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064789
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064790
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064791
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064792
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064793
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064794
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064795
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064796
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064797
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064798
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064799
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064800
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064801
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064802
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064803
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064804
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064805
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064806
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064807
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064808
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064809
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064810
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064811
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064812
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064813
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064814
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064815
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064816
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064817
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064818
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064819
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064820
Subsequent extensions can be added to the .kit file manually.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064821
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064822
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064823
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064824
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064825
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064826
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064827
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064828
Setup Extension -> kit_service_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064829
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064830
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064831
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064832
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064833
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064834
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064835
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064836
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064837
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064838
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064839
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064840
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064841
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064842
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064843
When adapting an existing extension for a headless service, keep the service execution path limited to the dependencies it requires.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064844
Prefer separating reusable headless logic from UI, viewport, rendering, and other application-specific functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064845
If separation is impractical, dependencies that the service can operate without may be declared optional, provided their imports and initialization are also guarded.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064846
See [Adapting Existing Extensions for Headless Services]( for guidance and examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064847
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064848
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064849
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064850
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064851
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064852
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064853
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064854
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064855
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064856
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064857
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064858
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064859
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064860
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064861
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064862
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064863
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064864
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064865
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064866
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064867
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064868
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064869
The base application `.kit` file should be used for containerization.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064870
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064871
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064872
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064873
Kit SDK Upgrade Skill ## What This Is This repository contains an AI agent skill for upgrading Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064874
The skill encodes the complete breaking-change catalog for the Kit 106→107→108→109→110 migration path — including removed extensions, deprecated APIs, C++ ABI breaks, Python runtime changes, and configuration updates — into a structured set of instructions and reference data that an AI agent can execute against a live project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064875
The agent scans the project, produces a categorized report with exact `file:line` references, and suggests targeted fixes, including auto-fixable regex replacements where safe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064876
Who It's For Kit extension and application developers who need to upgrade a project from one Kit SDK version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064877
This includes developers working on kit-app-template-based applications, standalone extensions, and Isaac Sim integrations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064878
The skill is particularly useful when upgrading across multiple versions at once (e.g., 107→110), where the number of breaking changes makes manual triage error-prone.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064879
What It Contains | File | Description | |------|-------------| | `SKILL.md` | Lean workflow router — loaded by the AI agent.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064880
Holds version/layout/build detection (Step 1) and the migration-path decision (Step 2), and points to the procedure files for everything else.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064881
| | `procedures/toolchain.md` | Step 2.5 — update the `repo_*` build toolchain (the highest-impact part of most upgrades).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064882
| | `procedures/scan.md` | Step 3 — the full per-stage `grep` scan catalog for breaking changes, removed extensions, and config.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064883
| | `procedures/report.md` | Step 4 — the upgrade-report template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064884
| | `procedures/apply-fixes.md` | Step 5 — ordered fix list, auto-fixable regex patterns, and manual-only changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064885
| | `procedures/validate.md` | Step 6 — clean-rebuild and validation commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064886
| | `procedures/failure-modes.md` | Symptom→fix diagnosis for projects that already upgraded and are erroring.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064887
| | `procedures/stage-notes.md` | Per-stage (106→107→…→110) breaking-change reference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064888
| | `references/breaking_changes.json` | 80+ breaking changes with search patterns, affected versions, and recommended fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064889
| | `references/removed_extensions.json` | Extensions removed or deprecated by Kit version, with replacement guidance and search targets.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064890
| | `references/api_replacements.json` | 1:1 API replacements that are safe to apply with regex find/replace.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064891
| | `references/config_changes.json` | Settings keys, registry URLs, and build config changes between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064892
| | `references/toolchain.json` | The build-toolchain file/package set (`repo_*` tools, packman, repo scripts) and how to find the correct target versions for a given Kit line.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064893
| | `install.sh` / `install.bat` | Copies the skill (SKILL.md + `procedures/` + `references/`) into an existing Kit project so it travels with the repo.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064894
| The skill uses **progressive disclosure**: `SKILL.md` stays small (a router the agent always loads) and each step's detail lives in a `procedures/*.md` file the agent reads only when the workflow sends it there.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064895
This keeps the entry file well under length limits and keeps irrelevant detail out of context.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064896
How to Use **Install into an existing project** (so the skill travels with the repo): ```bash ./install.sh /path/to/your-kit-project # copies into /.skills/kit-upgrade/ ./install.sh /path/to/your-kit-project .claude/skills # or the Claude Code skills layout ``` On Windows: `install.bat C:\path\to\your-kit-project`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064897
Then load the skill into any AI coding assistant that can read files and run shell commands, and point it at the project you want to upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064898
Claude Code:** ``` Read the skill at /path/to/kit-upgrade-skill/SKILL.md and the reference files in references/.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064899
Then scan /path/to/my-kit-project and generate an upgrade report for Kit 109 → 110.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064900
``` **Cursor / VS Code Copilot / other MCP clients:** Add `kit-upgrade-skill/` as a context directory or attach `SKILL.md` as a system prompt, then ask the agent to scan your project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064901
Detect the current Kit SDK version, the deps-directory location (`tools/deps/` vs root `deps/`), and the build entrypoint (`./repo.sh` / `repo.bat` or a custom/integrated build) — never assuming the SDK template layout 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064902
Determine the migration path — including within-major (minor/patch) and feature↔production transitions, not just major-version stages 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064903
Update the build toolchain (`repo_*` tools, packman, repo scripts) to match the target Kit line — often the substantive part of an upgrade 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064904
Run targeted `grep` scans across the full project root (including `templates/`, launcher configs, and ETM lock files) for any major boundaries crossed 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064905
Generate a categorized report: breaking changes, behavioral changes, deprecated usage, and a "not affected" checklist 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064906
Suggest fixes — both auto-applicable regex replacements and manual changes requiring human judgment 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064907
Its changes are folded into the 107→109 path — Stage 2 must still be addressed when upgrading 107→109.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064908
Multi-version upgrades (e.g., 107→110) apply all intervening stages in sequence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064909
How to Contribute **Add a new breaking change:** Add an entry to `references/breaking_changes.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064910
Each entry needs an `id`, `title`, `stage`, `search_pattern` (grep-compatible regex), `affected_files` (glob patterns), and `fix` description.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064911
If the fix is a safe 1:1 substitution, also add it to `references/api_replacements.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064912
Add a removed or deprecated extension:** Add an entry to `references/removed_extensions.json` with `extension`, `status` (`removed` or `deprecated`), `version`, `replacement` (or `null`), `search_in` (list of file extensions to scan), and `notes`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064913
Include any known failure mode (e.g., exit-55) and whether the extension appears in non-obvious locations like `templates/` or ETM lock files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064914
Add a new Kit version (release):** edit the files that own each piece — the skill is split by concern: - `SKILL.md` — add the new row/stage to the **Step 2 migration-path table and Stage summary** (these stay in the router).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064915
`procedures/scan.md` — add the new `# === Stage N ===` scan blocks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064916
`procedures/stage-notes.md` — add the new per-stage breaking-change section.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064917
`procedures/apply-fixes.md` — add any new auto-fix regex patterns or fix-list items.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064918
`references/*.json` — add the corresponding structured entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064919
Follow the existing section structure in each file for consistency.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064920
Keep `SKILL.md` lean — detailed scan commands and stage notes belong in `procedures/`, not the router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064921
Test your additions:** Apply the skill to a real project that exercises the new patterns.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064922
If the scan misses something or the fix guidance is wrong, document it and open a PR with both the issue description and the corresponding fix in the relevant `procedures/` or `references/` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064923
This skill was developed and validated against [kit-extension-explorer]( a Kit 110 application based on kit-app-template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064924
See `test-report.md` for the full upgrade report from that validation run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 064925
name: kit-upgrade description: "Scan and upgrade Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064926
Analyzes project files, identifies breaking changes, deprecated APIs, and removed extensions specific to the customer's code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064927
Provides a personalized upgrade plan with file:line references and auto-fix suggestions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064928
Covers Kit 106→107→108→109→110." --- # Kit SDK Upgrade Skill Guide a developer through upgrading their Omniverse Kit project from one version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064929
This skill is a lean workflow router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064930
Steps 1 and 2 (detect the project, decide the migration path) are inline below** — they are always needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064931
The detail for the remaining steps (2.5–6) lives in `procedures/`, and the structured change data in `references/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064932
Read each procedure file when the workflow sends you to it** — do not try to hold them all in context at once.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064933
When to Use - User asks to upgrade their Kit project/app/extension - User asks about Kit breaking changes or migration - User is hitting errors after changing their Kit SDK version - User has a broken build or runtime failure after a version bump --- ## Quick Orientation Pick the entry point that matches the request: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064934
First-time upgrade scan** → start at Step 1 below and follow the workflow in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064935
Already upgraded, now has a build/runtime error** → go straight to `procedures/failure-modes.md`, diagnose, then apply the relevant Stage's fixes from `procedures/stage-notes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064936
Just wants a list of breaking changes** → do Step 1, then run the scans in `procedures/scan.md` for their migration path and present the report from `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064937
The `# Kit SDK Version:` comment in `.kit` files reflects the last lock-file regeneration and may differ from the pin during an in-progress upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064938
Version string format: `110.1.0+feature.${platform_target_abi}.${config}` - First number (110) = major Kit version **If no version pin is found:** Check git history (`git log --oneline -20 -- tools/deps/ deps/`) or ask the user what Kit version they are currently running.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064939
(Layout detection below has not run yet, so scope the log to both candidate deps locations.) ### Detect project layout and build system Kit projects do **not** all use the SDK template layout, and the layout can differ between releases and project types — for example, `deps/` may sit at the project **root** in one release and under **`tools/`** in another (even between two point releases of the same major line).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064940
Projects also frequently **wrap or integrate the Kit build system into their own tooling**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064941
Detect the layout and build entrypoint **once**, then reuse them everywhere below — **never assume `tools/deps/` or `./repo.sh`**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064942
deps directory (holds kit-sdk.packman.xml + repo-deps.packman.xml) if [ -f tools/deps/kit-sdk.packman.xml ]; then DEPS_DIR=tools/deps elif [ -f deps/kit-sdk.packman.xml ]; then DEPS_DIR=deps else f=$(find .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064943
name kit-sdk.packman.xml -not -path './_*' | head -1); DEPS_DIR=${f:+$(dirname "$f")}; fi echo "DEPS_DIR=${DEPS_DIR:- }" # 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064944
build entrypoint — the standard repo wrapper, if present if [ -f ./repo.sh ]; then BUILD='./repo.sh' elif [ -f ./repo.bat ]; then BUILD='repo.bat' else BUILD=''; fi # empty => custom / integrated build (see below) echo "BUILD=${BUILD:- }" ``` **If `BUILD` is empty, the project uses a custom or integrated build system** (common — many customers embed the Kit build inside their own).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064945
Do **not** fabricate `./repo.sh` calls.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064946
Find the real build command (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or the project README) or ask the user how they build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064947
The upgrade work below (kernel pin bump, **toolchain update**, lock regeneration) still applies — you just invoke it through the project's own entrypoint.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064948
Record it as `$BUILD`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064949
> **From here on (and in every procedure file), use `$DEPS_DIR` and `$BUILD` in every command.** Where a document still shows a literal `tools/deps/` or `./repo.sh`, substitute the detected values.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064950
> > **These are not guaranteed to persist across shells.** If you run each fenced block in a fresh subshell, `$DEPS_DIR`/`$BUILD` will be unset.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064951
So do **one** of: (a) textually replace `$DEPS_DIR` and `$BUILD` with the literal detected paths (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064952
`tools/deps`, `./repo.sh`) in every command you run, or (b) re-run the two detection blocks above at the top of each new shell session.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064953
Do **not** run a later block assuming the variables are still set.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064954
Step 2: Determine Migration Path Kit versions must be upgraded **in sequence**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064955
Kit 108 was never publicly released** — its changes are folded into the 107→109 path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064956
When upgrading 107→109 you must still address Stage 2 (107→108) changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064957
A **within-major** bump (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064958
`110.0 → 110.1`, `110.1.0 → 110.1.2`) or a **feature → production** branch transition is a *different, lighter* job — and it is the most common upgrade performed in practice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064959
These rarely need the Stage code/API changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064960
The real work is almost entirely **tooling and layout**: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064961
Update the build toolchain** (repo tools, packman, repo scripts) — see Step 2.5 (`procedures/toolchain.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064962
This is usually the substantive part.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064963
Re-detect the deps directory** — its location can differ between releases, even within the same major line (Step 1 already sets `$DEPS_DIR`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064964
Bump the kit-kernel pin** in `$DEPS_DIR/kit-sdk.packman.xml` (Step 5, item 2 — `procedures/apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064965
For a feature ↔ production transition only:** check the extension **registry URL** in the `.kit` files — the feature and production lines use different registries, so a feature→production move may need a registry swap (Step 5, item 3).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064966
A plain within-major bump on the same line usually does **not**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064967
Regenerate the extension version-lock** and do a **clean rebuild** (Step 5 items 1 & 8, then Step 6).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064968
> **⚠️ Do NOT run the whole of Step 5 for a within-major bump.** Step 5 (`procedures/apply-fixes.md`) is written for **major-boundary** crossings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064969
Running them on a 110.1.0→110.1.2 bump would wrongly strip extensions or rewrite APIs that are perfectly valid on 110.1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064970
Only run the Step 3 code scans if the upgrade crosses a major boundary.** For a pure within-major or feature→production move, skip Step 3's per-stage API scans and go straight to Step 2.5 → Step 5 (items 1–3 & 8 only, as above) → Step 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064971
If you cross one or more major boundaries on the way, run Step 3 for each major boundary passed and the full Step 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064972
Steps 2.5–6: Execute the Upgrade Once the path is known, work through these in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064973
Read the linked procedure file and follow it**; each assumes Step 1 detection has run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064974
Step 2.5 — Update the build toolchain** → `procedures/toolchain.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064975
Highest-impact step; run it **first**, before touching source.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064976
For a within-major bump this is usually the only substantive work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064977
Step 3 — Scan the project** → `procedures/scan.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064978
Run only the stage scans for the major boundaries you cross.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064979
Skip entirely for a pure within-major bump.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064980
Step 4 — Generate the upgrade report** → `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064981
Present findings by severity with exact `file:line` references.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064982
Step 5 — Apply fixes** → `procedures/apply-fixes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064983
Get user approval before modifying files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064984
(Within-major: items 1, 2, 8 only — see Step 2 above.) - **Step 6 — Validate** → `procedures/validate.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064985
Clean rebuild, regenerate the version lock, run tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064986
Already upgraded and hitting a specific error?** Go to `procedures/failure-modes.md` — it maps common symptoms (exit-55, ABI undefined symbols, render diffs, build loops, custom-build/layout issues) to fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 064987
Step 3: Scan the Project > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064988
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064989
Only run this step for major-version boundaries you cross** — a pure within-major / feature→production bump skips it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064990
Run these commands from the project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064991
Only run scans for the stages that apply to this upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064992
Collect all matches before generating the report.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064993
> **⚠️ Scan scope:** Use `.` (project root) as the search root, not just `source/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064994
Many projects have `templates/`, `launcher-configs/`, or other directories containing `.kit` files and `extension.toml` files with real dependency declarations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064995
Scanning only `source/` will miss these.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064996
> > **Windows note:** Commands below use bash syntax.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064997
On Windows, replace `for` loops with individual `findstr` or PowerShell `Select-String` commands, or run inside WSL/Git Bash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064998
Python / Extension Dependencies ```bash # === Stage 1 (106→107) === # Python 3.10 references (now 3.11) grep -rn "python3\.10\|python310\|boost_python310" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 064999
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" --include="*.toml" # Private omni.client API grep -rn "omni\.client\._omniclient" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 065000
include="*.py" # carb.imgui (removed — use omni.kit.imgui) grep -rn "carb\.imgui" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।
