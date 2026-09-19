# डिजिटल महाग्रंथ 092

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 091001
concurrency: group: "pages" cancel-in-progress: false jobs: # Single deploy job since we're just deploying deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 - name: Setup Pages uses: actions/configure-pages@v5 - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: # Upload entire repository path: '.' - name: Deploy to GitHub Pages id: deployment uses: actions/deploy-pages@v4
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091002
Placeholder monitor workflow name: Monitor & Auto-Recover on: [schedule, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Monitor workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/monitor.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091003
Placeholder rollback workflow name: Rollback on: [workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Rollback workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/rollback.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091004
Placeholder deploy workflow for Omniverse-AI name: CI Deploy on: [push, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Deploy workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091005
[ {"text": "Welcome to the Supreme Omniverse AI Portal", "lang": "en"}, {"text": "संपूर्ण सृष्टि में निष्पक्ष समझ ही सर्वोच्च है", "lang": "hi"}, {"text": "Bienvenue dans le portail Suprême Omniverse AI", "lang": "fr"}, {"text": "Bienvenido al Portal Supremo Omniverse AI", "lang": "es"} ]
स्रोत: Omniverse-AI/analytics/scripts/guidance -massages.json · स्वतंत्र परीक्षण अपेक्षित।

## 091006
{ // Use IntelliSense to learn about possible attributes.
स्रोत: kit-app-template/.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 091007
// Hover to view descriptions of existing attributes.
स्रोत: kit-app-template/.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 091008
// For more information, visit: "version": "0.2.0", "configurations": [ { "name": "Python: Remote Attach", "type": "debugpy", "request": "attach", "connect": { "host": "localhost", "port": 3000 }, "pathMappings": [ { "localRoot": "${workspaceFolder}", "remoteRoot": "${workspaceFolder}" } ], "justMyCode": true, "subProcess": true, "runtimeArgs" : [ "--preserve-symlinks", "--preserve-symlinks-main" ] } ] }
स्रोत: kit-app-template/.vscode/launch.json · स्वतंत्र परीक्षण अपेक्षित।

## 091009
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091010
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091011
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091012
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091013
name: Question description: Ask a question title: "[QUESTION]: " labels: ["question"] body: - type: markdown attributes: value: | Thanks for taking the time to ask us a question!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091014
type: textarea id: text_of_question attributes: label: Question description: Ask your question.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091015
placeholder: "Question text" validations: required: true - type: textarea id: additional_context attributes: label: Additional Context description: Provide any related code, issues, or projects.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091016
placeholder: "Any related code, issues, or projects."
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091017
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091018
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091019
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091020
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091021
name: Feature Request description: Suggest an idea for this project title: "[FEATURE]: " labels: ["feature request"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this feature request!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091022
type: textarea id: description attributes: label: Description description: | Describe the proposed feature placeholder: | Feature description and problem or pain point being addressed validations: required: true - type: textarea id: use_case attributes: label: Use Case or Scenarios description: Describe how this feature would be used placeholder: e.g., User performing action A, would accomplish B, with benefit C.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091023
type: textarea id: implementation_ideas attributes: label: Possible Implementation Ideas description: If you have any suggestions on how this feature might be implemented, please share them here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091024
placeholder: Implementation ideas - type: textarea id: additional_context attributes: label: Additional Context or Recommendations description: Provide any other context or recommendations here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091025
placeholder: Any other relevant information.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091026
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091027
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091028
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091029
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091030
name: Bug Report description: File a bug report for the repository title: "[BUG]: " labels: ["bug"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this bug report!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091031
type: textarea id: description attributes: label: Description description: | Describe the bug in detail placeholder: | Expected Behavior vs.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091032
Actual Behavior: validations: required: true - type: textarea id: component attributes: label: Component description: Which component (Tool/Template/Extension) is showing the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091033
placeholder: "e.g., Kit Base Editor Template / repo launch tool / Kit SDK" - type: textarea id: system-details attributes: label: System Details description: | Provide details about your system placeholder: | OS / CPU / GPU / GPU Driver Version validations: required: true - type: textarea id: reproduction-steps attributes: label: Reproduction Steps description: What are the steps to reproduce the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091034
validations: required: true - type: textarea id: logs attributes: label: Logs description: | Include the relevant log files: - **repo.log:** Found in `_repo/repo.log` if the issue is with tooling.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091035
kit.log:** Found in `_build/{OS}/release/logs/.../kit_{...}log` if the issue is with App, Extension, or Kit SDK.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091036
placeholder: Paste the log content here or attach the log files.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091037
type: textarea id: additional-context attributes: label: Additional Context description: Provide any other context or information here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091038
placeholder: Any other information that might be helpful
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091039
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091040
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091041
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091042
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091043
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091044
Select the desired UI based application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091045
The developer bundle is not currently suitable for headless services.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091046
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091047
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091048
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091049
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091050
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091051
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091052
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091053
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091054
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091055
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091056
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091057
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091058
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091059
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 091060
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091061
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091062
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091063
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091064
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091065
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091066
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091067
What Are Application Layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091068
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091069
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091070
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091071
``` Answer `yes` to enable streaming for your application.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091072
You can then pick from the following streaming layers: ```bash ?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091073
Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091074
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming [ ] [omni_gdn_streaming]: GDN Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091075
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091076
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091077
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091078
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091079
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091080
GDN Streaming:** Streams applications through NVIDIA Graphics Delivery Network; especially useful for configurator workflows.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091081
Refer to the [End-to-End Configurator Example Guide]( for deployment instructions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091082
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091083
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091084
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091085
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091086
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091087
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091088
GDN Streaming** Refer to the [End-to-End Configurator Example Guide]( for instructions on packaging and deploying to NVIDIA GDN.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091089
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 091090
Usage and Troubleshooting This section provides high-level information and guidance related to using the Kit App Template repository, along with troubleshooting tips for common issues.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091091
Usage Information ### A Project per Repository The `build` and `package` tooling provided in this repository is designed to capture all code and assets contained within the `/source` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091092
Each time the `template new` command is executed, a new application or extension is created within `/source`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091093
For purposes of experimentation and initial development, housing all working assets within the `/source` directory is reasonable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091094
However, as the project matures or requires deployment, it is recommended to segregate projects (typically a single `.kit` file and any required custom extensions) to minimize build times and reduce the size of the resultant package.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091095
Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is considered an extension.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091096
The `.kit` files that define applications are simply a convenient method to assemble and configure a set of extensions for specific functionalities, while extensions (and combinations thereof) can act as modular components fulfilling particular tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091097
For additional information on the Kit SDK and how to create applications and extensions, refer to the [Kit SDK Companion Tutorial]( ### Extendable Templates and Tools The templates and tools provided in this repository are designed to be extendable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091098
Templates Templates consist of a directory structure and boilerplate code containing variables configurable at the time the templates are applied.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091099
The `templates.toml` file, located in `templates/templates.toml`, specifies which templates the tooling recognizes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091100
Tooling Most tooling is not stored directly within the repository; it is instead downloaded from a remote registry upon the initial use of the tooling.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091101
This design allows the tooling to be updated independently of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091102
The framework used for the tooling also supports the definition of custom tools.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091103
To see this extensibility in action, explore the local tooling defined within `tools/repoman`, specifically the `launch` tool.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091104
Configuration for this tool within the repo is delineated in the `repo_tools.toml` file at the root of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091105
Troubleshooting This section outlines potential issues that may arise when using the Kit App Template repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091106
Setup & Configuration Issues #### Windows Long Path Due to path length limitations on Windows it is recommended to place repository artifacts in a location closer to the root of the drive.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091107
This will help avoid issues with the path lengths when building and packaging applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091108
exFAT Drive Compatibility Limitations The Kit App Template repository and associated tooling are designed to work with drive formats that support junctions/symlinks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091109
If you are using an exFAT-formatted drive, you may encounter errors during the build process.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091110
To resolve this issue, consider using a different drive format such as NTFS.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091111
Extension Naming Guidelines When creating custom extensions, avoid using a top-level namespace that is the same as any built-in Python module (e.g., “random”, “sys”, “xml”).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091112
Doing so can cause import conflicts if Omniverse Kit attempts to load extensions from these Python modules.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091113
For example, instead of “random.extension.name”, use a unique namespace such as “my_company.my_app.my_extension”.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091114
Rendering & Performance #### Initial Rendering Startup Times When launching an application that requires the RTX renderer, the first launch may take considerably longer than subsequent launches due to shader compilation.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091115
The initial launch can take between 5 to 8 minutes.** Subsequent launches of RTX-enabled applications will be faster as the renderer caches the compiled shaders.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091116
Build & Packaging #### Build Issues The `template new` tooling ensures that any created application is properly configured to build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091117
However, extensive manual changes can occasionally cause the configuration and `/source` directory contents to become unsynchronized.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091118
The specifics of any given build are determined by three main factors: 1) The state of the top-level `repo.toml` file, especially the `.kit` files listed in the `apps` array within the `[[repo_precache_exts]]` section.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091119
2) The state of the `premake5.lua` file, particularly which `.kit` files are set to build via `define_app()` (e.g., `define_app("my_company.my_service.kit")`).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091120
3) The state of the `source` directory, specifically which `.kit` files are present within `source/apps`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091121
To ensure a build proceeds as intended, verify that the same `.kit` files are listed or defined in all three locations.** For a clean build, use the command `./repo.sh build -c` or `.\repo.bat build -c` to clean the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091122
Caching and Persistent Data The Omniverse Kit SDK caches data and required dependencies to improve build and runtime performance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091123
If you encounter issues with stale, incorrect, or missing dependencies/data, consider clearing application specific and/or global cache locations: - **Application Specific Caches**: Clearing application specific caches and settings can be done by adding arguments at launch time.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091124
Linux: ```bash ./repo.sh launch -- --clear-cache --clear-data --reset-user ``` Windows: ```powershell .\repo.bat launch -- --clear-cache --clear-data --reset-user ``` Upon selecting a `.kit` file to launch, the application will clear the cache and data directories before starting.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091125
Global Cache Locations (:warning:Use with Caution:warning:)**: **IMPORTANT NOTE -** Clearing any of the following cache locations will require a full rebuild of any existing applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091126
Deleting the directories responsible for caching ensures a fresh build of the relevant caches during the next build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091127
Extension AND Application Data Cache Locations**: `$HOME/.local/share/ov` on Linux, `%LOCALAPPDATA%\ov` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091128
Tooling AND Dependency Cache Location**: - **Packman :** `$PM_PACKAGES_ROOT` on Linux, `%PM_PACKAGES_ROOT%` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091129
If `PM_PACKAGES_ROOT` is not set on your system, the default location will revert to `$HOME/.cache/packman` on Linux, `{drive where packman is launched from}\packman-repo` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091130
uv :** `$HOME/.cache/uv` on Linux, `%LOCALAPPDATA%\uv\cache` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091131
Space Constraints Due to Docker Artifacts When performing extensive local testing of container images created via `repo package_container`, Docker artifacts can accumulate over time, consuming significant disk space.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091132
`docker system df` can be used to determine disk space utilized by Docker objects.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091133
To reclaim space, consider the following options: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091134
Regular Safe Cleanup**: - **Command**: `docker container prune` - **Description**: This command removes all stopped containers, which is typically safe and helps manage disk space without affecting images, networks, or volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091135
Use**: Recommended for regular maintenance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091136
Extensive Cleanup (:warning:Use with Caution:warning:)**: - **Command**: `docker system prune` - **Description**: This command removes all unused containers, networks, images, and optionally volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091137
It is akin to running a `rm -rf` for Docker resources.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091138
Warning**: Use this command carefully, as it will remove many resources indiscriminately.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091139
Ensure you review and understand what will be deleted.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091140
For image-specific cleanup, use `docker images` to list all images and `docker rmi ` to manually remove those that are no longer needed.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 091141
Windows C++ Developer Configuration ## Introduction This document guides you through setting up this repository for C++ development on Windows using Microsoft Visual Studio and the Windows SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091142
For New Users:** If you are new to Windows C++ development, this guide provides a step-by-step installation of Visual Studio 2022 Community and the Windows SDK, ensuring you have all the components required for standard development tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091143
For Advanced Configurations:** If you already have Visual Studio and the Windows SDK installed but wish to specify exact versions, this guide will help you configure your environment using the `[repo_build.msbuild]` configuration within `repo.toml` at the project root.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091144
Configuration To enable the Windows C++ build process: - Set the `"platform:windows-x86_64".enabled` flag to `true` in your `repo.toml` file: ```toml [repo_build.build] "platform:windows-x86_64".enabled = true ``` - Set the `link_host_toolchain` flag to `true` in your `repo.toml` file: ```toml [repo_build.msbuild] link_host_toolchain = true ``` **Note:** If you already have Visual Studio and the Windows SDK installed, this might be the only change needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091145
The tooling will auto-detect installed components.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091146
Microsoft Visual Studio and Windows SDK Setup ### Basic Installation #### Installing Visual Studio 2022 Community 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091147
Download Visual Studio Installer** ![VS Download](../vs_download.png) - Visit the [Visual Studio Downloads]( - Click "Free download" under "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091148
Run the Installer** - Open the downloaded installer.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091149
Select "Community" edition and click "Install".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091150
Select Workloads** ![VS Workloads](../vs_workloads.png) - Check "Desktop development with C++".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091151
This includes tools like the MSVC compiler and C++ libraries.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091152
Additional Components** ![VS Additional](../vs_additional.png) - If you need specific components, go to "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091153
Select additional tools as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091154
Complete the Installation** - Proceed with the installation to download and set up all files.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091155
Installing Windows SDK (as needed) Usually, the Windows SDK is included with the "Desktop development with C++" workload.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091156
To verify or install it separately: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091157
Launch Visual Studio Installer** - Open the installer if it's not already running.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091158
Modify Installation** ![VS Modify](../vs_modify.png) - Click "Modify" on your Visual Studio installation.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091159
Verify Windows SDK** ![VS WinSDK Verify](../vs_winsdk_verify.png) - Ensure "Windows SDK" is selected under "Optional" sections or "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091160
Apply Changes** - Click "Modify" to install or update the SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091161
Configuring an Existing Installation #### Default Installation Paths If Visual Studio and the Windows SDK are installed in default locations, the build tooling will auto-detect them without additional configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091162
Note:** If the path entered is incorrect or invalid, the build system will fall back to auto-detection.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091163
Multiple Installations For multiple Visual Studio or Windows SDK installations, the latest version is used by default.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091164
If unspecified, default edition preference is "Enterprise", "Professional", "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091165
Additional Resources - [Repo Build Documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 091166
Data Collection & Use ## Overview NVIDIA Omniverse Kit Application Template collects anonymous usage data to help improve software performance and aid in diagnostic purposes.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 091167
Rest assured, no personal information such as user email, name or any other PII field is collected.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 091168
Purpose Omniverse Kit Application Template starts collecting data when you begin interaction with our provided software.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 091169
After creating an application with the `template new` tooling, go to the `source/apps` directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 091170
Locate the `.kit` file for the application you want to disable telemetry for.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 091171
Find the following section in the `.kit` file: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = true ``` 4.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 091172
Change `enableAnonymousData` to `false`: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = false ``` Disabling telemetry stops data collection from your application.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 091173
Kit SDK Tooling Guide This document provides an overview of the practical aspects of using the tooling provided in the `kit-app-template`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091174
Intended for users with a basic familiarity with command-line operations, this guide offers typical usage patterns and recommendations for effective tool use.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091175
For a complete list of options for a given tool, use the help command: `./repo.sh [tool] -h` or `.\repo.bat [tool] -h`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091176
Overview of Tools The `kit-app-template` repository includes several tools designed to streamline the development of applications and extensions within the Omniverse Kit SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091177
Available Tools - `template` - `build` - `launch` - `test` - `package` Each tool plays a specific role in the development workflow: ## Template Tool **Command:** `./repo.sh template` or `.\repo.bat template` ### Purpose The template tool facilitates the initiation of new projects by generating scaffolds for applications or extensions based on predefined templates located in `/templates/templates.toml`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091178
Usage The template tool has three main commands: `list`, `new`, `replay`, `modify`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091179
`list` Lists available templates without initiating the configuration wizard.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091180
Linux:** ```bash ./repo.sh template list ``` **Windows:** ```powershell .\repo.bat template list ``` #### `new` Creates new applications or extensions from templates with interactive prompts guiding you through various configuration choices.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091181
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` #### `replay` In cases where automation is required for CI pipelines or other scripted workflows, it is possible to record and replay the `template new` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091182
Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the Application `.kit` file you want to update.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091183
Next, select (using Space) the Template Layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091184
After the operation completes, rebuild (`./repo.sh build` or `.\repo.bat build`) the project to pull in the new extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091185
What `template new` Modifies When creating applications, the template tool automatically updates build configuration files: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091186
`premake5.lua`** - Adds `define_app("appname.kit")` so the build system discovers your application 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091187
`repo.toml`** - Adds the app path to `repo_precache_exts.apps` so dependent extensions are pre-cached at build time 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091188
`source/rendered_template_metadata.json`** - Records which templates were rendered (enables `template modify` and `template list`) 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091189
Setup extension** (some templates) - Creates an extension in `source/extensions/` for application-specific initialization **Extensions** are automatically discovered by the Kit build system based on directory structure, so no build file modifications are needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091190
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091191
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091192
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091193
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091194
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091195
It includes all resources located in the `source/` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091196
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091197
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091198
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091199
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091200
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091201
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091202
`-p` or `--package`:** Launches a packaged application from a specified path.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091203
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091204
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091205
Any flags added after `--` will be passed through to Kit directly.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091206
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091207
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091208
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091209
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091210
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091211
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091212
Applications configurations (`.kit` files) are tested to ensure they can startup and shutdown without issue.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091213
However, the tests written within the extensions will dictate a majority of application functionality testing.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091214
Extension templates provided by the Kit App Template repository include sample tests which can be expanded upon to increase test coverage as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091215
Usage Always run a build before testing: **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ## Package Tool **Command:** `./repo.sh package` or `.\repo.bat package` ### Purpose This tool prepares your application for distribution or deployment by packaging it into a distributable format.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091216
Usage Always run a build before packaging to ensure the application is up-to-date: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` Additional launch options: - **`-n` or `--name`:** Specifies the package (or container image) name.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091217
Linux:** ```bash ./repo.sh package -n ``` **Windows:** ```powershell .\repo.bat package -n ``` - **`--thin`:** Creates a thin package that includes only custom extensions and configurations for required registry extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091218
Linux:** ```bash ./repo.sh package --thin ``` **Windows:** ```powershell .\repo.bat package --thin ``` :warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091219
The version is set within the `tools/VERSION.md` file.** ## Containerization Tool **Command:** `./repo.sh package_container` or `.\repo.bat package_container` ### Purpose The containerization tool provided by `repo_kit_tools` supports containerization of applications.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091220
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091221
How It Works The tool performs these steps: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091222
Creates a fat package** - Stages all dependencies into a temp directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091223
Trims unused extensions** - Removes disabled extensions to minimize image size 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091224
Splits into Docker layers** - Base layer (kit kernel + extscache) and app layer for faster rebuilds 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091225
Builds the container** - Uses a configurable base image (default: `nvcr.io/nvidia/omniverse/ov-base-ubuntu-22`) The container entrypoint supports runtime configuration via environment variables (`NVDA_KIT_ARGS`, `NVDA_KIT_NUCLEUS`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091226
Usage Always run a build before packaging to ensure the application is up-to-date: - **`package_container`:** Packages the application as a container image (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091227
When using the `package_container`, the user will be asked to select a `.kit` file to use within the entry point script for the container.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091228
This can also be specified without user interaction by passing it appropriate `.kit` file name via the `--app ${path_to_kit_file}` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091229
Linux:** ```bash ./repo.sh package_container ``` **Windows:** ```powershell .\repo.bat package_container ``` Additional command options: - **`--app`:** Specify the Kit app to containerize.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091230
One of defined in the config.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091231
Linux:** ```bash ./repo.sh package_container --app ${path_to_kit_file} ``` **Windows:** ```powershell .\repo.bat package_container --app ${path_to_kit_file} ``` - **`--image-tag`:** Optional image tag override to use for docker image.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091232
If includes ':', it will be used as is, e.g.: name:tag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091233
Linux:** ```bash ./repo.sh package_container --image-tag [container_image_name:container_image_tag] ``` **Windows:** ```powershell .\repo.bat package_container --image-tag [container_image_name:container_image_tag] ``` - **`-p` or `--from-package`:** Use package from 'kit-app-template/_build/packages/kit-app-template*.${config}.*' instead of a root folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091234
Linux:** ```bash ./repo.sh package_container -p ``` **Windows:** ```powershell .\repo.bat package_container -p ``` - **`-g` or `--generate`:** Generate default container template files into the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091235
Passed argument is the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091236
Linux:** ```bash ./repo.sh package_container -g ``` **Windows:** ```powershell .\repo.bat package_container -g ``` ## Additional Resources - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 091237
Configuring Kit App Template for DGXC Deployment This document covers Kit App Template specific configuration for deploying to NVIDIA DGX Cloud.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091238
For complete deployment instructions, see the [public DGXC documentation]( ## Streaming Layer Selection When creating your application with `./repo.sh template new`, select the appropriate streaming layer for DGXC: | Kit Version | Layer to Select | Generated File | |-------------|-----------------|----------------| | 108.x+ | `nvcf_streaming` | `{app_name}_nvcf.kit` | | 107.x | `ovc_streaming` | `{app_name}_ovc.kit` | | 106.x | `ovc_streaming` | `{app_name}_ovc.kit` | ### Selection Process 1.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091239
Run `./repo.sh template new` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091240
Select **Application** and your desired template 3.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091241
When prompted "Do you want to add application layers?", select **Yes** 4.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091242
`omni.cloud.open_stage`**: Provides Nucleus server connectivity for cloud deployments.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091243
[settings.exts."omni.kit.window.content_browser"] show_only_collections.6 = "" # Hides the "My Computer" connection from the content browser.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091244
``` ## Containerization After building (`./repo.sh build`), create a container: ```bash ./repo.sh package_container --image-tag myapp:v1.0 ``` When prompted, select the streaming `.kit` file (`*_ovc.kit` or `*_nvcf.kit`).
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091245
Next Steps For deployment to DGXC (container upload, NVCF function creation, portal registration), see: - [Containerization Guide]( - Building and packaging - [Deploying Kit Apps]( - NGC upload and NVCF deployment - [Troubleshooting]( - Common issues and FAQs ## Version-Specific Notes ### Kit 108.x+ (`main` branch) Select `nvcf_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091246
Streaming dependencies are automatically configured.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091247
Kit 107.x (`production/107.3` branch) Select `ovc_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091248
No manual edits required.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091249
Kit 106.x (`production/106.5` branch) The streaming layer may require manual edits.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091250
See the [public containerization guide]( for the "Replace Streaming Extension" section.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091251
Troubleshooting For deployment issues, log analysis, and common errors, see the [DGXC FAQs and Troubleshooting](
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 091252
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091253
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091254
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091255
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091256
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091257
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091258
Collaborating on large-scale design projects in real-time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091259
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091260
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091261
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091262
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091263
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091264
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091265
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091266
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091267
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091268
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091269
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091270
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091271
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091272
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091273
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091274
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091275
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091276
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091277
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091278
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091279
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091280
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091281
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091282
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091283
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091284
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091285
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091286
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091287
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091288
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091289
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091290
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091291
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091292
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091293
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091294
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091295
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091296
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091297
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091298
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091299
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091300
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091301
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091302
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091303
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091304
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091305
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091306
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091307
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091308
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091309
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091310
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091311
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091312
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091313
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091314
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091315
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091316
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091317
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091318
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091319
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091320
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091321
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091322
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091323
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091324
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091325
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091326
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091327
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091328
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091329
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091330
:warning: **Important**: These layers are not standalone application templates.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091331
They must be used in conjunction with a base application template.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091332
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091333
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091334
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091335
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091336
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091337
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091338
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091339
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091340
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091341
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091342
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091343
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091344
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091345
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091346
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091347
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091348
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091349
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091350
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091351
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091352
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091353
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091354
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091355
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091356
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091357
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091358
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091359
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091360
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091361
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091362
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091363
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091364
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091365
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091366
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091367
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091368
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091369
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091370
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091371
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091372
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091373
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091374
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091375
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091376
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091377
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091378
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091379
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091380
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091381
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091382
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091383
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091384
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091385
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091386
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091387
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091388
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091389
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091390
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091391
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091392
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091393
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091394
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091395
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091396
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091397
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091398
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091399
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091400
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091401
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091402
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091403
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091404
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091405
Start the Streaming Client Follow the [Quick Start instructions in the we
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091406
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091407
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091408
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091409
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091410
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091411
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091412
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091413
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091414
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091415
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091416
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091417
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091418
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091419
Subsequent extensions can be added to the .kit file manually.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091420
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091421
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091422
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091423
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091424
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091425
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091426
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091427
Setup Extension -> kit_service_setup* - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091428
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091429
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091430
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091431
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091432
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091433
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091434
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091435
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091436
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091437
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091438
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091439
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091440
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091441
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091442
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091443
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091444
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091445
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091446
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091447
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091448
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091449
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091450
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091451
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091452
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091453
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091454
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091455
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091456
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091457
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091458
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091459
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091460
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091461
The base application `.kit` file should be used for containerization.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091462
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091463
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091464
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091465
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091466
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091467
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091468
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091469
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091470
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091471
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091472
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091473
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091474
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091475
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091476
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091477
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091478
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091479
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091480
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091481
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091482
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091483
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091484
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091485
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091486
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091487
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091488
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091489
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091490
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091491
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091492
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091493
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091494
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091495
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091496
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091497
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091498
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091499
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091500
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091501
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091502
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091503
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091504
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091505
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091506
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091507
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091508
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091509
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091510
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091511
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091512
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091513
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091514
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091515
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091516
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091517
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091518
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091519
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091520
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091521
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091522
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091523
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091524
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091525
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091526
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091527
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091528
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091529
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091530
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091531
:warning: **Important:** Before proceeding with the cloning step, ensure that Git Large File Storage (Git LFS) is installed on your system.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091532
To verify this, run the following command in your terminal: ```bash git lfs --version ``` If the command returns a version number, Git LFS is installed correctly.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091533
If not, you will need to install Git LFS.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091534
You can download and install it from the official website [here]( #### Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091535
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091536
During Application configuration, you will be prompted for information about these extensions.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091537
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091538
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091539
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091540
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091541
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091542
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091543
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091544
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091545
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091546
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091547
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091548
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091549
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091550
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091551
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091552
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091553
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091554
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091555
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091556
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091557
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091558
The USD Viewer template includes sample assets for this purpose.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091559
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091560
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091561
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091562
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091563
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091564
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091565
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091566
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091567
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091568
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091569
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091570
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091571
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091572
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091573
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091574
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091575
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091576
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091577
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091578
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091579
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091580
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091581
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091582
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091583
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091584
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091585
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091586
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091587
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091588
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091589
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091590
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091591
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091592
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091593
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091594
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091595
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091596
Service Setup Extension Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Service Setup Extension Template is designed to facilitate the configuration and setup of a headless service that leverages the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091597
Though it is possible in this case, setup extensions are not typically intended to be used as a generic extension but as a specific component of a particular application.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091598
Use Cases This setup extension is well suited for: - Developers building headless services that require Kit SDK functionalities.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091599
Key Features - Sample ServiceAPIRouter setup.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091600
Sample endpoint to demonstrate interaction patterns within service Kit SDK and OpenUSD.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091601
Usage This extension is automatically created and configured when you generate a new service application using the [Service Application Template](../../apps/kit_service/README.md).
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091602
Additional Learning - [Omniverse Kit Service Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091603
Python UI Extension Template ## Overview The Python UI Extension Template offers a simple starting point for developers looking to build Python-based extensions with performant User Interfaces.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091604
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091605
Use Cases This template is ideal for developers looking to build: - UI based extensions that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091606
Key Features - A simple starter UI demonstrating how to build using the Omni UI framework.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091607
Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091608
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091609
Usage This section provides instructions for the setup and use of the Python UI Extension Template.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091610
Getting Started To get started with the Python UI Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091611
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091612
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091613
Select desired template with arrow keys ↑↓:**: Python UI Extension - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091614
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091615
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091616
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091617
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091618
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091619
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091620
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091621
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091622
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Omni UI Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091623
USD Explorer Setup Extension Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer Setup Extension Template is specifically designed to configure the USD Explorer Template application.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091624
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Explorer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091625
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Explorer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091626
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091627
Key Features - Custom configurations tailored to the USD Explorer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091628
Usage This extension is automatically created and configured when you generate a new application based on the [USD Explorer Template Application](../../apps/usd_explorer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091629
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091630
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091631
Basic C++ Extension Template ## Overview The Basic C++ Extension Template is a starting point for developers looking to build C++ based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091632
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091633
Note for Windows C++ Developers** : This template requires that Visual Studio is installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091634
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091635
For additional C++ configuration information [see here](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091636
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091637
Performance sensitive extensions that require the performance benefits of C++.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091638
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091639
Integrating with existing C++ libraries or codebases.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091640
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091641
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091642
Usage This section provides instructions for the setup and use of the Basic C++ Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091643
Getting Started To get started with the Basic C++ Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091644
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091645
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091646
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091647
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091648
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091649
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091650
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091651
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091652
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091653
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091654
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091655
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091656
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091657
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091658
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091659
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091660
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091661
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091662
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091663
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091664
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091665
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091666
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091667
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091668
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091669
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091670
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091671
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091672
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091673
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091674
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091675
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091676
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091677
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091678
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091679
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091680
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091681
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091682
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091683
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091684
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091685
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091686
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091687
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091688
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091689
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091690
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091691
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091692
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091693
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091694
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091695
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091696
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091697
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091698
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091699
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091700
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091701
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091702
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091703
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091704
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091705
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091706
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091707
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091708
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091709
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091710
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091711
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091712
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091713
Integrating other C++ or Python libraries as needed.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091714
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091715
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091716
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091717
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091718
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091719
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091720
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091721
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091722
Managing the state for selecting objects within the scene.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091723
Performing actions without traditional in-app UI and menus.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091724
Key Features - Remote communication with the Kit application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091725
Scene loading capabilities.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091726
State management for object selection within the USD Viewer.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091727
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091728
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091729
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091730
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091731
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091732
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091733
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091734
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091735
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091736
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091737
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091738
Changelog The format is based on [Keep a Changelog]( ## [0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091739
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091740
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091741
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091742
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091743
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091744
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091745
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091746
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091747
Args: object: The bound object to register.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091748
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091749
Args: object: The bound object to deregister.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091750
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091751
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091752
Return: The bound object if it exists, an empty object otherwise.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091753
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091754
Return: The id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091755
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091756
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091757
Return: The bound object that was created.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091758
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091759
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091760
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091761
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091762
Args: value_to_multiply: The value to multiply by.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091763
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091764
Return: The toggled bool value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091765
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091766
Args: value_to_append: The value to append.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091767
Return: The new string value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091768
)", py::arg("value_to_append")) /**/; } ```
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 091769
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091770
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091771
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091772
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091773
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 091774
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091775
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091776
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091777
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091778
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091779
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091780
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091781
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091782
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091783
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091784
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091785
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091786
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091787
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091788
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091789
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091790
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091791
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091792
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091793
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091794
{{ extension_display_name }} [{{ extension_name }}] A simple python UI extension example.
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091795
Use it as a starting point for your extensions.
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091796
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - 2024-03-13 - Initial version based on kit service extension template
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 091797
{{ extension_display_name }} [{{ extension_name }}] This is an example of a simple Kit Service extension.
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091798
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091799
Version Bump Skill Automates kit-sdk version bumps by updating version files, creating a branch, committing, and optionally pushing a merge request.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091800
Read Current State Read these files to determine the current version: - `tools/VERSION.md` — contains the current version string (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091801
`110.0.0-stage.17`) - `tools/deps/kit-sdk.packman.xml` — contains the current kit-kernel packman version in the `version="..."` attribute Display the current version and kit-kernel version to the user.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091802
Ask Build Type Use `AskUserQuestion` to ask: **"Is this a stage or rc build?"** with two options: `stage` and `rc`.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091803
Show the current version from `tools/VERSION.md` for context.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091804
Compute New Version Parse the current version from `tools/VERSION.md` which follows the format `X.Y.Z- .
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091805
`110.0.0-stage.17`).
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091806
Apply these transition rules: | Current Version | User picks | New Version | |---|---|---| | `X.Y.Z-stage.N` | stage | `X.Y.Z-stage.(N+1)` | | `X.Y.Z-stage.N` | rc | `X.Y.Z-rc.1` | | `X.Y.Z-rc.N` | rc | `X.Y.Z-rc.(N+1)` | | `X.Y.Z-rc.N` | stage | `X.Y.(Z+1)-stage.1` | Display the computed new version to the user.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091807
Auto-Detect Latest kit-kernel Version Query the omnipackages API to find available kit-kernel versions: ```bash curl -s " %2B&remote=cloudfront" ``` Where ` ` is extracted from the current version (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091808
Parse the JSON response: - Extract the `name` field from each item in the `items` array - Strip the platform/config suffix using this regex to get the base version: `^([\d.]+\+\w+\.\d+\.[a-f0-9]+\.gl)\.` - Deduplicate the base versions (multiple platform variants share the same base) - They are already sorted by `modificationTime` (newest first) Read the current kit-kernel version from `tools/deps/kit-sdk.packman.xml` to identify which ones are newer.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091809
If the newest available version matches the current kit-kernel version (i.e.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091810
there are no newer versions), notify the user that the kit-kernel is already up to date and exit without making any file changes.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091811
Otherwise, present the top available versions newer than the current one (up to 4) to the user via `AskUserQuestion`, with the newest version marked as "(Recommended)".
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091812
The "Other" option is automatically available for the user to paste a custom version.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091813
Show the current kit-kernel version for reference in the question text.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091814
Edit 3 Files Using the new version string from step 3 and the kit-kernel version from step 4: 1.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091815
`tools/VERSION.md`**: Replace the entire file content with the new version string (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091816
`110.0.0-stage.18`).
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091817
Do NOT include a trailing newline.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091818
`tools/deps/kit-sdk.packman.xml`**: Replace the `version="..."` attribute value on the ` ` line.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091819
The new value should be the selected kit-kernel base version + `.${platform_target_abi}.${config}`.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091820
For example: ``` version="110.0.0+feature.275000.abcd1234.gl.${platform_target_abi}.${config}" ``` 3.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091821
`templates/omni.all.template.extensions.kit`**: Replace the `# Kit SDK Version:` comment line.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091822
The new value should use just the base version (without platform suffix).
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091823
For example: ``` # Kit SDK Version: 110.0.0+feature.275000.abcd1234.gl ``` ### 6.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091824
Confirm and Push Use `AskUserQuestion` with yes/no options to confirm.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091825
The question should summarize the changes: - Previous version → new version (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091826
`110.0.0-stage.17` → `110.0.0-stage.18`) - Previous kit-kernel → new kit-kernel version - Ask: **"Create branch, commit, and push merge request?"** If the user declines, revert the 3 files back to their original content (restore the values read in step 1) and stop.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091827
If the user accepts, perform these substeps: **6a.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091828
Create Branch** Before creating the new branch, capture the current branch name to use as the MR target: ```bash git rev-parse --abbrev-ref HEAD ``` Derive the git username by running `git config user.email` and extracting the part before `@`.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091829
Create and switch to a new branch: ```bash git checkout -b / ``` For example: `gamato/110.0.0-stage.18` **6b.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091830
Commit** Stage and commit exactly the 3 modified files: ```bash git add tools/VERSION.md tools/deps/kit-sdk.packman.xml templates/omni.all.template.extensions.kit git commit -m " " ``` The commit message is just the version string (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091831
`110.0.0-stage.18`), matching the existing convention.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091832
Runs a set of commands using the runners shell - name: Run a multi-line script run: | echo Add other actions to build, echo test, and deploy your project.
स्रोत: omniverse-marketplace/.github/workflows/blank.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091833
name: Deploy GitHub Pages on: push: branches: - main jobs: deploy: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Deploy to GitHub Pages uses: peaceiris/actions-gh-pages@v3 with: github_token: ${{ secrets.GITHUB_TOKEN }} publish_dir: ./
स्रोत: omniverse-marketplace/.github/workflows/pages.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091834
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: shiromani-rampal-saini/public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 091835
Sacred Audio शिरोमणि अंनत असीम इश्क़ की क्षमता यह ध्वनि केवल श्रवण नहीं, चेतना की अनुभूति है।
स्रोत: shiromani-rampal-saini/public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 091836
▶ अंनत असीम इश्क़ – दिव्य ध्वनि Track 1 Track 2 Track 3
स्रोत: shiromani-rampal-saini/public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 091837
Runs a set of commands using the runners shell - name: Run a multi-line script run: | echo Add other actions to build, echo test, and deploy your project.
स्रोत: Omniverse-/.github/workflows/blank.yml · स्वतंत्र परीक्षण अपेक्षित।

## 091838
🔗 Shirmani Research Repositories — Central Integration यह फ़ाइल दो मौजूदा repositories को **Nishpaksh Samaj Omniverse Truth** के केंद्रीय ज्ञान-संग्रह से जोड़ती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091839
Shirmani Research Paper Repository: मुख्य विषय: - Time Deconstruction Theory - Neurobiology of Self - Ego Dissolution Framework - Heart-Mind Balance Model - research presentation / publication material केंद्रीय परियोजना में इसकी भूमिका: **Research Papers / Research Archive** ## 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091840
इससे पुराने Git इतिहास, स्वतंत्र GitHub Pages और मौजूदा सामग्री सुरक्षित रहती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091841
आगे आवश्यकता होने पर चयनित सामग्री को केंद्रीय repository में **स्रोत-संदर्भ और मूल repository attribution के साथ** व्यवस्थित रूप से पुनर्संयोजित किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091842
केंद्रीय repository = canonical knowledge hub 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091843
Research Paper repository = research archive 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091844
Research Institute repository = institute/archive/media layer 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091845
सभी repositories में परस्पर स्पष्ट navigation 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091846
duplicate सामग्री को धीरे-धीरे कम करना 6.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091847
प्रत्येक बड़े दावे के लिए स्रोत/स्थिति/अनिश्चितता स्पष्ट रखना --- **Canonical Hub:** *Integration document — continuously maintained.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 091848
Research Paper 17 — Practical Self-Observation Framework ## Status Conceptual/methodological proposal.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091849
Abstract यह paper “खुद का निरीक्षण” को एक structured reflective practice के रूप में स्पष्ट करने का प्रयास करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091850
इसे किसी विशेष मानसिक या चिकित्सीय परिणाम की गारंटी के रूप में प्रस्तुत नहीं किया जाता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091851
Framework **घटना → तत्काल अनुभव → विचार/व्याख्या → प्रतिक्रिया → परिणाम → पुनरावलोकन** ## Safeguards - अनुभव और तथ्य अलग रखें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091852
स्मृति को पूर्ण रिकॉर्ड न मानें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091853
बाहरी प्रमाण उपलब्ध हो तो जाँचें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091854
असहमति को त्रुटि का प्रमाण न मानें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091855
नकारात्मक परिणामों को छिपाएँ नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091856
Proposed study एक स्पष्ट दैनिक निरीक्षण प्रोटोकॉल बनाया जा सकता है, जिसकी adherence और self-reported outcomes को पूर्वनिर्धारित तरीके से दर्ज किया जाए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091857
यदि भविष्य में अध्ययन किया जाए तो protocol, sample, analysis और limitations सार्वजनिक किए जाएँ।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091858
Conclusion खुद का निरीक्षण तभी अधिक उपयोगी शोध-पद्धति बन सकता है जब वह स्पष्ट, दोहराने योग्य और आत्म-संशोधन के लिए खुला हो।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091859
शमीकरण: एक संतुलित परीक्षण-पद्धति **प्रकार:** Theoretical / Methodological Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश “शमीकरण” को अनुभव, विचार, प्रमाण और वैकल्पिक व्याख्याओं के बीच संतुलित परीक्षण की प्रस्तावित पद्धति के रूप में व्यवस्थित किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 091860
उद्देश्य पूर्वनिर्धारित निष्कर्ष को सिद्ध करना नहीं, बल्कि निष्कर्ष बनने की प्रक्रिया को पारदर्शी बनाना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 091861
शोध प्रश्न क्या अनुभव → प्रश्न → प्रमाण → वैकल्पिक व्याख्या → संशोधन का चक्र उपयोगी सामान्य पद्धति बन सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 091862
पद्धति अवधारणा-विश्लेषण, उदाहरण-निर्माण और भविष्य के empirical परीक्षण के लिए operational definitions।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 091863
प्रस्तावित प्रक्रिया **अनुभव → दावा → प्रश्न → प्रमाण → प्रतिवाद → वैकल्पिक व्याख्या → निष्कर्ष → पुनर्परीक्षण** ## सीमाएँ “शमीकरण” इस परियोजना में प्रस्तावित शब्द और मॉडल है; इसकी स्वतंत्र अकादमिक मान्यता या प्रभावशीलता इस पत्र से स्थापित नहीं होती।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 091864
निष्कर्ष पद्धति की सबसे महत्वपूर्ण कसौटी उसका स्वयं परीक्षण योग्य होना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 091865
Research Paper 16 — Nature-Compatible Philosophy ## Status Conceptual/philosophical paper.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091866
No empirical results are claimed.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091867
Abstract यह paper निष्पक्ष समझ के संदर्भ में मनुष्य-प्रकृति संबंध के लिए एक परीक्षणयोग्य वैचारिक ढाँचा प्रस्तावित करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091868
केंद्रीय प्रश्न है: क्या किसी जीवन-दृष्टि को उसके घोषित मूल्यों के साथ-साथ उसके वास्तविक पर्यावरणीय प्रभावों से भी परखा जाना चाहिए?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091869
Core propositions 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091870
मूल्य-घोषणा और वास्तविक व्यवहार अलग चीजें हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091871
प्रकृति-सम्मत दावा प्रभाव के प्रमाण से मजबूत या कमजोर हो सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091872
व्यक्तिगत अनुभव सार्वभौमिक वैज्ञानिक निष्कर्ष के समान नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091873
वैकल्पिक व्याख्याएँ हमेशा दर्ज की जानी चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091874
Proposed research questions - कौन-से दैनिक व्यवहार पर्यावरणीय प्रभाव को सबसे अधिक बदलते हैं?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091875
क्या आत्म-निरीक्षण आधारित अभ्यास व्यवहार में मापने योग्य परिवर्तन ला सकते हैं?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091876
किन परिस्थितियों में व्यक्तिगत संतुष्टि और पर्यावरणीय जिम्मेदारी में तनाव पैदा होता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091877
Method proposal पूर्व-पंजीकृत परिकल्पनाएँ, स्पष्ट outcome measures, comparison groups जहाँ उपयुक्त हों, और reproducible analysis।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091878
वास्तविक अध्ययन होने तक कोई परिणाम नहीं माना जाएगा।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091879
Conclusion दार्शनिक प्रस्ताव को व्यवहारिक परिणामों से जोड़ने के लिए प्रमाण और आत्म-संशोधन दोनों आवश्यक हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091880
निष्पक्ष समझ का वैचारिक मॉडल **प्रकार:** Conceptual / Philosophical Research Paper **लेखक:** शिरोमणि रामपॉल सैनी **स्थिति:** प्रारंभिक वैचारिक मसौदा ## सारांश यह शोध-पत्र “निष्पक्ष समझ” को ऐसी वैचारिक प्रक्रिया के रूप में प्रस्तावित करता है जिसमें व्यक्ति अपने अनुभव, विश्वास और निष्कर्षों पर समान परीक्षण-कसौटी लागू करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091881
यह किसी सार्वभौमिक सत्य की स्थापना का दावा नहीं करता; उद्देश्य एक परीक्षण योग्य दार्शनिक मॉडल प्रस्तुत करना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091882
मुख्य शब्द:** निष्पक्ष समझ, आत्म-परीक्षण, प्रमाण, तर्क, आत्म-संशोधन ## 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091883
शोध समस्या व्यक्तिगत विश्वास अनुभव, संस्कृति, प्राधिकार और पूर्व धारणाओं से प्रभावित हो सकते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091884
प्रश्न यह है कि क्या व्यक्ति अपने विचारों पर वही कसौटी लागू करता है जो दूसरों के विचारों पर करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091885
शोध प्रश्न क्या “समान कसौटी” को स्पष्ट वैचारिक मॉडल में बदला जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091886
वैकल्पिक व्याख्या देखना 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091887
नए प्रमाण पर निष्कर्ष संशोधित करना ## 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091888
पद्धति यह दार्शनिक अवधारणा-विश्लेषण है; empirical study नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091889
भविष्य का परीक्षण प्रतिभागियों से अपने और दूसरे व्यक्ति के समान प्रकार के दावों का मूल्यांकन कराया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091890
निष्पक्षता का operational measure पहले से तय करना होगा।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091891
सीमाएँ वर्तमान पत्र वास्तविक प्रतिभागियों या सांख्यिकीय परिणामों का दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091892
निष्कर्ष निष्पक्ष समझ को अंतिम उत्तर के बजाय आत्म-संशोधन की पद्धति के रूप में देखना इसे परीक्षण योग्य बनाता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091893
Research Paper 18 — Language, Art, Culture and Public Knowledge ## Abstract This conceptual paper examines how language, artistic expression, cultural inheritance, and digital publication interact with philosophical claims.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091894
The paper proposes a distinction between experience, interpretation, hypothesis, and externally verifiable fact.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091895
Status This is a **conceptual and methodological paper**.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091896
It reports no completed experiment, participant sample, statistical result, or causal finding.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091897
Core model **Experience → Expression → Interpretation → Claim → Evidence → Public dialogue → Revision** The model is intended to reduce a common category error: treating a personally meaningful experience as if every interpretation derived from it were automatically an externally established fact.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091898
Research questions 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091899
Does clearer separation of experience and factual claims improve reader comprehension?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091900
Does plain-language presentation improve accessibility without reducing conceptual precision?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091901
Can structured counterargument sections improve readers' ability to distinguish claims from evidence?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091902
How do poetry, music, and visual art affect reflection without being mistaken for empirical evidence?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091903
Does version-controlled publication improve correction and traceability of public philosophical material?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091904
Proposed study design A future study could preregister: - participant eligibility, - comprehension measures, - comparison texts, - randomization procedure where appropriate, - primary and secondary outcomes, - exclusion criteria, - analysis plan, - adverse or null-result reporting.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091905
No outcome should be claimed until data are actually collected and analyzed.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091906
Ethical principles - Do not manufacture evidence.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091907
Do not present artistic symbolism as scientific proof.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091908
Do not conceal meaningful counterarguments.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091909
Preserve uncertainty where evidence is incomplete.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091910
Correct public errors visibly.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091911
Respect readers' freedom to disagree.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091912
Practical publication standard Each major public claim should, where feasible, carry one of these labels: **[EXPERIENCE] [PHILOSOPHICAL CLAIM] [HYPOTHESIS] [FACT + SOURCE] [OPEN QUESTION]** This labeling system can be implemented across the digital corpus.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091913
Conclusion A philosophy can remain deep while becoming more testable.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091914
A poem can remain poetic while clearly being presented as poetry.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091915
A personal experience can remain meaningful without being promoted beyond what its evidence supports.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091916
The proposed framework therefore treats clarity, openness to criticism, and self-correction as integral parts of public philosophical practice.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 091917
स्वतंत्र समझ और प्राधिकार **प्रकार:** Conceptual Social Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र जाँचता है कि व्यक्ति किसी गुरु, संस्था, शिक्षक या अन्य प्राधिकार की बात को किस प्रकार स्वतंत्र रूप से परख सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091918
लक्ष्य प्राधिकार को स्वतः अस्वीकार या स्वीकार करना नहीं, बल्कि प्रमाण और तर्क को स्वतंत्र कसौटी के रूप में रखना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091919
शोध प्रश्न क्या प्राधिकार और स्वतंत्र परीक्षण के बीच ऐसा मॉडल बनाया जा सकता है जिसमें दोनों के कार्य स्पष्ट हों?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091920
प्रस्ताव प्राधिकार सूचना दे सकता है; स्वतंत्र परीक्षण दावे की जाँच करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091921
सीमा यह पत्र किसी विशिष्ट व्यक्ति या संस्था के बारे में तथ्यात्मक आरोप प्रस्तुत नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091922
व्यक्तिगत अनुभव और सार्वभौमिक दावे **प्रकार:** Philosophy of Knowledge **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश व्यक्तिगत अनुभव किसी व्यक्ति के लिए वास्तविक अनुभव हो सकता है, लेकिन उससे सार्वभौमिक निष्कर्ष निकालने के लिए अतिरिक्त तर्क और स्वतंत्र प्रमाण आवश्यक होते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091923
अनुभव — “मुझे ऐसा महसूस हुआ” 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091924
व्याख्या — “इसका अर्थ यह है” 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091925
सार्वभौमिक दावा — “यह सभी के लिए सत्य है” तीसरे स्तर के लिए स्वतंत्र जाँच आवश्यक है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091926
निष्कर्ष अनुभव का सम्मान और उसके दावे की स्वतंत्र जाँच एक-दूसरे के विरोधी नहीं हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091927
हृदय और मस्तक दृष्टिकोण: एक दार्शनिक मॉडल **प्रकार:** Conceptual Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र “हृदय दृष्टिकोण” और “मस्तक दृष्टिकोण” को क्रमशः भावात्मक प्रत्यक्षता तथा विचारात्मक/विश्लेषणात्मक प्रक्रिया के रूपकों के रूप में स्पष्ट करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091928
यह जैविक हृदय के बारे में वैज्ञानिक दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091929
मुख्य प्रश्न क्या भावना और तर्क को प्रतिस्पर्धी नहीं बल्कि पूरक प्रक्रियाओं के रूप में मॉडल किया जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091930
मॉडल हृदय = एहसास और मूल्य-संवेदना का रूपक।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091931
मस्तक = भाषा, स्मृति, तुलना, योजना और तर्क का रूपक।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091932
प्रस्ताव पहले अनुभव को पहचाना जाए, फिर संज्ञानात्मक विश्लेषण से विकल्पों और परिणामों की जाँच की जाए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091933
परीक्षण निर्णय-लेने के कार्यों में भावनात्मक जागरूकता और तर्कात्मक जाँच के संयुक्त प्रभाव का अध्ययन किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091934
सीमा यह पत्र किसी प्रतिशत-संतुलन को वैज्ञानिक रूप से स्थापित नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 091935
दावा, प्रमाण और आत्म-संशोधन **प्रकार:** Methodological Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र शोध-दैनंदिनी मॉडल प्रस्तावित करता है: दावा, प्रमाण, अनिश्चितता, विरोधी प्रमाण और अगला परीक्षण।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091936
उद्देश्य यह देखना है कि कोई विचार नए प्रमाण पर कितनी पारदर्शिता से संशोधित होता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091937
प्रस्तावित प्रोटोकॉल हर प्रमुख दावे के साथ पाँच फ़ील्ड रखें: दावा, समर्थन, विरोधी प्रमाण, अनिश्चितता, अगला परीक्षण।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091938
संभावित डेटा संस्करण इतिहास, शोध-दैनंदिनी और स्वतंत्र समीक्षकों की टिप्पणियाँ।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091939
सीमा प्रारंभिक प्रस्ताव में वास्तविक longitudinal dataset नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091940
“संपूर्ण संतुष्टि” की अवधारणा: परिभाषा और परीक्षण **प्रकार:** Conceptual / Measurement Proposal **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश “संपूर्ण संतुष्टि” को इस परियोजना में निरंतर संतुष्टि के व्यक्तिगत अनुभव के रूप में प्रस्तावित किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 091941
यह पत्र अवधारणा को स्पष्ट operational definition में बदलने की आवश्यकता पर केंद्रित है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 091942
शोध प्रश्न क्या “संपूर्ण संतुष्टि” को स्पष्ट, दोहराने योग्य और नैतिक self-report तथा behavioral measures में operationalize किया जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 091943
प्रस्तावित आयाम - वर्तमान क्षण में संतुष्टि - आंतरिक संघर्ष की अनुभूति - भविष्य-निर्भरता की अनुभूति - निर्णय के बाद स्थिरता - प्रतिकूल परिस्थिति में संतुलन ## सीमा वर्तमान पत्र में कोई validated instrument या empirical prevalence estimate नहीं दिया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 091944
डिजिटल दार्शनिक ज्ञान-संग्रह का मॉडल **प्रकार:** Digital Humanities / Knowledge Architecture **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र 100 ग्रंथों और दीर्घकालीन 100,000-पृष्ठ corpus को डिजिटल रूप में व्यवस्थित करने का मॉडल प्रस्तुत करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091945
लक्ष्य सामग्री की मात्रा के साथ खोज, संस्करण नियंत्रण, स्रोत-स्पष्टता और पुनरावृत्ति नियंत्रण बनाए रखना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091946
प्रस्तावित वास्तुकला - विषय-आधारित ग्रंथ - अध्याय और उप-अध्याय - शब्दावली - स्रोत-सूची - दावे और प्रमाण - संशोधन इतिहास - स्थायी लिंक - शोध-पत्र संग्रह - multilingual विस्तार ## मूल्यांकन भविष्य में navigation success, search accuracy, broken links और duplicate-content ratio जैसे संकेतकों से प्रणाली का मूल्यांकन किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091947
सीमा यह knowledge-architecture proposal है; वर्तमान पत्र usability study के परिणाम का दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091948
प्रकृति, मानव गरिमा और व्यवहारिक दर्शन **प्रकार:** Applied Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र प्रस्तावित करता है कि किसी दार्शनिक ढाँचे का व्यवहारिक मूल्य उसके वास्तविक जीवन में प्रकृति, मानव गरिमा और स्वतंत्रता के प्रति प्रभाव से भी जाँचा जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091949
शोध प्रश्न क्या ecological responsibility और human dignity को दार्शनिक सिद्धांतों के मूल्यांकन में operational criteria बनाया जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091950
प्रकृति पर प्रभाव 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091951
व्यक्ति की स्वायत्तता 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091952
संसाधनों और शक्ति में पारदर्शिता ## सीमा इस पत्र में कोई causal effect स्थापित नहीं किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 091953
आत्म-परीक्षण और मेटाकॉग्निशन **प्रकार:** Conceptual Research Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र “खुद का निरीक्षण” को metacognitive प्रक्रिया के साथ संवाद में रखता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091954
लक्ष्य यह समझना है कि व्यक्ति अपने विचार, विश्वास और निर्णय-प्रक्रिया को कैसे देख सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091955
मुख्य प्रश्न क्या नियमित self-observation से व्यक्ति अपने निष्कर्षों की अनिश्चितता और पूर्वधारणाओं को अधिक स्पष्ट रूप से पहचान सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091956
प्रस्तावित मॉडल अनुभव → विचार की पहचान → पूर्वधारणा → भावनात्मक प्रभाव → प्रमाण → वैकल्पिक विचार → संशोधित निष्कर्ष।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091957
संभावित अध्ययन दैनिक reflective journal और निर्णय-कार्य के longitudinal अध्ययन किए जा सकते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091958
सीमाएँ यह पत्र किसी विशेष intervention की प्रभावशीलता सिद्ध नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091959
निष्कर्ष आत्म-परीक्षण को व्यवस्थित रिकॉर्ड में बदलना भविष्य के empirical research का आधार बन सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 091960
शोध-पत्र संग्रह यह संग्रह “निष्पक्ष समझ — शमीकरण — यथार्थ सिद्धांत — उपलब्धि यथार्थ युग” से जुड़े शोध-पत्रों की क्रमिक श्रृंखला है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091961
संपादकीय स्थिति इन प्रारंभिक पत्रों को **दार्शनिक/सैद्धांतिक शोध-पत्र** के रूप में तैयार किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091962
जहाँ वास्तविक प्रतिभागी, प्रयोग, सांख्यिकीय परिणाम या स्वतंत्र सत्यापन उपलब्ध नहीं है, वहाँ कोई परिणाम गढ़ा नहीं गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091963
ऐसे स्थानों पर “प्रस्तावित अध्ययन”, “परिकल्पना” या “भविष्य के परीक्षण” स्पष्ट रूप से लिखे गए हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091964
शोध-पत्रों में समस्या, शोध-प्रश्न, पद्धति, विश्लेषण, सीमाएँ और संदर्भ रखे गए हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091965
वास्तविक जर्नल में भेजते समय उस जर्नल की author guidelines अलग से माननी होंगी।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091966
[निष्पक्ष समझ का वैचारिक मॉडल](./01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md) 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091967
[शमीकरण: एक संतुलित परीक्षण-पद्धति](./02-SHAMIKARAN-METHOD.md) 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091968
[हृदय और मस्तक दृष्टिकोण](./03-HEART-HEAD-MODEL.md) 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091969
[व्यक्तिगत अनुभव और सार्वभौमिक दावे](./04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md) 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091970
[दावा, प्रमाण और आत्म-संशोधन](./05-CLAIM-EVIDENCE-SELF-CORRECTION.md) 6.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091971
[स्वतंत्र समझ और प्राधिकार](./06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md) 7.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091972
[डिजिटल दार्शनिक ज्ञान-संग्रह](./07-DIGITAL-KNOWLEDGE-CORPUS.md) 8.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091973
[प्रकृति, मानव गरिमा और व्यवहारिक दर्शन](./08-NATURE-HUMAN-DIGNITY.md) 9.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091974
[संपूर्ण संतुष्टि: परिभाषा और परीक्षण](./09-COMPLETE-SATISFACTION-CONCEPT.md) 10.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091975
[यथार्थ युग: उभरती दार्शनिक रूपरेखा](./10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md) ## आगे की शोध दिशा - साहित्य समीक्षा और तुलनात्मक दर्शन - सर्वेक्षण-आधारित परीक्षण - अवधारणाओं के operational definitions - reproducible डेटा संग्रह - आलोचनात्मक समीक्षा - स्वतंत्र शोधकर्ताओं की प्रतिक्रिया ## 🔗 External/Legacy Research Repositories केंद्रीय शोध-संग्रह के साथ जुड़े repositories: 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091976
[Shirmani Research Paper]( 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091977
[Shirmani Research Institute]( [Integration architecture](../research-integration/SHIRMANI-REPOSITORIES.md)
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 091978
ज्ञानमीमांसीय निष्पक्षता: एक प्रस्तावित मॉडल **प्रकार:** Theoretical Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र ज्ञान-संबंधी निष्पक्षता को इस प्रश्न से जोड़ता है कि क्या समान प्रमाण पर समान मानदंड लागू किए जाते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091979
मॉडल व्यक्तिगत विश्वास, विरोधी विश्वास और तटस्थ दावे—तीनों पर एक समान परीक्षण की वकालत करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091980
शोध प्रश्न क्या “समान प्रमाण–समान कसौटी” को शोध व्यवहार के operational principle में बदला जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091981
प्रस्ताव दावे को समर्थन, विरोध, अनिश्चितता और संशोधन-सीमा के साथ दर्ज किया जाए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091982
संभावित परीक्षण Blind evaluation में यह जाँचा जा सकता है कि कथन के लेखक की पहचान हटाने पर मूल्यांकन बदलता है या नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091983
सीमाएँ यह प्रस्ताव है; empirical निष्कर्ष प्रस्तुत नहीं किए गए हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091984
निष्कर्ष निष्पक्षता को केवल भावना नहीं, रिकॉर्ड किए जा सकने वाले शोध व्यवहार के रूप में भी अध्ययन किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 091985
यथार्थ युग: एक उभरती दार्शनिक रूपरेखा **प्रकार:** Integrative Philosophical Research Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र “यथार्थ युग” को एक उभरती दार्शनिक रूपरेखा के रूप में व्यवस्थित करता है, जिसमें निष्पक्ष समझ, शमीकरण, हृदय–मस्तक संतुलन, स्वतंत्र परीक्षण और व्यवहारिक उत्तरदायित्व प्रमुख तत्व हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091986
पत्र इसे ऐतिहासिक या वैज्ञानिक रूप से स्थापित युग के रूप में सिद्ध करने का दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091987
शोध प्रश्न क्या इन अवधारणाओं को एक coherent philosophical framework में व्यवस्थित किया जा सकता है जिसे आलोचनात्मक परीक्षण के लिए प्रस्तुत किया जा सके?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091988
पद्धति अवधारणा-मानचित्रण, आंतरिक संगति का विश्लेषण, विरोधी प्रश्नों की पहचान और भविष्य के empirical परीक्षणों का प्रस्ताव।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091989
प्रमाण-संवेदनशीलता 8.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091990
प्रकृति और मानव गरिमा 9.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091991
डिजिटल ज्ञान-संग्रह ## सीमाएँ यह conceptual framework है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091992
इसकी मौलिकता, प्रभावशीलता और व्यापकता के लिए स्वतंत्र साहित्य समीक्षा तथा empirical research आवश्यक है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091993
भविष्य का शोध Systematic literature review, स्पष्ट hypotheses, preregistered studies, qualitative interviews, survey instruments और independent replication।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091994
निष्कर्ष “यथार्थ युग” को एक खुली शोध-परिकल्पना और दार्शनिक परियोजना के रूप में विकसित करना उसके दावों को परीक्षण और संशोधन के लिए उपलब्ध रखता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 091995
खुले डिजिटल ज्ञान और संस्करण नियंत्रण **प्रकार:** Digital Humanities / Knowledge Management **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र खुले डिजिटल ज्ञान-संग्रह में version history, स्रोत-स्पष्टता और संशोधन रिकॉर्ड के महत्व पर केंद्रित है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 091996
Git आधारित संरचना को दार्शनिक corpus के संपादकीय audit trail के रूप में प्रस्तावित किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 091997
मुख्य प्रश्न क्या संस्करण इतिहास पाठक को यह समझने में सहायता करता है कि किसी विचार में कब और क्यों परिवर्तन हुआ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 091998
प्रस्तावित संरचना हर प्रमुख दस्तावेज़ में संस्करण, तारीख, परिवर्तन-सार, स्रोत और संशोधन का कारण।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 091999
मूल्यांकन पाठक navigation, change traceability और source discovery को मापने वाले usability studies।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 092000
सीमा यह पत्र किसी विशिष्ट software workflow की superiority सिद्ध नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।
