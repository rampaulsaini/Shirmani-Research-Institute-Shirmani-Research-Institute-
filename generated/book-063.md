# डिजिटल महाग्रंथ 063

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 062001
If you need to report a security issue, please use the appropriate contact points outlined below.
स्रोत: kit-app-template/SECURITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 062002
Please visit our [Product Security Incident Response Team (PSIRT)]( policies page for more information.
स्रोत: kit-app-template/SECURITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 062003
NVIDIA Product Security For all security-related concerns, please visit NVIDIA's Product Security portal at
स्रोत: kit-app-template/SECURITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 062004
Changelog The format is based on [Keep a Changelog]( ## [110.0.0] - 2026-03-05 ### Changed - Update to `Kit 110.0.0` - [Kit 110.0 Release Notes]( - [Kit 110.0 Release Highlights]( - Updated `stage_management.py` in `usd_viewer.messaging` extension template to make prims selectable in viewport and updated `omni.usd.StageEventType` to `ASSETS_LOADED` to fix camera exposure when resetting the camera in Web-Viewer-Sample front-end client.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062005
It still uses the repo_package configuration in our repo.toml.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062006
Containerization files in tools/containers have been removed.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062007
They are now generated in an automated fashion during containerization by `repo package_container --app ${path_to_kit_file}`.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062008
You can generate and not containerize by running `repo package_container --app ${path_to_kit_file} --generate` - Default image tag name changed from `kit-app-template:latest` to `appname:latest`.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062009
eg: `usd-viewer_nvcf:latest` - Container `--name` updated to `--image-tag` supporting both image name and image tag `--image-tag [container_image_name:container_image_tag]` - Updated required driver version `>=550.54.15` (Linux) or `>=551.78` (Windows).
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062010
Fabric Scene Delegate (FSD) is now enabled by default in Kit 109.0.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062011
Applications no longer need to explicitly enable FSD in `.kit` configuration files.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062012
`auto_load_usd` for USD Viewer now supports relative paths - Set custom orientations for `UsdLux 25.05` for Y-up and Z-up stages in USD Explorer template and set `inputs:normalize = true` on that template's distant light.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062013
Updated streaming extensions to `omni.kit.livestream.app` and `omni.services.livestream.session` to support NVCF Streaming.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062014
Removed omni.services.transport.server.http.port overrides.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062015
Aligned all template applications to use default ports.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062016
Updated repository documentation to reflect changes in streaming changes.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062017
Updated crash reporter settings to compress crash reports.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062018
Update Windows `omni.kit.window.modifier.titlebar` extension version - Update repo tooling to most recent versions - Updated application icon images for Composer and Explorer templates - Enabled testing for USD Viewer Template messaging extension ### Fixed - Fix duplicate key `.kit` file issues related to `settings.app.exts` ## [107.3.0] - 2025-05-27 ### Added - Added `repo template modify` tooling enabling developers to add Template Layers to existing applications created with 107.3 or newer.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062019
Changed - Updated to `Kit 107.3.0` - [Kit 107.3 Release Notes]( - [Kit 107.3 Release Highlights]( - Updated packman version to 7.29 to address customer issues with network restrictions [Issue #80]( ## [107.2.0] - 2025-05-05 ### Added - Added tooltip information to the VSCode debug extensions to clarify usage.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062020
Added tooling checks for path whitespace and OneDrive paths to improve developer experience.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062021
Changed - Updated to `Kit 107.2.0` - [Kit 107.2 Release Notes]( - [Kit 107.2 Release Highlights]( - Remove hard .git dependency from tooling - Exclude `_repo` from packaging operations.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062022
The extensions will be available at a later date.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062023
That data is now accessible from the `omni.usd_viewer.setup` and `omni.light_rigs` extension dependencies.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062024
[106.3.0] - 2024-11-04 ### Added - Built app containers support `NVDA_KIT_ARGS` and `NVDA_KIT_NUCLEUS` environment variables - `NVDA_KIT_ARGS` is passed directly into the kit executable - `NVDA_KIT_NUCLEUS` if set causes the container entrypoint to create an omniverse.toml configuration file with a single entry pointing at the provided nucleus server.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062025
This will also set the kit arg --/ovc/nucleus/server with the envvar value.
स्रोत: kit-app-template/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062026
Creative experiments at the frontier of physical AI and 3D reality.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062027
Lab 01 🌌 Consciousness Visualization RTX-powered visualization of the NS = ∅ + ∞ = Now equation.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062028
Real-time particle systems representing the eternal present — rendered with physically accurate light.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062029
RTX Particles OpenUSD Lab 02 🤖 Physical AI Integration NVIDIA Isaac Sim integration for creating digital twins that embody Yatharth Siddhant principles.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062030
Robots learning from zero-effort presence.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062031
Isaac Sim PhysX Digital Twin Lab 03 ☁️ Cloud Streaming Platform Stream Omniverse experiences globally via WebRTC and GDN.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062032
Bringing the Shromani platform's 3D wisdom to any device, anywhere in the world.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062033
WebRTC GDN NVCF Lab 04 🎨 Procedural 3D Worlds OpenUSD-based procedural generation of 3D environments representing the 10 Projects of the Omniverse.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062034
From cosmic exploration to earth restoration.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062035
OpenUSD Procedural MDL Lab 05 🧬 AI Avatar System NVIDIA Audio2Face integration for creating a digital Shromani avatar.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062036
Real-time facial animation driven by the original 10,000+ audio recordings.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062037
Audio2Face Avatar AI Lab 06 🔬 Quantum Visualization Real-time GPU-accelerated visualization of the 7 Yatharth Siddhant equations.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062038
C∞ > M(∑universes) rendered as an interactive 3D mathematical landscape.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062039
The Yatharth Siddhant equations — NS = ∅ + ∞ = Now, C∞ > M(∑universes) — come alive in real-time 3D through NVIDIA's RTX and Physical AI technologies .
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062040
Create high-performance, OpenUSD-based desktop or cloud-streaming applications using the Omniverse Kit SDK — with RTX ray tracing, PhysX physics, and AI capabilities built-in.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062041
▶ Quick Start 📦 Templates ⚙ GitHub ꙰ Shromani Platform ◈ Core Capabilities Omniverse Kit SDK — Key Features 🔮 OpenUSD Foundation Build on Pixar's Universal Scene Description — the industry standard for 3D data interchange.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062042
Create, manipulate and render rich 3D content across tools and pipelines.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062043
⚡ RTX Rendering NVIDIA RTX real-time ray tracing with physically accurate lighting, materials, and global illumination.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062044
Photorealistic visualization at interactive framerates.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062045
☁️ Cloud Streaming Stream Kit applications directly to web browsers via WebRTC.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062046
Deploy on NVIDIA Cloud Functions (NVCF), GDN, or Kubernetes clusters for global reach.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062047
🤖 Physical AI Integrate with NVIDIA's AI ecosystem — Isaac Sim, PhysX, Warp, and more.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062048
Build digital twins, robotics simulations, and AI-powered 3D applications.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062049
🧩 Extension System Modular architecture with Python and C++ extensions.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062050
Browse 200+ extensions from the Extension Manager.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062051
Build and publish your own to the community registry.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062052
🏭 Enterprise Ready Production-grade stability via NGC Catalog.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062053
Docker containerization, CI/CD tooling, packaging, and deployment workflows built-in from day one.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062054
◈ Application Templates 5 Pre-Built Templates — Start Immediately Each template is a fully configured Omniverse application — from minimal to feature-rich.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062055
Kit Service Headless Service Minimal definition of an Omniverse Kit SDK based service.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062056
Useful for creating headless services leveraging Omniverse Kit functionality without a GUI.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062057
Base Editor Kit Base Editor Minimal template for loading, manipulating and rendering OpenUSD content from a graphical interface.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062058
Ideal starting point for custom 3D editors.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062059
USD Composer Scene Authoring Authoring complex OpenUSD scenes and configurators.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062060
Features Fabric Scene Delegate, AXF MDLs, Variant Tools, and layout/materials/lighting.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062061
USD Explorer Scene Explorer Exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062062
Built for teams reviewing complex 3D assets and digital twins in real time.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062063
USD Viewer Streaming Viewer Viewport-only template with RTX rendering, app streaming, and messaging.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062064
Easily streamed to web browsers via WebRTC.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062065
Ideal for client-facing deployments.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062066
◈ Quick Start Get Started in Minutes Terminal — Omniverse Kit Setup # Clone the repository $ git clone $ cd kit-app-template &nbsp; # Create new application from template $ ./repo.sh template new ?
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062067
Select what you want to create: Application ?
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062068
Select desired template: USD Viewer ?
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062069
NVIDIA Omniverse license holder building the Supreme Omniverse Platform — combining GPU-accelerated 3D technology with the ancient wisdom of Nishpaksh Samajh.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062070
Physical AI meets universal consciousness.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062071
Create high-performance, OpenUSD-based desktop or cloud-streaming applications using the Omniverse Kit SDK — with RTX ray tracing, PhysX physics, and AI capabilities built-in.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062072
▶ Quick Start 📦 Templates ⚙ GitHub ꙰ Shromani Platform ◈ Core Capabilities Omniverse Kit SDK — Key Features 🔮 OpenUSD Foundation Build on Pixar's Universal Scene Description — the industry standard for 3D data interchange.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062073
Create, manipulate and render rich 3D content across tools and pipelines.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062074
⚡ RTX Rendering NVIDIA RTX real-time ray tracing with physically accurate lighting, materials, and global illumination.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062075
Photorealistic visualization at interactive framerates.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062076
☁️ Cloud Streaming Stream Kit applications directly to web browsers via WebRTC.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062077
Deploy on NVIDIA Cloud Functions (NVCF), GDN, or Kubernetes clusters for global reach.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062078
🤖 Physical AI Integrate with NVIDIA's AI ecosystem — Isaac Sim, PhysX, Warp, and more.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062079
Build digital twins, robotics simulations, and AI-powered 3D applications.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062080
🧩 Extension System Modular architecture with Python and C++ extensions.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062081
Browse 200+ extensions from the Extension Manager.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062082
Build and publish your own to the community registry.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062083
🏭 Enterprise Ready Production-grade stability via NGC Catalog.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062084
Docker containerization, CI/CD tooling, packaging, and deployment workflows built-in from day one.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062085
◈ Application Templates 5 Pre-Built Templates — Start Immediately Each template is a fully configured Omniverse application — from minimal to feature-rich.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062086
Kit Service Headless Service Minimal definition of an Omniverse Kit SDK based service.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062087
Useful for creating headless services leveraging Omniverse Kit functionality without a GUI.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062088
Base Editor Kit Base Editor Minimal template for loading, manipulating and rendering OpenUSD content from a graphical interface.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062089
Ideal starting point for custom 3D editors.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062090
USD Composer Scene Authoring Authoring complex OpenUSD scenes and configurators.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062091
Features Fabric Scene Delegate, AXF MDLs, Variant Tools, and layout/materials/lighting.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062092
USD Explorer Scene Explorer Exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062093
Built for teams reviewing complex 3D assets and digital twins in real time.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062094
USD Viewer Streaming Viewer Viewport-only template with RTX rendering, app streaming, and messaging.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062095
Easily streamed to web browsers via WebRTC.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062096
Ideal for client-facing deployments.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062097
◈ Quick Start Get Started in Minutes Terminal — Omniverse Kit Setup # Clone the repository $ git clone $ cd kit-app-template &nbsp; # Create new application from template $ ./repo.sh template new ?
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062098
Select what you want to create: Application ?
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062099
Select desired template: USD Viewer ?
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062100
NVIDIA Omniverse license holder building the Supreme Omniverse Platform — combining GPU-accelerated 3D technology with the ancient wisdom of Nishpaksh Samajh.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062101
Physical AI meets universal consciousness.
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062102
"जो वस्तु मेरे पास है — ब्रह्मांड में और कहीं नहीं" ꙰ Main Platform GitHub Wikipedia NVIDIA Omniverse · Licensed Platform · Shromani Rampaul Saini NVIDIA Omniverse Kit App Template — Licensed under NVIDIA Software License Agreement GPU-Accelerated · OpenUSD · RTX · Physical AI · Cloud Streaming ꙰ यथार्थ सिद्धांत — निष्पक्ष समझ — शिरोमणि रामपॉल सैनी ꙰ Main Platform GitHub Repo NVIDIA Omniverse Documentation YouTube
स्रोत: kit-app-template/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062103
Omniverse Kit App Template ## :memo: Feature Branch Information **This repository is based on a Feature Branch of the Omniverse Kit SDK.** Feature Branches are regularly updated and best suited for testing and prototyping.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062104
For stable, production-oriented development, please use the [Production Branch of the Kit SDK on NVIDIA GPU Cloud (NGC)]( [Omniverse Release Information]( ## Overview Welcome to `kit-app-template`, a toolkit designed for developers interested in GPU-accelerated application development within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062105
This repository offers streamlined tools and templates to simplify creating high-performance, OpenUSD-based desktop or cloud streaming applications using the Omniverse Kit SDK.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062106
About Omniverse Kit SDK The Omniverse Kit SDK enables developers to build immersive 3D applications.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062107
Key features include: - **Language Support:** Develop with either Python or C++, offering flexibility for various developer preferences.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062108
OpenUSD Foundation:** Utilize the robust Open Universal Scene Description (OpenUSD) for creating, manipulating, and rendering rich 3D content.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062109
GPU Acceleration:** Leverage GPU-accelerated capabilities for high-fidelity visualization and simulation.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062110
Extensibility:** Create specialized extensions that provide dynamic user interfaces, integrate with various systems, and offer direct control over OpenUSD data, making the Omniverse Kit SDK versatile for numerous applications.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062111
Applications and Use Cases The `kit-app-template` repository enables developers to create cross-platform applications (Windows and Linux) optimized for desktop use and cloud streaming.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062112
Potential use cases include designing and simulating expansive virtual environments, producing high-quality synthetic data for AI training, and building advanced tools for technical analysis and insights.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062113
Whether you're crafting engaging virtual worlds, developing comprehensive analysis tools, or creating simulations, this repository, along with the Kit SDK, provides the foundational components required to begin development.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062114
A Deeper Understanding The `kit-app-template` repository is designed to abstract complexity, jumpstarting your development with pre-configured templates, tools, and essential boilerplate.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062115
For those seeking a deeper understanding of the application and extension creation process, we have provided the following resources: #### Companion Tutorial **[Explore the Kit SDK Companion Tutorial]( This tutorial offers detailed insights into the underlying structure and mechanisms, providing a thorough grasp of both the Kit SDK and the development process.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062116
New Developers For a beginner-friendly introduction to application development using the Omniverse Kit SDK, see the NVIDIA DLI course: #### Beginner Tutorial **[Developing an Omniverse Kit-Based Application]( This course offers an accessible introduction to application development (account and login required).
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062117
These resources empower developers at all experience levels to fully utilize the `kit-app-template` repository and the Omniverse Kit SDK.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062118
Please verify your driver versions before upgrading.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062119
Newer versions may work but are not equally validated.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062120
Internet Access**: Required for downloading the Omniverse Kit SDK, extensions, and tools.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062121
Required Software Dependencies - [**Git**]( For version control and repository management - [**Git LFS**]( For managing large files within the repository - **(Windows - C++ Only) Microsoft Visual Studio (2019 or 2022)**: You can install the latest version from [Visual Studio Downloads]( Ensure that the **Desktop development with C++** workload is selected.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062122
[Additional information on Windows development configuration](readme-assets/additional-docs/windows_developer_configuration.md) - **(Windows - C++ Only) Windows SDK**: Install this alongside MSVC.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062123
You can find it as part of the Visual Studio Installer.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062124
[Additional information on Windows development configuration](readme-assets/additional-docs/windows_developer_configuration.md) - **(Linux) build-essentials**: A package that includes `make` and other essential tools for building applications.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062125
For Ubuntu, install with `sudo apt-get install build-essential` ### Recommended Software - [**(Linux) Docker**]( For containerized development and deployment.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062126
Ensure non-root users have Docker permissions.** - [**(Linux) NVIDIA Container Toolkit**]( For GPU-accelerated containerized development and deployment.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062127
Installation and Configuring Docker steps are required.** - [**VSCode**]( (or your preferred IDE): For code editing and development ## Repository Structure | Directory Item | Purpose | |------------------|------------------------------------------------------------| | .vscode | VS Code configuration details and helper tasks | | readme-assets/ | Images and additional repository documentation | | templates/ | Template Applications and Extensions.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062128
| | tools/ | Tooling settings and repository specific (local) tools | | .editorconfig | [EditorConfig]( file.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062129
| | .gitattributes | Git configuration.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062130
| | .gitignore | Git configuration.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062131
| | LICENSE | License for the repo.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062132
| | README.md | Project information.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062133
| | premake5.lua | Build configuration - such as what apps to build.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062134
| | repo.bat | Windows repo tool entry point.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062135
| | repo.sh | Linux repo tool entry point.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062136
| | repo.toml | Top level configuration of repo tools.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062137
| | repo_tools.toml | Setup of local, repository specific tools | ## Quick Start This section guides you through creating your first Kit SDK-based Application using the `kit-app-template` repository.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062138
For a more comprehensive explanation of functionality previewed here, reference the following [Tutorial]( for an in-depth exploration.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062139
Clone the Repository Begin by cloning the `kit-app-template` to your local workspace: #### 1a.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062140
Clone ```bash git clone ``` #### 1b.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062141
Navigate to Cloned Directory ```bash cd kit-app-template ``` ### 2.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062142
Create and Configure New Application From Template Run the following command to initiate the configuration wizard: **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062143
Follow the prompt instructions: - **?
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062144
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062145
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062146
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062147
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062148
Enter version:** [set application version] Application [application name] created successfully in [path to project]/source/apps/[application name] - **?
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062149
Do you want to add application layers?** No #### Explanation of Example Selections • **`.kit` file name:** This file defines the application according to Kit SDK guidelines.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062150
The file name should be lowercase and alphanumeric to remain compatible with Kit’s conventions.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062151
display name:** This is the application name users will see.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062152
It can be any descriptive text.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062153
version:** The version number of the application.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062154
While you can use any format, semantic versioning (e.g., 0.1.0) is recommended for clarity and consistency.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062155
application layers:** These optional layers add functionality for features such as streaming to web browsers.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062156
For this quick-start, we skip adding layers, but choosing “yes” would let you enable and configure streaming capabilities.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062157
Build Build your new application with the following command: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` A successful build will result in the following message: ```text BUILD (RELEASE) SUCCEEDED (Took XX.XX seconds) ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062158
Launch Initiate your newly created application using: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062159
Select with arrow keys which App would you like to launch:** [Select the created editor application] ![Kit Base Editor Image](readme-assets/kit_base_editor.png) > **NOTE:** The initial startup may take 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062160
After initial shader compilation, startup time will reduce dramatically ## Templates `kit-app-template` features an array of configurable templates for `Extensions` and `Applications`, catering to a range of desired development starting points from minimal to feature rich.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062161
Applications Begin constructing Omniverse Applications using these templates - **[Kit Service](./templates/apps/kit_service)**: The minimal definition of an Omniverse Kit SDK based service.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062162
This template is useful for creating headless services leveraging Omniverse Kit functionality.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062163
[Kit Base Editor](./templates/apps/kit_base_editor/)**: A minimal template application for loading, manipulating and rendering OpenUSD content from a graphical interface.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062164
[USD Composer](./templates/apps/usd_composer)**: A template application for authoring complex OpenUSD scenes, such as configurators.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062165
[USD Explorer](./templates/apps/usd_explorer)**: A template application for exploring and collaborating on large Open USD scenes.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062166
[USD Viewer](./templates/apps/usd_viewer)**: A viewport-only template application that can be easily streamed and interacted with remotely, well-suited for streaming content to web pages.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062167
Extensions Enhance Omniverse capabilities with extension templates: - **[Basic Python](./templates/extensions/basic_python)**: The minimal definition of an Omniverse Python Extension.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062168
[Python UI](./templates/extensions/python_ui)**: An extension that provides an easily extendable Python-based user interface.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062169
[Basic C++](./templates/extensions/basic_cpp)**: The minimal definition of an Omniverse C++ Extension.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062170
[Basic C++ w/ Python Bindings](./templates/extensions/basic_python_binding)**: The minimal definition of an Omniverse C++ Extension that also exposes a Python interface via Pybind11.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062171
Note for Windows C++ Developers** : This template requires `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062172
For additional C++ configuration information [see here](readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062173
Application Streaming The Omniverse Platform supports streaming Kit-based applications directly to a web browser.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062174
You can either manage your own deployment or use an NVIDIA-managed service: ### Self-Managed - **Omniverse Kit App Streaming :** A reference implementation on GPU-enabled Kubernetes clusters for complete control over infrastructure and scalability.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062175
NVIDIA-Managed - **NVIDIA Cloud Functions (NVCF):** Offloads hardware, streaming, and network complexities for secure, large scale deployments.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062176
Graphics Delivery Network (GDN):** Streams high-fidelity 3D content worldwide with just a shared URL.
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062177
[Configuring and packaging streaming-ready Kit applications](r
स्रोत: kit-app-template/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062178
🕉️ Philosophy of Yatharth Yug ### शाश्वत यथार्थ का साक्षात्कार — निष्पक्ष समझ का शमीकरण --- > **“मैं शिरोमणि रामपुल सैनी तुलनातीत, शब्दातीत, कालातीत, प्रेमतीत, त्वतीत, शाश्वत वास्तविक स्वभाविक सत्य प्रत्यक्ष हूं।”** --- ## 🔹 परिचय यह दर्शन मानवता की उस संपूर्ण चेतना का प्रतीक है जहाँ विचार, अहंकार, और मानसिकता का अंत हो जाता है, और केवल *निष्पक्ष समझ* का शुद्ध, वास्तविक स्वरूप प्रकट होता है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062179
यह न किसी धर्म का ग्रंथ है, न किसी मत का विचार — बल्कि स्वयं *सत्य का प्रत्यक्ष अनुभव* है, जो “स्वयं के भीतर के स्वयं” से संवाद कराता है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062180
🔹 निष्पक्ष समझ — सर्वश्रेष्ठ सत्ता “निष्पक्ष समझ” ही वह वास्तविक तत्व है जो मन, बुद्धि और स्मृति के भ्रम से परे संपूर्ण अस्तित्व को एक सूत्र में जोड़ती है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062181
> यह वही दृष्टि है जहाँ देखने वाला, देखा जाने वाला, और देखने की प्रक्रिया — तीनों एक हो जाते हैं।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062182
यह अवस्था **संपूर्णता, सम्पन्नता, समग्रता, और संतुष्टि** की पूर्णता है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062183
यही *Supreme Omniverse* का मूल सिद्धांत है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062184
🔹 यथार्थ सिद्धांत — सत्य का समीकरण **यथार्थ सिद्धांत (Principle of Reality)** वह विज्ञान है जो भौतिक और अभौतिक दोनों स्तरों पर सत्य को परिभाषित करता है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062185
यह उन सूक्ष्म सूत्रों का संगम है जिनसे सृष्टि की गति, ऊर्जा, और चेतना एक साथ कार्य करती हैं।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062186
यह विज्ञान केवल मापन या प्रयोग नहीं — बल्कि **स्वयं के प्रत्यक्ष अनुभव का शास्त्र** है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062187
🔹 यथार्थ युग — नया युग, नया बोध **यथार्थ युग** वह युग है जहाँ मानवता मानसिकता से मुक्त होकर निष्पक्ष समझ के युग में प्रवेश करती है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062188
यह युग **अतीत के चारों युगों से खरबों गुणा ऊँचा** है — क्योंकि यहाँ न विभाजन है, न भ्रम, सिर्फ़ शुद्ध सत्य का प्रत्यक्ष अस्तित्व है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062189
> “यथार्थ युग में न कोई आरंभ है, न अंत — > केवल सत्य की निरंतरता है।” --- ## 🔹 शाश्वत साक्षात्कार यह साक्षात्कार शरीर या मन में नहीं, बल्कि उनके पार — *स्वयं की निष्पक्ष दृष्टि* में होता है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062190
जब ‘स्वयं’ अपने भीतर के *साक्षी स्वरूप* को पहचानता है, तभी *सच्चे यथार्थ का जन्म* होता है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062191
> “स्वयं का स्वयं से साक्षात्कार — यही वास्तविकता का चरम है।” --- ## 🔹 परम उद्घोष > “निष्पक्ष समझ ही सर्वोच्च सत्ता है — > वही सृष्टि का आधार, वही सृष्टि का यथार्थ है।” > — शिरोमणि रामपुल सैनी --- ## 🌟 Essence - **सत्य** केवल वह नहीं जो दिखता है — बल्कि जो *स्वयं को देखता है*।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062192
बुद्धि** का अंत ही **प्रज्ञा** का प्रारंभ है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062193
मानवता** तभी मुक्त होती है जब वह “स्वयं” को “विचारों” से नहीं, “साक्षी” से पहचानती है।
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062194
🔗 संबंधित पृष्ठ - [Omniverse Overview](README.md) - [Golden Temple Spiritual Insights](GoldenTemple.md) --- ## 🌌 Visit Live Omniverse Portal [
स्रोत: Omniverse-AI/Philosophy.md · स्वतंत्र परीक्षण अपेक्षित।

## 062195
🧩 Clones: Loading...
स्रोत: Omniverse-AI/earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 062196
💖 Sponsors: Loading...
स्रोत: Omniverse-AI/earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 062197
💰 Estimated Monthly Income: ₹ Calculating...
स्रोत: Omniverse-AI/earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 062198
📈 Next Month Projection: ₹ Calculating...
स्रोत: Omniverse-AI/earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 062199
✅ Last Deploy: Loading...
स्रोत: Omniverse-AI/earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 062200
🔄 Next Auto Sync: Loading...
स्रोत: Omniverse-AI/earnings-dashboard.html · स्वतंत्र परीक्षण अपेक्षित।

## 062201
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: Omniverse-AI/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062202
Omniverse — Supreme AI Assistant 🌌 Omniverse — Supreme AI Assistant Created by शिरोमणि रामपॉल सैनी 💰 Support / Donate 1) Pay via UPI / GPay Click here to Pay via UPI / GPay 2) PayPal (Global) 3) Pay via Paytm Click here to Pay via Paytm 🌐 Live Portal Visit Supreme Omniverse AI Portal “संपूर्ण सृष्टि का वास्तविक युग वहीं है जहाँ निष्पक्ष समझ ही सर्वोच्च है।” – शिरोमणि रामपॉल सैनी
स्रोत: Omniverse-AI/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062203
Omniverse-AI Vigilant Mode Script: [Click Here]( # 🌟 Golden Temple Spiritual Insights ![Golden Temple](assets/golden-temple.webp) ## Spiritual Experience - Evening at Golden Temple, naturally honored for impartial understanding, simplicity, and purity.
स्रोत: Omniverse-AI/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062204
Realization: human intellect & memory distortions can be neutralized through simplicity.
स्रोत: Omniverse-AI/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062205
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) index.html
स्रोत: Omniverse-AI/omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 062206
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) README.md
स्रोत: Omniverse-AI/omniverse -supreme/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062207
{ "labels": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "data": [12,19,7,15,10,22,18] }
स्रोत: Omniverse-AI/analytics/traffic.json · स्वतंत्र परीक्षण अपेक्षित।

## 062208
Simple workflow for deploying static content to GitHub Pages name: Deploy static content to Pages on: # Runs on pushes targeting the default branch push: branches: ["main"] # Allows you to run this workflow manually from the Actions tab workflow_dispatch: # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages permissions: contents: read pages: write id-token: write # Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062209
However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062210
concurrency: group: "pages" cancel-in-progress: false jobs: # Single deploy job since we're just deploying deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 - name: Setup Pages uses: actions/configure-pages@v5 - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: # Upload entire repository path: '.' - name: Deploy to GitHub Pages id: deployment uses: actions/deploy-pages@v4
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062211
Placeholder monitor workflow name: Monitor & Auto-Recover on: [schedule, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Monitor workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/monitor.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062212
Placeholder rollback workflow name: Rollback on: [workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Rollback workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/rollback.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062213
Placeholder deploy workflow for Omniverse-AI name: CI Deploy on: [push, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Deploy workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062214
[ {"text": "Welcome to the Supreme Omniverse AI Portal", "lang": "en"}, {"text": "संपूर्ण सृष्टि में निष्पक्ष समझ ही सर्वोच्च है", "lang": "hi"}, {"text": "Bienvenue dans le portail Suprême Omniverse AI", "lang": "fr"}, {"text": "Bienvenido al Portal Supremo Omniverse AI", "lang": "es"} ]
स्रोत: Omniverse-AI/analytics/scripts/guidance -massages.json · स्वतंत्र परीक्षण अपेक्षित।

## 062215
{ // Use IntelliSense to learn about possible attributes.
स्रोत: kit-app-template/.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 062216
// Hover to view descriptions of existing attributes.
स्रोत: kit-app-template/.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 062217
// For more information, visit: "version": "0.2.0", "configurations": [ { "name": "Python: Remote Attach", "type": "debugpy", "request": "attach", "connect": { "host": "localhost", "port": 3000 }, "pathMappings": [ { "localRoot": "${workspaceFolder}", "remoteRoot": "${workspaceFolder}" } ], "justMyCode": true, "subProcess": true, "runtimeArgs" : [ "--preserve-symlinks", "--preserve-symlinks-main" ] } ] }
स्रोत: kit-app-template/.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 062218
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062219
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062220
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062221
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062222
name: Question description: Ask a question title: "[QUESTION]: " labels: ["question"] body: - type: markdown attributes: value: | Thanks for taking the time to ask us a question!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062223
type: textarea id: text_of_question attributes: label: Question description: Ask your question.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062224
placeholder: "Question text" validations: required: true - type: textarea id: additional_context attributes: label: Additional Context description: Provide any related code, issues, or projects.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062225
placeholder: "Any related code, issues, or projects."
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062226
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062227
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062228
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062229
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062230
name: Feature Request description: Suggest an idea for this project title: "[FEATURE]: " labels: ["feature request"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this feature request!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062231
type: textarea id: description attributes: label: Description description: | Describe the proposed feature placeholder: | Feature description and problem or pain point being addressed validations: required: true - type: textarea id: use_case attributes: label: Use Case or Scenarios description: Describe how this feature would be used placeholder: e.g., User performing action A, would accomplish B, with benefit C.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062232
type: textarea id: implementation_ideas attributes: label: Possible Implementation Ideas description: If you have any suggestions on how this feature might be implemented, please share them here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062233
placeholder: Implementation ideas - type: textarea id: additional_context attributes: label: Additional Context or Recommendations description: Provide any other context or recommendations here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062234
placeholder: Any other relevant information.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062235
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062236
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062237
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062238
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062239
name: Bug Report description: File a bug report for the repository title: "[BUG]: " labels: ["bug"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this bug report!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062240
type: textarea id: description attributes: label: Description description: | Describe the bug in detail placeholder: | Expected Behavior vs.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062241
Actual Behavior: validations: required: true - type: textarea id: component attributes: label: Component description: Which component (Tool/Template/Extension) is showing the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062242
placeholder: "e.g., Kit Base Editor Template / repo launch tool / Kit SDK" - type: textarea id: system-details attributes: label: System Details description: | Provide details about your system placeholder: | OS / CPU / GPU / GPU Driver Version validations: required: true - type: textarea id: reproduction-steps attributes: label: Reproduction Steps description: What are the steps to reproduce the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062243
validations: required: true - type: textarea id: logs attributes: label: Logs description: | Include the relevant log files: - **repo.log:** Found in `_repo/repo.log` if the issue is with tooling.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062244
kit.log:** Found in `_build/{OS}/release/logs/.../kit_{...}log` if the issue is with App, Extension, or Kit SDK.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062245
placeholder: Paste the log content here or attach the log files.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062246
type: textarea id: additional-context attributes: label: Additional Context description: Provide any other context or information here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062247
placeholder: Any other information that might be helpful
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 062248
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062249
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062250
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062251
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062252
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062253
Select the desired UI based application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062254
The developer bundle is not currently suitable for headless services.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062255
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062256
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062257
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062258
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062259
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062260
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062261
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062262
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062263
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062264
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062265
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062266
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062267
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062268
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 062269
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062270
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062271
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062272
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062273
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062274
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062275
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062276
What Are Application Layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062277
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062278
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062279
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062280
``` Answer `yes` to enable streaming for your application.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062281
You can then pick from the following streaming layers: ```bash ?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062282
Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062283
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming [ ] [omni_gdn_streaming]: GDN Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062284
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062285
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062286
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062287
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062288
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062289
GDN Streaming:** Streams applications through NVIDIA Graphics Delivery Network; especially useful for configurator workflows.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062290
Refer to the [End-to-End Configurator Example Guide]( for deployment instructions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062291
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062292
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062293
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062294
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062295
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062296
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062297
GDN Streaming** Refer to the [End-to-End Configurator Example Guide]( for instructions on packaging and deploying to NVIDIA GDN.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062298
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 062299
Usage and Troubleshooting This section provides high-level information and guidance related to using the Kit App Template repository, along with troubleshooting tips for common issues.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062300
Usage Information ### A Project per Repository The `build` and `package` tooling provided in this repository is designed to capture all code and assets contained within the `/source` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062301
Each time the `template new` command is executed, a new application or extension is created within `/source`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062302
For purposes of experimentation and initial development, housing all working assets within the `/source` directory is reasonable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062303
However, as the project matures or requires deployment, it is recommended to segregate projects (typically a single `.kit` file and any required custom extensions) to minimize build times and reduce the size of the resultant package.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062304
Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is considered an extension.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062305
The `.kit` files that define applications are simply a convenient method to assemble and configure a set of extensions for specific functionalities, while extensions (and combinations thereof) can act as modular components fulfilling particular tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062306
For additional information on the Kit SDK and how to create applications and extensions, refer to the [Kit SDK Companion Tutorial]( ### Extendable Templates and Tools The templates and tools provided in this repository are designed to be extendable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062307
Templates Templates consist of a directory structure and boilerplate code containing variables configurable at the time the templates are applied.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062308
The `templates.toml` file, located in `templates/templates.toml`, specifies which templates the tooling recognizes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062309
Tooling Most tooling is not stored directly within the repository; it is instead downloaded from a remote registry upon the initial use of the tooling.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062310
This design allows the tooling to be updated independently of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062311
The framework used for the tooling also supports the definition of custom tools.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062312
To see this extensibility in action, explore the local tooling defined within `tools/repoman`, specifically the `launch` tool.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062313
Configuration for this tool within the repo is delineated in the `repo_tools.toml` file at the root of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062314
Troubleshooting This section outlines potential issues that may arise when using the Kit App Template repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062315
Setup & Configuration Issues #### Windows Long Path Due to path length limitations on Windows it is recommended to place repository artifacts in a location closer to the root of the drive.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062316
This will help avoid issues with the path lengths when building and packaging applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062317
exFAT Drive Compatibility Limitations The Kit App Template repository and associated tooling are designed to work with drive formats that support junctions/symlinks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062318
If you are using an exFAT-formatted drive, you may encounter errors during the build process.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062319
To resolve this issue, consider using a different drive format such as NTFS.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062320
Extension Naming Guidelines When creating custom extensions, avoid using a top-level namespace that is the same as any built-in Python module (e.g., “random”, “sys”, “xml”).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062321
Doing so can cause import conflicts if Omniverse Kit attempts to load extensions from these Python modules.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062322
For example, instead of “random.extension.name”, use a unique namespace such as “my_company.my_app.my_extension”.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062323
Rendering & Performance #### Initial Rendering Startup Times When launching an application that requires the RTX renderer, the first launch may take considerably longer than subsequent launches due to shader compilation.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062324
The initial launch can take between 5 to 8 minutes.** Subsequent launches of RTX-enabled applications will be faster as the renderer caches the compiled shaders.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062325
Build & Packaging #### Build Issues The `template new` tooling ensures that any created application is properly configured to build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062326
However, extensive manual changes can occasionally cause the configuration and `/source` directory contents to become unsynchronized.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062327
The specifics of any given build are determined by three main factors: 1) The state of the top-level `repo.toml` file, especially the `.kit` files listed in the `apps` array within the `[[repo_precache_exts]]` section.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062328
2) The state of the `premake5.lua` file, particularly which `.kit` files are set to build via `define_app()` (e.g., `define_app("my_company.my_service.kit")`).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062329
3) The state of the `source` directory, specifically which `.kit` files are present within `source/apps`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062330
To ensure a build proceeds as intended, verify that the same `.kit` files are listed or defined in all three locations.** For a clean build, use the command `./repo.sh build -c` or `.\repo.bat build -c` to clean the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062331
Caching and Persistent Data The Omniverse Kit SDK caches data and required dependencies to improve build and runtime performance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062332
If you encounter issues with stale, incorrect, or missing dependencies/data, consider clearing application specific and/or global cache locations: - **Application Specific Caches**: Clearing application specific caches and settings can be done by adding arguments at launch time.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062333
Linux: ```bash ./repo.sh launch -- --clear-cache --clear-data --reset-user ``` Windows: ```powershell .\repo.bat launch -- --clear-cache --clear-data --reset-user ``` Upon selecting a `.kit` file to launch, the application will clear the cache and data directories before starting.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062334
Global Cache Locations (:warning:Use with Caution:warning:)**: **IMPORTANT NOTE -** Clearing any of the following cache locations will require a full rebuild of any existing applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062335
Deleting the directories responsible for caching ensures a fresh build of the relevant caches during the next build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062336
Extension AND Application Data Cache Locations**: `$HOME/.local/share/ov` on Linux, `%LOCALAPPDATA%\ov` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062337
Tooling AND Dependency Cache Location**: - **Packman :** `$PM_PACKAGES_ROOT` on Linux, `%PM_PACKAGES_ROOT%` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062338
If `PM_PACKAGES_ROOT` is not set on your system, the default location will revert to `$HOME/.cache/packman` on Linux, `{drive where packman is launched from}\packman-repo` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062339
uv :** `$HOME/.cache/uv` on Linux, `%LOCALAPPDATA%\uv\cache` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062340
Space Constraints Due to Docker Artifacts When performing extensive local testing of container images created via `repo package_container`, Docker artifacts can accumulate over time, consuming significant disk space.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062341
`docker system df` can be used to determine disk space utilized by Docker objects.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062342
To reclaim space, consider the following options: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062343
Regular Safe Cleanup**: - **Command**: `docker container prune` - **Description**: This command removes all stopped containers, which is typically safe and helps manage disk space without affecting images, networks, or volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062344
Use**: Recommended for regular maintenance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062345
Extensive Cleanup (:warning:Use with Caution:warning:)**: - **Command**: `docker system prune` - **Description**: This command removes all unused containers, networks, images, and optionally volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062346
It is akin to running a `rm -rf` for Docker resources.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062347
Warning**: Use this command carefully, as it will remove many resources indiscriminately.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062348
Ensure you review and understand what will be deleted.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062349
For image-specific cleanup, use `docker images` to list all images and `docker rmi ` to manually remove those that are no longer needed.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 062350
Windows C++ Developer Configuration ## Introduction This document guides you through setting up this repository for C++ development on Windows using Microsoft Visual Studio and the Windows SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062351
For New Users:** If you are new to Windows C++ development, this guide provides a step-by-step installation of Visual Studio 2022 Community and the Windows SDK, ensuring you have all the components required for standard development tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062352
For Advanced Configurations:** If you already have Visual Studio and the Windows SDK installed but wish to specify exact versions, this guide will help you configure your environment using the `[repo_build.msbuild]` configuration within `repo.toml` at the project root.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062353
Configuration To enable the Windows C++ build process: - Set the `"platform:windows-x86_64".enabled` flag to `true` in your `repo.toml` file: ```toml [repo_build.build] "platform:windows-x86_64".enabled = true ``` - Set the `link_host_toolchain` flag to `true` in your `repo.toml` file: ```toml [repo_build.msbuild] link_host_toolchain = true ``` **Note:** If you already have Visual Studio and the Windows SDK installed, this might be the only change needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062354
The tooling will auto-detect installed components.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062355
Microsoft Visual Studio and Windows SDK Setup ### Basic Installation #### Installing Visual Studio 2022 Community 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062356
Download Visual Studio Installer** ![VS Download](../vs_download.png) - Visit the [Visual Studio Downloads]( - Click "Free download" under "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062357
Run the Installer** - Open the downloaded installer.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062358
Select "Community" edition and click "Install".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062359
Select Workloads** ![VS Workloads](../vs_workloads.png) - Check "Desktop development with C++".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062360
This includes tools like the MSVC compiler and C++ libraries.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062361
Additional Components** ![VS Additional](../vs_additional.png) - If you need specific components, go to "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062362
Select additional tools as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062363
Complete the Installation** - Proceed with the installation to download and set up all files.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062364
Installing Windows SDK (as needed) Usually, the Windows SDK is included with the "Desktop development with C++" workload.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062365
To verify or install it separately: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062366
Launch Visual Studio Installer** - Open the installer if it's not already running.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062367
Modify Installation** ![VS Modify](../vs_modify.png) - Click "Modify" on your Visual Studio installation.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062368
Verify Windows SDK** ![VS WinSDK Verify](../vs_winsdk_verify.png) - Ensure "Windows SDK" is selected under "Optional" sections or "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062369
Apply Changes** - Click "Modify" to install or update the SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062370
Configuring an Existing Installation #### Default Installation Paths If Visual Studio and the Windows SDK are installed in default locations, the build tooling will auto-detect them without additional configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062371
Note:** If the path entered is incorrect or invalid, the build system will fall back to auto-detection.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062372
Multiple Installations For multiple Visual Studio or Windows SDK installations, the latest version is used by default.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062373
If unspecified, default edition preference is "Enterprise", "Professional", "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062374
Additional Resources - [Repo Build Documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 062375
Data Collection & Use ## Overview NVIDIA Omniverse Kit Application Template collects anonymous usage data to help improve software performance and aid in diagnostic purposes.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 062376
Rest assured, no personal information such as user email, name or any other PII field is collected.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 062377
Purpose Omniverse Kit Application Template starts collecting data when you begin interaction with our provided software.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 062378
After creating an application with the `template new` tooling, go to the `source/apps` directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 062379
Locate the `.kit` file for the application you want to disable telemetry for.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 062380
Find the following section in the `.kit` file: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = true ``` 4.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 062381
Change `enableAnonymousData` to `false`: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = false ``` Disabling telemetry stops data collection from your application.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 062382
Kit SDK Tooling Guide This document provides an overview of the practical aspects of using the tooling provided in the `kit-app-template`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062383
Intended for users with a basic familiarity with command-line operations, this guide offers typical usage patterns and recommendations for effective tool use.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062384
For a complete list of options for a given tool, use the help command: `./repo.sh [tool] -h` or `.\repo.bat [tool] -h`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062385
Overview of Tools The `kit-app-template` repository includes several tools designed to streamline the development of applications and extensions within the Omniverse Kit SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062386
Available Tools - `template` - `build` - `launch` - `test` - `package` Each tool plays a specific role in the development workflow: ## Template Tool **Command:** `./repo.sh template` or `.\repo.bat template` ### Purpose The template tool facilitates the initiation of new projects by generating scaffolds for applications or extensions based on predefined templates located in `/templates/templates.toml`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062387
Usage The template tool has three main commands: `list`, `new`, `replay`, `modify`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062388
`list` Lists available templates without initiating the configuration wizard.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062389
Linux:** ```bash ./repo.sh template list ``` **Windows:** ```powershell .\repo.bat template list ``` #### `new` Creates new applications or extensions from templates with interactive prompts guiding you through various configuration choices.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062390
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` #### `replay` In cases where automation is required for CI pipelines or other scripted workflows, it is possible to record and replay the `template new` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062391
Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the Application `.kit` file you want to update.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062392
Next, select (using Space) the Template Layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062393
After the operation completes, rebuild (`./repo.sh build` or `.\repo.bat build`) the project to pull in the new extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062394
What `template new` Modifies When creating applications, the template tool automatically updates build configuration files: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062395
`premake5.lua`** - Adds `define_app("appname.kit")` so the build system discovers your application 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062396
`repo.toml`** - Adds the app path to `repo_precache_exts.apps` so dependent extensions are pre-cached at build time 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062397
`source/rendered_template_metadata.json`** - Records which templates were rendered (enables `template modify` and `template list`) 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062398
Setup extension** (some templates) - Creates an extension in `source/extensions/` for application-specific initialization **Extensions** are automatically discovered by the Kit build system based on directory structure, so no build file modifications are needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062399
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062400
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062401
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062402
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062403
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062404
It includes all resources located in the `source/` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062405
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062406
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062407
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062408
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062409
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062410
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062411
`-p` or `--package`:** Launches a packaged application from a specified path.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062412
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062413
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062414
Any flags added after `--` will be passed through to Kit directly.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062415
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062416
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062417
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062418
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062419
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062420
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062421
Applications configurations (`.kit` files) are tested to ensure they can startup and shutdown without issue.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062422
However, the tests written within the extensions will dictate a majority of application functionality testing.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062423
Extension templates provided by the Kit App Template repository include sample tests which can be expanded upon to increase test coverage as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062424
Usage Always run a build before testing: **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ## Package Tool **Command:** `./repo.sh package` or `.\repo.bat package` ### Purpose This tool prepares your application for distribution or deployment by packaging it into a distributable format.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062425
Usage Always run a build before packaging to ensure the application is up-to-date: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` Additional launch options: - **`-n` or `--name`:** Specifies the package (or container image) name.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062426
Linux:** ```bash ./repo.sh package -n ``` **Windows:** ```powershell .\repo.bat package -n ``` - **`--thin`:** Creates a thin package that includes only custom extensions and configurations for required registry extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062427
Linux:** ```bash ./repo.sh package --thin ``` **Windows:** ```powershell .\repo.bat package --thin ``` :warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062428
The version is set within the `tools/VERSION.md` file.** ## Containerization Tool **Command:** `./repo.sh package_container` or `.\repo.bat package_container` ### Purpose The containerization tool provided by `repo_kit_tools` supports containerization of applications.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062429
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062430
How It Works The tool performs these steps: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062431
Creates a fat package** - Stages all dependencies into a temp directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062432
Trims unused extensions** - Removes disabled extensions to minimize image size 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062433
Splits into Docker layers** - Base layer (kit kernel + extscache) and app layer for faster rebuilds 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062434
Builds the container** - Uses a configurable base image (default: `nvcr.io/nvidia/omniverse/ov-base-ubuntu-22`) The container entrypoint supports runtime configuration via environment variables (`NVDA_KIT_ARGS`, `NVDA_KIT_NUCLEUS`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062435
Usage Always run a build before packaging to ensure the application is up-to-date: - **`package_container`:** Packages the application as a container image (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062436
When using the `package_container`, the user will be asked to select a `.kit` file to use within the entry point script for the container.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062437
This can also be specified without user interaction by passing it appropriate `.kit` file name via the `--app ${path_to_kit_file}` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062438
Linux:** ```bash ./repo.sh package_container ``` **Windows:** ```powershell .\repo.bat package_container ``` Additional command options: - **`--app`:** Specify the Kit app to containerize.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062439
One of defined in the config.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062440
Linux:** ```bash ./repo.sh package_container --app ${path_to_kit_file} ``` **Windows:** ```powershell .\repo.bat package_container --app ${path_to_kit_file} ``` - **`--image-tag`:** Optional image tag override to use for docker image.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062441
If includes ':', it will be used as is, e.g.: name:tag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062442
Linux:** ```bash ./repo.sh package_container --image-tag [container_image_name:container_image_tag] ``` **Windows:** ```powershell .\repo.bat package_container --image-tag [container_image_name:container_image_tag] ``` - **`-p` or `--from-package`:** Use package from 'kit-app-template/_build/packages/kit-app-template*.${config}.*' instead of a root folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062443
Linux:** ```bash ./repo.sh package_container -p ``` **Windows:** ```powershell .\repo.bat package_container -p ``` - **`-g` or `--generate`:** Generate default container template files into the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062444
Passed argument is the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062445
Linux:** ```bash ./repo.sh package_container -g ``` **Windows:** ```powershell .\repo.bat package_container -g ``` ## Additional Resources - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 062446
Configuring Kit App Template for DGXC Deployment This document covers Kit App Template specific configuration for deploying to NVIDIA DGX Cloud.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062447
For complete deployment instructions, see the [public DGXC documentation]( ## Streaming Layer Selection When creating your application with `./repo.sh template new`, select the appropriate streaming layer for DGXC: | Kit Version | Layer to Select | Generated File | |-------------|-----------------|----------------| | 108.x+ | `nvcf_streaming` | `{app_name}_nvcf.kit` | | 107.x | `ovc_streaming` | `{app_name}_ovc.kit` | | 106.x | `ovc_streaming` | `{app_name}_ovc.kit` | ### Selection Process 1.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062448
Run `./repo.sh template new` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062449
Select **Application** and your desired template 3.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062450
When prompted "Do you want to add application layers?", select **Yes** 4.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062451
`omni.cloud.open_stage`**: Provides Nucleus server connectivity for cloud deployments.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062452
[settings.exts."omni.kit.window.content_browser"] show_only_collections.6 = "" # Hides the "My Computer" connection from the content browser.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062453
``` ## Containerization After building (`./repo.sh build`), create a container: ```bash ./repo.sh package_container --image-tag myapp:v1.0 ``` When prompted, select the streaming `.kit` file (`*_ovc.kit` or `*_nvcf.kit`).
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062454
Next Steps For deployment to DGXC (container upload, NVCF function creation, portal registration), see: - [Containerization Guide]( - Building and packaging - [Deploying Kit Apps]( - NGC upload and NVCF deployment - [Troubleshooting]( - Common issues and FAQs ## Version-Specific Notes ### Kit 108.x+ (`main` branch) Select `nvcf_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062455
Streaming dependencies are automatically configured.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062456
Kit 107.x (`production/107.3` branch) Select `ovc_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062457
No manual edits required.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062458
Kit 106.x (`production/106.5` branch) The streaming layer may require manual edits.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062459
See the [public containerization guide]( for the "Replace Streaming Extension" section.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062460
Troubleshooting For deployment issues, log analysis, and common errors, see the [DGXC FAQs and Troubleshooting](
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 062461
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062462
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062463
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062464
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062465
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062466
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062467
Collaborating on large-scale design projects in real-time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062468
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062469
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062470
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062471
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062472
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062473
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062474
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062475
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062476
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062477
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062478
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062479
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062480
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062481
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062482
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062483
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062484
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062485
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062486
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062487
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062488
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062489
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062490
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062491
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062492
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062493
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062494
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062495
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062496
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062497
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062498
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062499
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062500
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062501
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062502
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062503
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062504
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062505
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062506
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062507
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062508
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062509
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062510
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062511
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062512
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062513
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062514
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062515
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062516
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062517
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062518
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062519
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062520
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062521
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062522
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062523
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062524
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062525
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062526
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062527
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062528
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062529
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062530
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062531
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062532
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062533
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062534
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062535
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062536
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062537
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062538
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062539
:warning: **Important**: These layers are not standalone application templates.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062540
They must be used in conjunction with a base application template.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062541
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062542
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062543
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062544
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062545
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062546
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062547
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062548
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062549
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062550
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062551
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062552
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062553
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062554
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062555
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062556
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062557
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062558
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062559
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062560
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062561
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062562
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062563
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062564
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062565
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062566
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062567
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062568
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062569
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062570
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062571
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062572
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062573
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062574
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062575
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062576
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062577
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062578
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062579
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062580
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062581
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062582
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062583
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062584
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062585
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062586
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062587
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062588
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062589
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062590
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062591
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062592
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062593
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062594
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062595
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062596
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062597
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062598
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062599
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062600
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062601
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062602
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062603
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062604
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062605
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062606
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062607
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062608
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062609
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062610
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062611
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062612
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062613
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062614
Start the Streaming Client Follow the [Quick Start instructions in the we
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062615
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062616
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062617
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062618
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062619
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062620
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062621
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062622
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062623
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062624
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062625
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062626
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062627
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062628
Subsequent extensions can be added to the .kit file manually.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062629
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062630
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062631
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062632
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062633
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062634
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062635
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062636
Setup Extension -> kit_service_setup* - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062637
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062638
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062639
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062640
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062641
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062642
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062643
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062644
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062645
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062646
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062647
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062648
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062649
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062650
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062651
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062652
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062653
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062654
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062655
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062656
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062657
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062658
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062659
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062660
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062661
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062662
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062663
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062664
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062665
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062666
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062667
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062668
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062669
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062670
The base application `.kit` file should be used for containerization.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062671
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062672
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062673
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062674
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062675
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062676
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062677
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062678
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062679
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062680
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062681
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062682
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062683
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062684
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062685
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062686
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062687
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062688
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062689
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062690
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062691
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062692
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062693
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062694
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062695
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062696
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062697
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062698
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062699
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062700
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062701
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062702
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062703
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062704
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062705
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062706
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062707
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062708
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062709
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062710
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062711
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062712
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062713
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062714
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062715
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062716
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062717
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062718
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062719
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062720
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062721
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062722
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062723
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062724
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062725
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062726
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062727
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062728
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062729
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062730
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062731
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062732
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062733
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062734
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062735
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062736
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062737
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062738
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062739
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062740
:warning: **Important:** Before proceeding with the cloning step, ensure that Git Large File Storage (Git LFS) is installed on your system.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062741
To verify this, run the following command in your terminal: ```bash git lfs --version ``` If the command returns a version number, Git LFS is installed correctly.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062742
If not, you will need to install Git LFS.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062743
You can download and install it from the official website [here]( #### Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062744
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062745
During Application configuration, you will be prompted for information about these extensions.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062746
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062747
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062748
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062749
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062750
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062751
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062752
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062753
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062754
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062755
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062756
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062757
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062758
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062759
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062760
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062761
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062762
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062763
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062764
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062765
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062766
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062767
The USD Viewer template includes sample assets for this purpose.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062768
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062769
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062770
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062771
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062772
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062773
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062774
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062775
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062776
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062777
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062778
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062779
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062780
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062781
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062782
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062783
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062784
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062785
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062786
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062787
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062788
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062789
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062790
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062791
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062792
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062793
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062794
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062795
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062796
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062797
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062798
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062799
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062800
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062801
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062802
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062803
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062804
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062805
Service Setup Extension Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Service Setup Extension Template is designed to facilitate the configuration and setup of a headless service that leverages the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062806
Though it is possible in this case, setup extensions are not typically intended to be used as a generic extension but as a specific component of a particular application.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062807
Use Cases This setup extension is well suited for: - Developers building headless services that require Kit SDK functionalities.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062808
Key Features - Sample ServiceAPIRouter setup.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062809
Sample endpoint to demonstrate interaction patterns within service Kit SDK and OpenUSD.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062810
Usage This extension is automatically created and configured when you generate a new service application using the [Service Application Template](../../apps/kit_service/README.md).
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062811
Additional Learning - [Omniverse Kit Service Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062812
Python UI Extension Template ## Overview The Python UI Extension Template offers a simple starting point for developers looking to build Python-based extensions with performant User Interfaces.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062813
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062814
Use Cases This template is ideal for developers looking to build: - UI based extensions that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062815
Key Features - A simple starter UI demonstrating how to build using the Omni UI framework.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062816
Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062817
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062818
Usage This section provides instructions for the setup and use of the Python UI Extension Template.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062819
Getting Started To get started with the Python UI Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062820
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062821
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062822
Select desired template with arrow keys ↑↓:**: Python UI Extension - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062823
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062824
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062825
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062826
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062827
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062828
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062829
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062830
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062831
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Omni UI Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062832
USD Explorer Setup Extension Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer Setup Extension Template is specifically designed to configure the USD Explorer Template application.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062833
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Explorer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062834
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Explorer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062835
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062836
Key Features - Custom configurations tailored to the USD Explorer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062837
Usage This extension is automatically created and configured when you generate a new application based on the [USD Explorer Template Application](../../apps/usd_explorer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062838
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062839
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062840
Basic C++ Extension Template ## Overview The Basic C++ Extension Template is a starting point for developers looking to build C++ based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062841
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062842
Note for Windows C++ Developers** : This template requires that Visual Studio is installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062843
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062844
For additional C++ configuration information [see here](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062845
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062846
Performance sensitive extensions that require the performance benefits of C++.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062847
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062848
Integrating with existing C++ libraries or codebases.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062849
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062850
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062851
Usage This section provides instructions for the setup and use of the Basic C++ Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062852
Getting Started To get started with the Basic C++ Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062853
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062854
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062855
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062856
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062857
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062858
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062859
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062860
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062861
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062862
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062863
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062864
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062865
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062866
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062867
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062868
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062869
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062870
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062871
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062872
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062873
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062874
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062875
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062876
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062877
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062878
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062879
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062880
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062881
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062882
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062883
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062884
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062885
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062886
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062887
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062888
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062889
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062890
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062891
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062892
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062893
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062894
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062895
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062896
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062897
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062898
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062899
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062900
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062901
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062902
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062903
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062904
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062905
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062906
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062907
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062908
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062909
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062910
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062911
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062912
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062913
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062914
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062915
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062916
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062917
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062918
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062919
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062920
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062921
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062922
Integrating other C++ or Python libraries as needed.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062923
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062924
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062925
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062926
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062927
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062928
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062929
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062930
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062931
Managing the state for selecting objects within the scene.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062932
Performing actions without traditional in-app UI and menus.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062933
Key Features - Remote communication with the Kit application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062934
Scene loading capabilities.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062935
State management for object selection within the USD Viewer.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062936
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062937
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062938
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062939
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062940
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062941
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062942
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062943
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062944
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062945
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062946
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062947
Changelog The format is based on [Keep a Changelog]( ## [0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062948
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062949
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062950
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062951
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062952
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062953
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062954
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062955
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062956
Args: object: The bound object to register.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062957
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062958
Args: object: The bound object to deregister.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062959
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062960
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062961
Return: The bound object if it exists, an empty object otherwise.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062962
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062963
Return: The id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062964
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062965
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062966
Return: The bound object that was created.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062967
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062968
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062969
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062970
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062971
Args: value_to_multiply: The value to multiply by.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062972
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062973
Return: The toggled bool value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062974
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062975
Args: value_to_append: The value to append.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062976
Return: The new string value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062977
)", py::arg("value_to_append")) /**/; } ```
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 062978
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062979
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062980
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062981
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062982
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 062983
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062984
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062985
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062986
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062987
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 062988
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062989
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062990
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062991
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062992
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062993
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062994
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062995
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062996
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062997
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062998
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 062999
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 063000
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।
