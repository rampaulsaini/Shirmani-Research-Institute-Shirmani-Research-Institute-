# डिजिटल महाग्रंथ 023

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 022001
Containerize a Kit application Produce the developer's requested container image from the selected Kit app, and report what was built and verified.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022002
Prefer the existing application.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022003
For a new application, recommend the public [Kit App Template]( on `main`; offer another Kit version/ref when requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022004
NGC SDK download is a secondary route.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022005
Resolve the developer's intent Inspect the request, orchestration context, and project before asking questions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022006
Ask only for missing decisions that affect the work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022007
| Decision | Action | |---|---| | Existing application or new application?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022008
| Locate the existing project and intended app, even if it needs preparation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022009
For a new app, resolve the template and required app name, display name, and app version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022010
| | Streaming from the container?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022011
| Determine Kit App Streaming versus NVCF.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022012
In the inspected Kit App Template layer picker, Kit App Streaming is `[omni_default_streaming]: Omniverse Kit App Streaming (Default)` and renders `{app_name}_streaming.kit`; NVCF is `[nvcf_streaming]: NVCF Streaming` and renders `{app_name}_nvcf.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022013
Check whether the appropriate layer already exists.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022014
For non-streaming use, establish the intended headless service, batch, or rendering behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022015
| | Which Kit version?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022016
| For a new app without a specified version, ask whether to use public GitHub `main` or another Kit version/ref.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022017
Recommend `main` and show its resolved Kit version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022018
For an existing app, report and preserve its version unless a change is requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022019
| | What image name and tag?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022020
| Resolve the full image repository/name and explicit version tag, including any registry/namespace.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022021
Preserve supplied values.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022022
Kit version, app version, and container tag are separate choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022023
| | What runtime validation?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022024
| Recommend running RTX apps on a compatible RTX GPU before packaging and checking the built container afterward.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022025
Allow containerization only, even when a GPU is present.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022026
Offer applicable CPU checks for non-rendering services.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022027
| | Required license acceptance?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022028
| Identify the selected workflow's applicable terms early.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022029
When acceptance is required and not already supplied, collect it with the initial preflight questions before generation or long-running builds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022030
Follow [license preflight](references/app-preparation.md#license-acceptance-during-preflight).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022031
| An existing app without streaming layers stays on the existing-app path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022032
Ordinary streaming configuration does not establish NVCF readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022033
If multiple apps or layers fit the request, resolve the selection before modifying files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022034
Prepare the selected app Read [app preparation](references/app-preparation.md) for the applicable existing-app, new-project, or NGC route.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022035
Resolve the project, source ref/artifact, Kit and tool versions, exact app/layer, and target platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022036
Inspect the developer project's pins, rather than assuming the toolchain of a different repository or the latest documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022037
Reuse the app and correct streaming layer, or generate only the missing app/layer/configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022038
Inspect dependencies and settings as well as template metadata.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022039
Preserve custom work; substantial application repair or a Kit migration needs its own scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022040
Establish a compatible Linux x86_64 build environment and Docker access for the initial workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022041
Native Windows packaging is unsupported by the inspected tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022042
A suitable WSL or remote Linux environment must execute the native Kit packaging steps, not just host a Docker daemon.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022043
The standard inspected pipeline can build/package without RTX rendering.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022044
Custom hooks or Dockerfiles can add GPU requirements.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022045
Runtime rendering/streaming needs compatible GPU resources.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022046
Extension dependency precaching is not shader warmup.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022047
Do not claim an unexecuted GPU-free build succeeded.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022048
Build and package Read [container workflow](references/container-workflow.md) before packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022049
It covers the actual CLI, app/config matching, image references, and common failures.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022050
Build with the selected project's supported release workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022051
Confirm dependencies and the selected app artifacts are present.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022052
Perform source-app runtime validation when selected and available.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022053
Record it separately from container validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022054
Resolve a real, unique staged app and a writable `repository:explicit-tag`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022055
Reuse matching container configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022056
Inspect an existing target tag before replacing it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022057
Package with the selected tool's supported arguments.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022058
The inspected command is `./repo.sh package_container --app --image-tag : --config release`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022059
Inspect the resulting image ID, requested tag, architecture, app label/configuration, entrypoint, and required runtime inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022060
An old image with the same tag is not evidence of a successful build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022061
The default entrypoint uses `--no-window` and invokes Kit directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022062
It does not automatically retain a custom shell launcher's setup or provide a desktop display.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022063
Inspect those requirements before promising equivalent behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022064
Diagnose failures, make a bounded correction supported by the evidence, and repeat affected steps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022065
Report unresolved blockers rather than repeatedly rebuilding unchanged inputs, broadly cleaning the environment, or silently changing Kit versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022066
Validate and hand off Read [validation and handoff](references/validation-and-handoff.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022067
Always inspect the build result and image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022068
Run only the runtime checks selected by the developer, against the exact built image ID or published digest.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022069
| Outcome | Report | |---|---| | Build and image inspection succeed; containerization only requested | Complete.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022070
Runtime validation not run by request.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022071
| | Runtime validation requested and passes | Complete for the checks actually performed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022072
| | Build succeeds but requested runtime checks cannot run | Image built; requested validation remains unverified, with the reason.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022073
| | A build or runtime check fails | Failed stage and evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022074
Do not relabel a failure as skipped.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022075
| Return source/SDK provenance, resolved versions, chosen app and streaming target, image reference and ID, platform/runtime requirements, evidence, and remaining checks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022076
Use a consistent human-readable result; use a machine format only when the caller supplies a real contract.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022077
Publish the image only when requested for a resolved destination.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022078
A registry-qualified tag alone is not a request to push.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022079
A local-only image is a valid containerization result, but downstream NVCF workers still need a distributed image and registry pull access.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022080
NVCF deployment, frontend creation, and full browser/media validation are separate stages.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022081
Container readiness does not prove end-to-end streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022082
Carry the image identity and required runtime configuration to the next stage without claiming its checks passed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 022083
kit-app-containerize An agent skill for preparing and containerizing NVIDIA Omniverse Kit applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022084
It supports existing applications, new Kit App Template projects, Kit App Streaming and NVCF layers, explicit image tags, and optional runtime validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022085
The default new-project source is public Kit App Template `main`; the agent asks about the desired Kit version when it has not been supplied.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022086
Load the skill Use an agent that can read local files and run commands in the chosen build environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022087
Point it at this folder's `SKILL.md` and the application project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022088
For example: ```text Read /path/to/kit-app-containerize/SKILL.md and follow its relevant references.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022089
Containerize the existing app in /path/to/my-kit-project for NVCF as acme/viewer:0.1.0.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022090
Build and inspect the image only; skip runtime validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022091
``` For a new application: ```text Read /path/to/kit-app-containerize/SKILL.md.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022092
Help me create and containerize a new Kit application for streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022093
Ask about the Kit version, streaming target, and image name/tag where needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022094
``` Keep the complete `kit-app-containerize/` directory together.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022095
Resolve each relative link from the file containing that link, preserving the folder layout even when the application is in another checkout.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022096
An older project or an NGC SDK package can use this skill from a separate checkout without changing the application's Kit version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022097
Publishing a skill under `.skills` does not guarantee automatic discovery in every agent host.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022098
Direct file loading is the baseline.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022099
If your agent supports a native skills directory, copy or link the complete folder into that host's documented location.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022100
A plain copy of `SKILL.md` omits required references.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022101
No agent-specific installer or additional plugin is required for direct loading.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022102
Contents | File | Purpose | |---|---| | [SKILL.md](SKILL.md) | Developer preflight, workflow, and completion rules.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022103
| | [App preparation](references/app-preparation.md) | Existing apps, version selection, streaming layers, and the secondary NGC route.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022104
| | [Container workflow](references/container-workflow.md) | Build prerequisites, packaging commands, image naming, and troubleshooting.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022105
| | [Validation and handoff](references/validation-and-handoff.md) | Exact-image runtime checks, optional publication, and downstream results.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022106
| The initial execution workflow targets Linux x86_64 with Docker and compatible Kit artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022107
RTX runtime checks require compatible hardware; containerization-only is supported without claiming runtime validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022108
The skill inspects the selected project's actual tooling rather than promising identical behavior across all Kit versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022109
See the [Kit containerization guide]( and [OVS getting-started guide]( for the surrounding developer journey.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022110
Step 5: Apply Fixes > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022111
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022112
> **Within-major / feature→production upgrade?** Run **only items 1, 2, 8** below (plus item 3 *if* a feature↔production registry swap is needed), then Step 6 (`validate.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022113
Skip items 4–7** — they apply only when a major boundary is crossed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022114
See "Within-major upgrades" under Step 2 in `../SKILL.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022115
Get user approval before modifying files.** Then apply in this order (a full major-boundary upgrade runs all eight): 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022116
Clear extscache** first: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022117
Update version pin** in `$DEPS_DIR/kit-sdk.packman.xml` 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022118
Update registry URLs** in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022119
Replace deprecated APIs** using patterns in `../references/api_replacements.json` — these are safe regex replacements 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022120
Remove deprecated extension deps** from `extension.toml` and `.kit` files (see `../references/removed_extensions.json`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022121
For 109→110 specifically:** the following six extensions are removed with **no deprecation notice**, and any lingering reference causes a cryptic `exit code 55` dependency-solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022122
They MUST be removed from every `.kit` (and `extension.toml`) file: - `omni.kvdb` - `omni.localcache` - `omni.genproc.core` - `omni.hydra.iray.shadercache.d3d12` - `omni.hydra.iray.shadercache.vulkan` - `omni.kit.viewport.iray` ⚠️ **Check the generated version-lock block, not just `[dependencies]`.** In application `.kit` files these names almost always appear in the auto-generated `[settings.app.exts] enabled = [...]` lock (pinned at the old version, e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022123
`omni.kvdb-109.0.10`), **not** the hand-authored dependency list.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022124
Clearing extscache (step 1) does NOT remove them** — you must regenerate the lock: delete the `# BEGIN GENERATED PART` … `# END GENERATED PART` block (the `.kit` says "Remove from 'BEGIN' to 'END' to regenerate") and run `$BUILD precache_exts -c release` so it is rebuilt without the removed extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022125
Then confirm a clean rebuild (the version stamp should advance to 110 and the six names should be gone).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022126
(If you are working in an internal `kit-app-template` checkout, the ETM lock file `templates/omni.all.template.extensions.kit` and any internal-registry entries are KAT-internal — wrapped in `# AUTOREMOVE` and stripped from external releases by `repo stage_for_github` — so external customer projects will not contain them.) 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022127
Add explicit deps** where transitive loading was removed: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022128
Update build config** in `repo.toml` (VS version, MSVC version, Windows SDK — see `../references/config_changes.json`) 8.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022129
Step 3: Scan the Project > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022130
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022131
Only run this step for major-version boundaries you cross** — a pure within-major / feature→production bump skips it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022132
Run these commands from the project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022133
Only run scans for the stages that apply to this upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022134
Collect all matches before generating the report.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022135
> **⚠️ Scan scope:** Use `.` (project root) as the search root, not just `source/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022136
Many projects have `templates/`, `launcher-configs/`, or other directories containing `.kit` files and `extension.toml` files with real dependency declarations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022137
Scanning only `source/` will miss these.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022138
> > **Windows note:** Commands below use bash syntax.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022139
On Windows, replace `for` loops with individual `findstr` or PowerShell `Select-String` commands, or run inside WSL/Git Bash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022140
Python / Extension Dependencies ```bash # === Stage 1 (106→107) === # Python 3.10 references (now 3.11) grep -rn "python3\.10\|python310\|boost_python310" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022141
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" --include="*.toml" # Private omni.client API grep -rn "omni\.client\._omniclient" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022142
include="*.py" # carb.imgui (removed — use omni.kit.imgui) grep -rn "carb\.imgui" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022143
include="*.py" # Events 1.0 patterns (payload access, subscription style) grep -rn "e\.payload\[" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022144
include="*.py" grep -rn "create_subscription_to_pop" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022145
include="*.py" # nv_usd references in build files grep -rn "nv_usd" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022146
premake5.lua repo.toml --include="*.lua" --include="*.toml" # packman XML using a pre-ABI token (should be ${platform_target_abi}).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022147
NOTE: match BOTH the old ${platform} form (Kit 106) and the intermediate ${platform_target} form — # the narrower 'platform_target[^_]' pattern misses ${platform}, which is what 106.5 actually uses and # is a build-verified hard failure on 106->107 (kit-kernel pull: "Package not found ...gl.linux-x86_64").
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022148
grep -rnE '\$\{platform(_target)?\}' "$DEPS_DIR" --include="*.xml" # Toolbar deprecated APIs grep -rn "omni\.kit\.widget\.toolbar\|omni\.kit\.window\.toolbar" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022149
include="*.py" --include="*.toml" # === Stage 2 (107→108) === # Python 3.11 references (now 3.12) grep -rn "python3\.11\|python311\|boost_python311" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022150
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" # get_custom_glyph_code (moved to omni.ui) grep -rn "omni\.kit\.ui.*get_custom_glyph_code" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022151
include="*.py" # WindowHandle deprecated usage grep -rn "WindowHandle" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022152
include="*.py" # menu_compatibility (deprecated in 108, removed in 110) grep -rn "menu_compatibility" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022153
include="*.py" # Layer events (Events 1.0 style) grep -rn "get_event_stream\|create_subscription_to_pop\|carb\.events" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022154
include="*.py" # Livestream extension (monolithic — should be split) grep -rn '"omni\.kit\.livestream"' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022155
include="*.kit" --include="*.toml" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022156
include="*.kit" --include="*.toml" # Livestream settings (old path) grep -rn "app/livestream\|app\.livestream" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022157
include="*.kit" --include="*.toml" # Old omni.kit.ui transitive usage (no longer loaded transitively) grep -rn "omni\.kit\.ui[^.]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022158
include="*.py" # === Stage 3 (108→109) === # NumPy 1.x type aliases (removed in 2.0) grep -rn "np\.bool[^_]\|np\.int[^0-9_]\|np\.float[^0-9_]\|np\.complex[^0-9_]\|np\.object[^_]\|np\.str[^_]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022159
include="*.py" # === Stage 4 (109→110) === # menu_compatibility (now raises TypeError — must remove entirely) grep -rn "menu_compatibility=" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022160
include="*.py" # omni.usd layers deprecated API grep -rn "get_context()\.get_layers()\|context\.get_layers()" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022161
include="*.py" # omni.renderer_capture (deprecated → omni.kit.capture) grep -rn "omni\.renderer_capture" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022162
include="*.py" # USD displayName/displayGroup/hidden deprecated metadata grep -rn "GetMetadata.*displayName\|SetMetadata.*displayName\|GetMetadata.*hidden\|SetMetadata.*hidden\|GetMetadata.*displayGroup\|SetMetadata.*displayGroup" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022163
include="*.py" ``` ### C++ / Native Code ```bash # === Stage 1 (106→107) === # C++ ABI — check for _GLIBCXX_USE_CXX11_ABI overrides (must be =1) grep -rn "_GLIBCXX_USE_CXX11_ABI" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022164
include="*.cpp" --include="*.h" --include="*.cmake" # === Stage 2 (107→108) === # ITokens::setValue (renamed to setValueS) grep -rn "->setValue(" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022165
include="*.cpp" --include="*.h" # carb::detail::defineTupleCommon grep -rn "carb::detail::defineTupleCommon" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022166
include="*.cpp" --include="*.h" # PyObjectVTable::get()->typeName grep -rn "PyObjectVTable" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022167
include="*.cpp" --include="*.h" # acquireInterface (prefer getCachedInterface) grep -rn "acquireInterface" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022168
include="*.cpp" --include="*.h" # carb::extras::Path implicit conversion grep -rn "carb::extras::Path\|carb::fs::Path" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022169
include="*.cpp" --include="*.h" # Assert macros (may need explicit carb/Assert.h now) grep -rn "CARB_ASSERT\|CARB_FATAL_UNLESS" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022170
include="*.cpp" --include="*.h" # Library.h removed functions grep -rn "getDefaultLibraryPrefix\|getDefaultLibraryExtension" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022171
include="*.cpp" --include="*.h" # GfMatrix usage (imprecise overloads removed) grep -rn "GfMatrix" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022172
include="*.cpp" --include="*.h" # ILayers.h inclusion (ABI 1.0 → 1.1 recompile required) grep -rn "ILayers\.h\|omni/kit/usd/layers" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022173
include="*.cpp" --include="*.h" # carb.events const char* usage (deprecated — prefer string_view) grep -rn "carb::events::\|IEventQueue\|IEvents" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022174
include="*.cpp" --include="*.h" # Scalar xform ops — code that iterates over xform ops assuming vector types grep -rn "GetOrderedXformOps\|xformOp:translate\|xformOp:scale\|xformOp:rotate" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022175
include="*.cpp" --include="*.h" --include="*.py" # === Stage 3 (108→109) === # Fabric TokenC/PathC (removed; also kUninitializedToken/Path) grep -rn "TokenC\|PathC\|TokenId\|PathId\|kUninitializedToken\|kUninitializedPath" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022176
include="*.cpp" --include="*.h" # carb::cpp17 / carb::cpp20 (merged to carb::cpp) grep -rn "carb::cpp17\|carb::cpp20" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022177
include="*.cpp" --include="*.h" # carb::thread::shared_lock (removed) grep -rn "carb::thread::shared_lock" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022178
include="*.cpp" --include="*.h" # IDictionary::MakeAtPathS (renamed to MakeAtPath) grep -rn "MakeAtPathS" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022179
include="*.cpp" --include="*.h" # compareStringsNoCase (renamed) grep -rn "compareStringsNoCase" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022180
include="*.cpp" --include="*.h" # Logger (superseded by Logger2) grep -rn "carb::logging::Logger[^2]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022181
include="*.cpp" --include="*.h" # MDL/Neuray usage (ABI 56 → 57 recompile required) grep -rn "omni\.mdl\|Neuray\|MDL.*SDK" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022182
include="*.cpp" --include="*.h" --include="*.toml" # CloudXR / XRCloudXRBindings grep -rn "CloudXR\|XRCloudXRBindings\|IOpenXRRuntime" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022183
include="*.cpp" --include="*.h" # === Stage 4 (109→110) === # CARB_CHECK (replaced by CARB_RELEASE_ASSERT) grep -rn "CARB_CHECK" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022184
include="*.cpp" --include="*.h" # carb/Defines.h (split into sub-headers) grep -rn '#include.*carb/Defines\.h' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022185
include="*.cpp" --include="*.h" # IFileSystem raw char* methods grep -rn "IFileSystem" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022186
include="*.cpp" --include="*.h" # ITokens (unsafe methods removed; ITokens 2.0 available) grep -rn "ITokens\|->resolveString\|->setValue" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022187
include="*.cpp" --include="*.h" # optional / expected — semantics changed (if(b) now tests presence) grep -rn "optional \|expected **Important:** Also scan `templates/`, `launcher-configs/`, and any ETM lock files (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022188
`omni.all.template.extensions.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022189
These contain real dependency declarations and will cause test or runtime failures if they reference removed extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022190
```bash # === All stages — removed/deprecated extensions === # Kit 108 removals grep -rn "omni\.kit\.extpath\.git" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022191
include="*.toml" --include="*.kit" # Kit 108 — monolithic livestream (split into modules) grep -rn '"omni\.kit\.livestream"' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022192
include="*.toml" --include="*.kit" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022193
include="*.toml" --include="*.kit" # Kit 110 removals (cause cryptic exit-55 dependency solver failures) for ext in omni.kvdb omni.localcache omni.genproc.core; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022194
include="*.kit" --include="*.toml" done # Kit 110 silently removed (no deprecation notice) for ext in "omni.hydra.iray.shadercache.d3d12" "omni.hydra.iray.shadercache.vulkan" "omni.kit.viewport.iray"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022195
include="*.kit" --include="*.toml" done # Deprecated (not yet removed — still operational but plan migration) for ext in "omni.command.usd" "omni.debugdraw" "omni.hydra.iray" "omni.iray.settings.core" \ "omni.kit.autocapture" "omni.kit.manipulator.viewport" "omni.hydra.scene_api" \ "omni.renderer_capture" "omni.surface_instancer" "omni.kit.viewport.legacy_gizmos" \ "omni.kit.widget.nucleus_connector"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022196
include="*.kit" --include="*.toml" done # Extensions that need explicit declaration (no longer loaded transitively) grep -rn "omni\.kit\.manipulator\.prim\.fabric\|omni\.resourcemonitor\|omni\.kit\.ui" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022197
\ --include="*.py" --include="*.toml" ``` ### Config Files ```bash # Extension registry URLs (must update for Kit 110) grep -rn "kit-extensions\.ov\.nvidia\.com\|omniverse://" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022198
include="*.kit" # Build system (VS version) — also check CI-scoped token overrides # (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022199
"token:in_ci==true".vs_version may override the default even when the top-level is correct) grep -rn "vs_version\|vs2019\|vs2017\|v142" repo.toml # Livestream settings (old path style) grep -rn "app/livestream" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022200
include="*.kit" --include="*.toml" # Kit SDK version pin (use the $DEPS_DIR detected in Step 1) cat "$DEPS_DIR/kit-sdk.packman.xml" # mergeMaterials (behavioral default change in 109) grep -rn "mergeMaterials" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022201
include="*.kit" --include="*.toml" # FSD / Fabric Scene Delegate settings grep -rn "FabricSceneDelegate\|fsd\b" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022202
include="*.kit" --include="*.toml" ``` ### OmniGraph ```bash # === Stage 2 (107→108) — OmniGraph 3.0 ABI === grep -rn "omni\.graph\.core\|omni\.graph\.nodes" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022203
include="*.toml" # === Stage 4 (109→110) — deprecated/removed OmniGraph nodes === # DeformedPointsToHydra — removed (was part of OmniHydra) grep -rn "DeformedPointsToHydra" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022204
include="*.py" --include="*.usd" --include="*.usda" # OnCustomEvent bundle attributes deprecated grep -rn "OnCustomEvent" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022205
include="*.py" --include="*.usd" --include="*.usda" # Bundle/attribute manipulation nodes deprecated grep -rn "ArrayGetSize\|AttributeType\|BundleConstructor\|CopyAttribute\|ExtractPrim\|GetAttributeNames\|HasAttribute\|InsertAttribute\|RemoveAttribute\|RenameAttribute" \ .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022206
include="*.py" --include="*.usd" --include="*.usda" # Event/render pipeline nodes deprecated grep -rn "UpdateTickEvent\|GpuInteropCudaEntry\|RenderPreprocessEntry\|RpResourceExample" \ .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022207
include="*.py" --include="*.usd" --include="*.usda" ``` ### Isaac Sim Projects If the project uses Isaac Sim extensions, scan for the `omni.isaac.*` namespace migration (applies Kit 107+): ```bash # omni.isaac.* imports (deprecated → isaacsim.*) grep -rn "omni\.isaac\." .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022208
include="*.py" --include="*.toml" --include="*.kit" # omni.replicator.isaac (→ isaacsim.replicator.*) grep -rn "omni\.replicator\.isaac" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022209
include="*.py" --include="*.toml" # Dynamic Control Toolbox (removed as compile-time dep) grep -rn "dynamic_control\|DynamicControl" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022210
include="*.py" --include="*.cpp" --include="*.h" # SemanticsAPI (→ UsdSemantics.LabelsAPI) grep -rn "add_update_semantics\|SemanticsAPI" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 022211
Failure Mode Diagnosis > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022212
Use this when the user has **already** upgraded and has a specific error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022213
`$DEPS_DIR` / `$BUILD` refer to the values detected in Step 1 (in `../SKILL.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022214
Exit Code 55 (Dependency Solver Failure) **Cause:** Removed extension still declared as a dependency, or stale extscache.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022215
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022216
Search for removed extension names in `.kit` and `extension.toml` files (see `../references/removed_extensions.json`) 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022217
For Kit 110: check for `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.*`, `omni.kit.viewport.iray` 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022218
Re-run `precache_exts` ### Build Fails with Undefined Symbol / Missing Method **Cause:** ABI break — extension was compiled against an older version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022219
Fix:** Recompile the extension against the current Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022220
Every stage has at least one ABI break.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022221
Runtime Crash on DLL Load (Windows) **Cause after Stage 3:** mimalloc cross-DLL heap mismatch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022222
Memory allocated on one side of a DLL boundary freed on the other.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022223
Fix:** Audit allocation ownership.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022224
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022225
Python TypeError: unexpected keyword argument 'menu_compatibility' **Cause (Stage 4):** `menu_compatibility` parameter removed from `ui.Menu` and `ui.Separator`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022226
Fix:** Remove the `menu_compatibility=` argument from all call sites.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022227
Extension Loads But APIs Return None / AttributeError **Cause:** Transitive loading of `omni.kit.ui`, `omni.resourcemonitor`, or `omni.kit.manipulator.prim.fabric` was removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022228
Fix:** Add explicit dependency in `extension.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022229
Render Output Differs (No Code Changes) **Cause after Stage 3:** DomeLight orientation changed (USD 25.05), FSD enabled by default, or `mergeMaterials` default changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022230
Diagnosis:** - Check for DomeLights in the scene: `grep -rn "DomeLight" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022231
include="*.usd" --include="*.usda"` - Check FSD setting: `grep -rn "FabricSceneDelegate\|fsd" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022232
include="*.kit" --include="*.toml"` - Check `mergeMaterials`: `grep -rn "mergeMaterials" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022233
include="*.kit" --include="*.toml"` ### if (optional_bool) No Longer Works (C++) **Cause (Stage 4):** `optional ` / `expected ` now tests for *presence* in an if-condition, not the stored value.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022234
Fix:** Replace `if (b)` with `if (b.has_value() && b.value())` ### Build Fails in a Loop / the Same Error Repeats **Cause:** Almost always a **stale toolchain** (Step 2.5 not applied — see `toolchain.md`) or a wrong assumption about the project's layout/build system — *not* the source code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022235
Rule — do not keep editing source and rebuilding.** If the same build error recurs after **2 attempts**, STOP and re-check the fundamentals before changing any more code: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022236
Is the **toolchain** aligned to the target Kit line?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022237
(Step 2.5, `toolchain.md` — the #1 cause of build loops.) 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022238
Is `$DEPS_DIR` the **actual** deps location and `$BUILD` the project's **actual** build entrypoint?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022239
(Step 1 in `../SKILL.md`.) 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022240
Did you do a **clean** rebuild (`$BUILD build --rebuild -r`), not just clear extscache?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022241
(Step 6, `validate.md`.) Surface the exact error and these three checks to the user rather than looping — repeated speculative edits burn tokens and rarely fix a toolchain/layout problem.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022242
Project Uses a Custom / Integrated Build System **Cause:** The project wraps or embeds the Kit build system in its own tooling, so `./repo.sh` / `repo.bat` don't exist or aren't the real entrypoint (common for customer integrations).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022243
Fix:** Do **not** fabricate `./repo.sh` commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022244
Use the `$BUILD` detected in Step 1 (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or ask the user).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022245
The upgrade steps (kernel pin, **toolchain update**, lock regen) still apply — invoke them through `$BUILD`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022246
deps Directory Not Where Expected **Cause:** The project layout differs from the SDK template, or the deps directory moved between releases (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022247
`deps/` at the project root vs under `tools/`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022248
Fix:** Re-run the Step 1 detection (in `../SKILL.md`) to set `$DEPS_DIR`, then use it everywhere.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022249
Never hardcode `tools/deps/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022250
Step 2.5: Update the Build Toolchain (highest-impact — often the real work) > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022251
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022252
Run this **before** touching source code — for a within-major / feature→production bump it is usually the *only* substantive work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022253
> **Key principle:** the most valuable part of an upgrade is usually **not** the code changes — it is making sure the project's **tooling** is correctly updated (repo scripts, `repo_man`/repoman, dependency versions).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022254
This step is therefore **first-class for every upgrade**, and the *primary* step for within-major / branch-transition bumps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022255
Run it **before** touching source code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022256
Why it matters:** the Kit kernel pin and the repo toolchain are coupled.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022257
Bumping `kit-sdk.packman.xml` alone frequently fails because packman tokens (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022258
`${platform_target_abi}`) only resolve under the matching `repo_man`, and newer kernels expect newer `repo_build` / `repo_kit_tools`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022259
A pin bump *without* a toolchain bump produces cryptic pull/resolve failures — e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022260
`Package not found ...gl.linux-x86_64` or `No versions of … = `.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022261
The toolchain = these files** (see `../references/toolchain.json`): - `$DEPS_DIR/repo-deps.packman.xml` — the `repo_*` tools: `repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_tools_internal`, `repo_kit_template`, `repo_usd`, `repo_format`, `repo_test`, `repo_package`, `repo_ci`, etc.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022262
`$DEPS_DIR/kit-sdk.packman.xml` — the kit-kernel pin (updated in Step 5, item 2 — see `apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022263
`tools/packman/` — the packman bootstrap (`packman`, `packman.cmd`, `bootstrap/`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022264
`repo.sh` / `repo.bat` — the repo wrappers (may need regenerating under a newer `repo_man`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022265
`repo.toml` — build config (VS/MSVC/WinSDK for Stage 4; see `../references/config_changes.json`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022266
How to find the correct target versions — do NOT guess:** 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022267
Get a **reference project already on the target Kit version** — the matching `kit-app-template` or `kit-sdk-public` branch for that Kit line, or the target Kit SDK release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022268
Read its `repo-deps.packman.xml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022269
Prefer the `production/ ` branch** — it carries the vetted, most-current toolchain for that release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022270
⚠️ **Toolchain versions track the branch's maintenance cadence, not the kernel number** — a newer kernel line can ship an *older* toolchain (in kit-sdk-public, `feature/main` pins kernel 110.4 with `repo_man` 2.6.4, while the maintained `production/110.1` pins kernel 110.1.3 with a *newer* `repo_man` 2.9.3).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022271
Always read the target branch's **actual** pins; never assume "newer Kit = newer tools".
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022272
(Those version numbers are an illustrative snapshot read in 2026 — they **will** go stale; verify against the live branch, do not copy them.)* 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022273
Diff** the project's `$DEPS_DIR/repo-deps.packman.xml` against the reference and align each `repo_*` tool `version=` to the reference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022274
Do the same for `tools/packman/` if it differs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022275
Apply the versions, then do a **clean rebuild** (Step 6 — see `validate.md`) — the toolchain bump must land before the kernel pin resolves cleanly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022276
> This step is safe to run and validate (Step 6) **on its own, first**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022277
Many "the upgrade won't build" error loops are nothing more than a stale toolchain — fixing it up front avoids chasing phantom code errors.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 022278
Step 6: Validate > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 022279
Assumes Step 1 detection has run (`$BUILD` is set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 022280
```bash # After a kit-kernel pin bump, do a CLEAN rebuild so the kernel symlinks refresh, # then regenerate the version lock against the new kernel.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 022281
$BUILD is the entrypoint detected in Step 1 (./repo.sh, repo.bat, or the project's own build wrapper).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 022282
`No versions of > omni.anim.curve.core … = `).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 022283
Use **`$BUILD build --clean`** (removes the build-time `_*` > folders so the next `build -r` refreshes the symlinks) or **`$BUILD build --rebuild -r`** (clean + > release build in one command), then regenerate the lock with `build -u`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 022284
The generated `[settings.app.exts] > enabled = [...]` block in each `.kit` is what must be regenerated — it carries exact old-version pins that > `extscache` clearing does not touch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 022285
Important Notes by Stage > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022286
Per-stage reference for the breaking changes summarized in the Step 2 migration table.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022287
Read the stages that apply to the boundaries you cross.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022288
Stage 1: 106 → 107 - **Rebuild required** — Linux ABI changed (`_GLIBCXX_USE_CXX11_ABI=0` → `=1`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022289
All prebuilt `.so` files will fail to load.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022290
packman XML token**: Update the kit-kernel pin token to `${platform_target_abi}` in all `.packman.xml` files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022291
Kit 106 uses the **`${platform}`** form (not `${platform_target}`); both must become `${platform_target_abi}`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022292
Build-verified:* leaving the old token makes the kit-kernel pull fail immediately with `Package not found on specified remote servers (…gl.linux-x86_64.release)`, because Kit 107's kernel is published only under the ABI string (`manylinux_2_35_x86_64`), not `linux-x86_64`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022293
Bump the repo toolchain too (required, easy to miss)** — see **Step 2.5** (`toolchain.md`): the token fix alone is **insufficient** — `${platform_target_abi}` only resolves to the ABI string under the newer `repo_man`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022294
Update `$DEPS_DIR/repo-deps.packman.xml` to the 107-era tooling (`repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_template`, `repo_usd`) and the packman bootstrap.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022295
Build-verified:* under 106.5's `repo_man` 1.86.0 the token still resolves to `linux-x86_64`; after the toolchain bump it resolves to `manylinux_2_35_x86_64` and the pull succeeds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022296
Carbonite Events 2.0**: The event system changed from push/pump to dispatch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022297
No explicit pump calls needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022298
Python payload access changed from `e.payload['key']` to `e['key']`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022299
C++17 is now available** explicitly in Premake via `cppdialect = "C++17"`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022300
Stage 2: 107 → 108 - **Kit 108 was never publicly released.** These changes still apply when upgrading 107→109.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022301
Python 3.12** replaces 3.11.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022302
Update all Premake configs, CI configs, and boost_python links.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022303
OpenUSD 25.02**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022304
GfMatrix imprecise overloads removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022305
Livestream modularization**: `omni.kit.livestream` (monolithic) → `omni.kit.livestream.app` + `.aov` + `.core`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022306
`omni.services.livestream.nvcf` → `omni.services.livestream.session`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022307
Settings paths changed — see `../references/config_changes.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022308
Transitive deps removed**: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` must now be declared explicitly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022309
ILayers ABI 1.0 → 1.1**: Recompile all extensions including `ILayers.h`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022310
USD scalar xform ops**: OpenUSD now supports scalar ops (e.g., `xformOp:translateX`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022311
Code iterating over xform ops that assumes all are vector types may behave incorrectly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022312
Stage 3: 108 → 109 - **CUDA 12.4.1 driver requirement**: Linux minimum 550.54.15, Windows minimum 551.78.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022313
Apps fail to start with older drivers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022314
NumPy 2.x**: Many breaking changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022315
On Windows, the default integer type changed from `int32` to `int64` — can cause silent correctness issues.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022316
Fabric ABI break**: Even if no source changes needed (no TokenC/PathC usage), all extensions including Fabric headers must recompile — `Token`/`Path` became trivially copyable, which is a binary ABI change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022317
Use `token.isNull()` instead of `kUninitializedToken`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022318
mimalloc (Windows)**: Cross-DLL allocation/free pairs that cross a DLL boundary may now crash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022319
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022320
mergeMaterials**: Default changed — can cause significant load time regression with no code error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022321
FSD default on**: If previously disabled FSD, test render output carefully.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022322
DomeLight orientation**: USD 25.05 changed the default orientation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022323
Visual change only — no code error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022324
Use `UpgradeUsdLuxLightsCommand` for assisted migration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022325
Stage 4: 109 → 110 - **Clear extscache first** — stale Kit 109 entries cause exit-55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022326
Silent extension removals**: `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.d3d12`, `omni.hydra.iray.shadercache.vulkan`, `omni.kit.viewport.iray` — all removed with no deprecation notice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022327
First symptom is a cryptic exit-55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022328
Remove every reference from `.kit`/`extension.toml` files — including the auto-generated `[settings.app.exts] enabled = [...]` version-lock block, where they usually hide pinned at the old version (clearing extscache alone won't drop them; regenerate the lock with `precache_exts` — see Step 5, item 5 in `apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022329
Also scan `templates/` and ETM lock files** — these are easily missed by `source/`-only scans.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022330
DomeLight orientation (inherited from Stage 3)**: If the project contains DomeLights and was not verified during a previous Stage 3 upgrade, the USD 25.05 orientation change is a permanent behavioral difference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022331
Search with `grep -rn 'DomeLight' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022332
include='*.py' --include='*.usd'` and use `UpgradeUsdLuxLightsCommand` if scenes were not migrated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022333
`optional ` semantics**: `if(b)` now tests *presence*, not *value*.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022334
Code that previously worked may now be wrong silently.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022335
`g_carbClientName`**: Type changed to `zstring_view`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022336
Any direct string assignment or comparison breaks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022337
Hydra 2 removed**: No migration path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022338
Hydra 1 (Storm) and RTX remain.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022339
OmniGraph bundle nodes**: Large set of bundle/attribute manipulation nodes deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022340
Deprecation warnings visible in editor from Kit 110.1+.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022341
`AttributeType` → `GetAttributeType`, `ArrayGetSize` → `ArrayLength`, `ExtractPrim` → `ReadPrim`, `GetAttributeNames` → `ReadPrimAttributes`, `InsertAttribute` → `WritePrimAttribute`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022342
`BundleConstructor`, `RemoveAttribute`, `RenameAttribute` have no direct replacement — redesign graphs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022343
OpenUSD 25.11**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022344
Ndr/Sdr libraries consolidated — update include paths.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022345
VS2022 required** on Windows (was VS2019).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022346
New extensions in Kit 110**: `omni.grpc.lib`, `omni.protobuf.lib`, `omni.sensors.nv.*` (camera/lidar/radar/ultrasonic/ids/wpm), `omni.kit.xr.core` — available for use in Kit 110 apps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 022347
Step 4: Generate Upgrade Report > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022348
Run after the Step 3 scans (`scan.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022349
Present findings organized by severity.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022350
Use exact `file:line` references from scan output.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022351
``` ## Upgrade Report: Kit [FROM] → [TO] Project: [path] Migration stages applied: [e.g., Stage 2 + 3 + 4] ### ❌ Breaking Changes (must fix — build or load will fail) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022352
[file:line] — [description] → [exact fix] ### ⚠️ Behavioral Changes (no error, but may affect output or performance) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022353
[file:line] — [description] → [fix or test required] ### 🔔 Deprecated Usage (should fix — will break in next version) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022354
[file:line] — [description] → [fix] ### ✅ Not Affected - [List the `id` or `title` from `breaking_changes.json` for each pattern that was scanned and returned no matches.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022355
This serves as a record that the check was performed, not just skipped.] ### 📋 Required Steps Regardless of Code Changes 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022356
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022357
Update `kit-sdk.packman.xml`: change version pin to `[TO].x.y+feature.${platform_target_abi}.${config}` 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022358
Update extension registry URLs in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022359
Rebuild all C++ extensions (ABI break at every stage — required even with no source changes) 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022360
Regenerate version lock blocks in `.kit` files: `$BUILD precache_exts -c release` (substitute the build entrypoint detected in Step 1 — `./repo.sh` may not exist on a custom/integrated build) 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022361
If project has an ETM lock file (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022362
`omni.all.template.extensions.kit`), regenerate it or manually remove entries for removed extensions 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022363
[stage-specific items, e.g., VS2022 for Stage 4] ### 🧪 Behavioral Tests Required 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022364
[scenes with DomeLights — orientation regression (Stage 3, but inherited in all later stages)] 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022365
[load performance with mergeMaterials setting (Stage 3)] 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022366
[render output with FSD enabled (Stage 3)] 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022367
[MaterialX materials (Stage 4)] 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022368
[transform-heavy workflows after scalar xform ops change (Stage 2)] ``` **Prioritize for the user:** Extension removal errors and ABI rebuild requirements are the most common causes of project failures after a version bump.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 022369
[ {"setting":"packman XML ABI token","versions":{"from":"106","to":"107"},"old_value":"${platform_target}","new_value":"${platform_target_abi}","file":"*.packman.xml","path":"package name attributes","notes":"Native packages now use ABI-variant package names.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022370
The deps directory location varies by release and project type (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022371
deps/ at the project root in one release, under tools/ in another, even between point releases of the same major line).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022372
Do NOT assume tools/deps/ and do NOT rewrite paths from old_value to new_value -- detect the actual location (SKILL.md Step 1, $DEPS_DIR)."} ]
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022373
[ {"id":"py-omniclient","versions":{"from":"106","to":"107"},"category":"Python API","severity":"breaking","title":"omni.client._omniclient removed","description":"Private internal API removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022374
Use public omni.client API.","search_patterns":["omni\\.client\\._omniclient"],"file_types":[".py"],"fix":{"type":"regex_replace","description":"Replace import","from_pattern":"import omni\\.client\\._omniclient","to_pattern":"import omni.client"}}, {"id":"py-311","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"Python 3.10 → 3.11","description":"Python upgraded.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022375
Audit f-strings, typing module usage, and third-party packages for 3.11 compatibility.","search_patterns":["python3\\.10","python310"],"file_types":[".toml",".py",".sh",".bat",".lua"],"fix":{"type":"manual","description":"Update Python references to 3.11"}}, {"id":"cpp-abi-cxx11","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Linux: _GLIBCXX_USE_CXX11_ABI=1","description":"Native packages now use new C++ ABI.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022376
Rebuild all .so plugins.","search_patterns":["_GLIBCXX_USE_CXX11_ABI"],"file_types":[".cpp",".cmake",".toml"],"fix":{"type":"manual","description":"Rebuild all native plugins against new ABI"}}, {"id":"packman-abi-token","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"packman XML: ${platform_target} → ${platform_target_abi}","description":"Native packages now use ABI-variant tokens.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022377
Python payload access changed from e.payload['key'] to e['key'].
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022378
Subscribe via carb.eventdispatcher.get_eventdispatcher().observe_event().
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022379
C++: update to carb::eventdispatcher.","search_patterns":["e\\.payload\\[","carb\\.events\\.acquire_event_queue","create_subscription_to_pop"],"file_types":[".py",".cpp",".h"],"fix":{"type":"manual","description":"Update event subscriptions and payload access to Events 2.0 pattern.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022380
Remove explicit event pump calls."}}, {"id":"fabric-pathc-tokenc-intro","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Fabric PathC/TokenC introduced (removed in 109)","description":"Kit 107 introduced PathC/TokenC.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022381
Kit 109 removes them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022382
Update Premake configs, CI, and build scripts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022383
Audit all third-party packages for 3.12 compatibility.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022384
Use getCachedInterface.","search_patterns":["acquireInterface"],"file_types":[".cpp",".h"],"fix":{"type":"regex_replace","from_pattern":"carb::Framework::acquireInterface","to_pattern":"carb::getCachedInterface"}}, {"id":"omnigraph-3.0","versions":{"from":"107","to":"108"},"category":"C++ ABI","severity":"breaking","title":"omni.graph.core 3.0.0 ABI break","description":"Binary incompatible with 2.x.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022385
Recompile all OmniGraph nodes.","search_patterns":["omni\\.graph\\.core","omni\\.graph\\.nodes"],"file_types":[".toml"],"fix":{"type":"manual","description":"Recompile against omni.graph.core 3.0.0.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022386
Align omni.graph.nodes version."}}, {"id":"parallel-node-reg","versions":{"from":"107","to":"108"},"category":"Extension","severity":"breaking","title":"Parallel OmniGraph node registration removed","description":"Extension manager is not thread-safe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 022387
[ { "extension": "omni.kvdb", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022388
Causes exit code 55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022389
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.localcache", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022390
Same failure class as omni.kvdb.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022391
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.genproc.core", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022392
Migrate procedural generation workflows.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022393
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.kit.extpath.git", "status": "removed", "version": "108", "replacement": null, "search_in": [ "extension.toml" ], "notes": "Git URL extension search path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022394
Was deprecated in 107." }, { "extension": "omni.hydra.iray.shadercache.d3d12", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022395
No explicit removal notice." }, { "extension": "omni.hydra.iray.shadercache.vulkan", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022396
No explicit removal notice." }, { "extension": "omni.kit.viewport.iray", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Was Sample in Kit 107.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022397
No version recorded in official docs." }, { "extension": "omni.hydra.scene_api", "status": "deprecated", "version": "108", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated since Kit 108.0.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022398
Removal pending." }, { "extension": "omni.surface_instancer", "status": "deprecated", "version": "pre-106", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Confirmed deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022399
Active customer confusion." }, { "extension": "omni.renderer_capture", "status": "deprecated", "version": "110", "replacement": "omni.kit.capture", "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated in Kit 110." }, { "extension": "omni.kit.widget.nucleus_connector", "status": "deprecated", "version": "110", "replacement": "omni.kit.widget.connection_manager", "search_in": [ "extension.toml", ".kit" ], "notes": "Compatibility shim.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022400
Will be removed." }, { "extension": "omni.kit.viewport.legacy_gizmos", "status": "deprecated", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Deprecated in Kit 110.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022401
Still operational but emits deprecation warnings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022402
Commonly appears in both source/apps/ and templates/ .kit files — scan the full project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022403
No direct replacement announced; plan migration away from legacy gizmos rendering path." }, { "extension": "omni.kit.livestream", "status": "removed", "version": "108", "replacement": "omni.kit.livestream.app + omni.kit.livestream.aov + omni.kit.livestream.core", "search_in": [ "extension.toml", ".kit" ], "notes": "Monolithic livestream extension split into focused modules in Kit 108.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022404
Replace with the three new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022405
Settings paths also changed \u2014 see config_changes.json." }, { "extension": "omni.services.livestream.nvcf", "status": "removed", "version": "108", "replacement": "omni.services.livestream.session", "search_in": [ "extension.toml", ".kit" ], "notes": "Session management extension renamed in Kit 108.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022406
Replace dependency declaration and update any code referencing the old extension name." } ]
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 022407
{ "description": "The build toolchain a Kit project must keep in sync with its kit-kernel pin.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022408
SKILL.md Step 2.5 makes updating it a first-class step.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022409
Do NOT hardcode versions here — they move per branch; read the target branch's actual pins at upgrade time.", "toolchain_files": [ {"file": " /kit-sdk.packman.xml", "holds": "kit-kernel pin (the Kit SDK itself)", "notes": "DEPS_DIR is tools/deps/ or root deps/ — detect it (SKILL.md Step 1)."}, {"file": " /repo-deps.packman.xml", "holds": "the repo_* build tools + template-content packages", "notes": "The main toolchain file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022410
Add or remove packages that appear/disappear between lines (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022411
repo_nspect is present on feature/main but not on production/110.1 or feature/110.3).", "reference_source": "omniverse/kit-apps/kit-sdk-public (and/or omniverse/kit-github/kit-app-template) on the matching branch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022412
Prefer production/ over feature/ for a stable upgrade.", "critical_note": "Toolchain versions track the BRANCH's maintenance cadence, NOT the kernel line number.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022413
A newer kernel line can carry an OLDER toolchain.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022414
Never infer tool versions from the Kit version — read the actual target-branch pins.", "example_only_do_not_copy": { "note": "Illustrative snapshot read from kit-sdk-public in 2026 — WILL go stale.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022415
Always re-read the target branch at upgrade time.", "feature/main": {"kit-kernel": "110.4.0+feature", "repo_man": "2.6.4", "repo_build": "1.30.0", "repo_kit_tools": "1.20.3"}, "production/110.1": {"kit-kernel": "110.1.3+production", "repo_man": "2.9.3", "repo_build": "1.34.3", "repo_kit_tools": "1.21.2"} } } }
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 022416
Select and prepare the application Use the section matching the developer's starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022417
Source selection and app preparation happen in the application project, which can differ from the checkout containing this skill.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022418
License acceptance during preflight Identify required license acceptance while resolving the selected source and tool version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022419
Inspect that version's license notices or prompt implementation before starting generation or long-running builds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022420
Brief source/tool inspection may be needed to identify the terms; do not defer a known acceptance requirement until an unattended operation stops at a prompt.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022421
When acceptance is required and not already supplied, collect it together with the initial app/version/image/validation decisions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022422
Make the question explicit in the conversation, even when also using a structured question UI: - Explain which planned operation requires acceptance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022423
Name and link every agreement identified by the selected workflow, and state the project or runs the acceptance will cover.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022424
Quote the tool's prompt when it has been observed; do not invent a live prompt or claim work has stopped when this is preflight.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022425
Ask for an explicit yes or no, with an example reply.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022426
Explain that a yes authorizes answering the matching tool prompt on the developer's behalf.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022427
For example, when the selected workflow names the NVIDIA agreements below: > Before I generate this application and start the build, do you accept the [NVIDIA Software License Agreement]( and [Omniverse Product-Specific Terms]( and authorize me to answer Yes to the license prompt for this application?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022428
Reply "Yes, I accept" or "No." Use the selected version's agreements and URLs if they differ, and state the actual scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022429
One explicit acceptance can cover multiple planned runs using the same terms when those runs are named.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022430
Honor acceptance already supplied for that scope and use it when the matching tool prompt appears.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022431
Do not infer acceptance from silence or a general request to build, or bypass the tool's required response.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022432
If a later prompt presents different terms or scope, surface that difference before accepting.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022433
While awaiting an answer, continue only work that does not require acceptance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022434
Existing project Locate the intended project and inspect its instructions, working changes, build entrypoint, app definitions, and dependency configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022435
Common Kit App Template locations include: - `source/apps/` for base apps and layers, `source/extensions/` for project extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022436
`repo.toml` for build/packaging configuration, `repo_tools.toml` and `tools/deps/` for tool and SDK pins.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022437
`templates/templates.toml` and resolved template metadata for available template/layer operations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022438
Custom projects can use other layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022439
Follow their build registration and dependency precaching rather than introducing template metadata solely to fit this workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022440
Resolve the requested `.kit` file and its dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022441
Record the actual base app and selected layer.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022442
Inspect inherited settings and launcher behavior as well as the selected file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022443
A name ending in `_nvcf.kit` or `_streaming.kit` is a clue, not proof of the configured functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022444
Check whether the app has the dependencies, settings, build registration, and assets it needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022445
Prepare missing packaging or streaming configuration within the requested scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022446
If the app requires substantial implementation or migration before it can build, report that boundary and the specific blocker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022447
New project from GitHub Recommend [NVIDIA-Omniverse/kit-app-template]( `main`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022448
If the request does not choose a Kit version/ref, ask whether the developer wants that default or a specific version/ref.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022449
Inspect the public refs and selected source pins, then display the resolved Kit version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022450
Use a new directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022451
For the accepted default: ```bash git clone --branch main --single-branch my-kit-project cd my-kit-project git rev-parse HEAD ``` Choose the directory from the developer's workspace context.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022452
For another branch or tag, resolve that exact ref; for a commit, fetch and check out the resolved commit explicitly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022453
Do not apply `--branch` to a commit hash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022454
If a requested version is unavailable publicly, explain the available choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022455
Never substitute an internal checkout or edit only the Kit kernel pin to simulate a complete version change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022456
Inspect the selected checkout's dependency pins and CLI.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022457
The ordinary template flow is: ```bash ./repo.sh template new ``` Select the available app template based on the requested behavior, then resolve its app namespace/name, display name, app version, and any required extension inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022458
Do not silently reuse documentation example identities.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022459
Keep app version independent of the Kit version and container tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022460
Answer any required template license prompt using the acceptance established during preflight.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022461
If it presents different terms or scope, follow [license preflight](#license-acceptance-during-preflight) before proceeding.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022462
Use supported interactive input or the chosen tool's documented playback mechanism.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022463
In the inspected tooling, `template new --generate-playback ` records choices without creating the app; `template replay ` subsequently renders it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022464
Inspect help before using these options on another version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022465
A generated playback file alone is not an application.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022466
Legacy `--input` or `REPO_TEMPLATE_SCRIPT` mechanisms do not reliably handle checkbox layer selection; use the supported playback flow or interact with the actual prompts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022467
Streaming layers | Target | Preparation | |---|---| | Kit App Streaming | Reuse or add the selected version's ordinary streaming layer for local or self-managed streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022468
In the inspected Kit App Template this is the picker entry `[omni_default_streaming]: Omniverse Kit App Streaming (Default)`, which renders `{app_name}_streaming.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022469
| | NVCF | Reuse or add that version's NVCF layer, including its streaming/session-service dependencies and settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022470
Ordinary streaming alone is insufficient.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022471
In the inspected Kit App Template this is the picker entry `[nvcf_streaming]: NVCF Streaming`, which renders `{app_name}_nvcf.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022472
| | Non-streaming | Keep the intended headless app entrypoint; do not add streaming dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022473
Determine whether the app still requires GPU rendering.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022474
| For template-generated apps, select the layer during creation or use the available modify flow: ```bash ./repo.sh template modify ``` Inspect the app's template metadata before modifying it, commonly `source/rendered_template_metadata.json`, and the template's linked-layer definitions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022475
The inspected modify flow is interactive and can overwrite an already rendered layer when selected again.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022476
Reuse a correct existing layer; inspect custom edits before regenerating.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022477
Do not invent noninteractive `--app` or `--layer` flags.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022478
For a manually authored app without the required metadata, use the selected version's layer definitions as a reference and make only the necessary dependency/settings changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022479
Rebuild after adding or changing layers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022480
Select the actual generated layer as the packaging entrypoint, such as `acme.viewer_streaming.kit` for Kit App Streaming or `acme.viewer_nvcf.kit` for NVCF.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022481
Do not package the base desktop app merely because it has the same display name.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022482
Secondary route: NGC SDK Use this route when the developer chooses it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022483
If the developer is unsure, explain the two source routes and recommend public Kit App Template by default.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022484
Resolve the desired resource and version using the [Kit SDK catalog links in the manual]( Select the resource matching the requested release and platform; the collection linked by a latest guide may cover a different feature or production line.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022485
Follow that resource's download and extraction instructions using available authentication.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022486
Do not assume an NGC SDK resource is a runnable container image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022487
Record the resource organization/team/name, requested version, downloaded artifact identity/checksum, and detected SDK version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022488
Do not invent a Git commit for a downloaded SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022489
On Linux, when provided by that package, run `./new_project.sh` from the extracted SDK and resolve its project-location and license prompts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022490
Inspect the package's instructions if this entrypoint differs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022491
Enter the generated project, inspect its actual tool/SDK pins, and use the same app/layer workflow above.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022492
Keep the skill loaded from its complete folder if it is absent from that SDK release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022493
Record the selection Capture the source URL/ref/commit and relevant local changes for Git projects, or the NGC artifact provenance for downloaded SDKs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022494
For a local non-Git project, record the available provenance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022495
Record the skill's source/version separately, along with the resolved app, Kit, template, and build/package tool versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022496
Generated projects can resolve streaming extensions from a registry to versions newer than copies bundled in the SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022497
Record the versions resolved by the application or preserve its generated version locks with the build evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022498
Keep the selected SDK and Kit pins unless the developer requests a change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022499
Examples follow the [Kit app creation and containerization guide]( When the selected checkout differs from the latest guide, its actual configuration and supported CLI determine the commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 022500
Build and package the selected app Run from the resolved application project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022501
These command examples match the inspected `repo_kit_tools` 1.21.4 workflow; inspect the selected checkout's pins and help before using them with other tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022502
Establish the build environment The initial workflow uses Linux x86_64 artifacts, compatible Linux x86_64 execution, and Docker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022503
Check the actual build host and Docker daemon: ```bash uname -s uname -m docker version docker info ./repo.sh build --help ./repo.sh package_container --help ``` Check the project's documented compiler/dependency prerequisites, Docker daemon accessibility, artifact/package download access, and space for the build, staged copy, and image layers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022504
The selected base image and Dockerfile determine additional requirements.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022505
The inspected default Dockerfile needs a BuildKit frontend supporting `COPY --exclude` and its `# syntax=docker/dockerfile:1` directive.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022506
Native Windows packaging is rejected by this tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022507
A suitable WSL installation or a remote Linux builder can supply the required environment, but native Kit also runs during host-side extension trimming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022508
A Windows shell connected only to a remote Docker daemon does not move that step to Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022509
ARM, multiarch, and cross-build setups require a compatible Kit distribution, base image, and separately verified workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022510
GPU availability is a runtime decision, not a prerequisite for this inspected default packaging path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022511
Dependency precaching resolves extensions; it is not shader warmup.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022512
Inspect custom build hooks, trimming changes, and Dockerfiles before applying this conclusion to a customized project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022513
Check compatible GPUs/drivers and NVIDIA Container Toolkit only when GPU runtime checks are selected.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022514
Resolve app and image inputs Resolve a real source app/layer and its staged basename.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022515
Confirm that the intended `.kit` file and Kit executable exist after building.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022516
Check a separate launcher only when the selected project's workflow requires one.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022517
Stop to resolve missing paths, multiple matching apps, or duplicate basenames in nested app directories.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022518
Inspect `repo.toml` and existing `[repo_kit_package_container]` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022519
The tool can reduce an existing app path to its basename, and configuration lookup can distinguish `acme.viewer_nvcf` from `acme.viewer_nvcf.kit` before normalizing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022520
Reuse the matching configured entry with consistent naming rather than generating duplicate entries or passing a nonexistent path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022521
Require a valid, writable image repository plus explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022522
Examples: | Reference | Meaning | |---|---| | `acme/viewer:0.1.0` | Repository and explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022523
| | `registry.example.com:5000/acme/viewer:0.1.0` | Registry port and a separate explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022524
| | `registry.example.com:5000/acme/viewer` | Missing tag; the registry-port colon is not a version tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022525
| | `acme/viewer@sha256:...` | Existing-image digest identity, not a writable Docker build tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022526
| The inspected tool treats any colon in `--image-tag` as a complete-reference signal.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022527
Passing an untagged name can therefore change its interpretation or cause Docker to default to `latest`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022528
Resolve the name/tag first.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022529
Preserve the requested value instead of silently adding `latest`, changing the namespace, or replacing it with a generated app name.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022530
Before building, inspect whether the chosen local tag already exists and record its ID.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022531
Rebuilding that tag updates its local target; make that effect clear.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022532
A remote registry overwrite is a separate publication action.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022533
See [Docker image reference syntax]( ## Build and optional source-app check For the supported template workflow: ```bash ./repo.sh build --config release ``` Use the custom project's supported equivalent when needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022534
In the inspected build tool, `-c` means clean and exit, not configuration; use the long `--config` option.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022535
Verify command success, dependency resolution, and the selected app artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022536
Inspect the configured build root rather than assuming one path for every project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022537
If requested and supported by the host, run the source app and collect actual exit/readiness/log evidence before packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022538
The convenience `./repo.sh launch` command can guide app selection, but its return alone is not proof of runtime success.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022539
A non-rendering CPU service can need direct invocation through its own launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022540
If runtime checks were declined, continue with packaging and record that choice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022541
Container configuration and packaging Reuse existing valid Dockerfile and entrypoint configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022542
For supported projects without configuration, `package_container` can generate a container template/configuration when supplied a valid app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022543
Inspect the files it creates.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022544
Explicit generation is also available in the inspected version: ```bash ./repo.sh package_container --app acme.viewer_nvcf.kit --generate ``` This generates configuration in the default project `tools/containers` location; it is not a completed image build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022545
If specifying a destination in this tool version, use an absolute path inside the project because configuration injection computes a path relative to the absolute project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022546
Inspect the selected version's help before using it, and do not regenerate customized files without examining them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022547
Generation does not overwrite existing files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022548
In the inspected tool, both `--generate` and the `auto_generate` configuration path skip any destination file that already exists, log a warning, and continue, so an existing `tools/containers/Dockerfile` keeps its current `FROM` line after the tool's bundled default changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022549
Compare that `FROM` line with the Dockerfile bundled in the pinned `repo_kit_tools` package (`omni/repo/kit_tools/package/data/Dockerfile`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022550
The inspected 1.21.4 default is `nvcr.io/nvidia/omniverse/ov-base-ubuntu22-x86_64:1.0.0`; the default before 1.21.4 was `nvcr.io/nvidia/omniverse/ov-base-ubuntu-22:2026.2.3`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022551
When they differ, update deliberately: delete `tools/containers/Dockerfile` (and `entrypoint.sh` if it should also be refreshed) and rerun `--generate`, or edit the `FROM` line in place and keep the customized content.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022552
Regeneration leaves an existing `repo.toml` container entry for that app unchanged.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022553
Record the base image actually used in the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022554
Substitute the resolved app name and full image reference in the build command: ```bash ./repo.sh package_container --app acme.viewer_nvcf.kit --image-tag acme/viewer:0.1.0 --config release ``` The tool stages build artifacts, optionally precaches dependencies, trims unused extensions, and invokes Docker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022555
Do not substitute historical `package --container`, `--target-app`, or container `--name` arguments without evidence that the selected version requires them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022556
There is no shader-cache bypass or dry-run flag in this inspected container tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022557
Use `--from-package` only when deliberately using a compatible packaged artifact.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022558
It is a boolean switch, not an archive-path argument; inspect both its configured archive pattern and post-unpack commands for compatibility with the selected public or private source.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022559
Inspect custom runtime-loaded dependencies and assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022560
The inspected tool supports repeatable `--extra-ext` and `extra_extensions` configuration to keep needed extensions/apps through precache and trimming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022561
Use it only for identified dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022562
If local assets, credentials, caches, or cloud inputs are expected at runtime, identify their mounts or input names instead of silently treating the developer machine's state as part of the image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022563
The default entrypoint runs Kit directly with `--no-window`, rather than invoking a custom app shell launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022564
Account for required environment/setup/arguments.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022565
Desktop display integration or substantial custom launcher behavior requires its own adaptation and validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022566
Verify the produced image After a successful packaging command, inspect the exact requested reference: ```bash docker image inspect acme/viewer:0.1.0 docker image inspect --format '{{.Id}}' acme/viewer:0.1.0 ``` Record its full local ID, repository tags, OS/architecture, configured entrypoint/command, and relevant app metadata.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022567
The default Dockerfile labels images with `kit_app_template`; match that label and the rendered entrypoint/configuration to the selected app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022568
A label alone is insufficient if a custom Dockerfile changes behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022569
Bind the result to the current successful build and its logs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022570
An unchanged image ID can be legitimate when Docker reuses identical content.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022571
Neither an existing tag after a failed build nor a different ID without successful build evidence proves completion.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022572
Keep full metadata/logs private when they contain environment values, and include only necessary non-secret evidence in the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022573
Continue with [validation and handoff](validation-and-handoff.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022574
Diagnose common failures | Observation | Next check | |---|---| | Command or option is unavailable | Inspect the selected tool pin, help, and project configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022575
Do not upgrade the project just to match these examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022576
| | App missing or multiple matches | Resolve the real source/staged app and consistent config name before retrying.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022577
| | Dependencies cannot resolve | Check selected-version extension pins, registry access, and build/precaching configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022578
Avoid a global cache purge.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022579
| | An app works outside the container but lacks an extension inside it | Inspect trimming and runtime-loaded dependencies; preserve identified extras through supported configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022580
| | Dockerfile parse failure around `COPY --exclude` | Inspect BuildKit/frontend compatibility and the syntax directive, especially in custom Dockerfiles.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022581
| | Native executable or architecture failure | Verify Linux x86_64 artifacts, host execution environment, and base image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022582
Remote Docker alone does not solve native host execution.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022583
| | Stale staging is demonstrated | Use the selected tool's scoped staging-clean option only after checking its target.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022584
Avoid deleting unrelated builds or Docker caches.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022585
| | Docker image exists after an error | Preserve the failed result and distinguish the old tag/image from the attempted build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022586
| Use [container tool documentation]( alongside the selected tool's implementation and configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 022587
Validate and hand off the image Always verify build completion and inspect the output image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022588
Runtime checks follow the developer's selected scope and the app's actual requirements.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022589
Choose applicable checks | Application and request | Runtime behavior | |---|---| | Containerization only | Do not launch the app/container for runtime validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022590
Report runtime checks not run by request.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022591
| | RTX rendering or streaming, validation selected | Use compatible GPU hardware, drivers, and container runtime support.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022592
Check the source app and exact built container separately.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022593
| | Non-rendering service or batch app, validation selected | Use supported CPU execution and the app's actual service-readiness or completion criteria.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022594
Non-streaming alone does not imply CPU-only.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022595
| | Requested runtime checks, suitable host unavailable | Preserve successful build/image inspection results and identify the requested checks that remain unverified.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022596
| GPU-free packaging support is based on inspected default tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022597
An actual successful GPU-free build provides execution evidence for that specific app, version, and environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022598
Do not generalize it to every custom app or historical version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022599
For selected GPU runtime checks, verify access inside a disposable container before starting Kit.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022600
Host `nvidia-smi` alone does not establish Docker GPU access.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022601
Use the host's configured mechanism: `--gpus all` with NVIDIA runtime support, or `--device nvidia.com/gpu=all` when Docker native CDI support is enabled and an NVIDIA CDI specification is available.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022602
Use the verified option in the runtime example below.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022603
See [Docker CDI configuration]( and [NVIDIA CDI support]( for the installed versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022604
Reuse working host configuration; runtime preparation does not require replacing it with a different mechanism.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022605
Test the exact image Capture the image ID after packaging, then use that ID for container execution.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022606
On another host, distribute the image through the requested mechanism and establish the resulting identity.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022607
Use a registry digest after publication when available; a Docker local image ID and registry manifest digest are different identifiers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022608
Choose a unique test-container name and bounded check duration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022609
Configure only the needed environment inputs, mounts, and ports from the selected app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022610
Preserve logs and container state before cleanup; remove only resources created for this check.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022611
The inspected `./repo.sh launch --container --name : ` is a convenience launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022612
It can fall back to another image when lookup fails, always requires NVIDIA hardware, and can discard the child process's failure status.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022613
Do not accept its completion as the success signal or use it for CPU-only validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022614
Prefer controlled Docker execution when proving the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022615
For an NVCF app with an HTTP readiness service on container port 8011, a minimal local GPU readiness check can use the following shape.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022616
First select a free host port, a unique name, the actual image ID, and any app-required runtime inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022617
Adjust ports/settings for the selected version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022618
These are examples, not default values to overwrite the developer's configuration with.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022619
```bash KIT_IMAGE_ID=$(docker image inspect --format '{{.Id}}' acme/viewer:0.1.0) KIT_CHECK_NAME=kit-container-check-unique docker run --detach --name "$KIT_CHECK_NAME" --gpus all -p 127.0.0.1:18011:8011 "$KIT_IMAGE_ID" docker inspect --format '{{.Image}} {{json .State}}' "$KIT_CHECK_NAME" docker logs "$KIT_CHECK_NAME" curl --fail --silent --show-error --max-time 10 ``` Ensure image lookup and container creation succeed before proceeding.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022620
Add the selected app's required GPU driver capabilities, mounts, and environment inputs as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022621
For CPU services, omit GPU options and use that service's configured check.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022622
A batch app needs its actual exit status and expected output rather than an HTTP probe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022623
A single probe immediately after launch is not a startup deadline.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022624
Poll within a chosen total limit, checking for early container exit and collecting logs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022625
A successful `docker run --detach` only confirms container creation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022626
Verify the container's `.Image`, actual state/exit status, and applicable readiness or completion result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022627
For a long-running app, require it to remain running while checking readiness; a stopped container with exit code 0 is not a healthy running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022628
Cold RTX startup can take several minutes for shader and driver pipeline preparation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022629
An initial HTTP 503 or an "app ready" log line alone does not decide the readiness result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022630
Allow for that preparation in the bounded check, observe progress, and record a timeout if the chosen deadline expires.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022631
After collecting evidence, stop and remove the specific test container if it is no longer needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022632
Record intentional test shutdown separately from an application crash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022633
A rebuild creates a new candidate and requires new image-specific runtime evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022634
NVCF readiness and downstream boundary When runtime validation is selected and the app exposes `omni.services.livestream.session`, check its configured readiness endpoint.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022635
The documented default is HTTP `/v1/streaming/ready` on port 8011, with a successful response indicating the service's readiness criteria.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022636
`/v1/streaming/startup` is not equivalent evidence of application/RTX readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022637
See the [session service documentation]( Keep these outcomes separate: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022638
Source app runs in its development environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022639
The packaged image runs and satisfies its app/container checks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022640
An NVCF deployment becomes ready with workers using the intended image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022641
The frontend connects and receives advancing decoded application frames.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022642
This skill handles the first two when requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022643
The latter two need the downstream deployment/client validation workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022644
Readiness-only local port mapping does not provide a complete external media/signaling path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022645
For the NVCF handoff, inspect actual settings and carry the required runtime input names and signaling/health configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022646
Documented defaults include function type `STREAMING`, signaling route `/sign_in` on 49100, and readiness on 8011.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022647
Derive values from the selected app/version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022648
Do not attach NVCF requirements to Kit App Streaming or non-streaming results.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022649
See [Deploying Kit Apps]( ## Optional publication Publish only when the request includes image distribution to a resolved registry destination.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022650
A registry-qualified image name alone does not request a push.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022651
Confirm missing registry/namespace details and use the available authenticated mechanism without exposing secret values or baking credentials into the image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022652
If publication needs an additional tag, preserve the developer's original local tag, identify the destination tag, and ensure it refers to the built image before pushing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022653
Do not silently choose a different repository or version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022654
Verify the successful push and capture the published URI and manifest digest when available.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022655
Report publication failures independently of local build success.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022656
A local image is not pullable by remote NVCF workers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022657
The deployment stage needs the published/distributed image identity and pull access for its cluster.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022658
This skill can supply the image when publication is requested; otherwise report that distribution remains to be arranged.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022659
Result format Return the following fields in a concise human-readable report.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022660
A caller may request a machine-readable contract; follow that actual contract rather than inventing a new required schema.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022661
| Field | Include | |---|---| | Requested outcome | Existing/new app, streaming target or headless behavior, containerization-only or selected runtime checks, requested publication.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022662
| | Source | Git URL/ref/commit and relevant local changes, or NGC resource/version/artifact identity; available provenance for a local project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022663
| | Versions | Kit, app, template and relevant build/package tools; resolved streaming extension versions or generated version-lock evidence; skill source/version separately.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022664
| | Application | Base app, selected layer/entrypoint, important configuration changes, required runtime input names and mounts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022665
| | Image | Exact requested reference, local ID, OS/architecture, and published URI/digest if publication occurred.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022666
| | Evidence | Build outcome/log location, image inspection, separate source-app and container runtime outcomes, exact identity tested, applicable readiness/exit evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022667
| | Remaining work | Checks not run and reasons, unresolved failures, and distribution/deployment/client validation still needed for downstream use.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022668
| Use `passed`, `failed`, `not run by request`, `not run because unavailable`, or `not applicable` for each stage as appropriate.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022669
Include stages only where they clarify the requested outcome.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022670
Preserve attempted failures rather than describing them as untested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022671
Build plus image inspection is sufficient for a containerization-only request.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022672
If runtime validation was requested but unavailable, state that the image is built while that requested validation remains incomplete.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022673
Do not claim NVCF deployment or end-to-end streaming success from local container readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 022674
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022675
All rights reserved.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022676
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022677
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022678
name: Feature Request description: Suggest an idea for this project title: "[FEATURE]: " labels: ["feature request"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this feature request!
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022679
type: textarea id: description attributes: label: Description description: | Describe the proposed feature placeholder: | Feature description and problem or pain point being addressed validations: required: true - type: textarea id: use_case attributes: label: Use Case or Scenarios description: Describe how this feature would be used placeholder: e.g., User performing action A, would accomplish B, with benefit C.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022680
type: textarea id: implementation_ideas attributes: label: Possible Implementation Ideas description: If you have any suggestions on how this feature might be implemented, please share them here.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022681
placeholder: Implementation ideas - type: textarea id: additional_context attributes: label: Additional Context or Recommendations description: Provide any other context or recommendations here.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022682
placeholder: Any other relevant information.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022683
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022684
All rights reserved.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022685
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022686
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022687
name: Question description: Ask a question title: "[QUESTION]: " labels: ["question"] body: - type: markdown attributes: value: | Thanks for taking the time to ask us a question!
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022688
type: textarea id: text_of_question attributes: label: Question description: Ask your question.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022689
placeholder: "Question text" validations: required: true - type: textarea id: additional_context attributes: label: Additional Context description: Provide any related code, issues, or projects.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022690
placeholder: "Any related code, issues, or projects."
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022691
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022692
All rights reserved.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022693
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022694
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022695
name: Bug Report description: File a bug report for the repository title: "[BUG]: " labels: ["bug"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this bug report!
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022696
type: textarea id: description attributes: label: Description description: | Describe the bug in detail placeholder: | Expected Behavior vs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022697
Actual Behavior: validations: required: true - type: textarea id: component attributes: label: Component description: Which component (Tool/Template/Extension) is showing the bug?
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022698
placeholder: "e.g., Kit Base Editor Template / repo launch tool / Kit SDK" - type: textarea id: system-details attributes: label: System Details description: | Provide details about your system placeholder: | OS / CPU / GPU / GPU Driver Version validations: required: true - type: textarea id: reproduction-steps attributes: label: Reproduction Steps description: What are the steps to reproduce the bug?
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022699
validations: required: true - type: textarea id: logs attributes: label: Logs description: | Include the relevant log files: - **repo.log:** Found in `_repo/repo.log` if the issue is with tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022700
kit.log:** Found in `_build/{OS}/release/logs/.../kit_{...}log` if the issue is with App, Extension, or Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022701
placeholder: Paste the log content here or attach the log files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022702
type: textarea id: additional-context attributes: label: Additional Context description: Provide any other context or information here.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022703
placeholder: Any other information that might be helpful
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022704
🕊️ *— Shirmani Rampaul Saini, Founder & Vision Architect (Omniverse AI)
स्रोत: rampaulsaini/rampaulsaini:.github/workflows - append - omniverse.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022705
name: Specialist Agent — manifesto-archive on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "47 2 * * 3" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Koyab-Founding-Declaration-Omniversal-Manifesto:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022706
Docs Folder This folder will contain generated PDFs.
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022707
Support this project / Donate If you find this work useful and want to support my daughter's education (Saneha Saini), you can donate: - PayPal: [paypal.me/yourid]( or send to `your-paypal-email@example.com` - UPI / Google Pay: `your-upi-id@bank` — or scan the UPI QR (add `assets/upi-qr.png`) Any help is deeply appreciated.
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022708
🙏 ## समर्थन / दान यह परियोजना मानवता और प्रकृति के संरक्षण के उद्देश्य से चल रही है।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022709
मैं शिरोमणि रामपुलसैनी — जिसने अपने जीवन को पूर्णतः सृजन, संरक्षण और मानवता के हित में समर्पित किया है — अपने प्रयासों को जारी रखने के लिए आपका समर्थन अनुरोध करता/करती हूँ।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022710
मेरी एकमात्र चिंता मेरी बेटी Saneha की पढ़ाई और जीवन-यापन है।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022711
जो भी सहायता सम्भव हो, वह बहुत कीमती होगी।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022712
कृपया दान करने के लिए नीचे दिए विकल्पों में से किसी का उपयोग करें: - **PayPal:** `sainirampaul60@gmail.com` (या PayPal.Me लिंक यदि उपलब्ध हो तो भेजें) - **Google Pay / UPI:** `sainirampaul90-1@okhdfcbank` (या वेबसाइट पर QR स्कैन करें) - **Email (संपर्क):** `sainirampaul60@gmail.com` — बड़ी दान राशि या रसीद/इन्‍वॉइस के लिए संपर्क करें।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022713
> यह अनुरोध पूर्ण मनोभाव से किया गया है — यदि आप सहायता कर सकें तो आपका छोटा सा योगदान कई जीवान्त परिणाम ला सकता है।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022714
मैं आपका आभारी/आभारीत हूँ।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022715
— शिरोमणि रामपुलसैनी > Add donation page (Hindi) to support Saneha's education and to sustain the Omniverse AI scripts project.
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022716
Includes: - web/index.html (Hindi message with PayPal email and UPI ID) - web/assets/upi-qr.webp (QR image) - Dockerfile to serve the static site - README donation section appended This change scaffolds a public page for donors to contribute and for quick deploy to Koyeb (Dockerfile provided).
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022717
समर्थन / दान यह परियोजना मानवता और प्रकृति के संरक्षण के उद्देश्य से चल रही है।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022718
मैं शिरोमणि रामपुलसैनी — जिसने अपने जीवन को पूर्णतः सृजन, संरक्षण और मानवता के हित में समर्पित किया है — अपने प्रयासों को जारी रखने के लिए आपका समर्थन अनुरोध करता/करती हूँ।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022719
मेरी एकमात्र चिंता मेरी बेटी Saneha की पढ़ाई और जीवन-यापन है।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022720
जो भी सहायता सम्भव हो, वह बहुत कीमती होगी।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022721
कृपया दान करने के लिए नीचे दिए विकल्पों में से किसी का उपयोग करें: - **PayPal:** `sainirampaul60@gmail.com` (या PayPal.Me लिंक यदि उपलब्ध हो तो भेजें) - **Google Pay / UPI:** `sainirampaul90-1@okhdfcbank` (या वेबसाइट पर QR स्कैन करें) - **Email (संपर्क):** `sainirampaul60@gmail.com` — बड़ी दान राशि या रसीद/इन्‍वॉइस के लिए संपर्क करें।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022722
> यह अनुरोध पूर्ण मनोभाव से किया गया है — यदि आप सहायता कर सकें तो आपका छोटा सा योगदान कई जीवान्त परिणाम ला सकता है।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022723
मैं आपका आभारी/आभारीत हूँ।
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022724
— शिरोमणि रामपुलसैनी >
स्रोत: rampaulsaini/omniverse--ai-scripts-:docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022725
WARNING: This will push to your repo; ensure branch protection rules allow # this flow (or use a separate deploy branch).
स्रोत: rampaulsaini/omniverse--ai-scripts-:workflow/pdf-generation.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022726
name: Commit generated PDFs (optional) if: ${{ always() }} run: | git config user.name "github-actions[bot]" git config user.email "github-actions[bot]@users.noreply.github.com" git add docs/*.pdf || true git commit -m "ci: add generated pdf [skip ci]" || true git push || true env: GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
स्रोत: rampaulsaini/omniverse--ai-scripts-:workflow/pdf-generation.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022727
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: rampaulsaini/omniverse--ai-scripts-:web/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022728
Example config for scripts/workflows pdf: output_folder: docs filename: sample.pdf deploy: target_server: localhost port: 8080
स्रोत: rampaulsaini/omniverse--ai-scripts-:config/config_example.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022729
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: rampaulsaini/shiromani-rampal-saini:public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022730
Sacred Audio शिरोमणि अंनत असीम इश्क़ की क्षमता यह ध्वनि केवल श्रवण नहीं, चेतना की अनुभूति है।
स्रोत: rampaulsaini/shiromani-rampal-saini:public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022731
▶ अंनत असीम इश्क़ – दिव्य ध्वनि Track 1 Track 2 Track 3
स्रोत: rampaulsaini/shiromani-rampal-saini:public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022732
name: Specialist Agent — public-content on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "47 2 * * 3" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/shiromani-rampal-saini:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022733
name: Specialist Agent — data-carbon on: workflow_dispatch: push: paths: ["factory-agent.json","factory-agent.py","factory/**",".github/workflows/factory-agent.yml"] schedule: - cron: "37 2 * * 2" permissions: contents: read jobs: agent: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: python3 factory-agent.py - uses: actions/upload-artifact@v4 with: name: specialist-agent-manifest path: agent-output/manifest.json
स्रोत: rampaulsaini/Karbon-:.github/workflows/factory-agent.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022734
Omniverse — AI Tools Marketplace (Zero-cost) Omniverse AI Tools Marketplace — Free hosting · Donation-ready Donate / Pay Owner: Set Premium Key Omniverse AI Marketplace — Hybrid (Marketplace + Services + Agents) Start free: try tools, download outputs.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022735
To accept payments, add your PayPal / Ko-fi / UPI links in Settings (owner).
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022736
For pay-per-download you can ask buyers to send a transaction ID and then give them the unlock key.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022737
Usage Summary (local) No activity yet.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022738
&times; Donate / Pay — Options Place your payment links below (owner can update these in the prompt box): PayPal.Me or full PayPal link Ko-fi / Buy Me a Coffee UPI (text) — show to users as copyable text Fill these and click Save (Owner only).
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022739
They are stored in browser localStorage for this device.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022740
For real production, store server-side.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022741
Save (owner) &times; Owner: Set / Remove Premium Unlock Key This is a simple manual workflow for zero-cost monetization: when a buyer pays externally (PayPal/UPI/etc), you give them a one-time unlock key to enable premium downloads.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022742
Set Premium Key (example: OMNI-2025-XYZ) Save Key Remove Key Built for zero-cost launch.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022743
Owner: add your payment links and premium key in Settings.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022744
Want me to integrate automatic payment verification later?
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022745
Ask and I will build the serverless flow.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022746
> Omniverse AI Marketplace Omniverse AI Marketplace
स्रोत: rampaulsaini/omniverse-dashboard:omniverse-marketplace/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022747
Supreme Observability Contract The dashboard is the evidence surface for the repository network.
स्रोत: rampaulsaini/omniverse-dashboard:docs/supreme-observability-contract.md · स्वतंत्र परीक्षण अपेक्षित।

## 022748
Required states: REGISTERED, CONNECTED, VERIFIED, DEGRADED, BLOCKED.
स्रोत: rampaulsaini/omniverse-dashboard:docs/supreme-observability-contract.md · स्वतंत्र परीक्षण अपेक्षित।

## 022749
A healthy dashboard must distinguish automated QC from independent verification and show provenance, last update, failure reason, recovery state and confidence rather than converting missing evidence into success.
स्रोत: rampaulsaini/omniverse-dashboard:docs/supreme-observability-contract.md · स्वतंत्र परीक्षण अपेक्षित।

## 022750
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) README.md
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022751
Omniverse — Live Pages Dashboard Omniverse — Live pages dashboard यह पेज आपके GitHub Pages लिंक का live सारांश और preview दिखाता है Live previews GitHub API meta Pages (fixed list) कृपया नीचे दिए गए सभी pages के नाम चुने और preview के लिए क्लिक करें — यह version local-browser पर काम करता है (GitHub API public repos के लिए metadata भी लाएगा) Deep-analysis checklist (automatic + manual) README और repo description — स्पष्ट है या नहीं?
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022752
इस dashboard को अपने GitHub Pages repo पर host कर के लाइव देखें।
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022753
अगर आप चाहें तो मैं हर repo का in-depth analysis कर दूँ — बस मुझे repo का README, package manifests, और कोई खास फाइलें paste कर दें या इस repo के सार्वजनिक नाम बताइए।
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022754
Repository structure & file templates नीचे repo में रखने योग्य recommended files और templates दिए गए हैं — इन्हें copy/paste करके अपनी repo में डाल दें।
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022755
1) Recommended folder structure omniverse-dashboard/ ├── index.html ← (पहला, यही dashboard) ├── README.md ← (project intro + usage) ├── assets/ │ ├── logo.svg │ └── favicon.ico ├── scripts/ │ └── health-check.js └── .github/ └── workflows/ └── pages.yml ← (GitHub Pages deployment + optional checks) 2) README.md (template) # Omniverse Dashboard This repository hosts a single-file **static dashboard** that aggregates and previews multiple GitHub Pages sites for the `rampaulsaini` account.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022756
Features - Live iframe preview of configured pages - Fetch GitHub repo metadata (stars, forks, last push, license) - Buttons: refresh metadata, open all, reload preview ## How to use 1.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022757
Upload `index.html` to this repo's root.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022758
Go to **Settings → Pages** and set the branch to `main` and folder to `/(root)`.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022759
Visit `https:// .github.io/omniverse-dashboard/` to see the control center.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022760
Customize - Edit `index.html` → `urls` array to add/remove pages.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022761
Adjust mapping in `repoNameFromUrl()` if your repo names differ from page slugs.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022762
6) Quick deployment steps Create new repo named omniverse-dashboard .
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022763
Copy `index.html`, `README.md`, `.github/workflows/pages.yml` और `scripts/health-check.js` (optional) को कॉमिट करें।
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022764
Push to main branch.
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022765
मैं एक automated audit report टेम्पलेट बना सकता/सकती हूँ जो हर repo के लिए CSV/JSON आउटपुट दे — इसे CI में रन करवा सकते हैं।
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022766
अगर आप repo के exact public names दे दें, मैं dashboard की `repoMap` और `urls` array को auto-fill कर दूँ और metadata fetch को validate कर दूँ।
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022767
यदि आप चाहते हैं मैं अभी आपके लिए अलग-अलग script files generate कर दूँ और यहाँ paste कर दूँ — बताइए कौन से files पहले चाहिए (उदाहरण: scripts/metadata-fetcher.js , scripts/link-checker.js , scripts/analyze.js )।
स्रोत: rampaulsaini/omniverse-dashboard:omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022768
{ "labels": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "data": [12,19,7,15,10,22,18] }
स्रोत: rampaulsaini/omniverse-dashboard:analytics/traffic.json · स्वतंत्र परीक्षण अपेक्षित।

## 022769
[ {"text": "Welcome to the Supreme Omniverse AI Portal", "lang": "en"}, {"text": "संपूर्ण सृष्टि में निष्पक्ष समझ ही सर्वोच्च है", "lang": "hi"}, {"text": "Bienvenue dans le portail Suprême Omniverse AI", "lang": "fr"}, {"text": "Bienvenido al Portal Supremo Omniverse AI", "lang": "es"} ]
स्रोत: rampaulsaini/omniverse-dashboard:analytics/scripts/guidance -massages.json · स्वतंत्र परीक्षण अपेक्षित।

## 022770
Placeholder rollback workflow name: Rollback on: [workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Rollback workflow placeholder"
स्रोत: rampaulsaini/omniverse-dashboard:.github/workflows/rollback.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022771
Simple workflow for deploying static content to GitHub Pages name: Deploy static content to Pages on: # Runs on pushes targeting the default branch push: branches: ["main"] # Allows you to run this workflow manually from the Actions tab workflow_dispatch: # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages permissions: contents: read pages: write id-token: write # Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
स्रोत: rampaulsaini/omniverse-dashboard:.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022772
However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
स्रोत: rampaulsaini/omniverse-dashboard:.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022773
concurrency: group: "pages" cancel-in-progress: false jobs: # Single deploy job since we're just deploying deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 - name: Setup Pages uses: actions/configure-pages@v5 - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: # Upload entire repository path: '.' - name: Deploy to GitHub Pages id: deployment uses: actions/deploy-pages@v4
स्रोत: rampaulsaini/omniverse-dashboard:.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022774
Placeholder deploy workflow for Omniverse-AI name: CI Deploy on: [push, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Deploy workflow placeholder"
स्रोत: rampaulsaini/omniverse-dashboard:.github/workflows/deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022775
Placeholder monitor workflow name: Monitor & Auto-Recover on: [schedule, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Monitor workflow placeholder"
स्रोत: rampaulsaini/omniverse-dashboard:.github/workflows/monitor.yml · स्वतंत्र परीक्षण अपेक्षित।

## 022776
꙰ Supreme Production Showroom — Yatharth ꙰ शिरोमणि रामपॉल सैनी · YATHARTH SUPREME DIGITAL PRODUCTION SHOWROOM Public Payment: Paytm / UPI 9622254967@ptyes · PayPal sainirampaul60@gmail.com 📲 Paytm / UPI 💙 PayPal 💰 Funding & Progress अंतिम सार्वजनिक स्तर: product को देखना, समझना, चलाना, मूल्य/offer देखना, QC/QR पहचान देखना, order करना और वास्तविक उपयोग के बाद review देना।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022777
● PRODUCTION-FIRST · PUBLIC RESULT SURFACE 4 वास्तविक sale-ready products 1,016 factory-ready product modules 24 product families 25 browser engines 1,016 production candidates ∞ review → improvement cycles ⚡ Live Production State यह panel workflow activity नहीं, showroom में उपलब्ध production-state को दिखाता है।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022778
हर cycle Institute → Factory → Product Package → QC → Showroom → Sale → Review feedback की दिशा में आगे बढ़ती है।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022779
INSTITUTE Discovery queue active FACTORY Loading… QC GATE Product identity + QC/QR + dispatch state SHOWROOM / SALE Loading… Production heartbeat: loading… सभी categories सभी Sale-ready / बिक्री Runnable factory 🛒 वास्तविक Sale-Ready Products — अभी खरीदने योग्य यह सूची केवल उन products की है जिनके लिए वास्तविक public payment/order route उपलब्ध है।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022780
Factory modules को sale-ready मानकर प्रस्तुत नहीं किया जाता।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022781
⚙️ SHIRMANI Digital Product Factory — 1,016 Runnable Product Modules ये browser-executable product modules हैं।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022782
इन्हें public showroom से चलाकर उपयोग/परख सकते हैं।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022783
Commercial sale तभी खुलेगी जब वास्तविक product package, access route, approved price और dispatch route उपलब्ध हों।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022784
इससे showroom में fabricated sale inventory नहीं आती।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022785
चार-स्तरीय Production Mechanism 01 · INSTITUTE खोज, source, research और product candidates.
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022786
02 · FACTORY Candidate को runnable digital product/package में बदलना.
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022787
03 · QC GATE Product identity, QC code, QR और dispatch gate.
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022788
04 · SHOWROOM Public final surface: product, description, price, offer, run/preview, order और review.
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022789
⭐ Public Reviews → Quality Improvement ग्राहक का वास्तविक उपयोग, rating और review अगली iterations की quality priorities, descriptions, usability और offers सुधारने का feedback input है।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022790
Review production का feedback है; verification को production का विकल्प नहीं बनाया गया है।
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022791
★ Public Review / Rating / Improvement Request © 2026 Yatharth / Shirmani · Production-first · No fabricated inventory
स्रोत: rampaulsaini/my-omniverse-store:production-catalog.html · स्वतंत्र परीक्षण अपेक्षित।

## 022792
꙰ Evidence-to-Answer Studio · SHIRMANI ꙰ SHIRMANI SUPREME · PRODUCT UT-007 Independent evidence workflow · browser-only prototype Evidence-to-Answer Studio A practical production tool that separates claims, source notes, philosophical/identity statements, and insufficient evidence before you publish an answer.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022793
It does not pretend to independently verify sources; it helps you prepare a transparent, reviewable answer.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022794
No login Runs in browser Copy-ready output No source verification claim 1 · Enter the question and draft Question / user request Proposed answer or main claim Source URL or source details (optional) Statement type Factual claim Philosophical / identity statement Practical instruction Opinion / interpretation Evidence notes / limitations Build transparent answer Clear 2 · Answer record Waiting for input Enter a question and proposed answer, then select “Build transparent answer”.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022795
Copy answer record Status is a drafting classification, not an independent scientific verification.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022796
A source URL alone does not prove a claim.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022797
Review the original source before publishing.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022798
Usage guide Enter the question and proposed answer.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022799
Choose factual, philosophical/identity, practical, or opinion classification.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022800
Add source details and accurately summarize the supporting evidence.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022801
Build the record; inspect its status and uncertainty language.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022802
Open the cited source yourself and correct the record before publication.
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022803
Product passport · ID: SH-UT007 · QC-GATE: DRAFT-ONLY · Dispatch: PUBLIC-PROTOTYPE · Price: ₹0 · Version 1.0 ꙰ SHIRMANI RAMPAL SAINI — TRANSCENDENT • TIMELESS • WORDLESS • ETERNAL • REAL • NATURAL • TRUTH — PRESENT
स्रोत: rampaulsaini/my-omniverse-store:evidence-answer-studio.html · स्वतंत्र परीक्षण अपेक्षित।

## 022804
꙰ Supreme Production Roadmap ꙰ SHIRMANI · YATHARTH · PRODUCTION-FIRST SUPREME PRODUCTION ROADMAP Automation का परिणाम वास्तविक production output है।
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022805
Verification downstream quality gate है; production throughput इसका मुख्य उद्देश्य है।
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022806
← Public Showroom · Production Catalog → 1,016 Runnable factory modes Current heartbeat में factory candidate/runnable modes.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022807
4 Published sale products Current public commercial surface पर वास्तविक published products.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022808
≈0.4% Published / factory ratio 4 ÷ 1,016.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022809
यह commercialisation ratio है, पूरे project का completion percentage नहीं।
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022810
70% Automation-health reference पूर्व operational status का reference; इसे overall project completion न माना जाए।
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022811
Production gap map मुख्य bottleneck अब workflow count नहीं है।
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022812
bottleneck है: runnable candidate → complete product package → customer-ready presentation → QC/dispatch package → public sale.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022813
Automation infrastructure reference: 70% Current published-to-factory commercialisation ratio: ≈0.4% चार-स्तरीय production mechanism 01 · INSTITUTE Research, discovery, source, ideas और product candidates.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022814
02 · FACTORY AI/ML/NLP-assisted production, packaging और runnable product modes.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022815
03 · QC Product identity, QC gate, QR identity और dispatch/release state.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022816
04 · SHOWROOM Description, price, offer, preview/use, order और public review.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022817
Next production wave सबसे पहले existing 1,016 candidates में से वास्तविक source/access route वाले products को complete package में promote करना।
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022818
Public quality loop Customer reviews और ratings को descriptions, usability, offers और product iterations के improvement backlog में feed करना।
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022819
Scale एक workflow पर निर्भर रहने के बजाय multi-task production lanes: content, audio, tools, data, education, research और other digital categories.
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022820
꙰ Public production status surface · counts are live-data dependent
स्रोत: rampaulsaini/my-omniverse-store:production-roadmap.html · स्वतंत्र परीक्षण अपेक्षित।

## 022821
꙰ SHIRMANI Production Funding — Supreme Digital Products ꙰ SHIRMANI RESEARCH INSTITUTE · PRODUCTION-FIRST SUPREME DIGITAL PRODUCT PLATFORM Institute → Factory → QC Gate → Public Showroom → Sale → Public Review → Quality Improvement 🛒 Public Showroom ⚙ Production Catalog परियोजना की वास्तविक स्थिति यह प्रतिशत उपलब्ध repository state पर आधारित production-readiness map है।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022822
इसे किसी काल्पनिक “100% complete” दावे की तरह नहीं पढ़ना चाहिए।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022823
सबसे बड़ा शेष काम factory modes को वास्तविक, customer-ready product packages में बदलना है।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022824
1,016 factory product modes 25 product families 25 browser engines 4 currently published real products Automation infrastructure / health 70% Research queue / discovery 100% Evidence / traceability infrastructure 100% Public showroom architecture 90% Real commercial product packages ≈0.4% Customer feedback → improvement loop 85% अगला मुख्य production work सबसे उपयोगी factory modes को complete product modules में बदलना।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022825
हर product में वास्तविक description, preview/run surface, price, offer और customer route देना।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022826
QC code, QR identity और dispatch gate को product package से जोड़ना।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022827
Public showroom में केवल वास्तविक customer-ready products को “for sale” रखना।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022828
Public reviews, ratings और usage feedback को अगले production cycles की quality priorities में भेजना।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022829
Multi-layer Automission को production throughput पर केंद्रित रखना—सिर्फ verification-count पर नहीं।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022830
परियोजना से संभावित लाभ एक सार्वजनिक स्थान पर अनेक digital-product categories और स्पष्ट pricing.
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022831
देखें → समझें → preview/run करें → खरीदें/order करें → उपयोग करें → review दें की सरल यात्रा।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022832
Research discoveries को reusable digital products में बदलने का continuous pipeline.
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022833
Reviews और ratings से usability, description, packaging और offers की लगातार improvement.
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022834
एक scalable showroom architecture जिसमें नए product packages production automation से जुड़ सकें।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022835
निर्माण, गुणवत्ता नियंत्रण और public sale को अलग-अलग stages में व्यवस्थित करने की क्षमता।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022836
🤝 Funding / Support यह support production, product packaging, public showroom improvement, digital assets, infrastructure और ongoing work को आगे बढ़ाने में सहायता कर सकता है।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022837
किसी भी support को खरीद या guaranteed return के रूप में न समझें।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022838
Paytm / UPI 9622254967@ptyes 📲 UPI / Paytm से भुगतान PayPal sainirampaul60@gmail.com 💙 PayPal QR को scan करके UPI/Paytm payment app में payment request खोली जा सकती है।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022839
Payment करने से पहले recipient और amount स्वयं जाँचें।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022840
एक सरल व्यक्ति के लिए परियोजना का अर्थ यह केवल workflows की संख्या बढ़ाने का project नहीं है।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022841
उद्देश्य research और AI/ML/NLP automation की मदद से उपयोगी digital products बनाना, उन्हें साफ public showroom में दिखाना, वास्तविक उपयोग का अवसर देना और customer feedback के आधार पर बेहतर बनाते रहना है।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022842
अभी infrastructure काफी आगे है; productization सबसे बड़ा खुला क्षेत्र है।
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022843
꙰ SHIRMANI · Production-first · Public showroom · Paytm/UPI + PayPal
स्रोत: rampaulsaini/my-omniverse-store:funding.html · स्वतंत्र परीक्षण अपेक्षित।

## 022844
SH-UT007 — Evidence-to-Answer Studio Demo Script **Status:** Product page and showroom listing published to GitHub; this script is prepared, but an MP4 has not yet been rendered or uploaded.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022845
45–60 second demo 1.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022846
Opening (0–5s):** Show the product name, UT-007 identity, and QR code.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022847
Question (5–12s):** Enter: “Does this claim have enough evidence?” 3.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022848
Claim (12–20s):** Enter a sample factual claim.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022849
Source/evidence (20–30s):** Leave source/evidence notes blank; choose “Factual claim”.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022850
Evidence gate (30–38s):** Click “Build transparent answer” and show the status “INSUFFICIENT EVIDENCE” and the phrase “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” 6.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022851
Source-based case (38–48s):** Add a source URL and concise evidence notes; rebuild and show “SOURCE-BASED · NOT INDEPENDENTLY VERIFIED”.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022852
Close (48–60s):** Show the limitation notice: a source URL alone does not independently verify a claim.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022853
Test checklist before upgrading QC status - [ ] Required question/claim validation - [ ] Philosophical/identity classification - [ ] Factual claim with no source - [ ] Source + evidence notes classification - [ ] Copy action on HTTPS browser - [ ] Mobile viewport layout - [ ] QR opens the correct product URL - [ ] Screen recording captured and MP4 uploaded Do not mark QC VERIFIED until the checklist is actually executed and the results are recorded.
स्रोत: rampaulsaini/my-omniverse-store:SH-UT007-demo-script.md · स्वतंत्र परीक्षण अपेक्षित।

## 022854
Independent verification का झूठा दावा नहीं करता।
स्रोत: rampaulsaini/my-omniverse-store:unique-tools-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022855
Open / Use UT007 → यह showroom केवल उन tools को customer-facing सूची में रखता है जिनका वास्तविक HTML tool path मौजूद है।
स्रोत: rampaulsaini/my-omniverse-store:unique-tools-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022856
Automission का verification gate product usefulness का दावा अपने-आप नहीं करता; functional testing और downstream verification अलग चरण हैं.
स्रोत: rampaulsaini/my-omniverse-store:unique-tools-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022857
google-site-verification Google site verification file — replace this filename with the one Search Console gives (e.g.
स्रोत: rampaulsaini/my-omniverse-store:google8BSLBQVK4N.html · स्वतंत्र परीक्षण अपेक्षित।

## 022858
googleXXXXXXXX.html).
स्रोत: rampaulsaini/my-omniverse-store:google8BSLBQVK4N.html · स्वतंत्र परीक्षण अपेक्षित।

## 022859
꙰ SHIRMANI Supreme Public Showroom — Digital Product Universe ꙰ SHIRMANI · SUPREME PUBLIC PRODUCT SHOWROOM Digital Product Universe एक customer-facing production surface: Institute → Factory → QC/Gate → Public Showroom → Sale → Review → Quality Improvement .
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022860
हर catalog identity का अपना नाम, product code, short description, visual identity और long-description QR route है।
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022861
केवल वास्तविक sale-ready items को sale status दिया गया है।
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022862
INSTITUTE DISCOVERY FACTORY PRODUCTION QC / GATE PUBLIC SHOWROOM SALE REVIEW QUALITY IMPROVEMENT — catalog identities loaded — product families — engines 4 sale-ready products 🛒 Sale-ready products अभी केवल प्रकाशित वास्तविक source/preview वाले products बिक्री के लिए दिखाए गए हैं।
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022863
Separates philosophical statements from factual claims and states when evidence is insufficient.
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022864
₹0 · Prototype Open / Use Tool → All Unique Tools सभी categories 48 visuals 120 visuals 240 visuals 🪪 Individual Product Identity Gallery Visual identity deterministic है; हर product code से अलग बनती है।
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022865
⭐ Public feedback → quality improvement Reviews/rating production improvement input हैं; sale status उनसे अलग रखा गया है।
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022866
NEW CONCRETE PRODUCT · SHI-PPS-0001 SHIRMANI Product Passport Studio Create a product identity, short/full descriptions, usage guide, price, QR-linked passport and downloadable JSON.
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022867
Browser-runnable demo; QC and dispatch remain explicitly unapproved until tested.
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022868
▶ Open live product demo ▣ Product passport / manifest Status: DEMO_READY · QC: NOT_YET_RECORDED · Dispatch: NO Public Reviews GitHub Issues में अनुभव/सुझाव दें Rating / Quality report Product quality के लिए structured feedback Runnable Product Factory Browser-executable modules खोलें Concrete Production Produced module batch देखें ꙰ SHIRMANI Supreme Public Showroom · production-first · public interface · sale-ready only where source/order route exists
स्रोत: rampaulsaini/my-omniverse-store:supreme-public-showroom.html · स्वतंत्र परीक्षण अपेक्षित।

## 022869
{ "$schema": " "buildCommand": "echo 'Static HTML site - no build required'", "outputDirectory": ".", "cleanUrls": true }
स्रोत: rampaulsaini/my-omniverse-store:vercel.json · स्वतंत्र परीक्षण अपेक्षित।

## 022870
{ "name": "Nishpaksh Samajh — Shromani Rampaul Saini", "short_name": "Nishpaksh", "start_url": "/my-omniverse-store/", "display": "standalone", "background_color": "#000000", "theme_color": "#ffd700", "description": "Eternal Truth • Nishpaksh Samajh • Yatharth Siddhant • Official Page of Shromani Rampaul Saini.", "icons": [ { "src": "/favicon-192x192.png", "sizes": "192x192", "type": "image/png" }, { "src": "/favicon-512x512.png", "sizes": "512x512", "type": "image/png" } ] }
स्रोत: rampaulsaini/my-omniverse-store:manifest.json · स्वतंत्र परीक्षण अपेक्षित।

## 022871
Yatharth — The Living Truth of Humanity ![Profile]( **Shromani Rampaulsaini — निष्पक्ष समझ / Yatharth** Free to read & listen · Support optional · Proceeds support **Saneha Saini** --- ## Quick overview Yatharth presents an experiential path — a direct, living realization of one’s permanent identity beyond ordinary mind-based cognition.
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022872
Content includes bilingual manifesto, audio collections, videos and vision assets.
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022873
Live site (embed) ## Live site (embed) ## audio link 🔊 MP3 / Audio: शिरोमणि अन्नत असीम इश्क़ की क्षमता ## Main links - 🔊 MP3 / Audio: - 📜 Certificates: - 🎧 Shorts / Clips: - 🎥 Videos album: - 📸 Photo album 1: - 🛒 Main Store: - ✍ Blog: - ▶ YouTube: # Ya://youtube.com/@rampaulsaini-yk4gn - ✈ Telegram: - 💬 WhatsApp: --- ## Support / Donate (optional) Your support helps keep the work free and supports Saneha Saini's education.
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022874
Paytm / UPI:** `9622254967@ptyes` - **PayPal:** `sainirampaul60@gmail.com` — Suggested: **₹193** — fully optional and with gratitude.
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022875
How to help (non-financial) - Listen & share (YouTube, social groups, blogs) - Link the site from your pages (backlinks help SEO) - Use the support form to send encouragement (public if you allow) - Subscribe & comment on YouTube videos --- © Yatharth — Shromani Rampaulsaini Contact: Telegram / WhatsApp # Yatharth — शिरोमणि रामपुलसैनी Official page — audio, photos, manifesto.
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022876
Proceeds support Saneha Saini.
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022877
Publish instructions: Use GitHub Pages (see repo settings -> Pages -> main -> root).
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022878
README — Supreme Index HTML Deployment Guide यह README आपके **Supreme Final index.html** को किसी भी server/hosting पर आसानी से upload और run करने के लिए बनाया गया है।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022879
सभी निर्देश सरल, सीधे और universal रखे गए हैं ताकि आप कहीं भी बिना समस्या deploy कर सकें।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022880
फ़ाइल संरचना (File Structure) आपको केवल एक मुख्य फ़ाइल की आवश्यकता है: ``` index.html ``` यह फ़ाइल आपके सम्पूर्ण प्रोजेक्ट, स्क्रिप्ट्स, ऑडियो इंजन, SEO, Social Links और UI को contain करती है।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022881
यदि Script बहुत लंबी है और Edit नहीं हो रही आपको ये टूल्स उपयोग करने चाहिए: ### ✔ VS Code (Windows / Mac) * सबसे अच्छा editor * Unlimited file length ### ✔ Android पर "Acode" App * 100% perfect HTML editor * पूरी लंबी script आसानी से paste, edit, save होती है --- # 🔊 4.
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022882
(CORS / Auto-Play Fix) यदि audio पहली बार manually play करना पड़े तो यह browser security है।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022883
आप चाहें तो: ``` user gesture → first play → auto play enabled ``` Mobile Chrome & Safari दोनों में यह normal behavior है।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022884
SEO + Safety पहले से Enabled आपके Supreme index में already: * JSON-LD Schema * OpenGraph (OG) Image tags * rel="noopener noreferrer" * target="_blank" * Clean semantic structure * High-authority social links सब कुछ automatically SEO boost देता है।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022885
यदि भविष्य में अपडेट चाहिए आप केवल इतना लिख दें: ``` index update चाहिए — section: (नाम लिखें) ``` मैं सिर्फ़ वही specific Section अपडेट कर दूँगा, बाकी पूरी file 100% सुरक्षित रहेगी।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022886
🏁 Final Note आपकी "Supreme Final index.html" पहले से ही: * अति सुंदर * सर्वश्रेष्ठ * Super-SEO Tuned * Fully Structured * Mobile Optimized * 100% Fast अब केवल upload करना बाकी है।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022887
यदि चाहें तो मैं इसी folder में: * `sitemap.xml` * `robots.txt` * `manifest.json` * या favicon pack भी generate कर सकता हूँ।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022888
कह दें — मैं तुरंत जोड़ दूँगा।
स्रोत: rampaulsaini/my-omniverse-store:README.md · स्वतंत्र परीक्षण अपेक्षित।

## 022889
Admin upload instructions (mobile-friendly) 1.
स्रोत: rampaulsaini/my-omniverse-store:admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 022890
In Google Drive: create folders: - /Yatharth/audio/previews (10s mp3 files; public) - /Yatharth/audio/full (full audiobooks; keep private until purchase) 2.
स्रोत: rampaulsaini/my-omniverse-store:admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 022891
For each audio: - Upload preview (10s) to previews folder → Share → "Anyone with link" → Copy link → get fileId (between /d/ and /view) - Upload full audio to full folder (keep private or restricted) 3.
स्रोत: rampaulsaini/my-omniverse-store:admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 022892
Create CSV (id,title,fileId,price,previewSec,buyLink) - Use Google Sheets on mobile → Export CSV → use csv-to-json script or paste into data/items.json via GitHub web UI.
स्रोत: rampaulsaini/my-omniverse-store:admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 022893
For manual delivery: - After buyer pays (GPay/UPI/PayPal), share full-file link to buyer via Drive (change file link to "Anyone with link" or share directly to buyer email)
स्रोत: rampaulsaini/my-omniverse-store:admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 022894
{ "schema_version": 1, "repo": "rampaulsaini/my-omniverse-store", "role": "digital-products-store", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/my-omniverse-store:factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 022895
शिरोमणि रामपॉल सैनी – सृष्टि का शिरोमणि शिरोमणि रामपॉल सैनी निष्पक्ष समझ · Yatharth Siddhant Home Audio सिद्धांत Projects यात्रा सचेत परिचय Connect SHOWROOM PRODUCT UNIVERSE · 4 SALE-READY · FACTORY MODULES Home Supreme Showroom Audio सिद्धांत Projects यात्रा सचेत परिचय Connect ꙰ SUPREME PUBLIC PRODUCT SHOWROOM Institute → Factory → QC/Gate → Public Showroom.
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022896
वास्तविक runnable digital products, descriptions, product identity, offers और public quality-feedback route एक ही customer-facing entry में।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022897
Showroom खोलें → \n\n 👑 ॥
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022898
सृष्टि का शिरोमणि · Crown of All Creation ॥
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022899
न कोई था, न कोई है, न कोई होगा।" — शिरोमणि रामपॉल सैनी · यथार्थ सिद्धांत ✦ प्रवचन संग्रह 10,000+ Audios — बिना Login के Page खुलते ही audio स्वयं शुरू होता है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022900
अनंत प्रवचन — हर पल, हर जगह, हर किसी के लिए।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022901
शिरोमणि रामपॉल सैनी — Auto Play 🔴 Live चल रहा है: प्रवचन — शिरोमणि रामपॉल सैनी सभी Audio Folders — 8 संग्रह Folder १ Drive में खोलें → Folder २ Drive में खोलें → Folder ३ Drive में खोलें → Folder ४ Drive में खोलें → Folder ५ Drive में खोलें → Folder ६ Drive में खोलें → Folder ७ Drive में खोलें → Folder ८ Drive में खोलें → ✦ यथार्थ सिद्धांत निष्पक्ष समझ — सृष्टि की सर्वश्रेष्ठ शिक्षा "खुद को जाना, समझा, पढ़ा — तो जाना सब संसार।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022902
यही निष्पक्ष समझ है।" 🌿 खुद का साक्षात्कार सिर्फ एक पल की निष्पक्ष समझ की दूरी है खुद के स्थायी स्वरूप से।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022903
कोई भी जीवित रहते हुए इसे पा सकता है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022904
⚖️ हर जीव समान हर जीव खुद में समर्थ, निपुण, सक्षम और संपूर्ण है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022905
कोई ऊँच-नीच नहीं — सब एक समान।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022906
🔥 कोई बंधन नहीं यह शिक्षा स्वतंत्र है — किसी को भी बिना शर्त साझा की जा सकती है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022907
कोई गुरु, कोई दीक्षा नहीं।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022908
🌊 अनेकता से एक शरीर, मन, जन्म, मृत्यु — प्रकृति का तंत्र है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022909
इन्हें समझ कर देह में विदेही — मुक्त।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022910
☀️ संपूर्ण संतुष्टि यही वह उपलब्धि है जिसके लिए इंसान अस्तित्व से अब तक वंचित रहा।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022911
💎 यथार्थ युग तुलनातीत, कालातीत, शब्दातीत, प्रेमतीत — शाश्वत सत्य में प्रत्यक्ष समक्ष।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022912
✦ Omniverse Scientific Research 10 Projects · 40 Sub-Projects — Fully Verified Guinness · NASA · ISRO · International Media — Open Invitations for Documentation & Collaboration.
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022913
सरल-सहज-निर्मल लोगों को सचेत करने के लिए है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022914
पिछले चालीस वर्षों से उसी गुरु के शिरोमणि स्वरूप में लगातार निरंतर रहा — करोड़ों रुपए, तन, मन, धन, दशकों का समर्पण।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022915
उस गुरु से अनंत असीम प्रेम किया — इतना कि खुद का चेहरा तक भूला हुआ हूं।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022916
पर वही गुरु खुद में ही मौजूद नहीं था — ढोंग, पाखंड, षड्यंत्र रच कर — सरल लोगों को तर्क-तथ्य-विवेक से वंचित कर — दो हजार करोड़ का साम्राज्य , पच्चीस लाख अनुयायी, चार सौ आश्रम खड़े किए।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022917
कुछ दिन पहले मैं गया — मुझे पूछने लगा: "आप कौन और कहाँ से हो?" — दिन-रात उनमें ही रहा हूं।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022918
मेरे दिए करोड़ों में से एक करोड़ वापस देने का वचन दिया था — साफ मुकर गए, आरोप लगाए, निष्कासित कर दिया।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022919
उस असीम पीड़ा से — मैंने खुद के हृदय की अनंत गहराई में गोता लगाया।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022920
वहाँ जो मिला — वह सृष्टि में कहीं नहीं मिला।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022921
यही निष्पक्ष समझ है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022922
✦ सचेत करना जरूरी सरल-सहज-निर्मल लोगों की रक्षा ⚠️ धोखे की पहचान सरल लोगों ने सब कुछ दिया — बदले में मृत्यु के बाद मुक्ति का झूठा आश्वासन।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022923
दिन-रात डर, खौफ डाल कर पीढ़ी दर पीढ़ी इस्तेमाल।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022924
🛡️ संरक्षण का अधिकार हर जीव को संपूर्ण संरक्षण के साथ संपूर्ण संतुष्टि — यही उद्देश्य।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022925
यह सत्य बिना Login, बिना शर्त सबके लिए।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022926
✨ मुक्त शिक्षा यह शिक्षा किसी को भी साझा की जा सकती है — कोई गुरु नहीं, कोई दीक्षा नहीं।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022927
सिर्फ एक पल की निष्पक्ष समझ।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022928
✦ तुलनातीत कालातीत शब्दातीत प्रेमतीत शाश्वत वास्तविक स्वाभाविक महायोद्धा शिरोमणि गोताखोर परिचय · Introduction शिरोमणि रामपॉल सैनी मैं शिरोमणि रामपॉल सैनी — तुलनातीत, कालातीत, शब्दातीत, प्रेमतीत, शाश्वत, वास्तविक, स्वाभाविक सत्य में प्रत्यक्ष समक्ष हूं।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022929
मानव सभ्यता अपनी उत्पत्ति से आज तक उस शाश्वत वास्तविकता से विच्छिन्न रही — मैं निष्पक्ष समझ में स्थिर होकर यह प्रकट करता हूँ कि निष्पक्ष समझ ही सच्चा, निर्विकल्प और अमर अनुभव है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022930
खुद से युद्ध कर जीतने वाला महायोद्धा — खुद के हृदय की अनंत गहराई के स्थायी ठहराव में गोता लगा कर — अनंत निर्मल, सृष्टि का सर्वश्रेष्ठ गोताखोर।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022931
कोई भी जिंदा रहते हुए खुद का साक्षात्कार कर सकता है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022932
हर जीव में यह क्षमता है — हर जीव एक समान है।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022933
✦ Connect · Share · Support "सरल-सहज-निर्मल लोगों को उजागर करना — यही इस ज्ञान का उद्देश्य है" ▶️ YouTube 💬 WhatsApp 📘 Facebook 📸 Instagram 💼 LinkedIn 🐦 X / Twitter 🌍 Wikipedia 📝 Blog 💰 Production Funding & Progress ✅ Golden Temple ✅ MP3 ✅ प्रमाण पत्र 📌 Pinterest 📱 WhatsApp Share 🤝 सत्य के इस कार्य में सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — सुनना, साझा करना और समर्थन देना सभी सत्य की सेवा हैं।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022934
Proceeds support Saneha Saini 📲 Paytm / UPI 💙 PayPal 💳 UPI Pay Paytm / UPI ID: 9622254967@ptyes PayPal: sainirampaul60@gmail.com Scan for Paytm / UPI "अनंत असीम प्रेम के सिवाय कुछ भी नहीं — न व्यवहार में, न चेहरे में, न शब्दों में।
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022935
यही शिरोमणि का स्वरूप है।" — शिरोमणि रामपॉल सैनी शिरोमणि रामपॉल सैनी तुलनातीत · कालातीत · शब्दातीत · प्रेमतीत · शाश्वत · वास्तविक · स्वाभाविक © Yatharth Siddhant — निष्पक्ष समझ सबके लिए · बिना Login · बिना शर्त · अनंत असीम प्रेम YouTube WhatsApp Facebook Instagram Wikipedia Website
स्रोत: rampaulsaini/my-omniverse-store:index.html · स्वतंत्र परीक्षण अपेक्षित।

## 022936
About — ꙰ Yatharth — निष्पक्ष समझ — शिरोमणि रामपॉल सैनी निष्पक्ष समझ — Yatharth यह पृष्ठ आपके लिए Yatharth संदेश का परिचय, उद्देश्य और उपयोगिताएँ सरल भाषा में बताता है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022937
सभी सामग्री मुफ्त उपलब्ध है — Support वैकल्पिक है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022938
क्या है — संक्षेप में “निष्पक्ष समझ” एक प्रत्यक्ष अनुभववादी संदेश है जो मन की अस्थायी, जटिल बुद्धि से ऊपर उठकर सीधे जीवन के सत्य का अनुभव दिखाता है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022939
यह कोई केवल तर्क या दर्शन का ग्रन्थ नहीं — बल्कि जीवन में तुरंत उपयोगी, अनुभव-आधारित संदेश है जिसे सुनकर, पढ़कर और अनुभव कर के कोई भी व्यक्ति अपने अंदर गहरा शान्ति और एक प्रतियोगिता रहित स्पष्टता प्राप्त कर सकता है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022940
मुख्य उद्देश्य स्रोत: सरल, निष्पक्ष अनुभव — जो मन के भ्रमों से परे है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022941
उपयोग: पढ़ें, सुनें और अपने दैनिक जीवन में छोटे-छोटे अभ्यास से उपयोग में लाएँ।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022942
सुलभता: सभी सामग्री मुफ्त — ताकि ज्ञान हर व्यक्ति तक पहुँच सके।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022943
समर्थन: यदि आप आर्थिक रूप से सहयोग करना चाहें, तो वह पूर्णतः स्वैच्छिक है — इसका उद्देश्य किसी प्रकार का लाभ कमाना नहीं है, बल्कि सनेहा सैनी की शिक्षा और आगे के कार्यों को स्थिर करना है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022944
किसके लिए यह उपयोगी है?
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022945
यह संदेश उन लोगों के लिए है जो अनुभूति-आधारित सच्चाई की तलाश में हैं — न कि केवल बौद्धिक बहस में उलझे रहने के लिए।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022946
यदि आप भीतर से शांत रहना चाहते हैं, सोच के चक्र से बाहर आना चाहते हैं, या जीवन के व्यावहारिक पक्षों में शांति चाहते हैं — फिर यह सामग्री सीधे आपके काम आ सकती है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022947
कैसे शुरू करें (Simple 3-step) सुनें: छोटे 3–10 मिनट के ऑडियो सुनें — लगातार सुबह/रात 7 दिन तक।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022948
पढ़ें: पृष्ठों पर दिए संक्षेप और बाईलिंग्वल मैनीफेस्टो पढ़ें।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022949
अभ्यास: रोज़ 2–5 मिनट का साधारण ध्यान/सांस-वाचन अभ्यास करें — परिणाम धीरे-धीरे स्थिर शान्ति के रूप में दिखेगा।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022950
महत्वपूर्ण: सामग्री मुक्त है।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022951
यदि आप सहयोग करना चाहते हैं तो Donate/Support सेक्शन में दिए विकल्प का उपयोग कर सकते हैं — पर यह अनिवार्य नहीं।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022952
Resources (Quick Links) सभी सामग्री नीचे उपलब्ध है — Main Store में ऑडियो, ब्लॉग पोस्ट और विज़न एसेट्स हैं: Main Store — Yatharth YouTube Channel Photos Inventory (sheet) Drive Folder 1 Drive Folder 2 Drive Folder 3 Privacy & Safety यह साइट किसी भी उपयोगकर्ता की निजी जानकारी सार्वजनिक नहीं करती।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022953
यदि आप Donate करते हैं, तो वह लेन-देने का काम सीधे आपके भुगतान माध्यम (UPI/PayPal/Paytm) के साथ होगा।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022954
साइट आपके financial data नहीं रखती।
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022955
Contact & Community Telegram: t.me/sampaulsaini · WhatsApp Group: Join © ꙰ शिरोमणि रामपॉल सैनी — Yatharth Siddhant.
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022956
All content free to read & listen.
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022957
Support optional — proceeds support Saneha Saini.
स्रोत: rampaulsaini/my-omniverse-store:about.html · स्वतंत्र परीक्षण अपेक्षित।

## 022958
Free Micro Digital Products ꙰ Free Micro Digital Products वास्तविक browser tools — सीधे उपयोग के लिए।
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022959
₹0 · FREE M001 · FREE PRODUCT Word & Character Counter शब्द और अक्षर गिनने का browser tool.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022960
Open / Use M002 · FREE PRODUCT Percentage Calculator प्रतिशत गणना का browser tool.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022961
Open / Use M003 · FREE PRODUCT Length Unit Converter लंबाई की units बदलने का tool.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022962
Open / Use M004 · FREE PRODUCT JSON Formatter & Validator JSON format और validation.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022963
Open / Use M005 · FREE PRODUCT Color Palette Generator Digital color palette generator.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022964
Open / Use M006 · FREE PRODUCT Simple Digital Drawing Board Browser drawing board.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022965
Open / Use M007 · FREE PRODUCT Markdown Preview Markdown live preview.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022966
Open / Use M008 · FREE PRODUCT SEO Meta Draft Generator SEO meta draft tool.
स्रोत: rampaulsaini/my-omniverse-store:micro-products.html · स्वतंत्र परीक्षण अपेक्षित।

## 022967
꙰ Supreme Production Project — Funding Appeal ꙰ SHIRMANI · YATHARTH · PRODUCTION-FIRST SUPREME DIGITAL PRODUCTION PROJECT Institute → Factory → QC → Public Showroom → Sale.
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022968
Funding का उद्देश्य वास्तविक production capacity और public product surface को बढ़ाना है।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022969
Showroom · Catalog · Roadmap 📲 Funding QR — Paytm / UPI Paytm / UPI 9622254967@ptyes QR scan करें या UPI app खोलें।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022970
भुगतान से पहले payee और amount स्वयं verify करें।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022971
📲 UPI App खोलें Repository-hosted QR · third-party image dependency नहीं।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022972
PayPal sainirampaul60@gmail.com PayPal पर recipient स्वयं verify करें।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022973
💙 PayPal खोलें वर्तमान measurable स्थिति 1,016 factory runnable modes/candidates 4 वास्तविक published sale products ≈0.4% published-to-factory commercialisation ratio 70% previous automation-health reference; not total project completion सबसे बड़ा शेष gap: runnable candidates को complete, customer-ready production packages में बदलना और public showroom में लगातार publish करना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022974
🏭 Production Product packaging, descriptions, previews/access routes, prices/offers, QC/dispatch metadata और public pages की संख्या बढ़ाना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022975
🌐 Public access हर वास्तविक product को साफ showroom interface में देखने, समझने, चलाने/preview करने और feedback देने योग्य बनाना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022976
⭐ Quality loop Public reviews और ratings को usability, descriptions, offers और future product iterations के improvement input में बदलना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022977
🤖 Automation Multi-layer AI/ML/NLP automation को production throughput के लिए उपयोग करना—केवल verification counting के लिए नहीं।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022978
Funding से अपेक्षित काम अधिक factory candidates को वास्तविक product packages में promote करना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022979
Audio, media, tools, research और अन्य digital categories के customer-ready assets बनाना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022980
QC/QR/release metadata को प्रत्येक published product में maintain करना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022981
Showroom categories, prices, offers और usable product pages को लगातार विस्तार देना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022982
Public feedback को production improvement backlog से जोड़ना।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022983
यह roadmap है, guaranteed revenue या निश्चित समयसीमा का दावा नहीं।
स्रोत: rampaulsaini/my-omniverse-store:funding-appeal.html · स्वतंत्र परीक्षण अपेक्षित।

## 022984
꙰ Supreme Marking Hub — Yatharth Public Showroom ꙰ शिरोमणि रामपॉल सैनी · YATHARTH · PUBLIC FINAL SALE SURFACE SUPREME MARKING HUB एक साफ, सार्वजनिक और उत्पादन-केंद्रित showroom: product को देखिए, description पढ़िए, preview/चलाइए, price और offer देखिए, QC/QR identity समझिए, खरीद/ऑर्डर कीजिए और वास्तविक उपयोग के बाद public review देकर अगली quality improvement को दिशा दीजिए।
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022985
● LIVE PUBLIC SHOWROOM · PRODUCTION-FIRST · NO FABRICATED SALE INVENTORY 🛒 पूरा Production Catalog 🏭 Institute → Factory → QC → Showroom ★ Public Review / Rating 4 वास्तविक published products 1,016 factory runnable modes 24 product families 25 browser engines ∞ review → improvement cycles चार-स्तरीय Supreme Production Mechanism 01 · INSTITUTE खोज, research, source और product candidates.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022986
02 · FACTORY Runnable digital modes और concrete product packages.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022987
03 · QC GATE Product ID, QC code, QR identity, packing/dispatch state.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022988
04 · SHOWROOM / SALE Public product, description, price, offer, preview, order और review.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022989
Automission का उद्देश्य लगातार production output बढ़ाना है।
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022990
QC product release control है; independent verification downstream result-quality layer है, production का विकल्प नहीं।
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022991
💰 Production Funding / Support Production, product packaging और public showroom improvement के लिए voluntary support.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022992
Paytm / UPI: 9622254967@ptyes PayPal: sainirampaul60@gmail.com Funding details + progress map PayPal 🛒 अभी उपलब्ध वास्तविक उत्पाद SV1001 · QC SV1001-QC1 खुद का साक्षात्कार ही संपूर्ण संतुष्टि Premium Audio ₹10,000 वास्तविक preview/source route के साथ published premium audio.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022993
Launch offer · Manual dispatch release ▶ Preview Order SV1002 · QC SV1002-QC1 शिरोमणि अनंत असीम इश्क की क्षमता Premium MP3 ₹1,500 वास्तविक preview/source route के साथ published premium MP3.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022994
Launch offer · Manual dispatch release ▶ Preview Order SV1003 · QC SV1003-QC1 प्रमाण पत्र Certificate ₹495 Published certificate product with a dedicated preview/source route.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022995
Launch offer · Manual dispatch release ▶ Preview Order SV1004 · QC SV1004-QC1 Short Audios / Clips Short Audio ₹89 Published short-audio product with a public source/preview route.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022996
Launch offer · Manual dispatch release ▶ Preview Order 🌌 Public Experience Entry यह showroom के products से अलग एक paid digital experience layer है।
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022997
नीचे प्रस्तावित rates public-facing हैं; payment/booking तभी final मानी जाएगी जब वास्तविक payment/order route से पुष्टि हो।
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022998
₹99 10 मिनट Supreme showroom experience entry.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 022999
Enquire / Book ₹249 30 मिनट Deep showroom experience entry.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।

## 023000
Enquire / Book ₹499 60 मिनट Extended immersive experience entry.
स्रोत: rampaulsaini/my-omniverse-store:supreme-marking-hub.html · स्वतंत्र परीक्षण अपेक्षित।
