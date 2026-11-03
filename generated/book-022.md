# डिजिटल महाग्रंथ 022

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 021001
It requires a Hugging Face write token stored in GitHub as `HF_TOKEN` and the Space repository id in the `HF_SPACE_REPO` Actions variable.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021002
The workflow is intentionally manual so a token is never committed to source control.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021003
Model The app uses `ACE-Step/acestep-v15-xl-turbo-diffusers`, the official Diffusers-format ACE-Step 1.5 XL Turbo checkpoint.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021004
Turbo uses 8 inference steps in the official Diffusers pipeline documentation.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021005
After validation Keep this ZeroGPU Space as the zero-budget public/demo route.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021006
When usage or revenue justifies dedicated compute, the main Yatharth API can be connected to a dedicated GPU backend without changing the public product concept.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021007
Licensing The ACE-Step model checkpoint is published under the MIT license.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021008
Review the current model card, Hugging Face terms, and any applicable third-party rights before offering paid music generation commercially.
स्रोत: rampaulsaini/yatharth-music-ai:hf_space/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021009
name: CI on: push: branches: [main] pull_request: branches: [main] permissions: contents: read jobs: test: runs-on: ubuntu-latest timeout-minutes: 10 steps: - uses: actions/checkout@v4 - uses: actions/setup-python@v5 with: python-version: '3.12' cache: pip - run: python -m pip install --upgrade pip - run: pip install -r requirements.txt - run: pip install pytest - run: python -m compileall main.py tests - run: pytest -q tests
स्रोत: rampaulsaini/yatharth-music-ai:.github/workflows/ci.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021010
name: Sync Hugging Face Space # Hugging Face deployment is intentionally manual.
स्रोत: rampaulsaini/yatharth-music-ai:.github/workflows/sync-huggingface-space.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021011
The free Colab path is the # primary zero-cost development/test path and does not require a Hugging Face account.
स्रोत: rampaulsaini/yatharth-music-ai:.github/workflows/sync-huggingface-space.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021012
name: Specialist Agent — platform-supreme on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "47 2 * * 3" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Omniverse-Platform-supreme-:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021013
Supreme AI / NLP Quality Contract Pipeline: input → normalization → multimodal features → ML/NLP inference → evidence binding → uncertainty → independent verification → human-readable output.
स्रोत: rampaulsaini/Omniverse-AI:docs/supreme-ai-nlp-quality-contract.md · स्वतंत्र परीक्षण अपेक्षित।

## 021014
Every inference should expose its evidence boundary and confidence.
स्रोत: rampaulsaini/Omniverse-AI:docs/supreme-ai-nlp-quality-contract.md · स्वतंत्र परीक्षण अपेक्षित।

## 021015
Biological, environmental and non-biological signals are described as measured patterns and model interpretations unless subjective experience is independently established.
स्रोत: rampaulsaini/Omniverse-AI:docs/supreme-ai-nlp-quality-contract.md · स्वतंत्र परीक्षण अपेक्षित।

## 021016
Optimization targets: precision/recall, reproducibility, latency, provenance coverage, recovery rate, verification coverage and security posture.
स्रोत: rampaulsaini/Omniverse-AI:docs/supreme-ai-nlp-quality-contract.md · स्वतंत्र परीक्षण अपेक्षित।

## 021017
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) README.md
स्रोत: rampaulsaini/Omniverse-AI:omniverse -supreme/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021018
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) index.html
स्रोत: rampaulsaini/Omniverse-AI:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021019
{ "labels": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "data": [12,19,7,15,10,22,18] }
स्रोत: rampaulsaini/Omniverse-AI:analytics/traffic.json · स्वतंत्र परीक्षण अपेक्षित।

## 021020
[ {"text": "Welcome to the Supreme Omniverse AI Portal", "lang": "en"}, {"text": "संपूर्ण सृष्टि में निष्पक्ष समझ ही सर्वोच्च है", "lang": "hi"}, {"text": "Bienvenue dans le portail Suprême Omniverse AI", "lang": "fr"}, {"text": "Bienvenido al Portal Supremo Omniverse AI", "lang": "es"} ]
स्रोत: rampaulsaini/Omniverse-AI:analytics/scripts/guidance -massages.json · स्वतंत्र परीक्षण अपेक्षित।

