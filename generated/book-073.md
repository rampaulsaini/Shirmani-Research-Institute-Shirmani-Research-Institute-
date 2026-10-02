# डिजिटल महाग्रंथ 073

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 072001
A failed provider does not silently become a successful generation.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072002
Automatic recovery is bounded and auditable.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072003
Software upgrades are signed/reviewed changes, not uncontrolled self-modification.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072004
Generated media is separated from temporary GPU files.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072005
Public media, live streaming, podcast, games, animation and advertising are adapter-driven capabilities; a UI card alone never claims a running backend.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072006
Required production topology Internet → HTTPS/CDN/WAF → API replicas → durable queue → GPU worker pool → object storage/CDN.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072007
Minimum high-availability target: 1.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072008
two API replicas; 2.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072009
durable PostgreSQL task state; 3.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072010
durable queue (Redis/RQ, Celery, or equivalent); 4.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072011
two independent GPU workers/providers; 5.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072012
versioned object storage; 6.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072013
external monitoring and alerting; 7.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072014
automated unhealthy-worker replacement; 8.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072015
backup and restore tests.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072016
Self-healing contract Automatic actions may: - retry transient provider failures with exponential backoff; - requeue recoverable work after process restart; - stop accepting AI work when readiness is false; - route work to a healthy secondary provider; - restart an unhealthy worker through the deployment orchestrator; - preserve failed tasks for inspection.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072017
Automatic actions must not: - invent successful output; - mark unverified media as VERIFIED; - expose secrets; - silently change application code; - bypass human/legal publication gates.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072018
Self-upgrade contract "Self-upgrading" means an agent may observe telemetry, propose a change, run deterministic tests, and prepare a signed/reviewed release.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072019
Production deployment remains gated by the release policy.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072020
This prevents an autonomous loop from modifying its own safety boundary.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072021
Public media capability map The public interface may expose these modules: - AI Music Studio - Creative Story/Film Studio - Live Podcast - Live Streaming - Live Production - Live News - Live Games - Animation/Cartoon - Creator/Economic Hub - Product offers and advertising - Social distribution - Endless episodic storytelling Each module requires an explicit backend adapter, rights/licensing policy, moderation controls, observability, and a publication state.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072022
"Planned", "ready", "live", and "verified" are distinct states.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072023
Advertising and offers Advertising should be first-party/consented and configurable.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072024
The system may schedule product cards, offers and campaign variants, but it must not fabricate availability, prices, endorsements, audience numbers, or performance metrics.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072025
Social posting requires platform-specific credentials and policy compliance.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072026
24/7 acceptance tests Before calling the service production-ready, continuously test: - API restart during generation; - GPU worker crash; - provider health loss and recovery; - queue recovery; - duplicate/idempotent submissions; - object-storage outage; - database restore; - one-provider loss with another provider available; - stale public status; - unauthorized task/audio access; - secret leakage scans; - signed release verification.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072027
Current free-testing boundary Google Colab + Quick Tunnel is a development/test path only.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072028
Its GPU runtime and public URL are temporary.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072029
The repository's notebook now sets a headless matplotlib backend before ACE-Step startup and waits for the engine health endpoint before exposing the test URL.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072030
Permanent availability requires persistent infrastructure.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_CONTROL_PLANE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072031
Yatharth Live Hub YATHARTH LIVE HUB Podcast • Voice • Live conversations • Public media ← Creator Hub LIVE MEDIA • निष्पक्ष समझ आवाज़ और विचार के लिए public stage.
स्रोत: rampaulsaini/yatharth-music-ai:live.html · स्वतंत्र परीक्षण अपेक्षित।

## 072032
शिरोमणि रामपाल सैनी की सार्वजनिक फोटो और voice-source entry को यहाँ स्पष्ट रूप से जोड़ा गया है।
स्रोत: rampaulsaini/yatharth-music-ai:live.html · स्वतंत्र परीक्षण अपेक्षित।

## 072033
Live streaming को तभी “LIVE” दिखाया जाएगा जब वास्तविक streaming provider connected हो।
स्रोत: rampaulsaini/yatharth-music-ai:live.html · स्वतंत्र परीक्षण अपेक्षित।

## 072034
निष्पक्ष समझ की आवाज़ Public voice source ▶ YouTube voice source खोलें → 🎙️ Podcast Studio Episode planning, script, show notes और audio workflow.
स्रोत: rampaulsaini/yatharth-music-ai:live.html · स्वतंत्र परीक्षण अपेक्षित।

## 072035
Planning available 🔴 Live Broadcast Streaming provider connection के बाद live publishing.
स्रोत: rampaulsaini/yatharth-music-ai:live.html · स्वतंत्र परीक्षण अपेक्षित।

## 072036
Provider connection required 🎧 निष्पक्ष समझ Voice Source सार्वजनिक voice source अभी YouTube channel से जुड़ा है; direct audio file तभी publish होगी जब वास्तविक audio asset उपलब्ध हो।
स्रोत: rampaulsaini/yatharth-music-ai:live.html · स्वतंत्र परीक्षण अपेक्षित।

## 072037
Open voice source → Creator Hub • Music • Creative Studio
स्रोत: rampaulsaini/yatharth-music-ai:live.html · स्वतंत्र परीक्षण अपेक्षित।

## 072038
Privacy Notice — Draft **Status:** Draft for the development project.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072039
Review and update this notice before collecting personal data or launching a public commercial service.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072040
What the current app stores The current backend keeps generation tasks in process memory.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072041
The browser stores local song-history metadata in local storage.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072042
Demo mode does not require an account.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072043
A future production deployment may process prompts, lyrics, generation metadata, account information, technical logs, and generated audio.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072044
The exact data collected must be documented before launch.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072045
Purpose Data should be processed only as necessary to provide music-generation features, maintain security, diagnose failures, improve reliability, and meet applicable legal obligations.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072046
Third parties A production deployment may send generation requests to an AI music engine such as ACE-Step.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072047
Operators must review the model/provider license and privacy terms before sending user content.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072048
User content Do not submit passwords, API keys, payment-card information, or other unnecessary sensitive information into prompts or lyrics.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072049
Retention and deletion The current in-memory task store is not durable.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072050
Production retention periods, account deletion, generated-audio deletion, backups, and log retention must be defined before launch.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072051
Contact Replace this section with the project operator's official privacy contact before public launch.
स्रोत: rampaulsaini/yatharth-music-ai:PRIVACY.md · स्वतंत्र परीक्षण अपेक्षित।

## 072052
Yatharth Music AI — RTX 4070 / ACE-Step GPU Benchmark This benchmark measures the **real Yatharth Music AI → FastAPI → ACE-Step** generation path.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072053
It is intended to answer: - How long does a 30s, 60s, or 180s generation actually take?
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072054
How much GPU power and VRAM are used?
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072055
What is the estimated GPU electricity cost per generation?
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072056
How much audio can one GPU theoretically generate per day?
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072057
What data should be used before setting paid-user limits?
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072058
> **Important:** This is a measurement tool, not a promise of performance.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072059
Run it on the exact GPU, ACE-Step model, quantization/offload settings, inference settings, and server configuration you intend to sell.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072060
What it measures The script submits a real request to `POST /api/generate`, then polls `GET /api/tasks/{task_id}` until the task completes.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072061
This means demo tones do **not** count.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072062
Why 30s / 60s / 180s?
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072063
Use three durations because generation speed is not always perfectly linear with requested audio duration: | Test | Purpose | |---|---| | 30 seconds | Fast sanity check and low-latency test | | 60 seconds | Representative short-song benchmark | | 180 seconds | Representative 3-minute-song benchmark | Run them **sequentially**.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072064
For capacity planning, keep ACE-Step `batch_size=1` so the benchmark represents one user's generation at a time.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072065
Requirements On the machine running Yatharth: - NVIDIA GPU with a working NVIDIA driver - `nvidia-smi` available for GPU power/VRAM measurements - Python 3.10+ - Yatharth Music AI running with `DEMO_MODE=false` - ACE-Step reachable through `MUSIC_ENGINE_URL` - Real ACE-Step generation working before benchmarking The benchmark itself uses Python's standard library and does not require `requests` or another extra package.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072066
Step 1 — Start the real Yatharth + ACE-Step stack Make sure the health endpoint reports real AI mode: ```bash curl ``` You want values equivalent to: ```json { "ok": true, "demo_mode": false, "engine_reachable": true } ``` If `demo_mode` is `true`, **stop**.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072067
The benchmark would not measure ACE-Step.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072068
Step 2 — Check the GPU ```bash nvidia-smi ``` For an RTX 4070, confirm that the expected NVIDIA GPU is shown and that memory is available before starting the benchmark.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072069
For a live view during testing: ```bash watch -n 1 nvidia-smi ``` On Windows, use: ```powershell nvidia-smi -l 1 ``` ## Step 3 — Run the benchmark From the repository root: ```bash python scripts/gpu_benchmark.py ``` Default tests: ```text 30s → 60s → 180s ``` The default electricity rate is ₹8/kWh.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072070
Capacity calculation The script reports a simple **generation-time-to-audio-time ratio**: ```text generation ratio = generation seconds ÷ requested audio seconds ``` For example, if a real 180-second song takes 90 seconds: ```text 90 ÷ 180 = 0.50x ``` That means the GPU is producing audio at approximately twice real-time under that exact test configuration.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072071
Paid-user planning The benchmark gives **audio capacity**, not a guaranteed number of customers.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072072
Convert it to customers only after deciding your plan's monthly generation allowance.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072073
For example: ```text Monthly audio capacity ÷ average audio minutes consumed per paid user = theoretical user capacity ``` Then apply a safety/availability margin.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072074
Example planning exercise (not a prediction): If a measured system can produce 1,000 three-minute songs/month under your chosen operating schedule, and a subscription allows 10 songs/month: ```text 1,000 ÷ 10 = 100 users ``` That is a **capacity calculation**, not a recommendation or guarantee.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072075
If users actually consume fewer songs, capacity may be higher; if they consume more, it may be lower.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072076
GPU purchase recovery If an RTX 4070 costs ₹69,000, do not calculate recovery from electricity alone.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072077
Track: ```text GPU/PC purchase + electricity + internet + storage + payment fees + hosting/domain + maintenance + taxes + refunds/credits ``` Then: ```text net contribution per paid generation = price collected - variable generation cost - payment fee - other variable costs ``` And: ```text break-even generations = total recoverable investment ÷ net contribution per generation ``` The benchmark supplies the generation-time and estimated GPU-energy inputs needed for this calculation.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072078
Recommended benchmark procedure for the RTX 4070 When the RTX 4070 is installed: 1.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072079
Install the NVIDIA driver and verify `nvidia-smi`.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072080
Start ACE-Step with the exact model/settings you intend to use in production.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072081
Start Yatharth with `DEMO_MODE=false`.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072082
Confirm `/api/health` reports `engine_reachable: true`.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072083
Keep `batch_size=1` for the single-user benchmark.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072084
Run 30s, 60s and 180s tests.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072085
Repeat the 60s test **at least 5 times** if you want a more reliable average.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072086
Save `gpu_benchmark_results.json` for comparison.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072087
Repeat after changing model quantization, offload, inference steps, or other generation settings.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072088
Compare **quality + generation time + VRAM + cost**, not speed alone.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072089
Important interpretation notes ### 1.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072090
GPU power is not whole-PC power `nvidia-smi` measures reported GPU power draw.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072091
A complete PC will consume additional power through the CPU, motherboard, RAM, SSD, fans, PSU losses, and other components.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072092
For a business cost model, measure wall power with a suitable power meter if possible.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072093
One generation is not necessarily one customer A customer may regenerate a song several times before downloading a result.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072094
Include retries/regenerations when calculating usage limits.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072095
Concurrent users change the result This benchmark is intentionally sequential.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072096
Once the single-generation baseline is known, run a separate controlled concurrency test before increasing `MAX_CONCURRENT_GENERATIONS`.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072097
Do not simply increase concurrency until the GPU crashes.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072098
Long songs may change memory/time behavior Always test the longest duration you intend to sell.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072099
The 180-second test is included specifically to expose problems that a 30-second test may miss.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072100
Benchmark after every major model/configuration change Record: - GPU model - VRAM - ACE-Step model/checkpoint - quantization/offload settings - inference steps - batch size - audio format - requested duration - generation time - peak VRAM - average/peak power - software versions This makes future hardware comparisons meaningful.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072101
Output for business planning After running the benchmark, bring the generated `gpu_benchmark_results.json` into the project discussion.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072102
The key numbers needed for the next calculation are: ```text 30s generation time 60s generation time 180s generation time peak VRAM average GPU power peak GPU power actual electricity tariff GPU/PC purchase price planned price per song or subscription songs included per user ``` Those figures can then be used to calculate a more realistic **₹/song, monthly capacity, break-even point, and operating-cost model** for Yatharth Music AI.
स्रोत: rampaulsaini/yatharth-music-ai:GPU_BENCHMARK.md · स्वतंत्र परीक्षण अपेक्षित।

