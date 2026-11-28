# डिजिटल महाग्रंथ 094

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 093001
``` For a new application: ```text Read /path/to/kit-app-containerize/SKILL.md.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093002
Help me create and containerize a new Kit application for streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093003
Ask about the Kit version, streaming target, and image name/tag where needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093004
``` Keep the complete `kit-app-containerize/` directory together.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093005
Resolve each relative link from the file containing that link, preserving the folder layout even when the application is in another checkout.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093006
An older project or an NGC SDK package can use this skill from a separate checkout without changing the application's Kit version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093007
Publishing a skill under `.skills` does not guarantee automatic discovery in every agent host.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093008
Direct file loading is the baseline.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093009
If your agent supports a native skills directory, copy or link the complete folder into that host's documented location.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093010
A plain copy of `SKILL.md` omits required references.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093011
No agent-specific installer or additional plugin is required for direct loading.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093012
Contents | File | Purpose | |---|---| | [SKILL.md](SKILL.md) | Developer preflight, workflow, and completion rules.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093013
| | [App preparation](references/app-preparation.md) | Existing apps, version selection, streaming layers, and the secondary NGC route.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093014
| | [Container workflow](references/container-workflow.md) | Build prerequisites, packaging commands, image naming, and troubleshooting.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093015
| | [Validation and handoff](references/validation-and-handoff.md) | Exact-image runtime checks, optional publication, and downstream results.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093016
| The initial execution workflow targets Linux x86_64 with Docker and compatible Kit artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093017
RTX runtime checks require compatible hardware; containerization-only is supported without claiming runtime validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093018
The skill inspects the selected project's actual tooling rather than promising identical behavior across all Kit versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093019
See the [Kit containerization guide]( and [OVS getting-started guide]( for the surrounding developer journey.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093020
name: kit-app-containerize description: Prepare and containerize an existing or new NVIDIA Omniverse Kit application, including Kit App Streaming or NVCF layers, explicit image naming, optional runtime validation, and an image handoff.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093021
Use for Kit application container builds and packaging, rather than cluster deployment or frontend development.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093022
Containerize a Kit application Produce the developer's requested container image from the selected Kit app, and report what was built and verified.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093023
Prefer the existing application.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093024
For a new application, recommend the public [Kit App Template]( on `main`; offer another Kit version/ref when requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093025
NGC SDK download is a secondary route.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093026
Resolve the developer's intent Inspect the request, orchestration context, and project before asking questions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093027
Ask only for missing decisions that affect the work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093028
| Decision | Action | |---|---| | Existing application or new application?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093029
| Locate the existing project and intended app, even if it needs preparation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093030
For a new app, resolve the template and required app name, display name, and app version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093031
| | Streaming from the container?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093032
| Determine Kit App Streaming versus NVCF.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093033
In the inspected Kit App Template layer picker, Kit App Streaming is `[omni_default_streaming]: Omniverse Kit App Streaming (Default)` and renders `{app_name}_streaming.kit`; NVCF is `[nvcf_streaming]: NVCF Streaming` and renders `{app_name}_nvcf.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093034
Check whether the appropriate layer already exists.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093035
For non-streaming use, establish the intended headless service, batch, or rendering behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093036
| | Which Kit version?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093037
| For a new app without a specified version, ask whether to use public GitHub `main` or another Kit version/ref.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093038
Recommend `main` and show its resolved Kit version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093039
For an existing app, report and preserve its version unless a change is requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093040
| | What image name and tag?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093041
| Resolve the full image repository/name and explicit version tag, including any registry/namespace.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093042
Preserve supplied values.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093043
Kit version, app version, and container tag are separate choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093044
| | What runtime validation?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093045
| Recommend running RTX apps on a compatible RTX GPU before packaging and checking the built container afterward.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093046
Allow containerization only, even when a GPU is present.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093047
Offer applicable CPU checks for non-rendering services.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093048
| | Required license acceptance?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093049
| Identify the selected workflow's applicable terms early.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093050
When acceptance is required and not already supplied, collect it with the initial preflight questions before generation or long-running builds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093051
Follow [license preflight](references/app-preparation.md#license-acceptance-during-preflight).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093052
| An existing app without streaming layers stays on the existing-app path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093053
Ordinary streaming configuration does not establish NVCF readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093054
If multiple apps or layers fit the request, resolve the selection before modifying files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093055
Prepare the selected app Read [app preparation](references/app-preparation.md) for the applicable existing-app, new-project, or NGC route.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093056
Resolve the project, source ref/artifact, Kit and tool versions, exact app/layer, and target platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093057
Inspect the developer project's pins, rather than assuming the toolchain of a different repository or the latest documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093058
Reuse the app and correct streaming layer, or generate only the missing app/layer/configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093059
Inspect dependencies and settings as well as template metadata.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093060
Preserve custom work; substantial application repair or a Kit migration needs its own scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093061
Establish a compatible Linux x86_64 build environment and Docker access for the initial workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093062
Native Windows packaging is unsupported by the inspected tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093063
A suitable WSL or remote Linux environment must execute the native Kit packaging steps, not just host a Docker daemon.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093064
The standard inspected pipeline can build/package without RTX rendering.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093065
Custom hooks or Dockerfiles can add GPU requirements.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093066
Runtime rendering/streaming needs compatible GPU resources.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093067
Extension dependency precaching is not shader warmup.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093068
Do not claim an unexecuted GPU-free build succeeded.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093069
Build and package Read [container workflow](references/container-workflow.md) before packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093070
It covers the actual CLI, app/config matching, image references, and common failures.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093071
Build with the selected project's supported release workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093072
Confirm dependencies and the selected app artifacts are present.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093073
Perform source-app runtime validation when selected and available.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093074
Record it separately from container validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093075
Resolve a real, unique staged app and a writable `repository:explicit-tag`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093076
Reuse matching container configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093077
Inspect an existing target tag before replacing it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093078
Package with the selected tool's supported arguments.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093079
The inspected command is `./repo.sh package_container --app --image-tag : --config release`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093080
Inspect the resulting image ID, requested tag, architecture, app label/configuration, entrypoint, and required runtime inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093081
An old image with the same tag is not evidence of a successful build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093082
The default entrypoint uses `--no-window` and invokes Kit directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093083
It does not automatically retain a custom shell launcher's setup or provide a desktop display.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093084
Inspect those requirements before promising equivalent behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093085
Diagnose failures, make a bounded correction supported by the evidence, and repeat affected steps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093086
Report unresolved blockers rather than repeatedly rebuilding unchanged inputs, broadly cleaning the environment, or silently changing Kit versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093087
Validate and hand off Read [validation and handoff](references/validation-and-handoff.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093088
Always inspect the build result and image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093089
Run only the runtime checks selected by the developer, against the exact built image ID or published digest.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093090
| Outcome | Report | |---|---| | Build and image inspection succeed; containerization only requested | Complete.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093091
Runtime validation not run by request.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093092
| | Runtime validation requested and passes | Complete for the checks actually performed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093093
| | Build succeeds but requested runtime checks cannot run | Image built; requested validation remains unverified, with the reason.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093094
| | A build or runtime check fails | Failed stage and evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093095
Do not relabel a failure as skipped.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093096
| Return source/SDK provenance, resolved versions, chosen app and streaming target, image reference and ID, platform/runtime requirements, evidence, and remaining checks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093097
Use a consistent human-readable result; use a machine format only when the caller supplies a real contract.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093098
Publish the image only when requested for a resolved destination.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093099
A registry-qualified tag alone is not a request to push.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093100
A local-only image is a valid containerization result, but downstream NVCF workers still need a distributed image and registry pull access.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093101
NVCF deployment, frontend creation, and full browser/media validation are separate stages.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093102
Container readiness does not prove end-to-end streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093103
Carry the image identity and required runtime configuration to the next stage without claiming its checks passed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093104
Kit SDK Upgrade Skill ## What This Is This repository contains an AI agent skill for upgrading Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093105
The skill encodes the complete breaking-change catalog for the Kit 106→107→108→109→110 migration path — including removed extensions, deprecated APIs, C++ ABI breaks, Python runtime changes, and configuration updates — into a structured set of instructions and reference data that an AI agent can execute against a live project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093106
The agent scans the project, produces a categorized report with exact `file:line` references, and suggests targeted fixes, including auto-fixable regex replacements where safe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093107
Who It's For Kit extension and application developers who need to upgrade a project from one Kit SDK version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093108
This includes developers working on kit-app-template-based applications, standalone extensions, and Isaac Sim integrations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093109
The skill is particularly useful when upgrading across multiple versions at once (e.g., 107→110), where the number of breaking changes makes manual triage error-prone.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093110
What It Contains | File | Description | |------|-------------| | `SKILL.md` | Lean workflow router — loaded by the AI agent.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093111
Holds version/layout/build detection (Step 1) and the migration-path decision (Step 2), and points to the procedure files for everything else.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093112
| | `procedures/toolchain.md` | Step 2.5 — update the `repo_*` build toolchain (the highest-impact part of most upgrades).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093113
| | `procedures/scan.md` | Step 3 — the full per-stage `grep` scan catalog for breaking changes, removed extensions, and config.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093114
| | `procedures/report.md` | Step 4 — the upgrade-report template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093115
| | `procedures/apply-fixes.md` | Step 5 — ordered fix list, auto-fixable regex patterns, and manual-only changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093116
| | `procedures/validate.md` | Step 6 — clean-rebuild and validation commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093117
| | `procedures/failure-modes.md` | Symptom→fix diagnosis for projects that already upgraded and are erroring.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093118
| | `procedures/stage-notes.md` | Per-stage (106→107→…→110) breaking-change reference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093119
| | `references/breaking_changes.json` | 80+ breaking changes with search patterns, affected versions, and recommended fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093120
| | `references/removed_extensions.json` | Extensions removed or deprecated by Kit version, with replacement guidance and search targets.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093121
| | `references/api_replacements.json` | 1:1 API replacements that are safe to apply with regex find/replace.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093122
| | `references/config_changes.json` | Settings keys, registry URLs, and build config changes between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093123
| | `references/toolchain.json` | The build-toolchain file/package set (`repo_*` tools, packman, repo scripts) and how to find the correct target versions for a given Kit line.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093124
| | `install.sh` / `install.bat` | Copies the skill (SKILL.md + `procedures/` + `references/`) into an existing Kit project so it travels with the repo.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093125
| The skill uses **progressive disclosure**: `SKILL.md` stays small (a router the agent always loads) and each step's detail lives in a `procedures/*.md` file the agent reads only when the workflow sends it there.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093126
This keeps the entry file well under length limits and keeps irrelevant detail out of context.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093127
How to Use **Install into an existing project** (so the skill travels with the repo): ```bash ./install.sh /path/to/your-kit-project # copies into /.skills/kit-upgrade/ ./install.sh /path/to/your-kit-project .claude/skills # or the Claude Code skills layout ``` On Windows: `install.bat C:\path\to\your-kit-project`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093128
Then load the skill into any AI coding assistant that can read files and run shell commands, and point it at the project you want to upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093129
Claude Code:** ``` Read the skill at /path/to/kit-upgrade-skill/SKILL.md and the reference files in references/.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093130
Then scan /path/to/my-kit-project and generate an upgrade report for Kit 109 → 110.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093131
``` **Cursor / VS Code Copilot / other MCP clients:** Add `kit-upgrade-skill/` as a context directory or attach `SKILL.md` as a system prompt, then ask the agent to scan your project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093132
Detect the current Kit SDK version, the deps-directory location (`tools/deps/` vs root `deps/`), and the build entrypoint (`./repo.sh` / `repo.bat` or a custom/integrated build) — never assuming the SDK template layout 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093133
Determine the migration path — including within-major (minor/patch) and feature↔production transitions, not just major-version stages 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093134
Update the build toolchain (`repo_*` tools, packman, repo scripts) to match the target Kit line — often the substantive part of an upgrade 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093135
Run targeted `grep` scans across the full project root (including `templates/`, launcher configs, and ETM lock files) for any major boundaries crossed 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093136
Generate a categorized report: breaking changes, behavioral changes, deprecated usage, and a "not affected" checklist 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093137
Suggest fixes — both auto-applicable regex replacements and manual changes requiring human judgment 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093138
Its changes are folded into the 107→109 path — Stage 2 must still be addressed when upgrading 107→109.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093139
Multi-version upgrades (e.g., 107→110) apply all intervening stages in sequence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093140
How to Contribute **Add a new breaking change:** Add an entry to `references/breaking_changes.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093141
Each entry needs an `id`, `title`, `stage`, `search_pattern` (grep-compatible regex), `affected_files` (glob patterns), and `fix` description.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093142
If the fix is a safe 1:1 substitution, also add it to `references/api_replacements.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093143
Add a removed or deprecated extension:** Add an entry to `references/removed_extensions.json` with `extension`, `status` (`removed` or `deprecated`), `version`, `replacement` (or `null`), `search_in` (list of file extensions to scan), and `notes`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093144
Include any known failure mode (e.g., exit-55) and whether the extension appears in non-obvious locations like `templates/` or ETM lock files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093145
Add a new Kit version (release):** edit the files that own each piece — the skill is split by concern: - `SKILL.md` — add the new row/stage to the **Step 2 migration-path table and Stage summary** (these stay in the router).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093146
`procedures/scan.md` — add the new `# === Stage N ===` scan blocks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093147
`procedures/stage-notes.md` — add the new per-stage breaking-change section.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093148
`procedures/apply-fixes.md` — add any new auto-fix regex patterns or fix-list items.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093149
`references/*.json` — add the corresponding structured entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093150
Follow the existing section structure in each file for consistency.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093151
Keep `SKILL.md` lean — detailed scan commands and stage notes belong in `procedures/`, not the router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093152
Test your additions:** Apply the skill to a real project that exercises the new patterns.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093153
If the scan misses something or the fix guidance is wrong, document it and open a PR with both the issue description and the corresponding fix in the relevant `procedures/` or `references/` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093154
This skill was developed and validated against [kit-extension-explorer]( a Kit 110 application based on kit-app-template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093155
See `test-report.md` for the full upgrade report from that validation run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093156
name: kit-upgrade description: "Scan and upgrade Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093157
Analyzes project files, identifies breaking changes, deprecated APIs, and removed extensions specific to the customer's code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093158
Provides a personalized upgrade plan with file:line references and auto-fix suggestions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093159
Covers Kit 106→107→108→109→110." --- # Kit SDK Upgrade Skill Guide a developer through upgrading their Omniverse Kit project from one version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093160
This skill is a lean workflow router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093161
Steps 1 and 2 (detect the project, decide the migration path) are inline below** — they are always needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093162
The detail for the remaining steps (2.5–6) lives in `procedures/`, and the structured change data in `references/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093163
Read each procedure file when the workflow sends you to it** — do not try to hold them all in context at once.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093164
When to Use - User asks to upgrade their Kit project/app/extension - User asks about Kit breaking changes or migration - User is hitting errors after changing their Kit SDK version - User has a broken build or runtime failure after a version bump --- ## Quick Orientation Pick the entry point that matches the request: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093165
First-time upgrade scan** → start at Step 1 below and follow the workflow in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093166
Already upgraded, now has a build/runtime error** → go straight to `procedures/failure-modes.md`, diagnose, then apply the relevant Stage's fixes from `procedures/stage-notes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093167
Just wants a list of breaking changes** → do Step 1, then run the scans in `procedures/scan.md` for their migration path and present the report from `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093168
The `# Kit SDK Version:` comment in `.kit` files reflects the last lock-file regeneration and may differ from the pin during an in-progress upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093169
Version string format: `110.1.0+feature.${platform_target_abi}.${config}` - First number (110) = major Kit version **If no version pin is found:** Check git history (`git log --oneline -20 -- tools/deps/ deps/`) or ask the user what Kit version they are currently running.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093170
(Layout detection below has not run yet, so scope the log to both candidate deps locations.) ### Detect project layout and build system Kit projects do **not** all use the SDK template layout, and the layout can differ between releases and project types — for example, `deps/` may sit at the project **root** in one release and under **`tools/`** in another (even between two point releases of the same major line).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093171
Projects also frequently **wrap or integrate the Kit build system into their own tooling**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093172
Detect the layout and build entrypoint **once**, then reuse them everywhere below — **never assume `tools/deps/` or `./repo.sh`**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093173
deps directory (holds kit-sdk.packman.xml + repo-deps.packman.xml) if [ -f tools/deps/kit-sdk.packman.xml ]; then DEPS_DIR=tools/deps elif [ -f deps/kit-sdk.packman.xml ]; then DEPS_DIR=deps else f=$(find .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093174
name kit-sdk.packman.xml -not -path './_*' | head -1); DEPS_DIR=${f:+$(dirname "$f")}; fi echo "DEPS_DIR=${DEPS_DIR:- }" # 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093175
build entrypoint — the standard repo wrapper, if present if [ -f ./repo.sh ]; then BUILD='./repo.sh' elif [ -f ./repo.bat ]; then BUILD='repo.bat' else BUILD=''; fi # empty => custom / integrated build (see below) echo "BUILD=${BUILD:- }" ``` **If `BUILD` is empty, the project uses a custom or integrated build system** (common — many customers embed the Kit build inside their own).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093176
Do **not** fabricate `./repo.sh` calls.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093177
Find the real build command (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or the project README) or ask the user how they build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093178
The upgrade work below (kernel pin bump, **toolchain update**, lock regeneration) still applies — you just invoke it through the project's own entrypoint.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093179
Record it as `$BUILD`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093180
> **From here on (and in every procedure file), use `$DEPS_DIR` and `$BUILD` in every command.** Where a document still shows a literal `tools/deps/` or `./repo.sh`, substitute the detected values.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093181
> > **These are not guaranteed to persist across shells.** If you run each fenced block in a fresh subshell, `$DEPS_DIR`/`$BUILD` will be unset.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093182
So do **one** of: (a) textually replace `$DEPS_DIR` and `$BUILD` with the literal detected paths (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093183
`tools/deps`, `./repo.sh`) in every command you run, or (b) re-run the two detection blocks above at the top of each new shell session.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093184
Do **not** run a later block assuming the variables are still set.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093185
Step 2: Determine Migration Path Kit versions must be upgraded **in sequence**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093186
Kit 108 was never publicly released** — its changes are folded into the 107→109 path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093187
When upgrading 107→109 you must still address Stage 2 (107→108) changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093188
A **within-major** bump (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093189
`110.0 → 110.1`, `110.1.0 → 110.1.2`) or a **feature → production** branch transition is a *different, lighter* job — and it is the most common upgrade performed in practice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093190
These rarely need the Stage code/API changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093191
The real work is almost entirely **tooling and layout**: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093192
Update the build toolchain** (repo tools, packman, repo scripts) — see Step 2.5 (`procedures/toolchain.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093193
This is usually the substantive part.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093194
Re-detect the deps directory** — its location can differ between releases, even within the same major line (Step 1 already sets `$DEPS_DIR`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093195
Bump the kit-kernel pin** in `$DEPS_DIR/kit-sdk.packman.xml` (Step 5, item 2 — `procedures/apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093196
For a feature ↔ production transition only:** check the extension **registry URL** in the `.kit` files — the feature and production lines use different registries, so a feature→production move may need a registry swap (Step 5, item 3).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093197
A plain within-major bump on the same line usually does **not**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093198
Regenerate the extension version-lock** and do a **clean rebuild** (Step 5 items 1 & 8, then Step 6).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093199
> **⚠️ Do NOT run the whole of Step 5 for a within-major bump.** Step 5 (`procedures/apply-fixes.md`) is written for **major-boundary** crossings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093200
Running them on a 110.1.0→110.1.2 bump would wrongly strip extensions or rewrite APIs that are perfectly valid on 110.1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093201
Only run the Step 3 code scans if the upgrade crosses a major boundary.** For a pure within-major or feature→production move, skip Step 3's per-stage API scans and go straight to Step 2.5 → Step 5 (items 1–3 & 8 only, as above) → Step 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093202
If you cross one or more major boundaries on the way, run Step 3 for each major boundary passed and the full Step 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093203
Steps 2.5–6: Execute the Upgrade Once the path is known, work through these in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093204
Read the linked procedure file and follow it**; each assumes Step 1 detection has run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093205
Step 2.5 — Update the build toolchain** → `procedures/toolchain.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093206
Highest-impact step; run it **first**, before touching source.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093207
For a within-major bump this is usually the only substantive work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093208
Step 3 — Scan the project** → `procedures/scan.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093209
Run only the stage scans for the major boundaries you cross.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093210
Skip entirely for a pure within-major bump.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093211
Step 4 — Generate the upgrade report** → `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093212
Present findings by severity with exact `file:line` references.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093213
Step 5 — Apply fixes** → `procedures/apply-fixes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093214
Get user approval before modifying files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093215
(Within-major: items 1, 2, 8 only — see Step 2 above.) - **Step 6 — Validate** → `procedures/validate.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093216
Clean rebuild, regenerate the version lock, run tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093217
Already upgraded and hitting a specific error?** Go to `procedures/failure-modes.md` — it maps common symptoms (exit-55, ABI undefined symbols, render diffs, build loops, custom-build/layout issues) to fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 093218
[ { "extension": "omni.kvdb", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093219
Causes exit code 55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093220
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.localcache", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093221
Same failure class as omni.kvdb.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093222
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.genproc.core", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093223
Migrate procedural generation workflows.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093224
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.kit.extpath.git", "status": "removed", "version": "108", "replacement": null, "search_in": [ "extension.toml" ], "notes": "Git URL extension search path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093225
Was deprecated in 107." }, { "extension": "omni.hydra.iray.shadercache.d3d12", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093226
No explicit removal notice." }, { "extension": "omni.hydra.iray.shadercache.vulkan", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093227
No explicit removal notice." }, { "extension": "omni.kit.viewport.iray", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Was Sample in Kit 107.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093228
No version recorded in official docs." }, { "extension": "omni.hydra.scene_api", "status": "deprecated", "version": "108", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated since Kit 108.0.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093229
Removal pending." }, { "extension": "omni.surface_instancer", "status": "deprecated", "version": "pre-106", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Confirmed deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093230
Active customer confusion." }, { "extension": "omni.renderer_capture", "status": "deprecated", "version": "110", "replacement": "omni.kit.capture", "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated in Kit 110." }, { "extension": "omni.kit.widget.nucleus_connector", "status": "deprecated", "version": "110", "replacement": "omni.kit.widget.connection_manager", "search_in": [ "extension.toml", ".kit" ], "notes": "Compatibility shim.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093231
Will be removed." }, { "extension": "omni.kit.viewport.legacy_gizmos", "status": "deprecated", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Deprecated in Kit 110.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093232
Still operational but emits deprecation warnings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093233
Commonly appears in both source/apps/ and templates/ .kit files — scan the full project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093234
No direct replacement announced; plan migration away from legacy gizmos rendering path." }, { "extension": "omni.kit.livestream", "status": "removed", "version": "108", "replacement": "omni.kit.livestream.app + omni.kit.livestream.aov + omni.kit.livestream.core", "search_in": [ "extension.toml", ".kit" ], "notes": "Monolithic livestream extension split into focused modules in Kit 108.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093235
Replace with the three new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093236
Settings paths also changed \u2014 see config_changes.json." }, { "extension": "omni.services.livestream.nvcf", "status": "removed", "version": "108", "replacement": "omni.services.livestream.session", "search_in": [ "extension.toml", ".kit" ], "notes": "Session management extension renamed in Kit 108.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093237
Replace dependency declaration and update any code referencing the old extension name." } ]
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 093238
{ "description": "The build toolchain a Kit project must keep in sync with its kit-kernel pin.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093239
SKILL.md Step 2.5 makes updating it a first-class step.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093240
Do NOT hardcode versions here — they move per branch; read the target branch's actual pins at upgrade time.", "toolchain_files": [ {"file": " /kit-sdk.packman.xml", "holds": "kit-kernel pin (the Kit SDK itself)", "notes": "DEPS_DIR is tools/deps/ or root deps/ — detect it (SKILL.md Step 1)."}, {"file": " /repo-deps.packman.xml", "holds": "the repo_* build tools + template-content packages", "notes": "The main toolchain file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093241
Add or remove packages that appear/disappear between lines (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093242
repo_nspect is present on feature/main but not on production/110.1 or feature/110.3).", "reference_source": "omniverse/kit-apps/kit-sdk-public (and/or omniverse/kit-github/kit-app-template) on the matching branch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093243
Prefer production/ over feature/ for a stable upgrade.", "critical_note": "Toolchain versions track the BRANCH's maintenance cadence, NOT the kernel line number.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093244
A newer kernel line can carry an OLDER toolchain.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093245
Never infer tool versions from the Kit version — read the actual target-branch pins.", "example_only_do_not_copy": { "note": "Illustrative snapshot read from kit-sdk-public in 2026 — WILL go stale.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093246
Always re-read the target branch at upgrade time.", "feature/main": {"kit-kernel": "110.4.0+feature", "repo_man": "2.6.4", "repo_build": "1.30.0", "repo_kit_tools": "1.20.3"}, "production/110.1": {"kit-kernel": "110.1.3+production", "repo_man": "2.9.3", "repo_build": "1.34.3", "repo_kit_tools": "1.21.2"} } } }
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 093247
[ {"setting":"packman XML ABI token","versions":{"from":"106","to":"107"},"old_value":"${platform_target}","new_value":"${platform_target_abi}","file":"*.packman.xml","path":"package name attributes","notes":"Native packages now use ABI-variant package names.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093248
The deps directory location varies by release and project type (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093249
deps/ at the project root in one release, under tools/ in another, even between point releases of the same major line).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093250
Do NOT assume tools/deps/ and do NOT rewrite paths from old_value to new_value -- detect the actual location (SKILL.md Step 1, $DEPS_DIR)."} ]
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093251
[ {"id":"py-omniclient","versions":{"from":"106","to":"107"},"category":"Python API","severity":"breaking","title":"omni.client._omniclient removed","description":"Private internal API removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093252
Use public omni.client API.","search_patterns":["omni\\.client\\._omniclient"],"file_types":[".py"],"fix":{"type":"regex_replace","description":"Replace import","from_pattern":"import omni\\.client\\._omniclient","to_pattern":"import omni.client"}}, {"id":"py-311","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"Python 3.10 → 3.11","description":"Python upgraded.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093253
Audit f-strings, typing module usage, and third-party packages for 3.11 compatibility.","search_patterns":["python3\\.10","python310"],"file_types":[".toml",".py",".sh",".bat",".lua"],"fix":{"type":"manual","description":"Update Python references to 3.11"}}, {"id":"cpp-abi-cxx11","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Linux: _GLIBCXX_USE_CXX11_ABI=1","description":"Native packages now use new C++ ABI.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093254
Rebuild all .so plugins.","search_patterns":["_GLIBCXX_USE_CXX11_ABI"],"file_types":[".cpp",".cmake",".toml"],"fix":{"type":"manual","description":"Rebuild all native plugins against new ABI"}}, {"id":"packman-abi-token","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"packman XML: ${platform_target} → ${platform_target_abi}","description":"Native packages now use ABI-variant tokens.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093255
Python payload access changed from e.payload['key'] to e['key'].
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093256
Subscribe via carb.eventdispatcher.get_eventdispatcher().observe_event().
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093257
C++: update to carb::eventdispatcher.","search_patterns":["e\\.payload\\[","carb\\.events\\.acquire_event_queue","create_subscription_to_pop"],"file_types":[".py",".cpp",".h"],"fix":{"type":"manual","description":"Update event subscriptions and payload access to Events 2.0 pattern.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093258
Remove explicit event pump calls."}}, {"id":"fabric-pathc-tokenc-intro","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Fabric PathC/TokenC introduced (removed in 109)","description":"Kit 107 introduced PathC/TokenC.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093259
Kit 109 removes them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093260
Update Premake configs, CI, and build scripts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093261
Audit all third-party packages for 3.12 compatibility.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093262
Use getCachedInterface.","search_patterns":["acquireInterface"],"file_types":[".cpp",".h"],"fix":{"type":"regex_replace","from_pattern":"carb::Framework::acquireInterface","to_pattern":"carb::getCachedInterface"}}, {"id":"omnigraph-3.0","versions":{"from":"107","to":"108"},"category":"C++ ABI","severity":"breaking","title":"omni.graph.core 3.0.0 ABI break","description":"Binary incompatible with 2.x.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093263
Recompile all OmniGraph nodes.","search_patterns":["omni\\.graph\\.core","omni\\.graph\\.nodes"],"file_types":[".toml"],"fix":{"type":"manual","description":"Recompile against omni.graph.core 3.0.0.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093264
Align omni.graph.nodes version."}}, {"id":"parallel-node-reg","versions":{"from":"107","to":"108"},"category":"Extension","severity":"breaking","title":"Parallel OmniGraph node registration removed","description":"Extension manager is not thread-safe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 093265
Step 3: Scan the Project > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093266
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093267
Only run this step for major-version boundaries you cross** — a pure within-major / feature→production bump skips it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093268
Run these commands from the project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093269
Only run scans for the stages that apply to this upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093270
Collect all matches before generating the report.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093271
> **⚠️ Scan scope:** Use `.` (project root) as the search root, not just `source/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093272
Many projects have `templates/`, `launcher-configs/`, or other directories containing `.kit` files and `extension.toml` files with real dependency declarations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093273
Scanning only `source/` will miss these.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093274
> > **Windows note:** Commands below use bash syntax.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093275
On Windows, replace `for` loops with individual `findstr` or PowerShell `Select-String` commands, or run inside WSL/Git Bash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093276
Python / Extension Dependencies ```bash # === Stage 1 (106→107) === # Python 3.10 references (now 3.11) grep -rn "python3\.10\|python310\|boost_python310" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093277
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" --include="*.toml" # Private omni.client API grep -rn "omni\.client\._omniclient" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093278
include="*.py" # carb.imgui (removed — use omni.kit.imgui) grep -rn "carb\.imgui" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093279
include="*.py" # Events 1.0 patterns (payload access, subscription style) grep -rn "e\.payload\[" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093280
include="*.py" grep -rn "create_subscription_to_pop" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093281
include="*.py" # nv_usd references in build files grep -rn "nv_usd" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093282
premake5.lua repo.toml --include="*.lua" --include="*.toml" # packman XML using a pre-ABI token (should be ${platform_target_abi}).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093283
NOTE: match BOTH the old ${platform} form (Kit 106) and the intermediate ${platform_target} form — # the narrower 'platform_target[^_]' pattern misses ${platform}, which is what 106.5 actually uses and # is a build-verified hard failure on 106->107 (kit-kernel pull: "Package not found ...gl.linux-x86_64").
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093284
grep -rnE '\$\{platform(_target)?\}' "$DEPS_DIR" --include="*.xml" # Toolbar deprecated APIs grep -rn "omni\.kit\.widget\.toolbar\|omni\.kit\.window\.toolbar" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093285
include="*.py" --include="*.toml" # === Stage 2 (107→108) === # Python 3.11 references (now 3.12) grep -rn "python3\.11\|python311\|boost_python311" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093286
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" # get_custom_glyph_code (moved to omni.ui) grep -rn "omni\.kit\.ui.*get_custom_glyph_code" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093287
include="*.py" # WindowHandle deprecated usage grep -rn "WindowHandle" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093288
include="*.py" # menu_compatibility (deprecated in 108, removed in 110) grep -rn "menu_compatibility" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093289
include="*.py" # Layer events (Events 1.0 style) grep -rn "get_event_stream\|create_subscription_to_pop\|carb\.events" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093290
include="*.py" # Livestream extension (monolithic — should be split) grep -rn '"omni\.kit\.livestream"' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093291
include="*.kit" --include="*.toml" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093292
include="*.kit" --include="*.toml" # Livestream settings (old path) grep -rn "app/livestream\|app\.livestream" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093293
include="*.kit" --include="*.toml" # Old omni.kit.ui transitive usage (no longer loaded transitively) grep -rn "omni\.kit\.ui[^.]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093294
include="*.py" # === Stage 3 (108→109) === # NumPy 1.x type aliases (removed in 2.0) grep -rn "np\.bool[^_]\|np\.int[^0-9_]\|np\.float[^0-9_]\|np\.complex[^0-9_]\|np\.object[^_]\|np\.str[^_]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093295
include="*.py" # === Stage 4 (109→110) === # menu_compatibility (now raises TypeError — must remove entirely) grep -rn "menu_compatibility=" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093296
include="*.py" # omni.usd layers deprecated API grep -rn "get_context()\.get_layers()\|context\.get_layers()" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093297
include="*.py" # omni.renderer_capture (deprecated → omni.kit.capture) grep -rn "omni\.renderer_capture" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093298
include="*.py" # USD displayName/displayGroup/hidden deprecated metadata grep -rn "GetMetadata.*displayName\|SetMetadata.*displayName\|GetMetadata.*hidden\|SetMetadata.*hidden\|GetMetadata.*displayGroup\|SetMetadata.*displayGroup" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093299
include="*.py" ``` ### C++ / Native Code ```bash # === Stage 1 (106→107) === # C++ ABI — check for _GLIBCXX_USE_CXX11_ABI overrides (must be =1) grep -rn "_GLIBCXX_USE_CXX11_ABI" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093300
include="*.cpp" --include="*.h" --include="*.cmake" # === Stage 2 (107→108) === # ITokens::setValue (renamed to setValueS) grep -rn "->setValue(" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093301
include="*.cpp" --include="*.h" # carb::detail::defineTupleCommon grep -rn "carb::detail::defineTupleCommon" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093302
include="*.cpp" --include="*.h" # PyObjectVTable::get()->typeName grep -rn "PyObjectVTable" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093303
include="*.cpp" --include="*.h" # acquireInterface (prefer getCachedInterface) grep -rn "acquireInterface" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093304
include="*.cpp" --include="*.h" # carb::extras::Path implicit conversion grep -rn "carb::extras::Path\|carb::fs::Path" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093305
include="*.cpp" --include="*.h" # Assert macros (may need explicit carb/Assert.h now) grep -rn "CARB_ASSERT\|CARB_FATAL_UNLESS" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093306
include="*.cpp" --include="*.h" # Library.h removed functions grep -rn "getDefaultLibraryPrefix\|getDefaultLibraryExtension" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093307
include="*.cpp" --include="*.h" # GfMatrix usage (imprecise overloads removed) grep -rn "GfMatrix" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093308
include="*.cpp" --include="*.h" # ILayers.h inclusion (ABI 1.0 → 1.1 recompile required) grep -rn "ILayers\.h\|omni/kit/usd/layers" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093309
include="*.cpp" --include="*.h" # carb.events const char* usage (deprecated — prefer string_view) grep -rn "carb::events::\|IEventQueue\|IEvents" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093310
include="*.cpp" --include="*.h" # Scalar xform ops — code that iterates over xform ops assuming vector types grep -rn "GetOrderedXformOps\|xformOp:translate\|xformOp:scale\|xformOp:rotate" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093311
include="*.cpp" --include="*.h" --include="*.py" # === Stage 3 (108→109) === # Fabric TokenC/PathC (removed; also kUninitializedToken/Path) grep -rn "TokenC\|PathC\|TokenId\|PathId\|kUninitializedToken\|kUninitializedPath" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093312
include="*.cpp" --include="*.h" # carb::cpp17 / carb::cpp20 (merged to carb::cpp) grep -rn "carb::cpp17\|carb::cpp20" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093313
include="*.cpp" --include="*.h" # carb::thread::shared_lock (removed) grep -rn "carb::thread::shared_lock" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093314
include="*.cpp" --include="*.h" # IDictionary::MakeAtPathS (renamed to MakeAtPath) grep -rn "MakeAtPathS" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093315
include="*.cpp" --include="*.h" # compareStringsNoCase (renamed) grep -rn "compareStringsNoCase" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093316
include="*.cpp" --include="*.h" # Logger (superseded by Logger2) grep -rn "carb::logging::Logger[^2]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093317
include="*.cpp" --include="*.h" # MDL/Neuray usage (ABI 56 → 57 recompile required) grep -rn "omni\.mdl\|Neuray\|MDL.*SDK" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093318
include="*.cpp" --include="*.h" --include="*.toml" # CloudXR / XRCloudXRBindings grep -rn "CloudXR\|XRCloudXRBindings\|IOpenXRRuntime" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093319
include="*.cpp" --include="*.h" # === Stage 4 (109→110) === # CARB_CHECK (replaced by CARB_RELEASE_ASSERT) grep -rn "CARB_CHECK" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093320
include="*.cpp" --include="*.h" # carb/Defines.h (split into sub-headers) grep -rn '#include.*carb/Defines\.h' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093321
include="*.cpp" --include="*.h" # IFileSystem raw char* methods grep -rn "IFileSystem" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093322
include="*.cpp" --include="*.h" # ITokens (unsafe methods removed; ITokens 2.0 available) grep -rn "ITokens\|->resolveString\|->setValue" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093323
include="*.cpp" --include="*.h" # optional / expected — semantics changed (if(b) now tests presence) grep -rn "optional \|expected **Important:** Also scan `templates/`, `launcher-configs/`, and any ETM lock files (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093324
`omni.all.template.extensions.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093325
These contain real dependency declarations and will cause test or runtime failures if they reference removed extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093326
```bash # === All stages — removed/deprecated extensions === # Kit 108 removals grep -rn "omni\.kit\.extpath\.git" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093327
include="*.toml" --include="*.kit" # Kit 108 — monolithic livestream (split into modules) grep -rn '"omni\.kit\.livestream"' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093328
include="*.toml" --include="*.kit" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093329
include="*.toml" --include="*.kit" # Kit 110 removals (cause cryptic exit-55 dependency solver failures) for ext in omni.kvdb omni.localcache omni.genproc.core; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093330
include="*.kit" --include="*.toml" done # Kit 110 silently removed (no deprecation notice) for ext in "omni.hydra.iray.shadercache.d3d12" "omni.hydra.iray.shadercache.vulkan" "omni.kit.viewport.iray"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093331
include="*.kit" --include="*.toml" done # Deprecated (not yet removed — still operational but plan migration) for ext in "omni.command.usd" "omni.debugdraw" "omni.hydra.iray" "omni.iray.settings.core" \ "omni.kit.autocapture" "omni.kit.manipulator.viewport" "omni.hydra.scene_api" \ "omni.renderer_capture" "omni.surface_instancer" "omni.kit.viewport.legacy_gizmos" \ "omni.kit.widget.nucleus_connector"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093332
include="*.kit" --include="*.toml" done # Extensions that need explicit declaration (no longer loaded transitively) grep -rn "omni\.kit\.manipulator\.prim\.fabric\|omni\.resourcemonitor\|omni\.kit\.ui" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093333
\ --include="*.py" --include="*.toml" ``` ### Config Files ```bash # Extension registry URLs (must update for Kit 110) grep -rn "kit-extensions\.ov\.nvidia\.com\|omniverse://" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093334
include="*.kit" # Build system (VS version) — also check CI-scoped token overrides # (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093335
"token:in_ci==true".vs_version may override the default even when the top-level is correct) grep -rn "vs_version\|vs2019\|vs2017\|v142" repo.toml # Livestream settings (old path style) grep -rn "app/livestream" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093336
include="*.kit" --include="*.toml" # Kit SDK version pin (use the $DEPS_DIR detected in Step 1) cat "$DEPS_DIR/kit-sdk.packman.xml" # mergeMaterials (behavioral default change in 109) grep -rn "mergeMaterials" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093337
include="*.kit" --include="*.toml" # FSD / Fabric Scene Delegate settings grep -rn "FabricSceneDelegate\|fsd\b" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093338
include="*.kit" --include="*.toml" ``` ### OmniGraph ```bash # === Stage 2 (107→108) — OmniGraph 3.0 ABI === grep -rn "omni\.graph\.core\|omni\.graph\.nodes" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093339
include="*.toml" # === Stage 4 (109→110) — deprecated/removed OmniGraph nodes === # DeformedPointsToHydra — removed (was part of OmniHydra) grep -rn "DeformedPointsToHydra" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093340
include="*.py" --include="*.usd" --include="*.usda" # OnCustomEvent bundle attributes deprecated grep -rn "OnCustomEvent" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093341
include="*.py" --include="*.usd" --include="*.usda" # Bundle/attribute manipulation nodes deprecated grep -rn "ArrayGetSize\|AttributeType\|BundleConstructor\|CopyAttribute\|ExtractPrim\|GetAttributeNames\|HasAttribute\|InsertAttribute\|RemoveAttribute\|RenameAttribute" \ .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093342
include="*.py" --include="*.usd" --include="*.usda" # Event/render pipeline nodes deprecated grep -rn "UpdateTickEvent\|GpuInteropCudaEntry\|RenderPreprocessEntry\|RpResourceExample" \ .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093343
include="*.py" --include="*.usd" --include="*.usda" ``` ### Isaac Sim Projects If the project uses Isaac Sim extensions, scan for the `omni.isaac.*` namespace migration (applies Kit 107+): ```bash # omni.isaac.* imports (deprecated → isaacsim.*) grep -rn "omni\.isaac\." .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093344
include="*.py" --include="*.toml" --include="*.kit" # omni.replicator.isaac (→ isaacsim.replicator.*) grep -rn "omni\.replicator\.isaac" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093345
include="*.py" --include="*.toml" # Dynamic Control Toolbox (removed as compile-time dep) grep -rn "dynamic_control\|DynamicControl" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093346
include="*.py" --include="*.cpp" --include="*.h" # SemanticsAPI (→ UsdSemantics.LabelsAPI) grep -rn "add_update_semantics\|SemanticsAPI" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 093347
Step 2.5: Update the Build Toolchain (highest-impact — often the real work) > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093348
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093349
Run this **before** touching source code — for a within-major / feature→production bump it is usually the *only* substantive work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093350
> **Key principle:** the most valuable part of an upgrade is usually **not** the code changes — it is making sure the project's **tooling** is correctly updated (repo scripts, `repo_man`/repoman, dependency versions).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093351
This step is therefore **first-class for every upgrade**, and the *primary* step for within-major / branch-transition bumps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093352
Run it **before** touching source code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093353
Why it matters:** the Kit kernel pin and the repo toolchain are coupled.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093354
Bumping `kit-sdk.packman.xml` alone frequently fails because packman tokens (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093355
`${platform_target_abi}`) only resolve under the matching `repo_man`, and newer kernels expect newer `repo_build` / `repo_kit_tools`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093356
A pin bump *without* a toolchain bump produces cryptic pull/resolve failures — e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093357
`Package not found ...gl.linux-x86_64` or `No versions of … = `.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093358
The toolchain = these files** (see `../references/toolchain.json`): - `$DEPS_DIR/repo-deps.packman.xml` — the `repo_*` tools: `repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_tools_internal`, `repo_kit_template`, `repo_usd`, `repo_format`, `repo_test`, `repo_package`, `repo_ci`, etc.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093359
`$DEPS_DIR/kit-sdk.packman.xml` — the kit-kernel pin (updated in Step 5, item 2 — see `apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093360
`tools/packman/` — the packman bootstrap (`packman`, `packman.cmd`, `bootstrap/`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093361
`repo.sh` / `repo.bat` — the repo wrappers (may need regenerating under a newer `repo_man`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093362
`repo.toml` — build config (VS/MSVC/WinSDK for Stage 4; see `../references/config_changes.json`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093363
How to find the correct target versions — do NOT guess:** 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093364
Get a **reference project already on the target Kit version** — the matching `kit-app-template` or `kit-sdk-public` branch for that Kit line, or the target Kit SDK release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093365
Read its `repo-deps.packman.xml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093366
Prefer the `production/ ` branch** — it carries the vetted, most-current toolchain for that release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093367
⚠️ **Toolchain versions track the branch's maintenance cadence, not the kernel number** — a newer kernel line can ship an *older* toolchain (in kit-sdk-public, `feature/main` pins kernel 110.4 with `repo_man` 2.6.4, while the maintained `production/110.1` pins kernel 110.1.3 with a *newer* `repo_man` 2.9.3).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093368
Always read the target branch's **actual** pins; never assume "newer Kit = newer tools".
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093369
(Those version numbers are an illustrative snapshot read in 2026 — they **will** go stale; verify against the live branch, do not copy them.)* 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093370
Diff** the project's `$DEPS_DIR/repo-deps.packman.xml` against the reference and align each `repo_*` tool `version=` to the reference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093371
Do the same for `tools/packman/` if it differs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093372
Apply the versions, then do a **clean rebuild** (Step 6 — see `validate.md`) — the toolchain bump must land before the kernel pin resolves cleanly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093373
> This step is safe to run and validate (Step 6) **on its own, first**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093374
Many "the upgrade won't build" error loops are nothing more than a stale toolchain — fixing it up front avoids chasing phantom code errors.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 093375
Failure Mode Diagnosis > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093376
Use this when the user has **already** upgraded and has a specific error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093377
`$DEPS_DIR` / `$BUILD` refer to the values detected in Step 1 (in `../SKILL.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093378
Exit Code 55 (Dependency Solver Failure) **Cause:** Removed extension still declared as a dependency, or stale extscache.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093379
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093380
Search for removed extension names in `.kit` and `extension.toml` files (see `../references/removed_extensions.json`) 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093381
For Kit 110: check for `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.*`, `omni.kit.viewport.iray` 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093382
Re-run `precache_exts` ### Build Fails with Undefined Symbol / Missing Method **Cause:** ABI break — extension was compiled against an older version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093383
Fix:** Recompile the extension against the current Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093384
Every stage has at least one ABI break.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093385
Runtime Crash on DLL Load (Windows) **Cause after Stage 3:** mimalloc cross-DLL heap mismatch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093386
Memory allocated on one side of a DLL boundary freed on the other.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093387
Fix:** Audit allocation ownership.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093388
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093389
Python TypeError: unexpected keyword argument 'menu_compatibility' **Cause (Stage 4):** `menu_compatibility` parameter removed from `ui.Menu` and `ui.Separator`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093390
Fix:** Remove the `menu_compatibility=` argument from all call sites.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093391
Extension Loads But APIs Return None / AttributeError **Cause:** Transitive loading of `omni.kit.ui`, `omni.resourcemonitor`, or `omni.kit.manipulator.prim.fabric` was removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093392
Fix:** Add explicit dependency in `extension.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093393
Render Output Differs (No Code Changes) **Cause after Stage 3:** DomeLight orientation changed (USD 25.05), FSD enabled by default, or `mergeMaterials` default changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093394
Diagnosis:** - Check for DomeLights in the scene: `grep -rn "DomeLight" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093395
include="*.usd" --include="*.usda"` - Check FSD setting: `grep -rn "FabricSceneDelegate\|fsd" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093396
include="*.kit" --include="*.toml"` - Check `mergeMaterials`: `grep -rn "mergeMaterials" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093397
include="*.kit" --include="*.toml"` ### if (optional_bool) No Longer Works (C++) **Cause (Stage 4):** `optional ` / `expected ` now tests for *presence* in an if-condition, not the stored value.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093398
Fix:** Replace `if (b)` with `if (b.has_value() && b.value())` ### Build Fails in a Loop / the Same Error Repeats **Cause:** Almost always a **stale toolchain** (Step 2.5 not applied — see `toolchain.md`) or a wrong assumption about the project's layout/build system — *not* the source code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093399
Rule — do not keep editing source and rebuilding.** If the same build error recurs after **2 attempts**, STOP and re-check the fundamentals before changing any more code: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093400
Is the **toolchain** aligned to the target Kit line?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093401
(Step 2.5, `toolchain.md` — the #1 cause of build loops.) 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093402
Is `$DEPS_DIR` the **actual** deps location and `$BUILD` the project's **actual** build entrypoint?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093403
(Step 1 in `../SKILL.md`.) 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093404
Did you do a **clean** rebuild (`$BUILD build --rebuild -r`), not just clear extscache?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093405
(Step 6, `validate.md`.) Surface the exact error and these three checks to the user rather than looping — repeated speculative edits burn tokens and rarely fix a toolchain/layout problem.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093406
Project Uses a Custom / Integrated Build System **Cause:** The project wraps or embeds the Kit build system in its own tooling, so `./repo.sh` / `repo.bat` don't exist or aren't the real entrypoint (common for customer integrations).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093407
Fix:** Do **not** fabricate `./repo.sh` commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093408
Use the `$BUILD` detected in Step 1 (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or ask the user).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093409
The upgrade steps (kernel pin, **toolchain update**, lock regen) still apply — invoke them through `$BUILD`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093410
deps Directory Not Where Expected **Cause:** The project layout differs from the SDK template, or the deps directory moved between releases (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093411
`deps/` at the project root vs under `tools/`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093412
Fix:** Re-run the Step 1 detection (in `../SKILL.md`) to set `$DEPS_DIR`, then use it everywhere.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093413
Never hardcode `tools/deps/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093414
Important Notes by Stage > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093415
Per-stage reference for the breaking changes summarized in the Step 2 migration table.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093416
Read the stages that apply to the boundaries you cross.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093417
Stage 1: 106 → 107 - **Rebuild required** — Linux ABI changed (`_GLIBCXX_USE_CXX11_ABI=0` → `=1`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093418
All prebuilt `.so` files will fail to load.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093419
packman XML token**: Update the kit-kernel pin token to `${platform_target_abi}` in all `.packman.xml` files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093420
Kit 106 uses the **`${platform}`** form (not `${platform_target}`); both must become `${platform_target_abi}`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093421
Build-verified:* leaving the old token makes the kit-kernel pull fail immediately with `Package not found on specified remote servers (…gl.linux-x86_64.release)`, because Kit 107's kernel is published only under the ABI string (`manylinux_2_35_x86_64`), not `linux-x86_64`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093422
Bump the repo toolchain too (required, easy to miss)** — see **Step 2.5** (`toolchain.md`): the token fix alone is **insufficient** — `${platform_target_abi}` only resolves to the ABI string under the newer `repo_man`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093423
Update `$DEPS_DIR/repo-deps.packman.xml` to the 107-era tooling (`repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_template`, `repo_usd`) and the packman bootstrap.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093424
Build-verified:* under 106.5's `repo_man` 1.86.0 the token still resolves to `linux-x86_64`; after the toolchain bump it resolves to `manylinux_2_35_x86_64` and the pull succeeds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093425
Carbonite Events 2.0**: The event system changed from push/pump to dispatch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093426
No explicit pump calls needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093427
Python payload access changed from `e.payload['key']` to `e['key']`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093428
C++17 is now available** explicitly in Premake via `cppdialect = "C++17"`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093429
Stage 2: 107 → 108 - **Kit 108 was never publicly released.** These changes still apply when upgrading 107→109.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093430
Python 3.12** replaces 3.11.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093431
Update all Premake configs, CI configs, and boost_python links.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093432
OpenUSD 25.02**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093433
GfMatrix imprecise overloads removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093434
Livestream modularization**: `omni.kit.livestream` (monolithic) → `omni.kit.livestream.app` + `.aov` + `.core`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093435
`omni.services.livestream.nvcf` → `omni.services.livestream.session`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093436
Settings paths changed — see `../references/config_changes.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093437
Transitive deps removed**: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` must now be declared explicitly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093438
ILayers ABI 1.0 → 1.1**: Recompile all extensions including `ILayers.h`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093439
USD scalar xform ops**: OpenUSD now supports scalar ops (e.g., `xformOp:translateX`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093440
Code iterating over xform ops that assumes all are vector types may behave incorrectly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093441
Stage 3: 108 → 109 - **CUDA 12.4.1 driver requirement**: Linux minimum 550.54.15, Windows minimum 551.78.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093442
Apps fail to start with older drivers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093443
NumPy 2.x**: Many breaking changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093444
On Windows, the default integer type changed from `int32` to `int64` — can cause silent correctness issues.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093445
Fabric ABI break**: Even if no source changes needed (no TokenC/PathC usage), all extensions including Fabric headers must recompile — `Token`/`Path` became trivially copyable, which is a binary ABI change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093446
Use `token.isNull()` instead of `kUninitializedToken`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093447
mimalloc (Windows)**: Cross-DLL allocation/free pairs that cross a DLL boundary may now crash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093448
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093449
mergeMaterials**: Default changed — can cause significant load time regression with no code error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093450
FSD default on**: If previously disabled FSD, test render output carefully.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093451
DomeLight orientation**: USD 25.05 changed the default orientation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093452
Visual change only — no code error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093453
Use `UpgradeUsdLuxLightsCommand` for assisted migration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093454
Stage 4: 109 → 110 - **Clear extscache first** — stale Kit 109 entries cause exit-55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093455
Silent extension removals**: `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.d3d12`, `omni.hydra.iray.shadercache.vulkan`, `omni.kit.viewport.iray` — all removed with no deprecation notice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093456
First symptom is a cryptic exit-55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093457
Remove every reference from `.kit`/`extension.toml` files — including the auto-generated `[settings.app.exts] enabled = [...]` version-lock block, where they usually hide pinned at the old version (clearing extscache alone won't drop them; regenerate the lock with `precache_exts` — see Step 5, item 5 in `apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093458
Also scan `templates/` and ETM lock files** — these are easily missed by `source/`-only scans.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093459
DomeLight orientation (inherited from Stage 3)**: If the project contains DomeLights and was not verified during a previous Stage 3 upgrade, the USD 25.05 orientation change is a permanent behavioral difference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093460
Search with `grep -rn 'DomeLight' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093461
include='*.py' --include='*.usd'` and use `UpgradeUsdLuxLightsCommand` if scenes were not migrated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093462
`optional ` semantics**: `if(b)` now tests *presence*, not *value*.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093463
Code that previously worked may now be wrong silently.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093464
`g_carbClientName`**: Type changed to `zstring_view`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093465
Any direct string assignment or comparison breaks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093466
Hydra 2 removed**: No migration path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093467
Hydra 1 (Storm) and RTX remain.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093468
OmniGraph bundle nodes**: Large set of bundle/attribute manipulation nodes deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093469
Deprecation warnings visible in editor from Kit 110.1+.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093470
`AttributeType` → `GetAttributeType`, `ArrayGetSize` → `ArrayLength`, `ExtractPrim` → `ReadPrim`, `GetAttributeNames` → `ReadPrimAttributes`, `InsertAttribute` → `WritePrimAttribute`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093471
`BundleConstructor`, `RemoveAttribute`, `RenameAttribute` have no direct replacement — redesign graphs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093472
OpenUSD 25.11**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093473
Ndr/Sdr libraries consolidated — update include paths.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093474
VS2022 required** on Windows (was VS2019).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093475
New extensions in Kit 110**: `omni.grpc.lib`, `omni.protobuf.lib`, `omni.sensors.nv.*` (camera/lidar/radar/ultrasonic/ids/wpm), `omni.kit.xr.core` — available for use in Kit 110 apps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093476
Step 6: Validate > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 093477
Assumes Step 1 detection has run (`$BUILD` is set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 093478
```bash # After a kit-kernel pin bump, do a CLEAN rebuild so the kernel symlinks refresh, # then regenerate the version lock against the new kernel.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 093479
$BUILD is the entrypoint detected in Step 1 (./repo.sh, repo.bat, or the project's own build wrapper).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 093480
`No versions of > omni.anim.curve.core … = `).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 093481
Use **`$BUILD build --clean`** (removes the build-time `_*` > folders so the next `build -r` refreshes the symlinks) or **`$BUILD build --rebuild -r`** (clean + > release build in one command), then regenerate the lock with `build -u`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 093482
The generated `[settings.app.exts] > enabled = [...]` block in each `.kit` is what must be regenerated — it carries exact old-version pins that > `extscache` clearing does not touch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 093483
Step 5: Apply Fixes > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093484
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093485
> **Within-major / feature→production upgrade?** Run **only items 1, 2, 8** below (plus item 3 *if* a feature↔production registry swap is needed), then Step 6 (`validate.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093486
Skip items 4–7** — they apply only when a major boundary is crossed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093487
See "Within-major upgrades" under Step 2 in `../SKILL.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093488
Get user approval before modifying files.** Then apply in this order (a full major-boundary upgrade runs all eight): 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093489
Clear extscache** first: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093490
Update version pin** in `$DEPS_DIR/kit-sdk.packman.xml` 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093491
Update registry URLs** in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093492
Replace deprecated APIs** using patterns in `../references/api_replacements.json` — these are safe regex replacements 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093493
Remove deprecated extension deps** from `extension.toml` and `.kit` files (see `../references/removed_extensions.json`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093494
For 109→110 specifically:** the following six extensions are removed with **no deprecation notice**, and any lingering reference causes a cryptic `exit code 55` dependency-solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093495
They MUST be removed from every `.kit` (and `extension.toml`) file: - `omni.kvdb` - `omni.localcache` - `omni.genproc.core` - `omni.hydra.iray.shadercache.d3d12` - `omni.hydra.iray.shadercache.vulkan` - `omni.kit.viewport.iray` ⚠️ **Check the generated version-lock block, not just `[dependencies]`.** In application `.kit` files these names almost always appear in the auto-generated `[settings.app.exts] enabled = [...]` lock (pinned at the old version, e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093496
`omni.kvdb-109.0.10`), **not** the hand-authored dependency list.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093497
Clearing extscache (step 1) does NOT remove them** — you must regenerate the lock: delete the `# BEGIN GENERATED PART` … `# END GENERATED PART` block (the `.kit` says "Remove from 'BEGIN' to 'END' to regenerate") and run `$BUILD precache_exts -c release` so it is rebuilt without the removed extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093498
Then confirm a clean rebuild (the version stamp should advance to 110 and the six names should be gone).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093499
(If you are working in an internal `kit-app-template` checkout, the ETM lock file `templates/omni.all.template.extensions.kit` and any internal-registry entries are KAT-internal — wrapped in `# AUTOREMOVE` and stripped from external releases by `repo stage_for_github` — so external customer projects will not contain them.) 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093500
Add explicit deps** where transitive loading was removed: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093501
Update build config** in `repo.toml` (VS version, MSVC version, Windows SDK — see `../references/config_changes.json`) 8.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 093502
Step 4: Generate Upgrade Report > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093503
Run after the Step 3 scans (`scan.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093504
Present findings organized by severity.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093505
Use exact `file:line` references from scan output.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093506
``` ## Upgrade Report: Kit [FROM] → [TO] Project: [path] Migration stages applied: [e.g., Stage 2 + 3 + 4] ### ❌ Breaking Changes (must fix — build or load will fail) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093507
[file:line] — [description] → [exact fix] ### ⚠️ Behavioral Changes (no error, but may affect output or performance) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093508
[file:line] — [description] → [fix or test required] ### 🔔 Deprecated Usage (should fix — will break in next version) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093509
[file:line] — [description] → [fix] ### ✅ Not Affected - [List the `id` or `title` from `breaking_changes.json` for each pattern that was scanned and returned no matches.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093510
This serves as a record that the check was performed, not just skipped.] ### 📋 Required Steps Regardless of Code Changes 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093511
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093512
Update `kit-sdk.packman.xml`: change version pin to `[TO].x.y+feature.${platform_target_abi}.${config}` 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093513
Update extension registry URLs in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093514
Rebuild all C++ extensions (ABI break at every stage — required even with no source changes) 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093515
Regenerate version lock blocks in `.kit` files: `$BUILD precache_exts -c release` (substitute the build entrypoint detected in Step 1 — `./repo.sh` may not exist on a custom/integrated build) 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093516
If project has an ETM lock file (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093517
`omni.all.template.extensions.kit`), regenerate it or manually remove entries for removed extensions 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093518
[stage-specific items, e.g., VS2022 for Stage 4] ### 🧪 Behavioral Tests Required 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093519
[scenes with DomeLights — orientation regression (Stage 3, but inherited in all later stages)] 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093520
[load performance with mergeMaterials setting (Stage 3)] 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093521
[render output with FSD enabled (Stage 3)] 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093522
[MaterialX materials (Stage 4)] 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093523
[transform-heavy workflows after scalar xform ops change (Stage 2)] ``` **Prioritize for the user:** Extension removal errors and ABI rebuild requirements are the most common causes of project failures after a version bump.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 093524
Validate and hand off the image Always verify build completion and inspect the output image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093525
Runtime checks follow the developer's selected scope and the app's actual requirements.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093526
Choose applicable checks | Application and request | Runtime behavior | |---|---| | Containerization only | Do not launch the app/container for runtime validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093527
Report runtime checks not run by request.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093528
| | RTX rendering or streaming, validation selected | Use compatible GPU hardware, drivers, and container runtime support.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093529
Check the source app and exact built container separately.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093530
| | Non-rendering service or batch app, validation selected | Use supported CPU execution and the app's actual service-readiness or completion criteria.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093531
Non-streaming alone does not imply CPU-only.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093532
| | Requested runtime checks, suitable host unavailable | Preserve successful build/image inspection results and identify the requested checks that remain unverified.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093533
| GPU-free packaging support is based on inspected default tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093534
An actual successful GPU-free build provides execution evidence for that specific app, version, and environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093535
Do not generalize it to every custom app or historical version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093536
For selected GPU runtime checks, verify access inside a disposable container before starting Kit.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093537
Host `nvidia-smi` alone does not establish Docker GPU access.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093538
Use the host's configured mechanism: `--gpus all` with NVIDIA runtime support, or `--device nvidia.com/gpu=all` when Docker native CDI support is enabled and an NVIDIA CDI specification is available.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093539
Use the verified option in the runtime example below.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093540
See [Docker CDI configuration]( and [NVIDIA CDI support]( for the installed versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093541
Reuse working host configuration; runtime preparation does not require replacing it with a different mechanism.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093542
Test the exact image Capture the image ID after packaging, then use that ID for container execution.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093543
On another host, distribute the image through the requested mechanism and establish the resulting identity.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093544
Use a registry digest after publication when available; a Docker local image ID and registry manifest digest are different identifiers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093545
Choose a unique test-container name and bounded check duration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093546
Configure only the needed environment inputs, mounts, and ports from the selected app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093547
Preserve logs and container state before cleanup; remove only resources created for this check.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093548
The inspected `./repo.sh launch --container --name : ` is a convenience launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093549
It can fall back to another image when lookup fails, always requires NVIDIA hardware, and can discard the child process's failure status.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093550
Do not accept its completion as the success signal or use it for CPU-only validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093551
Prefer controlled Docker execution when proving the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093552
For an NVCF app with an HTTP readiness service on container port 8011, a minimal local GPU readiness check can use the following shape.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093553
First select a free host port, a unique name, the actual image ID, and any app-required runtime inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093554
Adjust ports/settings for the selected version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093555
These are examples, not default values to overwrite the developer's configuration with.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093556
```bash KIT_IMAGE_ID=$(docker image inspect --format '{{.Id}}' acme/viewer:0.1.0) KIT_CHECK_NAME=kit-container-check-unique docker run --detach --name "$KIT_CHECK_NAME" --gpus all -p 127.0.0.1:18011:8011 "$KIT_IMAGE_ID" docker inspect --format '{{.Image}} {{json .State}}' "$KIT_CHECK_NAME" docker logs "$KIT_CHECK_NAME" curl --fail --silent --show-error --max-time 10 ``` Ensure image lookup and container creation succeed before proceeding.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093557
Add the selected app's required GPU driver capabilities, mounts, and environment inputs as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093558
For CPU services, omit GPU options and use that service's configured check.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093559
A batch app needs its actual exit status and expected output rather than an HTTP probe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093560
A single probe immediately after launch is not a startup deadline.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093561
Poll within a chosen total limit, checking for early container exit and collecting logs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093562
A successful `docker run --detach` only confirms container creation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093563
Verify the container's `.Image`, actual state/exit status, and applicable readiness or completion result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093564
For a long-running app, require it to remain running while checking readiness; a stopped container with exit code 0 is not a healthy running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093565
Cold RTX startup can take several minutes for shader and driver pipeline preparation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093566
An initial HTTP 503 or an "app ready" log line alone does not decide the readiness result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093567
Allow for that preparation in the bounded check, observe progress, and record a timeout if the chosen deadline expires.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093568
After collecting evidence, stop and remove the specific test container if it is no longer needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093569
Record intentional test shutdown separately from an application crash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093570
A rebuild creates a new candidate and requires new image-specific runtime evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093571
NVCF readiness and downstream boundary When runtime validation is selected and the app exposes `omni.services.livestream.session`, check its configured readiness endpoint.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093572
The documented default is HTTP `/v1/streaming/ready` on port 8011, with a successful response indicating the service's readiness criteria.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093573
`/v1/streaming/startup` is not equivalent evidence of application/RTX readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093574
See the [session service documentation]( Keep these outcomes separate: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093575
Source app runs in its development environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093576
The packaged image runs and satisfies its app/container checks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093577
An NVCF deployment becomes ready with workers using the intended image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093578
The frontend connects and receives advancing decoded application frames.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093579
This skill handles the first two when requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093580
The latter two need the downstream deployment/client validation workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093581
Readiness-only local port mapping does not provide a complete external media/signaling path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093582
For the NVCF handoff, inspect actual settings and carry the required runtime input names and signaling/health configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093583
Documented defaults include function type `STREAMING`, signaling route `/sign_in` on 49100, and readiness on 8011.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093584
Derive values from the selected app/version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093585
Do not attach NVCF requirements to Kit App Streaming or non-streaming results.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093586
See [Deploying Kit Apps]( ## Optional publication Publish only when the request includes image distribution to a resolved registry destination.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093587
A registry-qualified image name alone does not request a push.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093588
Confirm missing registry/namespace details and use the available authenticated mechanism without exposing secret values or baking credentials into the image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093589
If publication needs an additional tag, preserve the developer's original local tag, identify the destination tag, and ensure it refers to the built image before pushing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093590
Do not silently choose a different repository or version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093591
Verify the successful push and capture the published URI and manifest digest when available.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093592
Report publication failures independently of local build success.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093593
A local image is not pullable by remote NVCF workers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093594
The deployment stage needs the published/distributed image identity and pull access for its cluster.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093595
This skill can supply the image when publication is requested; otherwise report that distribution remains to be arranged.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093596
Result format Return the following fields in a concise human-readable report.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093597
A caller may request a machine-readable contract; follow that actual contract rather than inventing a new required schema.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093598
| Field | Include | |---|---| | Requested outcome | Existing/new app, streaming target or headless behavior, containerization-only or selected runtime checks, requested publication.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093599
| | Source | Git URL/ref/commit and relevant local changes, or NGC resource/version/artifact identity; available provenance for a local project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093600
| | Versions | Kit, app, template and relevant build/package tools; resolved streaming extension versions or generated version-lock evidence; skill source/version separately.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093601
| | Application | Base app, selected layer/entrypoint, important configuration changes, required runtime input names and mounts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093602
| | Image | Exact requested reference, local ID, OS/architecture, and published URI/digest if publication occurred.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093603
| | Evidence | Build outcome/log location, image inspection, separate source-app and container runtime outcomes, exact identity tested, applicable readiness/exit evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093604
| | Remaining work | Checks not run and reasons, unresolved failures, and distribution/deployment/client validation still needed for downstream use.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093605
| Use `passed`, `failed`, `not run by request`, `not run because unavailable`, or `not applicable` for each stage as appropriate.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093606
Include stages only where they clarify the requested outcome.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093607
Preserve attempted failures rather than describing them as untested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093608
Build plus image inspection is sufficient for a containerization-only request.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093609
If runtime validation was requested but unavailable, state that the image is built while that requested validation remains incomplete.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093610
Do not claim NVCF deployment or end-to-end streaming success from local container readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 093611
Select and prepare the application Use the section matching the developer's starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093612
Source selection and app preparation happen in the application project, which can differ from the checkout containing this skill.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093613
License acceptance during preflight Identify required license acceptance while resolving the selected source and tool version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093614
Inspect that version's license notices or prompt implementation before starting generation or long-running builds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093615
Brief source/tool inspection may be needed to identify the terms; do not defer a known acceptance requirement until an unattended operation stops at a prompt.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093616
When acceptance is required and not already supplied, collect it together with the initial app/version/image/validation decisions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093617
Make the question explicit in the conversation, even when also using a structured question UI: - Explain which planned operation requires acceptance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093618
Name and link every agreement identified by the selected workflow, and state the project or runs the acceptance will cover.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093619
Quote the tool's prompt when it has been observed; do not invent a live prompt or claim work has stopped when this is preflight.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093620
Ask for an explicit yes or no, with an example reply.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093621
Explain that a yes authorizes answering the matching tool prompt on the developer's behalf.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093622
For example, when the selected workflow names the NVIDIA agreements below: > Before I generate this application and start the build, do you accept the [NVIDIA Software License Agreement]( and [Omniverse Product-Specific Terms]( and authorize me to answer Yes to the license prompt for this application?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093623
Reply "Yes, I accept" or "No." Use the selected version's agreements and URLs if they differ, and state the actual scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093624
One explicit acceptance can cover multiple planned runs using the same terms when those runs are named.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093625
Honor acceptance already supplied for that scope and use it when the matching tool prompt appears.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093626
Do not infer acceptance from silence or a general request to build, or bypass the tool's required response.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093627
If a later prompt presents different terms or scope, surface that difference before accepting.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093628
While awaiting an answer, continue only work that does not require acceptance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093629
Existing project Locate the intended project and inspect its instructions, working changes, build entrypoint, app definitions, and dependency configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093630
Common Kit App Template locations include: - `source/apps/` for base apps and layers, `source/extensions/` for project extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093631
`repo.toml` for build/packaging configuration, `repo_tools.toml` and `tools/deps/` for tool and SDK pins.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093632
`templates/templates.toml` and resolved template metadata for available template/layer operations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093633
Custom projects can use other layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093634
Follow their build registration and dependency precaching rather than introducing template metadata solely to fit this workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093635
Resolve the requested `.kit` file and its dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093636
Record the actual base app and selected layer.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093637
Inspect inherited settings and launcher behavior as well as the selected file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093638
A name ending in `_nvcf.kit` or `_streaming.kit` is a clue, not proof of the configured functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093639
Check whether the app has the dependencies, settings, build registration, and assets it needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093640
Prepare missing packaging or streaming configuration within the requested scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093641
If the app requires substantial implementation or migration before it can build, report that boundary and the specific blocker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093642
New project from GitHub Recommend [NVIDIA-Omniverse/kit-app-template]( `main`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093643
If the request does not choose a Kit version/ref, ask whether the developer wants that default or a specific version/ref.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093644
Inspect the public refs and selected source pins, then display the resolved Kit version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093645
Use a new directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093646
For the accepted default: ```bash git clone --branch main --single-branch my-kit-project cd my-kit-project git rev-parse HEAD ``` Choose the directory from the developer's workspace context.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093647
For another branch or tag, resolve that exact ref; for a commit, fetch and check out the resolved commit explicitly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093648
Do not apply `--branch` to a commit hash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093649
If a requested version is unavailable publicly, explain the available choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093650
Never substitute an internal checkout or edit only the Kit kernel pin to simulate a complete version change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093651
Inspect the selected checkout's dependency pins and CLI.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093652
The ordinary template flow is: ```bash ./repo.sh template new ``` Select the available app template based on the requested behavior, then resolve its app namespace/name, display name, app version, and any required extension inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093653
Do not silently reuse documentation example identities.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093654
Keep app version independent of the Kit version and container tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093655
Answer any required template license prompt using the acceptance established during preflight.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093656
If it presents different terms or scope, follow [license preflight](#license-acceptance-during-preflight) before proceeding.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093657
Use supported interactive input or the chosen tool's documented playback mechanism.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093658
In the inspected tooling, `template new --generate-playback ` records choices without creating the app; `template replay ` subsequently renders it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093659
Inspect help before using these options on another version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093660
A generated playback file alone is not an application.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093661
Legacy `--input` or `REPO_TEMPLATE_SCRIPT` mechanisms do not reliably handle checkbox layer selection; use the supported playback flow or interact with the actual prompts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093662
Streaming layers | Target | Preparation | |---|---| | Kit App Streaming | Reuse or add the selected version's ordinary streaming layer for local or self-managed streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093663
In the inspected Kit App Template this is the picker entry `[omni_default_streaming]: Omniverse Kit App Streaming (Default)`, which renders `{app_name}_streaming.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093664
| | NVCF | Reuse or add that version's NVCF layer, including its streaming/session-service dependencies and settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093665
Ordinary streaming alone is insufficient.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093666
In the inspected Kit App Template this is the picker entry `[nvcf_streaming]: NVCF Streaming`, which renders `{app_name}_nvcf.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093667
| | Non-streaming | Keep the intended headless app entrypoint; do not add streaming dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093668
Determine whether the app still requires GPU rendering.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093669
| For template-generated apps, select the layer during creation or use the available modify flow: ```bash ./repo.sh template modify ``` Inspect the app's template metadata before modifying it, commonly `source/rendered_template_metadata.json`, and the template's linked-layer definitions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093670
The inspected modify flow is interactive and can overwrite an already rendered layer when selected again.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093671
Reuse a correct existing layer; inspect custom edits before regenerating.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093672
Do not invent noninteractive `--app` or `--layer` flags.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093673
For a manually authored app without the required metadata, use the selected version's layer definitions as a reference and make only the necessary dependency/settings changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093674
Rebuild after adding or changing layers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093675
Select the actual generated layer as the packaging entrypoint, such as `acme.viewer_streaming.kit` for Kit App Streaming or `acme.viewer_nvcf.kit` for NVCF.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093676
Do not package the base desktop app merely because it has the same display name.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093677
Secondary route: NGC SDK Use this route when the developer chooses it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093678
If the developer is unsure, explain the two source routes and recommend public Kit App Template by default.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093679
Resolve the desired resource and version using the [Kit SDK catalog links in the manual]( Select the resource matching the requested release and platform; the collection linked by a latest guide may cover a different feature or production line.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093680
Follow that resource's download and extraction instructions using available authentication.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093681
Do not assume an NGC SDK resource is a runnable container image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093682
Record the resource organization/team/name, requested version, downloaded artifact identity/checksum, and detected SDK version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093683
Do not invent a Git commit for a downloaded SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093684
On Linux, when provided by that package, run `./new_project.sh` from the extracted SDK and resolve its project-location and license prompts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093685
Inspect the package's instructions if this entrypoint differs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093686
Enter the generated project, inspect its actual tool/SDK pins, and use the same app/layer workflow above.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093687
Keep the skill loaded from its complete folder if it is absent from that SDK release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093688
Record the selection Capture the source URL/ref/commit and relevant local changes for Git projects, or the NGC artifact provenance for downloaded SDKs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093689
For a local non-Git project, record the available provenance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093690
Record the skill's source/version separately, along with the resolved app, Kit, template, and build/package tool versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093691
Generated projects can resolve streaming extensions from a registry to versions newer than copies bundled in the SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093692
Record the versions resolved by the application or preserve its generated version locks with the build evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093693
Keep the selected SDK and Kit pins unless the developer requests a change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093694
Examples follow the [Kit app creation and containerization guide]( When the selected checkout differs from the latest guide, its actual configuration and supported CLI determine the commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 093695
Build and package the selected app Run from the resolved application project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093696
These command examples match the inspected `repo_kit_tools` 1.21.4 workflow; inspect the selected checkout's pins and help before using them with other tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093697
Establish the build environment The initial workflow uses Linux x86_64 artifacts, compatible Linux x86_64 execution, and Docker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093698
Check the actual build host and Docker daemon: ```bash uname -s uname -m docker version docker info ./repo.sh build --help ./repo.sh package_container --help ``` Check the project's documented compiler/dependency prerequisites, Docker daemon accessibility, artifact/package download access, and space for the build, staged copy, and image layers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093699
The selected base image and Dockerfile determine additional requirements.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093700
The inspected default Dockerfile needs a BuildKit frontend supporting `COPY --exclude` and its `# syntax=docker/dockerfile:1` directive.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093701
Native Windows packaging is rejected by this tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093702
A suitable WSL installation or a remote Linux builder can supply the required environment, but native Kit also runs during host-side extension trimming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093703
A Windows shell connected only to a remote Docker daemon does not move that step to Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093704
ARM, multiarch, and cross-build setups require a compatible Kit distribution, base image, and separately verified workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093705
GPU availability is a runtime decision, not a prerequisite for this inspected default packaging path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093706
Dependency precaching resolves extensions; it is not shader warmup.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093707
Inspect custom build hooks, trimming changes, and Dockerfiles before applying this conclusion to a customized project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093708
Check compatible GPUs/drivers and NVIDIA Container Toolkit only when GPU runtime checks are selected.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093709
Resolve app and image inputs Resolve a real source app/layer and its staged basename.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093710
Confirm that the intended `.kit` file and Kit executable exist after building.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093711
Check a separate launcher only when the selected project's workflow requires one.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093712
Stop to resolve missing paths, multiple matching apps, or duplicate basenames in nested app directories.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093713
Inspect `repo.toml` and existing `[repo_kit_package_container]` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093714
The tool can reduce an existing app path to its basename, and configuration lookup can distinguish `acme.viewer_nvcf` from `acme.viewer_nvcf.kit` before normalizing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093715
Reuse the matching configured entry with consistent naming rather than generating duplicate entries or passing a nonexistent path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093716
Require a valid, writable image repository plus explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093717
Examples: | Reference | Meaning | |---|---| | `acme/viewer:0.1.0` | Repository and explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093718
| | `registry.example.com:5000/acme/viewer:0.1.0` | Registry port and a separate explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093719
| | `registry.example.com:5000/acme/viewer` | Missing tag; the registry-port colon is not a version tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093720
| | `acme/viewer@sha256:...` | Existing-image digest identity, not a writable Docker build tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093721
| The inspected tool treats any colon in `--image-tag` as a complete-reference signal.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093722
Passing an untagged name can therefore change its interpretation or cause Docker to default to `latest`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093723
Resolve the name/tag first.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093724
Preserve the requested value instead of silently adding `latest`, changing the namespace, or replacing it with a generated app name.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093725
Before building, inspect whether the chosen local tag already exists and record its ID.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093726
Rebuilding that tag updates its local target; make that effect clear.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093727
A remote registry overwrite is a separate publication action.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093728
See [Docker image reference syntax]( ## Build and optional source-app check For the supported template workflow: ```bash ./repo.sh build --config release ``` Use the custom project's supported equivalent when needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093729
In the inspected build tool, `-c` means clean and exit, not configuration; use the long `--config` option.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093730
Verify command success, dependency resolution, and the selected app artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093731
Inspect the configured build root rather than assuming one path for every project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093732
If requested and supported by the host, run the source app and collect actual exit/readiness/log evidence before packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093733
The convenience `./repo.sh launch` command can guide app selection, but its return alone is not proof of runtime success.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093734
A non-rendering CPU service can need direct invocation through its own launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093735
If runtime checks were declined, continue with packaging and record that choice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093736
Container configuration and packaging Reuse existing valid Dockerfile and entrypoint configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093737
For supported projects without configuration, `package_container` can generate a container template/configuration when supplied a valid app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093738
Inspect the files it creates.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093739
Explicit generation is also available in the inspected version: ```bash ./repo.sh package_container --app acme.viewer_nvcf.kit --generate ``` This generates configuration in the default project `tools/containers` location; it is not a completed image build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093740
If specifying a destination in this tool version, use an absolute path inside the project because configuration injection computes a path relative to the absolute project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093741
Inspect the selected version's help before using it, and do not regenerate customized files without examining them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093742
Generation does not overwrite existing files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093743
In the inspected tool, both `--generate` and the `auto_generate` configuration path skip any destination file that already exists, log a warning, and continue, so an existing `tools/containers/Dockerfile` keeps its current `FROM` line after the tool's bundled default changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093744
Compare that `FROM` line with the Dockerfile bundled in the pinned `repo_kit_tools` package (`omni/repo/kit_tools/package/data/Dockerfile`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093745
The inspected 1.21.4 default is `nvcr.io/nvidia/omniverse/ov-base-ubuntu22-x86_64:1.0.0`; the default before 1.21.4 was `nvcr.io/nvidia/omniverse/ov-base-ubuntu-22:2026.2.3`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093746
When they differ, update deliberately: delete `tools/containers/Dockerfile` (and `entrypoint.sh` if it should also be refreshed) and rerun `--generate`, or edit the `FROM` line in place and keep the customized content.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093747
Regeneration leaves an existing `repo.toml` container entry for that app unchanged.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093748
Record the base image actually used in the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093749
Substitute the resolved app name and full image reference in the build command: ```bash ./repo.sh package_container --app acme.viewer_nvcf.kit --image-tag acme/viewer:0.1.0 --config release ``` The tool stages build artifacts, optionally precaches dependencies, trims unused extensions, and invokes Docker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093750
Do not substitute historical `package --container`, `--target-app`, or container `--name` arguments without evidence that the selected version requires them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093751
There is no shader-cache bypass or dry-run flag in this inspected container tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093752
Use `--from-package` only when deliberately using a compatible packaged artifact.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093753
It is a boolean switch, not an archive-path argument; inspect both its configured archive pattern and post-unpack commands for compatibility with the selected public or private source.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093754
Inspect custom runtime-loaded dependencies and assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093755
The inspected tool supports repeatable `--extra-ext` and `extra_extensions` configuration to keep needed extensions/apps through precache and trimming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093756
Use it only for identified dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093757
If local assets, credentials, caches, or cloud inputs are expected at runtime, identify their mounts or input names instead of silently treating the developer machine's state as part of the image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093758
The default entrypoint runs Kit directly with `--no-window`, rather than invoking a custom app shell launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093759
Account for required environment/setup/arguments.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093760
Desktop display integration or substantial custom launcher behavior requires its own adaptation and validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093761
Verify the produced image After a successful packaging command, inspect the exact requested reference: ```bash docker image inspect acme/viewer:0.1.0 docker image inspect --format '{{.Id}}' acme/viewer:0.1.0 ``` Record its full local ID, repository tags, OS/architecture, configured entrypoint/command, and relevant app metadata.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093762
The default Dockerfile labels images with `kit_app_template`; match that label and the rendered entrypoint/configuration to the selected app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093763
A label alone is insufficient if a custom Dockerfile changes behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093764
Bind the result to the current successful build and its logs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093765
An unchanged image ID can be legitimate when Docker reuses identical content.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093766
Neither an existing tag after a failed build nor a different ID without successful build evidence proves completion.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093767
Keep full metadata/logs private when they contain environment values, and include only necessary non-secret evidence in the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093768
Continue with [validation and handoff](validation-and-handoff.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093769
Diagnose common failures | Observation | Next check | |---|---| | Command or option is unavailable | Inspect the selected tool pin, help, and project configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093770
Do not upgrade the project just to match these examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093771
| | App missing or multiple matches | Resolve the real source/staged app and consistent config name before retrying.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093772
| | Dependencies cannot resolve | Check selected-version extension pins, registry access, and build/precaching configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093773
Avoid a global cache purge.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093774
| | An app works outside the container but lacks an extension inside it | Inspect trimming and runtime-loaded dependencies; preserve identified extras through supported configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093775
| | Dockerfile parse failure around `COPY --exclude` | Inspect BuildKit/frontend compatibility and the syntax directive, especially in custom Dockerfiles.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093776
| | Native executable or architecture failure | Verify Linux x86_64 artifacts, host execution environment, and base image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093777
Remote Docker alone does not solve native host execution.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093778
| | Stale staging is demonstrated | Use the selected tool's scoped staging-clean option only after checking its target.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093779
Avoid deleting unrelated builds or Docker caches.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093780
| | Docker image exists after an error | Preserve the failed result and distinguish the old tag/image from the attempted build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093781
| Use [container tool documentation]( alongside the selected tool's implementation and configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 093782
tomlkit==0.12.2 ; python_version >= "3.10" and python_version < "4.0" \ --hash=sha256:df32fab589a81f0d7dc525a4267b6d7a64ee99619cbd1eeb0fae32c1dd426977 \ --hash=sha256:eeea7ac7563faeab0a1ed8fe12c2e5a51c61f933f2502f7e9db0241a65163ad0
स्रोत: NVIDIA-Omniverse/kit-app-template:tools/repoman/requirements.txt · स्वतंत्र परीक्षण अपेक्षित।

## 093783
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093784
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093785
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093786
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093787
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093788
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093789
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093790
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093791
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093792
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093793
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093794
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093795
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093796
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093797
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093798
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093799
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093800
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093801
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093802
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093803
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093804
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093805
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093806
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093807
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093808
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093809
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093810
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093811
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093812
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093813
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093814
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093815
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093816
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093817
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093818
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093819
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093820
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093821
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093822
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093823
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093824
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093825
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093826
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093827
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093828
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093829
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093830
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093831
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093832
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093833
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093834
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093835
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093836
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093837
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093838
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093839
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093840
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093841
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093842
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093843
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093844
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093845
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093846
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093847
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093848
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093849
:warning: **Important**: These layers are not standalone application templates.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093850
They must be used in conjunction with a base application template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093851
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093852
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093853
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093854
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093855
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093856
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093857
Collaborating on large-scale design projects in real-time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093858
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093859
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093860
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093861
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093862
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093863
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093864
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093865
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093866
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093867
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093868
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093869
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093870
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093871
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093872
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093873
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093874
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093875
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093876
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093877
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093878
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093879
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093880
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093881
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093882
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093883
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093884
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093885
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093886
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093887
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093888
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093889
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093890
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093891
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093892
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093893
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093894
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093895
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093896
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093897
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093898
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093899
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093900
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093901
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093902
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093903
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093904
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093905
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093906
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093907
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093908
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093909
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093910
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093911
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093912
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093913
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093914
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093915
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093916
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093917
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093918
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093919
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093920
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093921
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093922
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093923
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093924
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093925
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093926
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093927
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093928
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093929
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093930
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093931
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093932
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093933
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093934
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093935
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093936
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093937
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093938
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093939
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093940
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093941
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093942
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093943
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093944
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093945
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093946
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093947
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093948
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093949
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093950
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093951
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093952
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093953
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093954
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093955
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093956
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093957
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093958
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093959
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093960
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093961
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093962
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093963
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093964
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093965
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093966
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093967
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093968
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093969
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093970
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093971
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093972
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093973
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093974
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093975
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093976
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093977
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093978
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093979
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093980
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093981
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093982
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093983
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093984
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093985
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093986
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093987
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093988
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093989
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093990
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093991
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093992
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093993
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093994
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093995
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093996
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093997
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093998
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 093999
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 094000
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।
