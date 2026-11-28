# डिजिटल महाग्रंथ 008

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 007001
Configure only the needed environment inputs, mounts, and ports from the selected app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007002
Preserve logs and container state before cleanup; remove only resources created for this check.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007003
The inspected `./repo.sh launch --container --name : ` is a convenience launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007004
It can fall back to another image when lookup fails, always requires NVIDIA hardware, and can discard the child process's failure status.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007005
Do not accept its completion as the success signal or use it for CPU-only validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007006
Prefer controlled Docker execution when proving the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007007
For an NVCF app with an HTTP readiness service on container port 8011, a minimal local GPU readiness check can use the following shape.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007008
First select a free host port, a unique name, the actual image ID, and any app-required runtime inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007009
Adjust ports/settings for the selected version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007010
These are examples, not default values to overwrite the developer's configuration with.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007011
```bash KIT_IMAGE_ID=$(docker image inspect --format '{{.Id}}' acme/viewer:0.1.0) KIT_CHECK_NAME=kit-container-check-unique docker run --detach --name "$KIT_CHECK_NAME" --gpus all -p 127.0.0.1:18011:8011 "$KIT_IMAGE_ID" docker inspect --format '{{.Image}} {{json .State}}' "$KIT_CHECK_NAME" docker logs "$KIT_CHECK_NAME" curl --fail --silent --show-error --max-time 10 ``` Ensure image lookup and container creation succeed before proceeding.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007012
Add the selected app's required GPU driver capabilities, mounts, and environment inputs as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007013
For CPU services, omit GPU options and use that service's configured check.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007014
A batch app needs its actual exit status and expected output rather than an HTTP probe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007015
A single probe immediately after launch is not a startup deadline.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007016
Poll within a chosen total limit, checking for early container exit and collecting logs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007017
A successful `docker run --detach` only confirms container creation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007018
Verify the container's `.Image`, actual state/exit status, and applicable readiness or completion result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007019
For a long-running app, require it to remain running while checking readiness; a stopped container with exit code 0 is not a healthy running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007020
Cold RTX startup can take several minutes for shader and driver pipeline preparation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007021
An initial HTTP 503 or an "app ready" log line alone does not decide the readiness result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007022
Allow for that preparation in the bounded check, observe progress, and record a timeout if the chosen deadline expires.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007023
After collecting evidence, stop and remove the specific test container if it is no longer needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007024
Record intentional test shutdown separately from an application crash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007025
A rebuild creates a new candidate and requires new image-specific runtime evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007026
NVCF readiness and downstream boundary When runtime validation is selected and the app exposes `omni.services.livestream.session`, check its configured readiness endpoint.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007027
The documented default is HTTP `/v1/streaming/ready` on port 8011, with a successful response indicating the service's readiness criteria.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007028
`/v1/streaming/startup` is not equivalent evidence of application/RTX readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007029
See the [session service documentation]( Keep these outcomes separate: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007030
Source app runs in its development environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007031
The packaged image runs and satisfies its app/container checks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007032
An NVCF deployment becomes ready with workers using the intended image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007033
The frontend connects and receives advancing decoded application frames.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007034
This skill handles the first two when requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007035
The latter two need the downstream deployment/client validation workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007036
Readiness-only local port mapping does not provide a complete external media/signaling path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007037
For the NVCF handoff, inspect actual settings and carry the required runtime input names and signaling/health configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007038
Documented defaults include function type `STREAMING`, signaling route `/sign_in` on 49100, and readiness on 8011.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007039
Derive values from the selected app/version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007040
Do not attach NVCF requirements to Kit App Streaming or non-streaming results.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007041
See [Deploying Kit Apps]( ## Optional publication Publish only when the request includes image distribution to a resolved registry destination.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007042
A registry-qualified image name alone does not request a push.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007043
Confirm missing registry/namespace details and use the available authenticated mechanism without exposing secret values or baking credentials into the image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007044
If publication needs an additional tag, preserve the developer's original local tag, identify the destination tag, and ensure it refers to the built image before pushing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007045
Do not silently choose a different repository or version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007046
Verify the successful push and capture the published URI and manifest digest when available.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007047
Report publication failures independently of local build success.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007048
A local image is not pullable by remote NVCF workers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007049
The deployment stage needs the published/distributed image identity and pull access for its cluster.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007050
This skill can supply the image when publication is requested; otherwise report that distribution remains to be arranged.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007051
Result format Return the following fields in a concise human-readable report.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007052
A caller may request a machine-readable contract; follow that actual contract rather than inventing a new required schema.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007053
| Field | Include | |---|---| | Requested outcome | Existing/new app, streaming target or headless behavior, containerization-only or selected runtime checks, requested publication.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007054
| | Source | Git URL/ref/commit and relevant local changes, or NGC resource/version/artifact identity; available provenance for a local project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007055
| | Versions | Kit, app, template and relevant build/package tools; resolved streaming extension versions or generated version-lock evidence; skill source/version separately.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007056
| | Application | Base app, selected layer/entrypoint, important configuration changes, required runtime input names and mounts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007057
| | Image | Exact requested reference, local ID, OS/architecture, and published URI/digest if publication occurred.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007058
| | Evidence | Build outcome/log location, image inspection, separate source-app and container runtime outcomes, exact identity tested, applicable readiness/exit evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007059
| | Remaining work | Checks not run and reasons, unresolved failures, and distribution/deployment/client validation still needed for downstream use.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007060
| Use `passed`, `failed`, `not run by request`, `not run because unavailable`, or `not applicable` for each stage as appropriate.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007061
Include stages only where they clarify the requested outcome.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007062
Preserve attempted failures rather than describing them as untested.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007063
Build plus image inspection is sufficient for a containerization-only request.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007064
If runtime validation was requested but unavailable, state that the image is built while that requested validation remains incomplete.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007065
Do not claim NVCF deployment or end-to-end streaming success from local container readiness.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/validation-and-handoff.md · स्वतंत्र परीक्षण अपेक्षित।

## 007066
Select and prepare the application Use the section matching the developer's starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007067
Source selection and app preparation happen in the application project, which can differ from the checkout containing this skill.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007068
License acceptance during preflight Identify required license acceptance while resolving the selected source and tool version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007069
Inspect that version's license notices or prompt implementation before starting generation or long-running builds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007070
Brief source/tool inspection may be needed to identify the terms; do not defer a known acceptance requirement until an unattended operation stops at a prompt.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007071
When acceptance is required and not already supplied, collect it together with the initial app/version/image/validation decisions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007072
Make the question explicit in the conversation, even when also using a structured question UI: - Explain which planned operation requires acceptance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007073
Name and link every agreement identified by the selected workflow, and state the project or runs the acceptance will cover.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007074
Quote the tool's prompt when it has been observed; do not invent a live prompt or claim work has stopped when this is preflight.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007075
Ask for an explicit yes or no, with an example reply.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007076
Explain that a yes authorizes answering the matching tool prompt on the developer's behalf.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007077
For example, when the selected workflow names the NVIDIA agreements below: > Before I generate this application and start the build, do you accept the [NVIDIA Software License Agreement]( and [Omniverse Product-Specific Terms]( and authorize me to answer Yes to the license prompt for this application?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007078
Reply "Yes, I accept" or "No." Use the selected version's agreements and URLs if they differ, and state the actual scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007079
One explicit acceptance can cover multiple planned runs using the same terms when those runs are named.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007080
Honor acceptance already supplied for that scope and use it when the matching tool prompt appears.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007081
Do not infer acceptance from silence or a general request to build, or bypass the tool's required response.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007082
If a later prompt presents different terms or scope, surface that difference before accepting.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007083
While awaiting an answer, continue only work that does not require acceptance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007084
Existing project Locate the intended project and inspect its instructions, working changes, build entrypoint, app definitions, and dependency configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007085
Common Kit App Template locations include: - `source/apps/` for base apps and layers, `source/extensions/` for project extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007086
`repo.toml` for build/packaging configuration, `repo_tools.toml` and `tools/deps/` for tool and SDK pins.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007087
`templates/templates.toml` and resolved template metadata for available template/layer operations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007088
Custom projects can use other layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007089
Follow their build registration and dependency precaching rather than introducing template metadata solely to fit this workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007090
Resolve the requested `.kit` file and its dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007091
Record the actual base app and selected layer.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007092
Inspect inherited settings and launcher behavior as well as the selected file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007093
A name ending in `_nvcf.kit` or `_streaming.kit` is a clue, not proof of the configured functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007094
Check whether the app has the dependencies, settings, build registration, and assets it needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007095
Prepare missing packaging or streaming configuration within the requested scope.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007096
If the app requires substantial implementation or migration before it can build, report that boundary and the specific blocker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007097
New project from GitHub Recommend [NVIDIA-Omniverse/kit-app-template]( `main`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007098
If the request does not choose a Kit version/ref, ask whether the developer wants that default or a specific version/ref.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007099
Inspect the public refs and selected source pins, then display the resolved Kit version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007100
Use a new directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007101
For the accepted default: ```bash git clone --branch main --single-branch my-kit-project cd my-kit-project git rev-parse HEAD ``` Choose the directory from the developer's workspace context.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007102
For another branch or tag, resolve that exact ref; for a commit, fetch and check out the resolved commit explicitly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007103
Do not apply `--branch` to a commit hash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007104
If a requested version is unavailable publicly, explain the available choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007105
Never substitute an internal checkout or edit only the Kit kernel pin to simulate a complete version change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007106
Inspect the selected checkout's dependency pins and CLI.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007107
The ordinary template flow is: ```bash ./repo.sh template new ``` Select the available app template based on the requested behavior, then resolve its app namespace/name, display name, app version, and any required extension inputs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007108
Do not silently reuse documentation example identities.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007109
Keep app version independent of the Kit version and container tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007110
Answer any required template license prompt using the acceptance established during preflight.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007111
If it presents different terms or scope, follow [license preflight](#license-acceptance-during-preflight) before proceeding.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007112
Use supported interactive input or the chosen tool's documented playback mechanism.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007113
In the inspected tooling, `template new --generate-playback ` records choices without creating the app; `template replay ` subsequently renders it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007114
Inspect help before using these options on another version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007115
A generated playback file alone is not an application.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007116
Legacy `--input` or `REPO_TEMPLATE_SCRIPT` mechanisms do not reliably handle checkbox layer selection; use the supported playback flow or interact with the actual prompts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007117
Streaming layers | Target | Preparation | |---|---| | Kit App Streaming | Reuse or add the selected version's ordinary streaming layer for local or self-managed streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007118
In the inspected Kit App Template this is the picker entry `[omni_default_streaming]: Omniverse Kit App Streaming (Default)`, which renders `{app_name}_streaming.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007119
| | NVCF | Reuse or add that version's NVCF layer, including its streaming/session-service dependencies and settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007120
Ordinary streaming alone is insufficient.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007121
In the inspected Kit App Template this is the picker entry `[nvcf_streaming]: NVCF Streaming`, which renders `{app_name}_nvcf.kit`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007122
| | Non-streaming | Keep the intended headless app entrypoint; do not add streaming dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007123
Determine whether the app still requires GPU rendering.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007124
| For template-generated apps, select the layer during creation or use the available modify flow: ```bash ./repo.sh template modify ``` Inspect the app's template metadata before modifying it, commonly `source/rendered_template_metadata.json`, and the template's linked-layer definitions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007125
The inspected modify flow is interactive and can overwrite an already rendered layer when selected again.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007126
Reuse a correct existing layer; inspect custom edits before regenerating.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007127
Do not invent noninteractive `--app` or `--layer` flags.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007128
For a manually authored app without the required metadata, use the selected version's layer definitions as a reference and make only the necessary dependency/settings changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007129
Rebuild after adding or changing layers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007130
Select the actual generated layer as the packaging entrypoint, such as `acme.viewer_streaming.kit` for Kit App Streaming or `acme.viewer_nvcf.kit` for NVCF.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007131
Do not package the base desktop app merely because it has the same display name.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007132
Secondary route: NGC SDK Use this route when the developer chooses it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007133
If the developer is unsure, explain the two source routes and recommend public Kit App Template by default.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007134
Resolve the desired resource and version using the [Kit SDK catalog links in the manual]( Select the resource matching the requested release and platform; the collection linked by a latest guide may cover a different feature or production line.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007135
Follow that resource's download and extraction instructions using available authentication.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007136
Do not assume an NGC SDK resource is a runnable container image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007137
Record the resource organization/team/name, requested version, downloaded artifact identity/checksum, and detected SDK version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007138
Do not invent a Git commit for a downloaded SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007139
On Linux, when provided by that package, run `./new_project.sh` from the extracted SDK and resolve its project-location and license prompts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007140
Inspect the package's instructions if this entrypoint differs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007141
Enter the generated project, inspect its actual tool/SDK pins, and use the same app/layer workflow above.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007142
Keep the skill loaded from its complete folder if it is absent from that SDK release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007143
Record the selection Capture the source URL/ref/commit and relevant local changes for Git projects, or the NGC artifact provenance for downloaded SDKs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007144
For a local non-Git project, record the available provenance.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007145
Record the skill's source/version separately, along with the resolved app, Kit, template, and build/package tool versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007146
Generated projects can resolve streaming extensions from a registry to versions newer than copies bundled in the SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007147
Record the versions resolved by the application or preserve its generated version locks with the build evidence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007148
Keep the selected SDK and Kit pins unless the developer requests a change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007149
Examples follow the [Kit app creation and containerization guide]( When the selected checkout differs from the latest guide, its actual configuration and supported CLI determine the commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/app-preparation.md · स्वतंत्र परीक्षण अपेक्षित।

## 007150
Build and package the selected app Run from the resolved application project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007151
These command examples match the inspected `repo_kit_tools` 1.21.4 workflow; inspect the selected checkout's pins and help before using them with other tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007152
Establish the build environment The initial workflow uses Linux x86_64 artifacts, compatible Linux x86_64 execution, and Docker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007153
Check the actual build host and Docker daemon: ```bash uname -s uname -m docker version docker info ./repo.sh build --help ./repo.sh package_container --help ``` Check the project's documented compiler/dependency prerequisites, Docker daemon accessibility, artifact/package download access, and space for the build, staged copy, and image layers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007154
The selected base image and Dockerfile determine additional requirements.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007155
The inspected default Dockerfile needs a BuildKit frontend supporting `COPY --exclude` and its `# syntax=docker/dockerfile:1` directive.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007156
Native Windows packaging is rejected by this tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007157
A suitable WSL installation or a remote Linux builder can supply the required environment, but native Kit also runs during host-side extension trimming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007158
A Windows shell connected only to a remote Docker daemon does not move that step to Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007159
ARM, multiarch, and cross-build setups require a compatible Kit distribution, base image, and separately verified workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007160
GPU availability is a runtime decision, not a prerequisite for this inspected default packaging path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007161
Dependency precaching resolves extensions; it is not shader warmup.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007162
Inspect custom build hooks, trimming changes, and Dockerfiles before applying this conclusion to a customized project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007163
Check compatible GPUs/drivers and NVIDIA Container Toolkit only when GPU runtime checks are selected.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007164
Resolve app and image inputs Resolve a real source app/layer and its staged basename.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007165
Confirm that the intended `.kit` file and Kit executable exist after building.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007166
Check a separate launcher only when the selected project's workflow requires one.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007167
Stop to resolve missing paths, multiple matching apps, or duplicate basenames in nested app directories.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007168
Inspect `repo.toml` and existing `[repo_kit_package_container]` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007169
The tool can reduce an existing app path to its basename, and configuration lookup can distinguish `acme.viewer_nvcf` from `acme.viewer_nvcf.kit` before normalizing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007170
Reuse the matching configured entry with consistent naming rather than generating duplicate entries or passing a nonexistent path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007171
Require a valid, writable image repository plus explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007172
Examples: | Reference | Meaning | |---|---| | `acme/viewer:0.1.0` | Repository and explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007173
| | `registry.example.com:5000/acme/viewer:0.1.0` | Registry port and a separate explicit tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007174
| | `registry.example.com:5000/acme/viewer` | Missing tag; the registry-port colon is not a version tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007175
| | `acme/viewer@sha256:...` | Existing-image digest identity, not a writable Docker build tag.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007176
| The inspected tool treats any colon in `--image-tag` as a complete-reference signal.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007177
Passing an untagged name can therefore change its interpretation or cause Docker to default to `latest`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007178
Resolve the name/tag first.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007179
Preserve the requested value instead of silently adding `latest`, changing the namespace, or replacing it with a generated app name.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007180
Before building, inspect whether the chosen local tag already exists and record its ID.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007181
Rebuilding that tag updates its local target; make that effect clear.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007182
A remote registry overwrite is a separate publication action.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007183
See [Docker image reference syntax]( ## Build and optional source-app check For the supported template workflow: ```bash ./repo.sh build --config release ``` Use the custom project's supported equivalent when needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007184
In the inspected build tool, `-c` means clean and exit, not configuration; use the long `--config` option.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007185
Verify command success, dependency resolution, and the selected app artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007186
Inspect the configured build root rather than assuming one path for every project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007187
If requested and supported by the host, run the source app and collect actual exit/readiness/log evidence before packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007188
The convenience `./repo.sh launch` command can guide app selection, but its return alone is not proof of runtime success.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007189
A non-rendering CPU service can need direct invocation through its own launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007190
If runtime checks were declined, continue with packaging and record that choice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007191
Container configuration and packaging Reuse existing valid Dockerfile and entrypoint configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007192
For supported projects without configuration, `package_container` can generate a container template/configuration when supplied a valid app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007193
Inspect the files it creates.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007194
Explicit generation is also available in the inspected version: ```bash ./repo.sh package_container --app acme.viewer_nvcf.kit --generate ``` This generates configuration in the default project `tools/containers` location; it is not a completed image build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007195
If specifying a destination in this tool version, use an absolute path inside the project because configuration injection computes a path relative to the absolute project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007196
Inspect the selected version's help before using it, and do not regenerate customized files without examining them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007197
Generation does not overwrite existing files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007198
In the inspected tool, both `--generate` and the `auto_generate` configuration path skip any destination file that already exists, log a warning, and continue, so an existing `tools/containers/Dockerfile` keeps its current `FROM` line after the tool's bundled default changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007199
Compare that `FROM` line with the Dockerfile bundled in the pinned `repo_kit_tools` package (`omni/repo/kit_tools/package/data/Dockerfile`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007200
The inspected 1.21.4 default is `nvcr.io/nvidia/omniverse/ov-base-ubuntu22-x86_64:1.0.0`; the default before 1.21.4 was `nvcr.io/nvidia/omniverse/ov-base-ubuntu-22:2026.2.3`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007201
When they differ, update deliberately: delete `tools/containers/Dockerfile` (and `entrypoint.sh` if it should also be refreshed) and rerun `--generate`, or edit the `FROM` line in place and keep the customized content.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007202
Regeneration leaves an existing `repo.toml` container entry for that app unchanged.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007203
Record the base image actually used in the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007204
Substitute the resolved app name and full image reference in the build command: ```bash ./repo.sh package_container --app acme.viewer_nvcf.kit --image-tag acme/viewer:0.1.0 --config release ``` The tool stages build artifacts, optionally precaches dependencies, trims unused extensions, and invokes Docker.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007205
Do not substitute historical `package --container`, `--target-app`, or container `--name` arguments without evidence that the selected version requires them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007206
There is no shader-cache bypass or dry-run flag in this inspected container tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007207
Use `--from-package` only when deliberately using a compatible packaged artifact.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007208
It is a boolean switch, not an archive-path argument; inspect both its configured archive pattern and post-unpack commands for compatibility with the selected public or private source.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007209
Inspect custom runtime-loaded dependencies and assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007210
The inspected tool supports repeatable `--extra-ext` and `extra_extensions` configuration to keep needed extensions/apps through precache and trimming.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007211
Use it only for identified dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007212
If local assets, credentials, caches, or cloud inputs are expected at runtime, identify their mounts or input names instead of silently treating the developer machine's state as part of the image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007213
The default entrypoint runs Kit directly with `--no-window`, rather than invoking a custom app shell launcher.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007214
Account for required environment/setup/arguments.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007215
Desktop display integration or substantial custom launcher behavior requires its own adaptation and validation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007216
Verify the produced image After a successful packaging command, inspect the exact requested reference: ```bash docker image inspect acme/viewer:0.1.0 docker image inspect --format '{{.Id}}' acme/viewer:0.1.0 ``` Record its full local ID, repository tags, OS/architecture, configured entrypoint/command, and relevant app metadata.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007217
The default Dockerfile labels images with `kit_app_template`; match that label and the rendered entrypoint/configuration to the selected app.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007218
A label alone is insufficient if a custom Dockerfile changes behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007219
Bind the result to the current successful build and its logs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007220
An unchanged image ID can be legitimate when Docker reuses identical content.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007221
Neither an existing tag after a failed build nor a different ID without successful build evidence proves completion.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007222
Keep full metadata/logs private when they contain environment values, and include only necessary non-secret evidence in the result.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007223
Continue with [validation and handoff](validation-and-handoff.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007224
Diagnose common failures | Observation | Next check | |---|---| | Command or option is unavailable | Inspect the selected tool pin, help, and project configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007225
Do not upgrade the project just to match these examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007226
| | App missing or multiple matches | Resolve the real source/staged app and consistent config name before retrying.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007227
| | Dependencies cannot resolve | Check selected-version extension pins, registry access, and build/precaching configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007228
Avoid a global cache purge.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007229
| | An app works outside the container but lacks an extension inside it | Inspect trimming and runtime-loaded dependencies; preserve identified extras through supported configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007230
| | Dockerfile parse failure around `COPY --exclude` | Inspect BuildKit/frontend compatibility and the syntax directive, especially in custom Dockerfiles.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007231
| | Native executable or architecture failure | Verify Linux x86_64 artifacts, host execution environment, and base image.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007232
Remote Docker alone does not solve native host execution.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007233
| | Stale staging is demonstrated | Use the selected tool's scoped staging-clean option only after checking its target.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007234
Avoid deleting unrelated builds or Docker caches.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007235
| | Docker image exists after an error | Preserve the failed result and distinguish the old tag/image from the attempted build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007236
| Use [container tool documentation]( alongside the selected tool's implementation and configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-app-containerize/references/container-workflow.md · स्वतंत्र परीक्षण अपेक्षित।

## 007237
tomlkit==0.12.2 ; python_version >= "3.10" and python_version < "4.0" \ --hash=sha256:df32fab589a81f0d7dc525a4267b6d7a64ee99619cbd1eeb0fae32c1dd426977 \ --hash=sha256:eeea7ac7563faeab0a1ed8fe12c2e5a51c61f933f2502f7e9db0241a65163ad0
स्रोत: NVIDIA-Omniverse/kit-app-template:tools/repoman/requirements.txt · स्वतंत्र परीक्षण अपेक्षित।

## 007238
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007239
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007240
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007241
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007242
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007243
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007244
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007245
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007246
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007247
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007248
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007249
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007250
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007251
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007252
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007253
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007254
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007255
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007256
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007257
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007258
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007259
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007260
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007261
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007262
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007263
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007264
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007265
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007266
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007267
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007268
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007269
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007270
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007271
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007272
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007273
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007274
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007275
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007276
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007277
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007278
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007279
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007280
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007281
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007282
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007283
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007284
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007285
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007286
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007287
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007288
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007289
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007290
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007291
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007292
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007293
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007294
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007295
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007296
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007297
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007298
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007299
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007300
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007301
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007302
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007303
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007304
:warning: **Important**: These layers are not standalone application templates.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007305
They must be used in conjunction with a base application template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007306
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007307
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007308
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007309
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007310
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007311
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007312
Collaborating on large-scale design projects in real-time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007313
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007314
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007315
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007316
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007317
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007318
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007319
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007320
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007321
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007322
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007323
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007324
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007325
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007326
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007327
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007328
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007329
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007330
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007331
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007332
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007333
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007334
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007335
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007336
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007337
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007338
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007339
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007340
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007341
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007342
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007343
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007344
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007345
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007346
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007347
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007348
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007349
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007350
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007351
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007352
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007353
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007354
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007355
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007356
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007357
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007358
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007359
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007360
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007361
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007362
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007363
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007364
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007365
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007366
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007367
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007368
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007369
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007370
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007371
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007372
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007373
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007374
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007375
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007376
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007377
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007378
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007379
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007380
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007381
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007382
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007383
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007384
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007385
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007386
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007387
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007388
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007389
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007390
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007391
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007392
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007393
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007394
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007395
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007396
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007397
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007398
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007399
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007400
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007401
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007402
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007403
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007404
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007405
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007406
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007407
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007408
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007409
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007410
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007411
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007412
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007413
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007414
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007415
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007416
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007417
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007418
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007419
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007420
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007421
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007422
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007423
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007424
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007425
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007426
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007427
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007428
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007429
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007430
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007431
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007432
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007433
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007434
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007435
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007436
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007437
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007438
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007439
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007440
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007441
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007442
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007443
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007444
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007445
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007446
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007447
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007448
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007449
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007450
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007451
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007452
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007453
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007454
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007455
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007456
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007457
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007458
If multiple container images exist, you will be
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007459
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007460
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007461
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007462
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007463
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007464
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007465
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007466
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007467
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007468
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007469
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007470
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007471
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007472
Subsequent extensions can be added to the .kit file manually.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007473
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007474
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007475
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007476
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007477
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007478
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007479
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007480
Setup Extension -> kit_service_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007481
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007482
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007483
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007484
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007485
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007486
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007487
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007488
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007489
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007490
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007491
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007492
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007493
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007494
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007495
When adapting an existing extension for a headless service, keep the service execution path limited to the dependencies it requires.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007496
Prefer separating reusable headless logic from UI, viewport, rendering, and other application-specific functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007497
If separation is impractical, dependencies that the service can operate without may be declared optional, provided their imports and initialization are also guarded.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007498
See [Adapting Existing Extensions for Headless Services]( for guidance and examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007499
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007500
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007501
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007502
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007503
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007504
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007505
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007506
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007507
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007508
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007509
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007510
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007511
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007512
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007513
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007514
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007515
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007516
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007517
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007518
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007519
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007520
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007521
The base application `.kit` file should be used for containerization.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007522
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007523
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007524
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007525
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007526
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007527
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007528
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007529
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007530
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007531
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007532
During Application configuration, you will be prompted for information about these extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007533
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007534
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007535
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007536
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007537
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007538
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007539
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007540
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007541
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007542
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007543
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007544
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007545
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007546
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007547
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007548
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007549
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007550
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007551
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007552
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007553
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007554
The USD Viewer template includes sample assets for this purpose.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007555
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007556
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007557
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007558
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007559
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007560
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007561
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007562
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007563
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007564
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007565
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007566
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007567
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007568
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007569
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007570
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007571
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007572
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007573
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007574
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007575
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007576
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007577
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007578
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007579
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007580
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007581
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007582
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007583
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007584
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007585
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007586
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007587
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007588
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007589
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007590
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007591
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007592
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007593
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007594
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007595
USD Explorer Setup Extension Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer Setup Extension Template is specifically designed to configure the USD Explorer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007596
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Explorer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007597
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Explorer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007598
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007599
Key Features - Custom configurations tailored to the USD Explorer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007600
Usage This extension is automatically created and configured when you generate a new application based on the [USD Explorer Template Application](../../apps/usd_explorer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007601
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007602
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007603
Basic C++ Extension Template ## Overview The Basic C++ Extension Template is a starting point for developers looking to build C++ based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007604
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007605
Note for Windows C++ Developers** : This template requires that Visual Studio is installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007606
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007607
For additional C++ configuration information [see here](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007608
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007609
Performance sensitive extensions that require the performance benefits of C++.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007610
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007611
Integrating with existing C++ libraries or codebases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007612
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007613
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007614
Usage This section provides instructions for the setup and use of the Basic C++ Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007615
Getting Started To get started with the Basic C++ Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007616
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007617
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007618
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007619
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007620
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007621
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007622
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007623
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007624
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007625
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007626
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007627
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007628
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007629
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007630
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007631
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007632
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007633
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007634
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007635
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007636
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007637
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007638
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007639
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007640
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007641
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007642
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007643
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007644
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007645
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007646
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007647
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007648
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007649
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007650
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007651
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007652
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007653
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007654
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007655
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007656
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007657
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007658
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007659
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007660
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007661
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007662
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007663
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007664
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007665
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007666
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007667
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007668
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007669
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007670
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007671
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007672
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007673
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007674
Integrating other C++ or Python libraries as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007675
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007676
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007677
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007678
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007679
Python UI Extension Template ## Overview The Python UI Extension Template offers a simple starting point for developers looking to build Python-based extensions with performant User Interfaces.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007680
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007681
Use Cases This template is ideal for developers looking to build: - UI based extensions that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007682
Key Features - A simple starter UI demonstrating how to build using the Omni UI framework.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007683
Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007684
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007685
Usage This section provides instructions for the setup and use of the Python UI Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007686
Getting Started To get started with the Python UI Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007687
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007688
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007689
Select desired template with arrow keys ↑↓:**: Python UI Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007690
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007691
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007692
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007693
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007694
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007695
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007696
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007697
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007698
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Omni UI Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007699
Service Setup Extension Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Service Setup Extension Template is designed to facilitate the configuration and setup of a headless service that leverages the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007700
Though it is possible in this case, setup extensions are not typically intended to be used as a generic extension but as a specific component of a particular application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007701
Use Cases This setup extension is well suited for: - Developers building headless services that require Kit SDK functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007702
Key Features - Sample ServiceAPIRouter setup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007703
Sample endpoint to demonstrate interaction patterns within service Kit SDK and OpenUSD.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007704
Usage This extension is automatically created and configured when you generate a new service application using the [Service Application Template](../../apps/kit_service/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007705
Additional Learning - [Omniverse Kit Service Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007706
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007707
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007708
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007709
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007710
Managing the state for selecting objects within the scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007711
Performing actions without traditional in-app UI and menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007712
Key Features - Remote communication with the Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007713
Scene loading capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007714
State management for object selection within the USD Viewer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007715
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007716
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007717
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007718
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007719
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007720
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007721
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007722
All required setup code for use with the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007723
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007724
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007725
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007726
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007727
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007728
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007729
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007730
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007731
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007732
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007733
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007734
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007735
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007736
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007737
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007738
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007739
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007740
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007741
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007742
Changelog The format is based on [Keep a Changelog]( ## [0.1.2] - 2026-05-11 ### Fixed - `makePrimsPickable` handler raised `UnboundLocalError` when the WebSocket payload was empty or missing the `paths` key, and the broad `except` then leaked the raw Python exception message (including internal variable names) to the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007743
The handler now initializes `paths` to an empty list before the conditional so an empty payload is a clean no-op, and unexpected exceptions are logged server-side via `carb.log_error` while only a generic error string is returned to the client (OMPE-90584, NVBug 6100326).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007744
Added - Regression test `test_make_prims_pickable_empty_payload` covering empty payload, missing-`paths` key, and explicit-empty-list cases.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007745
[0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007746
{{ extension_display_name }} [{{ extension_name }}] This is an example of a simple Kit Service extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007747
It is intended to be copied and to serve as a template to create new ones.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007748
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - 2024-03-13 - Initial version based on kit service extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/service.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007749
{{ extension_display_name }} [{{ extension_name }}] A simple python UI extension example.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007750
Use it as a starting point for your extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007751
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/python_ui/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007752
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007753
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007754
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007755
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007756
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007757
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007758
Args: object: The bound object to register.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007759
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007760
Args: object: The bound object to deregister.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007761
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007762
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007763
Return: The bound object if it exists, an empty object otherwise.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007764
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007765
Return: The id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007766
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007767
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007768
Return: The bound object that was created.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007769
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007770
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007771
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007772
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007773
Args: value_to_multiply: The value to multiply by.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007774
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007775
Return: The toggled bool value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007776
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007777
Args: value_to_append: The value to append.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007778
Return: The new string value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007779
)", py::arg("value_to_append")) /**/; } ```
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 007780
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007781
Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007782
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007783
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007784
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007785
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007786
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007787
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007788
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007789
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007790
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007791
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007792
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 007793
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007794
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007795
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007796
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 007797
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 007798
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007799
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007800
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007801
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007802
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007803
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007804
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007805
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007806
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007807
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007808
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007809
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007810
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007811
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007812
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 007813
Testing Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is an extension — including the `.kit` files that define applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007814
The `test` tool (`repo_test`) reflects this: it validates that your applications start up and shut down cleanly, and it runs the automated tests defined within your extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007815
Each extension template provided by the `kit-app-template` repository ships with sample tests that you can expand to grow your coverage.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007816
This document covers running tests, understanding what is tested, and adding your own tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007817
Prerequisites: Build Before You Test The test tool runs against the contents of the `_build` directory, so a successful build must precede any test run.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007818
If you have changed source since your last build, rebuild first.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007819
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` > **Note:** Tests run against a specific build configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007820
By default the tooling builds and tests the `release` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007821
If you build `debug`, pass the matching `--config debug` flag when testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007822
Running Tests ### Run the Default Test Suite Running `test` with no arguments executes the repository's default test suite (`alltests`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007823
The tool discovers every test-enabled extension in the build, launches each within the Kit test harness, and reports the aggregated results.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007824
Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` For each test-enabled extension — and each application `.kit` file — the tool starts a dedicated Kit process, loads the extension along with its test dependencies, runs the tests, and verifies a clean shutdown.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007825
Listing Tests Without Running Them Use `--list` (`-l`) to enumerate the tests that would run without executing them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007826
This is useful for confirming that a newly added extension or test is being discovered.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007827
Linux:** ```bash ./repo.sh test --list ``` **Windows:** ```powershell .\repo.bat test --list ``` ### Running a Subset of Tests Use `--filter-files` (`-f`) to narrow a run to specific test files, modules, classes, or individual tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007828
This shortens the feedback loop while iterating on a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007829
Linux:** ```bash ./repo.sh test -f my_company.my_extension ``` **Windows:** ```powershell .\repo.bat test -f my_company.my_extension ``` > **Note:** The accepted `--filter-files` format depends on the underlying test executor.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007830
For the Python (`omni.kit.test` / `unittest`) tests used by the extension templates, you may specify modules, classes, or individual tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007831
Run `./repo.sh test -h` for the full description.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007832
Selecting a Build Configuration By default the test tool targets the `release` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007833
To test a `debug` build, pass `--config` (`-c`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007834
The configuration must match the one you built.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007835
Linux:** ```bash ./repo.sh test --config debug ``` **Windows:** ```powershell .\repo.bat test --config debug ``` ### Other Useful Options | Option | Purpose | |--------|---------| | `-s, --suite` | Select which test suite(s) to run (default: `alltests`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007836
| | `-f, --filter-files` | Run only tests matching a file/module/class/test pattern.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007837
| | `-l, --list` | List the discovered tests and exit without running them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007838
| | `-c, --config` | Test the `release` (default) or `debug` build configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007839
| | `-p, --from-package` | Test an application package instead of the local build (see *Testing a Packaged Application* below).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007840
| | `-e, --extra-arg` | Pass an additional argument through to the test process.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007841
| | `--coverage` | Produce a Python code-coverage report after the run (for supported suite types).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007842
| | `--generate-report` | Run the configured report-generation command, if one is set, after all tests complete.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007843
| For the complete, authoritative list of options, run: **Linux:** ```bash ./repo.sh test -h ``` **Windows:** ```powershell .\repo.bat test -h ``` --- ## What Gets Tested ### Application Startup and Shutdown Every application `.kit` file is validated to confirm it can start up and shut down without error.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007844
This catches broken dependencies and misconfiguration early — a large portion of application health is covered simply by verifying that the fully assembled set of extensions loads cleanly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007845
An application declares how it should be launched during testing through a `[[test]]` table in its `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007846
For example, the Kit Base Editor template includes: ```toml [[test]] args = [ "--/app/file/ignoreUnsavedOnExit=true" ] ``` The `args` are passed to the Kit process when the application is tested.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007847
Extensions opt into testing with a `[[test]]` table in their `extension.toml`, which may declare test-only dependencies and extra arguments: ```toml [[test]] dependencies = [ "omni.kit.ui_test", # UI testing helper, loaded only during tests ] args = [ ] ``` Dependencies listed here are loaded only for the test run — a convenient place to pull in helpers such as `omni.kit.ui_test` without adding them to your extension's runtime dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007848
Writing Tests Tests use `omni.kit.test`, Python's standard `unittest` module wrapped to support `async`/`await`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007849
Placing a test class derived from `omni.kit.test.AsyncTestCase` at the root of a module within your extension's `tests/` package makes it auto-discoverable — no registration step is required.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007850
Every extension template includes a `tests/` package with a sample test to build on.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007851
To add coverage, place additional `test_*.py` modules in the extension's `tests/` package and grow the assertions from there.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007852
Because tests are standard `unittest` cases, refer to the [Python `unittest` documentation]( for available assertion methods and patterns.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007853
Test Suites and Configuration The behavior of the test tool for this repository is configured under `[repo_test]` in the top-level `repo.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007854
The most relevant settings are the default suite and any per-suite exclusions: ```toml [repo_test] default_suite = "alltests" [repo_test.suites."alltests"] exclude = [ # Setup extension tests are exercised as part of application testing "tests-omni.usd_explorer.setup${shell_ext}", ] ``` - **`default_suite`** determines which suite runs when you invoke `test` without `--suite`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007855
.exclude`** removes specific test executables from a suite — useful when a set of tests is already covered elsewhere.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007856
Adjust these settings as your project grows to control exactly what the default `./repo.sh test` run covers.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007857
Testing a Packaged Application In addition to testing the local build, the tool can run the suite against a packaged application archive — useful for validating a package before distribution.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007858
Use `--from-package` (`-p`), which by default looks for an archive in `_build/packages`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007859
Linux:** ```bash ./repo.sh test --from-package ``` **Windows:** ```powershell .\repo.bat test --from-package ``` The archive pattern is configurable in `repo.toml`: ```toml [repo_test] # When running from a package, find the archive using this pattern: archive_pattern = "${root}/_build/packages/*.zip" ``` > **Note:** Package testing is intended for the "fat" package type, which already contains the Kit Kernel and all extensions, so no additional download is required to run the tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007860
See [Packaging An Application]( for how to create a package.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007861
Testing in Continuous Integration `repo test` is the same entry point used by automated pipelines, so tests you run locally behave consistently in CI.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007862
Keeping the sample tests passing — and expanding them as you add functionality — helps ensure your applications and extensions remain buildable, launchable, and correct as the project evolves.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007863
Additional Resources - [Packaging An Application]( - [Kit SDK Tooling Guide](kit_app_template_tooling_guide.md) - [Kit SDK Companion Tutorial]( - [Python `unittest` documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 007864
Usage and Troubleshooting This section provides high-level information and guidance related to using the Kit App Template repository, along with troubleshooting tips for common issues.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007865
Usage Information ### A Project per Repository The `build` and `package` tooling provided in this repository is designed to capture all code and assets contained within the `/source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007866
Each time the `template new` command is executed, a new application or extension is created within `/source`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007867
For purposes of experimentation and initial development, housing all working assets within the `/source` directory is reasonable.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007868
However, as the project matures or requires deployment, it is recommended to segregate projects (typically a single `.kit` file and any required custom extensions) to minimize build times and reduce the size of the resultant package.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007869
Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is considered an extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007870
The `.kit` files that define applications are simply a convenient method to assemble and configure a set of extensions for specific functionalities, while extensions (and combinations thereof) can act as modular components fulfilling particular tasks.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007871
For additional information on the Kit SDK and how to create applications and extensions, refer to the [Kit SDK Companion Tutorial]( ### Extendable Templates and Tools The templates and tools provided in this repository are designed to be extendable.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007872
Templates Templates consist of a directory structure and boilerplate code containing variables configurable at the time the templates are applied.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007873
The `templates.toml` file, located in `templates/templates.toml`, specifies which templates the tooling recognizes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007874
Tooling Most tooling is not stored directly within the repository; it is instead downloaded from a remote registry upon the initial use of the tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007875
This design allows the tooling to be updated independently of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007876
The framework used for the tooling also supports the definition of custom tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007877
To see this extensibility in action, explore the local tooling defined within `tools/repoman`, specifically the `launch` tool.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007878
Configuration for this tool within the repo is delineated in the `repo_tools.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007879
Troubleshooting This section outlines potential issues that may arise when using the Kit App Template repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007880
Setup & Configuration Issues #### Windows Long Path Due to path length limitations on Windows it is recommended to place repository artifacts in a location closer to the root of the drive.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007881
This will help avoid issues with the path lengths when building and packaging applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007882
exFAT Drive Compatibility Limitations The Kit App Template repository and associated tooling are designed to work with drive formats that support junctions/symlinks.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007883
If you are using an exFAT-formatted drive, you may encounter errors during the build process.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007884
To resolve this issue, consider using a different drive format such as NTFS.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007885
Extension Naming Guidelines When creating custom extensions, avoid using a top-level namespace that is the same as any built-in Python module (e.g., “random”, “sys”, “xml”).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007886
Doing so can cause import conflicts if Omniverse Kit attempts to load extensions from these Python modules.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007887
For example, instead of “random.extension.name”, use a unique namespace such as “my_company.my_app.my_extension”.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007888
Rendering & Performance #### Initial Rendering Startup Times When launching an application that requires the RTX renderer, the first launch may take considerably longer than subsequent launches due to shader compilation.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007889
The initial launch can take between 5 to 8 minutes.** Subsequent launches of RTX-enabled applications will be faster as the renderer caches the compiled shaders.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007890
Build & Packaging #### Build Issues The `template new` tooling ensures that any created application is properly configured to build.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007891
However, extensive manual changes can occasionally cause the configuration and `/source` directory contents to become unsynchronized.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007892
The specifics of any given build are determined by three main factors: 1) The state of the top-level `repo.toml` file, especially the `.kit` files listed in the `apps` array within the `[[repo_precache_exts]]` section.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007893
2) The state of the `premake5.lua` file, particularly which `.kit` files are set to build via `define_app()` (e.g., `define_app("my_company.my_service.kit")`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007894
3) The state of the `source` directory, specifically which `.kit` files are present within `source/apps`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007895
To ensure a build proceeds as intended, verify that the same `.kit` files are listed or defined in all three locations.** For a clean build, use the command `./repo.sh build -c` or `.\repo.bat build -c` to clean the build directory before building.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007896
Caching and Persistent Data The Omniverse Kit SDK caches data and required dependencies to improve build and runtime performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007897
If you encounter issues with stale, incorrect, or missing dependencies/data, consider clearing application specific and/or global cache locations: - **Application Specific Caches**: Clearing application specific caches and settings can be done by adding arguments at launch time.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007898
Linux: ```bash ./repo.sh launch -- --clear-cache --clear-data --reset-user ``` Windows: ```powershell .\repo.bat launch -- --clear-cache --clear-data --reset-user ``` Upon selecting a `.kit` file to launch, the application will clear the cache and data directories before starting.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007899
Global Cache Locations (:warning:Use with Caution:warning:)**: **IMPORTANT NOTE -** Clearing any of the following cache locations will require a full rebuild of any existing applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007900
Deleting the directories responsible for caching ensures a fresh build of the relevant caches during the next build.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007901
Extension AND Application Data Cache Locations**: `$HOME/.local/share/ov` on Linux, `%LOCALAPPDATA%\ov` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007902
Tooling AND Dependency Cache Location**: - **Packman :** `$PM_PACKAGES_ROOT` on Linux, `%PM_PACKAGES_ROOT%` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007903
If `PM_PACKAGES_ROOT` is not set on your system, the default location will revert to `$HOME/.cache/packman` on Linux, `{drive where packman is launched from}\packman-repo` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007904
uv :** `$HOME/.cache/uv` on Linux, `%LOCALAPPDATA%\uv\cache` on Windows.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007905
Space Constraints Due to Docker Artifacts When performing extensive local testing of container images created via `repo package_container`, Docker artifacts can accumulate over time, consuming significant disk space.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007906
`docker system df` can be used to determine disk space utilized by Docker objects.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007907
To reclaim space, consider the following options: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007908
Regular Safe Cleanup**: - **Command**: `docker container prune` - **Description**: This command removes all stopped containers, which is typically safe and helps manage disk space without affecting images, networks, or volumes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007909
Use**: Recommended for regular maintenance.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007910
Extensive Cleanup (:warning:Use with Caution:warning:)**: - **Command**: `docker system prune` - **Description**: This command removes all unused containers, networks, images, and optionally volumes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007911
It is akin to running a `rm -rf` for Docker resources.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007912
Warning**: Use this command carefully, as it will remove many resources indiscriminately.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007913
Ensure you review and understand what will be deleted.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007914
For image-specific cleanup, use `docker images` to list all images and `docker rmi ` to manually remove those that are no longer needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 007915
Windows C++ Developer Configuration ## Introduction This document guides you through setting up this repository for C++ development on Windows using Microsoft Visual Studio and the Windows SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007916
For New Users:** If you are new to Windows C++ development, this guide provides a step-by-step installation of Visual Studio 2022 Community and the Windows SDK, ensuring you have all the components required for standard development tasks.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007917
For Advanced Configurations:** If you already have Visual Studio and the Windows SDK installed but wish to specify exact versions, this guide will help you configure your environment using the `[repo_build.msbuild]` configuration within `repo.toml` at the project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007918
Configuration To enable the Windows C++ build process: - Set the `"platform:windows-x86_64".enabled` flag to `true` in your `repo.toml` file: ```toml [repo_build.build] "platform:windows-x86_64".enabled = true ``` - Set the `link_host_toolchain` flag to `true` in your `repo.toml` file: ```toml [repo_build.msbuild] link_host_toolchain = true ``` **Note:** If you already have Visual Studio and the Windows SDK installed, this might be the only change needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007919
The tooling will auto-detect installed components.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007920
Microsoft Visual Studio and Windows SDK Setup ### Basic Installation #### Installing Visual Studio 2022 Community 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007921
Download Visual Studio Installer** ![VS Download](../vs_download.png) - Visit the [Visual Studio Downloads]( - Click "Free download" under "Community".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007922
Run the Installer** - Open the downloaded installer.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007923
Select "Community" edition and click "Install".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007924
Select Workloads** ![VS Workloads](../vs_workloads.png) - Check "Desktop development with C++".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007925
This includes tools like the MSVC compiler and C++ libraries.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007926
Additional Components** ![VS Additional](../vs_additional.png) - If you need specific components, go to "Individual components".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007927
Select additional tools as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007928
Complete the Installation** - Proceed with the installation to download and set up all files.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007929
Installing Windows SDK (as needed) Usually, the Windows SDK is included with the "Desktop development with C++" workload.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007930
To verify or install it separately: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007931
Launch Visual Studio Installer** - Open the installer if it's not already running.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007932
Modify Installation** ![VS Modify](../vs_modify.png) - Click "Modify" on your Visual Studio installation.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007933
Verify Windows SDK** ![VS WinSDK Verify](../vs_winsdk_verify.png) - Ensure "Windows SDK" is selected under "Optional" sections or "Individual components".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007934
Apply Changes** - Click "Modify" to install or update the SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007935
Configuring an Existing Installation #### Default Installation Paths If Visual Studio and the Windows SDK are installed in default locations, the build tooling will auto-detect them without additional configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007936
Note:** If the path entered is incorrect or invalid, the build system will fall back to auto-detection.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007937
Multiple Installations For multiple Visual Studio or Windows SDK installations, the latest version is used by default.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007938
If unspecified, default edition preference is "Enterprise", "Professional", "Community".
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007939
Additional Resources - [Repo Build Documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 007940
Kit SDK Tooling Guide This document provides an overview of the practical aspects of using the tooling provided in the `kit-app-template`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007941
Intended for users with a basic familiarity with command-line operations, this guide offers typical usage patterns and recommendations for effective tool use.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007942
For a complete list of options for a given tool, use the help command: `./repo.sh [tool] -h` or `.\repo.bat [tool] -h`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007943
Overview of Tools The `kit-app-template` repository includes several tools designed to streamline the development of applications and extensions within the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007944
Available Tools - `template` - `build` - `launch` - `test` - `package` Each tool plays a specific role in the development workflow: ## Template Tool **Command:** `./repo.sh template` or `.\repo.bat template` ### Purpose The template tool facilitates the initiation of new projects by generating scaffolds for applications or extensions based on predefined templates located in `/templates/templates.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007945
Usage The template tool has three main commands: `list`, `new`, `replay`, `modify`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007946
`list` Lists available templates without initiating the configuration wizard.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007947
Linux:** ```bash ./repo.sh template list ``` **Windows:** ```powershell .\repo.bat template list ``` #### `new` Creates new applications or extensions from templates with interactive prompts guiding you through various configuration choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007948
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` #### `replay` In cases where automation is required for CI pipelines or other scripted workflows, it is possible to record and replay the `template new` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007949
Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the Application `.kit` file you want to update.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007950
Next, select (using Space) the Template Layer(s) to add.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007951
After the operation completes, rebuild (`./repo.sh build` or `.\repo.bat build`) the project to pull in the new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007952
What `template new` Modifies When creating applications, the template tool automatically updates build configuration files: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007953
`premake5.lua`** - Adds `define_app("appname.kit")` so the build system discovers your application 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007954
`repo.toml`** - Adds the app path to `repo_precache_exts.apps` so dependent extensions are pre-cached at build time 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007955
`source/rendered_template_metadata.json`** - Records which templates were rendered (enables `template modify` and `template list`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007956
Setup extension** (some templates) - Creates an extension in `source/extensions/` for application-specific initialization **Extensions** are automatically discovered by the Kit build system based on directory structure, so no build file modifications are needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007957
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007958
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007959
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007960
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007961
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007962
It includes all resources located in the `source/` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007963
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007964
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007965
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007966
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007967
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007968
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007969
`-p` or `--package`:** *(Deprecated — will be removed in a future release.)* Launches a packaged application from a specified path.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007970
`repo launch` is intended as a developer tool; launching from a package archive does not serve a development workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007971
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007972
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007973
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007974
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007975
Any flags added after `--` will be passed through to Kit directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007976
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007977
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007978
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007979
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007980
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007981
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007982
Applications configurations (`.kit` files) are tested to ensure they can startup and shutdown without issue.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007983
However, the tests written within the extensions will dictate a majority of application functionality testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007984
Extension templates provided by the Kit App Template repository include sample tests which can be expanded upon to increase test coverage as needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007985
Usage Always run a build before testing: **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ## Package Tool **Command:** `./repo.sh package` or `.\repo.bat package` ### Purpose This tool prepares your application for distribution or deployment by packaging it into a distributable format.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007986
Usage Always run a build before packaging to ensure the application is up-to-date: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` Additional launch options: - **`-n` or `--name`:** Specifies the package (or container image) name.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007987
Linux:** ```bash ./repo.sh package -n ``` **Windows:** ```powershell .\repo.bat package -n ``` - **`--thin`:** Creates a thin package that includes only custom extensions and configurations for required registry extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007988
Linux:** ```bash ./repo.sh package --thin ``` **Windows:** ```powershell .\repo.bat package --thin ``` :warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007989
The version is set within the `tools/VERSION.md` file.** ## Containerization Tool **Command:** `./repo.sh package_container` or `.\repo.bat package_container` ### Purpose The containerization tool provided by `repo_kit_tools` supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007990
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007991
How It Works The tool performs these steps: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007992
Creates a fat package** - Stages all dependencies into a temp directory 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007993
Trims unused extensions** - Removes disabled extensions to minimize image size 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007994
Splits into Docker layers** - Base layer (kit kernel + extscache) and app layer for faster rebuilds 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007995
Builds the container** - Uses a configurable base image (default: `nvcr.io/nvidia/omniverse/ov-base-ubuntu22-x86_64`) The container entrypoint supports runtime configuration via environment variables (`NVDA_KIT_ARGS`, `NVDA_KIT_NUCLEUS`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007996
Usage Always run a build before packaging to ensure the application is up-to-date: - **`package_container`:** Packages the application as a container image (Linux only).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007997
When using the `package_container`, the user will be asked to select a `.kit` file to use within the entry point script for the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007998
This can also be specified without user interaction by passing it appropriate `.kit` file name via the `--app ${path_to_kit_file}` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 007999
Linux:** ```bash ./repo.sh package_container ``` **Windows:** ```powershell .\repo.bat package_container ``` Additional command options: - **`--app`:** Specify the Kit app to containerize.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 008000
One of defined in the config.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।