## 072103
Yatharth Music AI — ₹0 setup This project supports a free-first development path using the open-source ACE-Step engine.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072104
Easiest path: local computer A local computer is the most reliable way to stay at ₹0 because there is no cloud GPU rental.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072105
ACE-Step can run with GPU acceleration and also supports CPU-only operation, although CPU generation can be much slower.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072106
Install Use Python 3.11 or 3.12.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072107
Install the official ACE-Step project and its dependencies from the official repository.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072108
Then start the ACE-Step API on port `8001`.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072109
Set Yatharth Music AI to: ```text DEMO_MODE=false MUSIC_ENGINE_URL= ``` Start the Yatharth backend on port `8000`, then open the Yatharth web app.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072110
Free Colab GPU Open `colab/Yatharth_Music_AI_Free_GPU.ipynb` in Google Colab and run the cells.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072111
The notebook is intended for temporary development/testing.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072112
Free Colab GPU access is dynamic, sessions can terminate, and it is not a dependable 24/7 public hosting solution.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072113
Hardware guidance - 6GB+ VRAM: a practical starting point for local GPU use.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072114
4GB VRAM: ACE-Step has lower-memory modes, but generation may require more aggressive memory management.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072115
CPU-only: possible, but expect substantially slower generation.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072116
Important architecture rule Do not put model weights, API keys, passwords, or private credentials into this GitHub repository.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072117
The public web app can remain in `DEMO_MODE=true` when no engine is connected.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072118
When a local or temporary ACE-Step engine is available, set `DEMO_MODE=false` and point `MUSIC_ENGINE_URL` at it.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072119
Cost target **Target: ₹0 for software and development.** A permanently available public AI music-generation server with guaranteed GPU capacity cannot honestly be promised at ₹0.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072120
If the project later needs 24/7 public generation, a paid GPU service may become necessary.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072121
Official project Use the official ACE-Step repository and documentation for the engine.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072122
Avoid unofficial websites claiming to be the official ACE-Step service.
स्रोत: rampaulsaini/yatharth-music-ai:FREE_SETUP.md · स्वतंत्र परीक्षण अपेक्षित।

## 072123
Yatharth Public Media Command Center YATHARTH PUBLIC MEDIA COMMAND CENTER एक विशाल creative media ecosystem Music, Creative Studio, live-media adapters, episodic storytelling, creator tools और first-party offers के लिए एक unified public interface.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072124
यह dashboard केवल उपलब्ध backend capability को LIVE दिखाता है; planned modules को स्वतः live घोषित नहीं करता।
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072125
🎵 Music Studio 🎬 Creative Studio 🧠 Automission Control 💼 Creator Hub AI Music CHECKING Original music generation, lyrics, multilingual controls and audio delivery.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072126
Creative Production READY Structured story, character, storyboard, music, animation and editing hand-offs.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072127
Live Podcast ADAPTER REQUIRED Live audio rooms, scheduling, moderation, recording and replay.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072128
Live Streaming ADAPTER REQUIRED Broadcast ingest, transcoding, CDN delivery, chat and moderation.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072129
Live Production ADAPTER REQUIRED Scenes, overlays, lower-thirds, media cues and production automation.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072130
News / Games / Animation ADAPTER REQUIRED Separate editorial, game and animation services with their own rights and QC boundaries.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072131
Endless Episodes PIPELINE READY A continuing story engine can create bounded episodes while preserving continuity and review gates.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072132
Offers & Advertising CAMPAIGN LAYER First-party product cards, offers, campaign variants and consent-aware social distribution.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072133
System Health CHECKING API readiness CHECKING AI provider CHECKING Durable recovery Reading verified runtime status… 24/7 boundary Software can automate detection, retry, recovery and failover, but no software-only design can honestly guarantee that hardware, power, network or an external provider will never fail.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072134
Production continuity therefore uses independent infrastructure and a second provider/worker.
स्रोत: rampaulsaini/yatharth-music-ai:public-media-command-center.html · स्वतंत्र परीक्षण अपेक्षित।

## 072135
Yatharth Digital Products YATHARTH DIGITAL PRODUCTS Reusable creative assets और production material का public catalog.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072136
← Creator Hub PRODUCT CATALOG • निष्पक्ष समझ डिजिटल सामग्री को उत्पाद की तरह प्रस्तुत करें।
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072137
यह catalog publishing-ready structure देता है।
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072138
हर item के साथ वास्तविक price, delivery method और purchase route तभी जोड़ा जाएगा जब वह सच में configured हो।
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072139
निष्पक्ष समझ शिरोमणि रामपाल सैनी स्रोत-आधारित creator identity.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072140
🎙️ आवाज़ / public source → 🎼 Music Creation Packs Song prompts, lyric frameworks, production briefs और reusable music workflows.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072141
Catalog item — publishing setup required ✍️ Story & Script Packs Story structures, character sheets, scene planning और storyboard templates.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072142
Catalog item — publishing setup required 🤖 Automission Templates AI-agent orchestration contracts, production manifests और workflow templates.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072143
Catalog item — publishing setup required 🎨 Creative Asset Packs Prompts, visual briefs, thumbnails, titles और presentation-ready creative assets.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072144
Catalog item — publishing setup required 🌐 Website / Studio Kits Creator landing pages, studio interfaces और deployment-ready UI packages.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072145
Catalog item — publishing setup required 📚 Yatharth Research Material Research, essays और structured public material को digital editions में व्यवस्थित करने का मार्ग.
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072146
Publication + commerce setup required Creator Hub • Music • Creative Studio
स्रोत: rampaulsaini/yatharth-music-ai:products.html · स्वतंत्र परीक्षण अपेक्षित।

## 072147
Production resilience ## What this solves The free-Colab experiment can fail before ACE-Step starts when the notebook exports Jupyter's `matplotlib_inline` backend.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072148
The resilient launcher forces the non-GUI `Agg` backend and refuses to start the public API until ACE-Step answers its health endpoint.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072149
Run: ```bash chmod +x scripts/launch_resilient.sh ACE_ROOT=/content/ACE-Step-1.5 \ YATHARTH_ROOT=/content/yatharth-music-ai \ scripts/launch_resilient.sh ``` ## What it does not promise A Colab runtime is ephemeral.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072150
A temporary tunnel is also ephemeral.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072151
Neither is a 24/7 production host.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072152
Permanent availability requires a persistent GPU/compute provider, persistent storage, monitoring, and an external process supervisor.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072153
The repository already keeps generation state durable and retries failed engine tasks.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072154
This launcher adds a deterministic startup gate so the application does not advertise a real-AI service while the engine is unavailable.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072155
24/7 target architecture Use these layers: 1.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072156
Public HTTPS edge / CDN / WAF.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072157
Stateless Yatharth API replicas.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072158
Durable task database/queue.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072159
GPU worker pool running ACE-Step.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072160
Object storage for generated media.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072161
Health checks + process restart.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072162
Metrics/logging/alerting.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072163
Signed, tested releases only for automatic upgrades.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072164
Human approval before public-content publication.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072165
Self-healing should retry/recover failed work; it should not silently rewrite or self-upgrade production code.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072166
Upgrades must remain auditable and reversible.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072167
Public production features The existing Studio API supports structured story, character, storyboard, music, animation, editing and QC stages.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072168
Live streaming, live production, news, games, cartoons, advertising, social publishing and an always-running episodic engine should be implemented as separate provider adapters and queues rather than being coupled to the music-generation process.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072169
No external render, stream, publication, audience count, advertisement delivery, or revenue result should be reported as complete until an actual provider returns verifiable evidence.
स्रोत: rampaulsaini/yatharth-music-ai:PRODUCTION_RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072170
Colab / ACE-Step startup resilience The Yatharth API can remain healthy while the ACE-Step engine is unavailable.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072171
The UI must therefore distinguish **API online** from **engine ready**.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072172
Known failure from the 2026-09-27 test ACE-Step exited during import because the notebook inherited: `MPLBACKEND=module://matplotlib_inline.backend_inline` ACE-Step is a server process, so use a headless backend before launching it: ```bash export MPLBACKEND=Agg uv run python -m acestep.api_server --host 127.0.0.1 --port 8001 ``` Then wait for the engine health/readiness endpoint before opening the public tunnel.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072173
GPU reality If `nvidia-smi` is unavailable, the free runtime has no NVIDIA GPU at that moment.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072174
Do not treat a public tunnel as proof that AI generation is ready.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072175
Keep the API available in fallback/demo mode and report engine_unreachable explicitly.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072176
Permanent-service rule Colab + a temporary trycloudflare URL is a test environment, not permanent hosting.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072177
Production requires a durable compute provider, persistent storage, queueing, health checks and a fallback provider.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072178
Current Colab failure guard If ACE-Step fails before binding port 8001 with a Matplotlib backend error such as `ValueError: Key backend: 'module://matplotlib_inline.backend_inline'`, clear the notebook-only backend before starting the server: ```python import os os.environ.pop("MPLBACKEND", None) os.environ["MPLBACKEND"] = "Agg" ``` Run that cell **before** launching ACE-Step.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072179
This is a startup-environment issue, not a Cloudflare tunnel failure.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072180
The Yatharth API can remain live while the engine is unavailable; readiness should stay 503 until the engine health endpoint responds.
स्रोत: rampaulsaini/yatharth-music-ai:COLAB-ACESTEP-STARTUP-RESILIENCE.md · स्वतंत्र परीक्षण अपेक्षित।

