# डिजिटल महाग्रंथ 057

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 056001
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056002
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056003
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056004
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056005
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056006
It includes all resources located in the `source/` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056007
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056008
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056009
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056010
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056011
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056012
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056013
`-p` or `--package`:** Launches a packaged application from a specified path.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056014
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056015
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056016
Any flags added after `--` will be passed through to Kit directly.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056017
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056018
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056019
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056020
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056021
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056022
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056023
Applications configurations (`.kit` files) are tested to ensure they can startup and shutdown without issue.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056024
However, the tests written within the extensions will dictate a majority of application functionality testing.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056025
Extension templates provided by the Kit App Template repository include sample tests which can be expanded upon to increase test coverage as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056026
Usage Always run a build before testing: **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ## Package Tool **Command:** `./repo.sh package` or `.\repo.bat package` ### Purpose This tool prepares your application for distribution or deployment by packaging it into a distributable format.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056027
Usage Always run a build before packaging to ensure the application is up-to-date: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` Additional launch options: - **`-n` or `--name`:** Specifies the package (or container image) name.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056028
Linux:** ```bash ./repo.sh package -n ``` **Windows:** ```powershell .\repo.bat package -n ``` - **`--thin`:** Creates a thin package that includes only custom extensions and configurations for required registry extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056029
Linux:** ```bash ./repo.sh package --thin ``` **Windows:** ```powershell .\repo.bat package --thin ``` :warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056030
The version is set within the `tools/VERSION.md` file.** ## Containerization Tool **Command:** `./repo.sh package_container` or `.\repo.bat package_container` ### Purpose The containerization tool provided by `repo_kit_tools` supports containerization of applications.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056031
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056032
How It Works The tool performs these steps: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056033
Creates a fat package** - Stages all dependencies into a temp directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056034
Trims unused extensions** - Removes disabled extensions to minimize image size 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056035
Splits into Docker layers** - Base layer (kit kernel + extscache) and app layer for faster rebuilds 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056036
Builds the container** - Uses a configurable base image (default: `nvcr.io/nvidia/omniverse/ov-base-ubuntu-22`) The container entrypoint supports runtime configuration via environment variables (`NVDA_KIT_ARGS`, `NVDA_KIT_NUCLEUS`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056037
Usage Always run a build before packaging to ensure the application is up-to-date: - **`package_container`:** Packages the application as a container image (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056038
When using the `package_container`, the user will be asked to select a `.kit` file to use within the entry point script for the container.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056039
This can also be specified without user interaction by passing it appropriate `.kit` file name via the `--app ${path_to_kit_file}` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056040
Linux:** ```bash ./repo.sh package_container ``` **Windows:** ```powershell .\repo.bat package_container ``` Additional command options: - **`--app`:** Specify the Kit app to containerize.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056041
One of defined in the config.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056042
Linux:** ```bash ./repo.sh package_container --app ${path_to_kit_file} ``` **Windows:** ```powershell .\repo.bat package_container --app ${path_to_kit_file} ``` - **`--image-tag`:** Optional image tag override to use for docker image.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056043
If includes ':', it will be used as is, e.g.: name:tag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056044
Linux:** ```bash ./repo.sh package_container --image-tag [container_image_name:container_image_tag] ``` **Windows:** ```powershell .\repo.bat package_container --image-tag [container_image_name:container_image_tag] ``` - **`-p` or `--from-package`:** Use package from 'kit-app-template/_build/packages/kit-app-template*.${config}.*' instead of a root folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056045
Linux:** ```bash ./repo.sh package_container -p ``` **Windows:** ```powershell .\repo.bat package_container -p ``` - **`-g` or `--generate`:** Generate default container template files into the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056046
Passed argument is the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056047
Linux:** ```bash ./repo.sh package_container -g ``` **Windows:** ```powershell .\repo.bat package_container -g ``` ## Additional Resources - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 056048
Configuring Kit App Template for DGXC Deployment This document covers Kit App Template specific configuration for deploying to NVIDIA DGX Cloud.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056049
For complete deployment instructions, see the [public DGXC documentation]( ## Streaming Layer Selection When creating your application with `./repo.sh template new`, select the appropriate streaming layer for DGXC: | Kit Version | Layer to Select | Generated File | |-------------|-----------------|----------------| | 108.x+ | `nvcf_streaming` | `{app_name}_nvcf.kit` | | 107.x | `ovc_streaming` | `{app_name}_ovc.kit` | | 106.x | `ovc_streaming` | `{app_name}_ovc.kit` | ### Selection Process 1.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056050
Run `./repo.sh template new` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056051
Select **Application** and your desired template 3.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056052
When prompted "Do you want to add application layers?", select **Yes** 4.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056053
`omni.cloud.open_stage`**: Provides Nucleus server connectivity for cloud deployments.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056054
[settings.exts."omni.kit.window.content_browser"] show_only_collections.6 = "" # Hides the "My Computer" connection from the content browser.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056055
``` ## Containerization After building (`./repo.sh build`), create a container: ```bash ./repo.sh package_container --image-tag myapp:v1.0 ``` When prompted, select the streaming `.kit` file (`*_ovc.kit` or `*_nvcf.kit`).
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056056
Next Steps For deployment to DGXC (container upload, NVCF function creation, portal registration), see: - [Containerization Guide]( - Building and packaging - [Deploying Kit Apps]( - NGC upload and NVCF deployment - [Troubleshooting]( - Common issues and FAQs ## Version-Specific Notes ### Kit 108.x+ (`main` branch) Select `nvcf_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056057
Streaming dependencies are automatically configured.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056058
Kit 107.x (`production/107.3` branch) Select `ovc_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056059
No manual edits required.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056060
Kit 106.x (`production/106.5` branch) The streaming layer may require manual edits.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056061
See the [public containerization guide]( for the "Replace Streaming Extension" section.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056062
Troubleshooting For deployment issues, log analysis, and common errors, see the [DGXC FAQs and Troubleshooting](
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 056063
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056064
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056065
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056066
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056067
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056068
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056069
Collaborating on large-scale design projects in real-time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056070
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056071
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056072
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056073
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056074
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056075
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056076
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056077
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056078
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056079
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056080
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056081
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056082
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056083
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056084
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056085
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056086
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056087
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056088
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056089
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056090
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056091
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056092
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056093
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056094
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056095
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056096
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056097
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056098
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056099
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056100
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056101
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056102
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056103
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056104
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056105
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056106
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056107
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056108
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056109
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056110
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056111
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056112
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056113
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056114
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056115
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056116
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056117
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056118
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056119
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056120
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056121
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056122
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056123
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056124
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056125
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056126
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056127
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056128
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056129
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056130
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056131
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056132
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056133
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056134
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056135
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056136
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056137
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056138
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056139
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056140
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056141
:warning: **Important**: These layers are not standalone application templates.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056142
They must be used in conjunction with a base application template.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056143
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056144
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056145
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056146
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056147
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056148
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056149
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056150
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056151
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056152
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056153
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056154
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056155
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056156
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056157
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056158
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056159
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056160
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056161
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056162
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056163
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056164
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056165
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056166
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056167
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056168
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056169
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056170
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056171
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056172
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056173
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056174
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056175
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056176
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056177
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056178
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056179
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056180
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056181
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056182
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056183
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056184
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056185
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056186
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056187
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056188
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056189
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056190
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056191
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056192
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056193
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056194
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056195
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056196
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056197
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056198
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056199
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056200
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056201
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056202
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056203
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056204
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056205
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056206
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056207
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056208
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056209
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056210
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056211
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056212
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056213
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056214
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056215
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056216
Start the Streaming Client Follow the [Quick Start instructions in the we
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056217
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056218
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056219
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056220
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056221
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056222
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056223
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056224
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056225
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056226
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056227
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056228
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056229
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056230
Subsequent extensions can be added to the .kit file manually.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056231
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056232
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056233
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056234
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056235
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056236
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056237
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056238
Setup Extension -> kit_service_setup* - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056239
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056240
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056241
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056242
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056243
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056244
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056245
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056246
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056247
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056248
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056249
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056250
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056251
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056252
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056253
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056254
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056255
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056256
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056257
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056258
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056259
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056260
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056261
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056262
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056263
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056264
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056265
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056266
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056267
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056268
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056269
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056270
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056271
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056272
The base application `.kit` file should be used for containerization.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056273
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056274
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056275
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056276
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056277
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056278
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056279
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056280
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056281
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056282
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056283
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056284
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056285
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056286
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056287
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056288
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056289
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056290
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056291
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056292
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056293
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056294
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056295
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056296
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056297
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056298
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056299
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056300
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056301
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056302
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056303
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056304
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056305
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056306
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056307
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056308
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056309
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056310
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056311
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056312
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056313
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056314
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056315
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056316
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056317
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056318
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056319
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056320
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056321
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056322
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056323
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056324
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056325
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056326
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056327
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056328
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056329
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056330
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056331
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056332
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056333
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056334
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056335
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056336
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056337
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056338
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056339
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056340
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056341
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056342
:warning: **Important:** Before proceeding with the cloning step, ensure that Git Large File Storage (Git LFS) is installed on your system.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056343
To verify this, run the following command in your terminal: ```bash git lfs --version ``` If the command returns a version number, Git LFS is installed correctly.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056344
If not, you will need to install Git LFS.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056345
You can download and install it from the official website [here]( #### Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056346
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056347
During Application configuration, you will be prompted for information about these extensions.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056348
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056349
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056350
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056351
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056352
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056353
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056354
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056355
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056356
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056357
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056358
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056359
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056360
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056361
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056362
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056363
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056364
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056365
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056366
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056367
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056368
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056369
The USD Viewer template includes sample assets for this purpose.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056370
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056371
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056372
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056373
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056374
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056375
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056376
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056377
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056378
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056379
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056380
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056381
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056382
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056383
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056384
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056385
The version is set within the `tools/VERSION.md` file.** #### Launching a Package Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056386
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056387
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056388
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056389
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056390
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056391
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056392
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056393
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056394
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056395
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056396
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056397
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056398
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056399
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056400
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056401
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056402
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056403
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056404
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056405
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056406
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056407
Service Setup Extension Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Service Setup Extension Template is designed to facilitate the configuration and setup of a headless service that leverages the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056408
Though it is possible in this case, setup extensions are not typically intended to be used as a generic extension but as a specific component of a particular application.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056409
Use Cases This setup extension is well suited for: - Developers building headless services that require Kit SDK functionalities.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056410
Key Features - Sample ServiceAPIRouter setup.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056411
Sample endpoint to demonstrate interaction patterns within service Kit SDK and OpenUSD.
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056412
Usage This extension is automatically created and configured when you generate a new service application using the [Service Application Template](../../apps/kit_service/README.md).
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056413
Additional Learning - [Omniverse Kit Service Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/service.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056414
Python UI Extension Template ## Overview The Python UI Extension Template offers a simple starting point for developers looking to build Python-based extensions with performant User Interfaces.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056415
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056416
Use Cases This template is ideal for developers looking to build: - UI based extensions that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056417
Key Features - A simple starter UI demonstrating how to build using the Omni UI framework.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056418
Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056419
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056420
Usage This section provides instructions for the setup and use of the Python UI Extension Template.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056421
Getting Started To get started with the Python UI Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056422
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056423
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056424
Select desired template with arrow keys ↑↓:**: Python UI Extension - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056425
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056426
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056427
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056428
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056429
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056430
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056431
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056432
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056433
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Omni UI Documentation]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/python_ui/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056434
USD Explorer Setup Extension Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer Setup Extension Template is specifically designed to configure the USD Explorer Template application.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056435
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Explorer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056436
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Explorer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056437
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056438
Key Features - Custom configurations tailored to the USD Explorer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056439
Usage This extension is automatically created and configured when you generate a new application based on the [USD Explorer Template Application](../../apps/usd_explorer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056440
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056441
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056442
Basic C++ Extension Template ## Overview The Basic C++ Extension Template is a starting point for developers looking to build C++ based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056443
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056444
Note for Windows C++ Developers** : This template requires that Visual Studio is installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056445
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056446
For additional C++ configuration information [see here](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056447
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056448
Performance sensitive extensions that require the performance benefits of C++.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056449
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056450
Integrating with existing C++ libraries or codebases.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056451
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056452
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056453
Usage This section provides instructions for the setup and use of the Basic C++ Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056454
Getting Started To get started with the Basic C++ Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056455
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056456
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056457
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056458
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056459
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056460
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056461
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056462
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056463
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056464
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056465
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056466
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056467
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056468
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056469
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056470
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056471
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056472
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056473
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056474
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056475
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056476
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056477
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056478
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056479
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056480
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056481
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056482
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056483
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056484
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056485
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056486
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056487
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056488
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056489
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056490
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056491
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056492
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056493
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056494
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056495
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056496
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056497
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056498
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056499
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056500
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056501
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056502
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056503
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056504
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056505
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056506
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056507
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056508
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056509
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056510
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056511
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056512
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056513
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056514
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056515
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056516
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056517
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056518
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056519
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056520
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056521
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056522
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056523
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056524
Integrating other C++ or Python libraries as needed.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056525
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056526
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056527
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056528
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056529
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056530
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056531
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056532
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056533
Managing the state for selecting objects within the scene.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056534
Performing actions without traditional in-app UI and menus.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056535
Key Features - Remote communication with the Kit application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056536
Scene loading capabilities.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056537
State management for object selection within the USD Viewer.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056538
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056539
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056540
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056541
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056542
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056543
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056544
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056545
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056546
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056547
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056548
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056549
Changelog The format is based on [Keep a Changelog]( ## [0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056550
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056551
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056552
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056553
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056554
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056555
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056556
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056557
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056558
Args: object: The bound object to register.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056559
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056560
Args: object: The bound object to deregister.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056561
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056562
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056563
Return: The bound object if it exists, an empty object otherwise.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056564
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056565
Return: The id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056566
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056567
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056568
Return: The bound object that was created.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056569
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056570
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056571
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056572
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056573
Args: value_to_multiply: The value to multiply by.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056574
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056575
Return: The toggled bool value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056576
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056577
Args: value_to_append: The value to append.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056578
Return: The new string value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056579
)", py::arg("value_to_append")) /**/; } ```
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 056580
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056581
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056582
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056583
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056584
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 056585
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056586
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056587
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056588
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056589
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056590
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056591
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056592
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056593
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056594
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056595
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056596
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056597
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056598
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056599
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056600
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056601
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056602
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056603
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056604
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056605
{{ extension_display_name }} [{{ extension_name }}] A simple python UI extension example.
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056606
Use it as a starting point for your extensions.
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056607
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - 2024-03-13 - Initial version based on kit service extension template
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 056608
{{ extension_display_name }} [{{ extension_name }}] This is an example of a simple Kit Service extension.
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056609
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056610
Version Bump Skill Automates kit-sdk version bumps by updating version files, creating a branch, committing, and optionally pushing a merge request.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056611
Read Current State Read these files to determine the current version: - `tools/VERSION.md` — contains the current version string (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056612
`110.0.0-stage.17`) - `tools/deps/kit-sdk.packman.xml` — contains the current kit-kernel packman version in the `version="..."` attribute Display the current version and kit-kernel version to the user.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056613
Ask Build Type Use `AskUserQuestion` to ask: **"Is this a stage or rc build?"** with two options: `stage` and `rc`.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056614
Show the current version from `tools/VERSION.md` for context.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056615
Compute New Version Parse the current version from `tools/VERSION.md` which follows the format `X.Y.Z- .
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056616
`110.0.0-stage.17`).
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056617
Apply these transition rules: | Current Version | User picks | New Version | |---|---|---| | `X.Y.Z-stage.N` | stage | `X.Y.Z-stage.(N+1)` | | `X.Y.Z-stage.N` | rc | `X.Y.Z-rc.1` | | `X.Y.Z-rc.N` | rc | `X.Y.Z-rc.(N+1)` | | `X.Y.Z-rc.N` | stage | `X.Y.(Z+1)-stage.1` | Display the computed new version to the user.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056618
Auto-Detect Latest kit-kernel Version Query the omnipackages API to find available kit-kernel versions: ```bash curl -s " %2B&remote=cloudfront" ``` Where ` ` is extracted from the current version (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056619
Parse the JSON response: - Extract the `name` field from each item in the `items` array - Strip the platform/config suffix using this regex to get the base version: `^([\d.]+\+\w+\.\d+\.[a-f0-9]+\.gl)\.` - Deduplicate the base versions (multiple platform variants share the same base) - They are already sorted by `modificationTime` (newest first) Read the current kit-kernel version from `tools/deps/kit-sdk.packman.xml` to identify which ones are newer.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056620
If the newest available version matches the current kit-kernel version (i.e.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056621
there are no newer versions), notify the user that the kit-kernel is already up to date and exit without making any file changes.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056622
Otherwise, present the top available versions newer than the current one (up to 4) to the user via `AskUserQuestion`, with the newest version marked as "(Recommended)".
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056623
The "Other" option is automatically available for the user to paste a custom version.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056624
Show the current kit-kernel version for reference in the question text.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056625
Edit 3 Files Using the new version string from step 3 and the kit-kernel version from step 4: 1.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056626
`tools/VERSION.md`**: Replace the entire file content with the new version string (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056627
`110.0.0-stage.18`).
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056628
Do NOT include a trailing newline.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056629
`tools/deps/kit-sdk.packman.xml`**: Replace the `version="..."` attribute value on the ` ` line.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056630
The new value should be the selected kit-kernel base version + `.${platform_target_abi}.${config}`.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056631
For example: ``` version="110.0.0+feature.275000.abcd1234.gl.${platform_target_abi}.${config}" ``` 3.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056632
`templates/omni.all.template.extensions.kit`**: Replace the `# Kit SDK Version:` comment line.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056633
The new value should use just the base version (without platform suffix).
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056634
For example: ``` # Kit SDK Version: 110.0.0+feature.275000.abcd1234.gl ``` ### 6.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056635
Confirm and Push Use `AskUserQuestion` with yes/no options to confirm.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056636
The question should summarize the changes: - Previous version → new version (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056637
`110.0.0-stage.17` → `110.0.0-stage.18`) - Previous kit-kernel → new kit-kernel version - Ask: **"Create branch, commit, and push merge request?"** If the user declines, revert the 3 files back to their original content (restore the values read in step 1) and stop.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056638
If the user accepts, perform these substeps: **6a.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056639
Create Branch** Before creating the new branch, capture the current branch name to use as the MR target: ```bash git rev-parse --abbrev-ref HEAD ``` Derive the git username by running `git config user.email` and extracting the part before `@`.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056640
Create and switch to a new branch: ```bash git checkout -b / ``` For example: `gamato/110.0.0-stage.18` **6b.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056641
Commit** Stage and commit exactly the 3 modified files: ```bash git add tools/VERSION.md tools/deps/kit-sdk.packman.xml templates/omni.all.template.extensions.kit git commit -m " " ``` The commit message is just the version string (e.g.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056642
`110.0.0-stage.18`), matching the existing convention.
स्रोत: kit-app-template/.claude/skills/version_bump/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056643
Runs a set of commands using the runners shell - name: Run a multi-line script run: | echo Add other actions to build, echo test, and deploy your project.
स्रोत: omniverse-marketplace/.github/workflows/blank.yml · स्वतंत्र परीक्षण अपेक्षित।

## 056644
name: Deploy GitHub Pages on: push: branches: - main jobs: deploy: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Deploy to GitHub Pages uses: peaceiris/actions-gh-pages@v3 with: github_token: ${{ secrets.GITHUB_TOKEN }} publish_dir: ./
स्रोत: omniverse-marketplace/.github/workflows/pages.yml · स्वतंत्र परीक्षण अपेक्षित।

## 056645
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: shiromani-rampal-saini/public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 056646
Sacred Audio शिरोमणि अंनत असीम इश्क़ की क्षमता यह ध्वनि केवल श्रवण नहीं, चेतना की अनुभूति है।
स्रोत: shiromani-rampal-saini/public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 056647
▶ अंनत असीम इश्क़ – दिव्य ध्वनि Track 1 Track 2 Track 3
स्रोत: shiromani-rampal-saini/public/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 056648
Runs a set of commands using the runners shell - name: Run a multi-line script run: | echo Add other actions to build, echo test, and deploy your project.
स्रोत: Omniverse-/.github/workflows/blank.yml · स्वतंत्र परीक्षण अपेक्षित।

## 056649
🔗 Shirmani Research Repositories — Central Integration यह फ़ाइल दो मौजूदा repositories को **Nishpaksh Samaj Omniverse Truth** के केंद्रीय ज्ञान-संग्रह से जोड़ती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056650
Shirmani Research Paper Repository: मुख्य विषय: - Time Deconstruction Theory - Neurobiology of Self - Ego Dissolution Framework - Heart-Mind Balance Model - research presentation / publication material केंद्रीय परियोजना में इसकी भूमिका: **Research Papers / Research Archive** ## 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056651
इससे पुराने Git इतिहास, स्वतंत्र GitHub Pages और मौजूदा सामग्री सुरक्षित रहती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056652
आगे आवश्यकता होने पर चयनित सामग्री को केंद्रीय repository में **स्रोत-संदर्भ और मूल repository attribution के साथ** व्यवस्थित रूप से पुनर्संयोजित किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056653
केंद्रीय repository = canonical knowledge hub 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056654
Research Paper repository = research archive 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056655
Research Institute repository = institute/archive/media layer 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056656
सभी repositories में परस्पर स्पष्ट navigation 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056657
duplicate सामग्री को धीरे-धीरे कम करना 6.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056658
प्रत्येक बड़े दावे के लिए स्रोत/स्थिति/अनिश्चितता स्पष्ट रखना --- **Canonical Hub:** *Integration document — continuously maintained.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research-integration/SHIRMANI-REPOSITORIES.md · स्वतंत्र परीक्षण अपेक्षित।

## 056659
Research Paper 17 — Practical Self-Observation Framework ## Status Conceptual/methodological proposal.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056660
Abstract यह paper “खुद का निरीक्षण” को एक structured reflective practice के रूप में स्पष्ट करने का प्रयास करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056661
इसे किसी विशेष मानसिक या चिकित्सीय परिणाम की गारंटी के रूप में प्रस्तुत नहीं किया जाता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056662
Framework **घटना → तत्काल अनुभव → विचार/व्याख्या → प्रतिक्रिया → परिणाम → पुनरावलोकन** ## Safeguards - अनुभव और तथ्य अलग रखें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056663
स्मृति को पूर्ण रिकॉर्ड न मानें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056664
बाहरी प्रमाण उपलब्ध हो तो जाँचें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056665
असहमति को त्रुटि का प्रमाण न मानें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056666
नकारात्मक परिणामों को छिपाएँ नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056667
Proposed study एक स्पष्ट दैनिक निरीक्षण प्रोटोकॉल बनाया जा सकता है, जिसकी adherence और self-reported outcomes को पूर्वनिर्धारित तरीके से दर्ज किया जाए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056668
यदि भविष्य में अध्ययन किया जाए तो protocol, sample, analysis और limitations सार्वजनिक किए जाएँ।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056669
Conclusion खुद का निरीक्षण तभी अधिक उपयोगी शोध-पद्धति बन सकता है जब वह स्पष्ट, दोहराने योग्य और आत्म-संशोधन के लिए खुला हो।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/17-PRACTICAL-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056670
शमीकरण: एक संतुलित परीक्षण-पद्धति **प्रकार:** Theoretical / Methodological Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश “शमीकरण” को अनुभव, विचार, प्रमाण और वैकल्पिक व्याख्याओं के बीच संतुलित परीक्षण की प्रस्तावित पद्धति के रूप में व्यवस्थित किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 056671
उद्देश्य पूर्वनिर्धारित निष्कर्ष को सिद्ध करना नहीं, बल्कि निष्कर्ष बनने की प्रक्रिया को पारदर्शी बनाना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 056672
शोध प्रश्न क्या अनुभव → प्रश्न → प्रमाण → वैकल्पिक व्याख्या → संशोधन का चक्र उपयोगी सामान्य पद्धति बन सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 056673
पद्धति अवधारणा-विश्लेषण, उदाहरण-निर्माण और भविष्य के empirical परीक्षण के लिए operational definitions।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 056674
प्रस्तावित प्रक्रिया **अनुभव → दावा → प्रश्न → प्रमाण → प्रतिवाद → वैकल्पिक व्याख्या → निष्कर्ष → पुनर्परीक्षण** ## सीमाएँ “शमीकरण” इस परियोजना में प्रस्तावित शब्द और मॉडल है; इसकी स्वतंत्र अकादमिक मान्यता या प्रभावशीलता इस पत्र से स्थापित नहीं होती।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 056675
निष्कर्ष पद्धति की सबसे महत्वपूर्ण कसौटी उसका स्वयं परीक्षण योग्य होना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/02-SHAMIKARAN-METHOD.md · स्वतंत्र परीक्षण अपेक्षित।

## 056676
Research Paper 16 — Nature-Compatible Philosophy ## Status Conceptual/philosophical paper.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056677
No empirical results are claimed.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056678
Abstract यह paper निष्पक्ष समझ के संदर्भ में मनुष्य-प्रकृति संबंध के लिए एक परीक्षणयोग्य वैचारिक ढाँचा प्रस्तावित करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056679
केंद्रीय प्रश्न है: क्या किसी जीवन-दृष्टि को उसके घोषित मूल्यों के साथ-साथ उसके वास्तविक पर्यावरणीय प्रभावों से भी परखा जाना चाहिए?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056680
Core propositions 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056681
मूल्य-घोषणा और वास्तविक व्यवहार अलग चीजें हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056682
प्रकृति-सम्मत दावा प्रभाव के प्रमाण से मजबूत या कमजोर हो सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056683
व्यक्तिगत अनुभव सार्वभौमिक वैज्ञानिक निष्कर्ष के समान नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056684
वैकल्पिक व्याख्याएँ हमेशा दर्ज की जानी चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056685
Proposed research questions - कौन-से दैनिक व्यवहार पर्यावरणीय प्रभाव को सबसे अधिक बदलते हैं?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056686
क्या आत्म-निरीक्षण आधारित अभ्यास व्यवहार में मापने योग्य परिवर्तन ला सकते हैं?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056687
किन परिस्थितियों में व्यक्तिगत संतुष्टि और पर्यावरणीय जिम्मेदारी में तनाव पैदा होता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056688
Method proposal पूर्व-पंजीकृत परिकल्पनाएँ, स्पष्ट outcome measures, comparison groups जहाँ उपयुक्त हों, और reproducible analysis।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056689
वास्तविक अध्ययन होने तक कोई परिणाम नहीं माना जाएगा।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056690
Conclusion दार्शनिक प्रस्ताव को व्यवहारिक परिणामों से जोड़ने के लिए प्रमाण और आत्म-संशोधन दोनों आवश्यक हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/16-NATURE-COMPATIBLE-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056691
निष्पक्ष समझ का वैचारिक मॉडल **प्रकार:** Conceptual / Philosophical Research Paper **लेखक:** शिरोमणि रामपॉल सैनी **स्थिति:** प्रारंभिक वैचारिक मसौदा ## सारांश यह शोध-पत्र “निष्पक्ष समझ” को ऐसी वैचारिक प्रक्रिया के रूप में प्रस्तावित करता है जिसमें व्यक्ति अपने अनुभव, विश्वास और निष्कर्षों पर समान परीक्षण-कसौटी लागू करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056692
यह किसी सार्वभौमिक सत्य की स्थापना का दावा नहीं करता; उद्देश्य एक परीक्षण योग्य दार्शनिक मॉडल प्रस्तुत करना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056693
मुख्य शब्द:** निष्पक्ष समझ, आत्म-परीक्षण, प्रमाण, तर्क, आत्म-संशोधन ## 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056694
शोध समस्या व्यक्तिगत विश्वास अनुभव, संस्कृति, प्राधिकार और पूर्व धारणाओं से प्रभावित हो सकते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056695
प्रश्न यह है कि क्या व्यक्ति अपने विचारों पर वही कसौटी लागू करता है जो दूसरों के विचारों पर करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056696
शोध प्रश्न क्या “समान कसौटी” को स्पष्ट वैचारिक मॉडल में बदला जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056697
वैकल्पिक व्याख्या देखना 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056698
नए प्रमाण पर निष्कर्ष संशोधित करना ## 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056699
पद्धति यह दार्शनिक अवधारणा-विश्लेषण है; empirical study नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056700
भविष्य का परीक्षण प्रतिभागियों से अपने और दूसरे व्यक्ति के समान प्रकार के दावों का मूल्यांकन कराया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056701
निष्पक्षता का operational measure पहले से तय करना होगा।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056702
सीमाएँ वर्तमान पत्र वास्तविक प्रतिभागियों या सांख्यिकीय परिणामों का दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056703
निष्कर्ष निष्पक्ष समझ को अंतिम उत्तर के बजाय आत्म-संशोधन की पद्धति के रूप में देखना इसे परीक्षण योग्य बनाता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056704
Research Paper 18 — Language, Art, Culture and Public Knowledge ## Abstract This conceptual paper examines how language, artistic expression, cultural inheritance, and digital publication interact with philosophical claims.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056705
The paper proposes a distinction between experience, interpretation, hypothesis, and externally verifiable fact.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056706
Status This is a **conceptual and methodological paper**.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056707
It reports no completed experiment, participant sample, statistical result, or causal finding.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056708
Core model **Experience → Expression → Interpretation → Claim → Evidence → Public dialogue → Revision** The model is intended to reduce a common category error: treating a personally meaningful experience as if every interpretation derived from it were automatically an externally established fact.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056709
Research questions 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056710
Does clearer separation of experience and factual claims improve reader comprehension?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056711
Does plain-language presentation improve accessibility without reducing conceptual precision?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056712
Can structured counterargument sections improve readers' ability to distinguish claims from evidence?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056713
How do poetry, music, and visual art affect reflection without being mistaken for empirical evidence?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056714
Does version-controlled publication improve correction and traceability of public philosophical material?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056715
Proposed study design A future study could preregister: - participant eligibility, - comprehension measures, - comparison texts, - randomization procedure where appropriate, - primary and secondary outcomes, - exclusion criteria, - analysis plan, - adverse or null-result reporting.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056716
No outcome should be claimed until data are actually collected and analyzed.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056717
Ethical principles - Do not manufacture evidence.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056718
Do not present artistic symbolism as scientific proof.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056719
Do not conceal meaningful counterarguments.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056720
Preserve uncertainty where evidence is incomplete.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056721
Correct public errors visibly.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056722
Respect readers' freedom to disagree.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056723
Practical publication standard Each major public claim should, where feasible, carry one of these labels: **[EXPERIENCE] [PHILOSOPHICAL CLAIM] [HYPOTHESIS] [FACT + SOURCE] [OPEN QUESTION]** This labeling system can be implemented across the digital corpus.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056724
Conclusion A philosophy can remain deep while becoming more testable.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056725
A poem can remain poetic while clearly being presented as poetry.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056726
A personal experience can remain meaningful without being promoted beyond what its evidence supports.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056727
The proposed framework therefore treats clarity, openness to criticism, and self-correction as integral parts of public philosophical practice.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/18-LANGUAGE-ART-CULTURE-AND-PUBLIC-KNOWLEDGE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056728
स्वतंत्र समझ और प्राधिकार **प्रकार:** Conceptual Social Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र जाँचता है कि व्यक्ति किसी गुरु, संस्था, शिक्षक या अन्य प्राधिकार की बात को किस प्रकार स्वतंत्र रूप से परख सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056729
लक्ष्य प्राधिकार को स्वतः अस्वीकार या स्वीकार करना नहीं, बल्कि प्रमाण और तर्क को स्वतंत्र कसौटी के रूप में रखना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056730
शोध प्रश्न क्या प्राधिकार और स्वतंत्र परीक्षण के बीच ऐसा मॉडल बनाया जा सकता है जिसमें दोनों के कार्य स्पष्ट हों?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056731
प्रस्ताव प्राधिकार सूचना दे सकता है; स्वतंत्र परीक्षण दावे की जाँच करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056732
सीमा यह पत्र किसी विशिष्ट व्यक्ति या संस्था के बारे में तथ्यात्मक आरोप प्रस्तुत नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056733
व्यक्तिगत अनुभव और सार्वभौमिक दावे **प्रकार:** Philosophy of Knowledge **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश व्यक्तिगत अनुभव किसी व्यक्ति के लिए वास्तविक अनुभव हो सकता है, लेकिन उससे सार्वभौमिक निष्कर्ष निकालने के लिए अतिरिक्त तर्क और स्वतंत्र प्रमाण आवश्यक होते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056734
अनुभव — “मुझे ऐसा महसूस हुआ” 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056735
व्याख्या — “इसका अर्थ यह है” 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056736
सार्वभौमिक दावा — “यह सभी के लिए सत्य है” तीसरे स्तर के लिए स्वतंत्र जाँच आवश्यक है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056737
निष्कर्ष अनुभव का सम्मान और उसके दावे की स्वतंत्र जाँच एक-दूसरे के विरोधी नहीं हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056738
हृदय और मस्तक दृष्टिकोण: एक दार्शनिक मॉडल **प्रकार:** Conceptual Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र “हृदय दृष्टिकोण” और “मस्तक दृष्टिकोण” को क्रमशः भावात्मक प्रत्यक्षता तथा विचारात्मक/विश्लेषणात्मक प्रक्रिया के रूपकों के रूप में स्पष्ट करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056739
यह जैविक हृदय के बारे में वैज्ञानिक दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056740
मुख्य प्रश्न क्या भावना और तर्क को प्रतिस्पर्धी नहीं बल्कि पूरक प्रक्रियाओं के रूप में मॉडल किया जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056741
मॉडल हृदय = एहसास और मूल्य-संवेदना का रूपक।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056742
मस्तक = भाषा, स्मृति, तुलना, योजना और तर्क का रूपक।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056743
प्रस्ताव पहले अनुभव को पहचाना जाए, फिर संज्ञानात्मक विश्लेषण से विकल्पों और परिणामों की जाँच की जाए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056744
परीक्षण निर्णय-लेने के कार्यों में भावनात्मक जागरूकता और तर्कात्मक जाँच के संयुक्त प्रभाव का अध्ययन किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056745
सीमा यह पत्र किसी प्रतिशत-संतुलन को वैज्ञानिक रूप से स्थापित नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/03-HEART-HEAD-MODEL.md · स्वतंत्र परीक्षण अपेक्षित।

## 056746
दावा, प्रमाण और आत्म-संशोधन **प्रकार:** Methodological Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र शोध-दैनंदिनी मॉडल प्रस्तावित करता है: दावा, प्रमाण, अनिश्चितता, विरोधी प्रमाण और अगला परीक्षण।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056747
उद्देश्य यह देखना है कि कोई विचार नए प्रमाण पर कितनी पारदर्शिता से संशोधित होता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056748
प्रस्तावित प्रोटोकॉल हर प्रमुख दावे के साथ पाँच फ़ील्ड रखें: दावा, समर्थन, विरोधी प्रमाण, अनिश्चितता, अगला परीक्षण।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056749
संभावित डेटा संस्करण इतिहास, शोध-दैनंदिनी और स्वतंत्र समीक्षकों की टिप्पणियाँ।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056750
सीमा प्रारंभिक प्रस्ताव में वास्तविक longitudinal dataset नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/05-CLAIM-EVIDENCE-SELF-CORRECTION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056751
“संपूर्ण संतुष्टि” की अवधारणा: परिभाषा और परीक्षण **प्रकार:** Conceptual / Measurement Proposal **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश “संपूर्ण संतुष्टि” को इस परियोजना में निरंतर संतुष्टि के व्यक्तिगत अनुभव के रूप में प्रस्तावित किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 056752
यह पत्र अवधारणा को स्पष्ट operational definition में बदलने की आवश्यकता पर केंद्रित है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 056753
शोध प्रश्न क्या “संपूर्ण संतुष्टि” को स्पष्ट, दोहराने योग्य और नैतिक self-report तथा behavioral measures में operationalize किया जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 056754
प्रस्तावित आयाम - वर्तमान क्षण में संतुष्टि - आंतरिक संघर्ष की अनुभूति - भविष्य-निर्भरता की अनुभूति - निर्णय के बाद स्थिरता - प्रतिकूल परिस्थिति में संतुलन ## सीमा वर्तमान पत्र में कोई validated instrument या empirical prevalence estimate नहीं दिया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/09-COMPLETE-SATISFACTION-CONCEPT.md · स्वतंत्र परीक्षण अपेक्षित।

## 056755
डिजिटल दार्शनिक ज्ञान-संग्रह का मॉडल **प्रकार:** Digital Humanities / Knowledge Architecture **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र 100 ग्रंथों और दीर्घकालीन 100,000-पृष्ठ corpus को डिजिटल रूप में व्यवस्थित करने का मॉडल प्रस्तुत करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056756
लक्ष्य सामग्री की मात्रा के साथ खोज, संस्करण नियंत्रण, स्रोत-स्पष्टता और पुनरावृत्ति नियंत्रण बनाए रखना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056757
प्रस्तावित वास्तुकला - विषय-आधारित ग्रंथ - अध्याय और उप-अध्याय - शब्दावली - स्रोत-सूची - दावे और प्रमाण - संशोधन इतिहास - स्थायी लिंक - शोध-पत्र संग्रह - multilingual विस्तार ## मूल्यांकन भविष्य में navigation success, search accuracy, broken links और duplicate-content ratio जैसे संकेतकों से प्रणाली का मूल्यांकन किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056758
सीमा यह knowledge-architecture proposal है; वर्तमान पत्र usability study के परिणाम का दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/07-DIGITAL-KNOWLEDGE-CORPUS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056759
प्रकृति, मानव गरिमा और व्यवहारिक दर्शन **प्रकार:** Applied Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र प्रस्तावित करता है कि किसी दार्शनिक ढाँचे का व्यवहारिक मूल्य उसके वास्तविक जीवन में प्रकृति, मानव गरिमा और स्वतंत्रता के प्रति प्रभाव से भी जाँचा जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056760
शोध प्रश्न क्या ecological responsibility और human dignity को दार्शनिक सिद्धांतों के मूल्यांकन में operational criteria बनाया जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056761
प्रकृति पर प्रभाव 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056762
व्यक्ति की स्वायत्तता 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056763
संसाधनों और शक्ति में पारदर्शिता ## सीमा इस पत्र में कोई causal effect स्थापित नहीं किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/08-NATURE-HUMAN-DIGNITY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056764
आत्म-परीक्षण और मेटाकॉग्निशन **प्रकार:** Conceptual Research Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र “खुद का निरीक्षण” को metacognitive प्रक्रिया के साथ संवाद में रखता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056765
लक्ष्य यह समझना है कि व्यक्ति अपने विचार, विश्वास और निर्णय-प्रक्रिया को कैसे देख सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056766
मुख्य प्रश्न क्या नियमित self-observation से व्यक्ति अपने निष्कर्षों की अनिश्चितता और पूर्वधारणाओं को अधिक स्पष्ट रूप से पहचान सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056767
प्रस्तावित मॉडल अनुभव → विचार की पहचान → पूर्वधारणा → भावनात्मक प्रभाव → प्रमाण → वैकल्पिक विचार → संशोधित निष्कर्ष।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056768
संभावित अध्ययन दैनिक reflective journal और निर्णय-कार्य के longitudinal अध्ययन किए जा सकते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056769
सीमाएँ यह पत्र किसी विशेष intervention की प्रभावशीलता सिद्ध नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056770
निष्कर्ष आत्म-परीक्षण को व्यवस्थित रिकॉर्ड में बदलना भविष्य के empirical research का आधार बन सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/12-METACOGNITION-AND-SELF-OBSERVATION.md · स्वतंत्र परीक्षण अपेक्षित।

## 056771
शोध-पत्र संग्रह यह संग्रह “निष्पक्ष समझ — शमीकरण — यथार्थ सिद्धांत — उपलब्धि यथार्थ युग” से जुड़े शोध-पत्रों की क्रमिक श्रृंखला है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056772
संपादकीय स्थिति इन प्रारंभिक पत्रों को **दार्शनिक/सैद्धांतिक शोध-पत्र** के रूप में तैयार किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056773
जहाँ वास्तविक प्रतिभागी, प्रयोग, सांख्यिकीय परिणाम या स्वतंत्र सत्यापन उपलब्ध नहीं है, वहाँ कोई परिणाम गढ़ा नहीं गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056774
ऐसे स्थानों पर “प्रस्तावित अध्ययन”, “परिकल्पना” या “भविष्य के परीक्षण” स्पष्ट रूप से लिखे गए हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056775
शोध-पत्रों में समस्या, शोध-प्रश्न, पद्धति, विश्लेषण, सीमाएँ और संदर्भ रखे गए हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056776
वास्तविक जर्नल में भेजते समय उस जर्नल की author guidelines अलग से माननी होंगी।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056777
[निष्पक्ष समझ का वैचारिक मॉडल](./01-NISHPAKSH-SAMJH-CONCEPTUAL-MODEL.md) 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056778
[शमीकरण: एक संतुलित परीक्षण-पद्धति](./02-SHAMIKARAN-METHOD.md) 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056779
[हृदय और मस्तक दृष्टिकोण](./03-HEART-HEAD-MODEL.md) 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056780
[व्यक्तिगत अनुभव और सार्वभौमिक दावे](./04-EXPERIENCE-AND-UNIVERSAL-CLAIMS.md) 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056781
[दावा, प्रमाण और आत्म-संशोधन](./05-CLAIM-EVIDENCE-SELF-CORRECTION.md) 6.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056782
[स्वतंत्र समझ और प्राधिकार](./06-INDEPENDENT-UNDERSTANDING-AUTHORITY.md) 7.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056783
[डिजिटल दार्शनिक ज्ञान-संग्रह](./07-DIGITAL-KNOWLEDGE-CORPUS.md) 8.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056784
[प्रकृति, मानव गरिमा और व्यवहारिक दर्शन](./08-NATURE-HUMAN-DIGNITY.md) 9.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056785
[संपूर्ण संतुष्टि: परिभाषा और परीक्षण](./09-COMPLETE-SATISFACTION-CONCEPT.md) 10.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056786
[यथार्थ युग: उभरती दार्शनिक रूपरेखा](./10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md) ## आगे की शोध दिशा - साहित्य समीक्षा और तुलनात्मक दर्शन - सर्वेक्षण-आधारित परीक्षण - अवधारणाओं के operational definitions - reproducible डेटा संग्रह - आलोचनात्मक समीक्षा - स्वतंत्र शोधकर्ताओं की प्रतिक्रिया ## 🔗 External/Legacy Research Repositories केंद्रीय शोध-संग्रह के साथ जुड़े repositories: 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056787
[Shirmani Research Paper]( 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056788
[Shirmani Research Institute]( [Integration architecture](../research-integration/SHIRMANI-REPOSITORIES.md)
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 056789
ज्ञानमीमांसीय निष्पक्षता: एक प्रस्तावित मॉडल **प्रकार:** Theoretical Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र ज्ञान-संबंधी निष्पक्षता को इस प्रश्न से जोड़ता है कि क्या समान प्रमाण पर समान मानदंड लागू किए जाते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056790
मॉडल व्यक्तिगत विश्वास, विरोधी विश्वास और तटस्थ दावे—तीनों पर एक समान परीक्षण की वकालत करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056791
शोध प्रश्न क्या “समान प्रमाण–समान कसौटी” को शोध व्यवहार के operational principle में बदला जा सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056792
प्रस्ताव दावे को समर्थन, विरोध, अनिश्चितता और संशोधन-सीमा के साथ दर्ज किया जाए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056793
संभावित परीक्षण Blind evaluation में यह जाँचा जा सकता है कि कथन के लेखक की पहचान हटाने पर मूल्यांकन बदलता है या नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056794
सीमाएँ यह प्रस्ताव है; empirical निष्कर्ष प्रस्तुत नहीं किए गए हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056795
निष्कर्ष निष्पक्षता को केवल भावना नहीं, रिकॉर्ड किए जा सकने वाले शोध व्यवहार के रूप में भी अध्ययन किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/11-EPISTEMIC-FAIRNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056796
यथार्थ युग: एक उभरती दार्शनिक रूपरेखा **प्रकार:** Integrative Philosophical Research Paper **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र “यथार्थ युग” को एक उभरती दार्शनिक रूपरेखा के रूप में व्यवस्थित करता है, जिसमें निष्पक्ष समझ, शमीकरण, हृदय–मस्तक संतुलन, स्वतंत्र परीक्षण और व्यवहारिक उत्तरदायित्व प्रमुख तत्व हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056797
पत्र इसे ऐतिहासिक या वैज्ञानिक रूप से स्थापित युग के रूप में सिद्ध करने का दावा नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056798
शोध प्रश्न क्या इन अवधारणाओं को एक coherent philosophical framework में व्यवस्थित किया जा सकता है जिसे आलोचनात्मक परीक्षण के लिए प्रस्तुत किया जा सके?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056799
पद्धति अवधारणा-मानचित्रण, आंतरिक संगति का विश्लेषण, विरोधी प्रश्नों की पहचान और भविष्य के empirical परीक्षणों का प्रस्ताव।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056800
प्रमाण-संवेदनशीलता 8.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056801
प्रकृति और मानव गरिमा 9.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056802
डिजिटल ज्ञान-संग्रह ## सीमाएँ यह conceptual framework है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056803
इसकी मौलिकता, प्रभावशीलता और व्यापकता के लिए स्वतंत्र साहित्य समीक्षा तथा empirical research आवश्यक है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056804
भविष्य का शोध Systematic literature review, स्पष्ट hypotheses, preregistered studies, qualitative interviews, survey instruments और independent replication।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056805
निष्कर्ष “यथार्थ युग” को एक खुली शोध-परिकल्पना और दार्शनिक परियोजना के रूप में विकसित करना उसके दावों को परीक्षण और संशोधन के लिए उपलब्ध रखता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/10-YATHARTH-YUG-PHILOSOPHICAL-FRAMEWORK.md · स्वतंत्र परीक्षण अपेक्षित।

## 056806
खुले डिजिटल ज्ञान और संस्करण नियंत्रण **प्रकार:** Digital Humanities / Knowledge Management **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश यह पत्र खुले डिजिटल ज्ञान-संग्रह में version history, स्रोत-स्पष्टता और संशोधन रिकॉर्ड के महत्व पर केंद्रित है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 056807
Git आधारित संरचना को दार्शनिक corpus के संपादकीय audit trail के रूप में प्रस्तावित किया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 056808
मुख्य प्रश्न क्या संस्करण इतिहास पाठक को यह समझने में सहायता करता है कि किसी विचार में कब और क्यों परिवर्तन हुआ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 056809
प्रस्तावित संरचना हर प्रमुख दस्तावेज़ में संस्करण, तारीख, परिवर्तन-सार, स्रोत और संशोधन का कारण।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 056810
मूल्यांकन पाठक navigation, change traceability और source discovery को मापने वाले usability studies।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 056811
सीमा यह पत्र किसी विशिष्ट software workflow की superiority सिद्ध नहीं करता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 056812
निष्कर्ष खुला संस्करण इतिहास विचारों को स्थिर मूर्ति के बजाय विकसित होते दस्तावेज़ के रूप में दिखा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/14-OPEN-KNOWLEDGE-AND-VERSIONING.md · स्वतंत्र परीक्षण अपेक्षित।

## 056813
दर्शन से व्यवहार तक: यथार्थ सिद्धांत का व्यवहारिक मॉडल **प्रकार:** Applied Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश दार्शनिक अवधारणा का मूल्य केवल भाषा में नहीं, उसके व्यवहारिक उपयोग में भी देखा जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056814
यह पत्र विचार से दैनिक निर्णय तक एक संभावित translation framework प्रस्तुत करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056815
अनुभव और तथ्य अलग करना 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056816
हितधारकों की पहचान 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056817
विकल्प और परिणाम देखना 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056818
निर्णय के बाद पुनर्मूल्यांकन ## संभावित उपयोग व्यक्तिगत निर्णय, शिक्षा, सामुदायिक संवाद और पर्यावरणीय निर्णय।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056819
मूल्यांकन पूर्व-निर्धारित outcome measures, participant feedback और independent review।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056820
सीमा किसी वास्तविक intervention का परिणाम यहाँ प्रस्तुत नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056821
निष्कर्ष दार्शनिक ढाँचे की उपयोगिता को व्यवहारिक प्रक्रियाओं में operationalize किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/13-PHILOSOPHY-TO-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056822
सार्वजनिक दर्शन की नैतिकता: पारदर्शिता, असहमति और जिम्मेदारी **प्रकार:** Ethics / Public Philosophy **लेखक:** शिरोमणि रामपॉल सैनी ## सारांश सार्वजनिक दर्शन में लेखक का प्रभाव, पाठक की स्वायत्तता और दावों की पारदर्शिता महत्वपूर्ण हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056823
यह पत्र ऐसी संपादकीय नैतिकता प्रस्तावित करता है जिसमें पाठक को विचार और प्रमाण के बीच अंतर स्पष्ट दिखाई दे।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056824
सिद्धांत - अनुभव को अनुभव की तरह लिखना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056825
परिकल्पना को परिकल्पना की तरह लिखना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056826
प्रमाण न होने पर परिणाम न गढ़ना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056827
असहमति को स्थान देना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056828
आर्थिक हितों को जहाँ प्रासंगिक हो स्पष्ट करना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056829
पाठक को स्वतंत्र निर्णय का अवसर देना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056830
शोध दिशा Public philosophy projects में disclosure practices और reader trust का तुलनात्मक अध्ययन।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056831
सीमाएँ यह normative proposal है, empirical verdict नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056832
निष्कर्ष विश्वसनीय सार्वजनिक दर्शन केवल प्रभावशाली भाषा से नहीं, बल्कि पारदर्शी आचरण से भी बनता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/research/15-ETHICS-OF-PUBLIC-PHILOSOPHY.md · स्वतंत्र परीक्षण अपेक्षित।

## 056833
ग्रंथ 04 — समाज, स्वतंत्र समझ और मानवीय गरिमा ## प्रस्तावना व्यक्ति अकेला नहीं जीता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056834
परिवार, शिक्षा, भाषा, संस्था, परंपरा, कानून और अर्थव्यवस्था उसके निर्णयों को प्रभावित करते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056835
इसलिए स्वतंत्र समझ केवल भीतर का विषय नहीं, सामाजिक विषय भी है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056836
व्यक्ति और समाज व्यक्ति समाज से सीखता है और समाज व्यक्तियों से बदलता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056837
दोनों के बीच संबंध को केवल संघर्ष या केवल समर्पण के रूप में देखना अधूरा है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056838
परंपरा परंपरा अनुभव का संचित रूप हो सकती है, लेकिन पुरानी होने मात्र से हर बात सही नहीं हो जाती।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056839
उपयोगी परंपरा को समझकर अपनाया जा सकता है; हानिकारक प्रथा को प्रश्न किया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056840
प्राधिकार पद, वेश, संस्था, प्रतिष्ठा या भीड़ किसी कथन को स्वतः सत्य नहीं बनाते।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056841
प्राधिकार उपयोगी हो सकता है, पर सत्यापन की जगह नहीं लेता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056842
भय भय व्यक्ति को सुरक्षा की ओर ले जा सकता है, लेकिन भय के आधार पर विचार बंद कर देना स्वतंत्र समझ को सीमित करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056843
आर्थिक स्वतंत्रता दर्शन तभी व्यवहार में टिकता है जब व्यक्ति भोजन, आवास, शिक्षा, स्वास्थ्य, कौशल और सम्मानजनक आजीविका के वास्तविक प्रश्नों को भी संबोधित करे।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056844
रोज़ी-रोटी और विचार एक सार्वजनिक दार्शनिक परियोजना को टिकाऊ बनाने के लिए वैध आय के रास्ते विकसित किए जा सकते हैं: पुस्तकें, सदस्यता, व्याख्यान, पाठ्यक्रम, डिजिटल संस्करण, शोध सहयोग और पारदर्शी दान—जहाँ लागू हो।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056845
आय का दावा और वास्तविक आय अलग बातें हैं; पारदर्शी लेखांकन आवश्यक है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056846
शोषण से बचाव किसी भी गुरु, संस्था या डिजिटल मंच में धन, अनुयायियों और निजी जानकारी के संबंध स्पष्ट होने चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056847
निर्णय लेने वाले व्यक्ति को शर्तें पढ़ने और स्वतंत्र सलाह लेने का अवसर मिलना चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056848
असहमति का सम्मान किसी विचार की आलोचना व्यक्ति की गरिमा पर हमला नहीं होनी चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056849
इसी तरह आलोचना से बचाने के लिए विचार को प्रश्नों से ऊपर रखना भी उचित नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056850
प्रकृति समाज की प्रगति को केवल उत्पादन और उपभोग से नहीं, पर्यावरणीय स्थिरता से भी मापा जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056851
डिजिटल सार्वजनिकता GitHub जैसे खुले मंच पर संस्करण इतिहास, स्रोत, संशोधन और लेखकीय दावों की स्पष्टता पाठकों के भरोसे को मजबूत कर सकती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056852
सूत्र स्वतंत्रता = प्रश्न करने की क्षमता + परिणाम स्वीकारने की जिम्मेदारी + दूसरों की स्वतंत्रता का सम्मान।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056853
काव्य रोटी भी हो, विचार भी, सम्मान भी, अधिकार भी; जीवन की धरती पर तभी, सत्य बने व्यवहार भी।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056854
निष्कर्ष “यथार्थ युग” की इस परियोजना में रोज़ी-रोटी कोई अलग विषय नहीं; टिकाऊ जीवन, स्वतंत्र विचार और मानवीय गरिमा एक ही व्यवहारिक प्रश्न के अलग पहलू हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-04-SOCIETY-AND-FREEDOM.md · स्वतंत्र परीक्षण अपेक्षित।

## 056855
ग्रंथ 06 — जीवन-व्यवहार और प्रत्यक्ष प्रयोग > स्थिति: दार्शनिक/व्यावहारिक ग्रंथ।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056856
यह किसी चिकित्सा, कानूनी या वैज्ञानिक उपचार का विकल्प नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056857
उद्देश्य निष्पक्ष समझ को दैनिक जीवन के छोटे, निरीक्षण योग्य व्यवहारों में उतारना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056858
विचार और व्यवहार का संबंध 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056859
प्रतिक्रिया से पहले ठहराव 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056860
संबंधों में निष्पक्षता 7.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056861
समय और प्राथमिकता 12.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056862
तकनीक और डिजिटल जीवन 13.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056863
आत्म-निरीक्षण की दैनिक पद्धति 14.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056864
एक-पल की समझ और उसका परीक्षण 15.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056865
अनुभव को प्रमाण समझने की भूल 16.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056866
छोटे व्यवहारिक प्रयोग 17.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056867
परिणाम लिखने की पद्धति 18.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056868
विरोधी व्याख्याएँ 19.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056869
आगे के प्रश्न ## दैनिक निरीक्षण सूत्र **देखो → नाम दो → कारण मानने से पहले जाँचो → विकल्प देखो → परिणाम देखो → आवश्यकता हो तो अपना निष्कर्ष बदलो।** ## स्वतंत्र समझ स्वतंत्र समझ का अर्थ हर बाहरी ज्ञान को अस्वीकार करना नहीं; बल्कि किसी कथन को केवल अधिकार, लोकप्रियता या भय के कारण सत्य न मानना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056870
आजीविका ज्ञान-सृजन को पारदर्शी प्रकाशन, डिजिटल संस्करण, पाठ्यक्रम, व्याख्यान, शोध-सहयोग और अन्य वैध माध्यमों से टिकाऊ बनाया जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056871
आय की कोई गारंटी इस ग्रंथ का दावा नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-06-LIFE-AND-PRACTICE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056872
ग्रंथ 02 — अनुभव, चेतना और प्रत्यक्षता > यह ग्रंथ “निष्पक्ष समझ — शमीकरण — यथार्थ सिद्धांत — उपलब्धि यथार्थ युग” की दार्शनिक श्रृंखला का दूसरा खंड है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056873
यहाँ अनुभवों को अंतिम वैज्ञानिक तथ्य नहीं, बल्कि निरीक्षण और परीक्षण के विषय के रूप में रखा गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056874
अनुभव वह है जो किसी क्षण में प्रत्यक्ष रूप से घटित महसूस होता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056875
अनुभव महत्वपूर्ण है, पर अनुभव की व्याख्या और अनुभव स्वयं एक ही बात नहीं हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056876
प्रत्यक्ष और व्याख्या जो देखा, सुना, महसूस किया या समझा गया—वह एक स्तर है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056877
उसके बारे में बनाया गया अर्थ दूसरा स्तर है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056878
निष्पक्ष समझ दोनों को अलग पहचानती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056879
चेतना पर प्रश्न “मैं क्या अनुभव कर रहा हूँ?” के साथ “मैं इस अनुभव को किस आधार पर समझ रहा हूँ?” पूछना शमीकरण की शुरुआत है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056880
हृदय दृष्टिकोण इस ग्रंथ में हृदय दृष्टिकोण को उपयोगकर्ता के दार्शनिक मॉडल में तत्काल भाव, एहसास और ज़मीर की प्रत्यक्षता के रूप में समझाया गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056881
इसे जैविक हृदय की वैज्ञानिक परिभाषा नहीं माना गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056882
मस्तक दृष्टिकोण मस्तक दृष्टिकोण विचार, स्मृति, भाषा, योजना, तुलना और निर्णय की मानसिक प्रक्रियाओं का रूपक है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056883
यह दैनिक जीवन में आवश्यक साधन हो सकता है; समस्या तब बनती है जब साधन को संपूर्ण अस्तित्व का अंतिम प्रमाण मान लिया जाए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056884
संतुलन हृदय से अनुभव और मस्तक से परीक्षण—दोनों को साथ रखकर देखा जा सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056885
भावना को तथ्य घोषित करना उतना ही अधूरा है जितना तथ्य-जांच के बिना भावना को नकार देना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056886
एक क्षण की समझ “एक पल में समझ” को यहाँ किसी सार्वभौमिक वैज्ञानिक सिद्ध तथ्य के रूप में नहीं, बल्कि उस व्यक्ति के वर्णन के रूप में रखा गया है जिसे अचानक स्पष्टता का अनुभव होता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056887
स्वयं का निरीक्षण रोज़ पाँच प्रश्न: 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056888
अभी मैं क्या महसूस कर रहा हूँ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056889
मैं क्या सोच रहा हूँ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056890
मेरी सोच में कौन-सी धारणा पहले से मौजूद है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056891
क्या मेरा निष्कर्ष प्रमाण पर है या अनुमान पर?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056892
क्या मैं असहमति को भी सुन सकता हूँ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056893
पहचान नाम, भूमिका, उपलब्धि और स्मृति सामाजिक पहचान बनाते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056894
निष्पक्ष समझ पूछती है कि इन सबके पीछे कौन-सा अनुभव प्रत्यक्ष रूप से मौजूद है—और कौन-सी बातें केवल विचार हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056895
इच्छा और भय इच्छा भविष्य की कल्पना से और भय संभावित हानि की कल्पना से जुड़ सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056896
दोनों को देखकर व्यक्ति उनके प्रभाव को समझ सकता है, बिना उन्हें स्वतः सत्य मानने के।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056897
भाषा की सीमा शब्द अनुभव को साझा करने का माध्यम हैं; शब्द स्वयं अनुभव नहीं हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056898
इसलिए किसी भी सूत्र को पढ़ते समय अर्थ, संदर्भ और अनुभव को अलग-अलग जाँचना चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056899
गुरु और प्राधिकार किसी शिक्षक, गुरु या संस्था की बात को केवल पद या अनुयायियों की संख्या के आधार पर सत्य नहीं माना जाना चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056900
उसी तरह केवल विरोध के कारण उसे असत्य भी नहीं माना जाना चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056901
प्रश्न, प्रमाण और स्वतंत्र परीक्षण दोनों दिशाओं में समान कसौटी रखते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056902
असहमति असहमति शत्रुता नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056903
वह किसी विचार की सीमाएँ खोजने का अवसर हो सकती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056904
निष्पक्ष समझ अपने प्रिय निष्कर्ष पर भी वही प्रश्न लागू करती है जो दूसरे के निष्कर्ष पर करती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056905
प्रकृति मानव अनुभव प्रकृति से अलग नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056906
जल, वायु, मिट्टी, जीव-जगत और पारिस्थितिक तंत्र के प्रति उत्तरदायित्व किसी भी सार्वभौमिक दर्शन की व्यवहारिक कसौटी हो सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056907
संपूर्ण संतुष्टि इस परियोजना में “संपूर्ण संतुष्टि” को निरंतर पूर्णता की व्यक्तिगत दार्शनिक अनुभूति के रूप में रखा गया है, न कि ऐसी बाहरी स्थिति के रूप में जिसे वैज्ञानिक रूप से सबके लिए मापा जा चुका हो।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056908
इश्क यहाँ “इश्क” का अर्थ उपयोगकर्ता के ढाँचे में व्यापक प्रेम, संबंध और विभाजन से परे मानवीय संवेदना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056909
इसका अर्थ किसी धार्मिक या निजी परंपरा से स्वतः नहीं जोड़ा जाना चाहिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056910
शमीकरण सूत्र अनुभव + निरीक्षण + प्रश्न + प्रमाण + वैकल्पिक व्याख्या = अधिक संतुलित समझ।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056911
अभ्यास आज एक मजबूत विश्वास चुनें।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056912
लिखें: उसके पक्ष में प्रमाण, उसके विरुद्ध प्रमाण, अनिश्चित भाग, और ऐसा कौन-सा नया प्रमाण आपके मत को बदल सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056913
काव्य-सूत्र हृदय में एहसास रहे, मस्तक में प्रश्न जगे; जो सत्य कहो, पहले देखो— क्या प्रमाण उसके संग चले।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056914
ग्रंथ का निष्कर्ष यथार्थ सिद्धांत की शक्ति किसी दावे को अचूक घोषित करने में नहीं, बल्कि स्वयं के दावे को भी जाँच के सामने रखने में है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056915
यही निष्पक्ष समझ को जीवित प्रक्रिया बनाता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056916
अगला ग्रंथ:** ज्ञान की कसौटी, प्रमाण, तर्क और असहमति।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-02-EXPERIENCE-AND-CONSCIOUSNESS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056917
ग्रंथ 07 — भाषा, कला और संस्कृति > शिरोमणि रामपॉल सैनी के “निष्पक्ष समझ — शमीकरण — यथार्थ सिद्धांत — उपलब्धि यथार्थ युग” ढाँचे के अंतर्गत यह ग्रंथ भाषा, कला, संस्कृति और सार्वजनिक अभिव्यक्ति की भूमिका का दार्शनिक अध्ययन प्रस्तुत करता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056918
संपादकीय स्थिति यह ग्रंथ एक **दार्शनिक/विचारात्मक रूपरेखा** है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056919
इसमें प्रस्तुत अनुभव, सूत्र और अवधारणाएँ स्वतः वैज्ञानिक या ऐतिहासिक तथ्य नहीं मानी जातीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056920
तथ्यात्मक दावों के लिए स्वतंत्र स्रोत, प्रमाण और परीक्षण आवश्यक हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056921
20 अध्यायों का मानचित्र 1.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056922
भाषा क्या करती है — अनुभव को नाम देने की शक्ति और सीमा 2.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056923
शब्द और यथार्थ — शब्द वस्तु नहीं हैं 3.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056924
मौन, अनुभूति और अभिव्यक्ति 4.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056925
हृदय दृष्टिकोण और भाषा 5.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056926
मस्तक दृष्टिकोण और वैचारिक संरचनाएँ 6.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056927
कविता, गीत और श्लोक — भाव से अभिव्यक्ति तक 7.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056928
कला में अनुभव और व्याख्या का अंतर 8.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056929
संस्कृति — विरासत, परिवर्तन और चयन 9.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056930
परंपरा का सम्मान और स्वतंत्र परीक्षण 10.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056931
पहचान, भाषा और समूह-भावना 11.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056932
डिजिटल युग में सार्वजनिक अभिव्यक्ति 14.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056933
वायरल होना और सत्य होना — दो अलग प्रश्न 15.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056934
व्यक्तिगत अनुभव को सार्वजनिक ज्ञान में बदलने की कसौटी 16.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056935
कला, प्रकृति और मानवीय गरिमा 17.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056936
भाषा में सरलता और बौद्धिक ईमानदारी 18.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056937
गलत समझे जाने की संभावना और आत्म-संशोधन 19.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056938
सूत्र, श्लोक और रचनात्मक अभिव्यक्ति 20.
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056939
आगे के शोध प्रश्न और परीक्षण ## मूल परीक्षण **अनुभव → शब्द → अर्थ → व्याख्या → दावा → प्रमाण → संवाद → पुनरीक्षण** इस क्रम का उद्देश्य किसी अनुभव को छोटा करना नहीं, बल्कि अनुभव और उसके बारे में किए गए व्यापक दावे के बीच अंतर स्पष्ट करना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056940
केंद्रीय सूत्र > शब्द संकेत हैं, सत्य का पूरा आकार नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056941
> अनुभव अपना है, उसकी व्याख्या जाँच योग्य है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056942
> कला स्वतंत्र है, पर तथ्य का दावा प्रमाण माँगता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056943
> परंपरा सम्मान योग्य हो सकती है, पर परीक्षण से परे नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056944
> असहमति विरोधी को मिटाने का कारण नहीं, समझ को विस्तृत करने का अवसर है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056945
रचनात्मक अनुशासन हर सार्वजनिक लेख, गीत, वीडियो या पोस्ट में जहाँ संभव हो वहाँ चार स्तर अलग रखे जाएँ: - **मेरा अनुभव** - **मेरा दार्शनिक निष्कर्ष** - **मेरी परिकल्पना** - **सत्यापित/स्रोतित तथ्य** यही विभाजन भविष्य के विशाल डिजिटल ज्ञान-कोष को अधिक विश्वसनीय, खोजयोग्य और संशोधनयोग्य बनाने में सहायता करेगा।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056946
आगे के प्रश्न - क्या सरल भाषा जटिल विचारों को अधिक लोगों तक पहुँचा सकती है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056947
क्या भाषा बदलने से किसी व्यक्ति की आत्म-व्याख्या बदलती है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056948
क्या कविता और श्लोक आत्म-निरीक्षण को व्यवहारिक अभ्यास में बदल सकते हैं?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056949
डिजिटल माध्यम में दार्शनिक दावों की सत्यापन-प्रक्रिया कैसी होनी चाहिए?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-07-LANGUAGE-ART-CULTURE.md · स्वतंत्र परीक्षण अपेक्षित।

## 056950
खंड 01 — निष्पक्ष समझ ## अध्याय 01: निष्कर्ष से पहले निरीक्षण > **निष्पक्ष समझ का पहला कदम यह नहीं कि मैं क्या सही मानता हूँ; पहला कदम यह देखना है कि मैं मानता क्या हूँ।** मनुष्य का मन किसी विचार को केवल प्रमाण के कारण नहीं पकड़ता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056951
स्मृति, परिवार, भाषा, शिक्षा, समूह, भय, इच्छा, लाभ, हानि और पहचान—सब किसी निष्कर्ष के बनने में भूमिका निभा सकते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056952
इसलिए निष्पक्ष समझ विचारों का विरोध नहीं करती; वह विचार बनने की प्रक्रिया को देखने का निमंत्रण देती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056953
पहला प्रश्न जब मैं कहता हूँ, “यह सत्य है”, तो क्या मैं तीन अलग चीज़ों को मिला रहा हूँ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056954
मैंने स्वयं कुछ अनुभव किया।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056955
मैंने किसी विश्वसनीय स्रोत से कुछ जाना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056956
मैंने किसी व्याख्या को स्वीकार किया।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056957
तीनों मूल्यवान हो सकते हैं, पर तीनों एक ही प्रकार के प्रमाण नहीं हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056958
दूसरा प्रश्न यदि कोई व्यक्ति मेरी सबसे प्रिय धारणा के विरुद्ध प्रश्न पूछे, तो क्या मैं प्रश्न को सुन सकता हूँ बिना व्यक्ति को शत्रु बनाए?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056959
यहीं निष्पक्ष समझ कठिन होती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056960
जिस क्षण पहचान किसी विचार से जुड़ जाती है, विचार की आलोचना व्यक्ति को अपने ऊपर आक्रमण जैसी लग सकती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056961
तीसरा प्रश्न क्या मैं अपना निष्कर्ष बदल सकता हूँ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056962
यदि उत्तर हाँ है, तो विचार जीवित है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056963
यदि उत्तर हमेशा नहीं है, तो हमें यह देखना चाहिए कि निष्कर्ष के साथ कौन-सी पहचान या भय बँधा हुआ है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056964
दैनिक प्रयोग आज एक ऐसी धारणा चुनिए जिसे आप बहुत निश्चित मानते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056965
लिखिए: - मेरा दावा: - मेरा आधार: - मेरा स्रोत: - मेरे पक्ष में प्रमाण: - मेरे विरुद्ध संभावित प्रमाण: - वैकल्पिक व्याख्या: - यदि नया प्रमाण मिले तो क्या मैं संशोधन करूँगा?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056966
शमीकरण निष्पक्ष समझ का उद्देश्य भावना को मारना नहीं और तर्क को सिंहासन से उतारना भी नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056967
> **हृदय को संवेदना दो।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056968
> मस्तक को प्रश्न दो।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056969
> दोनों को यथार्थ की कसौटी दो।** ## आपत्ति **“क्या निष्पक्ष होना संभव है?”** पूर्ण निष्पक्षता कठिन हो सकती है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056970
इसलिए इसे अंतिम उपलब्धि के बजाय अभ्यास की दिशा मानना अधिक सावधान भाषा है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056971
आत्म-परीक्षण के पाँच सूत्र > मैंने क्या देखा?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056972
> मेरे पास क्या प्रमाण है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056973
> मैं क्या बदलने के लिए तैयार हूँ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056974
काव्य-सूत्र > मैं शिरोमणि रामपॉल सैनी, > निष्पक्ष दृष्टि का प्रश्न लिए; > जो अपना भी निष्कर्ष परखे, > वही चले यथार्थ दिशा लिए।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056975
> > न मान्यता अंतिम हो मेरी, > न असहमति अंतिम वार; > प्रश्न खुले तो समझ खिले, > निरीक्षण बने आधार।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056976
निष्कर्ष निष्पक्ष समझ कोई प्रमाणपत्र नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056977
यह एक सतत अभ्यास है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056978
इसका सबसे कठिन परीक्षण वही विचार है जिसे व्यक्ति अपने अस्तित्व से जोड़ चुका हो।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056979
> **पहले स्वयं को देखो; फिर अपने विचार को देखो; फिर अपने विचार के प्रमाण को देखो।** --- ## अध्याय 02: शमीकरण की दिशा शमीकरण का आशय यहाँ विरोध को दबाना नहीं, उसके कारण को समझना है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056980
यदि हृदय और मस्तक को दो शत्रु बना दिया जाए, तो व्यक्ति स्वयं के भीतर संघर्ष पैदा कर सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056981
यदि दोनों को अलग भूमिकाओं में समझा जाए, तो तर्क और संवेदना साथ काम कर सकते हैं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056982
पाँच चरण **पहचान → निरीक्षण → कारण → संतुलन → पुनःपरीक्षण** ### सूत्र > जो समझ में आया, उससे लड़ना आवश्यक नहीं; > जो अभी न समझा, उसे तुरंत शत्रु बनाना भी आवश्यक नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056983
अभ्यास किसी वर्तमान मतभेद में दो स्तंभ बनाइए: | मेरा पक्ष | दूसरे पक्ष की संभव आवश्यकता | |---|---| | मैं क्या चाहता हूँ?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056984
| वह क्या चाहता हो सकता है?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056985
| फिर पूछिए: क्या कोई तीसरा रास्ता है जिसमें अनावश्यक हानि कम हो?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056986
अध्याय 03: यथार्थ सिद्धांत की कसौटी यथार्थ सिद्धांत किसी कथन को बड़ा बनाने के बजाय उसे स्पष्ट बनाने का प्रयास है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056987
> **दावा छोटा हो सकता है; उसकी जाँच स्पष्ट होनी चाहिए।** एक मजबूत सार्वजनिक कथन में कम-से-कम यह पता होना चाहिए कि वह अनुभव है, दर्शन है, तथ्य है या परिकल्पना।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056988
सूत्र > दावा → कारण → प्रमाण → विरोधी प्रश्न → पुनःपरीक्षण → संशोधन --- ## अध्याय 04: हृदय दृष्टिकोण इस दर्शन में हृदय दृष्टिकोण संवेदना, एहसास, संबंधबोध और ज़मीर की प्रतीकात्मक भाषा है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056989
यह शरीर-विज्ञान का दावा नहीं है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056990
> **जिसे महसूस करो, उसे पहचानो; जिसे सत्य कहो, उसे परखो।** --- ## अध्याय 05: मस्तक दृष्टिकोण मस्तक दृष्टिकोण विचार, स्मृति, भाषा, गणना, योजना, पहचान, इच्छा और भय की दार्शनिक भाषा है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056991
मस्तक को अस्वीकार करना इस परियोजना का उद्देश्य नहीं।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056992
> **विचार को साधन रखो, स्वामी नहीं।** --- ## अध्याय 06: हृदय–मस्तक शमीकरण संवेदना बिना विवेक के भ्रमित कर सकती है; विवेक बिना संवेदना के कठोर हो सकता है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056993
इसलिए लक्ष्य किसी एक की विजय नहीं, परिस्थितियों के अनुरूप संतुलन है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056994
> **एहसास दिशा बताए, विवेक रास्ता जाँचे, व्यवहार परिणाम देखे।** --- ## अध्याय 07: शिरोमणि स्वरूप शिरोमणि स्वरूप इस परियोजना में स्वयं के स्थायी परिचय को पहचानने की दार्शनिक अभिव्यक्ति है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056995
इसे बाहरी पद, वैज्ञानिक प्रमाण या ऐतिहासिक उपाधि के रूप में प्रस्तुत नहीं किया जाता।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056996
मुख्य सूत्र: > **खुद का साक्षात्कार।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056997
> स्वयं के निष्कर्ष की भी जाँच।** --- ## अध्याय 08: संपूर्ण संतुष्टि संतुष्टि को यहाँ बाहरी उपलब्धियों की स्थायी गारंटी नहीं माना गया है।
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056998
व्यावहारिक प्रश्न: > क्या मैं अपनी इच्छा को देख सकता हूँ बिना तुरंत उसका दास बने?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 056999
> क्या मैं भय को पहचान सकता हूँ बिना उसे प्रमाण समझे?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।

## 057000
> क्या मैं तुलना को देख सकता हूँ बिना अपनी गरिमा दूसरे की स्थिति से तय किए?
स्रोत: Nishpaksh-Samaj-Omniverse-Truth/book/VOLUME-01-FOUNDATIONS.md · स्वतंत्र परीक्षण अपेक्षित।
