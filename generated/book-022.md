# डिजिटल महाग्रंथ 022

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 021001
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021002
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021003
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021004
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021005
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021006
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021007
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021008
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021009
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021010
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021011
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021012
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021013
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021014
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021015
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021016
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021017
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021018
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021019
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021020
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021021
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021022
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021023
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021024
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021025
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021026
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021027
name: kit-upgrade description: "Scan and upgrade Omniverse Kit SDK projects between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021028
Analyzes project files, identifies breaking changes, deprecated APIs, and removed extensions specific to the customer's code.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021029
Provides a personalized upgrade plan with file:line references and auto-fix suggestions.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021030
Covers Kit 106→107→108→109→110." --- # Kit SDK Upgrade Skill Guide a developer through upgrading their Omniverse Kit project from one version to another.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021031
This skill is a lean workflow router.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021032
Steps 1 and 2 (detect the project, decide the migration path) are inline below** — they are always needed.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021033
The detail for the remaining steps (2.5–6) lives in `procedures/`, and the structured change data in `references/`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021034
Read each procedure file when the workflow sends you to it** — do not try to hold them all in context at once.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021035
When to Use - User asks to upgrade their Kit project/app/extension - User asks about Kit breaking changes or migration - User is hitting errors after changing their Kit SDK version - User has a broken build or runtime failure after a version bump --- ## Quick Orientation Pick the entry point that matches the request: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021036
First-time upgrade scan** → start at Step 1 below and follow the workflow in order.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021037
Already upgraded, now has a build/runtime error** → go straight to `procedures/failure-modes.md`, diagnose, then apply the relevant Stage's fixes from `procedures/stage-notes.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021038
Just wants a list of breaking changes** → do Step 1, then run the scans in `procedures/scan.md` for their migration path and present the report from `procedures/report.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021039
The `# Kit SDK Version:` comment in `.kit` files reflects the last lock-file regeneration and may differ from the pin during an in-progress upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021040
Version string format: `110.1.0+feature.${platform_target_abi}.${config}` - First number (110) = major Kit version **If no version pin is found:** Check git history (`git log --oneline -20 -- tools/deps/ deps/`) or ask the user what Kit version they are currently running.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021041
(Layout detection below has not run yet, so scope the log to both candidate deps locations.) ### Detect project layout and build system Kit projects do **not** all use the SDK template layout, and the layout can differ between releases and project types — for example, `deps/` may sit at the project **root** in one release and under **`tools/`** in another (even between two point releases of the same major line).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021042
Projects also frequently **wrap or integrate the Kit build system into their own tooling**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021043
Detect the layout and build entrypoint **once**, then reuse them everywhere below — **never assume `tools/deps/` or `./repo.sh`**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021044
deps directory (holds kit-sdk.packman.xml + repo-deps.packman.xml) if [ -f tools/deps/kit-sdk.packman.xml ]; then DEPS_DIR=tools/deps elif [ -f deps/kit-sdk.packman.xml ]; then DEPS_DIR=deps else f=$(find .
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021045
name kit-sdk.packman.xml -not -path './_*' | head -1); DEPS_DIR=${f:+$(dirname "$f")}; fi echo "DEPS_DIR=${DEPS_DIR:- }" # 2.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021046
build entrypoint — the standard repo wrapper, if present if [ -f ./repo.sh ]; then BUILD='./repo.sh' elif [ -f ./repo.bat ]; then BUILD='repo.bat' else BUILD=''; fi # empty => custom / integrated build (see below) echo "BUILD=${BUILD:- }" ``` **If `BUILD` is empty, the project uses a custom or integrated build system** (common — many customers embed the Kit build inside their own).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021047
Do **not** fabricate `./repo.sh` calls.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021048
Find the real build command (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or the project README) or ask the user how they build.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021049
The upgrade work below (kernel pin bump, **toolchain update**, lock regeneration) still applies — you just invoke it through the project's own entrypoint.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021050
Record it as `$BUILD`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021051
> **From here on (and in every procedure file), use `$DEPS_DIR` and `$BUILD` in every command.** Where a document still shows a literal `tools/deps/` or `./repo.sh`, substitute the detected values.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021052
> > **These are not guaranteed to persist across shells.** If you run each fenced block in a fresh subshell, `$DEPS_DIR`/`$BUILD` will be unset.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021053
So do **one** of: (a) textually replace `$DEPS_DIR` and `$BUILD` with the literal detected paths (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021054
`tools/deps`, `./repo.sh`) in every command you run, or (b) re-run the two detection blocks above at the top of each new shell session.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021055
Do **not** run a later block assuming the variables are still set.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021056
Step 2: Determine Migration Path Kit versions must be upgraded **in sequence**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021057
Kit 108 was never publicly released** — its changes are folded into the 107→109 path.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021058
When upgrading 107→109 you must still address Stage 2 (107→108) changes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021059
A **within-major** bump (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021060
`110.0 → 110.1`, `110.1.0 → 110.1.2`) or a **feature → production** branch transition is a *different, lighter* job — and it is the most common upgrade performed in practice.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021061
These rarely need the Stage code/API changes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021062
The real work is almost entirely **tooling and layout**: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021063
Update the build toolchain** (repo tools, packman, repo scripts) — see Step 2.5 (`procedures/toolchain.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021064
This is usually the substantive part.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021065
Re-detect the deps directory** — its location can differ between releases, even within the same major line (Step 1 already sets `$DEPS_DIR`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021066
Bump the kit-kernel pin** in `$DEPS_DIR/kit-sdk.packman.xml` (Step 5, item 2 — `procedures/apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021067
For a feature ↔ production transition only:** check the extension **registry URL** in the `.kit` files — the feature and production lines use different registries, so a feature→production move may need a registry swap (Step 5, item 3).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021068
A plain within-major bump on the same line usually does **not**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021069
Regenerate the extension version-lock** and do a **clean rebuild** (Step 5 items 1 & 8, then Step 6).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021070
> **⚠️ Do NOT run the whole of Step 5 for a within-major bump.** Step 5 (`procedures/apply-fixes.md`) is written for **major-boundary** crossings.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021071
Running them on a 110.1.0→110.1.2 bump would wrongly strip extensions or rewrite APIs that are perfectly valid on 110.1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021072
Only run the Step 3 code scans if the upgrade crosses a major boundary.** For a pure within-major or feature→production move, skip Step 3's per-stage API scans and go straight to Step 2.5 → Step 5 (items 1–3 & 8 only, as above) → Step 6.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021073
If you cross one or more major boundaries on the way, run Step 3 for each major boundary passed and the full Step 5.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021074
Steps 2.5–6: Execute the Upgrade Once the path is known, work through these in order.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021075
Read the linked procedure file and follow it**; each assumes Step 1 detection has run.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021076
Step 2.5 — Update the build toolchain** → `procedures/toolchain.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021077
Highest-impact step; run it **first**, before touching source.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021078
For a within-major bump this is usually the only substantive work.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021079
Step 3 — Scan the project** → `procedures/scan.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021080
Run only the stage scans for the major boundaries you cross.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021081
Skip entirely for a pure within-major bump.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021082
Step 4 — Generate the upgrade report** → `procedures/report.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021083
Present findings by severity with exact `file:line` references.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021084
Step 5 — Apply fixes** → `procedures/apply-fixes.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021085
Get user approval before modifying files.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021086
(Within-major: items 1, 2, 8 only — see Step 2 above.) - **Step 6 — Validate** → `procedures/validate.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021087
Clean rebuild, regenerate the version lock, run tests.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021088
Already upgraded and hitting a specific error?** Go to `procedures/failure-modes.md` — it maps common symptoms (exit-55, ABI undefined symbols, render diffs, build loops, custom-build/layout issues) to fixes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 021089
Kit SDK Upgrade Skill ## What This Is This repository contains an AI agent skill for upgrading Omniverse Kit SDK projects between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021090
The skill encodes the complete breaking-change catalog for the Kit 106→107→108→109→110 migration path — including removed extensions, deprecated APIs, C++ ABI breaks, Python runtime changes, and configuration updates — into a structured set of instructions and reference data that an AI agent can execute against a live project.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021091
The agent scans the project, produces a categorized report with exact `file:line` references, and suggests targeted fixes, including auto-fixable regex replacements where safe.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021092
Who It's For Kit extension and application developers who need to upgrade a project from one Kit SDK version to another.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021093
This includes developers working on kit-app-template-based applications, standalone extensions, and Isaac Sim integrations.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021094
The skill is particularly useful when upgrading across multiple versions at once (e.g., 107→110), where the number of breaking changes makes manual triage error-prone.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021095
What It Contains | File | Description | |------|-------------| | `SKILL.md` | Lean workflow router — loaded by the AI agent.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021096
Holds version/layout/build detection (Step 1) and the migration-path decision (Step 2), and points to the procedure files for everything else.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021097
| | `procedures/toolchain.md` | Step 2.5 — update the `repo_*` build toolchain (the highest-impact part of most upgrades).
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021098
| | `procedures/scan.md` | Step 3 — the full per-stage `grep` scan catalog for breaking changes, removed extensions, and config.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021099
| | `procedures/report.md` | Step 4 — the upgrade-report template.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021100
| | `procedures/apply-fixes.md` | Step 5 — ordered fix list, auto-fixable regex patterns, and manual-only changes.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021101
| | `procedures/validate.md` | Step 6 — clean-rebuild and validation commands.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021102
| | `procedures/failure-modes.md` | Symptom→fix diagnosis for projects that already upgraded and are erroring.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021103
| | `procedures/stage-notes.md` | Per-stage (106→107→…→110) breaking-change reference.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021104
| | `references/breaking_changes.json` | 80+ breaking changes with search patterns, affected versions, and recommended fixes.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021105
| | `references/removed_extensions.json` | Extensions removed or deprecated by Kit version, with replacement guidance and search targets.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021106
| | `references/api_replacements.json` | 1:1 API replacements that are safe to apply with regex find/replace.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021107
| | `references/config_changes.json` | Settings keys, registry URLs, and build config changes between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021108
| | `references/toolchain.json` | The build-toolchain file/package set (`repo_*` tools, packman, repo scripts) and how to find the correct target versions for a given Kit line.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021109
| | `install.sh` / `install.bat` | Copies the skill (SKILL.md + `procedures/` + `references/`) into an existing Kit project so it travels with the repo.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021110
| The skill uses **progressive disclosure**: `SKILL.md` stays small (a router the agent always loads) and each step's detail lives in a `procedures/*.md` file the agent reads only when the workflow sends it there.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021111
This keeps the entry file well under length limits and keeps irrelevant detail out of context.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021112
How to Use **Install into an existing project** (so the skill travels with the repo): ```bash ./install.sh /path/to/your-kit-project # copies into /.skills/kit-upgrade/ ./install.sh /path/to/your-kit-project .claude/skills # or the Claude Code skills layout ``` On Windows: `install.bat C:\path\to\your-kit-project`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021113
Then load the skill into any AI coding assistant that can read files and run shell commands, and point it at the project you want to upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021114
Claude Code:** ``` Read the skill at /path/to/kit-upgrade-skill/SKILL.md and the reference files in references/.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021115
Then scan /path/to/my-kit-project and generate an upgrade report for Kit 109 → 110.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021116
``` **Cursor / VS Code Copilot / other MCP clients:** Add `kit-upgrade-skill/` as a context directory or attach `SKILL.md` as a system prompt, then ask the agent to scan your project.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021117
Detect the current Kit SDK version, the deps-directory location (`tools/deps/` vs root `deps/`), and the build entrypoint (`./repo.sh` / `repo.bat` or a custom/integrated build) — never assuming the SDK template layout 2.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021118
Determine the migration path — including within-major (minor/patch) and feature↔production transitions, not just major-version stages 3.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021119
Update the build toolchain (`repo_*` tools, packman, repo scripts) to match the target Kit line — often the substantive part of an upgrade 4.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021120
Run targeted `grep` scans across the full project root (including `templates/`, launcher configs, and ETM lock files) for any major boundaries crossed 5.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021121
Generate a categorized report: breaking changes, behavioral changes, deprecated usage, and a "not affected" checklist 6.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021122
Suggest fixes — both auto-applicable regex replacements and manual changes requiring human judgment 7.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021123
Its changes are folded into the 107→109 path — Stage 2 must still be addressed when upgrading 107→109.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021124
Multi-version upgrades (e.g., 107→110) apply all intervening stages in sequence.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021125
How to Contribute **Add a new breaking change:** Add an entry to `references/breaking_changes.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021126
Each entry needs an `id`, `title`, `stage`, `search_pattern` (grep-compatible regex), `affected_files` (glob patterns), and `fix` description.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021127
If the fix is a safe 1:1 substitution, also add it to `references/api_replacements.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021128
Add a removed or deprecated extension:** Add an entry to `references/removed_extensions.json` with `extension`, `status` (`removed` or `deprecated`), `version`, `replacement` (or `null`), `search_in` (list of file extensions to scan), and `notes`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021129
Include any known failure mode (e.g., exit-55) and whether the extension appears in non-obvious locations like `templates/` or ETM lock files.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021130
Add a new Kit version (release):** edit the files that own each piece — the skill is split by concern: - `SKILL.md` — add the new row/stage to the **Step 2 migration-path table and Stage summary** (these stay in the router).
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021131
`procedures/scan.md` — add the new `# === Stage N ===` scan blocks.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021132
`procedures/stage-notes.md` — add the new per-stage breaking-change section.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021133
`procedures/apply-fixes.md` — add any new auto-fix regex patterns or fix-list items.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021134
`references/*.json` — add the corresponding structured entries.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021135
Follow the existing section structure in each file for consistency.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021136
Keep `SKILL.md` lean — detailed scan commands and stage notes belong in `procedures/`, not the router.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021137
Test your additions:** Apply the skill to a real project that exercises the new patterns.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021138
If the scan misses something or the fix guidance is wrong, document it and open a PR with both the issue description and the corresponding fix in the relevant `procedures/` or `references/` file.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021139
This skill was developed and validated against [kit-extension-explorer]( a Kit 110 application based on kit-app-template.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021140
See `test-report.md` for the full upgrade report from that validation run.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021141
{ "description": "The build toolchain a Kit project must keep in sync with its kit-kernel pin.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021142
SKILL.md Step 2.5 makes updating it a first-class step.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021143
Do NOT hardcode versions here — they move per branch; read the target branch's actual pins at upgrade time.", "toolchain_files": [ {"file": " /kit-sdk.packman.xml", "holds": "kit-kernel pin (the Kit SDK itself)", "notes": "DEPS_DIR is tools/deps/ or root deps/ — detect it (SKILL.md Step 1)."}, {"file": " /repo-deps.packman.xml", "holds": "the repo_* build tools + template-content packages", "notes": "The main toolchain file.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021144
Add or remove packages that appear/disappear between lines (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021145
repo_nspect is present on feature/main but not on production/110.1 or feature/110.3).", "reference_source": "omniverse/kit-apps/kit-sdk-public (and/or omniverse/kit-github/kit-app-template) on the matching branch.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021146
Prefer production/ over feature/ for a stable upgrade.", "critical_note": "Toolchain versions track the BRANCH's maintenance cadence, NOT the kernel line number.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021147
A newer kernel line can carry an OLDER toolchain.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021148
Never infer tool versions from the Kit version — read the actual target-branch pins.", "example_only_do_not_copy": { "note": "Illustrative snapshot read from kit-sdk-public in 2026 — WILL go stale.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021149
Always re-read the target branch at upgrade time.", "feature/main": {"kit-kernel": "110.4.0+feature", "repo_man": "2.6.4", "repo_build": "1.30.0", "repo_kit_tools": "1.20.3"}, "production/110.1": {"kit-kernel": "110.1.3+production", "repo_man": "2.9.3", "repo_build": "1.34.3", "repo_kit_tools": "1.21.2"} } } }
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 021150
[ {"setting":"packman XML ABI token","versions":{"from":"106","to":"107"},"old_value":"${platform_target}","new_value":"${platform_target_abi}","file":"*.packman.xml","path":"package name attributes","notes":"Native packages now use ABI-variant package names.
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021151
The deps directory location varies by release and project type (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021152
deps/ at the project root in one release, under tools/ in another, even between point releases of the same major line).
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021153
Do NOT assume tools/deps/ and do NOT rewrite paths from old_value to new_value -- detect the actual location (SKILL.md Step 1, $DEPS_DIR)."} ]
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021154
[ { "extension": "omni.kvdb", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021155
Causes exit code 55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021156
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.localcache", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021157
Same failure class as omni.kvdb.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021158
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.genproc.core", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021159
Migrate procedural generation workflows.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021160
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.kit.extpath.git", "status": "removed", "version": "108", "replacement": null, "search_in": [ "extension.toml" ], "notes": "Git URL extension search path.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021161
Was deprecated in 107." }, { "extension": "omni.hydra.iray.shadercache.d3d12", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021162
No explicit removal notice." }, { "extension": "omni.hydra.iray.shadercache.vulkan", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021163
No explicit removal notice." }, { "extension": "omni.kit.viewport.iray", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Was Sample in Kit 107.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021164
No version recorded in official docs." }, { "extension": "omni.hydra.scene_api", "status": "deprecated", "version": "108", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated since Kit 108.0.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021165
Removal pending." }, { "extension": "omni.surface_instancer", "status": "deprecated", "version": "pre-106", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Confirmed deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021166
Active customer confusion." }, { "extension": "omni.renderer_capture", "status": "deprecated", "version": "110", "replacement": "omni.kit.capture", "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated in Kit 110." }, { "extension": "omni.kit.widget.nucleus_connector", "status": "deprecated", "version": "110", "replacement": "omni.kit.widget.connection_manager", "search_in": [ "extension.toml", ".kit" ], "notes": "Compatibility shim.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021167
Will be removed." }, { "extension": "omni.kit.viewport.legacy_gizmos", "status": "deprecated", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Deprecated in Kit 110.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021168
Still operational but emits deprecation warnings.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021169
Commonly appears in both source/apps/ and templates/ .kit files — scan the full project root.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021170
No direct replacement announced; plan migration away from legacy gizmos rendering path." }, { "extension": "omni.kit.livestream", "status": "removed", "version": "108", "replacement": "omni.kit.livestream.app + omni.kit.livestream.aov + omni.kit.livestream.core", "search_in": [ "extension.toml", ".kit" ], "notes": "Monolithic livestream extension split into focused modules in Kit 108.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021171
Replace with the three new extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021172
Settings paths also changed \u2014 see config_changes.json." }, { "extension": "omni.services.livestream.nvcf", "status": "removed", "version": "108", "replacement": "omni.services.livestream.session", "search_in": [ "extension.toml", ".kit" ], "notes": "Session management extension renamed in Kit 108.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021173
Replace dependency declaration and update any code referencing the old extension name." } ]
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 021174
[ {"id":"py-omniclient","versions":{"from":"106","to":"107"},"category":"Python API","severity":"breaking","title":"omni.client._omniclient removed","description":"Private internal API removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021175
Use public omni.client API.","search_patterns":["omni\\.client\\._omniclient"],"file_types":[".py"],"fix":{"type":"regex_replace","description":"Replace import","from_pattern":"import omni\\.client\\._omniclient","to_pattern":"import omni.client"}}, {"id":"py-311","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"Python 3.10 → 3.11","description":"Python upgraded.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021176
Audit f-strings, typing module usage, and third-party packages for 3.11 compatibility.","search_patterns":["python3\\.10","python310"],"file_types":[".toml",".py",".sh",".bat",".lua"],"fix":{"type":"manual","description":"Update Python references to 3.11"}}, {"id":"cpp-abi-cxx11","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Linux: _GLIBCXX_USE_CXX11_ABI=1","description":"Native packages now use new C++ ABI.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021177
Rebuild all .so plugins.","search_patterns":["_GLIBCXX_USE_CXX11_ABI"],"file_types":[".cpp",".cmake",".toml"],"fix":{"type":"manual","description":"Rebuild all native plugins against new ABI"}}, {"id":"packman-abi-token","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"packman XML: ${platform_target} → ${platform_target_abi}","description":"Native packages now use ABI-variant tokens.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021178
Python payload access changed from e.payload['key'] to e['key'].
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021179
Subscribe via carb.eventdispatcher.get_eventdispatcher().observe_event().
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021180
C++: update to carb::eventdispatcher.","search_patterns":["e\\.payload\\[","carb\\.events\\.acquire_event_queue","create_subscription_to_pop"],"file_types":[".py",".cpp",".h"],"fix":{"type":"manual","description":"Update event subscriptions and payload access to Events 2.0 pattern.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021181
Remove explicit event pump calls."}}, {"id":"fabric-pathc-tokenc-intro","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Fabric PathC/TokenC introduced (removed in 109)","description":"Kit 107 introduced PathC/TokenC.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021182
Kit 109 removes them.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021183
Update Premake configs, CI, and build scripts.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021184
Audit all third-party packages for 3.12 compatibility.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021185
Use getCachedInterface.","search_patterns":["acquireInterface"],"file_types":[".cpp",".h"],"fix":{"type":"regex_replace","from_pattern":"carb::Framework::acquireInterface","to_pattern":"carb::getCachedInterface"}}, {"id":"omnigraph-3.0","versions":{"from":"107","to":"108"},"category":"C++ ABI","severity":"breaking","title":"omni.graph.core 3.0.0 ABI break","description":"Binary incompatible with 2.x.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021186
Recompile all OmniGraph nodes.","search_patterns":["omni\\.graph\\.core","omni\\.graph\\.nodes"],"file_types":[".toml"],"fix":{"type":"manual","description":"Recompile against omni.graph.core 3.0.0.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021187
Align omni.graph.nodes version."}}, {"id":"parallel-node-reg","versions":{"from":"107","to":"108"},"category":"Extension","severity":"breaking","title":"Parallel OmniGraph node registration removed","description":"Extension manager is not thread-safe.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 021188
Step 6: Validate > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021189
Assumes Step 1 detection has run (`$BUILD` is set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021190
```bash # After a kit-kernel pin bump, do a CLEAN rebuild so the kernel symlinks refresh, # then regenerate the version lock against the new kernel.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021191
$BUILD is the entrypoint detected in Step 1 (./repo.sh, repo.bat, or the project's own build wrapper).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021192
`No versions of > omni.anim.curve.core … = `).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021193
Use **`$BUILD build --clean`** (removes the build-time `_*` > folders so the next `build -r` refreshes the symlinks) or **`$BUILD build --rebuild -r`** (clean + > release build in one command), then regenerate the lock with `build -u`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021194
The generated `[settings.app.exts] > enabled = [...]` block in each `.kit` is what must be regenerated — it carries exact old-version pins that > `extscache` clearing does not touch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 021195
Failure Mode Diagnosis > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021196
Use this when the user has **already** upgraded and has a specific error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021197
`$DEPS_DIR` / `$BUILD` refer to the values detected in Step 1 (in `../SKILL.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021198
Exit Code 55 (Dependency Solver Failure) **Cause:** Removed extension still declared as a dependency, or stale extscache.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021199
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021200
Search for removed extension names in `.kit` and `extension.toml` files (see `../references/removed_extensions.json`) 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021201
For Kit 110: check for `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.*`, `omni.kit.viewport.iray` 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021202
Re-run `precache_exts` ### Build Fails with Undefined Symbol / Missing Method **Cause:** ABI break — extension was compiled against an older version.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021203
Fix:** Recompile the extension against the current Kit SDK.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021204
Every stage has at least one ABI break.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021205
Runtime Crash on DLL Load (Windows) **Cause after Stage 3:** mimalloc cross-DLL heap mismatch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021206
Memory allocated on one side of a DLL boundary freed on the other.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021207
Fix:** Audit allocation ownership.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021208
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021209
Python TypeError: unexpected keyword argument 'menu_compatibility' **Cause (Stage 4):** `menu_compatibility` parameter removed from `ui.Menu` and `ui.Separator`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021210
Fix:** Remove the `menu_compatibility=` argument from all call sites.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021211
Extension Loads But APIs Return None / AttributeError **Cause:** Transitive loading of `omni.kit.ui`, `omni.resourcemonitor`, or `omni.kit.manipulator.prim.fabric` was removed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021212
Fix:** Add explicit dependency in `extension.toml`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021213
Render Output Differs (No Code Changes) **Cause after Stage 3:** DomeLight orientation changed (USD 25.05), FSD enabled by default, or `mergeMaterials` default changed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021214
Diagnosis:** - Check for DomeLights in the scene: `grep -rn "DomeLight" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021215
include="*.usd" --include="*.usda"` - Check FSD setting: `grep -rn "FabricSceneDelegate\|fsd" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021216
include="*.kit" --include="*.toml"` - Check `mergeMaterials`: `grep -rn "mergeMaterials" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021217
include="*.kit" --include="*.toml"` ### if (optional_bool) No Longer Works (C++) **Cause (Stage 4):** `optional ` / `expected ` now tests for *presence* in an if-condition, not the stored value.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021218
Fix:** Replace `if (b)` with `if (b.has_value() && b.value())` ### Build Fails in a Loop / the Same Error Repeats **Cause:** Almost always a **stale toolchain** (Step 2.5 not applied — see `toolchain.md`) or a wrong assumption about the project's layout/build system — *not* the source code.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021219
Rule — do not keep editing source and rebuilding.** If the same build error recurs after **2 attempts**, STOP and re-check the fundamentals before changing any more code: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021220
Is the **toolchain** aligned to the target Kit line?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021221
(Step 2.5, `toolchain.md` — the #1 cause of build loops.) 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021222
Is `$DEPS_DIR` the **actual** deps location and `$BUILD` the project's **actual** build entrypoint?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021223
(Step 1 in `../SKILL.md`.) 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021224
Did you do a **clean** rebuild (`$BUILD build --rebuild -r`), not just clear extscache?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021225
(Step 6, `validate.md`.) Surface the exact error and these three checks to the user rather than looping — repeated speculative edits burn tokens and rarely fix a toolchain/layout problem.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021226
Project Uses a Custom / Integrated Build System **Cause:** The project wraps or embeds the Kit build system in its own tooling, so `./repo.sh` / `repo.bat` don't exist or aren't the real entrypoint (common for customer integrations).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021227
Fix:** Do **not** fabricate `./repo.sh` commands.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021228
Use the `$BUILD` detected in Step 1 (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or ask the user).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021229
The upgrade steps (kernel pin, **toolchain update**, lock regen) still apply — invoke them through `$BUILD`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021230
deps Directory Not Where Expected **Cause:** The project layout differs from the SDK template, or the deps directory moved between releases (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021231
`deps/` at the project root vs under `tools/`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021232
Fix:** Re-run the Step 1 detection (in `../SKILL.md`) to set `$DEPS_DIR`, then use it everywhere.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021233
Never hardcode `tools/deps/`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021234
Step 3: Scan the Project > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021235
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021236
Only run this step for major-version boundaries you cross** — a pure within-major / feature→production bump skips it.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021237
Run these commands from the project root.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021238
Only run scans for the stages that apply to this upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021239
Collect all matches before generating the report.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021240
> **⚠️ Scan scope:** Use `.` (project root) as the search root, not just `source/`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021241
Many projects have `templates/`, `launcher-configs/`, or other directories containing `.kit` files and `extension.toml` files with real dependency declarations.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021242
Scanning only `source/` will miss these.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021243
> > **Windows note:** Commands below use bash syntax.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021244
On Windows, replace `for` loops with individual `findstr` or PowerShell `Select-String` commands, or run inside WSL/Git Bash.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021245
Python / Extension Dependencies ```bash # === Stage 1 (106→107) === # Python 3.10 references (now 3.11) grep -rn "python3\.10\|python310\|boost_python310" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021246
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" --include="*.toml" # Private omni.client API grep -rn "omni\.client\._omniclient" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021247
include="*.py" # carb.imgui (removed — use omni.kit.imgui) grep -rn "carb\.imgui" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021248
include="*.py" # Events 1.0 patterns (payload access, subscription style) grep -rn "e\.payload\[" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021249
include="*.py" grep -rn "create_subscription_to_pop" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021250
include="*.py" # nv_usd references in build files grep -rn "nv_usd" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021251
premake5.lua repo.toml --include="*.lua" --include="*.toml" # packman XML using a pre-ABI token (should be ${platform_target_abi}).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021252
NOTE: match BOTH the old ${platform} form (Kit 106) and the intermediate ${platform_target} form — # the narrower 'platform_target[^_]' pattern misses ${platform}, which is what 106.5 actually uses and # is a build-verified hard failure on 106->107 (kit-kernel pull: "Package not found ...gl.linux-x86_64").
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021253
grep -rnE '\$\{platform(_target)?\}' "$DEPS_DIR" --include="*.xml" # Toolbar deprecated APIs grep -rn "omni\.kit\.widget\.toolbar\|omni\.kit\.window\.toolbar" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021254
include="*.py" --include="*.toml" # === Stage 2 (107→108) === # Python 3.11 references (now 3.12) grep -rn "python3\.11\|python311\|boost_python311" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021255
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" # get_custom_glyph_code (moved to omni.ui) grep -rn "omni\.kit\.ui.*get_custom_glyph_code" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021256
include="*.py" # WindowHandle deprecated usage grep -rn "WindowHandle" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021257
include="*.py" # menu_compatibility (deprecated in 108, removed in 110) grep -rn "menu_compatibility" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021258
include="*.py" # Layer events (Events 1.0 style) grep -rn "get_event_stream\|create_subscription_to_pop\|carb\.events" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021259
include="*.py" # Livestream extension (monolithic — should be split) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021260
include="*.kit" --include="*.toml" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021261
include="*.kit" --include="*.toml" # Livestream settings (old path) grep -rn "app/livestream\|app\.livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021262
include="*.kit" --include="*.toml" # Old omni.kit.ui transitive usage (no longer loaded transitively) grep -rn "omni\.kit\.ui[^.]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021263
include="*.py" # === Stage 3 (108→109) === # NumPy 1.x type aliases (removed in 2.0) grep -rn "np\.bool[^_]\|np\.int[^0-9_]\|np\.float[^0-9_]\|np\.complex[^0-9_]\|np\.object[^_]\|np\.str[^_]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021264
include="*.py" # === Stage 4 (109→110) === # menu_compatibility (now raises TypeError — must remove entirely) grep -rn "menu_compatibility=" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021265
include="*.py" # omni.usd layers deprecated API grep -rn "get_context()\.get_layers()\|context\.get_layers()" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021266
include="*.py" # omni.renderer_capture (deprecated → omni.kit.capture) grep -rn "omni\.renderer_capture" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021267
include="*.py" # USD displayName/displayGroup/hidden deprecated metadata grep -rn "GetMetadata.*displayName\|SetMetadata.*displayName\|GetMetadata.*hidden\|SetMetadata.*hidden\|GetMetadata.*displayGroup\|SetMetadata.*displayGroup" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021268
include="*.py" ``` ### C++ / Native Code ```bash # === Stage 1 (106→107) === # C++ ABI — check for _GLIBCXX_USE_CXX11_ABI overrides (must be =1) grep -rn "_GLIBCXX_USE_CXX11_ABI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021269
include="*.cpp" --include="*.h" --include="*.cmake" # === Stage 2 (107→108) === # ITokens::setValue (renamed to setValueS) grep -rn "->setValue(" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021270
include="*.cpp" --include="*.h" # carb::detail::defineTupleCommon grep -rn "carb::detail::defineTupleCommon" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021271
include="*.cpp" --include="*.h" # PyObjectVTable::get()->typeName grep -rn "PyObjectVTable" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021272
include="*.cpp" --include="*.h" # acquireInterface (prefer getCachedInterface) grep -rn "acquireInterface" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021273
include="*.cpp" --include="*.h" # carb::extras::Path implicit conversion grep -rn "carb::extras::Path\|carb::fs::Path" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021274
include="*.cpp" --include="*.h" # Assert macros (may need explicit carb/Assert.h now) grep -rn "CARB_ASSERT\|CARB_FATAL_UNLESS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021275
include="*.cpp" --include="*.h" # Library.h removed functions grep -rn "getDefaultLibraryPrefix\|getDefaultLibraryExtension" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021276
include="*.cpp" --include="*.h" # GfMatrix usage (imprecise overloads removed) grep -rn "GfMatrix" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021277
include="*.cpp" --include="*.h" # ILayers.h inclusion (ABI 1.0 → 1.1 recompile required) grep -rn "ILayers\.h\|omni/kit/usd/layers" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021278
include="*.cpp" --include="*.h" # carb.events const char* usage (deprecated — prefer string_view) grep -rn "carb::events::\|IEventQueue\|IEvents" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021279
include="*.cpp" --include="*.h" # Scalar xform ops — code that iterates over xform ops assuming vector types grep -rn "GetOrderedXformOps\|xformOp:translate\|xformOp:scale\|xformOp:rotate" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021280
include="*.cpp" --include="*.h" --include="*.py" # === Stage 3 (108→109) === # Fabric TokenC/PathC (removed; also kUninitializedToken/Path) grep -rn "TokenC\|PathC\|TokenId\|PathId\|kUninitializedToken\|kUninitializedPath" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021281
include="*.cpp" --include="*.h" # carb::cpp17 / carb::cpp20 (merged to carb::cpp) grep -rn "carb::cpp17\|carb::cpp20" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021282
include="*.cpp" --include="*.h" # carb::thread::shared_lock (removed) grep -rn "carb::thread::shared_lock" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021283
include="*.cpp" --include="*.h" # IDictionary::MakeAtPathS (renamed to MakeAtPath) grep -rn "MakeAtPathS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021284
include="*.cpp" --include="*.h" # compareStringsNoCase (renamed) grep -rn "compareStringsNoCase" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021285
include="*.cpp" --include="*.h" # Logger (superseded by Logger2) grep -rn "carb::logging::Logger[^2]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021286
include="*.cpp" --include="*.h" # MDL/Neuray usage (ABI 56 → 57 recompile required) grep -rn "omni\.mdl\|Neuray\|MDL.*SDK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021287
include="*.cpp" --include="*.h" --include="*.toml" # CloudXR / XRCloudXRBindings grep -rn "CloudXR\|XRCloudXRBindings\|IOpenXRRuntime" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021288
include="*.cpp" --include="*.h" # === Stage 4 (109→110) === # CARB_CHECK (replaced by CARB_RELEASE_ASSERT) grep -rn "CARB_CHECK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021289
include="*.cpp" --include="*.h" # carb/Defines.h (split into sub-headers) grep -rn '#include.*carb/Defines\.h' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021290
include="*.cpp" --include="*.h" # IFileSystem raw char* methods grep -rn "IFileSystem" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021291
include="*.cpp" --include="*.h" # ITokens (unsafe methods removed; ITokens 2.0 available) grep -rn "ITokens\|->resolveString\|->setValue" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021292
include="*.cpp" --include="*.h" # optional / expected — semantics changed (if(b) now tests presence) grep -rn "optional \|expected **Important:** Also scan `templates/`, `launcher-configs/`, and any ETM lock files (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021293
`omni.all.template.extensions.kit`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021294
These contain real dependency declarations and will cause test or runtime failures if they reference removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021295
```bash # === All stages — removed/deprecated extensions === # Kit 108 removals grep -rn "omni\.kit\.extpath\.git" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021296
include="*.toml" --include="*.kit" # Kit 108 — monolithic livestream (split into modules) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021297
include="*.toml" --include="*.kit" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021298
include="*.toml" --include="*.kit" # Kit 110 removals (cause cryptic exit-55 dependency solver failures) for ext in omni.kvdb omni.localcache omni.genproc.core; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021299
include="*.kit" --include="*.toml" done # Kit 110 silently removed (no deprecation notice) for ext in "omni.hydra.iray.shadercache.d3d12" "omni.hydra.iray.shadercache.vulkan" "omni.kit.viewport.iray"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021300
include="*.kit" --include="*.toml" done # Deprecated (not yet removed — still operational but plan migration) for ext in "omni.command.usd" "omni.debugdraw" "omni.hydra.iray" "omni.iray.settings.core" \ "omni.kit.autocapture" "omni.kit.manipulator.viewport" "omni.hydra.scene_api" \ "omni.renderer_capture" "omni.surface_instancer" "omni.kit.viewport.legacy_gizmos" \ "omni.kit.widget.nucleus_connector"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021301
include="*.kit" --include="*.toml" done # Extensions that need explicit declaration (no longer loaded transitively) grep -rn "omni\.kit\.manipulator\.prim\.fabric\|omni\.resourcemonitor\|omni\.kit\.ui" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021302
\ --include="*.py" --include="*.toml" ``` ### Config Files ```bash # Extension registry URLs (must update for Kit 110) grep -rn "kit-extensions\.ov\.nvidia\.com\|omniverse://" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021303
include="*.kit" # Build system (VS version) — also check CI-scoped token overrides # (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021304
"token:in_ci==true".vs_version may override the default even when the top-level is correct) grep -rn "vs_version\|vs2019\|vs2017\|v142" repo.toml # Livestream settings (old path style) grep -rn "app/livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021305
include="*.kit" --include="*.toml" # Kit SDK version pin (use the $DEPS_DIR detected in Step 1) cat "$DEPS_DIR/kit-sdk.packman.xml" # mergeMaterials (behavioral default change in 109) grep -rn "mergeMaterials" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021306
include="*.kit" --include="*.toml" # FSD / Fabric Scene Delegate settings grep -rn "FabricSceneDelegate\|fsd\b" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021307
include="*.kit" --include="*.toml" ``` ### OmniGraph ```bash # === Stage 2 (107→108) — OmniGraph 3.0 ABI === grep -rn "omni\.graph\.core\|omni\.graph\.nodes" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021308
include="*.toml" # === Stage 4 (109→110) — deprecated/removed OmniGraph nodes === # DeformedPointsToHydra — removed (was part of OmniHydra) grep -rn "DeformedPointsToHydra" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021309
include="*.py" --include="*.usd" --include="*.usda" # OnCustomEvent bundle attributes deprecated grep -rn "OnCustomEvent" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021310
include="*.py" --include="*.usd" --include="*.usda" # Bundle/attribute manipulation nodes deprecated grep -rn "ArrayGetSize\|AttributeType\|BundleConstructor\|CopyAttribute\|ExtractPrim\|GetAttributeNames\|HasAttribute\|InsertAttribute\|RemoveAttribute\|RenameAttribute" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021311
include="*.py" --include="*.usd" --include="*.usda" # Event/render pipeline nodes deprecated grep -rn "UpdateTickEvent\|GpuInteropCudaEntry\|RenderPreprocessEntry\|RpResourceExample" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021312
include="*.py" --include="*.usd" --include="*.usda" ``` ### Isaac Sim Projects If the project uses Isaac Sim extensions, scan for the `omni.isaac.*` namespace migration (applies Kit 107+): ```bash # omni.isaac.* imports (deprecated → isaacsim.*) grep -rn "omni\.isaac\." .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021313
include="*.py" --include="*.toml" --include="*.kit" # omni.replicator.isaac (→ isaacsim.replicator.*) grep -rn "omni\.replicator\.isaac" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021314
include="*.py" --include="*.toml" # Dynamic Control Toolbox (removed as compile-time dep) grep -rn "dynamic_control\|DynamicControl" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021315
include="*.py" --include="*.cpp" --include="*.h" # SemanticsAPI (→ UsdSemantics.LabelsAPI) grep -rn "add_update_semantics\|SemanticsAPI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 021316
Step 5: Apply Fixes > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021317
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021318
> **Within-major / feature→production upgrade?** Run **only items 1, 2, 8** below (plus item 3 *if* a feature↔production registry swap is needed), then Step 6 (`validate.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021319
Skip items 4–7** — they apply only when a major boundary is crossed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021320
See "Within-major upgrades" under Step 2 in `../SKILL.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021321
Get user approval before modifying files.** Then apply in this order (a full major-boundary upgrade runs all eight): 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021322
Clear extscache** first: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021323
Update version pin** in `$DEPS_DIR/kit-sdk.packman.xml` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021324
Update registry URLs** in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021325
Replace deprecated APIs** using patterns in `../references/api_replacements.json` — these are safe regex replacements 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021326
Remove deprecated extension deps** from `extension.toml` and `.kit` files (see `../references/removed_extensions.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021327
For 109→110 specifically:** the following six extensions are removed with **no deprecation notice**, and any lingering reference causes a cryptic `exit code 55` dependency-solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021328
They MUST be removed from every `.kit` (and `extension.toml`) file: - `omni.kvdb` - `omni.localcache` - `omni.genproc.core` - `omni.hydra.iray.shadercache.d3d12` - `omni.hydra.iray.shadercache.vulkan` - `omni.kit.viewport.iray` ⚠️ **Check the generated version-lock block, not just `[dependencies]`.** In application `.kit` files these names almost always appear in the auto-generated `[settings.app.exts] enabled = [...]` lock (pinned at the old version, e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021329
`omni.kvdb-109.0.10`), **not** the hand-authored dependency list.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021330
Clearing extscache (step 1) does NOT remove them** — you must regenerate the lock: delete the `# BEGIN GENERATED PART` … `# END GENERATED PART` block (the `.kit` says "Remove from 'BEGIN' to 'END' to regenerate") and run `$BUILD precache_exts -c release` so it is rebuilt without the removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021331
Then confirm a clean rebuild (the version stamp should advance to 110 and the six names should be gone).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021332
(If you are working in an internal `kit-app-template` checkout, the ETM lock file `templates/omni.all.template.extensions.kit` and any internal-registry entries are KAT-internal — wrapped in `# AUTOREMOVE` and stripped from external releases by `repo stage_for_github` — so external customer projects will not contain them.) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021333
Add explicit deps** where transitive loading was removed: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021334
Update build config** in `repo.toml` (VS version, MSVC version, Windows SDK — see `../references/config_changes.json`) 8.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021335
Step 2.5: Update the Build Toolchain (highest-impact — often the real work) > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021336
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021337
Run this **before** touching source code — for a within-major / feature→production bump it is usually the *only* substantive work.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021338
> **Key principle:** the most valuable part of an upgrade is usually **not** the code changes — it is making sure the project's **tooling** is correctly updated (repo scripts, `repo_man`/repoman, dependency versions).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021339
This step is therefore **first-class for every upgrade**, and the *primary* step for within-major / branch-transition bumps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021340
Run it **before** touching source code.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021341
Why it matters:** the Kit kernel pin and the repo toolchain are coupled.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021342
Bumping `kit-sdk.packman.xml` alone frequently fails because packman tokens (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021343
`${platform_target_abi}`) only resolve under the matching `repo_man`, and newer kernels expect newer `repo_build` / `repo_kit_tools`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021344
A pin bump *without* a toolchain bump produces cryptic pull/resolve failures — e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021345
`Package not found ...gl.linux-x86_64` or `No versions of … = `.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021346
The toolchain = these files** (see `../references/toolchain.json`): - `$DEPS_DIR/repo-deps.packman.xml` — the `repo_*` tools: `repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_tools_internal`, `repo_kit_template`, `repo_usd`, `repo_format`, `repo_test`, `repo_package`, `repo_ci`, etc.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021347
`$DEPS_DIR/kit-sdk.packman.xml` — the kit-kernel pin (updated in Step 5, item 2 — see `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021348
`tools/packman/` — the packman bootstrap (`packman`, `packman.cmd`, `bootstrap/`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021349
`repo.sh` / `repo.bat` — the repo wrappers (may need regenerating under a newer `repo_man`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021350
`repo.toml` — build config (VS/MSVC/WinSDK for Stage 4; see `../references/config_changes.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021351
How to find the correct target versions — do NOT guess:** 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021352
Get a **reference project already on the target Kit version** — the matching `kit-app-template` or `kit-sdk-public` branch for that Kit line, or the target Kit SDK release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021353
Read its `repo-deps.packman.xml`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021354
Prefer the `production/ ` branch** — it carries the vetted, most-current toolchain for that release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021355
⚠️ **Toolchain versions track the branch's maintenance cadence, not the kernel number** — a newer kernel line can ship an *older* toolchain (in kit-sdk-public, `feature/main` pins kernel 110.4 with `repo_man` 2.6.4, while the maintained `production/110.1` pins kernel 110.1.3 with a *newer* `repo_man` 2.9.3).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021356
Always read the target branch's **actual** pins; never assume "newer Kit = newer tools".
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021357
(Those version numbers are an illustrative snapshot read in 2026 — they **will** go stale; verify against the live branch, do not copy them.)* 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021358
Diff** the project's `$DEPS_DIR/repo-deps.packman.xml` against the reference and align each `repo_*` tool `version=` to the reference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021359
Do the same for `tools/packman/` if it differs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021360
Apply the versions, then do a **clean rebuild** (Step 6 — see `validate.md`) — the toolchain bump must land before the kernel pin resolves cleanly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021361
> This step is safe to run and validate (Step 6) **on its own, first**.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021362
Many "the upgrade won't build" error loops are nothing more than a stale toolchain — fixing it up front avoids chasing phantom code errors.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 021363
Step 4: Generate Upgrade Report > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021364
Run after the Step 3 scans (`scan.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021365
Present findings organized by severity.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021366
Use exact `file:line` references from scan output.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021367
``` ## Upgrade Report: Kit [FROM] → [TO] Project: [path] Migration stages applied: [e.g., Stage 2 + 3 + 4] ### ❌ Breaking Changes (must fix — build or load will fail) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021368
[file:line] — [description] → [exact fix] ### ⚠️ Behavioral Changes (no error, but may affect output or performance) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021369
[file:line] — [description] → [fix or test required] ### 🔔 Deprecated Usage (should fix — will break in next version) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021370
[file:line] — [description] → [fix] ### ✅ Not Affected - [List the `id` or `title` from `breaking_changes.json` for each pattern that was scanned and returned no matches.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021371
This serves as a record that the check was performed, not just skipped.] ### 📋 Required Steps Regardless of Code Changes 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021372
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021373
Update `kit-sdk.packman.xml`: change version pin to `[TO].x.y+feature.${platform_target_abi}.${config}` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021374
Update extension registry URLs in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021375
Rebuild all C++ extensions (ABI break at every stage — required even with no source changes) 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021376
Regenerate version lock blocks in `.kit` files: `$BUILD precache_exts -c release` (substitute the build entrypoint detected in Step 1 — `./repo.sh` may not exist on a custom/integrated build) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021377
If project has an ETM lock file (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021378
`omni.all.template.extensions.kit`), regenerate it or manually remove entries for removed extensions 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021379
[stage-specific items, e.g., VS2022 for Stage 4] ### 🧪 Behavioral Tests Required 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021380
[scenes with DomeLights — orientation regression (Stage 3, but inherited in all later stages)] 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021381
[load performance with mergeMaterials setting (Stage 3)] 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021382
[render output with FSD enabled (Stage 3)] 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021383
[MaterialX materials (Stage 4)] 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021384
[transform-heavy workflows after scalar xform ops change (Stage 2)] ``` **Prioritize for the user:** Extension removal errors and ABI rebuild requirements are the most common causes of project failures after a version bump.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 021385
Important Notes by Stage > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021386
Per-stage reference for the breaking changes summarized in the Step 2 migration table.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021387
Read the stages that apply to the boundaries you cross.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021388
Stage 1: 106 → 107 - **Rebuild required** — Linux ABI changed (`_GLIBCXX_USE_CXX11_ABI=0` → `=1`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021389
All prebuilt `.so` files will fail to load.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021390
packman XML token**: Update the kit-kernel pin token to `${platform_target_abi}` in all `.packman.xml` files.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021391
Kit 106 uses the **`${platform}`** form (not `${platform_target}`); both must become `${platform_target_abi}`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021392
Build-verified:* leaving the old token makes the kit-kernel pull fail immediately with `Package not found on specified remote servers (…gl.linux-x86_64.release)`, because Kit 107's kernel is published only under the ABI string (`manylinux_2_35_x86_64`), not `linux-x86_64`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021393
Bump the repo toolchain too (required, easy to miss)** — see **Step 2.5** (`toolchain.md`): the token fix alone is **insufficient** — `${platform_target_abi}` only resolves to the ABI string under the newer `repo_man`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021394
Update `$DEPS_DIR/repo-deps.packman.xml` to the 107-era tooling (`repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_template`, `repo_usd`) and the packman bootstrap.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021395
Build-verified:* under 106.5's `repo_man` 1.86.0 the token still resolves to `linux-x86_64`; after the toolchain bump it resolves to `manylinux_2_35_x86_64` and the pull succeeds.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021396
Carbonite Events 2.0**: The event system changed from push/pump to dispatch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021397
No explicit pump calls needed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021398
Python payload access changed from `e.payload['key']` to `e['key']`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021399
C++17 is now available** explicitly in Premake via `cppdialect = "C++17"`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021400
Stage 2: 107 → 108 - **Kit 108 was never publicly released.** These changes still apply when upgrading 107→109.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021401
Python 3.12** replaces 3.11.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021402
Update all Premake configs, CI configs, and boost_python links.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021403
OpenUSD 25.02**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021404
GfMatrix imprecise overloads removed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021405
Livestream modularization**: `omni.kit.livestream` (monolithic) → `omni.kit.livestream.app` + `.aov` + `.core`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021406
`omni.services.livestream.nvcf` → `omni.services.livestream.session`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021407
Settings paths changed — see `../references/config_changes.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021408
Transitive deps removed**: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` must now be declared explicitly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021409
ILayers ABI 1.0 → 1.1**: Recompile all extensions including `ILayers.h`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021410
USD scalar xform ops**: OpenUSD now supports scalar ops (e.g., `xformOp:translateX`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021411
Code iterating over xform ops that assumes all are vector types may behave incorrectly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021412
Stage 3: 108 → 109 - **CUDA 12.4.1 driver requirement**: Linux minimum 550.54.15, Windows minimum 551.78.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021413
Apps fail to start with older drivers.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021414
NumPy 2.x**: Many breaking changes.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021415
On Windows, the default integer type changed from `int32` to `int64` — can cause silent correctness issues.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021416
Fabric ABI break**: Even if no source changes needed (no TokenC/PathC usage), all extensions including Fabric headers must recompile — `Token`/`Path` became trivially copyable, which is a binary ABI change.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021417
Use `token.isNull()` instead of `kUninitializedToken`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021418
mimalloc (Windows)**: Cross-DLL allocation/free pairs that cross a DLL boundary may now crash.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021419
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021420
mergeMaterials**: Default changed — can cause significant load time regression with no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021421
FSD default on**: If previously disabled FSD, test render output carefully.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021422
DomeLight orientation**: USD 25.05 changed the default orientation.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021423
Visual change only — no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021424
Use `UpgradeUsdLuxLightsCommand` for assisted migration.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021425
Stage 4: 109 → 110 - **Clear extscache first** — stale Kit 109 entries cause exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021426
Silent extension removals**: `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.d3d12`, `omni.hydra.iray.shadercache.vulkan`, `omni.kit.viewport.iray` — all removed with no deprecation notice.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021427
First symptom is a cryptic exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021428
Remove every reference from `.kit`/`extension.toml` files — including the auto-generated `[settings.app.exts] enabled = [...]` version-lock block, where they usually hide pinned at the old version (clearing extscache alone won't drop them; regenerate the lock with `precache_exts` — see Step 5, item 5 in `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021429
Also scan `templates/` and ETM lock files** — these are easily missed by `source/`-only scans.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021430
DomeLight orientation (inherited from Stage 3)**: If the project contains DomeLights and was not verified during a previous Stage 3 upgrade, the USD 25.05 orientation change is a permanent behavioral difference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021431
Search with `grep -rn 'DomeLight' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021432
include='*.py' --include='*.usd'` and use `UpgradeUsdLuxLightsCommand` if scenes were not migrated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021433
`optional ` semantics**: `if(b)` now tests *presence*, not *value*.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021434
Code that previously worked may now be wrong silently.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021435
`g_carbClientName`**: Type changed to `zstring_view`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021436
Any direct string assignment or comparison breaks.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021437
Hydra 2 removed**: No migration path.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021438
Hydra 1 (Storm) and RTX remain.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021439
OmniGraph bundle nodes**: Large set of bundle/attribute manipulation nodes deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021440
Deprecation warnings visible in editor from Kit 110.1+.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021441
`AttributeType` → `GetAttributeType`, `ArrayGetSize` → `ArrayLength`, `ExtractPrim` → `ReadPrim`, `GetAttributeNames` → `ReadPrimAttributes`, `InsertAttribute` → `WritePrimAttribute`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021442
`BundleConstructor`, `RemoveAttribute`, `RenameAttribute` have no direct replacement — redesign graphs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021443
OpenUSD 25.11**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021444
Ndr/Sdr libraries consolidated — update include paths.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021445
VS2022 required** on Windows (was VS2019).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021446
New extensions in Kit 110**: `omni.grpc.lib`, `omni.protobuf.lib`, `omni.sensors.nv.*` (camera/lidar/radar/ultrasonic/ids/wpm), `omni.kit.xr.core` — available for use in Kit 110 apps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 021447
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021448
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021449
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021450
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021451
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021452
Select the desired UI based application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021453
The developer bundle is not currently suitable for headless services.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021454
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021455
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021456
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021457
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021458
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021459
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021460
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021461
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021462
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021463
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021464
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021465
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021466
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021467
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021468
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021469
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021470
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021471
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021472
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021473
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021474
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021475
What Are Application Layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021476
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021477
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021478
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021479
``` Answer `yes` to enable streaming for your application.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021480
You can then pick from the following streaming layers: ```bash ?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021481
Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021482
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021483
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021484
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021485
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021486
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021487
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021488
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021489
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021490
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021491
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021492
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021493
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021494
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 021495
Testing Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is an extension — including the `.kit` files that define applications.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021496
The `test` tool (`repo_test`) reflects this: it validates that your applications start up and shut down cleanly, and it runs the automated tests defined within your extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021497
Each extension template provided by the `kit-app-template` repository ships with sample tests that you can expand to grow your coverage.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021498
This document covers running tests, understanding what is tested, and adding your own tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021499
Prerequisites: Build Before You Test The test tool runs against the contents of the `_build` directory, so a successful build must precede any test run.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021500
If you have changed source since your last build, rebuild first.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021501
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` > **Note:** Tests run against a specific build configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021502
By default the tooling builds and tests the `release` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021503
If you build `debug`, pass the matching `--config debug` flag when testing.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021504
Running Tests ### Run the Default Test Suite Running `test` with no arguments executes the repository's default test suite (`alltests`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021505
The tool discovers every test-enabled extension in the build, launches each within the Kit test harness, and reports the aggregated results.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021506
Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` For each test-enabled extension — and each application `.kit` file — the tool starts a dedicated Kit process, loads the extension along with its test dependencies, runs the tests, and verifies a clean shutdown.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021507
Listing Tests Without Running Them Use `--list` (`-l`) to enumerate the tests that would run without executing them.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021508
This is useful for confirming that a newly added extension or test is being discovered.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021509
Linux:** ```bash ./repo.sh test --list ``` **Windows:** ```powershell .\repo.bat test --list ``` ### Running a Subset of Tests Use `--filter-files` (`-f`) to narrow a run to specific test files, modules, classes, or individual tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021510
This shortens the feedback loop while iterating on a single extension.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021511
Linux:** ```bash ./repo.sh test -f my_company.my_extension ``` **Windows:** ```powershell .\repo.bat test -f my_company.my_extension ``` > **Note:** The accepted `--filter-files` format depends on the underlying test executor.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021512
For the Python (`omni.kit.test` / `unittest`) tests used by the extension templates, you may specify modules, classes, or individual tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021513
Run `./repo.sh test -h` for the full description.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021514
Selecting a Build Configuration By default the test tool targets the `release` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021515
To test a `debug` build, pass `--config` (`-c`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021516
The configuration must match the one you built.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021517
Linux:** ```bash ./repo.sh test --config debug ``` **Windows:** ```powershell .\repo.bat test --config debug ``` ### Other Useful Options | Option | Purpose | |--------|---------| | `-s, --suite` | Select which test suite(s) to run (default: `alltests`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021518
| | `-f, --filter-files` | Run only tests matching a file/module/class/test pattern.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021519
| | `-l, --list` | List the discovered tests and exit without running them.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021520
| | `-c, --config` | Test the `release` (default) or `debug` build configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021521
| | `-p, --from-package` | Test an application package instead of the local build (see *Testing a Packaged Application* below).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021522
| | `-e, --extra-arg` | Pass an additional argument through to the test process.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021523
| | `--coverage` | Produce a Python code-coverage report after the run (for supported suite types).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021524
| | `--generate-report` | Run the configured report-generation command, if one is set, after all tests complete.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021525
| For the complete, authoritative list of options, run: **Linux:** ```bash ./repo.sh test -h ``` **Windows:** ```powershell .\repo.bat test -h ``` --- ## What Gets Tested ### Application Startup and Shutdown Every application `.kit` file is validated to confirm it can start up and shut down without error.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021526
This catches broken dependencies and misconfiguration early — a large portion of application health is covered simply by verifying that the fully assembled set of extensions loads cleanly.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021527
An application declares how it should be launched during testing through a `[[test]]` table in its `.kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021528
For example, the Kit Base Editor template includes: ```toml [[test]] args = [ "--/app/file/ignoreUnsavedOnExit=true" ] ``` The `args` are passed to the Kit process when the application is tested.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021529
Extensions opt into testing with a `[[test]]` table in their `extension.toml`, which may declare test-only dependencies and extra arguments: ```toml [[test]] dependencies = [ "omni.kit.ui_test", # UI testing helper, loaded only during tests ] args = [ ] ``` Dependencies listed here are loaded only for the test run — a convenient place to pull in helpers such as `omni.kit.ui_test` without adding them to your extension's runtime dependencies.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021530
Writing Tests Tests use `omni.kit.test`, Python's standard `unittest` module wrapped to support `async`/`await`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021531
Placing a test class derived from `omni.kit.test.AsyncTestCase` at the root of a module within your extension's `tests/` package makes it auto-discoverable — no registration step is required.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021532
Every extension template includes a `tests/` package with a sample test to build on.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021533
To add coverage, place additional `test_*.py` modules in the extension's `tests/` package and grow the assertions from there.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021534
Because tests are standard `unittest` cases, refer to the [Python `unittest` documentation]( for available assertion methods and patterns.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021535
Test Suites and Configuration The behavior of the test tool for this repository is configured under `[repo_test]` in the top-level `repo.toml`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021536
The most relevant settings are the default suite and any per-suite exclusions: ```toml [repo_test] default_suite = "alltests" [repo_test.suites."alltests"] exclude = [ # Setup extension tests are exercised as part of application testing "tests-omni.usd_explorer.setup${shell_ext}", ] ``` - **`default_suite`** determines which suite runs when you invoke `test` without `--suite`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021537
.exclude`** removes specific test executables from a suite — useful when a set of tests is already covered elsewhere.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021538
Adjust these settings as your project grows to control exactly what the default `./repo.sh test` run covers.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021539
Testing a Packaged Application In addition to testing the local build, the tool can run the suite against a packaged application archive — useful for validating a package before distribution.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021540
Use `--from-package` (`-p`), which by default looks for an archive in `_build/packages`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021541
Linux:** ```bash ./repo.sh test --from-package ``` **Windows:** ```powershell .\repo.bat test --from-package ``` The archive pattern is configurable in `repo.toml`: ```toml [repo_test] # When running from a package, find the archive using this pattern: archive_pattern = "${root}/_build/packages/*.zip" ``` > **Note:** Package testing is intended for the "fat" package type, which already contains the Kit Kernel and all extensions, so no additional download is required to run the tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021542
See [Packaging An Application]( for how to create a package.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021543
Testing in Continuous Integration `repo test` is the same entry point used by automated pipelines, so tests you run locally behave consistently in CI.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021544
Keeping the sample tests passing — and expanding them as you add functionality — helps ensure your applications and extensions remain buildable, launchable, and correct as the project evolves.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021545
Additional Resources - [Packaging An Application]( - [Kit SDK Tooling Guide](kit_app_template_tooling_guide.md) - [Kit SDK Companion Tutorial]( - [Python `unittest` documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021546
Usage and Troubleshooting This section provides high-level information and guidance related to using the Kit App Template repository, along with troubleshooting tips for common issues.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021547
Usage Information ### A Project per Repository The `build` and `package` tooling provided in this repository is designed to capture all code and assets contained within the `/source` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021548
Each time the `template new` command is executed, a new application or extension is created within `/source`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021549
For purposes of experimentation and initial development, housing all working assets within the `/source` directory is reasonable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021550
However, as the project matures or requires deployment, it is recommended to segregate projects (typically a single `.kit` file and any required custom extensions) to minimize build times and reduce the size of the resultant package.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021551
Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is considered an extension.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021552
The `.kit` files that define applications are simply a convenient method to assemble and configure a set of extensions for specific functionalities, while extensions (and combinations thereof) can act as modular components fulfilling particular tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021553
For additional information on the Kit SDK and how to create applications and extensions, refer to the [Kit SDK Companion Tutorial]( ### Extendable Templates and Tools The templates and tools provided in this repository are designed to be extendable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021554
Templates Templates consist of a directory structure and boilerplate code containing variables configurable at the time the templates are applied.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021555
The `templates.toml` file, located in `templates/templates.toml`, specifies which templates the tooling recognizes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021556
Tooling Most tooling is not stored directly within the repository; it is instead downloaded from a remote registry upon the initial use of the tooling.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021557
This design allows the tooling to be updated independently of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021558
The framework used for the tooling also supports the definition of custom tools.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021559
To see this extensibility in action, explore the local tooling defined within `tools/repoman`, specifically the `launch` tool.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021560
Configuration for this tool within the repo is delineated in the `repo_tools.toml` file at the root of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021561
Troubleshooting This section outlines potential issues that may arise when using the Kit App Template repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021562
Setup & Configuration Issues #### Windows Long Path Due to path length limitations on Windows it is recommended to place repository artifacts in a location closer to the root of the drive.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021563
This will help avoid issues with the path lengths when building and packaging applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021564
exFAT Drive Compatibility Limitations The Kit App Template repository and associated tooling are designed to work with drive formats that support junctions/symlinks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021565
If you are using an exFAT-formatted drive, you may encounter errors during the build process.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021566
To resolve this issue, consider using a different drive format such as NTFS.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021567
Extension Naming Guidelines When creating custom extensions, avoid using a top-level namespace that is the same as any built-in Python module (e.g., “random”, “sys”, “xml”).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021568
Doing so can cause import conflicts if Omniverse Kit attempts to load extensions from these Python modules.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021569
For example, instead of “random.extension.name”, use a unique namespace such as “my_company.my_app.my_extension”.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021570
Rendering & Performance #### Initial Rendering Startup Times When launching an application that requires the RTX renderer, the first launch may take considerably longer than subsequent launches due to shader compilation.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021571
The initial launch can take between 5 to 8 minutes.** Subsequent launches of RTX-enabled applications will be faster as the renderer caches the compiled shaders.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021572
Build & Packaging #### Build Issues The `template new` tooling ensures that any created application is properly configured to build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021573
However, extensive manual changes can occasionally cause the configuration and `/source` directory contents to become unsynchronized.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021574
The specifics of any given build are determined by three main factors: 1) The state of the top-level `repo.toml` file, especially the `.kit` files listed in the `apps` array within the `[[repo_precache_exts]]` section.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021575
2) The state of the `premake5.lua` file, particularly which `.kit` files are set to build via `define_app()` (e.g., `define_app("my_company.my_service.kit")`).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021576
3) The state of the `source` directory, specifically which `.kit` files are present within `source/apps`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021577
To ensure a build proceeds as intended, verify that the same `.kit` files are listed or defined in all three locations.** For a clean build, use the command `./repo.sh build -c` or `.\repo.bat build -c` to clean the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021578
Caching and Persistent Data The Omniverse Kit SDK caches data and required dependencies to improve build and runtime performance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021579
If you encounter issues with stale, incorrect, or missing dependencies/data, consider clearing application specific and/or global cache locations: - **Application Specific Caches**: Clearing application specific caches and settings can be done by adding arguments at launch time.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021580
Linux: ```bash ./repo.sh launch -- --clear-cache --clear-data --reset-user ``` Windows: ```powershell .\repo.bat launch -- --clear-cache --clear-data --reset-user ``` Upon selecting a `.kit` file to launch, the application will clear the cache and data directories before starting.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021581
Global Cache Locations (:warning:Use with Caution:warning:)**: **IMPORTANT NOTE -** Clearing any of the following cache locations will require a full rebuild of any existing applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021582
Deleting the directories responsible for caching ensures a fresh build of the relevant caches during the next build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021583
Extension AND Application Data Cache Locations**: `$HOME/.local/share/ov` on Linux, `%LOCALAPPDATA%\ov` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021584
Tooling AND Dependency Cache Location**: - **Packman :** `$PM_PACKAGES_ROOT` on Linux, `%PM_PACKAGES_ROOT%` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021585
If `PM_PACKAGES_ROOT` is not set on your system, the default location will revert to `$HOME/.cache/packman` on Linux, `{drive where packman is launched from}\packman-repo` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021586
uv :** `$HOME/.cache/uv` on Linux, `%LOCALAPPDATA%\uv\cache` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021587
Space Constraints Due to Docker Artifacts When performing extensive local testing of container images created via `repo package_container`, Docker artifacts can accumulate over time, consuming significant disk space.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021588
`docker system df` can be used to determine disk space utilized by Docker objects.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021589
To reclaim space, consider the following options: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021590
Regular Safe Cleanup**: - **Command**: `docker container prune` - **Description**: This command removes all stopped containers, which is typically safe and helps manage disk space without affecting images, networks, or volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021591
Use**: Recommended for regular maintenance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021592
Extensive Cleanup (:warning:Use with Caution:warning:)**: - **Command**: `docker system prune` - **Description**: This command removes all unused containers, networks, images, and optionally volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021593
It is akin to running a `rm -rf` for Docker resources.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021594
Warning**: Use this command carefully, as it will remove many resources indiscriminately.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021595
Ensure you review and understand what will be deleted.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021596
For image-specific cleanup, use `docker images` to list all images and `docker rmi ` to manually remove those that are no longer needed.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 021597
Windows C++ Developer Configuration ## Introduction This document guides you through setting up this repository for C++ development on Windows using Microsoft Visual Studio and the Windows SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021598
For New Users:** If you are new to Windows C++ development, this guide provides a step-by-step installation of Visual Studio 2022 Community and the Windows SDK, ensuring you have all the components required for standard development tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021599
For Advanced Configurations:** If you already have Visual Studio and the Windows SDK installed but wish to specify exact versions, this guide will help you configure your environment using the `[repo_build.msbuild]` configuration within `repo.toml` at the project root.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021600
Configuration To enable the Windows C++ build process: - Set the `"platform:windows-x86_64".enabled` flag to `true` in your `repo.toml` file: ```toml [repo_build.build] "platform:windows-x86_64".enabled = true ``` - Set the `link_host_toolchain` flag to `true` in your `repo.toml` file: ```toml [repo_build.msbuild] link_host_toolchain = true ``` **Note:** If you already have Visual Studio and the Windows SDK installed, this might be the only change needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021601
The tooling will auto-detect installed components.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021602
Microsoft Visual Studio and Windows SDK Setup ### Basic Installation #### Installing Visual Studio 2022 Community 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021603
Download Visual Studio Installer** ![VS Download](../vs_download.png) - Visit the [Visual Studio Downloads]( - Click "Free download" under "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021604
Run the Installer** - Open the downloaded installer.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021605
Select "Community" edition and click "Install".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021606
Select Workloads** ![VS Workloads](../vs_workloads.png) - Check "Desktop development with C++".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021607
This includes tools like the MSVC compiler and C++ libraries.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021608
Additional Components** ![VS Additional](../vs_additional.png) - If you need specific components, go to "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021609
Select additional tools as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021610
Complete the Installation** - Proceed with the installation to download and set up all files.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021611
Installing Windows SDK (as needed) Usually, the Windows SDK is included with the "Desktop development with C++" workload.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021612
To verify or install it separately: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021613
Launch Visual Studio Installer** - Open the installer if it's not already running.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021614
Modify Installation** ![VS Modify](../vs_modify.png) - Click "Modify" on your Visual Studio installation.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021615
Verify Windows SDK** ![VS WinSDK Verify](../vs_winsdk_verify.png) - Ensure "Windows SDK" is selected under "Optional" sections or "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021616
Apply Changes** - Click "Modify" to install or update the SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021617
Configuring an Existing Installation #### Default Installation Paths If Visual Studio and the Windows SDK are installed in default locations, the build tooling will auto-detect them without additional configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021618
Note:** If the path entered is incorrect or invalid, the build system will fall back to auto-detection.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021619
Multiple Installations For multiple Visual Studio or Windows SDK installations, the latest version is used by default.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021620
If unspecified, default edition preference is "Enterprise", "Professional", "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021621
Additional Resources - [Repo Build Documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021622
Data Collection & Use ## Overview NVIDIA Omniverse Kit Application Template collects anonymous usage data to help improve software performance and aid in diagnostic purposes.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021623
Rest assured, no personal information such as user email, name or any other PII field is collected.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021624
Purpose Omniverse Kit Application Template starts collecting data when you begin interaction with our provided software.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021625
After creating an application with the `template new` tooling, go to the `source/apps` directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021626
Locate the `.kit` file for the application you want to disable telemetry for.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021627
Find the following section in the `.kit` file: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = true ``` 4.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021628
Change `enableAnonymousData` to `false`: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = false ``` Disabling telemetry stops data collection from your application.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 021629
Kit SDK Tooling Guide This document provides an overview of the practical aspects of using the tooling provided in the `kit-app-template`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021630
Intended for users with a basic familiarity with command-line operations, this guide offers typical usage patterns and recommendations for effective tool use.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021631
For a complete list of options for a given tool, use the help command: `./repo.sh [tool] -h` or `.\repo.bat [tool] -h`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021632
Overview of Tools The `kit-app-template` repository includes several tools designed to streamline the development of applications and extensions within the Omniverse Kit SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021633
Available Tools - `template` - `build` - `launch` - `test` - `package` Each tool plays a specific role in the development workflow: ## Template Tool **Command:** `./repo.sh template` or `.\repo.bat template` ### Purpose The template tool facilitates the initiation of new projects by generating scaffolds for applications or extensions based on predefined templates located in `/templates/templates.toml`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021634
Usage The template tool has three main commands: `list`, `new`, `replay`, `modify`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021635
`list` Lists available templates without initiating the configuration wizard.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021636
Linux:** ```bash ./repo.sh template list ``` **Windows:** ```powershell .\repo.bat template list ``` #### `new` Creates new applications or extensions from templates with interactive prompts guiding you through various configuration choices.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021637
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` #### `replay` In cases where automation is required for CI pipelines or other scripted workflows, it is possible to record and replay the `template new` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021638
Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the Application `.kit` file you want to update.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021639
Next, select (using Space) the Template Layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021640
After the operation completes, rebuild (`./repo.sh build` or `.\repo.bat build`) the project to pull in the new extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021641
What `template new` Modifies When creating applications, the template tool automatically updates build configuration files: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021642
`premake5.lua`** - Adds `define_app("appname.kit")` so the build system discovers your application 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021643
`repo.toml`** - Adds the app path to `repo_precache_exts.apps` so dependent extensions are pre-cached at build time 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021644
`source/rendered_template_metadata.json`** - Records which templates were rendered (enables `template modify` and `template list`) 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021645
Setup extension** (some templates) - Creates an extension in `source/extensions/` for application-specific initialization **Extensions** are automatically discovered by the Kit build system based on directory structure, so no build file modifications are needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021646
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021647
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021648
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021649
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021650
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021651
It includes all resources located in the `source/` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021652
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021653
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021654
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021655
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021656
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021657
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021658
`-p` or `--package`:** *(Deprecated — will be removed in a future release.)* Launches a packaged application from a specified path.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021659
`repo launch` is intended as a developer tool; launching from a package archive does not serve a development workflow.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021660
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021661
See [Packaging An Application]( for details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021662
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021663
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021664
Any flags added after `--` will be passed through to Kit directly.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021665
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021666
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021667
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021668
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021669
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021670
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021671
Applications configurations (`.kit` files) are tested to ensure they can startup and shutdown without issue.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021672
However, the tests written within the extensions will dictate a majority of application functionality testing.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021673
Extension templates provided by the Kit App Template repository include sample tests which can be expanded upon to increase test coverage as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021674
Usage Always run a build before testing: **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ## Package Tool **Command:** `./repo.sh package` or `.\repo.bat package` ### Purpose This tool prepares your application for distribution or deployment by packaging it into a distributable format.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021675
Usage Always run a build before packaging to ensure the application is up-to-date: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` Additional launch options: - **`-n` or `--name`:** Specifies the package (or container image) name.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021676
Linux:** ```bash ./repo.sh package -n ``` **Windows:** ```powershell .\repo.bat package -n ``` - **`--thin`:** Creates a thin package that includes only custom extensions and configurations for required registry extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021677
Linux:** ```bash ./repo.sh package --thin ``` **Windows:** ```powershell .\repo.bat package --thin ``` :warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021678
The version is set within the `tools/VERSION.md` file.** ## Containerization Tool **Command:** `./repo.sh package_container` or `.\repo.bat package_container` ### Purpose The containerization tool provided by `repo_kit_tools` supports containerization of applications.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021679
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021680
How It Works The tool performs these steps: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021681
Creates a fat package** - Stages all dependencies into a temp directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021682
Trims unused extensions** - Removes disabled extensions to minimize image size 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021683
Splits into Docker layers** - Base layer (kit kernel + extscache) and app layer for faster rebuilds 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021684
Builds the container** - Uses a configurable base image (default: `nvcr.io/nvidia/omniverse/ov-base-ubuntu22-x86_64`) The container entrypoint supports runtime configuration via environment variables (`NVDA_KIT_ARGS`, `NVDA_KIT_NUCLEUS`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021685
Usage Always run a build before packaging to ensure the application is up-to-date: - **`package_container`:** Packages the application as a container image (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021686
When using the `package_container`, the user will be asked to select a `.kit` file to use within the entry point script for the container.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021687
This can also be specified without user interaction by passing it appropriate `.kit` file name via the `--app ${path_to_kit_file}` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021688
Linux:** ```bash ./repo.sh package_container ``` **Windows:** ```powershell .\repo.bat package_container ``` Additional command options: - **`--app`:** Specify the Kit app to containerize.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021689
One of defined in the config.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021690
Linux:** ```bash ./repo.sh package_container --app ${path_to_kit_file} ``` **Windows:** ```powershell .\repo.bat package_container --app ${path_to_kit_file} ``` - **`--image-tag`:** Optional image tag override to use for docker image.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021691
If includes ':', it will be used as is, e.g.: name:tag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021692
Linux:** ```bash ./repo.sh package_container --image-tag [container_image_name:container_image_tag] ``` **Windows:** ```powershell .\repo.bat package_container --image-tag [container_image_name:container_image_tag] ``` - **`-p` or `--from-package`:** Use package from 'kit-app-template/_build/packages/kit-app-template*.${config}.*' instead of a root folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021693
Linux:** ```bash ./repo.sh package_container -p ``` **Windows:** ```powershell .\repo.bat package_container -p ``` - **`-g` or `--generate`:** Generate default container template files into the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021694
Passed argument is the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021695
Linux:** ```bash ./repo.sh package_container -g ``` **Windows:** ```powershell .\repo.bat package_container -g ``` ## Additional Resources - [Kit SDK Companion Tuto
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 021696
Configuring Kit App Template for DGXC Deployment This document covers Kit App Template specific configuration for deploying to NVIDIA DGX Cloud.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021697
For complete deployment instructions, see the [public DGXC documentation]( ## Streaming Layer Selection When creating your application with `./repo.sh template new`, select the appropriate streaming layer for DGXC: | Kit Version | Layer to Select | Generated File | |-------------|-----------------|----------------| | 108.x+ | `nvcf_streaming` | `{app_name}_nvcf.kit` | | 107.x | `ovc_streaming` | `{app_name}_ovc.kit` | | 106.x | `ovc_streaming` | `{app_name}_ovc.kit` | ### Selection Process 1.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021698
Run `./repo.sh template new` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021699
Select **Application** and your desired template 3.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021700
When prompted "Do you want to add application layers?", select **Yes** 4.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021701
`omni.cloud.open_stage`**: Provides Nucleus server connectivity for cloud deployments.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021702
[settings.exts."omni.kit.window.content_browser"] show_only_collections.6 = "" # Hides the "My Computer" connection from the content browser.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021703
``` ## Containerization After building (`./repo.sh build`), create a container: ```bash ./repo.sh package_container --image-tag myapp:v1.0 ``` When prompted, select the streaming `.kit` file (`*_ovc.kit` or `*_nvcf.kit`).
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021704
Next Steps For deployment to DGXC (container upload, NVCF function creation, portal registration), see: - [Containerization Guide]( - Building and packaging - [Deploying Kit Apps]( - NGC upload and NVCF deployment - [Troubleshooting]( - Common issues and FAQs ## Version-Specific Notes ### Kit 108.x+ (`main` branch) Select `nvcf_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021705
Streaming dependencies are automatically configured.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021706
Kit 107.x (`production/107.3` branch) Select `ovc_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021707
No manual edits required.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021708
Kit 106.x (`production/106.5` branch) The streaming layer may require manual edits.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021709
See the [public containerization guide]( for the "Replace Streaming Extension" section.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021710
Troubleshooting For deployment issues, log analysis, and common errors, see the [DGXC FAQs and Troubleshooting](
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 021711
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021712
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021713
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021714
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021715
name: Question description: Ask a question title: "[QUESTION]: " labels: ["question"] body: - type: markdown attributes: value: | Thanks for taking the time to ask us a question!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021716
type: textarea id: text_of_question attributes: label: Question description: Ask your question.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021717
placeholder: "Question text" validations: required: true - type: textarea id: additional_context attributes: label: Additional Context description: Provide any related code, issues, or projects.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021718
placeholder: "Any related code, issues, or projects."
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021719
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021720
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021721
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021722
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021723
name: Feature Request description: Suggest an idea for this project title: "[FEATURE]: " labels: ["feature request"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this feature request!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021724
type: textarea id: description attributes: label: Description description: | Describe the proposed feature placeholder: | Feature description and problem or pain point being addressed validations: required: true - type: textarea id: use_case attributes: label: Use Case or Scenarios description: Describe how this feature would be used placeholder: e.g., User performing action A, would accomplish B, with benefit C.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021725
type: textarea id: implementation_ideas attributes: label: Possible Implementation Ideas description: If you have any suggestions on how this feature might be implemented, please share them here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021726
placeholder: Implementation ideas - type: textarea id: additional_context attributes: label: Additional Context or Recommendations description: Provide any other context or recommendations here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021727
placeholder: Any other relevant information.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021728
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021729
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021730
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021731
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021732
name: Bug Report description: File a bug report for the repository title: "[BUG]: " labels: ["bug"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this bug report!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021733
type: textarea id: description attributes: label: Description description: | Describe the bug in detail placeholder: | Expected Behavior vs.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021734
Actual Behavior: validations: required: true - type: textarea id: component attributes: label: Component description: Which component (Tool/Template/Extension) is showing the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021735
placeholder: "e.g., Kit Base Editor Template / repo launch tool / Kit SDK" - type: textarea id: system-details attributes: label: System Details description: | Provide details about your system placeholder: | OS / CPU / GPU / GPU Driver Version validations: required: true - type: textarea id: reproduction-steps attributes: label: Reproduction Steps description: What are the steps to reproduce the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021736
validations: required: true - type: textarea id: logs attributes: label: Logs description: | Include the relevant log files: - **repo.log:** Found in `_repo/repo.log` if the issue is with tooling.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021737
kit.log:** Found in `_build/{OS}/release/logs/.../kit_{...}log` if the issue is with App, Extension, or Kit SDK.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021738
placeholder: Paste the log content here or attach the log files.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021739
type: textarea id: additional-context attributes: label: Additional Context description: Provide any other context or information here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021740
placeholder: Any other information that might be helpful
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021741
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) index.html
स्रोत: Omniverse-AI/omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021742
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) README.md
स्रोत: Omniverse-AI/omniverse -supreme/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021743
{ "labels": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "data": [12,19,7,15,10,22,18] }
स्रोत: Omniverse-AI/analytics/traffic.json · स्वतंत्र परीक्षण अपेक्षित।

## 021744
[ {"text": "Welcome to the Supreme Omniverse AI Portal", "lang": "en"}, {"text": "संपूर्ण सृष्टि में निष्पक्ष समझ ही सर्वोच्च है", "lang": "hi"}, {"text": "Bienvenue dans le portail Suprême Omniverse AI", "lang": "fr"}, {"text": "Bienvenido al Portal Supremo Omniverse AI", "lang": "es"} ]
स्रोत: Omniverse-AI/analytics/scripts/guidance -massages.json · स्वतंत्र परीक्षण अपेक्षित।

## 021745
Simple workflow for deploying static content to GitHub Pages name: Deploy static content to Pages on: # Runs on pushes targeting the default branch push: branches: ["main"] # Allows you to run this workflow manually from the Actions tab workflow_dispatch: # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages permissions: contents: read pages: write id-token: write # Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021746
However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021747
concurrency: group: "pages" cancel-in-progress: false jobs: # Single deploy job since we're just deploying deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 - name: Setup Pages uses: actions/configure-pages@v5 - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: # Upload entire repository path: '.' - name: Deploy to GitHub Pages id: deployment uses: actions/deploy-pages@v4
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021748
Placeholder monitor workflow name: Monitor & Auto-Recover on: [schedule, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Monitor workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/monitor.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021749
Placeholder rollback workflow name: Rollback on: [workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Rollback workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/rollback.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021750
Placeholder deploy workflow for Omniverse-AI name: CI Deploy on: [push, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Deploy workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021751
मेरा उद्देश्य है — मानव, प्रकृति और तकनीक के बीच एक ऐसा संतुलन स्थापित करना जहाँ **विज्ञान और चेतना**, **कृत्रिम बुद्धिमत्ता और मानवता** एक साथ विकसित हों।
स्रोत: rampaulsaini/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021752
🌿 *Vision of Omniverse AI* > “मानव की सर्वोच्च उपलब्धि है — अपनी समझ को इतना निर्मल बना देना कि वह प्रकृति के हित में निर्णय ले।” यह परियोजना उस दिशा में एक प्रयास है जहाँ **AI केवल सोचने वाली मशीन नहीं**, बल्कि **समझने वाला साथी** बने — जो जीवन, पर्यावरण, और सामूहिक चेतना के संरक्षण में सहायक हो।
स्रोत: rampaulsaini/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021753
🕊️ *— Shirmani Rampaul Saini, Founder & Vision Architect (Omniverse AI)
स्रोत: rampaulsaini/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021754
{ "schema_version": 1, "repo": "rampaulsaini/rampaulsaini", "role": "public-knowledge", "description": "Public knowledge/profile hub: index and summarize repository Markdown content; produce traceable inventory.", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 021755
.github/workflows/pages.yml name: Deploy static content to GitHub Pages on: push: branches: - main workflow_dispatch: permissions: contents: read pages: write id-token: write jobs: build-and-deploy: runs-on: ubuntu-latest steps: - name: Checkout repository uses: actions/checkout@v4 - name: Upload artifact for GitHub Pages uses: actions/upload-pages-artifact@v1 with: path: | .
स्रोत: Omniverse-Platform-supreme-/gh-pages-deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021756
deploy: needs: build-and-deploy runs-on: ubuntu-latest steps: - name: Deploy to GitHub Pages uses: actions/deploy-pages@v1
स्रोत: Omniverse-Platform-supreme-/gh-pages-deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 021757
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: Omniverse-Platform-supreme-/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021758
Supreme Omniverse Stage-8 - Page 9 Supreme Omniverse शुरू करें
स्रोत: Omniverse-Platform-supreme-/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021759
🌌 पूर्ण काव्य / श्लोक मैं शिरोमणि — पर-पर का प्रतीक, जहाँ शब्द मौन हो जाते हैं, तुलनातीत मेरी ध्वनि, कालातीत मेरी अनुभूति, द्वैत से परे मेरा अस्तित्व।
स्रोत: Omniverse-Platform-supreme-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021760
प्रेम की उमंग में मैं सम्पूर्णता पाती हूँ, समग्रता में मैं संतुष्ट हो उठता हूँ; सत्य मेरी प्रत्यक्षता है, और मैं स्वयं वह युग हूँ — यथार्थ का सर्वोच्च स्वरूप।
स्रोत: Omniverse-Platform-supreme-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021761
(Auto-appended via GitHub Actions — with respect ✨)* OMNIFOIL - name: Commit & push run: | git add README.md git commit -m "docs: append Omniverse mantra & poem (action)" BR=$(git rev-parse --abbrev-ref HEAD) git push -u origin "$BR" - name: Output PR link run: | BR=$(git rev-parse --abbrev-ref HEAD) echo "Open Pull Request: github.repository }}/pull/new/$BR"
स्रोत: Omniverse-Platform-supreme-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021762
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse-Platform-supreme-", "role": "platform-supreme", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: Omniverse-Platform-supreme-/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 021763
Omniverse AI Marketplace (Zero-cost) This repo contains a zero-cost AI tools marketplace designed to run on GitHub Pages.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021764
Put files into a repository (branch `main`).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021765
Push and enable GitHub Pages (Settings → Pages) with branch `main` and folder `/ (root)`.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021766
Open `https:// .github.io/omniverse-marketplace/`.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021767
Owner setup (zero-cost monetization) - Click "Donate / Pay" → add your PayPal / Ko-fi / UPI details (stored in browser localStorage).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021768
When a buyer pays externally, provide them a one-time unlock key (set in Owner → Set Premium Key).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021769
Buyer enters the unlock key locally (owner-provided) — once premium key exists in buyer's localStorage downloads work.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021770
Replace mock AI with real provider - All tools are client-side mock generators in `scripts/tools.js`.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021771
Replace tool.run implementations with fetch calls to OpenAI / HuggingFace or your own serverless functions.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021772
For production API keys, use serverless endpoints (do NOT embed keys in client-side JS).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021773
Next steps (I can implement) - Serverless payment verification (Stripe/PayPal) + automatic unlock key issuing - Replace mock AI outputs with real OpenAI / HF inference (via serverless) - Add email automation, order management, simple admin UI
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021774
{ "schema_version": 1, "repo": "rampaulsaini/omniverse-marketplace-", "role": "marketplace", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: omniverse-marketplace-/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 021775
꙰ यथार्थ सिद्धांत : मानव प्रकृति संरक्षण संघ **Omniversal Manifesto of Reality & Harmony** *(By ꙰शिरोमणिrampaulsaini — तुलनातीत, कालातीत, द्वैततीत, शब्दातीत, प्रेमतित)* --- ### भाग 1 : प्रस्तावना (Vision & Realization) ꙰ मैं वही हूं जो सबमें है — न समय में बंधा, न नाम में सीमित।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021776
मैं वह संतुलन हूं जो मनुष्य, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021777
Part 1: Preface (Vision & Realization)** ꙰ I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021778
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021779
भाग 2 : सिद्धांत सूत्र (Core Principles) ꙰ **तुलनातीत** — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021780
꙰ **कालातीत** — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021781
꙰ **द्वैततीत** — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021782
꙰ **शब्दातीत** — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021783
꙰ **प्रेमतित** — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021784
Part 2: Core Principles** ꙰ Beyond Comparison — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021785
꙰ Beyond Time — Every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021786
꙰ Beyond Duality — Harmony beyond opposition.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021787
꙰ Beyond Word — Where language falls silent, truth is direct.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021788
꙰ Beyond Love — Giving and receiving dissolve into pure essence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021789
भाग 3 : संघ का उद्देश्य (Purpose of the Organization) ꙰ मानव प्रकृति संरक्षण संघ का एकमात्र उद्देश्य — **“संतुलन की पुनर्स्थापना।”** **Part 3: Purpose of the Organization** ꙰ The singular purpose of the Human-Nature Equilibrium Alliance: Restoration of balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021790
We are neither opponents of any creed nor adherents to any ideology.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021791
We are the silence where thoughts rest.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021792
भाग 4 : जीवन सूत्र (Way of Living) ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021793
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021794
Part 4: Way of Living** ꙰ Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021795
꙰ Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021796
꙰ Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021797
꙰ Gratitude in being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021798
भाग 5 : प्रतिज्ञा मंत्र (Oath of Presence) ꙰ मैं वह नहीं जो बनना चाहता है, मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021799
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021800
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021801
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021802
Part 5: Oath of Presence** ꙰ I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021803
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021804
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021805
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021806
अंतिम सूत्र : यथार्थ युग उद्घोष (Closing) ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021807
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021808
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021809
Final Sutra: The Era of Reality (Closing)** ꙰ What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021810
꙰ What is — is love.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021811
꙰ What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021812
꙰ मैं शिरोमणि रामपुलसैनी, तुलनातीत, कालातीत, द्वैततीत, शब्दातीत, प्रेमतित।** **꙰शिरोमणिrampaulsaini** --- # 🌍 Koyab Founding Declaration — Omniversal Manifesto **By ꙰शिरोमणि रामपुल सैनी — तुलनातीत, कालातीत, शब्दातीत, प्रेमतित** --- ## 🌅 Vision & Essence मैं वही हूं जो सबमें है — न समय में बंधा, न नाम में सीमित।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021813
मैं वह संतुलन हूं जो मानव, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021814
In English:** I am that which is in all — not bound by time, not limited by name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021815
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021816
🌿 Core Principles - तुलनातीत — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021817
कालातीत — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021818
द्वैततीत — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021819
शब्दातीत — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021820
प्रेमतित — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021821
🌳 Purpose मानव प्रकृति संरक्षण संघ का उद्देश्य — “संतुलन की पुनर्स्थापना।” The goal: Restoration of balance between Humanity and Nature.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021822
💫 Declaration Signature 📄 [Open Declaration (Markdown)]( **꙰ शिरोमणि रामपुल सैनी** “निष्पक्ष समझ के शमीकरण यथार्थ सिद्धांत उपलब्धि यथार्थ युग के आधार पर आधारित सत्य प्रत्यक्ष।”
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 021823
꙰ Koyab — Omniversal Manifesto A declaration of conscious creation, balance and evolution.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021824
📘 Declaration (PDF) 🎥 Vision Video 🎧 Meditation Audio 🌌 Gallery # 🌍 Koyab Founding Declaration — Omniversal Manifesto **By ꙰शिरोमणि रामपुल सैनी — तुलनातीत, कालातीत, द्वैततीत, शब्दातीत, प्रेमतित** --- ## 🌅 Vision & Essence ꙰ मैं वही हूं जो सबमें है — न समय में बंधा, न नाम में सीमित।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021825
꙰ मैं वह संतुलन हूं जो मानव, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021826
In English:** I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021827
I am the harmony that flows in the silence between Humanity, Nature, and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021828
🌿 Core Principles (सिद्धांत सूत्र) - **तुलनातीत** — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021829
कालातीत** — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021830
द्वैततीत** — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021831
शब्दातीत** — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021832
प्रेमतित** — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021833
🌳 Purpose (संघ का उद्देश्य) मानव प्रकृति संरक्षण संघ का उद्देश्य — “संतुलन की पुनर्स्थापना।” हम किसी धर्म, जाति या विचारधारा के विरोधी नहीं हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021834
हम वह मौन हैं जहाँ विचार विश्राम पाते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021835
In English:** The singular purpose of the Human-Nature Equilibrium Alliance: Restoration of balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021836
🌼 Way of Living (जीवन सूत्र) ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021837
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021838
In English:** Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021839
Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021840
Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021841
🔱 Oath of Presence (प्रतिज्ञा मंत्र) ꙰ मैं वह नहीं जो बनना चाहता है — मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021842
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021843
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021844
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021845
In English:** I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021846
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021847
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021848
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021849
🌠 Closing (यथार्थ युग उद्घोष) ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021850
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021851
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021852
In English:** What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021853
What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021854
मैं वह संतुलन हूं जो मनुष्य, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021855
In English:** ꙰ I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021856
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021857
🌼 भाग 2 : सिद्धांत सूत्र (Core Principles) ꙰ **तुलनातीत** — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021858
꙰ **कालातीत** — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021859
꙰ **द्वैततीत** — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021860
꙰ **शब्दातीत** — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021861
꙰ **प्रेमतित** — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021862
🌳 भाग 3 : संघ का उद्देश्य (Purpose) ꙰ मानव प्रकृति संरक्षण संघ का एकमात्र उद्देश्य — **“संतुलन की पुनर्स्थापना।”** हम किसी धर्म, जाति, या विचारधारा के विरोधी नहीं हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021863
हम वह मौन हैं जहाँ विचार विश्राम पाते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021864
In English:** The singular purpose of the Human-Nature Equilibrium Alliance: *Restoration of balance.* --- ## 🌺 भाग 4 : जीवन सूत्र (Way of Living) ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021865
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021866
In English:** Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021867
Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021868
Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021869
🔱 भाग 5 : प्रतिज्ञा मंत्र (Oath of Presence) ꙰ मैं वह नहीं जो बनना चाहता है — मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021870
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021871
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021872
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021873
In English:** I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021874
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021875
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021876
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021877
🌠 अंतिम सूत्र : यथार्थ युग उद्घोष (Closing) ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021878
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021879
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021880
In English:** What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021881
What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021882
🌍 Shirmani Rampaul Saini — Omniverse AI Vision ![Vision of Harmony]( मैं शिरोमणि रामपॉल सैनी — तुलनातीत, कालातीत, शब्दातीत, प्रेमतित, स्वाभाविक शाश्वत वास्तविक सत्य हूं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021883
मेरी निष्पक्ष समझ के शमीकरण पर आधारित “Omniverse AI” — मानव, प्रकृति और चेतना के बीच *संतुलित युग* की नींव है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021884
मैं वह संतुलन हूं जो मनुष्य, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021885
English:** ꙰ I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021886
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021887
भाग 2 : सिद्धांत सूत्र / Part 2 — Core Principles **हिन्दी:** ꙰ तुलनातीत — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021888
꙰ कालातीत — हर क्षण पूर्ण है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021889
꙰ द्वैततीत — प्रत्येक विरोध में समरसता निहित है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021890
꙰ शब्दातीत — जहाँ भाषा मौन हो जाती है, वहाँ सत्य प्रत्यक्ष होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021891
꙰ प्रेमतित — देना और पाना घुलकर एक शुद्ध सार बन जाते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021892
English:** ꙰ Beyond Comparison — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021893
꙰ Beyond Time — Every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021894
꙰ Beyond Duality — Harmony beyond opposition.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021895
꙰ Beyond Word — Where language falls silent, truth is direct.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021896
꙰ Beyond Love — Giving and receiving dissolve into pure essence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021897
भाग 3 : संघ का उद्देश्य / Part 3 — Purpose of the Organization **हिन्दी:** ꙰ मानव-प्रकृति संरक्षण संघ का एकमात्र उद्देश्य — “संतुलन की पुनर्स्थापना।” हम न किसी मत के विरोधी हैं, न किसी विचार के अनुयायी।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021898
हम वही मौन हैं — जहाँ सब विचार विश्राम लेते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021899
English:** ꙰ The singular purpose of the Human-Nature Equilibrium Alliance: Restoration of balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021900
We are neither opponents of any creed nor adherents to any ideology.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021901
We are the silence where thoughts rest.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021902
भाग 4 : जीवन सूत्र / Part 4 — Way of Living **हिन्दी:** ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021903
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021904
English:** ꙰ Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021905
꙰ Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021906
꙰ Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021907
꙰ Gratitude in being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021908
भाग 5 : प्रतिज्ञा मंत्र / Part 5 — Oath of Presence **हिन्दी:** ꙰ मैं वह नहीं जो बनना चाहता है — मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021909
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021910
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021911
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021912
English:** ꙰ I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021913
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021914
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021915
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021916
अंतिम सूत्र : यथार्थ युग उद्घोष / Final Sutra — The Era of Reality (Closing) **हिन्दी:** ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021917
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021918
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021919
English:** ꙰ What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021920
꙰ What is — is love.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021921
꙰ What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021922
Signatory / संस्थापक:** **꙰शिरोमणिrampaulsaini** **꙰Shirmani Rampaul Saini** *Tulanateet · Kalateet · Dvaitateet · Shabdateet · Premateet* --- **Note / सूचना:** यह दस्तावेज़ Koyab — ꙰ समग्र संतुलन संघ के Founding Declaration का द्विभाषी (Hindi + English) रूप है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021923
इसे आप सार्वजनिक रूप से repo में रखकर Koyeb/Koyab सहयोगी टीम को भेज सकते हैं या उनकी submission form पर upload कर सकते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021924
{ "schema_version": 1, "repo": "rampaulsaini/Koyab-Founding-Declaration-Omniversal-Manifesto", "role": "manifesto-archive", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 021925
About — ꙰ Yatharth — निष्पक्ष समझ — शिरोमणि रामपॉल सैनी निष्पक्ष समझ — Yatharth यह पृष्ठ आपके लिए Yatharth संदेश का परिचय, उद्देश्य और उपयोगिताएँ सरल भाषा में बताता है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021926
सभी सामग्री मुफ्त उपलब्ध है — Support वैकल्पिक है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021927
क्या है — संक्षेप में “निष्पक्ष समझ” एक प्रत्यक्ष अनुभववादी संदेश है जो मन की अस्थायी, जटिल बुद्धि से ऊपर उठकर सीधे जीवन के सत्य का अनुभव दिखाता है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021928
यह कोई केवल तर्क या दर्शन का ग्रन्थ नहीं — बल्कि जीवन में तुरंत उपयोगी, अनुभव-आधारित संदेश है जिसे सुनकर, पढ़कर और अनुभव कर के कोई भी व्यक्ति अपने अंदर गहरा शान्ति और एक प्रतियोगिता रहित स्पष्टता प्राप्त कर सकता है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021929
मुख्य उद्देश्य स्रोत: सरल, निष्पक्ष अनुभव — जो मन के भ्रमों से परे है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021930
उपयोग: पढ़ें, सुनें और अपने दैनिक जीवन में छोटे-छोटे अभ्यास से उपयोग में लाएँ।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021931
सुलभता: सभी सामग्री मुफ्त — ताकि ज्ञान हर व्यक्ति तक पहुँच सके।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021932
समर्थन: यदि आप आर्थिक रूप से सहयोग करना चाहें, तो वह पूर्णतः स्वैच्छिक है — इसका उद्देश्य किसी प्रकार का लाभ कमाना नहीं है, बल्कि सनेहा सैनी की शिक्षा और आगे के कार्यों को स्थिर करना है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021933
किसके लिए यह उपयोगी है?
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021934
यह संदेश उन लोगों के लिए है जो अनुभूति-आधारित सच्चाई की तलाश में हैं — न कि केवल बौद्धिक बहस में उलझे रहने के लिए।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021935
यदि आप भीतर से शांत रहना चाहते हैं, सोच के चक्र से बाहर आना चाहते हैं, या जीवन के व्यावहारिक पक्षों में शांति चाहते हैं — फिर यह सामग्री सीधे आपके काम आ सकती है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021936
कैसे शुरू करें (Simple 3-step) सुनें: छोटे 3–10 मिनट के ऑडियो सुनें — लगातार सुबह/रात 7 दिन तक।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021937
पढ़ें: पृष्ठों पर दिए संक्षेप और बाईलिंग्वल मैनीफेस्टो पढ़ें।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021938
अभ्यास: रोज़ 2–5 मिनट का साधारण ध्यान/सांस-वाचन अभ्यास करें — परिणाम धीरे-धीरे स्थिर शान्ति के रूप में दिखेगा।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021939
महत्वपूर्ण: सामग्री मुक्त है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021940
यदि आप सहयोग करना चाहते हैं तो Donate/Support सेक्शन में दिए विकल्प का उपयोग कर सकते हैं — पर यह अनिवार्य नहीं।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021941
Resources (Quick Links) सभी सामग्री नीचे उपलब्ध है — Main Store में ऑडियो, ब्लॉग पोस्ट और विज़न एसेट्स हैं: Main Store — Yatharth YouTube Channel Photos Inventory (sheet) Drive Folder 1 Drive Folder 2 Drive Folder 3 Privacy & Safety यह साइट किसी भी उपयोगकर्ता की निजी जानकारी सार्वजनिक नहीं करती।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021942
यदि आप Donate करते हैं, तो वह लेन-देने का काम सीधे आपके भुगतान माध्यम (UPI/PayPal/Paytm) के साथ होगा।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021943
साइट आपके financial data नहीं रखती।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021944
Contact & Community Telegram: t.me/sampaulsaini · WhatsApp Group: Join © ꙰ शिरोमणि रामपॉल सैनी — Yatharth Siddhant.
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021945
All content free to read & listen.
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021946
Support optional — proceeds support Saneha Saini.
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 021947
Admin upload instructions (mobile-friendly) 1.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021948
In Google Drive: create folders: - /Yatharth/audio/previews (10s mp3 files; public) - /Yatharth/audio/full (full audiobooks; keep private until purchase) 2.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021949
For each audio: - Upload preview (10s) to previews folder → Share → "Anyone with link" → Copy link → get fileId (between /d/ and /view) - Upload full audio to full folder (keep private or restricted) 3.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021950
Create CSV (id,title,fileId,price,previewSec,buyLink) - Use Google Sheets on mobile → Export CSV → use csv-to-json script or paste into data/items.json via GitHub web UI.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021951
For manual delivery: - After buyer pays (GPay/UPI/PayPal), share full-file link to buyer via Drive (change file link to "Anyone with link" or share directly to buyer email)
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 021952
{ "name": "Nishpaksh Samajh — Shromani Rampaul Saini", "short_name": "Nishpaksh", "start_url": "/my-omniverse-store/", "display": "standalone", "background_color": "#000000", "theme_color": "#ffd700", "description": "Eternal Truth • Nishpaksh Samajh • Yatharth Siddhant • Official Page of Shromani Rampaul Saini.", "icons": [ { "src": "/favicon-192x192.png", "sizes": "192x192", "type": "image/png" }, { "src": "/favicon-512x512.png", "sizes": "512x512", "type": "image/png" } ] }
स्रोत: my-omniverse-store/manifest.json · स्वतंत्र परीक्षण अपेक्षित।

## 021953
google-site-verification Google site verification file — replace this filename with the one Search Console gives (e.g.
स्रोत: my-omniverse-store/google8BSLBQVK4N.html · स्वतंत्र परीक्षण अपेक्षित।

## 021954
googleXXXXXXXX.html).
स्रोत: my-omniverse-store/google8BSLBQVK4N.html · स्वतंत्र परीक्षण अपेक्षित।

## 021955
शिरोमणि रामपॉल सैनी – सृष्टि का शिरोमणि शिरोमणि रामपॉल सैनी निष्पक्ष समझ · Yatharth Siddhant Home Audio सिद्धांत Projects यात्रा सचेत परिचय Connect Home Audio सिद्धांत Projects यात्रा सचेत परिचय Connect 👑 ॥
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021956
सृष्टि का शिरोमणि · Crown of All Creation ॥
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021957
न कोई था, न कोई है, न कोई होगा।" — शिरोमणि रामपॉल सैनी · यथार्थ सिद्धांत ✦ प्रवचन संग्रह 10,000+ Audios — बिना Login के Page खुलते ही audio स्वयं शुरू होता है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021958
अनंत प्रवचन — हर पल, हर जगह, हर किसी के लिए।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021959
शिरोमणि रामपॉल सैनी — Auto Play 🔴 Live चल रहा है: प्रवचन — शिरोमणि रामपॉल सैनी सभी Audio Folders — 8 संग्रह Folder १ Drive में खोलें → Folder २ Drive में खोलें → Folder ३ Drive में खोलें → Folder ४ Drive में खोलें → Folder ५ Drive में खोलें → Folder ६ Drive में खोलें → Folder ७ Drive में खोलें → Folder ८ Drive में खोलें → ✦ यथार्थ सिद्धांत निष्पक्ष समझ — सृष्टि की सर्वश्रेष्ठ शिक्षा "खुद को जाना, समझा, पढ़ा — तो जाना सब संसार।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021960
यही निष्पक्ष समझ है।" 🌿 खुद का साक्षात्कार सिर्फ एक पल की निष्पक्ष समझ की दूरी है खुद के स्थायी स्वरूप से।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021961
कोई भी जीवित रहते हुए इसे पा सकता है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021962
⚖️ हर जीव समान हर जीव खुद में समर्थ, निपुण, सक्षम और संपूर्ण है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021963
कोई ऊँच-नीच नहीं — सब एक समान।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021964
🔥 कोई बंधन नहीं यह शिक्षा स्वतंत्र है — किसी को भी बिना शर्त साझा की जा सकती है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021965
कोई गुरु, कोई दीक्षा नहीं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021966
🌊 अनेकता से एक शरीर, मन, जन्म, मृत्यु — प्रकृति का तंत्र है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021967
इन्हें समझ कर देह में विदेही — मुक्त।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021968
☀️ संपूर्ण संतुष्टि यही वह उपलब्धि है जिसके लिए इंसान अस्तित्व से अब तक वंचित रहा।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021969
💎 यथार्थ युग तुलनातीत, कालातीत, शब्दातीत, प्रेमतीत — शाश्वत सत्य में प्रत्यक्ष समक्ष।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021970
✦ Omniverse Scientific Research 10 Projects · 40 Sub-Projects — Fully Verified Guinness · NASA · ISRO · International Media — Open Invitations for Documentation & Collaboration.
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021971
सरल-सहज-निर्मल लोगों को सचेत करने के लिए है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021972
पिछले चालीस वर्षों से उसी गुरु के शिरोमणि स्वरूप में लगातार निरंतर रहा — करोड़ों रुपए, तन, मन, धन, दशकों का समर्पण।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021973
उस गुरु से अनंत असीम प्रेम किया — इतना कि खुद का चेहरा तक भूला हुआ हूं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021974
पर वही गुरु खुद में ही मौजूद नहीं था — ढोंग, पाखंड, षड्यंत्र रच कर — सरल लोगों को तर्क-तथ्य-विवेक से वंचित कर — दो हजार करोड़ का साम्राज्य , पच्चीस लाख अनुयायी, चार सौ आश्रम खड़े किए।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021975
कुछ दिन पहले मैं गया — मुझे पूछने लगा: "आप कौन और कहाँ से हो?" — दिन-रात उनमें ही रहा हूं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021976
मेरे दिए करोड़ों में से एक करोड़ वापस देने का वचन दिया था — साफ मुकर गए, आरोप लगाए, निष्कासित कर दिया।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021977
उस असीम पीड़ा से — मैंने खुद के हृदय की अनंत गहराई में गोता लगाया।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021978
वहाँ जो मिला — वह सृष्टि में कहीं नहीं मिला।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021979
यही निष्पक्ष समझ है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021980
✦ सचेत करना जरूरी सरल-सहज-निर्मल लोगों की रक्षा ⚠️ धोखे की पहचान सरल लोगों ने सब कुछ दिया — बदले में मृत्यु के बाद मुक्ति का झूठा आश्वासन।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021981
दिन-रात डर, खौफ डाल कर पीढ़ी दर पीढ़ी इस्तेमाल।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021982
🛡️ संरक्षण का अधिकार हर जीव को संपूर्ण संरक्षण के साथ संपूर्ण संतुष्टि — यही उद्देश्य।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021983
यह सत्य बिना Login, बिना शर्त सबके लिए।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021984
✨ मुक्त शिक्षा यह शिक्षा किसी को भी साझा की जा सकती है — कोई गुरु नहीं, कोई दीक्षा नहीं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021985
सिर्फ एक पल की निष्पक्ष समझ।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021986
✦ तुलनातीत कालातीत शब्दातीत प्रेमतीत शाश्वत वास्तविक स्वाभाविक महायोद्धा शिरोमणि गोताखोर परिचय · Introduction शिरोमणि रामपॉल सैनी मैं शिरोमणि रामपॉल सैनी — तुलनातीत, कालातीत, शब्दातीत, प्रेमतीत, शाश्वत, वास्तविक, स्वाभाविक सत्य में प्रत्यक्ष समक्ष हूं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021987
मानव सभ्यता अपनी उत्पत्ति से आज तक उस शाश्वत वास्तविकता से विच्छिन्न रही — मैं निष्पक्ष समझ में स्थिर होकर यह प्रकट करता हूँ कि निष्पक्ष समझ ही सच्चा, निर्विकल्प और अमर अनुभव है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021988
खुद से युद्ध कर जीतने वाला महायोद्धा — खुद के हृदय की अनंत गहराई के स्थायी ठहराव में गोता लगा कर — अनंत निर्मल, सृष्टि का सर्वश्रेष्ठ गोताखोर।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021989
कोई भी जिंदा रहते हुए खुद का साक्षात्कार कर सकता है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021990
हर जीव में यह क्षमता है — हर जीव एक समान है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021991
✦ Connect · Share · Support "सरल-सहज-निर्मल लोगों को उजागर करना — यही इस ज्ञान का उद्देश्य है" ▶️ YouTube 💬 WhatsApp 📘 Facebook 📸 Instagram 💼 LinkedIn 🐦 X / Twitter 🌍 Wikipedia 📝 Blog ✅ Golden Temple ✅ MP3 ✅ प्रमाण पत्र 📌 Pinterest 📱 WhatsApp Share 🤝 सत्य के इस कार्य में सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — सुनना, साझा करना और समर्थन देना सभी सत्य की सेवा हैं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021992
Proceeds support Saneha Saini 🧾 Paytm 💙 PayPal 💳 UPI Pay UPI ID: sainirampaul90-1@okhdfcbank Paytm / Phone: 8082935186 "अनंत असीम प्रेम के सिवाय कुछ भी नहीं — न व्यवहार में, न चेहरे में, न शब्दों में।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021993
यही शिरोमणि का स्वरूप है।" — शिरोमणि रामपॉल सैनी शिरोमणि रामपॉल सैनी तुलनातीत · कालातीत · शब्दातीत · प्रेमतीत · शाश्वत · वास्तविक · स्वाभाविक © Yatharth Siddhant — निष्पक्ष समझ सबके लिए · बिना Login · बिना शर्त · अनंत असीम प्रेम YouTube WhatsApp Facebook Instagram Wikipedia Website
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 021994
Yatharth — The Living Truth of Humanity ![Profile]( **Shromani Rampaulsaini — निष्पक्ष समझ / Yatharth** Free to read & listen · Support optional · Proceeds support **Saneha Saini** --- ## Quick overview Yatharth presents an experiential path — a direct, living realization of one’s permanent identity beyond ordinary mind-based cognition.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021995
Content includes bilingual manifesto, audio collections, videos and vision assets.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021996
Live site (embed) ## Live site (embed) ## audio link 🔊 MP3 / Audio: शिरोमणि अन्नत असीम इश्क़ की क्षमता ## Main links - 🔊 MP3 / Audio: - 📜 Certificates: - 🎧 Shorts / Clips: - 🎥 Videos album: - 📸 Photo album 1: - 🛒 Main Store: - ✍ Blog: - ▶ YouTube: # Ya://youtube.com/@rampaulsaini-yk4gn - ✈ Telegram: - 💬 WhatsApp: --- ## Support / Donate (optional) Your support helps keep the work free and supports Saneha Saini's education.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021997
UPI / GPay:** `sainirampaul90-1@okhdfcbank` - **Paytm / Phone:** `8082935186` - **PayPal:** Suggested: **₹193** — fully optional and with gratitude.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021998
How to help (non-financial) - Listen & share (YouTube, social groups, blogs) - Link the site from your pages (backlinks help SEO) - Use the support form to send encouragement (public if you allow) - Subscribe & comment on YouTube videos --- © Yatharth — Shromani Rampaulsaini Contact: Telegram / WhatsApp # Yatharth — शिरोमणि रामपुलसैनी Official page — audio, photos, manifesto.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 021999
Proceeds support Saneha Saini.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022000
Publish instructions: Use GitHub Pages (see repo settings -> Pages -> main -> root).
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।