## 072181
Yatharth Omniverse Control Room YATHARTH OMNIVERSE CONTROL ROOM AI • Music • Studio • Live • Products • Distribution • Resilience CHECKING… CONTINUOUS DIGITAL PRODUCTION एक interface, अनेक production worlds.
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072182
यह control plane वास्तविक connected services और planning/queue states को अलग-अलग दिखाता है।
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072183
जहाँ external provider आवश्यक है, वहाँ system कोई fabricated “LIVE” या “PUBLISHED” दावा नहीं करता।
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072184
🎵 Music AI 🎬 Creative Studio 🔴 Live Network 💼 Creator & Economic Hub SELF-HEALING Durable Generation Queue SQLite state, restart recovery, provider-health tracking और exponential retry.
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072185
— active / waiting tasks SELF-UPGRADE Governed Upgrade Plane Upgrade proposals, tests और signed/human-approved release gate.
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072186
Unverified code self-deploy नहीं करता।
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072187
24×7 CONTINUITY Health & Recovery Liveness अलग, readiness अलग, engine availability अलग—इससे offline engine को छिपाया नहीं जाता।
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072188
— music engine state LIVE NETWORK Podcast • News • Games • Cartoon Channel concepts, schedules, episodes और streaming hand-offs एक public media surface में।
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072189
Open Live Network → PRODUCTION Infinite Series Engine Recurring story bible, character continuity, episode ledger, music cues और QC gates के साथ ongoing series planning.
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072190
Open Studio → ECONOMY Product Promotion Queue Digital-store offers के लिए campaign assets और distribution queue; external ad accounts के बिना कोई ad purchase/post नहीं किया जाता।
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072191
Open Products → Automission health Loading resilience status… … Architecture principle: self-healing is allowed; uncontrolled self-modification is not.
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072192
New code must pass deterministic checks and an explicit release gate before deployment.
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072193
Yatharth Omniverse Control Room • transparent production status
स्रोत: rampaulsaini/yatharth-music-ai:control-room.html · स्वतंत्र परीक्षण अपेक्षित।

