# डिजिटल महाग्रंथ 084

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 083001
Return: The bound object if it exists, an empty object otherwise.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083002
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083003
Return: The id of this bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083004
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083005
Args: id: Id of the bound object.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083006
Return: The bound object that was created.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083007
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083008
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083009
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083010
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083011
Args: value_to_multiply: The value to multiply by.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083012
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083013
Return: The toggled bool value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083014
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083015
Args: value_to_append: The value to append.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083016
Return: The new string value.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083017
)", py::arg("value_to_append")) /**/; } ```
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 083018
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083019
Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083020
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083021
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083022
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083023
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083024
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083025
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083026
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083027
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083028
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083029
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083030
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 083031
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083032
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083033
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083034
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083035
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083036
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083037
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083038
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083039
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083040
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083041
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083042
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083043
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083044
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 083045
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083046
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083047
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083048
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083049
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083050
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083051
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083052
During Application configuration, you will be prompted for information about these extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083053
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083054
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083055
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083056
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083057
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083058
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083059
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083060
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083061
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083062
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083063
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083064
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083065
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083066
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083067
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083068
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083069
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083070
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083071
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083072
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083073
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083074
The USD Viewer template includes sample assets for this purpose.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083075
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083076
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083077
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083078
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083079
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083080
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083081
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083082
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083083
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083084
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083085
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083086
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083087
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083088
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083089
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083090
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083091
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083092
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083093
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083094
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083095
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083096
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083097
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083098
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083099
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083100
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083101
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083102
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083103
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083104
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083105
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083106
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083107
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083108
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083109
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083110
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083111
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083112
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083113
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083114
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083115
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083116
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083117
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083118
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083119
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083120
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083121
Collaborating on large-scale design projects in real-time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083122
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083123
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083124
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083125
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083126
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083127
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083128
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083129
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083130
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083131
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083132
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083133
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083134
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083135
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083136
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083137
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083138
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083139
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083140
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083141
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083142
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083143
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083144
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083145
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083146
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083147
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083148
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083149
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083150
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083151
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083152
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083153
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083154
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083155
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083156
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083157
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083158
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083159
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083160
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083161
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083162
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083163
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083164
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083165
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083166
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083167
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083168
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083169
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083170
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083171
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083172
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083173
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083174
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083175
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083176
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083177
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083178
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083179
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083180
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083181
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083182
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083183
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083184
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083185
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083186
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083187
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083188
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083189
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083190
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083191
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083192
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083193
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083194
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083195
:warning: **Important**: These layers are not standalone application templates.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083196
They must be used in conjunction with a base application template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083197
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083198
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083199
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083200
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083201
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083202
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083203
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083204
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083205
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083206
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083207
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083208
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083209
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083210
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083211
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083212
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083213
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083214
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083215
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083216
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083217
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083218
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083219
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083220
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083221
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083222
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083223
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083224
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083225
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083226
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083227
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083228
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083229
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083230
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083231
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083232
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083233
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083234
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083235
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083236
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083237
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083238
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083239
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083240
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083241
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083242
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083243
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083244
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083245
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083246
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083247
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083248
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083249
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083250
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083251
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083252
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083253
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083254
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083255
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083256
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083257
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083258
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083259
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083260
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083261
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083262
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083263
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083264
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083265
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083266
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083267
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083268
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083269
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083270
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083271
If multiple container images exist, you will be
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083272
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083273
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083274
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083275
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083276
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083277
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083278
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083279
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083280
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083281
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083282
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083283
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083284
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083285
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083286
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083287
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083288
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083289
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083290
After initial shader compilation, startup time will reduce dramatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083291
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083292
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083293
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083294
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083295
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083296
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083297
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083298
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083299
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083300
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083301
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083302
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083303
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083304
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083305
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083306
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083307
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083308
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083309
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083310
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083311
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083312
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083313
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083314
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083315
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083316
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083317
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083318
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083319
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083320
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083321
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083322
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083323
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083324
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083325
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083326
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083327
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083328
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083329
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083330
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083331
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083332
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083333
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083334
You should see the streaming client connect to the running Kit application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083335
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083336
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083337
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083338
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083339
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083340
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083341
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083342
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083343
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083344
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083345
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083346
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083347
During Application configuration, you will be prompted for information about this extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083348
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083349
Subsequent extensions can be added to the .kit file manually.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083350
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083351
Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083352
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083353
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083354
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083355
Enter application_display_name:** [set application display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083356
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083357
Setup Extension -> kit_service_setup* - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083358
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083359
Enter extension_display_name:** [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083360
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083361
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083362
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083363
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083364
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083365
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083366
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083367
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083368
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083369
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083370
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083371
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083372
When adapting an existing extension for a headless service, keep the service execution path limited to the dependencies it requires.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083373
Prefer separating reusable headless logic from UI, viewport, rendering, and other application-specific functionality.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083374
If separation is impractical, dependencies that the service can operate without may be declared optional, provided their imports and initialization are also guarded.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083375
See [Adapting Existing Extensions for Headless Services]( for guidance and examples.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083376
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083377
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083378
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083379
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083380
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083381
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083382
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083383
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083384
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083385
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083386
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083387
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083388
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083389
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083390
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083391
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083392
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083393
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083394
This will dictate the behavior of your containerized application.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083395
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083396
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083397
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083398
The base application `.kit` file should be used for containerization.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083399
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083400
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083401
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: NVIDIA-Omniverse/kit-app-template:templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083402
Kit SDK Upgrade Skill ## What This Is This repository contains an AI agent skill for upgrading Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083403
The skill encodes the complete breaking-change catalog for the Kit 106→107→108→109→110 migration path — including removed extensions, deprecated APIs, C++ ABI breaks, Python runtime changes, and configuration updates — into a structured set of instructions and reference data that an AI agent can execute against a live project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083404
The agent scans the project, produces a categorized report with exact `file:line` references, and suggests targeted fixes, including auto-fixable regex replacements where safe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083405
Who It's For Kit extension and application developers who need to upgrade a project from one Kit SDK version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083406
This includes developers working on kit-app-template-based applications, standalone extensions, and Isaac Sim integrations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083407
The skill is particularly useful when upgrading across multiple versions at once (e.g., 107→110), where the number of breaking changes makes manual triage error-prone.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083408
What It Contains | File | Description | |------|-------------| | `SKILL.md` | Lean workflow router — loaded by the AI agent.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083409
Holds version/layout/build detection (Step 1) and the migration-path decision (Step 2), and points to the procedure files for everything else.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083410
| | `procedures/toolchain.md` | Step 2.5 — update the `repo_*` build toolchain (the highest-impact part of most upgrades).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083411
| | `procedures/scan.md` | Step 3 — the full per-stage `grep` scan catalog for breaking changes, removed extensions, and config.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083412
| | `procedures/report.md` | Step 4 — the upgrade-report template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083413
| | `procedures/apply-fixes.md` | Step 5 — ordered fix list, auto-fixable regex patterns, and manual-only changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083414
| | `procedures/validate.md` | Step 6 — clean-rebuild and validation commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083415
| | `procedures/failure-modes.md` | Symptom→fix diagnosis for projects that already upgraded and are erroring.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083416
| | `procedures/stage-notes.md` | Per-stage (106→107→…→110) breaking-change reference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083417
| | `references/breaking_changes.json` | 80+ breaking changes with search patterns, affected versions, and recommended fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083418
| | `references/removed_extensions.json` | Extensions removed or deprecated by Kit version, with replacement guidance and search targets.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083419
| | `references/api_replacements.json` | 1:1 API replacements that are safe to apply with regex find/replace.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083420
| | `references/config_changes.json` | Settings keys, registry URLs, and build config changes between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083421
| | `references/toolchain.json` | The build-toolchain file/package set (`repo_*` tools, packman, repo scripts) and how to find the correct target versions for a given Kit line.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083422
| | `install.sh` / `install.bat` | Copies the skill (SKILL.md + `procedures/` + `references/`) into an existing Kit project so it travels with the repo.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083423
| The skill uses **progressive disclosure**: `SKILL.md` stays small (a router the agent always loads) and each step's detail lives in a `procedures/*.md` file the agent reads only when the workflow sends it there.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083424
This keeps the entry file well under length limits and keeps irrelevant detail out of context.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083425
How to Use **Install into an existing project** (so the skill travels with the repo): ```bash ./install.sh /path/to/your-kit-project # copies into /.skills/kit-upgrade/ ./install.sh /path/to/your-kit-project .claude/skills # or the Claude Code skills layout ``` On Windows: `install.bat C:\path\to\your-kit-project`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083426
Then load the skill into any AI coding assistant that can read files and run shell commands, and point it at the project you want to upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083427
Claude Code:** ``` Read the skill at /path/to/kit-upgrade-skill/SKILL.md and the reference files in references/.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083428
Then scan /path/to/my-kit-project and generate an upgrade report for Kit 109 → 110.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083429
``` **Cursor / VS Code Copilot / other MCP clients:** Add `kit-upgrade-skill/` as a context directory or attach `SKILL.md` as a system prompt, then ask the agent to scan your project.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083430
Detect the current Kit SDK version, the deps-directory location (`tools/deps/` vs root `deps/`), and the build entrypoint (`./repo.sh` / `repo.bat` or a custom/integrated build) — never assuming the SDK template layout 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083431
Determine the migration path — including within-major (minor/patch) and feature↔production transitions, not just major-version stages 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083432
Update the build toolchain (`repo_*` tools, packman, repo scripts) to match the target Kit line — often the substantive part of an upgrade 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083433
Run targeted `grep` scans across the full project root (including `templates/`, launcher configs, and ETM lock files) for any major boundaries crossed 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083434
Generate a categorized report: breaking changes, behavioral changes, deprecated usage, and a "not affected" checklist 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083435
Suggest fixes — both auto-applicable regex replacements and manual changes requiring human judgment 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083436
Its changes are folded into the 107→109 path — Stage 2 must still be addressed when upgrading 107→109.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083437
Multi-version upgrades (e.g., 107→110) apply all intervening stages in sequence.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083438
How to Contribute **Add a new breaking change:** Add an entry to `references/breaking_changes.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083439
Each entry needs an `id`, `title`, `stage`, `search_pattern` (grep-compatible regex), `affected_files` (glob patterns), and `fix` description.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083440
If the fix is a safe 1:1 substitution, also add it to `references/api_replacements.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083441
Add a removed or deprecated extension:** Add an entry to `references/removed_extensions.json` with `extension`, `status` (`removed` or `deprecated`), `version`, `replacement` (or `null`), `search_in` (list of file extensions to scan), and `notes`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083442
Include any known failure mode (e.g., exit-55) and whether the extension appears in non-obvious locations like `templates/` or ETM lock files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083443
Add a new Kit version (release):** edit the files that own each piece — the skill is split by concern: - `SKILL.md` — add the new row/stage to the **Step 2 migration-path table and Stage summary** (these stay in the router).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083444
`procedures/scan.md` — add the new `# === Stage N ===` scan blocks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083445
`procedures/stage-notes.md` — add the new per-stage breaking-change section.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083446
`procedures/apply-fixes.md` — add any new auto-fix regex patterns or fix-list items.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083447
`references/*.json` — add the corresponding structured entries.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083448
Follow the existing section structure in each file for consistency.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083449
Keep `SKILL.md` lean — detailed scan commands and stage notes belong in `procedures/`, not the router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083450
Test your additions:** Apply the skill to a real project that exercises the new patterns.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083451
If the scan misses something or the fix guidance is wrong, document it and open a PR with both the issue description and the corresponding fix in the relevant `procedures/` or `references/` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083452
This skill was developed and validated against [kit-extension-explorer]( a Kit 110 application based on kit-app-template.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083453
See `test-report.md` for the full upgrade report from that validation run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 083454
name: kit-upgrade description: "Scan and upgrade Omniverse Kit SDK projects between versions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083455
Analyzes project files, identifies breaking changes, deprecated APIs, and removed extensions specific to the customer's code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083456
Provides a personalized upgrade plan with file:line references and auto-fix suggestions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083457
Covers Kit 106→107→108→109→110." --- # Kit SDK Upgrade Skill Guide a developer through upgrading their Omniverse Kit project from one version to another.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083458
This skill is a lean workflow router.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083459
Steps 1 and 2 (detect the project, decide the migration path) are inline below** — they are always needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083460
The detail for the remaining steps (2.5–6) lives in `procedures/`, and the structured change data in `references/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083461
Read each procedure file when the workflow sends you to it** — do not try to hold them all in context at once.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083462
When to Use - User asks to upgrade their Kit project/app/extension - User asks about Kit breaking changes or migration - User is hitting errors after changing their Kit SDK version - User has a broken build or runtime failure after a version bump --- ## Quick Orientation Pick the entry point that matches the request: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083463
First-time upgrade scan** → start at Step 1 below and follow the workflow in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083464
Already upgraded, now has a build/runtime error** → go straight to `procedures/failure-modes.md`, diagnose, then apply the relevant Stage's fixes from `procedures/stage-notes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083465
Just wants a list of breaking changes** → do Step 1, then run the scans in `procedures/scan.md` for their migration path and present the report from `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083466
The `# Kit SDK Version:` comment in `.kit` files reflects the last lock-file regeneration and may differ from the pin during an in-progress upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083467
Version string format: `110.1.0+feature.${platform_target_abi}.${config}` - First number (110) = major Kit version **If no version pin is found:** Check git history (`git log --oneline -20 -- tools/deps/ deps/`) or ask the user what Kit version they are currently running.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083468
(Layout detection below has not run yet, so scope the log to both candidate deps locations.) ### Detect project layout and build system Kit projects do **not** all use the SDK template layout, and the layout can differ between releases and project types — for example, `deps/` may sit at the project **root** in one release and under **`tools/`** in another (even between two point releases of the same major line).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083469
Projects also frequently **wrap or integrate the Kit build system into their own tooling**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083470
Detect the layout and build entrypoint **once**, then reuse them everywhere below — **never assume `tools/deps/` or `./repo.sh`**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083471
deps directory (holds kit-sdk.packman.xml + repo-deps.packman.xml) if [ -f tools/deps/kit-sdk.packman.xml ]; then DEPS_DIR=tools/deps elif [ -f deps/kit-sdk.packman.xml ]; then DEPS_DIR=deps else f=$(find .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083472
name kit-sdk.packman.xml -not -path './_*' | head -1); DEPS_DIR=${f:+$(dirname "$f")}; fi echo "DEPS_DIR=${DEPS_DIR:- }" # 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083473
build entrypoint — the standard repo wrapper, if present if [ -f ./repo.sh ]; then BUILD='./repo.sh' elif [ -f ./repo.bat ]; then BUILD='repo.bat' else BUILD=''; fi # empty => custom / integrated build (see below) echo "BUILD=${BUILD:- }" ``` **If `BUILD` is empty, the project uses a custom or integrated build system** (common — many customers embed the Kit build inside their own).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083474
Do **not** fabricate `./repo.sh` calls.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083475
Find the real build command (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or the project README) or ask the user how they build.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083476
The upgrade work below (kernel pin bump, **toolchain update**, lock regeneration) still applies — you just invoke it through the project's own entrypoint.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083477
Record it as `$BUILD`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083478
> **From here on (and in every procedure file), use `$DEPS_DIR` and `$BUILD` in every command.** Where a document still shows a literal `tools/deps/` or `./repo.sh`, substitute the detected values.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083479
> > **These are not guaranteed to persist across shells.** If you run each fenced block in a fresh subshell, `$DEPS_DIR`/`$BUILD` will be unset.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083480
So do **one** of: (a) textually replace `$DEPS_DIR` and `$BUILD` with the literal detected paths (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083481
`tools/deps`, `./repo.sh`) in every command you run, or (b) re-run the two detection blocks above at the top of each new shell session.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083482
Do **not** run a later block assuming the variables are still set.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083483
Step 2: Determine Migration Path Kit versions must be upgraded **in sequence**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083484
Kit 108 was never publicly released** — its changes are folded into the 107→109 path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083485
When upgrading 107→109 you must still address Stage 2 (107→108) changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083486
A **within-major** bump (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083487
`110.0 → 110.1`, `110.1.0 → 110.1.2`) or a **feature → production** branch transition is a *different, lighter* job — and it is the most common upgrade performed in practice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083488
These rarely need the Stage code/API changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083489
The real work is almost entirely **tooling and layout**: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083490
Update the build toolchain** (repo tools, packman, repo scripts) — see Step 2.5 (`procedures/toolchain.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083491
This is usually the substantive part.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083492
Re-detect the deps directory** — its location can differ between releases, even within the same major line (Step 1 already sets `$DEPS_DIR`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083493
Bump the kit-kernel pin** in `$DEPS_DIR/kit-sdk.packman.xml` (Step 5, item 2 — `procedures/apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083494
For a feature ↔ production transition only:** check the extension **registry URL** in the `.kit` files — the feature and production lines use different registries, so a feature→production move may need a registry swap (Step 5, item 3).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083495
A plain within-major bump on the same line usually does **not**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083496
Regenerate the extension version-lock** and do a **clean rebuild** (Step 5 items 1 & 8, then Step 6).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083497
> **⚠️ Do NOT run the whole of Step 5 for a within-major bump.** Step 5 (`procedures/apply-fixes.md`) is written for **major-boundary** crossings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083498
Running them on a 110.1.0→110.1.2 bump would wrongly strip extensions or rewrite APIs that are perfectly valid on 110.1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083499
Only run the Step 3 code scans if the upgrade crosses a major boundary.** For a pure within-major or feature→production move, skip Step 3's per-stage API scans and go straight to Step 2.5 → Step 5 (items 1–3 & 8 only, as above) → Step 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083500
If you cross one or more major boundaries on the way, run Step 3 for each major boundary passed and the full Step 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083501
Steps 2.5–6: Execute the Upgrade Once the path is known, work through these in order.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083502
Read the linked procedure file and follow it**; each assumes Step 1 detection has run.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083503
Step 2.5 — Update the build toolchain** → `procedures/toolchain.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083504
Highest-impact step; run it **first**, before touching source.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083505
For a within-major bump this is usually the only substantive work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083506
Step 3 — Scan the project** → `procedures/scan.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083507
Run only the stage scans for the major boundaries you cross.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083508
Skip entirely for a pure within-major bump.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083509
Step 4 — Generate the upgrade report** → `procedures/report.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083510
Present findings by severity with exact `file:line` references.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083511
Step 5 — Apply fixes** → `procedures/apply-fixes.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083512
Get user approval before modifying files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083513
(Within-major: items 1, 2, 8 only — see Step 2 above.) - **Step 6 — Validate** → `procedures/validate.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083514
Clean rebuild, regenerate the version lock, run tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083515
Already upgraded and hitting a specific error?** Go to `procedures/failure-modes.md` — it maps common symptoms (exit-55, ABI undefined symbols, render diffs, build loops, custom-build/layout issues) to fixes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 083516
Step 3: Scan the Project > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083517
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083518
Only run this step for major-version boundaries you cross** — a pure within-major / feature→production bump skips it.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083519
Run these commands from the project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083520
Only run scans for the stages that apply to this upgrade.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083521
Collect all matches before generating the report.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083522
> **⚠️ Scan scope:** Use `.` (project root) as the search root, not just `source/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083523
Many projects have `templates/`, `launcher-configs/`, or other directories containing `.kit` files and `extension.toml` files with real dependency declarations.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083524
Scanning only `source/` will miss these.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083525
> > **Windows note:** Commands below use bash syntax.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083526
On Windows, replace `for` loops with individual `findstr` or PowerShell `Select-String` commands, or run inside WSL/Git Bash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083527
Python / Extension Dependencies ```bash # === Stage 1 (106→107) === # Python 3.10 references (now 3.11) grep -rn "python3\.10\|python310\|boost_python310" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083528
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" --include="*.toml" # Private omni.client API grep -rn "omni\.client\._omniclient" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083529
include="*.py" # carb.imgui (removed — use omni.kit.imgui) grep -rn "carb\.imgui" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083530
include="*.py" # Events 1.0 patterns (payload access, subscription style) grep -rn "e\.payload\[" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083531
include="*.py" grep -rn "create_subscription_to_pop" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083532
include="*.py" # nv_usd references in build files grep -rn "nv_usd" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083533
premake5.lua repo.toml --include="*.lua" --include="*.toml" # packman XML using a pre-ABI token (should be ${platform_target_abi}).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083534
NOTE: match BOTH the old ${platform} form (Kit 106) and the intermediate ${platform_target} form — # the narrower 'platform_target[^_]' pattern misses ${platform}, which is what 106.5 actually uses and # is a build-verified hard failure on 106->107 (kit-kernel pull: "Package not found ...gl.linux-x86_64").
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083535
grep -rnE '\$\{platform(_target)?\}' "$DEPS_DIR" --include="*.xml" # Toolbar deprecated APIs grep -rn "omni\.kit\.widget\.toolbar\|omni\.kit\.window\.toolbar" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083536
include="*.py" --include="*.toml" # === Stage 2 (107→108) === # Python 3.11 references (now 3.12) grep -rn "python3\.11\|python311\|boost_python311" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083537
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" # get_custom_glyph_code (moved to omni.ui) grep -rn "omni\.kit\.ui.*get_custom_glyph_code" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083538
include="*.py" # WindowHandle deprecated usage grep -rn "WindowHandle" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083539
include="*.py" # menu_compatibility (deprecated in 108, removed in 110) grep -rn "menu_compatibility" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083540
include="*.py" # Layer events (Events 1.0 style) grep -rn "get_event_stream\|create_subscription_to_pop\|carb\.events" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083541
include="*.py" # Livestream extension (monolithic — should be split) grep -rn '"omni\.kit\.livestream"' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083542
include="*.kit" --include="*.toml" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083543
include="*.kit" --include="*.toml" # Livestream settings (old path) grep -rn "app/livestream\|app\.livestream" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083544
include="*.kit" --include="*.toml" # Old omni.kit.ui transitive usage (no longer loaded transitively) grep -rn "omni\.kit\.ui[^.]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083545
include="*.py" # === Stage 3 (108→109) === # NumPy 1.x type aliases (removed in 2.0) grep -rn "np\.bool[^_]\|np\.int[^0-9_]\|np\.float[^0-9_]\|np\.complex[^0-9_]\|np\.object[^_]\|np\.str[^_]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083546
include="*.py" # === Stage 4 (109→110) === # menu_compatibility (now raises TypeError — must remove entirely) grep -rn "menu_compatibility=" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083547
include="*.py" # omni.usd layers deprecated API grep -rn "get_context()\.get_layers()\|context\.get_layers()" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083548
include="*.py" # omni.renderer_capture (deprecated → omni.kit.capture) grep -rn "omni\.renderer_capture" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083549
include="*.py" # USD displayName/displayGroup/hidden deprecated metadata grep -rn "GetMetadata.*displayName\|SetMetadata.*displayName\|GetMetadata.*hidden\|SetMetadata.*hidden\|GetMetadata.*displayGroup\|SetMetadata.*displayGroup" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083550
include="*.py" ``` ### C++ / Native Code ```bash # === Stage 1 (106→107) === # C++ ABI — check for _GLIBCXX_USE_CXX11_ABI overrides (must be =1) grep -rn "_GLIBCXX_USE_CXX11_ABI" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083551
include="*.cpp" --include="*.h" --include="*.cmake" # === Stage 2 (107→108) === # ITokens::setValue (renamed to setValueS) grep -rn "->setValue(" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083552
include="*.cpp" --include="*.h" # carb::detail::defineTupleCommon grep -rn "carb::detail::defineTupleCommon" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083553
include="*.cpp" --include="*.h" # PyObjectVTable::get()->typeName grep -rn "PyObjectVTable" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083554
include="*.cpp" --include="*.h" # acquireInterface (prefer getCachedInterface) grep -rn "acquireInterface" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083555
include="*.cpp" --include="*.h" # carb::extras::Path implicit conversion grep -rn "carb::extras::Path\|carb::fs::Path" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083556
include="*.cpp" --include="*.h" # Assert macros (may need explicit carb/Assert.h now) grep -rn "CARB_ASSERT\|CARB_FATAL_UNLESS" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083557
include="*.cpp" --include="*.h" # Library.h removed functions grep -rn "getDefaultLibraryPrefix\|getDefaultLibraryExtension" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083558
include="*.cpp" --include="*.h" # GfMatrix usage (imprecise overloads removed) grep -rn "GfMatrix" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083559
include="*.cpp" --include="*.h" # ILayers.h inclusion (ABI 1.0 → 1.1 recompile required) grep -rn "ILayers\.h\|omni/kit/usd/layers" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083560
include="*.cpp" --include="*.h" # carb.events const char* usage (deprecated — prefer string_view) grep -rn "carb::events::\|IEventQueue\|IEvents" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083561
include="*.cpp" --include="*.h" # Scalar xform ops — code that iterates over xform ops assuming vector types grep -rn "GetOrderedXformOps\|xformOp:translate\|xformOp:scale\|xformOp:rotate" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083562
include="*.cpp" --include="*.h" --include="*.py" # === Stage 3 (108→109) === # Fabric TokenC/PathC (removed; also kUninitializedToken/Path) grep -rn "TokenC\|PathC\|TokenId\|PathId\|kUninitializedToken\|kUninitializedPath" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083563
include="*.cpp" --include="*.h" # carb::cpp17 / carb::cpp20 (merged to carb::cpp) grep -rn "carb::cpp17\|carb::cpp20" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083564
include="*.cpp" --include="*.h" # carb::thread::shared_lock (removed) grep -rn "carb::thread::shared_lock" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083565
include="*.cpp" --include="*.h" # IDictionary::MakeAtPathS (renamed to MakeAtPath) grep -rn "MakeAtPathS" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083566
include="*.cpp" --include="*.h" # compareStringsNoCase (renamed) grep -rn "compareStringsNoCase" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083567
include="*.cpp" --include="*.h" # Logger (superseded by Logger2) grep -rn "carb::logging::Logger[^2]" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083568
include="*.cpp" --include="*.h" # MDL/Neuray usage (ABI 56 → 57 recompile required) grep -rn "omni\.mdl\|Neuray\|MDL.*SDK" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083569
include="*.cpp" --include="*.h" --include="*.toml" # CloudXR / XRCloudXRBindings grep -rn "CloudXR\|XRCloudXRBindings\|IOpenXRRuntime" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083570
include="*.cpp" --include="*.h" # === Stage 4 (109→110) === # CARB_CHECK (replaced by CARB_RELEASE_ASSERT) grep -rn "CARB_CHECK" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083571
include="*.cpp" --include="*.h" # carb/Defines.h (split into sub-headers) grep -rn '#include.*carb/Defines\.h' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083572
include="*.cpp" --include="*.h" # IFileSystem raw char* methods grep -rn "IFileSystem" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083573
include="*.cpp" --include="*.h" # ITokens (unsafe methods removed; ITokens 2.0 available) grep -rn "ITokens\|->resolveString\|->setValue" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083574
include="*.cpp" --include="*.h" # optional / expected — semantics changed (if(b) now tests presence) grep -rn "optional \|expected **Important:** Also scan `templates/`, `launcher-configs/`, and any ETM lock files (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083575
`omni.all.template.extensions.kit`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083576
These contain real dependency declarations and will cause test or runtime failures if they reference removed extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083577
```bash # === All stages — removed/deprecated extensions === # Kit 108 removals grep -rn "omni\.kit\.extpath\.git" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083578
include="*.toml" --include="*.kit" # Kit 108 — monolithic livestream (split into modules) grep -rn '"omni\.kit\.livestream"' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083579
include="*.toml" --include="*.kit" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083580
include="*.toml" --include="*.kit" # Kit 110 removals (cause cryptic exit-55 dependency solver failures) for ext in omni.kvdb omni.localcache omni.genproc.core; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083581
include="*.kit" --include="*.toml" done # Kit 110 silently removed (no deprecation notice) for ext in "omni.hydra.iray.shadercache.d3d12" "omni.hydra.iray.shadercache.vulkan" "omni.kit.viewport.iray"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083582
include="*.kit" --include="*.toml" done # Deprecated (not yet removed — still operational but plan migration) for ext in "omni.command.usd" "omni.debugdraw" "omni.hydra.iray" "omni.iray.settings.core" \ "omni.kit.autocapture" "omni.kit.manipulator.viewport" "omni.hydra.scene_api" \ "omni.renderer_capture" "omni.surface_instancer" "omni.kit.viewport.legacy_gizmos" \ "omni.kit.widget.nucleus_connector"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083583
include="*.kit" --include="*.toml" done # Extensions that need explicit declaration (no longer loaded transitively) grep -rn "omni\.kit\.manipulator\.prim\.fabric\|omni\.resourcemonitor\|omni\.kit\.ui" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083584
\ --include="*.py" --include="*.toml" ``` ### Config Files ```bash # Extension registry URLs (must update for Kit 110) grep -rn "kit-extensions\.ov\.nvidia\.com\|omniverse://" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083585
include="*.kit" # Build system (VS version) — also check CI-scoped token overrides # (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083586
"token:in_ci==true".vs_version may override the default even when the top-level is correct) grep -rn "vs_version\|vs2019\|vs2017\|v142" repo.toml # Livestream settings (old path style) grep -rn "app/livestream" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083587
include="*.kit" --include="*.toml" # Kit SDK version pin (use the $DEPS_DIR detected in Step 1) cat "$DEPS_DIR/kit-sdk.packman.xml" # mergeMaterials (behavioral default change in 109) grep -rn "mergeMaterials" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083588
include="*.kit" --include="*.toml" # FSD / Fabric Scene Delegate settings grep -rn "FabricSceneDelegate\|fsd\b" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083589
include="*.kit" --include="*.toml" ``` ### OmniGraph ```bash # === Stage 2 (107→108) — OmniGraph 3.0 ABI === grep -rn "omni\.graph\.core\|omni\.graph\.nodes" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083590
include="*.toml" # === Stage 4 (109→110) — deprecated/removed OmniGraph nodes === # DeformedPointsToHydra — removed (was part of OmniHydra) grep -rn "DeformedPointsToHydra" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083591
include="*.py" --include="*.usd" --include="*.usda" # OnCustomEvent bundle attributes deprecated grep -rn "OnCustomEvent" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083592
include="*.py" --include="*.usd" --include="*.usda" # Bundle/attribute manipulation nodes deprecated grep -rn "ArrayGetSize\|AttributeType\|BundleConstructor\|CopyAttribute\|ExtractPrim\|GetAttributeNames\|HasAttribute\|InsertAttribute\|RemoveAttribute\|RenameAttribute" \ .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083593
include="*.py" --include="*.usd" --include="*.usda" # Event/render pipeline nodes deprecated grep -rn "UpdateTickEvent\|GpuInteropCudaEntry\|RenderPreprocessEntry\|RpResourceExample" \ .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083594
include="*.py" --include="*.usd" --include="*.usda" ``` ### Isaac Sim Projects If the project uses Isaac Sim extensions, scan for the `omni.isaac.*` namespace migration (applies Kit 107+): ```bash # omni.isaac.* imports (deprecated → isaacsim.*) grep -rn "omni\.isaac\." .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083595
include="*.py" --include="*.toml" --include="*.kit" # omni.replicator.isaac (→ isaacsim.replicator.*) grep -rn "omni\.replicator\.isaac" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083596
include="*.py" --include="*.toml" # Dynamic Control Toolbox (removed as compile-time dep) grep -rn "dynamic_control\|DynamicControl" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083597
include="*.py" --include="*.cpp" --include="*.h" # SemanticsAPI (→ UsdSemantics.LabelsAPI) grep -rn "add_update_semantics\|SemanticsAPI" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 083598
Step 6: Validate > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 083599
Assumes Step 1 detection has run (`$BUILD` is set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 083600
```bash # After a kit-kernel pin bump, do a CLEAN rebuild so the kernel symlinks refresh, # then regenerate the version lock against the new kernel.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 083601
$BUILD is the entrypoint detected in Step 1 (./repo.sh, repo.bat, or the project's own build wrapper).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 083602
`No versions of > omni.anim.curve.core … = `).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 083603
Use **`$BUILD build --clean`** (removes the build-time `_*` > folders so the next `build -r` refreshes the symlinks) or **`$BUILD build --rebuild -r`** (clean + > release build in one command), then regenerate the lock with `build -u`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 083604
The generated `[settings.app.exts] > enabled = [...]` block in each `.kit` is what must be regenerated — it carries exact old-version pins that > `extscache` clearing does not touch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 083605
Step 4: Generate Upgrade Report > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083606
Run after the Step 3 scans (`scan.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083607
Present findings organized by severity.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083608
Use exact `file:line` references from scan output.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083609
``` ## Upgrade Report: Kit [FROM] → [TO] Project: [path] Migration stages applied: [e.g., Stage 2 + 3 + 4] ### ❌ Breaking Changes (must fix — build or load will fail) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083610
[file:line] — [description] → [exact fix] ### ⚠️ Behavioral Changes (no error, but may affect output or performance) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083611
[file:line] — [description] → [fix or test required] ### 🔔 Deprecated Usage (should fix — will break in next version) 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083612
[file:line] — [description] → [fix] ### ✅ Not Affected - [List the `id` or `title` from `breaking_changes.json` for each pattern that was scanned and returned no matches.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083613
This serves as a record that the check was performed, not just skipped.] ### 📋 Required Steps Regardless of Code Changes 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083614
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083615
Update `kit-sdk.packman.xml`: change version pin to `[TO].x.y+feature.${platform_target_abi}.${config}` 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083616
Update extension registry URLs in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083617
Rebuild all C++ extensions (ABI break at every stage — required even with no source changes) 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083618
Regenerate version lock blocks in `.kit` files: `$BUILD precache_exts -c release` (substitute the build entrypoint detected in Step 1 — `./repo.sh` may not exist on a custom/integrated build) 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083619
If project has an ETM lock file (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083620
`omni.all.template.extensions.kit`), regenerate it or manually remove entries for removed extensions 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083621
[stage-specific items, e.g., VS2022 for Stage 4] ### 🧪 Behavioral Tests Required 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083622
[scenes with DomeLights — orientation regression (Stage 3, but inherited in all later stages)] 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083623
[load performance with mergeMaterials setting (Stage 3)] 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083624
[render output with FSD enabled (Stage 3)] 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083625
[MaterialX materials (Stage 4)] 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083626
[transform-heavy workflows after scalar xform ops change (Stage 2)] ``` **Prioritize for the user:** Extension removal errors and ABI rebuild requirements are the most common causes of project failures after a version bump.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 083627
Failure Mode Diagnosis > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083628
Use this when the user has **already** upgraded and has a specific error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083629
`$DEPS_DIR` / `$BUILD` refer to the values detected in Step 1 (in `../SKILL.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083630
Exit Code 55 (Dependency Solver Failure) **Cause:** Removed extension still declared as a dependency, or stale extscache.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083631
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083632
Search for removed extension names in `.kit` and `extension.toml` files (see `../references/removed_extensions.json`) 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083633
For Kit 110: check for `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.*`, `omni.kit.viewport.iray` 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083634
Re-run `precache_exts` ### Build Fails with Undefined Symbol / Missing Method **Cause:** ABI break — extension was compiled against an older version.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083635
Fix:** Recompile the extension against the current Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083636
Every stage has at least one ABI break.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083637
Runtime Crash on DLL Load (Windows) **Cause after Stage 3:** mimalloc cross-DLL heap mismatch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083638
Memory allocated on one side of a DLL boundary freed on the other.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083639
Fix:** Audit allocation ownership.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083640
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083641
Python TypeError: unexpected keyword argument 'menu_compatibility' **Cause (Stage 4):** `menu_compatibility` parameter removed from `ui.Menu` and `ui.Separator`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083642
Fix:** Remove the `menu_compatibility=` argument from all call sites.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083643
Extension Loads But APIs Return None / AttributeError **Cause:** Transitive loading of `omni.kit.ui`, `omni.resourcemonitor`, or `omni.kit.manipulator.prim.fabric` was removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083644
Fix:** Add explicit dependency in `extension.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083645
Render Output Differs (No Code Changes) **Cause after Stage 3:** DomeLight orientation changed (USD 25.05), FSD enabled by default, or `mergeMaterials` default changed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083646
Diagnosis:** - Check for DomeLights in the scene: `grep -rn "DomeLight" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083647
include="*.usd" --include="*.usda"` - Check FSD setting: `grep -rn "FabricSceneDelegate\|fsd" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083648
include="*.kit" --include="*.toml"` - Check `mergeMaterials`: `grep -rn "mergeMaterials" .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083649
include="*.kit" --include="*.toml"` ### if (optional_bool) No Longer Works (C++) **Cause (Stage 4):** `optional ` / `expected ` now tests for *presence* in an if-condition, not the stored value.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083650
Fix:** Replace `if (b)` with `if (b.has_value() && b.value())` ### Build Fails in a Loop / the Same Error Repeats **Cause:** Almost always a **stale toolchain** (Step 2.5 not applied — see `toolchain.md`) or a wrong assumption about the project's layout/build system — *not* the source code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083651
Rule — do not keep editing source and rebuilding.** If the same build error recurs after **2 attempts**, STOP and re-check the fundamentals before changing any more code: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083652
Is the **toolchain** aligned to the target Kit line?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083653
(Step 2.5, `toolchain.md` — the #1 cause of build loops.) 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083654
Is `$DEPS_DIR` the **actual** deps location and `$BUILD` the project's **actual** build entrypoint?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083655
(Step 1 in `../SKILL.md`.) 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083656
Did you do a **clean** rebuild (`$BUILD build --rebuild -r`), not just clear extscache?
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083657
(Step 6, `validate.md`.) Surface the exact error and these three checks to the user rather than looping — repeated speculative edits burn tokens and rarely fix a toolchain/layout problem.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083658
Project Uses a Custom / Integrated Build System **Cause:** The project wraps or embeds the Kit build system in its own tooling, so `./repo.sh` / `repo.bat` don't exist or aren't the real entrypoint (common for customer integrations).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083659
Fix:** Do **not** fabricate `./repo.sh` commands.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083660
Use the `$BUILD` detected in Step 1 (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or ask the user).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083661
The upgrade steps (kernel pin, **toolchain update**, lock regen) still apply — invoke them through `$BUILD`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083662
deps Directory Not Where Expected **Cause:** The project layout differs from the SDK template, or the deps directory moved between releases (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083663
`deps/` at the project root vs under `tools/`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083664
Fix:** Re-run the Step 1 detection (in `../SKILL.md`) to set `$DEPS_DIR`, then use it everywhere.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083665
Never hardcode `tools/deps/`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083666
Step 2.5: Update the Build Toolchain (highest-impact — often the real work) > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083667
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083668
Run this **before** touching source code — for a within-major / feature→production bump it is usually the *only* substantive work.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083669
> **Key principle:** the most valuable part of an upgrade is usually **not** the code changes — it is making sure the project's **tooling** is correctly updated (repo scripts, `repo_man`/repoman, dependency versions).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083670
This step is therefore **first-class for every upgrade**, and the *primary* step for within-major / branch-transition bumps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083671
Run it **before** touching source code.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083672
Why it matters:** the Kit kernel pin and the repo toolchain are coupled.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083673
Bumping `kit-sdk.packman.xml` alone frequently fails because packman tokens (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083674
`${platform_target_abi}`) only resolve under the matching `repo_man`, and newer kernels expect newer `repo_build` / `repo_kit_tools`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083675
A pin bump *without* a toolchain bump produces cryptic pull/resolve failures — e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083676
`Package not found ...gl.linux-x86_64` or `No versions of … = `.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083677
The toolchain = these files** (see `../references/toolchain.json`): - `$DEPS_DIR/repo-deps.packman.xml` — the `repo_*` tools: `repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_tools_internal`, `repo_kit_template`, `repo_usd`, `repo_format`, `repo_test`, `repo_package`, `repo_ci`, etc.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083678
`$DEPS_DIR/kit-sdk.packman.xml` — the kit-kernel pin (updated in Step 5, item 2 — see `apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083679
`tools/packman/` — the packman bootstrap (`packman`, `packman.cmd`, `bootstrap/`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083680
`repo.sh` / `repo.bat` — the repo wrappers (may need regenerating under a newer `repo_man`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083681
`repo.toml` — build config (VS/MSVC/WinSDK for Stage 4; see `../references/config_changes.json`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083682
How to find the correct target versions — do NOT guess:** 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083683
Get a **reference project already on the target Kit version** — the matching `kit-app-template` or `kit-sdk-public` branch for that Kit line, or the target Kit SDK release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083684
Read its `repo-deps.packman.xml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083685
Prefer the `production/ ` branch** — it carries the vetted, most-current toolchain for that release.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083686
⚠️ **Toolchain versions track the branch's maintenance cadence, not the kernel number** — a newer kernel line can ship an *older* toolchain (in kit-sdk-public, `feature/main` pins kernel 110.4 with `repo_man` 2.6.4, while the maintained `production/110.1` pins kernel 110.1.3 with a *newer* `repo_man` 2.9.3).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083687
Always read the target branch's **actual** pins; never assume "newer Kit = newer tools".
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083688
(Those version numbers are an illustrative snapshot read in 2026 — they **will** go stale; verify against the live branch, do not copy them.)* 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083689
Diff** the project's `$DEPS_DIR/repo-deps.packman.xml` against the reference and align each `repo_*` tool `version=` to the reference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083690
Do the same for `tools/packman/` if it differs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083691
Apply the versions, then do a **clean rebuild** (Step 6 — see `validate.md`) — the toolchain bump must land before the kernel pin resolves cleanly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083692
> This step is safe to run and validate (Step 6) **on its own, first**.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083693
Many "the upgrade won't build" error loops are nothing more than a stale toolchain — fixing it up front avoids chasing phantom code errors.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 083694
Step 5: Apply Fixes > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083695
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083696
> **Within-major / feature→production upgrade?** Run **only items 1, 2, 8** below (plus item 3 *if* a feature↔production registry swap is needed), then Step 6 (`validate.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083697
Skip items 4–7** — they apply only when a major boundary is crossed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083698
See "Within-major upgrades" under Step 2 in `../SKILL.md`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083699
Get user approval before modifying files.** Then apply in this order (a full major-boundary upgrade runs all eight): 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083700
Clear extscache** first: `rm -rf _build/*/release/extscache/` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083701
Update version pin** in `$DEPS_DIR/kit-sdk.packman.xml` 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083702
Update registry URLs** in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083703
Replace deprecated APIs** using patterns in `../references/api_replacements.json` — these are safe regex replacements 5.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083704
Remove deprecated extension deps** from `extension.toml` and `.kit` files (see `../references/removed_extensions.json`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083705
For 109→110 specifically:** the following six extensions are removed with **no deprecation notice**, and any lingering reference causes a cryptic `exit code 55` dependency-solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083706
They MUST be removed from every `.kit` (and `extension.toml`) file: - `omni.kvdb` - `omni.localcache` - `omni.genproc.core` - `omni.hydra.iray.shadercache.d3d12` - `omni.hydra.iray.shadercache.vulkan` - `omni.kit.viewport.iray` ⚠️ **Check the generated version-lock block, not just `[dependencies]`.** In application `.kit` files these names almost always appear in the auto-generated `[settings.app.exts] enabled = [...]` lock (pinned at the old version, e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083707
`omni.kvdb-109.0.10`), **not** the hand-authored dependency list.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083708
Clearing extscache (step 1) does NOT remove them** — you must regenerate the lock: delete the `# BEGIN GENERATED PART` … `# END GENERATED PART` block (the `.kit` says "Remove from 'BEGIN' to 'END' to regenerate") and run `$BUILD precache_exts -c release` so it is rebuilt without the removed extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083709
Then confirm a clean rebuild (the version stamp should advance to 110 and the six names should be gone).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083710
(If you are working in an internal `kit-app-template` checkout, the ETM lock file `templates/omni.all.template.extensions.kit` and any internal-registry entries are KAT-internal — wrapped in `# AUTOREMOVE` and stripped from external releases by `repo stage_for_github` — so external customer projects will not contain them.) 6.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083711
Add explicit deps** where transitive loading was removed: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` 7.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083712
Update build config** in `repo.toml` (VS version, MSVC version, Windows SDK — see `../references/config_changes.json`) 8.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083713
Important Notes by Stage > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083714
Per-stage reference for the breaking changes summarized in the Step 2 migration table.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083715
Read the stages that apply to the boundaries you cross.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083716
Stage 1: 106 → 107 - **Rebuild required** — Linux ABI changed (`_GLIBCXX_USE_CXX11_ABI=0` → `=1`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083717
All prebuilt `.so` files will fail to load.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083718
packman XML token**: Update the kit-kernel pin token to `${platform_target_abi}` in all `.packman.xml` files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083719
Kit 106 uses the **`${platform}`** form (not `${platform_target}`); both must become `${platform_target_abi}`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083720
Build-verified:* leaving the old token makes the kit-kernel pull fail immediately with `Package not found on specified remote servers (…gl.linux-x86_64.release)`, because Kit 107's kernel is published only under the ABI string (`manylinux_2_35_x86_64`), not `linux-x86_64`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083721
Bump the repo toolchain too (required, easy to miss)** — see **Step 2.5** (`toolchain.md`): the token fix alone is **insufficient** — `${platform_target_abi}` only resolves to the ABI string under the newer `repo_man`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083722
Update `$DEPS_DIR/repo-deps.packman.xml` to the 107-era tooling (`repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_template`, `repo_usd`) and the packman bootstrap.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083723
Build-verified:* under 106.5's `repo_man` 1.86.0 the token still resolves to `linux-x86_64`; after the toolchain bump it resolves to `manylinux_2_35_x86_64` and the pull succeeds.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083724
Carbonite Events 2.0**: The event system changed from push/pump to dispatch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083725
No explicit pump calls needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083726
Python payload access changed from `e.payload['key']` to `e['key']`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083727
C++17 is now available** explicitly in Premake via `cppdialect = "C++17"`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083728
Stage 2: 107 → 108 - **Kit 108 was never publicly released.** These changes still apply when upgrading 107→109.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083729
Python 3.12** replaces 3.11.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083730
Update all Premake configs, CI configs, and boost_python links.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083731
OpenUSD 25.02**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083732
GfMatrix imprecise overloads removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083733
Livestream modularization**: `omni.kit.livestream` (monolithic) → `omni.kit.livestream.app` + `.aov` + `.core`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083734
`omni.services.livestream.nvcf` → `omni.services.livestream.session`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083735
Settings paths changed — see `../references/config_changes.json`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083736
Transitive deps removed**: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` must now be declared explicitly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083737
ILayers ABI 1.0 → 1.1**: Recompile all extensions including `ILayers.h`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083738
USD scalar xform ops**: OpenUSD now supports scalar ops (e.g., `xformOp:translateX`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083739
Code iterating over xform ops that assumes all are vector types may behave incorrectly.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083740
Stage 3: 108 → 109 - **CUDA 12.4.1 driver requirement**: Linux minimum 550.54.15, Windows minimum 551.78.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083741
Apps fail to start with older drivers.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083742
NumPy 2.x**: Many breaking changes.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083743
On Windows, the default integer type changed from `int32` to `int64` — can cause silent correctness issues.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083744
Fabric ABI break**: Even if no source changes needed (no TokenC/PathC usage), all extensions including Fabric headers must recompile — `Token`/`Path` became trivially copyable, which is a binary ABI change.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083745
Use `token.isNull()` instead of `kUninitializedToken`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083746
mimalloc (Windows)**: Cross-DLL allocation/free pairs that cross a DLL boundary may now crash.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083747
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083748
mergeMaterials**: Default changed — can cause significant load time regression with no code error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083749
FSD default on**: If previously disabled FSD, test render output carefully.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083750
DomeLight orientation**: USD 25.05 changed the default orientation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083751
Visual change only — no code error.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083752
Use `UpgradeUsdLuxLightsCommand` for assisted migration.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083753
Stage 4: 109 → 110 - **Clear extscache first** — stale Kit 109 entries cause exit-55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083754
Silent extension removals**: `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.d3d12`, `omni.hydra.iray.shadercache.vulkan`, `omni.kit.viewport.iray` — all removed with no deprecation notice.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083755
First symptom is a cryptic exit-55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083756
Remove every reference from `.kit`/`extension.toml` files — including the auto-generated `[settings.app.exts] enabled = [...]` version-lock block, where they usually hide pinned at the old version (clearing extscache alone won't drop them; regenerate the lock with `precache_exts` — see Step 5, item 5 in `apply-fixes.md`).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083757
Also scan `templates/` and ETM lock files** — these are easily missed by `source/`-only scans.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083758
DomeLight orientation (inherited from Stage 3)**: If the project contains DomeLights and was not verified during a previous Stage 3 upgrade, the USD 25.05 orientation change is a permanent behavioral difference.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083759
Search with `grep -rn 'DomeLight' .
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083760
include='*.py' --include='*.usd'` and use `UpgradeUsdLuxLightsCommand` if scenes were not migrated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083761
`optional ` semantics**: `if(b)` now tests *presence*, not *value*.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083762
Code that previously worked may now be wrong silently.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083763
`g_carbClientName`**: Type changed to `zstring_view`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083764
Any direct string assignment or comparison breaks.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083765
Hydra 2 removed**: No migration path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083766
Hydra 1 (Storm) and RTX remain.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083767
OmniGraph bundle nodes**: Large set of bundle/attribute manipulation nodes deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083768
Deprecation warnings visible in editor from Kit 110.1+.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083769
`AttributeType` → `GetAttributeType`, `ArrayGetSize` → `ArrayLength`, `ExtractPrim` → `ReadPrim`, `GetAttributeNames` → `ReadPrimAttributes`, `InsertAttribute` → `WritePrimAttribute`.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083770
`BundleConstructor`, `RemoveAttribute`, `RenameAttribute` have no direct replacement — redesign graphs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083771
OpenUSD 25.11**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083772
Ndr/Sdr libraries consolidated — update include paths.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083773
VS2022 required** on Windows (was VS2019).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083774
New extensions in Kit 110**: `omni.grpc.lib`, `omni.protobuf.lib`, `omni.sensors.nv.*` (camera/lidar/radar/ultrasonic/ids/wpm), `omni.kit.xr.core` — available for use in Kit 110 apps.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 083775
[ {"id":"py-omniclient","versions":{"from":"106","to":"107"},"category":"Python API","severity":"breaking","title":"omni.client._omniclient removed","description":"Private internal API removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083776
Use public omni.client API.","search_patterns":["omni\\.client\\._omniclient"],"file_types":[".py"],"fix":{"type":"regex_replace","description":"Replace import","from_pattern":"import omni\\.client\\._omniclient","to_pattern":"import omni.client"}}, {"id":"py-311","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"Python 3.10 → 3.11","description":"Python upgraded.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083777
Audit f-strings, typing module usage, and third-party packages for 3.11 compatibility.","search_patterns":["python3\\.10","python310"],"file_types":[".toml",".py",".sh",".bat",".lua"],"fix":{"type":"manual","description":"Update Python references to 3.11"}}, {"id":"cpp-abi-cxx11","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Linux: _GLIBCXX_USE_CXX11_ABI=1","description":"Native packages now use new C++ ABI.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083778
Rebuild all .so plugins.","search_patterns":["_GLIBCXX_USE_CXX11_ABI"],"file_types":[".cpp",".cmake",".toml"],"fix":{"type":"manual","description":"Rebuild all native plugins against new ABI"}}, {"id":"packman-abi-token","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"packman XML: ${platform_target} → ${platform_target_abi}","description":"Native packages now use ABI-variant tokens.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083779
Python payload access changed from e.payload['key'] to e['key'].
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083780
Subscribe via carb.eventdispatcher.get_eventdispatcher().observe_event().
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083781
C++: update to carb::eventdispatcher.","search_patterns":["e\\.payload\\[","carb\\.events\\.acquire_event_queue","create_subscription_to_pop"],"file_types":[".py",".cpp",".h"],"fix":{"type":"manual","description":"Update event subscriptions and payload access to Events 2.0 pattern.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083782
Remove explicit event pump calls."}}, {"id":"fabric-pathc-tokenc-intro","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Fabric PathC/TokenC introduced (removed in 109)","description":"Kit 107 introduced PathC/TokenC.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083783
Kit 109 removes them.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083784
Update Premake configs, CI, and build scripts.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083785
Audit all third-party packages for 3.12 compatibility.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083786
Use getCachedInterface.","search_patterns":["acquireInterface"],"file_types":[".cpp",".h"],"fix":{"type":"regex_replace","from_pattern":"carb::Framework::acquireInterface","to_pattern":"carb::getCachedInterface"}}, {"id":"omnigraph-3.0","versions":{"from":"107","to":"108"},"category":"C++ ABI","severity":"breaking","title":"omni.graph.core 3.0.0 ABI break","description":"Binary incompatible with 2.x.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083787
Recompile all OmniGraph nodes.","search_patterns":["omni\\.graph\\.core","omni\\.graph\\.nodes"],"file_types":[".toml"],"fix":{"type":"manual","description":"Recompile against omni.graph.core 3.0.0.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083788
Align omni.graph.nodes version."}}, {"id":"parallel-node-reg","versions":{"from":"107","to":"108"},"category":"Extension","severity":"breaking","title":"Parallel OmniGraph node registration removed","description":"Extension manager is not thread-safe.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083789
[ {"setting":"packman XML ABI token","versions":{"from":"106","to":"107"},"old_value":"${platform_target}","new_value":"${platform_target_abi}","file":"*.packman.xml","path":"package name attributes","notes":"Native packages now use ABI-variant package names.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083790
The deps directory location varies by release and project type (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083791
deps/ at the project root in one release, under tools/ in another, even between point releases of the same major line).
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083792
Do NOT assume tools/deps/ and do NOT rewrite paths from old_value to new_value -- detect the actual location (SKILL.md Step 1, $DEPS_DIR)."} ]
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 083793
{ "description": "The build toolchain a Kit project must keep in sync with its kit-kernel pin.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083794
SKILL.md Step 2.5 makes updating it a first-class step.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083795
Do NOT hardcode versions here — they move per branch; read the target branch's actual pins at upgrade time.", "toolchain_files": [ {"file": " /kit-sdk.packman.xml", "holds": "kit-kernel pin (the Kit SDK itself)", "notes": "DEPS_DIR is tools/deps/ or root deps/ — detect it (SKILL.md Step 1)."}, {"file": " /repo-deps.packman.xml", "holds": "the repo_* build tools + template-content packages", "notes": "The main toolchain file.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083796
Add or remove packages that appear/disappear between lines (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083797
repo_nspect is present on feature/main but not on production/110.1 or feature/110.3).", "reference_source": "omniverse/kit-apps/kit-sdk-public (and/or omniverse/kit-github/kit-app-template) on the matching branch.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083798
Prefer production/ over feature/ for a stable upgrade.", "critical_note": "Toolchain versions track the BRANCH's maintenance cadence, NOT the kernel line number.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083799
A newer kernel line can carry an OLDER toolchain.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083800
Never infer tool versions from the Kit version — read the actual target-branch pins.", "example_only_do_not_copy": { "note": "Illustrative snapshot read from kit-sdk-public in 2026 — WILL go stale.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083801
Always re-read the target branch at upgrade time.", "feature/main": {"kit-kernel": "110.4.0+feature", "repo_man": "2.6.4", "repo_build": "1.30.0", "repo_kit_tools": "1.20.3"}, "production/110.1": {"kit-kernel": "110.1.3+production", "repo_man": "2.9.3", "repo_build": "1.34.3", "repo_kit_tools": "1.21.2"} } } }
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 083802
[ { "extension": "omni.kvdb", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083803
Causes exit code 55 dependency solver failure.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083804
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.localcache", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083805
Same failure class as omni.kvdb.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083806
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.genproc.core", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083807
Migrate procedural generation workflows.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083808
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.kit.extpath.git", "status": "removed", "version": "108", "replacement": null, "search_in": [ "extension.toml" ], "notes": "Git URL extension search path.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083809
Was deprecated in 107." }, { "extension": "omni.hydra.iray.shadercache.d3d12", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083810
No explicit removal notice." }, { "extension": "omni.hydra.iray.shadercache.vulkan", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083811
No explicit removal notice." }, { "extension": "omni.kit.viewport.iray", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Was Sample in Kit 107.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083812
No version recorded in official docs." }, { "extension": "omni.hydra.scene_api", "status": "deprecated", "version": "108", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated since Kit 108.0.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083813
Removal pending." }, { "extension": "omni.surface_instancer", "status": "deprecated", "version": "pre-106", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Confirmed deprecated.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083814
Active customer confusion." }, { "extension": "omni.renderer_capture", "status": "deprecated", "version": "110", "replacement": "omni.kit.capture", "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated in Kit 110." }, { "extension": "omni.kit.widget.nucleus_connector", "status": "deprecated", "version": "110", "replacement": "omni.kit.widget.connection_manager", "search_in": [ "extension.toml", ".kit" ], "notes": "Compatibility shim.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083815
Will be removed." }, { "extension": "omni.kit.viewport.legacy_gizmos", "status": "deprecated", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Deprecated in Kit 110.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083816
Still operational but emits deprecation warnings.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083817
Commonly appears in both source/apps/ and templates/ .kit files — scan the full project root.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083818
No direct replacement announced; plan migration away from legacy gizmos rendering path." }, { "extension": "omni.kit.livestream", "status": "removed", "version": "108", "replacement": "omni.kit.livestream.app + omni.kit.livestream.aov + omni.kit.livestream.core", "search_in": [ "extension.toml", ".kit" ], "notes": "Monolithic livestream extension split into focused modules in Kit 108.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083819
Replace with the three new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083820
Settings paths also changed \u2014 see config_changes.json." }, { "extension": "omni.services.livestream.nvcf", "status": "removed", "version": "108", "replacement": "omni.services.livestream.session", "search_in": [ "extension.toml", ".kit" ], "notes": "Session management extension renamed in Kit 108.
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083821
Replace dependency declaration and update any code referencing the old extension name." } ]
स्रोत: NVIDIA-Omniverse/kit-app-template:.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 083822
tomlkit==0.12.2 ; python_version >= "3.10" and python_version < "4.0" \ --hash=sha256:df32fab589a81f0d7dc525a4267b6d7a64ee99619cbd1eeb0fae32c1dd426977 \ --hash=sha256:eeea7ac7563faeab0a1ed8fe12c2e5a51c61f933f2502f7e9db0241a65163ad0
स्रोत: NVIDIA-Omniverse/kit-app-template:tools/repoman/requirements.txt · स्वतंत्र परीक्षण अपेक्षित।

## 083823
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083824
All rights reserved.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083825
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083826
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083827
name: Feature Request description: Suggest an idea for this project title: "[FEATURE]: " labels: ["feature request"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this feature request!
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083828
type: textarea id: description attributes: label: Description description: | Describe the proposed feature placeholder: | Feature description and problem or pain point being addressed validations: required: true - type: textarea id: use_case attributes: label: Use Case or Scenarios description: Describe how this feature would be used placeholder: e.g., User performing action A, would accomplish B, with benefit C.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083829
type: textarea id: implementation_ideas attributes: label: Possible Implementation Ideas description: If you have any suggestions on how this feature might be implemented, please share them here.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083830
placeholder: Implementation ideas - type: textarea id: additional_context attributes: label: Additional Context or Recommendations description: Provide any other context or recommendations here.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083831
placeholder: Any other relevant information.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083832
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083833
All rights reserved.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083834
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083835
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083836
name: Bug Report description: File a bug report for the repository title: "[BUG]: " labels: ["bug"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this bug report!
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083837
type: textarea id: description attributes: label: Description description: | Describe the bug in detail placeholder: | Expected Behavior vs.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083838
Actual Behavior: validations: required: true - type: textarea id: component attributes: label: Component description: Which component (Tool/Template/Extension) is showing the bug?
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083839
placeholder: "e.g., Kit Base Editor Template / repo launch tool / Kit SDK" - type: textarea id: system-details attributes: label: System Details description: | Provide details about your system placeholder: | OS / CPU / GPU / GPU Driver Version validations: required: true - type: textarea id: reproduction-steps attributes: label: Reproduction Steps description: What are the steps to reproduce the bug?
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083840
validations: required: true - type: textarea id: logs attributes: label: Logs description: | Include the relevant log files: - **repo.log:** Found in `_repo/repo.log` if the issue is with tooling.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083841
kit.log:** Found in `_build/{OS}/release/logs/.../kit_{...}log` if the issue is with App, Extension, or Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083842
placeholder: Paste the log content here or attach the log files.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083843
type: textarea id: additional-context attributes: label: Additional Context description: Provide any other context or information here.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083844
placeholder: Any other information that might be helpful
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083845
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083846
All rights reserved.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083847
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083848
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083849
name: Question description: Ask a question title: "[QUESTION]: " labels: ["question"] body: - type: markdown attributes: value: | Thanks for taking the time to ask us a question!
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083850
type: textarea id: text_of_question attributes: label: Question description: Ask your question.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083851
placeholder: "Question text" validations: required: true - type: textarea id: additional_context attributes: label: Additional Context description: Provide any related code, issues, or projects.
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083852
placeholder: "Any related code, issues, or projects."
स्रोत: NVIDIA-Omniverse/kit-app-template:.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 083853
Data Collection & Use ## Overview NVIDIA Omniverse Kit Application Template collects anonymous usage data to help improve software performance and aid in diagnostic purposes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 083854
Rest assured, no personal information such as user email, name or any other PII field is collected.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 083855
Purpose Omniverse Kit Application Template starts collecting data when you begin interaction with our provided software.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 083856
After creating an application with the `template new` tooling, go to the `source/apps` directory 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 083857
Locate the `.kit` file for the application you want to disable telemetry for.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 083858
Find the following section in the `.kit` file: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = true ``` 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 083859
Change `enableAnonymousData` to `false`: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = false ``` Disabling telemetry stops data collection from your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 083860
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083861
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083862
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083863
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083864
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083865
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083866
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083867
What Are Application Layers?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083868
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083869
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083870
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083871
``` Answer `yes` to enable streaming for your application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083872
You can then pick from the following streaming layers: ```bash ?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083873
Do you want to add application layers?
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083874
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083875
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083876
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083877
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083878
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083879
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083880
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083881
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083882
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083883
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083884
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083885
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083886
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 083887
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083888
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083889
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083890
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083891
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083892
Select the desired UI based application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083893
The developer bundle is not currently suitable for headless services.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083894
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083895
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083896
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083897
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083898
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083899
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083900
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083901
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083902
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083903
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083904
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083905
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083906
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083907
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083908
Testing Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is an extension — including the `.kit` files that define applications.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083909
The `test` tool (`repo_test`) reflects this: it validates that your applications start up and shut down cleanly, and it runs the automated tests defined within your extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083910
Each extension template provided by the `kit-app-template` repository ships with sample tests that you can expand to grow your coverage.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083911
This document covers running tests, understanding what is tested, and adding your own tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083912
Prerequisites: Build Before You Test The test tool runs against the contents of the `_build` directory, so a successful build must precede any test run.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083913
If you have changed source since your last build, rebuild first.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083914
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` > **Note:** Tests run against a specific build configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083915
By default the tooling builds and tests the `release` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083916
If you build `debug`, pass the matching `--config debug` flag when testing.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083917
Running Tests ### Run the Default Test Suite Running `test` with no arguments executes the repository's default test suite (`alltests`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083918
The tool discovers every test-enabled extension in the build, launches each within the Kit test harness, and reports the aggregated results.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083919
Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` For each test-enabled extension — and each application `.kit` file — the tool starts a dedicated Kit process, loads the extension along with its test dependencies, runs the tests, and verifies a clean shutdown.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083920
Listing Tests Without Running Them Use `--list` (`-l`) to enumerate the tests that would run without executing them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083921
This is useful for confirming that a newly added extension or test is being discovered.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083922
Linux:** ```bash ./repo.sh test --list ``` **Windows:** ```powershell .\repo.bat test --list ``` ### Running a Subset of Tests Use `--filter-files` (`-f`) to narrow a run to specific test files, modules, classes, or individual tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083923
This shortens the feedback loop while iterating on a single extension.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083924
Linux:** ```bash ./repo.sh test -f my_company.my_extension ``` **Windows:** ```powershell .\repo.bat test -f my_company.my_extension ``` > **Note:** The accepted `--filter-files` format depends on the underlying test executor.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083925
For the Python (`omni.kit.test` / `unittest`) tests used by the extension templates, you may specify modules, classes, or individual tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083926
Run `./repo.sh test -h` for the full description.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083927
Selecting a Build Configuration By default the test tool targets the `release` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083928
To test a `debug` build, pass `--config` (`-c`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083929
The configuration must match the one you built.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083930
Linux:** ```bash ./repo.sh test --config debug ``` **Windows:** ```powershell .\repo.bat test --config debug ``` ### Other Useful Options | Option | Purpose | |--------|---------| | `-s, --suite` | Select which test suite(s) to run (default: `alltests`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083931
| | `-f, --filter-files` | Run only tests matching a file/module/class/test pattern.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083932
| | `-l, --list` | List the discovered tests and exit without running them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083933
| | `-c, --config` | Test the `release` (default) or `debug` build configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083934
| | `-p, --from-package` | Test an application package instead of the local build (see *Testing a Packaged Application* below).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083935
| | `-e, --extra-arg` | Pass an additional argument through to the test process.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083936
| | `--coverage` | Produce a Python code-coverage report after the run (for supported suite types).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083937
| | `--generate-report` | Run the configured report-generation command, if one is set, after all tests complete.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083938
| For the complete, authoritative list of options, run: **Linux:** ```bash ./repo.sh test -h ``` **Windows:** ```powershell .\repo.bat test -h ``` --- ## What Gets Tested ### Application Startup and Shutdown Every application `.kit` file is validated to confirm it can start up and shut down without error.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083939
This catches broken dependencies and misconfiguration early — a large portion of application health is covered simply by verifying that the fully assembled set of extensions loads cleanly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083940
An application declares how it should be launched during testing through a `[[test]]` table in its `.kit` file.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083941
For example, the Kit Base Editor template includes: ```toml [[test]] args = [ "--/app/file/ignoreUnsavedOnExit=true" ] ``` The `args` are passed to the Kit process when the application is tested.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083942
Extensions opt into testing with a `[[test]]` table in their `extension.toml`, which may declare test-only dependencies and extra arguments: ```toml [[test]] dependencies = [ "omni.kit.ui_test", # UI testing helper, loaded only during tests ] args = [ ] ``` Dependencies listed here are loaded only for the test run — a convenient place to pull in helpers such as `omni.kit.ui_test` without adding them to your extension's runtime dependencies.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083943
Writing Tests Tests use `omni.kit.test`, Python's standard `unittest` module wrapped to support `async`/`await`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083944
Placing a test class derived from `omni.kit.test.AsyncTestCase` at the root of a module within your extension's `tests/` package makes it auto-discoverable — no registration step is required.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083945
Every extension template includes a `tests/` package with a sample test to build on.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083946
To add coverage, place additional `test_*.py` modules in the extension's `tests/` package and grow the assertions from there.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083947
Because tests are standard `unittest` cases, refer to the [Python `unittest` documentation]( for available assertion methods and patterns.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083948
Test Suites and Configuration The behavior of the test tool for this repository is configured under `[repo_test]` in the top-level `repo.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083949
The most relevant settings are the default suite and any per-suite exclusions: ```toml [repo_test] default_suite = "alltests" [repo_test.suites."alltests"] exclude = [ # Setup extension tests are exercised as part of application testing "tests-omni.usd_explorer.setup${shell_ext}", ] ``` - **`default_suite`** determines which suite runs when you invoke `test` without `--suite`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083950
.exclude`** removes specific test executables from a suite — useful when a set of tests is already covered elsewhere.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083951
Adjust these settings as your project grows to control exactly what the default `./repo.sh test` run covers.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083952
Testing a Packaged Application In addition to testing the local build, the tool can run the suite against a packaged application archive — useful for validating a package before distribution.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083953
Use `--from-package` (`-p`), which by default looks for an archive in `_build/packages`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083954
Linux:** ```bash ./repo.sh test --from-package ``` **Windows:** ```powershell .\repo.bat test --from-package ``` The archive pattern is configurable in `repo.toml`: ```toml [repo_test] # When running from a package, find the archive using this pattern: archive_pattern = "${root}/_build/packages/*.zip" ``` > **Note:** Package testing is intended for the "fat" package type, which already contains the Kit Kernel and all extensions, so no additional download is required to run the tests.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083955
See [Packaging An Application]( for how to create a package.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083956
Testing in Continuous Integration `repo test` is the same entry point used by automated pipelines, so tests you run locally behave consistently in CI.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083957
Keeping the sample tests passing — and expanding them as you add functionality — helps ensure your applications and extensions remain buildable, launchable, and correct as the project evolves.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083958
Additional Resources - [Packaging An Application]( - [Kit SDK Tooling Guide](kit_app_template_tooling_guide.md) - [Kit SDK Companion Tutorial]( - [Python `unittest` documentation](
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 083959
Kit SDK Tooling Guide This document provides an overview of the practical aspects of using the tooling provided in the `kit-app-template`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083960
Intended for users with a basic familiarity with command-line operations, this guide offers typical usage patterns and recommendations for effective tool use.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083961
For a complete list of options for a given tool, use the help command: `./repo.sh [tool] -h` or `.\repo.bat [tool] -h`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083962
Overview of Tools The `kit-app-template` repository includes several tools designed to streamline the development of applications and extensions within the Omniverse Kit SDK.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083963
Available Tools - `template` - `build` - `launch` - `test` - `package` Each tool plays a specific role in the development workflow: ## Template Tool **Command:** `./repo.sh template` or `.\repo.bat template` ### Purpose The template tool facilitates the initiation of new projects by generating scaffolds for applications or extensions based on predefined templates located in `/templates/templates.toml`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083964
Usage The template tool has three main commands: `list`, `new`, `replay`, `modify`.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083965
`list` Lists available templates without initiating the configuration wizard.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083966
Linux:** ```bash ./repo.sh template list ``` **Windows:** ```powershell .\repo.bat template list ``` #### `new` Creates new applications or extensions from templates with interactive prompts guiding you through various configuration choices.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083967
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` #### `replay` In cases where automation is required for CI pipelines or other scripted workflows, it is possible to record and replay the `template new` configuration.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083968
Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the Application `.kit` file you want to update.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083969
Next, select (using Space) the Template Layer(s) to add.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083970
After the operation completes, rebuild (`./repo.sh build` or `.\repo.bat build`) the project to pull in the new extensions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083971
What `template new` Modifies When creating applications, the template tool automatically updates build configuration files: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083972
`premake5.lua`** - Adds `define_app("appname.kit")` so the build system discovers your application 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083973
`repo.toml`** - Adds the app path to `repo_precache_exts.apps` so dependent extensions are pre-cached at build time 3.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083974
`source/rendered_template_metadata.json`** - Records which templates were rendered (enables `template modify` and `template list`) 4.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083975
Setup extension** (some templates) - Creates an extension in `source/extensions/` for application-specific initialization **Extensions** are automatically discovered by the Kit build system based on directory structure, so no build file modifications are needed.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083976
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083977
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083978
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083979
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083980
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083981
It includes all resources located in the `source/` directory.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083982
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083983
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083984
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083985
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083986
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083987
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083988
`-p` or `--package`:** *(Deprecated — will be removed in a future release.)* Launches a packaged application from a specified path.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083989
`repo launch` is intended as a developer tool; launching from a package archive does not serve a development workflow.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083990
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083991
See [Packaging An Application]( for details.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083992
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083993
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083994
Any flags added after `--` will be passed through to Kit directly.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083995
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083996
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083997
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083998
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 083999
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 084000
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: NVIDIA-Omniverse/kit-app-template:readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।