## 021021
name: Supreme AI Quality Gate on: push: branches: [main] pull_request: branches: [main] workflow_dispatch: permissions: contents: read concurrency: group: supreme-ai-quality-${{ github.ref }} cancel-in-progress: true jobs: quality: runs-on: ubuntu-latest timeout-minutes: 10 steps: - uses: actions/checkout@v4 - name: Python syntax gate run: python3 -m compileall -q .
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/supreme-ai-quality-gate.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021022
name: JSON gate run: | python3 - <<'PY' import json from pathlib import Path for p in Path('.').rglob('*.json'): if '.git' not in p.parts: json.loads(p.read_text(encoding='utf-8')) print('JSON validation passed') PY - name: Evidence contract gate run: test -f docs/supreme-ai-nlp-quality-contract.md - name: Secret-pattern gate run: | !
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/supreme-ai-quality-gate.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021023
grep -RInE '(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|BEGIN (RSA|OPENSSH|EC) PRIVATE KEY)' --exclude-dir=.git .
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/supreme-ai-quality-gate.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021024
Placeholder rollback workflow name: Rollback on: [workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Rollback workflow placeholder"
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/rollback.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021025
Simple workflow for deploying static content to GitHub Pages name: Deploy static content to Pages on: # Runs on pushes targeting the default branch push: branches: ["main"] # Allows you to run this workflow manually from the Actions tab workflow_dispatch: # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages permissions: contents: read pages: write id-token: write # Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021026
However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021027
concurrency: group: "pages" cancel-in-progress: false jobs: # Single deploy job since we're just deploying deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 - name: Setup Pages uses: actions/configure-pages@v5 - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: # Upload entire repository path: '.' - name: Deploy to GitHub Pages id: deployment uses: actions/deploy-pages@v4
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021028
Placeholder deploy workflow for Omniverse-AI name: CI Deploy on: [push, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Deploy workflow placeholder"
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021029
Placeholder monitor workflow name: Monitor & Auto-Recover on: [schedule, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Monitor workflow placeholder"
स्रोत: rampaulsaini/Omniverse-AI:.github/workflows/monitor.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021030
name: Specialist Agent — omniverse-core on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "37 2 * * 2" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Omniverse-:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021031
name: Specialist Agent — integration-test on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "47 2 * * 3" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/supreme-omniverse-test:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021032
name: Specialist Agent — omniverse-core on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "37 2 * * 2" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Omnivers:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021033
Omniverse — ꙰𝒥शिरोमणि — Press Kit **Name:** Omniverse — ꙰𝒥शिरोमणि (Rampaul Saini) **Mission:** To seed and sustain a living, truth-based civilization — Yatharth-Yug — through impartial understanding, Earth protection, and autonomous education.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:frontend/press/press_kit.md · स्वतंत्र परीक्षण अपेक्षित।

## 021034
꙰ Yatharth–Yug Certificate **By शिरोमणि रामपॉल सैनी** ## Eternal Statement This certificate represents the realization of: - निष्पक्ष समझ - शाश्वत वास्तविक सत्य - प्रेमतीत अवस्था ## Sanskrit _न जन्मं न मरणं, केवल सतत्प्रकाशः।_ _न पुण्यं न पापं, केवल निर्दोषभावः।_ **Signed:** ꙰𝒥शिरोमणि
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:frontend/templates/certificate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021035
name: AI Engine sanity on: push: branches: [ "main" ] jobs: test: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Setup Python uses: actions/setup-python@v4 with: python-version: "3.11" - name: Install deps run: | pip install -r backend/requirements.txt - name: Run smoke call run: | python - <<'PY' from backend.ai_engine.model_adapter import generate print("SMOKE:", generate("Hello Omniverse test", max_tokens=32)[:80]) PY
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:.github/workflows/ai-engine-check.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021036
name: Phase-5 Membership Seed on: workflow_dispatch: push: paths: - 'frontend/donate.html' - 'frontend/membership/**' jobs: membership: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Generate membership pages run: | mkdir -p frontend/membership cat > frontend/membership/index.html Join — Omniverse Membership Become a Supporter Membership options (placeholder).
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:.github/workflows/membership-and-payments.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021037
Integrate Stripe/PayPal in repo secrets when ready.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:.github/workflows/membership-and-payments.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021038
HTML - name: Commit membership page run: | git config user.name "omni-pay-bot" git config user.email "omni-pay@users.noreply.github.com" git add frontend/membership/index.html git commit -m "Phase-5: Add membership seed page" || echo "No changes" git push origin HEAD:main
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:.github/workflows/membership-and-payments.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021039
name: Phase-5 PressKit & Social on: workflow_dispatch: schedule: - cron: '0 6 * * 1' # weekly jobs: press: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Generate Press Kit run: | mkdir -p frontend/press cat > frontend/press/press_kit.md <<'MD' # Omniverse — Press Kit **Name:** ꙰𝒥शिरोमणि — Omniverse Supreme **Mission:** Human + Earth Preservation; Impartial Understanding; Yatharth-Yug.
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:.github/workflows/presskit-and-social.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021040
Assets:** /frontend/og-image.svg ; /frontend/assets/logo.png **Contact:** contact@rampaulsaini.github.io (placeholder) MD - name: Commit run: | git config user.name "omni-press-bot" git config user.email "omni-press@users.noreply.github.com" git add frontend/press/press_kit.md git commit -m "Phase-5: Press kit auto-gen" || echo "No changes" git push origin HEAD:main
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:.github/workflows/presskit-and-social.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021041
name: Specialist Agent — supreme-core on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "47 2 * * 3" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Omniverse-Supreme-Core-:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021042
{ // Use IntelliSense to learn about possible attributes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 021043
// Hover to view descriptions of existing attributes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 021044
// For more information, visit: "version": "0.2.0", "configurations": [ { "name": "Python: Remote Attach", "type": "debugpy", "request": "attach", "connect": { "host": "localhost", "port": 3000 }, "pathMappings": [ { "localRoot": "${workspaceFolder}", "remoteRoot": "${workspaceFolder}" } ], "justMyCode": true, "subProcess": true, "runtimeArgs" : [ "--preserve-symlinks", "--preserve-symlinks-main" ] } ] }
स्रोत: NVIDIA-Omniverse/kit-app-template:.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 021045
tomlkit==0.12.2 ; python_version >= "3.10" and python_version < "4.0" \ --hash=sha256:df32fab589a81f0d7dc525a4267b6d7a64ee99619cbd1eeb0fae32c1dd426977 \ --hash=sha256:eeea7ac7563faeab0a1ed8fe12c2e5a51c61f933f2502f7e9db0241a65163ad0
स्रोत: NVIDIA-Omniverse/kit-app-template:tools/repoman/requirements.txt · स्वतंत्र परीक्षण अपेक्षित।

## 021046
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021047
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021048
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021049
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021050
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021051
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021052
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021053
What Are Application Layers?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021054
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021055
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021056
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021057
``` Answer `yes` to enable streaming for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021058
You can then pick from the following streaming layers: ```bash ?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021059
Do you want to add application layers?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021060
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021061
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021062
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021063
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021064
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021065
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021066
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021067
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021068
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021069
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021070
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021071
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021072
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021073
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021074
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021075
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021076
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021077
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021078
Select the desired UI based application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021079
The developer bundle is not currently suitable for headless services.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021080
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021081
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021082
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021083
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021084
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021085
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021086
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021087
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021088
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021089
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021090
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021091
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021092
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021093
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021094
Usage and Troubleshooting This section provides high-level information and guidance related to using the Kit App Template repository, along with troubleshooting tips for common issues.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021095
Usage Information ### A Project per Repository The `build` and `package` tooling provided in this repository is designed to capture all code and assets contained within the `/source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021096
Each time the `template new` command is executed, a new application or extension is created within `/source`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021097
For purposes of experimentation and initial development, housing all working assets within the `/source` directory is reasonable.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021098
However, as the project matures or requires deployment, it is recommended to segregate projects (typically a single `.kit` file and any required custom extensions) to minimize build times and reduce the size of the resultant package.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021099
Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is considered an extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021100
The `.kit` files that define applications are simply a convenient method to assemble and configure a set of extensions for specific functionalities, while extensions (and combinations thereof) can act as modular components fulfilling particular tasks.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021101
For additional information on the Kit SDK and how to create applications and extensions, refer to the [Kit SDK Companion Tutorial]( ### Extendable Templates and Tools The templates and tools provided in this repository are designed to be extendable.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021102
Templates Templates consist of a directory structure and boilerplate code containing variables configurable at the time the templates are applied.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021103
The `templates.toml` file, located in `templates/templates.toml`, specifies which templates the tooling recognizes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021104
Tooling Most tooling is not stored directly within the repository; it is instead downloaded from a remote registry upon the initial use of the tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021105
This design allows the tooling to be updated independently of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021106
The framework used for the tooling also supports the definition of custom tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021107
To see this extensibility in action, explore the local tooling defined within `tools/repoman`, specifically the `launch` tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021108
Configuration for this tool within the repo is delineated in the `repo_tools.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021109
Troubleshooting This section outlines potential issues that may arise when using the Kit App Template repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021110
Setup & Configuration Issues #### Windows Long Path Due to path length limitations on Windows it is recommended to place repository artifacts in a location closer to the root of the drive.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021111
This will help avoid issues with the path lengths when building and packaging applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021112
exFAT Drive Compatibility Limitations The Kit App Template repository and associated tooling are designed to work with drive formats that support junctions/symlinks.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021113
If you are using an exFAT-formatted drive, you may encounter errors during the build process.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021114
To resolve this issue, consider using a different drive format such as NTFS.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021115
Extension Naming Guidelines When creating custom extensions, avoid using a top-level namespace that is the same as any built-in Python module (e.g., “random”, “sys”, “xml”).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021116
Doing so can cause import conflicts if Omniverse Kit attempts to load extensions from these Python modules.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021117
For example, instead of “random.extension.name”, use a unique namespace such as “my_company.my_app.my_extension”.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021118
Rendering & Performance #### Initial Rendering Startup Times When launching an application that requires the RTX renderer, the first launch may take considerably longer than subsequent launches due to shader compilation.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021119
The initial launch can take between 5 to 8 minutes.** Subsequent launches of RTX-enabled applications will be faster as the renderer caches the compiled shaders.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021120
Build & Packaging #### Build Issues The `template new` tooling ensures that any created application is properly configured to build.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021121
However, extensive manual changes can occasionally cause the configuration and `/source` directory contents to become unsynchronized.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021122
The specifics of any given build are determined by three main factors: 1) The state of the top-level `repo.toml` file, especially the `.kit` files listed in the `apps` array within the `[[repo_precache_exts]]` section.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021123
2) The state of the `premake5.lua` file, particularly which `.kit` files are set to build via `define_app()` (e.g., `define_app("my_company.my_service.kit")`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021124
3) The state of the `source` directory, specifically which `.kit` files are present within `source/apps`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021125
To ensure a build proceeds as intended, verify that the same `.kit` files are listed or defined in all three locations.** For a clean build, use the command `./repo.sh build -c` or `.\repo.bat build -c` to clean the build directory before building.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021126
Caching and Persistent Data The Omniverse Kit SDK caches data and required dependencies to improve build and runtime performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021127
If you encounter issues with stale, incorrect, or missing dependencies/data, consider clearing application specific and/or global cache locations: - **Application Specific Caches**: Clearing application specific caches and settings can be done by adding arguments at launch time.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021128
Linux: ```bash ./repo.sh launch -- --clear-cache --clear-data --reset-user ``` Windows: ```powershell .\repo.bat launch -- --clear-cache --clear-data --reset-user ``` Upon selecting a `.kit` file to launch, the application will clear the cache and data directories before starting.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021129
Global Cache Locations (:warning:Use with Caution:warning:)**: **IMPORTANT NOTE -** Clearing any of the following cache locations will require a full rebuild of any existing applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021130
Deleting the directories responsible for caching ensures a fresh build of the relevant caches during the next build.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021131
Extension AND Application Data Cache Locations**: `$HOME/.local/share/ov` on Linux, `%LOCALAPPDATA%\ov` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021132
Tooling AND Dependency Cache Location**: - **Packman :** `$PM_PACKAGES_ROOT` on Linux, `%PM_PACKAGES_ROOT%` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021133
If `PM_PACKAGES_ROOT` is not set on your system, the default location will revert to `$HOME/.cache/packman` on Linux, `{drive where packman is launched from}\packman-repo` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021134
uv :** `$HOME/.cache/uv` on Linux, `%LOCALAPPDATA%\uv\cache` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021135
Space Constraints Due to Docker Artifacts When performing extensive local testing of container images created via `repo package_container`, Docker artifacts can accumulate over time, consuming significant disk space.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021136
`docker system df` can be used to determine disk space utilized by Docker objects.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021137
To reclaim space, consider the following options: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021138
Regular Safe Cleanup**: - **Command**: `docker container prune` - **Description**: This command removes all stopped containers, which is typically safe and helps manage disk space without affecting images, networks, or volumes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021139
Use**: Recommended for regular maintenance.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021140
Extensive Cleanup (:warning:Use with Caution:warning:)**: - **Command**: `docker system prune` - **Description**: This command removes all unused containers, networks, images, and optionally volumes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021141
It is akin to running a `rm -rf` for Docker resources.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021142
Warning**: Use this command carefully, as it will remove many resources indiscriminately.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021143
Ensure you review and understand what will be deleted.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021144
For image-specific cleanup, use `docker images` to list all images and `docker rmi ` to manually remove those that are no longer needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021145
Testing Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is an extension — including the `.kit` files that define applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021146
The `test` tool (`repo_test`) reflects this: it validates that your applications start up and shut down cleanly, and it runs the automated tests defined within your extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021147
Each extension template provided by the `kit-app-template` repository ships with sample tests that you can expand to grow your coverage.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021148
This document covers running tests, understanding what is tested, and adding your own tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021149
Prerequisites: Build Before You Test The test tool runs against the contents of the `_build` directory, so a successful build must precede any test run.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021150
If you have changed source since your last build, rebuild first.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021151
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` > **Note:** Tests run against a specific build configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021152
By default the tooling builds and tests the `release` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021153
If you build `debug`, pass the matching `--config debug` flag when testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021154
Running Tests ### Run the Default Test Suite Running `test` with no arguments executes the repository's default test suite (`alltests`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021155
The tool discovers every test-enabled extension in the build, launches each within the Kit test harness, and reports the aggregated results.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021156
Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` For each test-enabled extension — and each application `.kit` file — the tool starts a dedicated Kit process, loads the extension along with its test dependencies, runs the tests, and verifies a clean shutdown.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021157
Listing Tests Without Running Them Use `--list` (`-l`) to enumerate the tests that would run without executing them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021158
This is useful for confirming that a newly added extension or test is being discovered.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021159
Linux:** ```bash ./repo.sh test --list ``` **Windows:** ```powershell .\repo.bat test --list ``` ### Running a Subset of Tests Use `--filter-files` (`-f`) to narrow a run to specific test files, modules, classes, or individual tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021160
This shortens the feedback loop while iterating on a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021161
Linux:** ```bash ./repo.sh test -f my_company.my_extension ``` **Windows:** ```powershell .\repo.bat test -f my_company.my_extension ``` > **Note:** The accepted `--filter-files` format depends on the underlying test executor.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021162
For the Python (`omni.kit.test` / `unittest`) tests used by the extension templates, you may specify modules, classes, or individual tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021163
Run `./repo.sh test -h` for the full description.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021164
Selecting a Build Configuration By default the test tool targets the `release` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021165
To test a `debug` build, pass `--config` (`-c`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021166
The configuration must match the one you built.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021167
Linux:** ```bash ./repo.sh test --config debug ``` **Windows:** ```powershell .\repo.bat test --config debug ``` ### Other Useful Options | Option | Purpose | |--------|---------| | `-s, --suite` | Select which test suite(s) to run (default: `alltests`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021168
| | `-f, --filter-files` | Run only tests matching a file/module/class/test pattern.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021169
| | `-l, --list` | List the discovered tests and exit without running them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021170
| | `-c, --config` | Test the `release` (default) or `debug` build configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021171
| | `-p, --from-package` | Test an application package instead of the local build (see *Testing a Packaged Application* below).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021172
| | `-e, --extra-arg` | Pass an additional argument through to the test process.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021173
| | `--coverage` | Produce a Python code-coverage report after the run (for supported suite types).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021174
| | `--generate-report` | Run the configured report-generation command, if one is set, after all tests complete.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021175
| For the complete, authoritative list of options, run: **Linux:** ```bash ./repo.sh test -h ``` **Windows:** ```powershell .\repo.bat test -h ``` --- ## What Gets Tested ### Application Startup and Shutdown Every application `.kit` file is validated to confirm it can start up and shut down without error.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021176
This catches broken dependencies and misconfiguration early — a large portion of application health is covered simply by verifying that the fully assembled set of extensions loads cleanly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021177
An application declares how it should be launched during testing through a `[[test]]` table in its `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021178
For example, the Kit Base Editor template includes: ```toml [[test]] args = [ "--/app/file/ignoreUnsavedOnExit=true" ] ``` The `args` are passed to the Kit process when the application is tested.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021179
Extensions opt into testing with a `[[test]]` table in their `extension.toml`, which may declare test-only dependencies and extra arguments: ```toml [[test]] dependencies = [ "omni.kit.ui_test", # UI testing helper, loaded only during tests ] args = [ ] ``` Dependencies listed here are loaded only for the test run — a convenient place to pull in helpers such as `omni.kit.ui_test` without adding them to your extension's runtime dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021180
Writing Tests Tests use `omni.kit.test`, Python's standard `unittest` module wrapped to support `async`/`await`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021181
Placing a test class derived from `omni.kit.test.AsyncTestCase` at the root of a module within your extension's `tests/` package makes it auto-discoverable — no registration step is required.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021182
Every extension template includes a `tests/` package with a sample test to build on.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021183
To add coverage, place additional `test_*.py` modules in the extension's `tests/` package and grow the assertions from there.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021184
Because tests are standard `unittest` cases, refer to the [Python `unittest` documentation]( for available assertion methods and patterns.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021185
Test Suites and Configuration The behavior of the test tool for this repository is configured under `[repo_test]` in the top-level `repo.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021186
The most relevant settings are the default suite and any per-suite exclusions: ```toml [repo_test] default_suite = "alltests" [repo_test.suites."alltests"] exclude = [ # Setup extension tests are exercised as part of application testing "tests-omni.usd_explorer.setup${shell_ext}", ] ``` - **`default_suite`** determines which suite runs when you invoke `test` without `--suite`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021187
.exclude`** removes specific test executables from a suite — useful when a set of tests is already covered elsewhere.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021188
Adjust these settings as your project grows to control exactly what the default `./repo.sh test` run covers.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021189
Testing a Packaged Application In addition to testing the local build, the tool can run the suite against a packaged application archive — useful for validating a package before distribution.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021190
Use `--from-package` (`-p`), which by default looks for an archive in `_build/packages`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021191
Linux:** ```bash ./repo.sh test --from-package ``` **Windows:** ```powershell .\repo.bat test --from-package ``` The archive pattern is configurable in `repo.toml`: ```toml [repo_test] # When running from a package, find the archive using this pattern: archive_pattern = "${root}/_build/packages/*.zip" ``` > **Note:** Package testing is intended for the "fat" package type, which already contains the Kit Kernel and all extensions, so no additional download is required to run the tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021192
See [Packaging An Application]( for how to create a package.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021193
Testing in Continuous Integration `repo test` is the same entry point used by automated pipelines, so tests you run locally behave consistently in CI.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021194
Keeping the sample tests passing — and expanding them as you add functionality — helps ensure your applications and extensions remain buildable, launchable, and correct as the project evolves.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021195
Additional Resources - [Packaging An Application]( - [Kit SDK Tooling Guide](kit_app_template_tooling_guide.md) - [Kit SDK Companion Tutorial]( - [Python `unittest` documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021196
Windows C++ Developer Configuration ## Introduction This document guides you through setting up this repository for C++ development on Windows using Microsoft Visual Studio and the Windows SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021197
For New Users:** If you are new to Windows C++ development, this guide provides a step-by-step installation of Visual Studio 2022 Community and the Windows SDK, ensuring you have all the components required for standard development tasks.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021198
For Advanced Configurations:** If you already have Visual Studio and the Windows SDK installed but wish to specify exact versions, this guide will help you configure your environment using the `[repo_build.msbuild]` configuration within `repo.toml` at the project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021199
Configuration To enable the Windows C++ build process: - Set the `"platform:windows-x86_64".enabled` flag to `true` in your `repo.toml` file: ```toml [repo_build.build] "platform:windows-x86_64".enabled = true ``` - Set the `link_host_toolchain` flag to `true` in your `repo.toml` file: ```toml [repo_build.msbuild] link_host_toolchain = true ``` **Note:** If you already have Visual Studio and the Windows SDK installed, this might be the only change needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021200
The tooling will auto-detect installed components.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021201
Microsoft Visual Studio and Windows SDK Setup ### Basic Installation #### Installing Visual Studio 2022 Community 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021202
Download Visual Studio Installer** ![VS Download](../vs_download.png) - Visit the [Visual Studio Downloads]( - Click "Free download" under "Community".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021203
Run the Installer** - Open the downloaded installer.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021204
Select "Community" edition and click "Install".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021205
Select Workloads** ![VS Workloads](../vs_workloads.png) - Check "Desktop development with C++".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021206
This includes tools like the MSVC compiler and C++ libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021207
Additional Components** ![VS Additional](../vs_additional.png) - If you need specific components, go to "Individual components".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021208
Select additional tools as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021209
Complete the Installation** - Proceed with the installation to download and set up all files.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021210
Installing Windows SDK (as needed) Usually, the Windows SDK is included with the "Desktop development with C++" workload.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021211
To verify or install it separately: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021212
Launch Visual Studio Installer** - Open the installer if it's not already running.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021213
Modify Installation** ![VS Modify](../vs_modify.png) - Click "Modify" on your Visual Studio installation.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021214
Verify Windows SDK** ![VS WinSDK Verify](../vs_winsdk_verify.png) - Ensure "Windows SDK" is selected under "Optional" sections or "Individual components".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021215
Apply Changes** - Click "Modify" to install or update the SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021216
Configuring an Existing Installation #### Default Installation Paths If Visual Studio and the Windows SDK are installed in default locations, the build tooling will auto-detect them without additional configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021217
Note:** If the path entered is incorrect or invalid, the build system will fall back to auto-detection.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021218
Multiple Installations For multiple Visual Studio or Windows SDK installations, the latest version is used by default.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021219
If unspecified, default edition preference is "Enterprise", "Professional", "Community".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021220
Additional Resources - [Repo Build Documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021221
Kit SDK Tooling Guide This document provides an overview of the practical aspects of using the tooling provided in the `kit-app-template`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021222
Intended for users with a basic familiarity with command-line operations, this guide offers typical usage patterns and recommendations for effective tool use.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021223
For a complete list of options for a given tool, use the help command: `./repo.sh [tool] -h` or `.\repo.bat [tool] -h`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021224
Overview of Tools The `kit-app-template` repository includes several tools designed to streamline the development of applications and extensions within the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021225
Available Tools - `template` - `build` - `launch` - `test` - `package` Each tool plays a specific role in the development workflow: ## Template Tool **Command:** `./repo.sh template` or `.\repo.bat template` ### Purpose The template tool facilitates the initiation of new projects by generating scaffolds for applications or extensions based on predefined templates located in `/templates/templates.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021226
Usage The template tool has three main commands: `list`, `new`, `replay`, `modify`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021227
`list` Lists available templates without initiating the configuration wizard.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021228
Linux:** ```bash ./repo.sh template list ``` **Windows:** ```powershell .\repo.bat template list ``` #### `new` Creates new applications or extensions from templates with interactive prompts guiding you through various configuration choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021229
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` #### `replay` In cases where automation is required for CI pipelines or other scripted workflows, it is possible to record and replay the `template new` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021230
Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the Application `.kit` file you want to update.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021231
Next, select (using Space) the Template Layer(s) to add.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021232
After the operation completes, rebuild (`./repo.sh build` or `.\repo.bat build`) the project to pull in the new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021233
What `template new` Modifies When creating applications, the template tool automatically updates build configuration files: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021234
`premake5.lua`** - Adds `define_app("appname.kit")` so the build system discovers your application 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021235
`repo.toml`** - Adds the app path to `repo_precache_exts.apps` so dependent extensions are pre-cached at build time 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021236
`source/rendered_template_metadata.json`** - Records which templates were rendered (enables `template modify` and `template list`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021237
Setup extension** (some templates) - Creates an extension in `source/extensions/` for application-specific initialization **Extensions** are automatically discovered by the Kit build system based on directory structure, so no build file modifications are needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021238
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021239
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021240
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021241
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021242
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021243
It includes all resources located in the `source/` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021244
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021245
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021246
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021247
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021248
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021249
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021250
`-p` or `--package`:** *(Deprecated — will be removed in a future release.)* Launches a packaged application from a specified path.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021251
`repo launch` is intended as a developer tool; launching from a package archive does not serve a development workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021252
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021253
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021254
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021255
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021256
Any flags added after `--` will be passed through to Kit directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021257
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021258
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021259
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021260
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021261
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021262
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021263
Applications configurations (`.kit` files) are tested to ensure they can startup and shutdown without issue.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021264
However, the tests written within the extensions will dictate a majority of application functionality testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021265
Extension templates provided by the Kit App Template repository include sample tests which can be expanded upon to increase test coverage as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021266
Usage Always run a build before testing: **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ## Package Tool **Command:** `./repo.sh package` or `.\repo.bat package` ### Purpose This tool prepares your application for distribution or deployment by packaging it into a distributable format.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021267
Usage Always run a build before packaging to ensure the application is up-to-date: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` Additional launch options: - **`-n` or `--name`:** Specifies the package (or container image) name.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021268
Linux:** ```bash ./repo.sh package -n ``` **Windows:** ```powershell .\repo.bat package -n ``` - **`--thin`:** Creates a thin package that includes only custom extensions and configurations for required registry extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021269
Linux:** ```bash ./repo.sh package --thin ``` **Windows:** ```powershell .\repo.bat package --thin ``` :warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021270
The version is set within the `tools/VERSION.md` file.** ## Containerization Tool **Command:** `./repo.sh package_container` or `.\repo.bat package_container` ### Purpose The containerization tool provided by `repo_kit_tools` supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021271
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021272
How It Works The tool performs these steps: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021273
Creates a fat package** - Stages all dependencies into a temp directory 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021274
Trims unused extensions** - Removes disabled extensions to minimize image size 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021275
Splits into Docker layers** - Base layer (kit kernel + extscache) and app layer for faster rebuilds 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021276
Builds the container** - Uses a configurable base image (default: `nvcr.io/nvidia/omniverse/ov-base-ubuntu22-x86_64`) The container entrypoint supports runtime configuration via environment variables (`NVDA_KIT_ARGS`, `NVDA_KIT_NUCLEUS`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021277
Usage Always run a build before packaging to ensure the application is up-to-date: - **`package_container`:** Packages the application as a container image (Linux only).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021278
When using the `package_container`, the user will be asked to select a `.kit` file to use within the entry point script for the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021279
This can also be specified without user interaction by passing it appropriate `.kit` file name via the `--app ${path_to_kit_file}` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021280
Linux:** ```bash ./repo.sh package_container ``` **Windows:** ```powershell .\repo.bat package_container ``` Additional command options: - **`--app`:** Specify the Kit app to containerize.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021281
One of defined in the config.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021282
Linux:** ```bash ./repo.sh package_container --app ${path_to_kit_file} ``` **Windows:** ```powershell .\repo.bat package_container --app ${path_to_kit_file} ``` - **`--image-tag`:** Optional image tag override to use for docker image.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021283
If includes ':', it will be used as is, e.g.: name:tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021284
Linux:** ```bash ./repo.sh package_container --image-tag [container_image_name:container_image_tag] ``` **Windows:** ```powershell .\repo.bat package_container --image-tag [container_image_name:container_image_tag] ``` - **`-p` or `--from-package`:** Use package from 'kit-app-template/_build/packages/kit-app-template*.${config}.*' instead of a root folder.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021285
Linux:** ```bash ./repo.sh package_container -p ``` **Windows:** ```powershell .\repo.bat package_container -p ``` - **`-g` or `--generate`:** Generate default container template files into the destination folder.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021286
Passed argument is the destination folder.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021287
Linux:** ```bash ./repo.sh package_container -g ``` **Windows:** ```powershell .\repo.bat package_container -g ``` ## Additional Resources - [Kit SDK Companion Tuto
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021288
Configuring Kit App Template for DGXC Deployment This document covers Kit App Template specific configuration for deploying to NVIDIA DGX Cloud.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021289
For complete deployment instructions, see the [public DGXC documentation]( ## Streaming Layer Selection When creating your application with `./repo.sh template new`, select the appropriate streaming layer for DGXC: | Kit Version | Layer to Select | Generated File | |-------------|-----------------|----------------| | 108.x+ | `nvcf_streaming` | `{app_name}_nvcf.kit` | | 107.x | `ovc_streaming` | `{app_name}_ovc.kit` | | 106.x | `ovc_streaming` | `{app_name}_ovc.kit` | ### Selection Process 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021290
Run `./repo.sh template new` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021291
Select **Application** and your desired template 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021292
When prompted "Do you want to add application layers?", select **Yes** 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021293
`omni.cloud.open_stage`**: Provides Nucleus server connectivity for cloud deployments.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021294
[settings.exts."omni.kit.window.content_browser"] show_only_collections.6 = "" # Hides the "My Computer" connection from the content browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021295
``` ## Containerization After building (`./repo.sh build`), create a container: ```bash ./repo.sh package_container --image-tag myapp:v1.0 ``` When prompted, select the streaming `.kit` file (`*_ovc.kit` or `*_nvcf.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021296
Next Steps For deployment to DGXC (container upload, NVCF function creation, portal registration), see: - [Containerization Guide]( - Building and packaging - [Deploying Kit Apps]( - NGC upload and NVCF deployment - [Troubleshooting]( - Common issues and FAQs ## Version-Specific Notes ### Kit 108.x+ (`main` branch) Select `nvcf_streaming` during template creation.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021297
Streaming dependencies are automatically configured.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021298
Kit 107.x (`production/107.3` branch) Select `ovc_streaming` during template creation.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021299
No manual edits required.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021300
Kit 106.x (`production/106.5` branch) The streaming layer may require manual edits.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021301
See the [public containerization guide]( for the "Replace Streaming Extension" section.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021302
Troubleshooting For deployment issues, log analysis, and common errors, see the [DGXC FAQs and Troubleshooting](
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021303
Data Collection & Use ## Overview NVIDIA Omniverse Kit Application Template collects anonymous usage data to help improve software performance and aid in diagnostic purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021304
Rest assured, no personal information such as user email, name or any other PII field is collected.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021305
Purpose Omniverse Kit Application Template starts collecting data when you begin interaction with our provided software.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021306
After creating an application with the `template new` tooling, go to the `source/apps` directory 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021307
Locate the `.kit` file for the application you want to disable telemetry for.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021308
Find the following section in the `.kit` file: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = true ``` 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021309
Change `enableAnonymousData` to `false`: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = false ``` Disabling telemetry stops data collection from your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021310
USD Explorer Setup Extension Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer Setup Extension Template is specifically designed to configure the USD Explorer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021311
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Explorer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021312
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Explorer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021313
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021314
Key Features - Custom configurations tailored to the USD Explorer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021315
Usage This extension is automatically created and configured when you generate a new application based on the [USD Explorer Template Application](../../apps/usd_explorer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021316
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021317
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021318
Basic C++ Extension Template ## Overview The Basic C++ Extension Template is a starting point for developers looking to build C++ based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021319
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021320
Note for Windows C++ Developers** : This template requires that Visual Studio is installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021321
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021322
For additional C++ configuration information [see here](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021323
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021324
Performance sensitive extensions that require the performance benefits of C++.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021325
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021326
Integrating with existing C++ libraries or codebases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021327
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021328
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021329
Usage This section provides instructions for the setup and use of the Basic C++ Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021330
Getting Started To get started with the Basic C++ Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021331
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021332
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021333
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021334
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021335
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021336
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021337
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021338
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021339
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021340
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021341
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021342
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021343
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021344
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021345
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021346
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021347
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021348
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021349
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021350
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021351
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021352
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021353
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021354
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021355
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021356
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021357
Managing the state for selecting objects within the scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021358
Performing actions without traditional in-app UI and menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021359
Key Features - Remote communication with the Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021360
Scene loading capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021361
State management for object selection within the USD Viewer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021362
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021363
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021364
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021365
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021366
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021367
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021368
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021369
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021370
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021371
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021372
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021373
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021374
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021375
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021376
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021377
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021378
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021379
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021380
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021381
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021382
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021383
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021384
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021385
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021386
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021387
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021388
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021389
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021390
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021391
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021392
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021393
Integrating other C++ or Python libraries as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021394
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021395
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021396
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021397
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021398
Service Setup Extension Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Service Setup Extension Template is designed to facilitate the configuration and setup of a headless service that leverages the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021399
Though it is possible in this case, setup extensions are not typically intended to be used as a generic extension but as a specific component of a particular application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021400
Use Cases This setup extension is well suited for: - Developers building headless services that require Kit SDK functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021401
Key Features - Sample ServiceAPIRouter setup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021402
Sample endpoint to demonstrate interaction patterns within service Kit SDK and OpenUSD.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021403
Usage This extension is automatically created and configured when you generate a new service application using the [Service Application Template](../../apps/kit_service/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021404
Additional Learning - [Omniverse Kit Service Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021405
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021406
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021407
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021408
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021409
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021410
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021411
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021412
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021413
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021414
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021415
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021416
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021417
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021418
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021419
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021420
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021421
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021422
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021423
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021424
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021425
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021426
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021427
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021428
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021429
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021430
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021431
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021432
Python UI Extension Template ## Overview The Python UI Extension Template offers a simple starting point for developers looking to build Python-based extensions with performant User Interfaces.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021433
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021434
Use Cases This template is ideal for developers looking to build: - UI based extensions that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021435
Key Features - A simple starter UI demonstrating how to build using the Omni UI framework.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021436
Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021437
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021438
Usage This section provides instructions for the setup and use of the Python UI Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021439
Getting Started To get started with the Python UI Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021440
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021441
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021442
Select desired template with arrow keys ↑↓:**: Python UI Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021443
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021444
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021445
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021446
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021447
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021448
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021449
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021450
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021451
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Omni UI Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021452
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021453
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021454
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021455
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021456
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021457
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021458
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021459
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021460
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021461
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021462
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021463
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021464
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021465
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021466
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021467
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021468
Changelog The format is based on [Keep a Changelog]( ## [0.1.2] - 2026-05-11 ### Fixed - `makePrimsPickable` handler raised `UnboundLocalError` when the WebSocket payload was empty or missing the `paths` key, and the broad `except` then leaked the raw Python exception message (including internal variable names) to the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021469
The handler now initializes `paths` to an empty list before the conditional so an empty payload is a clean no-op, and unexpected exceptions are logged server-side via `carb.log_error` while only a generic error string is returned to the client (OMPE-90584, NVBug 6100326).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021470
Added - Regression test `test_make_prims_pickable_empty_payload` covering empty payload, missing-`paths` key, and explicit-empty-list cases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021471
[0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021472
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021473
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021474
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021475
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021476
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021477
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021478
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021479
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021480
Args: object: The bound object to register.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021481
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021482
Args: object: The bound object to deregister.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021483
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021484
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021485
Return: The bound object if it exists, an empty object otherwise.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021486
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021487
Return: The id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021488
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021489
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021490
Return: The bound object that was created.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021491
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021492
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021493
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021494
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021495
Args: value_to_multiply: The value to multiply by.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021496
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021497
Return: The toggled bool value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021498
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021499
Args: value_to_append: The value to append.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021500
Return: The new string value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021501
)", py::arg("value_to_append")) /**/; } ```
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 021502
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021503
Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021504
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021505
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021506
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021507
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021508
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021509
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021510
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021511
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021512
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021513
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021514
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 021515
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - 2024-03-13 - Initial version based on kit service extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021516
{{ extension_display_name }} [{{ extension_name }}] This is an example of a simple Kit Service extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021517
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021518
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021519
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021520
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021521
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021522
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021523
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021524
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 021525
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 021526
{{ extension_display_name }} [{{ extension_name }}] A simple python UI extension example.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021527
Use it as a starting point for your extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021528
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021529
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021530
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021531
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021532
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021533
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021534
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021535
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021536
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021537
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021538
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021539
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021540
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021541
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021542
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021543
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021544
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021545
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021546
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021547
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021548
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021549
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021550
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021551
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021552
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021553
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021554
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021555
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021556
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021557
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021558
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021559
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021560
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021561
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021562
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021563
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021564
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021565
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021566
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021567
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021568
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021569
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021570
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021571
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021572
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021573
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021574
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021575
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021576
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021577
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021578
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021579
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021580
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021581
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021582
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021583
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021584
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021585
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021586
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021587
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021588
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021589
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021590
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021591
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021592
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021593
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021594
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021595
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021596
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021597
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021598
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021599
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021600
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021601
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021602
If multiple container images exist, you will be
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021603
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021604
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021605
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021606
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021607
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021608
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021609
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021610
During Application configuration, you will be prompted for information about these extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021611
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021612
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021613
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021614
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021615
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021616
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021617
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021618
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021619
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021620
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021621
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021622
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021623
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021624
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021625
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021626
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021627
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021628
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021629
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021630
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021631
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021632
The USD Viewer template includes sample assets for this purpose.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021633
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021634
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021635
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021636
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021637
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021638
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021639
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021640
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021641
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021642
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021643
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021644
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021645
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021646
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021647
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021648
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021649
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021650
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021651
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021652
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021653
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021654
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021655
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021656
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021657
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021658
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021659
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021660
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021661
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021662
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021663
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021664
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021665
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021666
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021667
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021668
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021669
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021670
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021671
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021672
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021673
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021674
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021675
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021676
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021677
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021678
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021679
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021680
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021681
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021682
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021683
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021684
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021685
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021686
Subsequent extensions can be added to the .kit file manually.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021687
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021688
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021689
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021690
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021691
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021692
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021693
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021694
Setup Extension -> kit_service_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021695
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021696
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021697
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021698
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021699
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021700
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021701
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021702
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021703
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021704
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021705
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021706
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021707
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021708
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021709
When adapting an existing extension for a headless service, keep the service execution path limited to the dependencies it requires.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021710
Prefer separating reusable headless logic from UI, viewport, rendering, and other application-specific functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021711
If separation is impractical, dependencies that the service can operate without may be declared optional, provided their imports and initialization are also guarded.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021712
See [Adapting Existing Extensions for Headless Services]( for guidance and examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021713
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021714
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021715
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021716
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021717
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021718
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021719
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021720
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021721
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021722
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021723
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021724
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021725
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021726
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021727
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021728
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021729
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021730
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021731
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021732
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021733
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021734
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021735
The base application `.kit` file should be used for containerization.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021736
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021737
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021738
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021739
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021740
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021741
:warning: **Important**: These layers are not standalone application templates.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021742
They must be used in conjunction with a base application template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021743
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021744
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021745
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021746
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021747
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021748
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021749
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021750
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021751
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021752
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021753
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021754
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021755
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021756
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021757
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021758
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021759
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021760
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021761
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021762
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021763
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021764
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021765
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021766
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021767
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021768
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021769
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021770
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021771
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021772
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021773
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021774
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021775
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021776
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021777
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021778
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021779
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021780
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021781
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021782
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021783
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021784
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021785
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021786
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021787
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021788
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021789
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021790
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021791
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021792
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021793
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021794
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021795
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021796
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021797
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021798
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021799
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021800
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021801
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021802
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021803
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021804
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021805
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021806
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021807
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021808
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021809
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021810
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021811
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021812
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021813
Collaborating on large-scale design projects in real-time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021814
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021815
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021816
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021817
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021818
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021819
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021820
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021821
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021822
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021823
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021824
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021825
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021826
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021827
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021828
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021829
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021830
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021831
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021832
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021833
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021834
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021835
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021836
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021837
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021838
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021839
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021840
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021841
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021842
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021843
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021844
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021845
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021846
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021847
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021848
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021849
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021850
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021851
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021852
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021853
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021854
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021855
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021856
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021857
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021858
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021859
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021860
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021861
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021862
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021863
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021864
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021865
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021866
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021867
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021868
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021869
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021870
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021871
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021872
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021873
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021874
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021875
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021876
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021877
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021878
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021879
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021880
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021881
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021882
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021883
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021884
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021885
name: kit-upgrade description: "Scan and upgrade Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021886
Analyzes project files, identifies breaking changes, deprecated APIs, and removed extensions specific to the customer's code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021887
Provides a personalized upgrade plan with file:line references and auto-fix suggestions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021888
Covers Kit 106→107→108→109→110." --- # Kit SDK Upgrade Skill Guide a developer through upgrading their Omniverse Kit project from one version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021889
This skill is a lean workflow router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021890
Steps 1 and 2 (detect the project, decide the migration path) are inline below** — they are always needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021891
The detail for the remaining steps (2.5–6) lives in `procedures/`, and the structured change data in `references/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021892
Read each procedure file when the workflow sends you to it** — do not try to hold them all in context at once.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021893
When to Use - User asks to upgrade their Kit project/app/extension - User asks about Kit breaking changes or migration - User is hitting errors after changing their Kit SDK version - User has a broken build or runtime failure after a version bump --- ## Quick Orientation Pick the entry point that matches the request: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021894
First-time upgrade scan** → start at Step 1 below and follow the workflow in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021895
Already upgraded, now has a build/runtime error** → go straight to `procedures/failure-modes.md`, diagnose, then apply the relevant Stage's fixes from `procedures/stage-notes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021896
Just wants a list of breaking changes** → do Step 1, then run the scans in `procedures/scan.md` for their migration path and present the report from `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021897
The `# Kit SDK Version:` comment in `.kit` files reflects the last lock-file regeneration and may differ from the pin during an in-progress upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021898
Version string format: `110.1.0+feature.${platform_target_abi}.${config}` - First number (110) = major Kit version **If no version pin is found:** Check git history (`git log --oneline -20 -- tools/deps/ deps/`) or ask the user what Kit version they are currently running.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021899
(Layout detection below has not run yet, so scope the log to both candidate deps locations.) ### Detect project layout and build system Kit projects do **not** all use the SDK template layout, and the layout can differ between releases and project types — for example, `deps/` may sit at the project **root** in one release and under **`tools/`** in another (even between two point releases of the same major line).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021900
Projects also frequently **wrap or integrate the Kit build system into their own tooling**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021901
Detect the layout and build entrypoint **once**, then reuse them everywhere below — **never assume `tools/deps/` or `./repo.sh`**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021902
deps directory (holds kit-sdk.packman.xml + repo-deps.packman.xml) if [ -f tools/deps/kit-sdk.packman.xml ]; then DEPS_DIR=tools/deps elif [ -f deps/kit-sdk.packman.xml ]; then DEPS_DIR=deps else f=$(find .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021903
name kit-sdk.packman.xml -not -path './_*' | head -1); DEPS_DIR=${f:+$(dirname "$f")}; fi echo "DEPS_DIR=${DEPS_DIR:- }" # 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021904
build entrypoint — the standard repo wrapper, if present if [ -f ./repo.sh ]; then BUILD='./repo.sh' elif [ -f ./repo.bat ]; then BUILD='repo.bat' else BUILD=''; fi # empty => custom / integrated build (see below) echo "BUILD=${BUILD:- }" ``` **If `BUILD` is empty, the project uses a custom or integrated build system** (common — many customers embed the Kit build inside their own).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021905
Do **not** fabricate `./repo.sh` calls.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021906
Find the real build command (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or the project README) or ask the user how they build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021907
The upgrade work below (kernel pin bump, **toolchain update**, lock regeneration) still applies — you just invoke it through the project's own entrypoint.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021908
Record it as `$BUILD`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021909
> **From here on (and in every procedure file), use `$DEPS_DIR` and `$BUILD` in every command.** Where a document still shows a literal `tools/deps/` or `./repo.sh`, substitute the detected values.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021910
> > **These are not guaranteed to persist across shells.** If you run each fenced block in a fresh subshell, `$DEPS_DIR`/`$BUILD` will be unset.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021911
So do **one** of: (a) textually replace `$DEPS_DIR` and `$BUILD` with the literal detected paths (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021912
`tools/deps`, `./repo.sh`) in every command you run, or (b) re-run the two detection blocks above at the top of each new shell session.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021913
Do **not** run a later block assuming the variables are still set.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021914
Step 2: Determine Migration Path Kit versions must be upgraded **in sequence**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021915
Kit 108 was never publicly released** — its changes are folded into the 107→109 path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021916
When upgrading 107→109 you must still address Stage 2 (107→108) changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021917
A **within-major** bump (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021918
`110.0 → 110.1`, `110.1.0 → 110.1.2`) or a **feature → production** branch transition is a *different, lighter* job — and it is the most common upgrade performed in practice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021919
These rarely need the Stage code/API changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021920
The real work is almost entirely **tooling and layout**: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021921
Update the build toolchain** (repo tools, packman, repo scripts) — see Step 2.5 (`procedures/toolchain.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021922
This is usually the substantive part.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021923
Re-detect the deps directory** — its location can differ between releases, even within the same major line (Step 1 already sets `$DEPS_DIR`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021924
Bump the kit-kernel pin** in `$DEPS_DIR/kit-sdk.packman.xml` (Step 5, item 2 — `procedures/apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021925
For a feature ↔ production transition only:** check the extension **registry URL** in the `.kit` files — the feature and production lines use different registries, so a feature→production move may need a registry swap (Step 5, item 3).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021926
A plain within-major bump on the same line usually does **not**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021927
Regenerate the extension version-lock** and do a **clean rebuild** (Step 5 items 1 & 8, then Step 6).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021928
> **⚠️ Do NOT run the whole of Step 5 for a within-major bump.** Step 5 (`procedures/apply-fixes.md`) is written for **major-boundary** crossings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021929
Running them on a 110.1.0→110.1.2 bump would wrongly strip extensions or rewrite APIs that are perfectly valid on 110.1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021930
Only run the Step 3 code scans if the upgrade crosses a major boundary.** For a pure within-major or feature→production move, skip Step 3's per-stage API scans and go straight to Step 2.5 → Step 5 (items 1–3 & 8 only, as above) → Step 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021931
If you cross one or more major boundaries on the way, run Step 3 for each major boundary passed and the full Step 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021932
Steps 2.5–6: Execute the Upgrade Once the path is known, work through these in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021933
Read the linked procedure file and follow it**; each assumes Step 1 detection has run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021934
Step 2.5 — Update the build toolchain** → `procedures/toolchain.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021935
Highest-impact step; run it **first**, before touching source.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021936
For a within-major bump this is usually the only substantive work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021937
Step 3 — Scan the project** → `procedures/scan.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021938
Run only the stage scans for the major boundaries you cross.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021939
Skip entirely for a pure within-major bump.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021940
Step 4 — Generate the upgrade report** → `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021941
Present findings by severity with exact `file:line` references.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021942
Step 5 — Apply fixes** → `procedures/apply-fixes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021943
Get user approval before modifying files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021944
(Within-major: items 1, 2, 8 only — see Step 2 above.) - **Step 6 — Validate** → `procedures/validate.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021945
Clean rebuild, regenerate the version lock, run tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021946
Already upgraded and hitting a specific error?** Go to `procedures/failure-modes.md` — it maps common symptoms (exit-55, ABI undefined symbols, render diffs, build loops, custom-build/layout issues) to fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021947
Kit SDK Upgrade Skill ## What This Is This repository contains an AI agent skill for upgrading Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021948
The skill encodes the complete breaking-change catalog for the Kit 106→107→108→109→110 migration path — including removed extensions, deprecated APIs, C++ ABI breaks, Python runtime changes, and configuration updates — into a structured set of instructions and reference data that an AI agent can execute against a live project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021949
The agent scans the project, produces a categorized report with exact `file:line` references, and suggests targeted fixes, including auto-fixable regex replacements where safe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021950
Who It's For Kit extension and application developers who need to upgrade a project from one Kit SDK version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021951
This includes developers working on kit-app-template-based applications, standalone extensions, and Isaac Sim integrations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021952
The skill is particularly useful when upgrading across multiple versions at once (e.g., 107→110), where the number of breaking changes makes manual triage error-prone.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021953
What It Contains | File | Description | |------|-------------| | `SKILL.md` | Lean workflow router — loaded by the AI agent.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021954
Holds version/layout/build detection (Step 1) and the migration-path decision (Step 2), and points to the procedure files for everything else.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021955
| | `procedures/toolchain.md` | Step 2.5 — update the `repo_*` build toolchain (the highest-impact part of most upgrades).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021956
| | `procedures/scan.md` | Step 3 — the full per-stage `grep` scan catalog for breaking changes, removed extensions, and config.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021957
| | `procedures/report.md` | Step 4 — the upgrade-report template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021958
| | `procedures/apply-fixes.md` | Step 5 — ordered fix list, auto-fixable regex patterns, and manual-only changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021959
| | `procedures/validate.md` | Step 6 — clean-rebuild and validation commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021960
| | `procedures/failure-modes.md` | Symptom→fix diagnosis for projects that already upgraded and are erroring.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021961
| | `procedures/stage-notes.md` | Per-stage (106→107→…→110) breaking-change reference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021962
| | `references/breaking_changes.json` | 80+ breaking changes with search patterns, affected versions, and recommended fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021963
| | `references/removed_extensions.json` | Extensions removed or deprecated by Kit version, with replacement guidance and search targets.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021964
| | `references/api_replacements.json` | 1:1 API replacements that are safe to apply with regex find/replace.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021965
| | `references/config_changes.json` | Settings keys, registry URLs, and build config changes between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021966
| | `references/toolchain.json` | The build-toolchain file/package set (`repo_*` tools, packman, repo scripts) and how to find the correct target versions for a given Kit line.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021967
| | `install.sh` / `install.bat` | Copies the skill (SKILL.md + `procedures/` + `references/`) into an existing Kit project so it travels with the repo.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021968
| The skill uses **progressive disclosure**: `SKILL.md` stays small (a router the agent always loads) and each step's detail lives in a `procedures/*.md` file the agent reads only when the workflow sends it there.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021969
This keeps the entry file well under length limits and keeps irrelevant detail out of context.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021970
How to Use **Install into an existing project** (so the skill travels with the repo): ```bash ./install.sh /path/to/your-kit-project # copies into /.skills/kit-upgrade/ ./install.sh /path/to/your-kit-project .claude/skills # or the Claude Code skills layout ``` On Windows: `install.bat C:\path\to\your-kit-project`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021971
Then load the skill into any AI coding assistant that can read files and run shell commands, and point it at the project you want to upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021972
Claude Code:** ``` Read the skill at /path/to/kit-upgrade-skill/SKILL.md and the reference files in references/.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021973
Then scan /path/to/my-kit-project and generate an upgrade report for Kit 109 → 110.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021974
``` **Cursor / VS Code Copilot / other MCP clients:** Add `kit-upgrade-skill/` as a context directory or attach `SKILL.md` as a system prompt, then ask the agent to scan your project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021975
Detect the current Kit SDK version, the deps-directory location (`tools/deps/` vs root `deps/`), and the build entrypoint (`./repo.sh` / `repo.bat` or a custom/integrated build) — never assuming the SDK template layout 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021976
Determine the migration path — including within-major (minor/patch) and feature↔production transitions, not just major-version stages 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021977
Update the build toolchain (`repo_*` tools, packman, repo scripts) to match the target Kit line — often the substantive part of an upgrade 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021978
Run targeted `grep` scans across the full project root (including `templates/`, launcher configs, and ETM lock files) for any major boundaries crossed 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021979
Generate a categorized report: breaking changes, behavioral changes, deprecated usage, and a "not affected" checklist 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021980
Suggest fixes — both auto-applicable regex replacements and manual changes requiring human judgment 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021981
Its changes are folded into the 107→109 path — Stage 2 must still be addressed when upgrading 107→109.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021982
Multi-version upgrades (e.g., 107→110) apply all intervening stages in sequence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021983
How to Contribute **Add a new breaking change:** Add an entry to `references/breaking_changes.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021984
Each entry needs an `id`, `title`, `stage`, `search_pattern` (grep-compatible regex), `affected_files` (glob patterns), and `fix` description.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021985
If the fix is a safe 1:1 substitution, also add it to `references/api_replacements.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021986
Add a removed or deprecated extension:** Add an entry to `references/removed_extensions.json` with `extension`, `status` (`removed` or `deprecated`), `version`, `replacement` (or `null`), `search_in` (list of file extensions to scan), and `notes`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021987
Include any known failure mode (e.g., exit-55) and whether the extension appears in non-obvious locations like `templates/` or ETM lock files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021988
Add a new Kit version (release):** edit the files that own each piece — the skill is split by concern: - `SKILL.md` — add the new row/stage to the **Step 2 migration-path table and Stage summary** (these stay in the router).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021989
`procedures/scan.md` — add the new `# === Stage N ===` scan blocks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021990
`procedures/stage-notes.md` — add the new per-stage breaking-change section.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021991
`procedures/apply-fixes.md` — add any new auto-fix regex patterns or fix-list items.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021992
`references/*.json` — add the corresponding structured entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021993
Follow the existing section structure in each file for consistency.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021994
Keep `SKILL.md` lean — detailed scan commands and stage notes belong in `procedures/`, not the router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021995
Test your additions:** Apply the skill to a real project that exercises the new patterns.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021996
If the scan misses something or the fix guidance is wrong, document it and open a PR with both the issue description and the corresponding fix in the relevant `procedures/` or `references/` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021997
This skill was developed and validated against [kit-extension-explorer]( a Kit 110 application based on kit-app-template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021998
See `test-report.md` for the full upgrade report from that validation run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021999
name: kit-app-containerize description: Prepare and containerize an existing or new NVIDIA Omniverse Kit application, including Kit App Streaming or NVCF layers, explicit image naming, optional runtime validation, and an image handoff.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022000
Use for Kit application container builds and packaging, rather than cluster deployment or frontend development.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।