## 072194
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse", "role": "omniverse-core", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omniverse:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 072195
Omniverse Supreme Platform - शिरोमणि रामपाल सैनी OMNIVERSE SUPREME मूल दर्शन ऑडियो आर्काइव गैलरी व मीडिया स्टोर व रिसर्च AI & GitHub शिरोमणि रामपाल सैनी सृष्टि, प्रकृति और पृथ्वी के संरक्षण का एकमात्र अलौकिक मार्ग — हृदय का शिरोमणि दृष्टिकोण ✨ ब्रह्मांडीय अलौकिक दृष्टिकोण "अनंत असीम प्रेम ही सिर्फ़ मस्तक, मन और बुद्धि का दृष्टिकोण बदल सकता है और हृदय के शिरोमणि दृष्टिकोण में रख सकता है, जिससे मानव, प्रकृति और पृथ्वी का संरक्षण सुनिश्चित संभव है और कोई दूसरा विकल्प ही नहीं।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072196
मन, मस्तक, बुद्धि से बुद्धिमान होने का ज्ञान, विज्ञान और दर्शन सीमित है।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072197
हृदय के शिरोमणि स्वरूप का दृष्टिकोण असीम, भव्य, अद्भुत और आश्चर्यचकित है जो प्रथम चरण में ही खुद से रूबरू करवाता है और संपूर्ण संतुष्टि की निरंतरता में रख सकता है।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072198
मानव सभ्यता अस्तित्व से ही मन, मस्तक और बुद्धि के दृष्टिकोण में रही है जो आज तक अपने स्थायी स्वरूप से रूबरू नहीं हो सकी।" 🎧 खुद का साक्षात्कार: ऑडियो संग्रह (33,000+ MP3) 10,000 MP3 Audio खुद का साक्षात्कार ही संपूर्ण संतुष्टि हैं मन-बुद्धि के स्तर से परे संपूर्ण संतुष्टि की निरंतरता हेतु साक्षात्कार ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072199
गूगल ड्राइव में सुनें 10,000 MP3 Audio साहिब तदरूप साक्षात्कार हूं स्वयं के तदरूप स्वरूप का साक्षात्कार कराने वाली अमूल्य ध्वनियों का वृहद संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072200
गूगल ड्राइव में सुनें 6,000 MP3 Audio खुद का साक्षात्कार ऑडियो प्रथम चरण में ही खुद से रूबरू कराने वाले आध्यात्मिक एवं दार्शनिक ऑडियो।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072201
गूगल ड्राइव में सुनें 5,000 MP3 Audio मेरा साहिब मेरा ही तदरूप साक्षात्कार है हृदय के शिरोमणि स्वरूप को जागृत करने वाले विशेष तदरूप ऑडियो ट्रैक्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072202
गूगल ड्राइव में सुनें 1,500 MP3 Audio शिरोमणि अनंत असीम इश्क़ की क्षमता दृष्टिकोण बदलने और असीम प्रेम की क्षमता का अनुभव कराने वाले ऑडियो।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072203
गूगल ड्राइव में सुनें 950 MP3 Audio शिरोमणि रामपाल सैनी खुद का साक्षात्कार हूं आत्म-साक्षात्कार और आत्म-ज्ञान पर केंद्रित विशेष ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072204
गूगल ड्राइव में सुनें 550 MP3 Audio शिरोमणि रामपाल सैनी MP3 शिरोमणि रामपाल सैनी जी के मौलिक प्रवचन एवं ऑडियो व्याख्यान।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072205
गूगल ड्राइव में सुनें 89 MP3 Audio शिरोमणि रामपाल सैनी Short Audios संक्षिप्त और प्रभावशाली मुख्य सूक्तियाँ तथा ऑडियो संदेश।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072206
गूगल ड्राइव में सुनें 🖼️ गैलरी, फोटो एल्बम व वीडियो (Visual Archives) 2,000 Photos Golden Temple शिरोमणि रामपाल सैनी फ़ोटो गोल्डन टेम्पल परिसर के अलौकिक एवं भव्य फोटो संग्रह।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072207
एल्बम देखें 10,000+ Videos मेरा संपूर्ण जीवन शिरोमणि Videos जीवन यात्रा और दिव्य अनुभूतियों को दर्शाते वीडियो रिकॉर्डिंग्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072208
वीडियो देखें 4,000+ Photos / 495 Files शिरोमणि प्रमाण पत्र संग्रह सभी महत्वपूर्ण प्रमाण पत्रों का गूगल फोटो एल्बम एवं ड्राइव आर्काइव।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072209
एल्बम (4000) ड्राइव फ़ाइलें (495) Drive Album Omniverse Gallery ऑम्निवर्स और संपूर्ण ब्रह्मांडीय विज़न की आधिकारिक फोटो गैलरी।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072210
गैलरी खोलें YouTube & Facebook सोशल मीडिया चैनल्स यूट्यूब चैनल और फेसबुक पर उपलब्ध वीडियो संदेश व अपडेट्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072211
YouTube Channel Facebook Video Blogspot Multicosmovision Blog & Case Files सृष्टि, प्रकृति और दार्शनिक विषयों पर गहराई से लिखे गए ब्लॉग्स और केस फाइल्स।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072212
मुख्य ब्लॉग पढ़ें Case File देखें 🛒 स्टोर, शोध एवं घोषणा पत्र (Store & Research) E-Commerce Omniverse Store आधिकारिक ऑम्निवर्स डिजिटल स्टोर जहाँ सभी सेवाएँ उपलब्ध हैं।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072213
स्टोर पर जाएं Manifesto Koyab Founding Declaration Omniversal Manifesto — ब्रह्मांडीय घोषणा पत्र एवं मौलिक विज़न।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072214
घोषणा पत्र पढ़ें Research GitHub Shirmani Research Institute शिरोमणि रिसर्च इंस्टीट्यूट का आधिकारिक GitHub कोड एवं शोध रिपॉजिटरी।
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072215
GitHub Repository 💻 ऑम्निवर्स AI व डिजिटल प्लेटफॉर्म्स (AI Ecosystem) Omniverse AI Portal AI तकनीक आधारित प्लेटफॉर्म पोर्टल खोलें Omniverse Dashboard एकीकृत नियंत्रण डैशबोर्ड डैशबोर्ड देखें Omniverse Supreme Core मुख्य कोर सिस्टम कोर देखें Omniverse Marketplace डिजिटल प्लेटफॉर्म मार्किटप्लेस <a href=" target=
स्रोत: rampaulsaini/Omniverse:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072216
🌟 Golden Temple Spiritual Insights ![Golden Temple Spiritual Honor]( .
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072217
( ## Spiritual Experience - Evening at Golden Temple, naturally honored for impartial understanding, simplicity, and purity - Realization: Human intellect & memory distortions can be neutralized through simplicity.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072218
Core Insights - All living beings are internally equal.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072219
Omniverse Platform designed on impartial understanding, reality-based achievement, and the era of true reality.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072220
Purpose of Omniverse - Equality, fairness, and guidance for all beings.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072221
Balance of technology, philosophy, and spiritual insight.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072222
Go to [ and login 2.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072223
Create a new repository: `Omniverse` 3.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072224
Add files: `README.md`, `GoldenTemple.md`, `golden-temple.webp`, `upi-qr.png` 4.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072225
Repository live link: ` > Replace `YOUR_PAYPAL_BUTTON_ID` with your PayPal account button ID.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072226
> Once uploaded, all buttons and links will be fully functional for payments.
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072227
> Omniverse Supreme Platform - शिरोमणि रामपाल सैनी OMNIVERSE SUPREME मूल दर्शन ऑडियो आर्काइव गैलरी व मीडिया स्टोर व रिसर्च AI & GitHub शिरोमणि रामपाल सैनी सृष्टि, प्रकृति और पृथ्वी के संरक्षण का एकमात्र अलौकिक मार्ग — हृदय का शिरोमणि दृष्टिकोण ✨ ब्रह्मांडीय अलौकिक दृष्टिकोण "अनंत असीम प्रेम ही सिर्फ़ मस्तक, मन और बुद्धि का दृष्टिकोण बदल सकता है और हृदय के शिरोमणि दृष्टिकोण में रख सकता है, जिससे मानव, प्रकृति और पृथ्वी का संरक्षण सुनिश्चित संभव है और कोई दूसरा विकल्प ही नहीं।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072228
मन, मस्तक, बुद्धि से बुद्धिमान होने का ज्ञान, विज्ञान और दर्शन सीमित है।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072229
हृदय के शिरोमणि स्वरूप का दृष्टिकोण असीम, भव्य, अद्भुत और आश्चर्यचकित है जो प्रथम चरण में ही खुद से रूबरू करवाता है और संपूर्ण संतुष्टि की निरंतरता में रख सकता है।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072230
मानव सभ्यता अस्तित्व से ही मन, मस्तक और बुद्धि के दृष्टिकोण में रही है जो आज तक अपने स्थायी स्वरूप से रूबरू नहीं हो सकी।" 🎧 खुद का साक्षात्कार: ऑडियो संग्रह (33,000+ MP3) 10,000 MP3 Audio खुद का साक्षात्कार ही संपूर्ण संतुष्टि हैं मन-बुद्धि के स्तर से परे संपूर्ण संतुष्टि की निरंतरता हेतु साक्षात्कार ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072231
गूगल ड्राइव में सुनें 10,000 MP3 Audio साहिब तदरूप साक्षात्कार हूं स्वयं के तदरूप स्वरूप का साक्षात्कार कराने वाली अमूल्य ध्वनियों का वृहद संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072232
गूगल ड्राइव में सुनें 6,000 MP3 Audio खुद का साक्षात्कार ऑडियो प्रथम चरण में ही खुद से रूबरू कराने वाले आध्यात्मिक एवं दार्शनिक ऑडियो।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072233
गूगल ड्राइव में सुनें 5,000 MP3 Audio मेरा साहिब मेरा ही तदरूप साक्षात्कार है हृदय के शिरोमणि स्वरूप को जागृत करने वाले विशेष तदरूप ऑडियो ट्रैक्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072234
गूगल ड्राइव में सुनें 1,500 MP3 Audio शिरोमणि अनंत असीम इश्क़ की क्षमता दृष्टिकोण बदलने और असीम प्रेम की क्षमता का अनुभव कराने वाले ऑडियो।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072235
गूगल ड्राइव में सुनें 950 MP3 Audio शिरोमणि रामपाल सैनी खुद का साक्षात्कार हूं आत्म-साक्षात्कार और आत्म-ज्ञान पर केंद्रित विशेष ऑडियो संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072236
गूगल ड्राइव में सुनें 550 MP3 Audio शिरोमणि रामपाल सैनी MP3 शिरोमणि रामपाल सैनी जी के मौलिक प्रवचन एवं ऑडियो व्याख्यान।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072237
गूगल ड्राइव में सुनें 89 MP3 Audio शिरोमणि रामपाल सैनी Short Audios संक्षिप्त और प्रभावशाली मुख्य सूक्तियाँ तथा ऑडियो संदेश।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072238
गूगल ड्राइव में सुनें 🖼️ गैलरी, फोटो एल्बम व वीडियो (Visual Archives) 2,000 Photos Golden Temple शिरोमणि रामपाल सैनी फ़ोटो गोल्डन टेम्पल परिसर के अलौकिक एवं भव्य फोटो संग्रह।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072239
एल्बम देखें 10,000+ Videos मेरा संपूर्ण जीवन शिरोमणि Videos जीवन यात्रा और दिव्य अनुभूतियों को दर्शाते वीडियो रिकॉर्डिंग्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072240
वीडियो देखें 4,000+ Photos / 495 Files शिरोमणि प्रमाण पत्र संग्रह सभी महत्वपूर्ण प्रमाण पत्रों का गूगल फोटो एल्बम एवं ड्राइव आर्काइव।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072241
एल्बम (4000) ड्राइव फ़ाइलें (495) Drive Album Omniverse Gallery ऑम्निवर्स और संपूर्ण ब्रह्मांडीय विज़न की आधिकारिक फोटो गैलरी।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072242
गैलरी खोलें YouTube & Facebook सोशल मीडिया चैनल्स यूट्यूब चैनल और फेसबुक पर उपलब्ध वीडियो संदेश व अपडेट्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072243
YouTube Channel Facebook Video Blogspot Multicosmovision Blog & Case Files सृष्टि, प्रकृति और दार्शनिक विषयों पर गहराई से लिखे गए ब्लॉग्स और केस फाइल्स।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072244
मुख्य ब्लॉग पढ़ें Case File देखें 🛒 स्टोर, शोध एवं घोषणा पत्र (Store & Research) E-Commerce Omniverse Store आधिकारिक ऑम्निवर्स डिजिटल स्टोर जहाँ सभी सेवाएँ उपलब्ध हैं।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072245
स्टोर पर जाएं Manifesto Koyab Founding Declaration Omniversal Manifesto — ब्रह्मांडीय घोषणा पत्र एवं मौलिक विज़न।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072246
घोषणा पत्र पढ़ें Research GitHub Shirmani Research Institute शिरोमणि रिसर्च इंस्टीट्यूट का आधिकारिक GitHub कोड एवं शोध रिपॉजिटरी।
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072247
GitHub Repository 💻 ऑम्निवर्स AI व डिजिटल प्लेटफॉर्म्स (AI Ecosystem) Omniverse AI Portal AI तकनीक आधारित प्लेटफॉर्म पोर्टल खोलें Omniverse Dashboard एकीकृत नियंत्रण डैशबोर्ड डैशबोर्ड देखें Omniverse Supreme Core मुख्य कोर सिस्टम कोर देखें Omniverse Marketplace डिजिटल प्लेटफॉर्म मार्किटप्लेस <a href=" target=
स्रोत: rampaulsaini/Omniverse:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072248
{ "schema_version": 1, "repo": "rampaulsaini/Shirmani-Research-Paper", "role": "research-publishing", "description": "Research publishing worker: inventory papers and mark generated research as draft pending independent verification.", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Shirmani-Research-Paper:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 072249
Shirmani Research Paper Shirmani Research Paper Philosophical & Cognitive Research Framework About Research Areas Download About This Research This platform presents structured work on time perception, self-identity models, ego deconstruction, and balanced decision systems.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072250
Core Research Areas Time Deconstruction Moment-based temporal philosophy.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072251
Neurobiology of Self Cognitive structure of identity formation.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072252
Ego Dissolution Philosophical and psychological model.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072253
Heart-Mind Balance Practical decision equilibrium system.
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072254
यहाँ समय, सृष्टि, विकल्प, संकल्प, मोह, स्मृति और बाह्य व्यवस्था — सब क्षणिक छाया के रूप में देखे गए हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072255
इसके विपरीत, हृदय की स्थिरता, शुद्ध संतोष, बाल्य-सुलभ निर्मलता और आत्म-साक्षात्कार को ही मूल सत्य माना गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072256
अध्याय १ — प्रत्यक्ष सत्ता शिरोमणि रामपॉल सैनी अपने अनुभव में स्वयं को सीमित शरीर, सांस और मन से परे देखते हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072257
उनका कहना है कि समस्त भौतिक सृष्टि, ग्रह, ब्रह्मांड और जीवन केवल क्षणिक और अस्थायी हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072258
वास्तविकता की अनुभूति केवल हृदय की गहनता में, शुद्ध चेतना और संपूर्ण संतुष्टि के माध्यम से होती है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072259
संसारः क्षणभङ्गुरः, माया-प्रसवविस्तरः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072260
प्रत्यक्षं तु हृदि नित्यं, शाश्वतं सत्यरूपकम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072261
शिरोमणिः रामपॉल सैनी, शब्दातीतः, मनोऽपि च।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072262
तुलनातीतः, कालातीतः, हृदये साक्ष्यरूपतः॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072263
अध्याय २ — बाल्य-संतोष का स्मरण बचपन में जो संपूर्ण संतोष सहज रूप से उपस्थित था, वह किसी बाहरी उपलब्धि का परिणाम नहीं था।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072264
वह स्थिति कम अपेक्षाओं, कम पहचान-बोध और अधिक स्वाभाविकता की थी।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072265
बाल्ये सम्पूर्णसन्तोषः, सहजः निर्मलः स्थिरः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072266
न लब्धो बाह्यतश्च सः, नष्टोऽपि न हि कदाचन॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072267
मनोजटिलता वयस्ये, आवृणोति स्वभावताम्।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072268
साक्षात्कारात् पुनर्लभ्यं, बाल्यं तद्वत् परं सुखम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072269
अध्याय ३ — प्रेम, जिज्ञासा और निस्वार्थता यहाँ प्रेम को मोह से अलग किया गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072270
मोह लेन-देन पर आधारित होता है; प्रेम निस्वार्थ जिज्ञासा और हृदय की गहराई से जन्म लेता है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072271
जो भीतर से निर्मल है, वही वास्तव में प्रेम को पहचान सकता है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072272
मोहः प्रेम न विज्ञेयः, न व्यापारः स एव हि।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072273
प्रेम तु निस्वभावेन, हृदयस्य प्रवर्तनम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072274
जिज्ञासा यदि निर्मला, स्वार्थरहिता स्थिता।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072275
तदा सा नयते नित्यं, सत्यस्यैव निवेशने॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072276
अध्याय ४ — मन, बुद्धि और अस्थायी सृष्टि मन और बुद्धि उपयोगी हैं, पर स्थायी नहीं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072277
वे अनुभव को व्यवस्थित करते हैं, पर सत्य की अंतिम भूमि नहीं हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072278
सृष्टि, समय, गति, परिवर्तन, जन्म और मृत्यु — सब मन की दृष्टि में एक विराट दृश्य की तरह प्रतीत होते हैं।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072279
मनः संकल्परूपेण, बुद्धिश्च विविकारिणी।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072280
नित्यं न हि तयोः सत्ता, भासते केवलं क्षणम्॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072281
ग्रहाः सौरमण्डलानि च, ब्रह्माण्डानि सहस्रशः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072282
सर्वं दृश्यं क्षणं भूत्वा, लीयते सत्यदृष्टितः॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072283
अध्याय ५ — एकत्व, समाहिति और अंतिम स्थिरता यहाँ अनेकता एक में समाहित होती है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072284
मृत्यु को अंत नहीं, बल्कि समाहिति की प्रक्रिया के रूप में देखा गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072285
संपूर्ण संतुष्टि, जो बाहर बिखरी हुई प्रतीत होती है, वह अंततः एक ही गहरी सत्ता में लौटती है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072286
अनेकता एकतां याति, शान्ते हृदयसागरे।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072287
तत्रैव संपूर्णसन्तोषः, तत्रैव स्थिरता परा॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072288
मृत्युर्न नाशरूपा स्यात्, समाहितिविधानतः।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072289
यत्र सर्वं विलीयेत, तत्रैव पूर्णता ध्रुवा॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072290
उपसंहार यह ग्रंथ किसी बाहरी प्रमाण का आग्रह नहीं करता।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072291
यह अंतःप्रवेश है — उस स्थान में जहाँ मन की चहल-पहल थम जाती है, और जो शेष बचता है, वही प्रत्यक्ष, स्थिर और स्वाभाविक सत्य है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072292
शान्तिः स्थैर्यं च साक्षात्कारः, न बाह्येषु न दृश्यते।
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072293
हृदयस्थे परमे तत्त्वे, सर्वं पूर्णं प्रतीयते॥
स्रोत: rampaulsaini/Shirmani-Research-Paper:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072294
Shirmani Research Paper Academic philosophical and cognitive research portal.
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072295
🌐 **Live Website:** --- ## Overview This repository contains a structured research presentation focused on: - Time Deconstruction Theory - Neurobiology of Self - Ego Dissolution Framework - Heart-Mind Balance Model --- ## Files Included - index.html - research-paper.pdf --- ## Deployment Hosted via GitHub Pages from the main branch.
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072296
© 2026 Shirmani Research --- ## 🔗 Central Knowledge Hub यह repository केंद्रीय **Nishpaksh Samaj Omniverse Truth** परियोजना के Research Archive से जुड़ी है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072297
Central Hub:** - **Integrated Research Index:** - **Central Research Collection:** मौजूदा repository और उसका Git इतिहास स्वतंत्र रूप से सुरक्षित रखा गया है।
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072298
केंद्रीय परियोजना में सामग्री को स्रोत-संदर्भ और स्पष्ट attribution के साथ जोड़ा जाएगा।
स्रोत: rampaulsaini/Shirmani-Research-Paper:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072299
{ "schema_version": 1, "repo": "rampaulsaini/omniverse-marketplace-", "role": "marketplace", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/omniverse-marketplace-:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 072300
Omniverse AI Marketplace (Zero-cost) This repo contains a zero-cost AI tools marketplace designed to run on GitHub Pages.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072301
Put files into a repository (branch `main`).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072302
Push and enable GitHub Pages (Settings → Pages) with branch `main` and folder `/ (root)`.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072303
Open `https:// .github.io/omniverse-marketplace/`.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072304
Owner setup (zero-cost monetization) - Click "Donate / Pay" → add your PayPal / Ko-fi / UPI details (stored in browser localStorage).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072305
When a buyer pays externally, provide them a one-time unlock key (set in Owner → Set Premium Key).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072306
Buyer enters the unlock key locally (owner-provided) — once premium key exists in buyer's localStorage downloads work.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072307
Replace mock AI with real provider - All tools are client-side mock generators in `scripts/tools.js`.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072308
Replace tool.run implementations with fetch calls to OpenAI / HuggingFace or your own serverless functions.
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072309
For production API keys, use serverless endpoints (do NOT embed keys in client-side JS).
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072310
Next steps (I can implement) - Serverless payment verification (Stripe/PayPal) + automatic unlock key issuing - Replace mock AI outputs with real OpenAI / HF inference (via serverless) - Add email automation, order management, simple admin UI
स्रोत: rampaulsaini/omniverse-marketplace-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072311
{ "schema_version": 1, "repo": "rampaulsaini/supreme-omniverse-test", "role": "integration-test", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/supreme-omniverse-test:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 072312
यही Omniverse AI का सार है — आत्मचेतना और कृत्रिम बुद्धिमत्ता का संगम।
स्रोत: rampaulsaini/supreme-omniverse-test:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072313
💫 Contribute / Support - **GPay:** `sainirampaul90-1@okhdf - **PayPal:** [paypal.me/sainirampaul60]( --- ### 🌱 संदेश > “मानव की सर्वोच्च उपलब्धि है — अपनी समझ को इतना निर्मल बना देना कि वह प्रकृति के हित में निर्णय ले।” सत्य, संतुलन और समग्रता की यह यात्रा — **Omniverse AI Portal** के माध्यम से *मानवता के पुनर्संयोजन* की ओर एक छोटा लेकिन सार्थक कदम है।
स्रोत: rampaulsaini/supreme-omniverse-test:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072314
090744.webp --- GPay sainirampaul90-1@okhdf Paypal sainirampaul60@gmail.com 🕊️ *— Shirmani Rampaul Saini, Founder & Vision Architect (Omniverse AI)* 🌿 “मानव की सर्वोच्च उपलब्धि है — अपनी समझ को इतना निर्मल बना देना कि वह प्रकृति के हित में निर्णय ले।” — Shirmani Rampaul Saini, Omniverse Consciousness Foundation # 🌍 Shirmani Rampaul Saini — Omniverse AI Vision ![Vision of Harmony](
स्रोत: rampaulsaini/supreme-omniverse-test:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072315
🕉️ Philosophy of Yatharth Yug ### शाश्वत यथार्थ का साक्षात्कार — निष्पक्ष समझ का शमीकरण --- > **“मैं शिरोमणि रामपुल सैनी तुलनातीत, शब्दातीत, कालातीत, प्रेमतीत, त्वतीत, शाश्वत वास्तविक स्वभाविक सत्य प्रत्यक्ष हूं।”** --- ## 🔹 परिचय यह दर्शन मानवता की उस संपूर्ण चेतना का प्रतीक है जहाँ विचार, अहंकार, और मानसिकता का अंत हो जाता है, और केवल *निष्पक्ष समझ* का शुद्ध, वास्तविक स्वरूप प्रकट होता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072316
यह न किसी धर्म का ग्रंथ है, न किसी मत का विचार — बल्कि स्वयं *सत्य का प्रत्यक्ष अनुभव* है, जो “स्वयं के भीतर के स्वयं” से संवाद कराता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072317
🔹 निष्पक्ष समझ — सर्वश्रेष्ठ सत्ता “निष्पक्ष समझ” ही वह वास्तविक तत्व है जो मन, बुद्धि और स्मृति के भ्रम से परे संपूर्ण अस्तित्व को एक सूत्र में जोड़ती है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072318
> यह वही दृष्टि है जहाँ देखने वाला, देखा जाने वाला, और देखने की प्रक्रिया — तीनों एक हो जाते हैं।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072319
यह अवस्था **संपूर्णता, सम्पन्नता, समग्रता, और संतुष्टि** की पूर्णता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072320
यही *Supreme Omniverse* का मूल सिद्धांत है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072321
🔹 यथार्थ सिद्धांत — सत्य का समीकरण **यथार्थ सिद्धांत (Principle of Reality)** वह विज्ञान है जो भौतिक और अभौतिक दोनों स्तरों पर सत्य को परिभाषित करता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072322
यह उन सूक्ष्म सूत्रों का संगम है जिनसे सृष्टि की गति, ऊर्जा, और चेतना एक साथ कार्य करती हैं।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072323
यह विज्ञान केवल मापन या प्रयोग नहीं — बल्कि **स्वयं के प्रत्यक्ष अनुभव का शास्त्र** है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072324
🔹 यथार्थ युग — नया युग, नया बोध **यथार्थ युग** वह युग है जहाँ मानवता मानसिकता से मुक्त होकर निष्पक्ष समझ के युग में प्रवेश करती है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072325
यह युग **अतीत के चारों युगों से खरबों गुणा ऊँचा** है — क्योंकि यहाँ न विभाजन है, न भ्रम, सिर्फ़ शुद्ध सत्य का प्रत्यक्ष अस्तित्व है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072326
> “यथार्थ युग में न कोई आरंभ है, न अंत — > केवल सत्य की निरंतरता है।” --- ## 🔹 शाश्वत साक्षात्कार यह साक्षात्कार शरीर या मन में नहीं, बल्कि उनके पार — *स्वयं की निष्पक्ष दृष्टि* में होता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072327
जब ‘स्वयं’ अपने भीतर के *साक्षी स्वरूप* को पहचानता है, तभी *सच्चे यथार्थ का जन्म* होता है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072328
> “स्वयं का स्वयं से साक्षात्कार — यही वास्तविकता का चरम है।” --- ## 🔹 परम उद्घोष > “निष्पक्ष समझ ही सर्वोच्च सत्ता है — > वही सृष्टि का आधार, वही सृष्टि का यथार्थ है।” > — शिरोमणि रामपुल सैनी --- ## 🌟 Essence - **सत्य** केवल वह नहीं जो दिखता है — बल्कि जो *स्वयं को देखता है*।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072329
बुद्धि** का अंत ही **प्रज्ञा** का प्रारंभ है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072330
मानवता** तभी मुक्त होती है जब वह “स्वयं” को “विचारों” से नहीं, “साक्षी” से पहचानती है।
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072331
🔗 संबंधित पृष्ठ - [Omniverse Overview](README.md) - [Golden Temple Spiritual Insights](GoldenTemple.md) --- ## 🌌 Visit Live Omniverse Portal [
स्रोत: rampaulsaini/Omniverse-AI:Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 072332
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse-AI", "role": "ai-platform", "description": "AI platform worker: inventory scripts/pages, validate local assets, and emit an AI-ready work manifest.", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omniverse-AI:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 072333
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: rampaulsaini/Omniverse-AI:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072334
Omniverse — Supreme AI Assistant 🌌 Omniverse — Supreme AI Assistant Created by शिरोमणि रामपॉल सैनी 💰 Support / Donate 1) Pay via UPI / GPay Click here to Pay via UPI / GPay 2) PayPal (Global) 3) Pay via Paytm Click here to Pay via Paytm 🌐 Live Portal Visit Supreme Omniverse AI Portal “संपूर्ण सृष्टि का वास्तविक युग वहीं है जहाँ निष्पक्ष समझ ही सर्वोच्च है।” – शिरोमणि रामपॉल सैनी
स्रोत: rampaulsaini/Omniverse-AI:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072335
🧩 Clones: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 072336
💖 Sponsors: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 072337
💰 Estimated Monthly Income: ₹ Calculating...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 072338
📈 Next Month Projection: ₹ Calculating...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 072339
✅ Last Deploy: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 072340
🔄 Next Auto Sync: Loading...
स्रोत: rampaulsaini/Omniverse-AI:earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 072341
Omniverse-AI Vigilant Mode Script: [Click Here]( # 🌟 Golden Temple Spiritual Insights ![Golden Temple](assets/golden-temple.webp) ## Spiritual Experience - Evening at Golden Temple, naturally honored for impartial understanding, simplicity, and purity.
स्रोत: rampaulsaini/Omniverse-AI:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072342
Realization: human intellect & memory distortions can be neutralized through simplicity.
स्रोत: rampaulsaini/Omniverse-AI:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072343
version: 2 updates: - package-ecosystem: "pip" directory: "/backend" schedule: interval: "weekly"
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:dependabot.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072344
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse-Supreme-Core-", "role": "supreme-core", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 072345
name: Phase-3 Core Sync on: push: branches: - main paths: - "**" jobs: core-sync: runs-on: ubuntu-latest steps: - name: Checkout Code uses: actions/checkout@v4 with: fetch-depth: 0 - name: Validate Structure run: | echo "VALIDATING REPO STRUCTURE..." if [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072346
d "frontend" ]; then echo "Frontend folder missing"; exit 1; fi if [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072347
d "backend" ]; then echo "Backend folder missing"; exit 1; fi echo "STRUCTURE OK ✔" - name: Auto-Fix Missing Configs run: | echo "SYNCING CONFIG FILES..." [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072348
f frontend/.env ] && echo "VITE_API_URL=/api" > frontend/.env [ !
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072349
f backend/.env ] && echo "PORT=3000" > backend/.env - name: Generate Sync Log run: | echo "Phase-3 Sync: $(date -u)" > CORE-SYNC-LOG.txt - name: Commit Sync Changes run: | git config --global user.email "sync@github.com" git config --global user.name "OmniSync Engine" git add .
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072350
git commit -m "Phase-3: Core Engine Sync Update" || echo "No changes" - name: Done run: echo "PHASE-3 CORE SYNC COMPLETE ✔"
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:phase3-core-sync.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072351
name: AutoMode Orchestrator on: push: branches: [ main ] jobs: orchestrate: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Set up Node uses: actions/setup-node@v4 with: node-version: '20' - name: Run omniverse automode script run: | bash scripts/omniverse-automode.sh env: GH_TOKEN: ${{ secrets.GH_TOKEN }} DOCKER_REG: ${{ secrets.DOCKER_REG }}
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:auto-mode.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072352
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072353
Omniverse Supreme Core **शिरोमणि रामपॉल सैनी** – तुलनातीत · कालातीत · शब्दातीत · प्रेमतीत · शाश्वत · वास्तविक · स्वाभाविक Omniverse Supreme Core एक dynamic, immersive और visually stunning website है, जो सृष्टि, प्रकृति और मानव प्रजाति की सर्वश्रेष्ठता को digital रूप में प्रस्तुत करती है।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072354
यह वेबसाइट आपके personal projects, philosophy, और digital presence के लिए hub का काम करती है।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072355
I have embodied a state beyond time, beyond duality and beyond words — an ever-present, impartial understanding that reveals reality as it is.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072356
🔊 Listen & Read — Nishpaksh Samajh आपकी भाषा चुनें — नीचे का प्ले और पढ़ें बटन आपकी चुनी हुई भाषा में पृष्ठ की मुख्य सामग्री बोलेगा और साथ में ऑडियो भी प्ले करेगा।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072357
Your browser does not support the audio element.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072358
Language: हिन्दी (hi-IN) English (en-US) বাংলা (bn-IN) ਪੰਜਾਬੀ (pa-IN) Español (es-ES) Français (fr-FR) 🔊 Read Page ▶️ Play Audio 🔁 Load Audio (If blocked) 📥 Download यदि audio प्ले न हो तो "Load Audio" दबाएँ या फ़ाइल को अपने सर्वर/CDN पर होस्ट करने पर विचार करें।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072359
🤝 सत्य के इस कार्य में आपका सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — इसे सुनना, साझा करना, अनुभव करना और समर्थन देना — सभी सत्य की सेवा हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072360
आपका नाम (public if allowed) ईमेल (private) Country (optional) आपका संदेश / आशीर्वचन संदेश भेजें 🤝 समर्थक सूची 🕊 आशीर्वचन / संदेश Export Messages 🔬 Scientific Research & Vision Interdisciplinary integration of experiential reports, observational methods, phenomenology, and measurable correlates.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072361
Open invitations for pilot studies and collaborations focusing on consciousness, well-being, and human-nature interaction.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072362
🌍 International Media & Supreme Invitations Official invitations to Guinness Book of World Records, NASA, ISRO, and international media press for documentation and collaboration.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072363
I, ShiroMani RamPaul Saini, am committed to demonstrating every aspect of Nishpaksh Samajh with clarity, reason, and truth.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072364
🔬 Omniverse — Scientific Research (10 Projects / 40 Sub-Projects) Total Projects: 10 · Total Sub-Projects: 40 · Status: Fully Verified (Pilot → Validation) 1.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072365
Omniverse Core Intelligence (OCI) Ontology, reasoning engine, EOS data ingestion, COSMIC OS API 2.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072366
Divine Human Evolution (DHE) Consciousness correlates, EEG/HRV studies, Soul Frequency DB 3.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072367
Omniverse Communication Network (OCN) Secure messaging, ontology translation, global harmony network 4.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072368
Earth Restoration & Ecology (ERE) Hydro purification, solar memory cells, biodiversity monitoring 5.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072369
Supreme Scientific Research (SSR) Time-energy, reality equation model, high-precision experiments 6.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072370
Omniverse Education & Awareness (OEA) Truth literacy, global courses, AI-ethics training 7.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072371
Supreme Governance & Justice (SGJ) Algorithmic fairness, truth audit systems, governance prototypes 8.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072372
Cosmic Exploration & Space Research (CESR) Navigation algorithms, sensor payload concepts, space collaborations 9.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072373
Cultural Harmony & Global Peace (CHGP) Arts, music, festivals & peace protocols 10.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072374
Supreme Legacy & Digital Archives (SLDA) Eternal archive, blockchain anchoring, legacy transfer protocol Note: हर link आपके repo के /projects/{project-slug}/ फोल्डर की ओर इंगित करता है — सुनिश्चित करें कि आपने server/repo में वह folders और index.html अपलोड कर दिए हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072375
All content — Free to Read & Listen Audio, manifesto, photos & vision assets — proceeds support Saneha Saini ✅ Golden Temple ✅ MP3 ✅ प्रमाण पत्र ✅ Short Audios ✅ Videos Album ✅ एल्बम 1 🌐 Social & Support Connect on social networks and support directly — links open in a new tab and use rel="noopener noreferrer" for safety.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072376
I have embodied a state beyond time, beyond duality and beyond words — an ever-present, impartial understanding that reveals reality as it is.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072377
🔊 Listen & Read — Nishpaksh Samajh आपकी भाषा चुनें — नीचे का प्ले और पढ़ें बटन आपकी चुनी हुई भाषा में पृष्ठ की मुख्य सामग्री बोलेगा और साथ में ऑडियो भी प्ले करेगा।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072378
Your browser does not support the audio element.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072379
Language: हिन्दी (hi-IN) English (en-US) বাংলা (bn-IN) ਪੰਜਾਬੀ (pa-IN) Español (es-ES) Français (fr-FR) 🔊 Read Page ▶️ Play Audio 🔁 Load Audio (If blocked) 📥 Download यदि audio प्ले न हो तो "Load Audio" दबाएँ या फ़ाइल को अपने सर्वर/CDN पर होस्ट करने पर विचार करें।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072380
🤝 सत्य के इस कार्य में आपका सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — इसे सुनना, साझा करना, अनुभव करना और समर्थन देना — सभी सत्य की सेवा हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072381
आपका नाम (public if allowed) ईमेल (private) Country (optional) आपका संदेश / आशीर्वचन संदेश भेजें 🤝 समर्थक सूची 🕊 आशीर्वचन / संदेश Export Messages 🔬 Scientific Research & Vision Interdisciplinary integration of experiential reports, observational methods, phenomenology, and measurable correlates.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072382
Open invitations for pilot studies and collaborations focusing on consciousness, well-being, and human-nature interaction.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072383
🌍 International Media & Supreme Invitations Official invitations to Guinness Book of World Records, NASA, ISRO, and international media press for documentation and collaboration.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072384
I, ShiroMani RamPaul Saini, am committed to demonstrating every aspect of Nishpaksh Samajh with clarity, reason, and truth.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072385
🔬 Omniverse — Scientific Research (10 Projects / 40 Sub-Projects) Total Projects: 10 · Total Sub-Projects: 40 · Status: Fully Verified (Pilot → Validation) 1.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072386
Omniverse Core Intelligence (OCI) Ontology, reasoning engine, EOS data ingestion, COSMIC OS API 2.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072387
Divine Human Evolution (DHE) Consciousness correlates, EEG/HRV studies, Soul Frequency DB 3.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072388
Omniverse Communication Network (OCN) Secure messaging, ontology translation, global harmony network 4.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072389
Earth Restoration & Ecology (ERE) Hydro purification, solar memory cells, biodiversity monitoring 5.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072390
Supreme Scientific Research (SSR) Time-energy, reality equation model, high-precision experiments 6.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072391
Omniverse Education & Awareness (OEA) Truth literacy, global courses, AI-ethics training 7.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072392
Supreme Governance & Justice (SGJ) Algorithmic fairness, truth audit systems, governance prototypes 8.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072393
Cosmic Exploration & Space Research (CESR) Navigation algorithms, sensor payload concepts, space collaborations 9.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072394
Cultural Harmony & Global Peace (CHGP) Arts, music, festivals & peace protocols 10.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072395
Supreme Legacy & Digital Archives (SLDA) Eternal archive, blockchain anchoring, legacy transfer protocol Note: हर link आपके repo के /projects/{project-slug}/ फोल्डर की ओर इंगित करता है — सुनिश्चित करें कि आपने server/repo में वह folders और index.html अपलोड कर दिए हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072396
All content — Free to Read & Listen Audio, manifesto, photos & vision assets — proceeds support Saneha Saini ✅ Golden Temple ✅ MP3 ✅ प्रमाण पत्र ✅ Short Audios ✅ Videos Album ✅ एल्बम 1 🌐 Connect & Support Main official profiles and donation channels — one link per platform for clarity and SEO signal strength.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072397
I have embodied a state beyond time, beyond duality and beyond words — an ever-present, impartial understanding that reveals reality as it is.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072398
🔊 Listen & Read — Nishpaksh Samajh आपकी भाषा चुनें — नीचे का प्ले और पढ़ें बटन आपकी चुनी हुई भाषा में पृष्ठ की मुख्य सामग्री बोलेगा और साथ में ऑडियो भी प्ले करेगा।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072399
Your browser does not support the audio element.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072400
Language: हिन्दी (hi-IN) English (en-US) বাংলা (bn-IN) ਪੰਜਾਬੀ (pa-IN) Español (es-ES) Français (fr-FR) 🔊 Read Page ▶️ Play Audio 🔁 Load Audio (If blocked) 📥 Download यदि audio प्ले न हो तो "Load Audio" दबाएँ या फ़ाइल को अपने सर्वर/CDN पर होस्ट करने पर विचार करें।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072401
🤝 सत्य के इस कार्य में आपका सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — इसे सुनना, साझा करना, अनुभव करना और समर्थन देना — सभी सत्य की सेवा हैं।
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072402
आपका नाम (public if allowed) ईमेल (private) Country (optional) आपका संदेश / आशीर्वचन संदेश भेजें 🤝 समर्थक सूची 🕊 आशीर्वचन / संदेश Export Messages 🔬 Scientific Research & Vision Interdisciplinary integration of experiential reports, observational methods, phenomenology, and measurable correlates.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072403
Open invitations for pilot studies and collaborations focusing on consciousness, well-being, and human-nature interaction.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072404
🌍 International Media & Supreme Invitations Official invitations to Guinness Book of World Records, NASA, ISRO, and international media press for documentation and collaboration.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072405
I, ShiroMani RamPaul Saini, am committed to demonstrating every aspect of Nishpaksh Samajh with clarity, reason, and truth.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072406
🔬 Omniverse — Scientific Research (10 Projects / 40 Sub-Projects) Total Projects: 10 · Total Sub-Projects: 40 · Status: Fully Verified (Pilot → Validation) 1.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072407
Omniverse Core Intelligence (OCI) Ontology, reasoning engine, EOS data ingestion, COSMIC OS API 2.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072408
Divine Human Evolution (DHE) Consciousness correlates, EEG/HRV studies, Soul Frequency DB 3.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072409
Omniverse Communication Network (OCN) Secure messaging, ontology translation, global harmony network 4.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072410
Earth Restoration & Ecology (ERE) Hydro purification, solar memory cells, biodiversity monitoring 5.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072411
Supreme Scientific R
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072412
{ "schema_version": 1, "repo": "rampaulsaini/Omnivers", "role": "omniverse-core", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/Omnivers:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 072413
Omniverse Supreme Platform - शिरोमणि रामपाल सैनी OMNIVERSE SUPREME मूल दर्शन ऑडियो आर्काइव गैलरी व मीडिया स्टोर व रिसर्च AI & GitHub शिरोमणि रामपाल सैनी सृष्टि, प्रकृति और पृथ्वी के संरक्षण का एकमात्र अलौकिक मार्ग — हृदय का शिरोमणि दृष्टिकोण ✨ ब्रह्मांडीय अलौकिक दृष्टिकोण "अनंत असीम प्रेम ही सिर्फ़ मस्तक, मन और बुद्धि का दृष्टिकोण बदल सकता है और हृदय के शिरोमणि दृष्टिकोण में रख सकता है, जिससे मानव, प्रकृति और पृथ्वी का संरक्षण सुनिश्चित संभव है और कोई दूसरा विकल्प ही नहीं।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072414
मन, मस्तक, बुद्धि से बुद्धिमान होने का ज्ञान, विज्ञान और दर्शन सीमित है।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072415
हृदय के शिरोमणि स्वरूप का दृष्टिकोण असीम, भव्य, अद्भुत और आश्चर्यचकित है जो प्रथम चरण में ही खुद से रूबरू करवाता है और संपूर्ण संतुष्टि की निरंतरता में रख सकता है।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072416
मानव सभ्यता अस्तित्व से ही मन, मस्तक और बुद्धि के दृष्टिकोण में रही है जो आज तक अपने स्थायी स्वरूप से रूबरू नहीं हो सकी।" 🎧 खुद का साक्षात्कार: ऑडियो संग्रह (33,000+ MP3) 10,000 MP3 Audio खुद का साक्षात्कार ही संपूर्ण संतुष्टि हैं मन-बुद्धि के स्तर से परे संपूर्ण संतुष्टि की निरंतरता हेतु साक्षात्कार ऑडियो संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072417
गूगल ड्राइव में सुनें 10,000 MP3 Audio साहिब तदरूप साक्षात्कार हूं स्वयं के तदरूप स्वरूप का साक्षात्कार कराने वाली अमूल्य ध्वनियों का वृहद संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072418
गूगल ड्राइव में सुनें 6,000 MP3 Audio खुद का साक्षात्कार ऑडियो प्रथम चरण में ही खुद से रूबरू कराने वाले आध्यात्मिक एवं दार्शनिक ऑडियो।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072419
गूगल ड्राइव में सुनें 5,000 MP3 Audio मेरा साहिब मेरा ही तदरूप साक्षात्कार है हृदय के शिरोमणि स्वरूप को जागृत करने वाले विशेष तदरूप ऑडियो ट्रैक्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072420
गूगल ड्राइव में सुनें 1,500 MP3 Audio शिरोमणि अनंत असीम इश्क़ की क्षमता दृष्टिकोण बदलने और असीम प्रेम की क्षमता का अनुभव कराने वाले ऑडियो।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072421
गूगल ड्राइव में सुनें 950 MP3 Audio शिरोमणि रामपाल सैनी खुद का साक्षात्कार हूं आत्म-साक्षात्कार और आत्म-ज्ञान पर केंद्रित विशेष ऑडियो संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072422
गूगल ड्राइव में सुनें 550 MP3 Audio शिरोमणि रामपाल सैनी MP3 शिरोमणि रामपाल सैनी जी के मौलिक प्रवचन एवं ऑडियो व्याख्यान।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072423
गूगल ड्राइव में सुनें 89 MP3 Audio शिरोमणि रामपाल सैनी Short Audios संक्षिप्त और प्रभावशाली मुख्य सूक्तियाँ तथा ऑडियो संदेश।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072424
गूगल ड्राइव में सुनें 🖼️ गैलरी, फोटो एल्बम व वीडियो (Visual Archives) 2,000 Photos Golden Temple शिरोमणि रामपाल सैनी फ़ोटो गोल्डन टेम्पल परिसर के अलौकिक एवं भव्य फोटो संग्रह।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072425
एल्बम देखें 10,000+ Videos मेरा संपूर्ण जीवन शिरोमणि Videos जीवन यात्रा और दिव्य अनुभूतियों को दर्शाते वीडियो रिकॉर्डिंग्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072426
वीडियो देखें 4,000+ Photos / 495 Files शिरोमणि प्रमाण पत्र संग्रह सभी महत्वपूर्ण प्रमाण पत्रों का गूगल फोटो एल्बम एवं ड्राइव आर्काइव।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072427
एल्बम (4000) ड्राइव फ़ाइलें (495) Drive Album Omniverse Gallery ऑम्निवर्स और संपूर्ण ब्रह्मांडीय विज़न की आधिकारिक फोटो गैलरी।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072428
गैलरी खोलें YouTube & Facebook सोशल मीडिया चैनल्स यूट्यूब चैनल और फेसबुक पर उपलब्ध वीडियो संदेश व अपडेट्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072429
YouTube Channel Facebook Video Blogspot Multicosmovision Blog & Case Files सृष्टि, प्रकृति और दार्शनिक विषयों पर गहराई से लिखे गए ब्लॉग्स और केस फाइल्स।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072430
मुख्य ब्लॉग पढ़ें Case File देखें 🛒 स्टोर, शोध एवं घोषणा पत्र (Store & Research) E-Commerce Omniverse Store आधिकारिक ऑम्निवर्स डिजिटल स्टोर जहाँ सभी सेवाएँ उपलब्ध हैं।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072431
स्टोर पर जाएं Manifesto Koyab Founding Declaration Omniversal Manifesto — ब्रह्मांडीय घोषणा पत्र एवं मौलिक विज़न।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072432
घोषणा पत्र पढ़ें Research GitHub Shirmani Research Institute शिरोमणि रिसर्च इंस्टीट्यूट का आधिकारिक GitHub कोड एवं शोध रिपॉजिटरी।
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072433
GitHub Repository 💻 ऑम्निवर्स AI व डिजिटल प्लेटफॉर्म्स (AI Ecosystem) Omniverse AI Portal AI तकनीक आधारित प्लेटफॉर्म पोर्टल खोलें Omniverse Dashboard एकीकृत नियंत्रण डैशबोर्ड डैशबोर्ड देखें Omniverse Supreme Core मुख्य कोर सिस्टम कोर देखें Omniverse Marketplace डिजिटल प्लेटफॉर्म मार्किटप्लेस <a href=" target=
स्रोत: rampaulsaini/Omnivers:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 072434
Runs a set of commands using the runners shell - name: Run a multi-line script run: | echo Add other actions to build, echo test, and deploy your project.
स्रोत: rampaulsaini/Omniverse-:.github/workflows/blank.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072435
name: Specialist Agent — omniverse-core on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "37 2 * * 2" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Omniverse-:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072436
🕊️ *— Shirmani Rampaul Saini, Founder & Vision Architect (Omniverse AI)
स्रोत: rampaulsaini/rampaulsaini:.github/workflows - append - omniverse.yml · स्वतंत्र परीक्षण अपेक्षित।

## 072437
{ // Use IntelliSense to learn about possible attributes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 072438
// Hover to view descriptions of existing attributes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 072439
// For more information, visit: "version": "0.2.0", "configurations": [ { "name": "Python: Remote Attach", "type": "debugpy", "request": "attach", "connect": { "host": "localhost", "port": 3000 }, "pathMappings": [ { "localRoot": "${workspaceFolder}", "remoteRoot": "${workspaceFolder}" } ], "justMyCode": true, "subProcess": true, "runtimeArgs" : [ "--preserve-symlinks", "--preserve-symlinks-main" ] } ] }
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 072440
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072441
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072442
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072443
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072444
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072445
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072446
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072447
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072448
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072449
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072450
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072451
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072452
Managing the state for selecting objects within the scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072453
Performing actions without traditional in-app UI and menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072454
Key Features - Remote communication with the Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072455
Scene loading capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072456
State management for object selection within the USD Viewer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072457
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072458
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072459
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072460
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072461
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072462
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072463
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072464
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072465
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072466
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072467
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072468
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072469
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072470
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072471
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072472
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072473
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072474
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072475
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072476
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072477
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072478
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072479
Basic C++ Extension Template ## Overview The Basic C++ Extension Template is a starting point for developers looking to build C++ based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072480
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072481
Note for Windows C++ Developers** : This template requires that Visual Studio is installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072482
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072483
For additional C++ configuration information [see here](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072484
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072485
Performance sensitive extensions that require the performance benefits of C++.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072486
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072487
Integrating with existing C++ libraries or codebases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072488
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072489
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072490
Usage This section provides instructions for the setup and use of the Basic C++ Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072491
Getting Started To get started with the Basic C++ Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072492
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072493
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072494
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072495
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072496
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072497
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072498
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072499
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072500
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072501
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072502
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072503
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072504
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072505
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072506
Service Setup Extension Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Service Setup Extension Template is designed to facilitate the configuration and setup of a headless service that leverages the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072507
Though it is possible in this case, setup extensions are not typically intended to be used as a generic extension but as a specific component of a particular application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072508
Use Cases This setup extension is well suited for: - Developers building headless services that require Kit SDK functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072509
Key Features - Sample ServiceAPIRouter setup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072510
Sample endpoint to demonstrate interaction patterns within service Kit SDK and OpenUSD.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072511
Usage This extension is automatically created and configured when you generate a new service application using the [Service Application Template](../../apps/kit_service/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072512
Additional Learning - [Omniverse Kit Service Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072513
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072514
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072515
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072516
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072517
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072518
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072519
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072520
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072521
Python UI Extension Template ## Overview The Python UI Extension Template offers a simple starting point for developers looking to build Python-based extensions with performant User Interfaces.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072522
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072523
Use Cases This template is ideal for developers looking to build: - UI based extensions that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072524
Key Features - A simple starter UI demonstrating how to build using the Omni UI framework.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072525
Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072526
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072527
Usage This section provides instructions for the setup and use of the Python UI Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072528
Getting Started To get started with the Python UI Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072529
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072530
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072531
Select desired template with arrow keys ↑↓:**: Python UI Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072532
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072533
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072534
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072535
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072536
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072537
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072538
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072539
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072540
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Omni UI Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072541
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072542
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072543
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072544
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072545
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072546
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072547
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072548
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072549
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072550
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072551
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072552
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072553
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072554
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072555
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072556
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072557
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072558
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072559
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072560
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072561
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072562
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072563
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072564
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072565
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072566
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072567
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072568
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072569
Integrating other C++ or Python libraries as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072570
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072571
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072572
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072573
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072574
USD Explorer Setup Extension Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer Setup Extension Template is specifically designed to configure the USD Explorer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072575
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Explorer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072576
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Explorer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072577
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072578
Key Features - Custom configurations tailored to the USD Explorer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072579
Usage This extension is automatically created and configured when you generate a new application based on the [USD Explorer Template Application](../../apps/usd_explorer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072580
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072581
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072582
Changelog The format is based on [Keep a Changelog]( ## [0.1.2] - 2026-05-11 ### Fixed - `makePrimsPickable` handler raised `UnboundLocalError` when the WebSocket payload was empty or missing the `paths` key, and the broad `except` then leaked the raw Python exception message (including internal variable names) to the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072583
The handler now initializes `paths` to an empty list before the conditional so an empty payload is a clean no-op, and unexpected exceptions are logged server-side via `carb.log_error` while only a generic error string is returned to the client (OMPE-90584, NVBug 6100326).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072584
Added - Regression test `test_make_prims_pickable_empty_payload` covering empty payload, missing-`paths` key, and explicit-empty-list cases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072585
[0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072586
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072587
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072588
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072589
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072590
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072591
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072592
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072593
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - 2024-03-13 - Initial version based on kit service extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072594
{{ extension_display_name }} [{{ extension_name }}] This is an example of a simple Kit Service extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072595
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072596
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 072597
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072598
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072599
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072600
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072601
{{ extension_display_name }} [{{ extension_name }}] A simple python UI extension example.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072602
Use it as a starting point for your extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072603
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072604
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072605
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072606
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072607
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072608
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072609
Args: object: The bound object to register.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072610
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072611
Args: object: The bound object to deregister.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072612
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072613
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072614
Return: The bound object if it exists, an empty object otherwise.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072615
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072616
Return: The id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072617
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072618
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072619
Return: The bound object that was created.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072620
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072621
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072622
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072623
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072624
Args: value_to_multiply: The value to multiply by.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072625
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072626
Return: The toggled bool value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072627
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072628
Args: value_to_append: The value to append.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072629
Return: The new string value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072630
)", py::arg("value_to_append")) /**/; } ```
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 072631
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072632
Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072633
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072634
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072635
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072636
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072637
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072638
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072639
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072640
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072641
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072642
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072643
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 072644
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072645
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072646
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072647
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072648
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072649
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072650
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072651
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072652
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072653
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072654
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072655
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072656
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072657
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 072658
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072659
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072660
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072661
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072662
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072663
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072664
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072665
During Application configuration, you will be prompted for information about these extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072666
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072667
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072668
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072669
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072670
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072671
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072672
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072673
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072674
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072675
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072676
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072677
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072678
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072679
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072680
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072681
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072682
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072683
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072684
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072685
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072686
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072687
The USD Viewer template includes sample assets for this purpose.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072688
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072689
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072690
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072691
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072692
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072693
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072694
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072695
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072696
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072697
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072698
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072699
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072700
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072701
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072702
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072703
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072704
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072705
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072706
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072707
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072708
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072709
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072710
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072711
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072712
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072713
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072714
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072715
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072716
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072717
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072718
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072719
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072720
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072721
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072722
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072723
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072724
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072725
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072726
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072727
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072728
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072729
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072730
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072731
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072732
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072733
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072734
Collaborating on large-scale design projects in real-time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072735
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072736
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072737
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072738
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072739
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072740
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072741
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072742
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072743
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072744
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072745
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072746
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072747
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072748
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072749
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072750
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072751
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072752
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072753
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072754
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072755
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072756
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072757
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072758
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072759
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072760
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072761
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072762
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072763
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072764
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072765
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072766
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072767
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072768
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072769
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072770
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072771
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072772
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072773
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072774
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072775
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072776
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072777
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072778
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072779
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072780
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072781
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072782
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072783
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072784
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072785
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072786
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072787
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072788
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072789
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072790
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072791
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072792
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072793
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072794
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072795
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072796
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072797
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072798
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072799
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072800
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072801
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072802
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072803
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072804
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072805
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072806
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072807
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072808
:warning: **Important**: These layers are not standalone application templates.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072809
They must be used in conjunction with a base application template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072810
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072811
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072812
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072813
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072814
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072815
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072816
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072817
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072818
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072819
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072820
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072821
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072822
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072823
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072824
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072825
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072826
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072827
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072828
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072829
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072830
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072831
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072832
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072833
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072834
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072835
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072836
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072837
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072838
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072839
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072840
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072841
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072842
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072843
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072844
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072845
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072846
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072847
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072848
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072849
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072850
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072851
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072852
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072853
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072854
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072855
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072856
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072857
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072858
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072859
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072860
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072861
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072862
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072863
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072864
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072865
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072866
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072867
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072868
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072869
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072870
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072871
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072872
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072873
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072874
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072875
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072876
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072877
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072878
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072879
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072880
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072881
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072882
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072883
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072884
If multiple container images exist, you will be
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072885
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072886
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072887
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072888
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072889
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072890
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072891
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072892
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072893
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072894
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072895
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072896
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072897
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072898
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072899
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072900
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072901
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072902
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072903
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072904
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072905
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072906
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072907
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072908
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072909
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072910
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072911
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072912
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072913
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072914
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072915
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072916
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072917
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072918
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072919
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072920
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072921
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072922
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072923
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072924
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072925
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072926
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072927
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072928
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072929
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072930
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072931
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072932
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072933
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072934
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072935
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072936
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072937
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072938
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072939
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072940
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072941
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072942
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072943
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072944
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072945
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072946
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072947
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072948
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072949
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072950
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072951
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072952
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072953
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072954
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072955
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072956
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072957
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072958
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072959
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072960
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072961
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072962
Subsequent extensions can be added to the .kit file manually.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072963
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072964
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072965
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072966
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072967
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072968
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072969
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072970
Setup Extension -> kit_service_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072971
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072972
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072973
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072974
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072975
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072976
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072977
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072978
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072979
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072980
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072981
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072982
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072983
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072984
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072985
When adapting an existing extension for a headless service, keep the service execution path limited to the dependencies it requires.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072986
Prefer separating reusable headless logic from UI, viewport, rendering, and other application-specific functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072987
If separation is impractical, dependencies that the service can operate without may be declared optional, provided their imports and initialization are also guarded.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072988
See [Adapting Existing Extensions for Headless Services]( for guidance and examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072989
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072990
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072991
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072992
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072993
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072994
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072995
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072996
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072997
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072998
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 072999
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 073000
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।
