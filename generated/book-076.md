# डिजिटल महाग्रंथ 076

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 075001
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075002
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075003
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075004
Args: object: The bound object to register.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075005
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075006
Args: object: The bound object to deregister.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075007
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075008
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075009
Return: The bound object if it exists, an empty object otherwise.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075010
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075011
Return: The id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075012
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075013
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075014
Return: The bound object that was created.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075015
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075016
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075017
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075018
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075019
Args: value_to_multiply: The value to multiply by.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075020
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075021
Return: The toggled bool value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075022
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075023
Args: value_to_append: The value to append.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075024
Return: The new string value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075025
)", py::arg("value_to_append")) /**/; } ```
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 075026
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 075027
Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075028
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075029
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075030
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075031
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075032
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075033
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075034
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075035
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075036
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075037
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075038
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 075039
Changelog The format is based on [Keep a Changelog]( ## [0.1.2] - 2026-05-11 ### Fixed - `makePrimsPickable` handler raised `UnboundLocalError` when the WebSocket payload was empty or missing the `paths` key, and the broad `except` then leaked the raw Python exception message (including internal variable names) to the streaming client.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 075040
The handler now initializes `paths` to an empty list before the conditional so an empty payload is a clean no-op, and unexpected exceptions are logged server-side via `carb.log_error` while only a generic error string is returned to the client (OMPE-90584, NVBug 6100326).
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 075041
Added - Regression test `test_make_prims_pickable_empty_payload` covering empty payload, missing-`paths` key, and explicit-empty-list cases.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 075042
[0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 075043
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075044
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075045
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075046
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075047
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075048
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075049
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075050
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075051
Collaborating on large-scale design projects in real-time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075052
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075053
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075054
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075055
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075056
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075057
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075058
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075059
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075060
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075061
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075062
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075063
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075064
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075065
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075066
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075067
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075068
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075069
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075070
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075071
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075072
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075073
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075074
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075075
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075076
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075077
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075078
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075079
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075080
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075081
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075082
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075083
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075084
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075085
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075086
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075087
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075088
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075089
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075090
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075091
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075092
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075093
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075094
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075095
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075096
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075097
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075098
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075099
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075100
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075101
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075102
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075103
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075104
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075105
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075106
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075107
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075108
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075109
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075110
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075111
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075112
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075113
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075114
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075115
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075116
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075117
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075118
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075119
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075120
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075121
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075122
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075123
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075124
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075125
:warning: **Important**: These layers are not standalone application templates.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075126
They must be used in conjunction with a base application template.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075127
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075128
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075129
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075130
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075131
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075132
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075133
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075134
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075135
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075136
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075137
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075138
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075139
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075140
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075141
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075142
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075143
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075144
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075145
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075146
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075147
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075148
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075149
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075150
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075151
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075152
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075153
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075154
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075155
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075156
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075157
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075158
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075159
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075160
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075161
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075162
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075163
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075164
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075165
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075166
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075167
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075168
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075169
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075170
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075171
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075172
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075173
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075174
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075175
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075176
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075177
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075178
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075179
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075180
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075181
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075182
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075183
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075184
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075185
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075186
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075187
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075188
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075189
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075190
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075191
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075192
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075193
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075194
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075195
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075196
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075197
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075198
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075199
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075200
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075201
If multiple container images exist, you will be
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075202
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075203
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075204
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075205
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075206
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075207
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075208
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075209
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075210
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075211
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075212
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075213
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075214
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075215
Subsequent extensions can be added to the .kit file manually.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075216
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075217
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075218
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075219
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075220
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075221
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075222
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075223
Setup Extension -> kit_service_setup* - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075224
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075225
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075226
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075227
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075228
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075229
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075230
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075231
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075232
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075233
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075234
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075235
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075236
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075237
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075238
When adapting an existing extension for a headless service, keep the service execution path limited to the dependencies it requires.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075239
Prefer separating reusable headless logic from UI, viewport, rendering, and other application-specific functionality.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075240
If separation is impractical, dependencies that the service can operate without may be declared optional, provided their imports and initialization are also guarded.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075241
See [Adapting Existing Extensions for Headless Services]( for guidance and examples.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075242
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075243
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075244
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075245
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075246
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075247
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075248
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075249
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075250
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075251
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075252
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075253
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075254
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075255
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075256
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075257
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075258
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075259
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075260
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075261
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075262
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075263
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075264
The base application `.kit` file should be used for containerization.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075265
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075266
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075267
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075268
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075269
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075270
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075271
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075272
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075273
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075274
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075275
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075276
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075277
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075278
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075279
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075280
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075281
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075282
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075283
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075284
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075285
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075286
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075287
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075288
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075289
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075290
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075291
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075292
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075293
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075294
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075295
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075296
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075297
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075298
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075299
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075300
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075301
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075302
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075303
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075304
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075305
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075306
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075307
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075308
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075309
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075310
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075311
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075312
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075313
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075314
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075315
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075316
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075317
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075318
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075319
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075320
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075321
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075322
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075323
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075324
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075325
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075326
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075327
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075328
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075329
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075330
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075331
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075332
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075333
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075334
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075335
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075336
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075337
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075338
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075339
During Application configuration, you will be prompted for information about these extensions.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075340
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075341
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075342
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075343
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075344
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075345
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075346
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075347
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075348
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075349
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075350
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075351
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075352
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075353
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075354
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075355
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075356
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075357
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075358
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075359
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075360
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075361
The USD Viewer template includes sample assets for this purpose.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075362
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075363
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075364
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075365
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075366
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075367
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075368
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075369
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075370
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075371
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075372
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075373
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075374
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075375
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075376
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075377
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075378
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075379
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075380
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075381
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075382
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075383
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075384
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075385
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075386
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075387
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075388
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075389
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075390
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075391
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075392
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075393
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075394
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075395
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075396
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075397
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075398
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075399
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075400
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075401
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075402
name: kit-upgrade description: "Scan and upgrade Omniverse Kit SDK projects between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075403
Analyzes project files, identifies breaking changes, deprecated APIs, and removed extensions specific to the customer's code.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075404
Provides a personalized upgrade plan with file:line references and auto-fix suggestions.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075405
Covers Kit 106→107→108→109→110." --- # Kit SDK Upgrade Skill Guide a developer through upgrading their Omniverse Kit project from one version to another.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075406
This skill is a lean workflow router.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075407
Steps 1 and 2 (detect the project, decide the migration path) are inline below** — they are always needed.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075408
The detail for the remaining steps (2.5–6) lives in `procedures/`, and the structured change data in `references/`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075409
Read each procedure file when the workflow sends you to it** — do not try to hold them all in context at once.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075410
When to Use - User asks to upgrade their Kit project/app/extension - User asks about Kit breaking changes or migration - User is hitting errors after changing their Kit SDK version - User has a broken build or runtime failure after a version bump --- ## Quick Orientation Pick the entry point that matches the request: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075411
First-time upgrade scan** → start at Step 1 below and follow the workflow in order.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075412
Already upgraded, now has a build/runtime error** → go straight to `procedures/failure-modes.md`, diagnose, then apply the relevant Stage's fixes from `procedures/stage-notes.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075413
Just wants a list of breaking changes** → do Step 1, then run the scans in `procedures/scan.md` for their migration path and present the report from `procedures/report.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075414
The `# Kit SDK Version:` comment in `.kit` files reflects the last lock-file regeneration and may differ from the pin during an in-progress upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075415
Version string format: `110.1.0+feature.${platform_target_abi}.${config}` - First number (110) = major Kit version **If no version pin is found:** Check git history (`git log --oneline -20 -- tools/deps/ deps/`) or ask the user what Kit version they are currently running.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075416
(Layout detection below has not run yet, so scope the log to both candidate deps locations.) ### Detect project layout and build system Kit projects do **not** all use the SDK template layout, and the layout can differ between releases and project types — for example, `deps/` may sit at the project **root** in one release and under **`tools/`** in another (even between two point releases of the same major line).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075417
Projects also frequently **wrap or integrate the Kit build system into their own tooling**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075418
Detect the layout and build entrypoint **once**, then reuse them everywhere below — **never assume `tools/deps/` or `./repo.sh`**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075419
deps directory (holds kit-sdk.packman.xml + repo-deps.packman.xml) if [ -f tools/deps/kit-sdk.packman.xml ]; then DEPS_DIR=tools/deps elif [ -f deps/kit-sdk.packman.xml ]; then DEPS_DIR=deps else f=$(find .
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075420
name kit-sdk.packman.xml -not -path './_*' | head -1); DEPS_DIR=${f:+$(dirname "$f")}; fi echo "DEPS_DIR=${DEPS_DIR:- }" # 2.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075421
build entrypoint — the standard repo wrapper, if present if [ -f ./repo.sh ]; then BUILD='./repo.sh' elif [ -f ./repo.bat ]; then BUILD='repo.bat' else BUILD=''; fi # empty => custom / integrated build (see below) echo "BUILD=${BUILD:- }" ``` **If `BUILD` is empty, the project uses a custom or integrated build system** (common — many customers embed the Kit build inside their own).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075422
Do **not** fabricate `./repo.sh` calls.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075423
Find the real build command (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or the project README) or ask the user how they build.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075424
The upgrade work below (kernel pin bump, **toolchain update**, lock regeneration) still applies — you just invoke it through the project's own entrypoint.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075425
Record it as `$BUILD`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075426
> **From here on (and in every procedure file), use `$DEPS_DIR` and `$BUILD` in every command.** Where a document still shows a literal `tools/deps/` or `./repo.sh`, substitute the detected values.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075427
> > **These are not guaranteed to persist across shells.** If you run each fenced block in a fresh subshell, `$DEPS_DIR`/`$BUILD` will be unset.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075428
So do **one** of: (a) textually replace `$DEPS_DIR` and `$BUILD` with the literal detected paths (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075429
`tools/deps`, `./repo.sh`) in every command you run, or (b) re-run the two detection blocks above at the top of each new shell session.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075430
Do **not** run a later block assuming the variables are still set.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075431
Step 2: Determine Migration Path Kit versions must be upgraded **in sequence**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075432
Kit 108 was never publicly released** — its changes are folded into the 107→109 path.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075433
When upgrading 107→109 you must still address Stage 2 (107→108) changes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075434
A **within-major** bump (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075435
`110.0 → 110.1`, `110.1.0 → 110.1.2`) or a **feature → production** branch transition is a *different, lighter* job — and it is the most common upgrade performed in practice.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075436
These rarely need the Stage code/API changes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075437
The real work is almost entirely **tooling and layout**: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075438
Update the build toolchain** (repo tools, packman, repo scripts) — see Step 2.5 (`procedures/toolchain.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075439
This is usually the substantive part.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075440
Re-detect the deps directory** — its location can differ between releases, even within the same major line (Step 1 already sets `$DEPS_DIR`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075441
Bump the kit-kernel pin** in `$DEPS_DIR/kit-sdk.packman.xml` (Step 5, item 2 — `procedures/apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075442
For a feature ↔ production transition only:** check the extension **registry URL** in the `.kit` files — the feature and production lines use different registries, so a feature→production move may need a registry swap (Step 5, item 3).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075443
A plain within-major bump on the same line usually does **not**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075444
Regenerate the extension version-lock** and do a **clean rebuild** (Step 5 items 1 & 8, then Step 6).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075445
> **⚠️ Do NOT run the whole of Step 5 for a within-major bump.** Step 5 (`procedures/apply-fixes.md`) is written for **major-boundary** crossings.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075446
Running them on a 110.1.0→110.1.2 bump would wrongly strip extensions or rewrite APIs that are perfectly valid on 110.1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075447
Only run the Step 3 code scans if the upgrade crosses a major boundary.** For a pure within-major or feature→production move, skip Step 3's per-stage API scans and go straight to Step 2.5 → Step 5 (items 1–3 & 8 only, as above) → Step 6.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075448
If you cross one or more major boundaries on the way, run Step 3 for each major boundary passed and the full Step 5.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075449
Steps 2.5–6: Execute the Upgrade Once the path is known, work through these in order.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075450
Read the linked procedure file and follow it**; each assumes Step 1 detection has run.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075451
Step 2.5 — Update the build toolchain** → `procedures/toolchain.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075452
Highest-impact step; run it **first**, before touching source.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075453
For a within-major bump this is usually the only substantive work.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075454
Step 3 — Scan the project** → `procedures/scan.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075455
Run only the stage scans for the major boundaries you cross.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075456
Skip entirely for a pure within-major bump.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075457
Step 4 — Generate the upgrade report** → `procedures/report.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075458
Present findings by severity with exact `file:line` references.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075459
Step 5 — Apply fixes** → `procedures/apply-fixes.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075460
Get user approval before modifying files.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075461
(Within-major: items 1, 2, 8 only — see Step 2 above.) - **Step 6 — Validate** → `procedures/validate.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075462
Clean rebuild, regenerate the version lock, run tests.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075463
Already upgraded and hitting a specific error?** Go to `procedures/failure-modes.md` — it maps common symptoms (exit-55, ABI undefined symbols, render diffs, build loops, custom-build/layout issues) to fixes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 075464
Kit SDK Upgrade Skill ## What This Is This repository contains an AI agent skill for upgrading Omniverse Kit SDK projects between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075465
The skill encodes the complete breaking-change catalog for the Kit 106→107→108→109→110 migration path — including removed extensions, deprecated APIs, C++ ABI breaks, Python runtime changes, and configuration updates — into a structured set of instructions and reference data that an AI agent can execute against a live project.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075466
The agent scans the project, produces a categorized report with exact `file:line` references, and suggests targeted fixes, including auto-fixable regex replacements where safe.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075467
Who It's For Kit extension and application developers who need to upgrade a project from one Kit SDK version to another.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075468
This includes developers working on kit-app-template-based applications, standalone extensions, and Isaac Sim integrations.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075469
The skill is particularly useful when upgrading across multiple versions at once (e.g., 107→110), where the number of breaking changes makes manual triage error-prone.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075470
What It Contains | File | Description | |------|-------------| | `SKILL.md` | Lean workflow router — loaded by the AI agent.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075471
Holds version/layout/build detection (Step 1) and the migration-path decision (Step 2), and points to the procedure files for everything else.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075472
| | `procedures/toolchain.md` | Step 2.5 — update the `repo_*` build toolchain (the highest-impact part of most upgrades).
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075473
| | `procedures/scan.md` | Step 3 — the full per-stage `grep` scan catalog for breaking changes, removed extensions, and config.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075474
| | `procedures/report.md` | Step 4 — the upgrade-report template.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075475
| | `procedures/apply-fixes.md` | Step 5 — ordered fix list, auto-fixable regex patterns, and manual-only changes.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075476
| | `procedures/validate.md` | Step 6 — clean-rebuild and validation commands.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075477
| | `procedures/failure-modes.md` | Symptom→fix diagnosis for projects that already upgraded and are erroring.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075478
| | `procedures/stage-notes.md` | Per-stage (106→107→…→110) breaking-change reference.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075479
| | `references/breaking_changes.json` | 80+ breaking changes with search patterns, affected versions, and recommended fixes.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075480
| | `references/removed_extensions.json` | Extensions removed or deprecated by Kit version, with replacement guidance and search targets.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075481
| | `references/api_replacements.json` | 1:1 API replacements that are safe to apply with regex find/replace.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075482
| | `references/config_changes.json` | Settings keys, registry URLs, and build config changes between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075483
| | `references/toolchain.json` | The build-toolchain file/package set (`repo_*` tools, packman, repo scripts) and how to find the correct target versions for a given Kit line.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075484
| | `install.sh` / `install.bat` | Copies the skill (SKILL.md + `procedures/` + `references/`) into an existing Kit project so it travels with the repo.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075485
| The skill uses **progressive disclosure**: `SKILL.md` stays small (a router the agent always loads) and each step's detail lives in a `procedures/*.md` file the agent reads only when the workflow sends it there.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075486
This keeps the entry file well under length limits and keeps irrelevant detail out of context.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075487
How to Use **Install into an existing project** (so the skill travels with the repo): ```bash ./install.sh /path/to/your-kit-project # copies into /.skills/kit-upgrade/ ./install.sh /path/to/your-kit-project .claude/skills # or the Claude Code skills layout ``` On Windows: `install.bat C:\path\to\your-kit-project`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075488
Then load the skill into any AI coding assistant that can read files and run shell commands, and point it at the project you want to upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075489
Claude Code:** ``` Read the skill at /path/to/kit-upgrade-skill/SKILL.md and the reference files in references/.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075490
Then scan /path/to/my-kit-project and generate an upgrade report for Kit 109 → 110.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075491
``` **Cursor / VS Code Copilot / other MCP clients:** Add `kit-upgrade-skill/` as a context directory or attach `SKILL.md` as a system prompt, then ask the agent to scan your project.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075492
Detect the current Kit SDK version, the deps-directory location (`tools/deps/` vs root `deps/`), and the build entrypoint (`./repo.sh` / `repo.bat` or a custom/integrated build) — never assuming the SDK template layout 2.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075493
Determine the migration path — including within-major (minor/patch) and feature↔production transitions, not just major-version stages 3.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075494
Update the build toolchain (`repo_*` tools, packman, repo scripts) to match the target Kit line — often the substantive part of an upgrade 4.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075495
Run targeted `grep` scans across the full project root (including `templates/`, launcher configs, and ETM lock files) for any major boundaries crossed 5.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075496
Generate a categorized report: breaking changes, behavioral changes, deprecated usage, and a "not affected" checklist 6.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075497
Suggest fixes — both auto-applicable regex replacements and manual changes requiring human judgment 7.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075498
Its changes are folded into the 107→109 path — Stage 2 must still be addressed when upgrading 107→109.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075499
Multi-version upgrades (e.g., 107→110) apply all intervening stages in sequence.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075500
How to Contribute **Add a new breaking change:** Add an entry to `references/breaking_changes.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075501
Each entry needs an `id`, `title`, `stage`, `search_pattern` (grep-compatible regex), `affected_files` (glob patterns), and `fix` description.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075502
If the fix is a safe 1:1 substitution, also add it to `references/api_replacements.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075503
Add a removed or deprecated extension:** Add an entry to `references/removed_extensions.json` with `extension`, `status` (`removed` or `deprecated`), `version`, `replacement` (or `null`), `search_in` (list of file extensions to scan), and `notes`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075504
Include any known failure mode (e.g., exit-55) and whether the extension appears in non-obvious locations like `templates/` or ETM lock files.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075505
Add a new Kit version (release):** edit the files that own each piece — the skill is split by concern: - `SKILL.md` — add the new row/stage to the **Step 2 migration-path table and Stage summary** (these stay in the router).
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075506
`procedures/scan.md` — add the new `# === Stage N ===` scan blocks.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075507
`procedures/stage-notes.md` — add the new per-stage breaking-change section.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075508
`procedures/apply-fixes.md` — add any new auto-fix regex patterns or fix-list items.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075509
`references/*.json` — add the corresponding structured entries.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075510
Follow the existing section structure in each file for consistency.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075511
Keep `SKILL.md` lean — detailed scan commands and stage notes belong in `procedures/`, not the router.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075512
Test your additions:** Apply the skill to a real project that exercises the new patterns.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075513
If the scan misses something or the fix guidance is wrong, document it and open a PR with both the issue description and the corresponding fix in the relevant `procedures/` or `references/` file.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075514
This skill was developed and validated against [kit-extension-explorer]( a Kit 110 application based on kit-app-template.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075515
See `test-report.md` for the full upgrade report from that validation run.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 075516
{ "description": "The build toolchain a Kit project must keep in sync with its kit-kernel pin.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075517
SKILL.md Step 2.5 makes updating it a first-class step.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075518
Do NOT hardcode versions here — they move per branch; read the target branch's actual pins at upgrade time.", "toolchain_files": [ {"file": " /kit-sdk.packman.xml", "holds": "kit-kernel pin (the Kit SDK itself)", "notes": "DEPS_DIR is tools/deps/ or root deps/ — detect it (SKILL.md Step 1)."}, {"file": " /repo-deps.packman.xml", "holds": "the repo_* build tools + template-content packages", "notes": "The main toolchain file.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075519
Add or remove packages that appear/disappear between lines (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075520
repo_nspect is present on feature/main but not on production/110.1 or feature/110.3).", "reference_source": "omniverse/kit-apps/kit-sdk-public (and/or omniverse/kit-github/kit-app-template) on the matching branch.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075521
Prefer production/ over feature/ for a stable upgrade.", "critical_note": "Toolchain versions track the BRANCH's maintenance cadence, NOT the kernel line number.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075522
A newer kernel line can carry an OLDER toolchain.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075523
Never infer tool versions from the Kit version — read the actual target-branch pins.", "example_only_do_not_copy": { "note": "Illustrative snapshot read from kit-sdk-public in 2026 — WILL go stale.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075524
Always re-read the target branch at upgrade time.", "feature/main": {"kit-kernel": "110.4.0+feature", "repo_man": "2.6.4", "repo_build": "1.30.0", "repo_kit_tools": "1.20.3"}, "production/110.1": {"kit-kernel": "110.1.3+production", "repo_man": "2.9.3", "repo_build": "1.34.3", "repo_kit_tools": "1.21.2"} } } }
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 075525
[ {"setting":"packman XML ABI token","versions":{"from":"106","to":"107"},"old_value":"${platform_target}","new_value":"${platform_target_abi}","file":"*.packman.xml","path":"package name attributes","notes":"Native packages now use ABI-variant package names.
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075526
The deps directory location varies by release and project type (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075527
deps/ at the project root in one release, under tools/ in another, even between point releases of the same major line).
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075528
Do NOT assume tools/deps/ and do NOT rewrite paths from old_value to new_value -- detect the actual location (SKILL.md Step 1, $DEPS_DIR)."} ]
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075529
[ { "extension": "omni.kvdb", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075530
Causes exit code 55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075531
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.localcache", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075532
Same failure class as omni.kvdb.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075533
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.genproc.core", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075534
Migrate procedural generation workflows.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075535
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.kit.extpath.git", "status": "removed", "version": "108", "replacement": null, "search_in": [ "extension.toml" ], "notes": "Git URL extension search path.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075536
Was deprecated in 107." }, { "extension": "omni.hydra.iray.shadercache.d3d12", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075537
No explicit removal notice." }, { "extension": "omni.hydra.iray.shadercache.vulkan", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075538
No explicit removal notice." }, { "extension": "omni.kit.viewport.iray", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Was Sample in Kit 107.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075539
No version recorded in official docs." }, { "extension": "omni.hydra.scene_api", "status": "deprecated", "version": "108", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated since Kit 108.0.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075540
Removal pending." }, { "extension": "omni.surface_instancer", "status": "deprecated", "version": "pre-106", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Confirmed deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075541
Active customer confusion." }, { "extension": "omni.renderer_capture", "status": "deprecated", "version": "110", "replacement": "omni.kit.capture", "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated in Kit 110." }, { "extension": "omni.kit.widget.nucleus_connector", "status": "deprecated", "version": "110", "replacement": "omni.kit.widget.connection_manager", "search_in": [ "extension.toml", ".kit" ], "notes": "Compatibility shim.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075542
Will be removed." }, { "extension": "omni.kit.viewport.legacy_gizmos", "status": "deprecated", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Deprecated in Kit 110.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075543
Still operational but emits deprecation warnings.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075544
Commonly appears in both source/apps/ and templates/ .kit files — scan the full project root.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075545
No direct replacement announced; plan migration away from legacy gizmos rendering path." }, { "extension": "omni.kit.livestream", "status": "removed", "version": "108", "replacement": "omni.kit.livestream.app + omni.kit.livestream.aov + omni.kit.livestream.core", "search_in": [ "extension.toml", ".kit" ], "notes": "Monolithic livestream extension split into focused modules in Kit 108.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075546
Replace with the three new extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075547
Settings paths also changed \u2014 see config_changes.json." }, { "extension": "omni.services.livestream.nvcf", "status": "removed", "version": "108", "replacement": "omni.services.livestream.session", "search_in": [ "extension.toml", ".kit" ], "notes": "Session management extension renamed in Kit 108.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075548
Replace dependency declaration and update any code referencing the old extension name." } ]
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 075549
[ {"id":"py-omniclient","versions":{"from":"106","to":"107"},"category":"Python API","severity":"breaking","title":"omni.client._omniclient removed","description":"Private internal API removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075550
Use public omni.client API.","search_patterns":["omni\\.client\\._omniclient"],"file_types":[".py"],"fix":{"type":"regex_replace","description":"Replace import","from_pattern":"import omni\\.client\\._omniclient","to_pattern":"import omni.client"}}, {"id":"py-311","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"Python 3.10 → 3.11","description":"Python upgraded.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075551
Audit f-strings, typing module usage, and third-party packages for 3.11 compatibility.","search_patterns":["python3\\.10","python310"],"file_types":[".toml",".py",".sh",".bat",".lua"],"fix":{"type":"manual","description":"Update Python references to 3.11"}}, {"id":"cpp-abi-cxx11","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Linux: _GLIBCXX_USE_CXX11_ABI=1","description":"Native packages now use new C++ ABI.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075552
Rebuild all .so plugins.","search_patterns":["_GLIBCXX_USE_CXX11_ABI"],"file_types":[".cpp",".cmake",".toml"],"fix":{"type":"manual","description":"Rebuild all native plugins against new ABI"}}, {"id":"packman-abi-token","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"packman XML: ${platform_target} → ${platform_target_abi}","description":"Native packages now use ABI-variant tokens.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075553
Python payload access changed from e.payload['key'] to e['key'].
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075554
Subscribe via carb.eventdispatcher.get_eventdispatcher().observe_event().
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075555
C++: update to carb::eventdispatcher.","search_patterns":["e\\.payload\\[","carb\\.events\\.acquire_event_queue","create_subscription_to_pop"],"file_types":[".py",".cpp",".h"],"fix":{"type":"manual","description":"Update event subscriptions and payload access to Events 2.0 pattern.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075556
Remove explicit event pump calls."}}, {"id":"fabric-pathc-tokenc-intro","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Fabric PathC/TokenC introduced (removed in 109)","description":"Kit 107 introduced PathC/TokenC.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075557
Kit 109 removes them.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075558
Update Premake configs, CI, and build scripts.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075559
Audit all third-party packages for 3.12 compatibility.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075560
Use getCachedInterface.","search_patterns":["acquireInterface"],"file_types":[".cpp",".h"],"fix":{"type":"regex_replace","from_pattern":"carb::Framework::acquireInterface","to_pattern":"carb::getCachedInterface"}}, {"id":"omnigraph-3.0","versions":{"from":"107","to":"108"},"category":"C++ ABI","severity":"breaking","title":"omni.graph.core 3.0.0 ABI break","description":"Binary incompatible with 2.x.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075561
Recompile all OmniGraph nodes.","search_patterns":["omni\\.graph\\.core","omni\\.graph\\.nodes"],"file_types":[".toml"],"fix":{"type":"manual","description":"Recompile against omni.graph.core 3.0.0.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075562
Align omni.graph.nodes version."}}, {"id":"parallel-node-reg","versions":{"from":"107","to":"108"},"category":"Extension","severity":"breaking","title":"Parallel OmniGraph node registration removed","description":"Extension manager is not thread-safe.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 075563
Step 6: Validate > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 075564
Assumes Step 1 detection has run (`$BUILD` is set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 075565
```bash # After a kit-kernel pin bump, do a CLEAN rebuild so the kernel symlinks refresh, # then regenerate the version lock against the new kernel.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 075566
$BUILD is the entrypoint detected in Step 1 (./repo.sh, repo.bat, or the project's own build wrapper).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 075567
`No versions of > omni.anim.curve.core … = `).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 075568
Use **`$BUILD build --clean`** (removes the build-time `_*` > folders so the next `build -r` refreshes the symlinks) or **`$BUILD build --rebuild -r`** (clean + > release build in one command), then regenerate the lock with `build -u`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 075569
The generated `[settings.app.exts] > enabled = [...]` block in each `.kit` is what must be regenerated — it carries exact old-version pins that > `extscache` clearing does not touch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 075570
Failure Mode Diagnosis > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075571
Use this when the user has **already** upgraded and has a specific error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075572
`$DEPS_DIR` / `$BUILD` refer to the values detected in Step 1 (in `../SKILL.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075573
Exit Code 55 (Dependency Solver Failure) **Cause:** Removed extension still declared as a dependency, or stale extscache.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075574
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075575
Search for removed extension names in `.kit` and `extension.toml` files (see `../references/removed_extensions.json`) 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075576
For Kit 110: check for `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.*`, `omni.kit.viewport.iray` 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075577
Re-run `precache_exts` ### Build Fails with Undefined Symbol / Missing Method **Cause:** ABI break — extension was compiled against an older version.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075578
Fix:** Recompile the extension against the current Kit SDK.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075579
Every stage has at least one ABI break.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075580
Runtime Crash on DLL Load (Windows) **Cause after Stage 3:** mimalloc cross-DLL heap mismatch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075581
Memory allocated on one side of a DLL boundary freed on the other.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075582
Fix:** Audit allocation ownership.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075583
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075584
Python TypeError: unexpected keyword argument 'menu_compatibility' **Cause (Stage 4):** `menu_compatibility` parameter removed from `ui.Menu` and `ui.Separator`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075585
Fix:** Remove the `menu_compatibility=` argument from all call sites.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075586
Extension Loads But APIs Return None / AttributeError **Cause:** Transitive loading of `omni.kit.ui`, `omni.resourcemonitor`, or `omni.kit.manipulator.prim.fabric` was removed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075587
Fix:** Add explicit dependency in `extension.toml`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075588
Render Output Differs (No Code Changes) **Cause after Stage 3:** DomeLight orientation changed (USD 25.05), FSD enabled by default, or `mergeMaterials` default changed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075589
Diagnosis:** - Check for DomeLights in the scene: `grep -rn "DomeLight" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075590
include="*.usd" --include="*.usda"` - Check FSD setting: `grep -rn "FabricSceneDelegate\|fsd" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075591
include="*.kit" --include="*.toml"` - Check `mergeMaterials`: `grep -rn "mergeMaterials" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075592
include="*.kit" --include="*.toml"` ### if (optional_bool) No Longer Works (C++) **Cause (Stage 4):** `optional ` / `expected ` now tests for *presence* in an if-condition, not the stored value.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075593
Fix:** Replace `if (b)` with `if (b.has_value() && b.value())` ### Build Fails in a Loop / the Same Error Repeats **Cause:** Almost always a **stale toolchain** (Step 2.5 not applied — see `toolchain.md`) or a wrong assumption about the project's layout/build system — *not* the source code.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075594
Rule — do not keep editing source and rebuilding.** If the same build error recurs after **2 attempts**, STOP and re-check the fundamentals before changing any more code: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075595
Is the **toolchain** aligned to the target Kit line?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075596
(Step 2.5, `toolchain.md` — the #1 cause of build loops.) 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075597
Is `$DEPS_DIR` the **actual** deps location and `$BUILD` the project's **actual** build entrypoint?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075598
(Step 1 in `../SKILL.md`.) 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075599
Did you do a **clean** rebuild (`$BUILD build --rebuild -r`), not just clear extscache?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075600
(Step 6, `validate.md`.) Surface the exact error and these three checks to the user rather than looping — repeated speculative edits burn tokens and rarely fix a toolchain/layout problem.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075601
Project Uses a Custom / Integrated Build System **Cause:** The project wraps or embeds the Kit build system in its own tooling, so `./repo.sh` / `repo.bat` don't exist or aren't the real entrypoint (common for customer integrations).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075602
Fix:** Do **not** fabricate `./repo.sh` commands.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075603
Use the `$BUILD` detected in Step 1 (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or ask the user).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075604
The upgrade steps (kernel pin, **toolchain update**, lock regen) still apply — invoke them through `$BUILD`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075605
deps Directory Not Where Expected **Cause:** The project layout differs from the SDK template, or the deps directory moved between releases (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075606
`deps/` at the project root vs under `tools/`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075607
Fix:** Re-run the Step 1 detection (in `../SKILL.md`) to set `$DEPS_DIR`, then use it everywhere.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075608
Never hardcode `tools/deps/`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075609
Step 3: Scan the Project > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075610
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075611
Only run this step for major-version boundaries you cross** — a pure within-major / feature→production bump skips it.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075612
Run these commands from the project root.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075613
Only run scans for the stages that apply to this upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075614
Collect all matches before generating the report.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075615
> **⚠️ Scan scope:** Use `.` (project root) as the search root, not just `source/`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075616
Many projects have `templates/`, `launcher-configs/`, or other directories containing `.kit` files and `extension.toml` files with real dependency declarations.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075617
Scanning only `source/` will miss these.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075618
> > **Windows note:** Commands below use bash syntax.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075619
On Windows, replace `for` loops with individual `findstr` or PowerShell `Select-String` commands, or run inside WSL/Git Bash.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075620
Python / Extension Dependencies ```bash # === Stage 1 (106→107) === # Python 3.10 references (now 3.11) grep -rn "python3\.10\|python310\|boost_python310" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075621
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" --include="*.toml" # Private omni.client API grep -rn "omni\.client\._omniclient" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075622
include="*.py" # carb.imgui (removed — use omni.kit.imgui) grep -rn "carb\.imgui" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075623
include="*.py" # Events 1.0 patterns (payload access, subscription style) grep -rn "e\.payload\[" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075624
include="*.py" grep -rn "create_subscription_to_pop" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075625
include="*.py" # nv_usd references in build files grep -rn "nv_usd" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075626
premake5.lua repo.toml --include="*.lua" --include="*.toml" # packman XML using a pre-ABI token (should be ${platform_target_abi}).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075627
NOTE: match BOTH the old ${platform} form (Kit 106) and the intermediate ${platform_target} form — # the narrower 'platform_target[^_]' pattern misses ${platform}, which is what 106.5 actually uses and # is a build-verified hard failure on 106->107 (kit-kernel pull: "Package not found ...gl.linux-x86_64").
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075628
grep -rnE '\$\{platform(_target)?\}' "$DEPS_DIR" --include="*.xml" # Toolbar deprecated APIs grep -rn "omni\.kit\.widget\.toolbar\|omni\.kit\.window\.toolbar" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075629
include="*.py" --include="*.toml" # === Stage 2 (107→108) === # Python 3.11 references (now 3.12) grep -rn "python3\.11\|python311\|boost_python311" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075630
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" # get_custom_glyph_code (moved to omni.ui) grep -rn "omni\.kit\.ui.*get_custom_glyph_code" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075631
include="*.py" # WindowHandle deprecated usage grep -rn "WindowHandle" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075632
include="*.py" # menu_compatibility (deprecated in 108, removed in 110) grep -rn "menu_compatibility" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075633
include="*.py" # Layer events (Events 1.0 style) grep -rn "get_event_stream\|create_subscription_to_pop\|carb\.events" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075634
include="*.py" # Livestream extension (monolithic — should be split) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075635
include="*.kit" --include="*.toml" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075636
include="*.kit" --include="*.toml" # Livestream settings (old path) grep -rn "app/livestream\|app\.livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075637
include="*.kit" --include="*.toml" # Old omni.kit.ui transitive usage (no longer loaded transitively) grep -rn "omni\.kit\.ui[^.]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075638
include="*.py" # === Stage 3 (108→109) === # NumPy 1.x type aliases (removed in 2.0) grep -rn "np\.bool[^_]\|np\.int[^0-9_]\|np\.float[^0-9_]\|np\.complex[^0-9_]\|np\.object[^_]\|np\.str[^_]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075639
include="*.py" # === Stage 4 (109→110) === # menu_compatibility (now raises TypeError — must remove entirely) grep -rn "menu_compatibility=" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075640
include="*.py" # omni.usd layers deprecated API grep -rn "get_context()\.get_layers()\|context\.get_layers()" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075641
include="*.py" # omni.renderer_capture (deprecated → omni.kit.capture) grep -rn "omni\.renderer_capture" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075642
include="*.py" # USD displayName/displayGroup/hidden deprecated metadata grep -rn "GetMetadata.*displayName\|SetMetadata.*displayName\|GetMetadata.*hidden\|SetMetadata.*hidden\|GetMetadata.*displayGroup\|SetMetadata.*displayGroup" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075643
include="*.py" ``` ### C++ / Native Code ```bash # === Stage 1 (106→107) === # C++ ABI — check for _GLIBCXX_USE_CXX11_ABI overrides (must be =1) grep -rn "_GLIBCXX_USE_CXX11_ABI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075644
include="*.cpp" --include="*.h" --include="*.cmake" # === Stage 2 (107→108) === # ITokens::setValue (renamed to setValueS) grep -rn "->setValue(" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075645
include="*.cpp" --include="*.h" # carb::detail::defineTupleCommon grep -rn "carb::detail::defineTupleCommon" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075646
include="*.cpp" --include="*.h" # PyObjectVTable::get()->typeName grep -rn "PyObjectVTable" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075647
include="*.cpp" --include="*.h" # acquireInterface (prefer getCachedInterface) grep -rn "acquireInterface" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075648
include="*.cpp" --include="*.h" # carb::extras::Path implicit conversion grep -rn "carb::extras::Path\|carb::fs::Path" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075649
include="*.cpp" --include="*.h" # Assert macros (may need explicit carb/Assert.h now) grep -rn "CARB_ASSERT\|CARB_FATAL_UNLESS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075650
include="*.cpp" --include="*.h" # Library.h removed functions grep -rn "getDefaultLibraryPrefix\|getDefaultLibraryExtension" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075651
include="*.cpp" --include="*.h" # GfMatrix usage (imprecise overloads removed) grep -rn "GfMatrix" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075652
include="*.cpp" --include="*.h" # ILayers.h inclusion (ABI 1.0 → 1.1 recompile required) grep -rn "ILayers\.h\|omni/kit/usd/layers" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075653
include="*.cpp" --include="*.h" # carb.events const char* usage (deprecated — prefer string_view) grep -rn "carb::events::\|IEventQueue\|IEvents" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075654
include="*.cpp" --include="*.h" # Scalar xform ops — code that iterates over xform ops assuming vector types grep -rn "GetOrderedXformOps\|xformOp:translate\|xformOp:scale\|xformOp:rotate" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075655
include="*.cpp" --include="*.h" --include="*.py" # === Stage 3 (108→109) === # Fabric TokenC/PathC (removed; also kUninitializedToken/Path) grep -rn "TokenC\|PathC\|TokenId\|PathId\|kUninitializedToken\|kUninitializedPath" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075656
include="*.cpp" --include="*.h" # carb::cpp17 / carb::cpp20 (merged to carb::cpp) grep -rn "carb::cpp17\|carb::cpp20" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075657
include="*.cpp" --include="*.h" # carb::thread::shared_lock (removed) grep -rn "carb::thread::shared_lock" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075658
include="*.cpp" --include="*.h" # IDictionary::MakeAtPathS (renamed to MakeAtPath) grep -rn "MakeAtPathS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075659
include="*.cpp" --include="*.h" # compareStringsNoCase (renamed) grep -rn "compareStringsNoCase" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075660
include="*.cpp" --include="*.h" # Logger (superseded by Logger2) grep -rn "carb::logging::Logger[^2]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075661
include="*.cpp" --include="*.h" # MDL/Neuray usage (ABI 56 → 57 recompile required) grep -rn "omni\.mdl\|Neuray\|MDL.*SDK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075662
include="*.cpp" --include="*.h" --include="*.toml" # CloudXR / XRCloudXRBindings grep -rn "CloudXR\|XRCloudXRBindings\|IOpenXRRuntime" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075663
include="*.cpp" --include="*.h" # === Stage 4 (109→110) === # CARB_CHECK (replaced by CARB_RELEASE_ASSERT) grep -rn "CARB_CHECK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075664
include="*.cpp" --include="*.h" # carb/Defines.h (split into sub-headers) grep -rn '#include.*carb/Defines\.h' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075665
include="*.cpp" --include="*.h" # IFileSystem raw char* methods grep -rn "IFileSystem" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075666
include="*.cpp" --include="*.h" # ITokens (unsafe methods removed; ITokens 2.0 available) grep -rn "ITokens\|->resolveString\|->setValue" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075667
include="*.cpp" --include="*.h" # optional / expected — semantics changed (if(b) now tests presence) grep -rn "optional \|expected **Important:** Also scan `templates/`, `launcher-configs/`, and any ETM lock files (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075668
`omni.all.template.extensions.kit`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075669
These contain real dependency declarations and will cause test or runtime failures if they reference removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075670
```bash # === All stages — removed/deprecated extensions === # Kit 108 removals grep -rn "omni\.kit\.extpath\.git" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075671
include="*.toml" --include="*.kit" # Kit 108 — monolithic livestream (split into modules) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075672
include="*.toml" --include="*.kit" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075673
include="*.toml" --include="*.kit" # Kit 110 removals (cause cryptic exit-55 dependency solver failures) for ext in omni.kvdb omni.localcache omni.genproc.core; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075674
include="*.kit" --include="*.toml" done # Kit 110 silently removed (no deprecation notice) for ext in "omni.hydra.iray.shadercache.d3d12" "omni.hydra.iray.shadercache.vulkan" "omni.kit.viewport.iray"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075675
include="*.kit" --include="*.toml" done # Deprecated (not yet removed — still operational but plan migration) for ext in "omni.command.usd" "omni.debugdraw" "omni.hydra.iray" "omni.iray.settings.core" \ "omni.kit.autocapture" "omni.kit.manipulator.viewport" "omni.hydra.scene_api" \ "omni.renderer_capture" "omni.surface_instancer" "omni.kit.viewport.legacy_gizmos" \ "omni.kit.widget.nucleus_connector"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075676
include="*.kit" --include="*.toml" done # Extensions that need explicit declaration (no longer loaded transitively) grep -rn "omni\.kit\.manipulator\.prim\.fabric\|omni\.resourcemonitor\|omni\.kit\.ui" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075677
\ --include="*.py" --include="*.toml" ``` ### Config Files ```bash # Extension registry URLs (must update for Kit 110) grep -rn "kit-extensions\.ov\.nvidia\.com\|omniverse://" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075678
include="*.kit" # Build system (VS version) — also check CI-scoped token overrides # (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075679
"token:in_ci==true".vs_version may override the default even when the top-level is correct) grep -rn "vs_version\|vs2019\|vs2017\|v142" repo.toml # Livestream settings (old path style) grep -rn "app/livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075680
include="*.kit" --include="*.toml" # Kit SDK version pin (use the $DEPS_DIR detected in Step 1) cat "$DEPS_DIR/kit-sdk.packman.xml" # mergeMaterials (behavioral default change in 109) grep -rn "mergeMaterials" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075681
include="*.kit" --include="*.toml" # FSD / Fabric Scene Delegate settings grep -rn "FabricSceneDelegate\|fsd\b" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075682
include="*.kit" --include="*.toml" ``` ### OmniGraph ```bash # === Stage 2 (107→108) — OmniGraph 3.0 ABI === grep -rn "omni\.graph\.core\|omni\.graph\.nodes" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075683
include="*.toml" # === Stage 4 (109→110) — deprecated/removed OmniGraph nodes === # DeformedPointsToHydra — removed (was part of OmniHydra) grep -rn "DeformedPointsToHydra" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075684
include="*.py" --include="*.usd" --include="*.usda" # OnCustomEvent bundle attributes deprecated grep -rn "OnCustomEvent" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075685
include="*.py" --include="*.usd" --include="*.usda" # Bundle/attribute manipulation nodes deprecated grep -rn "ArrayGetSize\|AttributeType\|BundleConstructor\|CopyAttribute\|ExtractPrim\|GetAttributeNames\|HasAttribute\|InsertAttribute\|RemoveAttribute\|RenameAttribute" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075686
include="*.py" --include="*.usd" --include="*.usda" # Event/render pipeline nodes deprecated grep -rn "UpdateTickEvent\|GpuInteropCudaEntry\|RenderPreprocessEntry\|RpResourceExample" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075687
include="*.py" --include="*.usd" --include="*.usda" ``` ### Isaac Sim Projects If the project uses Isaac Sim extensions, scan for the `omni.isaac.*` namespace migration (applies Kit 107+): ```bash # omni.isaac.* imports (deprecated → isaacsim.*) grep -rn "omni\.isaac\." .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075688
include="*.py" --include="*.toml" --include="*.kit" # omni.replicator.isaac (→ isaacsim.replicator.*) grep -rn "omni\.replicator\.isaac" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075689
include="*.py" --include="*.toml" # Dynamic Control Toolbox (removed as compile-time dep) grep -rn "dynamic_control\|DynamicControl" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075690
include="*.py" --include="*.cpp" --include="*.h" # SemanticsAPI (→ UsdSemantics.LabelsAPI) grep -rn "add_update_semantics\|SemanticsAPI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 075691
Step 5: Apply Fixes > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075692
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075693
> **Within-major / feature→production upgrade?** Run **only items 1, 2, 8** below (plus item 3 *if* a feature↔production registry swap is needed), then Step 6 (`validate.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075694
Skip items 4–7** — they apply only when a major boundary is crossed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075695
See "Within-major upgrades" under Step 2 in `../SKILL.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075696
Get user approval before modifying files.** Then apply in this order (a full major-boundary upgrade runs all eight): 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075697
Clear extscache** first: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075698
Update version pin** in `$DEPS_DIR/kit-sdk.packman.xml` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075699
Update registry URLs** in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075700
Replace deprecated APIs** using patterns in `../references/api_replacements.json` — these are safe regex replacements 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075701
Remove deprecated extension deps** from `extension.toml` and `.kit` files (see `../references/removed_extensions.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075702
For 109→110 specifically:** the following six extensions are removed with **no deprecation notice**, and any lingering reference causes a cryptic `exit code 55` dependency-solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075703
They MUST be removed from every `.kit` (and `extension.toml`) file: - `omni.kvdb` - `omni.localcache` - `omni.genproc.core` - `omni.hydra.iray.shadercache.d3d12` - `omni.hydra.iray.shadercache.vulkan` - `omni.kit.viewport.iray` ⚠️ **Check the generated version-lock block, not just `[dependencies]`.** In application `.kit` files these names almost always appear in the auto-generated `[settings.app.exts] enabled = [...]` lock (pinned at the old version, e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075704
`omni.kvdb-109.0.10`), **not** the hand-authored dependency list.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075705
Clearing extscache (step 1) does NOT remove them** — you must regenerate the lock: delete the `# BEGIN GENERATED PART` … `# END GENERATED PART` block (the `.kit` says "Remove from 'BEGIN' to 'END' to regenerate") and run `$BUILD precache_exts -c release` so it is rebuilt without the removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075706
Then confirm a clean rebuild (the version stamp should advance to 110 and the six names should be gone).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075707
(If you are working in an internal `kit-app-template` checkout, the ETM lock file `templates/omni.all.template.extensions.kit` and any internal-registry entries are KAT-internal — wrapped in `# AUTOREMOVE` and stripped from external releases by `repo stage_for_github` — so external customer projects will not contain them.) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075708
Add explicit deps** where transitive loading was removed: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075709
Update build config** in `repo.toml` (VS version, MSVC version, Windows SDK — see `../references/config_changes.json`) 8.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075710
Step 2.5: Update the Build Toolchain (highest-impact — often the real work) > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075711
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075712
Run this **before** touching source code — for a within-major / feature→production bump it is usually the *only* substantive work.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075713
> **Key principle:** the most valuable part of an upgrade is usually **not** the code changes — it is making sure the project's **tooling** is correctly updated (repo scripts, `repo_man`/repoman, dependency versions).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075714
This step is therefore **first-class for every upgrade**, and the *primary* step for within-major / branch-transition bumps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075715
Run it **before** touching source code.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075716
Why it matters:** the Kit kernel pin and the repo toolchain are coupled.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075717
Bumping `kit-sdk.packman.xml` alone frequently fails because packman tokens (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075718
`${platform_target_abi}`) only resolve under the matching `repo_man`, and newer kernels expect newer `repo_build` / `repo_kit_tools`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075719
A pin bump *without* a toolchain bump produces cryptic pull/resolve failures — e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075720
`Package not found ...gl.linux-x86_64` or `No versions of … = `.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075721
The toolchain = these files** (see `../references/toolchain.json`): - `$DEPS_DIR/repo-deps.packman.xml` — the `repo_*` tools: `repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_tools_internal`, `repo_kit_template`, `repo_usd`, `repo_format`, `repo_test`, `repo_package`, `repo_ci`, etc.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075722
`$DEPS_DIR/kit-sdk.packman.xml` — the kit-kernel pin (updated in Step 5, item 2 — see `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075723
`tools/packman/` — the packman bootstrap (`packman`, `packman.cmd`, `bootstrap/`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075724
`repo.sh` / `repo.bat` — the repo wrappers (may need regenerating under a newer `repo_man`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075725
`repo.toml` — build config (VS/MSVC/WinSDK for Stage 4; see `../references/config_changes.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075726
How to find the correct target versions — do NOT guess:** 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075727
Get a **reference project already on the target Kit version** — the matching `kit-app-template` or `kit-sdk-public` branch for that Kit line, or the target Kit SDK release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075728
Read its `repo-deps.packman.xml`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075729
Prefer the `production/ ` branch** — it carries the vetted, most-current toolchain for that release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075730
⚠️ **Toolchain versions track the branch's maintenance cadence, not the kernel number** — a newer kernel line can ship an *older* toolchain (in kit-sdk-public, `feature/main` pins kernel 110.4 with `repo_man` 2.6.4, while the maintained `production/110.1` pins kernel 110.1.3 with a *newer* `repo_man` 2.9.3).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075731
Always read the target branch's **actual** pins; never assume "newer Kit = newer tools".
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075732
(Those version numbers are an illustrative snapshot read in 2026 — they **will** go stale; verify against the live branch, do not copy them.)* 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075733
Diff** the project's `$DEPS_DIR/repo-deps.packman.xml` against the reference and align each `repo_*` tool `version=` to the reference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075734
Do the same for `tools/packman/` if it differs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075735
Apply the versions, then do a **clean rebuild** (Step 6 — see `validate.md`) — the toolchain bump must land before the kernel pin resolves cleanly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075736
> This step is safe to run and validate (Step 6) **on its own, first**.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075737
Many "the upgrade won't build" error loops are nothing more than a stale toolchain — fixing it up front avoids chasing phantom code errors.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 075738
Step 4: Generate Upgrade Report > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075739
Run after the Step 3 scans (`scan.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075740
Present findings organized by severity.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075741
Use exact `file:line` references from scan output.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075742
``` ## Upgrade Report: Kit [FROM] → [TO] Project: [path] Migration stages applied: [e.g., Stage 2 + 3 + 4] ### ❌ Breaking Changes (must fix — build or load will fail) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075743
[file:line] — [description] → [exact fix] ### ⚠️ Behavioral Changes (no error, but may affect output or performance) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075744
[file:line] — [description] → [fix or test required] ### 🔔 Deprecated Usage (should fix — will break in next version) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075745
[file:line] — [description] → [fix] ### ✅ Not Affected - [List the `id` or `title` from `breaking_changes.json` for each pattern that was scanned and returned no matches.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075746
This serves as a record that the check was performed, not just skipped.] ### 📋 Required Steps Regardless of Code Changes 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075747
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075748
Update `kit-sdk.packman.xml`: change version pin to `[TO].x.y+feature.${platform_target_abi}.${config}` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075749
Update extension registry URLs in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075750
Rebuild all C++ extensions (ABI break at every stage — required even with no source changes) 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075751
Regenerate version lock blocks in `.kit` files: `$BUILD precache_exts -c release` (substitute the build entrypoint detected in Step 1 — `./repo.sh` may not exist on a custom/integrated build) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075752
If project has an ETM lock file (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075753
`omni.all.template.extensions.kit`), regenerate it or manually remove entries for removed extensions 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075754
[stage-specific items, e.g., VS2022 for Stage 4] ### 🧪 Behavioral Tests Required 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075755
[scenes with DomeLights — orientation regression (Stage 3, but inherited in all later stages)] 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075756
[load performance with mergeMaterials setting (Stage 3)] 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075757
[render output with FSD enabled (Stage 3)] 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075758
[MaterialX materials (Stage 4)] 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075759
[transform-heavy workflows after scalar xform ops change (Stage 2)] ``` **Prioritize for the user:** Extension removal errors and ABI rebuild requirements are the most common causes of project failures after a version bump.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 075760
Important Notes by Stage > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075761
Per-stage reference for the breaking changes summarized in the Step 2 migration table.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075762
Read the stages that apply to the boundaries you cross.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075763
Stage 1: 106 → 107 - **Rebuild required** — Linux ABI changed (`_GLIBCXX_USE_CXX11_ABI=0` → `=1`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075764
All prebuilt `.so` files will fail to load.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075765
packman XML token**: Update the kit-kernel pin token to `${platform_target_abi}` in all `.packman.xml` files.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075766
Kit 106 uses the **`${platform}`** form (not `${platform_target}`); both must become `${platform_target_abi}`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075767
Build-verified:* leaving the old token makes the kit-kernel pull fail immediately with `Package not found on specified remote servers (…gl.linux-x86_64.release)`, because Kit 107's kernel is published only under the ABI string (`manylinux_2_35_x86_64`), not `linux-x86_64`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075768
Bump the repo toolchain too (required, easy to miss)** — see **Step 2.5** (`toolchain.md`): the token fix alone is **insufficient** — `${platform_target_abi}` only resolves to the ABI string under the newer `repo_man`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075769
Update `$DEPS_DIR/repo-deps.packman.xml` to the 107-era tooling (`repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_template`, `repo_usd`) and the packman bootstrap.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075770
Build-verified:* under 106.5's `repo_man` 1.86.0 the token still resolves to `linux-x86_64`; after the toolchain bump it resolves to `manylinux_2_35_x86_64` and the pull succeeds.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075771
Carbonite Events 2.0**: The event system changed from push/pump to dispatch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075772
No explicit pump calls needed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075773
Python payload access changed from `e.payload['key']` to `e['key']`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075774
C++17 is now available** explicitly in Premake via `cppdialect = "C++17"`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075775
Stage 2: 107 → 108 - **Kit 108 was never publicly released.** These changes still apply when upgrading 107→109.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075776
Python 3.12** replaces 3.11.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075777
Update all Premake configs, CI configs, and boost_python links.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075778
OpenUSD 25.02**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075779
GfMatrix imprecise overloads removed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075780
Livestream modularization**: `omni.kit.livestream` (monolithic) → `omni.kit.livestream.app` + `.aov` + `.core`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075781
`omni.services.livestream.nvcf` → `omni.services.livestream.session`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075782
Settings paths changed — see `../references/config_changes.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075783
Transitive deps removed**: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` must now be declared explicitly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075784
ILayers ABI 1.0 → 1.1**: Recompile all extensions including `ILayers.h`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075785
USD scalar xform ops**: OpenUSD now supports scalar ops (e.g., `xformOp:translateX`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075786
Code iterating over xform ops that assumes all are vector types may behave incorrectly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075787
Stage 3: 108 → 109 - **CUDA 12.4.1 driver requirement**: Linux minimum 550.54.15, Windows minimum 551.78.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075788
Apps fail to start with older drivers.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075789
NumPy 2.x**: Many breaking changes.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075790
On Windows, the default integer type changed from `int32` to `int64` — can cause silent correctness issues.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075791
Fabric ABI break**: Even if no source changes needed (no TokenC/PathC usage), all extensions including Fabric headers must recompile — `Token`/`Path` became trivially copyable, which is a binary ABI change.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075792
Use `token.isNull()` instead of `kUninitializedToken`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075793
mimalloc (Windows)**: Cross-DLL allocation/free pairs that cross a DLL boundary may now crash.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075794
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075795
mergeMaterials**: Default changed — can cause significant load time regression with no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075796
FSD default on**: If previously disabled FSD, test render output carefully.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075797
DomeLight orientation**: USD 25.05 changed the default orientation.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075798
Visual change only — no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075799
Use `UpgradeUsdLuxLightsCommand` for assisted migration.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075800
Stage 4: 109 → 110 - **Clear extscache first** — stale Kit 109 entries cause exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075801
Silent extension removals**: `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.d3d12`, `omni.hydra.iray.shadercache.vulkan`, `omni.kit.viewport.iray` — all removed with no deprecation notice.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075802
First symptom is a cryptic exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075803
Remove every reference from `.kit`/`extension.toml` files — including the auto-generated `[settings.app.exts] enabled = [...]` version-lock block, where they usually hide pinned at the old version (clearing extscache alone won't drop them; regenerate the lock with `precache_exts` — see Step 5, item 5 in `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075804
Also scan `templates/` and ETM lock files** — these are easily missed by `source/`-only scans.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075805
DomeLight orientation (inherited from Stage 3)**: If the project contains DomeLights and was not verified during a previous Stage 3 upgrade, the USD 25.05 orientation change is a permanent behavioral difference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075806
Search with `grep -rn 'DomeLight' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075807
include='*.py' --include='*.usd'` and use `UpgradeUsdLuxLightsCommand` if scenes were not migrated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075808
`optional ` semantics**: `if(b)` now tests *presence*, not *value*.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075809
Code that previously worked may now be wrong silently.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075810
`g_carbClientName`**: Type changed to `zstring_view`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075811
Any direct string assignment or comparison breaks.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075812
Hydra 2 removed**: No migration path.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075813
Hydra 1 (Storm) and RTX remain.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075814
OmniGraph bundle nodes**: Large set of bundle/attribute manipulation nodes deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075815
Deprecation warnings visible in editor from Kit 110.1+.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075816
`AttributeType` → `GetAttributeType`, `ArrayGetSize` → `ArrayLength`, `ExtractPrim` → `ReadPrim`, `GetAttributeNames` → `ReadPrimAttributes`, `InsertAttribute` → `WritePrimAttribute`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075817
`BundleConstructor`, `RemoveAttribute`, `RenameAttribute` have no direct replacement — redesign graphs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075818
OpenUSD 25.11**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075819
Ndr/Sdr libraries consolidated — update include paths.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075820
VS2022 required** on Windows (was VS2019).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075821
New extensions in Kit 110**: `omni.grpc.lib`, `omni.protobuf.lib`, `omni.sensors.nv.*` (camera/lidar/radar/ultrasonic/ids/wpm), `omni.kit.xr.core` — available for use in Kit 110 apps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 075822
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075823
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075824
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075825
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075826
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075827
Select the desired UI based application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075828
The developer bundle is not currently suitable for headless services.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075829
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075830
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075831
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075832
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075833
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075834
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075835
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075836
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075837
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075838
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075839
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075840
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075841
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075842
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075843
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075844
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075845
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075846
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075847
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075848
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075849
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075850
What Are Application Layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075851
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075852
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075853
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075854
``` Answer `yes` to enable streaming for your application.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075855
You can then pick from the following streaming layers: ```bash ?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075856
Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075857
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075858
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075859
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075860
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075861
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075862
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075863
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075864
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075865
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075866
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075867
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075868
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075869
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 075870
Testing Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is an extension — including the `.kit` files that define applications.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075871
The `test` tool (`repo_test`) reflects this: it validates that your applications start up and shut down cleanly, and it runs the automated tests defined within your extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075872
Each extension template provided by the `kit-app-template` repository ships with sample tests that you can expand to grow your coverage.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075873
This document covers running tests, understanding what is tested, and adding your own tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075874
Prerequisites: Build Before You Test The test tool runs against the contents of the `_build` directory, so a successful build must precede any test run.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075875
If you have changed source since your last build, rebuild first.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075876
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` > **Note:** Tests run against a specific build configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075877
By default the tooling builds and tests the `release` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075878
If you build `debug`, pass the matching `--config debug` flag when testing.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075879
Running Tests ### Run the Default Test Suite Running `test` with no arguments executes the repository's default test suite (`alltests`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075880
The tool discovers every test-enabled extension in the build, launches each within the Kit test harness, and reports the aggregated results.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075881
Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` For each test-enabled extension — and each application `.kit` file — the tool starts a dedicated Kit process, loads the extension along with its test dependencies, runs the tests, and verifies a clean shutdown.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075882
Listing Tests Without Running Them Use `--list` (`-l`) to enumerate the tests that would run without executing them.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075883
This is useful for confirming that a newly added extension or test is being discovered.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075884
Linux:** ```bash ./repo.sh test --list ``` **Windows:** ```powershell .\repo.bat test --list ``` ### Running a Subset of Tests Use `--filter-files` (`-f`) to narrow a run to specific test files, modules, classes, or individual tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075885
This shortens the feedback loop while iterating on a single extension.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075886
Linux:** ```bash ./repo.sh test -f my_company.my_extension ``` **Windows:** ```powershell .\repo.bat test -f my_company.my_extension ``` > **Note:** The accepted `--filter-files` format depends on the underlying test executor.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075887
For the Python (`omni.kit.test` / `unittest`) tests used by the extension templates, you may specify modules, classes, or individual tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075888
Run `./repo.sh test -h` for the full description.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075889
Selecting a Build Configuration By default the test tool targets the `release` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075890
To test a `debug` build, pass `--config` (`-c`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075891
The configuration must match the one you built.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075892
Linux:** ```bash ./repo.sh test --config debug ``` **Windows:** ```powershell .\repo.bat test --config debug ``` ### Other Useful Options | Option | Purpose | |--------|---------| | `-s, --suite` | Select which test suite(s) to run (default: `alltests`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075893
| | `-f, --filter-files` | Run only tests matching a file/module/class/test pattern.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075894
| | `-l, --list` | List the discovered tests and exit without running them.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075895
| | `-c, --config` | Test the `release` (default) or `debug` build configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075896
| | `-p, --from-package` | Test an application package instead of the local build (see *Testing a Packaged Application* below).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075897
| | `-e, --extra-arg` | Pass an additional argument through to the test process.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075898
| | `--coverage` | Produce a Python code-coverage report after the run (for supported suite types).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075899
| | `--generate-report` | Run the configured report-generation command, if one is set, after all tests complete.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075900
| For the complete, authoritative list of options, run: **Linux:** ```bash ./repo.sh test -h ``` **Windows:** ```powershell .\repo.bat test -h ``` --- ## What Gets Tested ### Application Startup and Shutdown Every application `.kit` file is validated to confirm it can start up and shut down without error.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075901
This catches broken dependencies and misconfiguration early — a large portion of application health is covered simply by verifying that the fully assembled set of extensions loads cleanly.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075902
An application declares how it should be launched during testing through a `[[test]]` table in its `.kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075903
For example, the Kit Base Editor template includes: ```toml [[test]] args = [ "--/app/file/ignoreUnsavedOnExit=true" ] ``` The `args` are passed to the Kit process when the application is tested.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075904
Extensions opt into testing with a `[[test]]` table in their `extension.toml`, which may declare test-only dependencies and extra arguments: ```toml [[test]] dependencies = [ "omni.kit.ui_test", # UI testing helper, loaded only during tests ] args = [ ] ``` Dependencies listed here are loaded only for the test run — a convenient place to pull in helpers such as `omni.kit.ui_test` without adding them to your extension's runtime dependencies.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075905
Writing Tests Tests use `omni.kit.test`, Python's standard `unittest` module wrapped to support `async`/`await`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075906
Placing a test class derived from `omni.kit.test.AsyncTestCase` at the root of a module within your extension's `tests/` package makes it auto-discoverable — no registration step is required.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075907
Every extension template includes a `tests/` package with a sample test to build on.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075908
To add coverage, place additional `test_*.py` modules in the extension's `tests/` package and grow the assertions from there.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075909
Because tests are standard `unittest` cases, refer to the [Python `unittest` documentation]( for available assertion methods and patterns.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075910
Test Suites and Configuration The behavior of the test tool for this repository is configured under `[repo_test]` in the top-level `repo.toml`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075911
The most relevant settings are the default suite and any per-suite exclusions: ```toml [repo_test] default_suite = "alltests" [repo_test.suites."alltests"] exclude = [ # Setup extension tests are exercised as part of application testing "tests-omni.usd_explorer.setup${shell_ext}", ] ``` - **`default_suite`** determines which suite runs when you invoke `test` without `--suite`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075912
.exclude`** removes specific test executables from a suite — useful when a set of tests is already covered elsewhere.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075913
Adjust these settings as your project grows to control exactly what the default `./repo.sh test` run covers.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075914
Testing a Packaged Application In addition to testing the local build, the tool can run the suite against a packaged application archive — useful for validating a package before distribution.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075915
Use `--from-package` (`-p`), which by default looks for an archive in `_build/packages`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075916
Linux:** ```bash ./repo.sh test --from-package ``` **Windows:** ```powershell .\repo.bat test --from-package ``` The archive pattern is configurable in `repo.toml`: ```toml [repo_test] # When running from a package, find the archive using this pattern: archive_pattern = "${root}/_build/packages/*.zip" ``` > **Note:** Package testing is intended for the "fat" package type, which already contains the Kit Kernel and all extensions, so no additional download is required to run the tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075917
See [Packaging An Application]( for how to create a package.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075918
Testing in Continuous Integration `repo test` is the same entry point used by automated pipelines, so tests you run locally behave consistently in CI.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075919
Keeping the sample tests passing — and expanding them as you add functionality — helps ensure your applications and extensions remain buildable, launchable, and correct as the project evolves.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075920
Additional Resources - [Packaging An Application]( - [Kit SDK Tooling Guide](kit_app_template_tooling_guide.md) - [Kit SDK Companion Tutorial]( - [Python `unittest` documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 075921
Usage and Troubleshooting This section provides high-level information and guidance related to using the Kit App Template repository, along with troubleshooting tips for common issues.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075922
Usage Information ### A Project per Repository The `build` and `package` tooling provided in this repository is designed to capture all code and assets contained within the `/source` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075923
Each time the `template new` command is executed, a new application or extension is created within `/source`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075924
For purposes of experimentation and initial development, housing all working assets within the `/source` directory is reasonable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075925
However, as the project matures or requires deployment, it is recommended to segregate projects (typically a single `.kit` file and any required custom extensions) to minimize build times and reduce the size of the resultant package.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075926
Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is considered an extension.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075927
The `.kit` files that define applications are simply a convenient method to assemble and configure a set of extensions for specific functionalities, while extensions (and combinations thereof) can act as modular components fulfilling particular tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075928
For additional information on the Kit SDK and how to create applications and extensions, refer to the [Kit SDK Companion Tutorial]( ### Extendable Templates and Tools The templates and tools provided in this repository are designed to be extendable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075929
Templates Templates consist of a directory structure and boilerplate code containing variables configurable at the time the templates are applied.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075930
The `templates.toml` file, located in `templates/templates.toml`, specifies which templates the tooling recognizes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075931
Tooling Most tooling is not stored directly within the repository; it is instead downloaded from a remote registry upon the initial use of the tooling.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075932
This design allows the tooling to be updated independently of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075933
The framework used for the tooling also supports the definition of custom tools.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075934
To see this extensibility in action, explore the local tooling defined within `tools/repoman`, specifically the `launch` tool.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075935
Configuration for this tool within the repo is delineated in the `repo_tools.toml` file at the root of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075936
Troubleshooting This section outlines potential issues that may arise when using the Kit App Template repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075937
Setup & Configuration Issues #### Windows Long Path Due to path length limitations on Windows it is recommended to place repository artifacts in a location closer to the root of the drive.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075938
This will help avoid issues with the path lengths when building and packaging applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075939
exFAT Drive Compatibility Limitations The Kit App Template repository and associated tooling are designed to work with drive formats that support junctions/symlinks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075940
If you are using an exFAT-formatted drive, you may encounter errors during the build process.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075941
To resolve this issue, consider using a different drive format such as NTFS.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075942
Extension Naming Guidelines When creating custom extensions, avoid using a top-level namespace that is the same as any built-in Python module (e.g., “random”, “sys”, “xml”).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075943
Doing so can cause import conflicts if Omniverse Kit attempts to load extensions from these Python modules.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075944
For example, instead of “random.extension.name”, use a unique namespace such as “my_company.my_app.my_extension”.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075945
Rendering & Performance #### Initial Rendering Startup Times When launching an application that requires the RTX renderer, the first launch may take considerably longer than subsequent launches due to shader compilation.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075946
The initial launch can take between 5 to 8 minutes.** Subsequent launches of RTX-enabled applications will be faster as the renderer caches the compiled shaders.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075947
Build & Packaging #### Build Issues The `template new` tooling ensures that any created application is properly configured to build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075948
However, extensive manual changes can occasionally cause the configuration and `/source` directory contents to become unsynchronized.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075949
The specifics of any given build are determined by three main factors: 1) The state of the top-level `repo.toml` file, especially the `.kit` files listed in the `apps` array within the `[[repo_precache_exts]]` section.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075950
2) The state of the `premake5.lua` file, particularly which `.kit` files are set to build via `define_app()` (e.g., `define_app("my_company.my_service.kit")`).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075951
3) The state of the `source` directory, specifically which `.kit` files are present within `source/apps`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075952
To ensure a build proceeds as intended, verify that the same `.kit` files are listed or defined in all three locations.** For a clean build, use the command `./repo.sh build -c` or `.\repo.bat build -c` to clean the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075953
Caching and Persistent Data The Omniverse Kit SDK caches data and required dependencies to improve build and runtime performance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075954
If you encounter issues with stale, incorrect, or missing dependencies/data, consider clearing application specific and/or global cache locations: - **Application Specific Caches**: Clearing application specific caches and settings can be done by adding arguments at launch time.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075955
Linux: ```bash ./repo.sh launch -- --clear-cache --clear-data --reset-user ``` Windows: ```powershell .\repo.bat launch -- --clear-cache --clear-data --reset-user ``` Upon selecting a `.kit` file to launch, the application will clear the cache and data directories before starting.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075956
Global Cache Locations (:warning:Use with Caution:warning:)**: **IMPORTANT NOTE -** Clearing any of the following cache locations will require a full rebuild of any existing applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075957
Deleting the directories responsible for caching ensures a fresh build of the relevant caches during the next build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075958
Extension AND Application Data Cache Locations**: `$HOME/.local/share/ov` on Linux, `%LOCALAPPDATA%\ov` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075959
Tooling AND Dependency Cache Location**: - **Packman :** `$PM_PACKAGES_ROOT` on Linux, `%PM_PACKAGES_ROOT%` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075960
If `PM_PACKAGES_ROOT` is not set on your system, the default location will revert to `$HOME/.cache/packman` on Linux, `{drive where packman is launched from}\packman-repo` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075961
uv :** `$HOME/.cache/uv` on Linux, `%LOCALAPPDATA%\uv\cache` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075962
Space Constraints Due to Docker Artifacts When performing extensive local testing of container images created via `repo package_container`, Docker artifacts can accumulate over time, consuming significant disk space.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075963
`docker system df` can be used to determine disk space utilized by Docker objects.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075964
To reclaim space, consider the following options: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075965
Regular Safe Cleanup**: - **Command**: `docker container prune` - **Description**: This command removes all stopped containers, which is typically safe and helps manage disk space without affecting images, networks, or volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075966
Use**: Recommended for regular maintenance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075967
Extensive Cleanup (:warning:Use with Caution:warning:)**: - **Command**: `docker system prune` - **Description**: This command removes all unused containers, networks, images, and optionally volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075968
It is akin to running a `rm -rf` for Docker resources.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075969
Warning**: Use this command carefully, as it will remove many resources indiscriminately.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075970
Ensure you review and understand what will be deleted.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075971
For image-specific cleanup, use `docker images` to list all images and `docker rmi ` to manually remove those that are no longer needed.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 075972
Windows C++ Developer Configuration ## Introduction This document guides you through setting up this repository for C++ development on Windows using Microsoft Visual Studio and the Windows SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075973
For New Users:** If you are new to Windows C++ development, this guide provides a step-by-step installation of Visual Studio 2022 Community and the Windows SDK, ensuring you have all the components required for standard development tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075974
For Advanced Configurations:** If you already have Visual Studio and the Windows SDK installed but wish to specify exact versions, this guide will help you configure your environment using the `[repo_build.msbuild]` configuration within `repo.toml` at the project root.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075975
Configuration To enable the Windows C++ build process: - Set the `"platform:windows-x86_64".enabled` flag to `true` in your `repo.toml` file: ```toml [repo_build.build] "platform:windows-x86_64".enabled = true ``` - Set the `link_host_toolchain` flag to `true` in your `repo.toml` file: ```toml [repo_build.msbuild] link_host_toolchain = true ``` **Note:** If you already have Visual Studio and the Windows SDK installed, this might be the only change needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075976
The tooling will auto-detect installed components.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075977
Microsoft Visual Studio and Windows SDK Setup ### Basic Installation #### Installing Visual Studio 2022 Community 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075978
Download Visual Studio Installer** ![VS Download](../vs_download.png) - Visit the [Visual Studio Downloads]( - Click "Free download" under "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075979
Run the Installer** - Open the downloaded installer.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075980
Select "Community" edition and click "Install".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075981
Select Workloads** ![VS Workloads](../vs_workloads.png) - Check "Desktop development with C++".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075982
This includes tools like the MSVC compiler and C++ libraries.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075983
Additional Components** ![VS Additional](../vs_additional.png) - If you need specific components, go to "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075984
Select additional tools as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075985
Complete the Installation** - Proceed with the installation to download and set up all files.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075986
Installing Windows SDK (as needed) Usually, the Windows SDK is included with the "Desktop development with C++" workload.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075987
To verify or install it separately: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075988
Launch Visual Studio Installer** - Open the installer if it's not already running.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075989
Modify Installation** ![VS Modify](../vs_modify.png) - Click "Modify" on your Visual Studio installation.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075990
Verify Windows SDK** ![VS WinSDK Verify](../vs_winsdk_verify.png) - Ensure "Windows SDK" is selected under "Optional" sections or "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075991
Apply Changes** - Click "Modify" to install or update the SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075992
Configuring an Existing Installation #### Default Installation Paths If Visual Studio and the Windows SDK are installed in default locations, the build tooling will auto-detect them without additional configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075993
Note:** If the path entered is incorrect or invalid, the build system will fall back to auto-detection.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075994
Multiple Installations For multiple Visual Studio or Windows SDK installations, the latest version is used by default.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075995
If unspecified, default edition preference is "Enterprise", "Professional", "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075996
Additional Resources - [Repo Build Documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 075997
Data Collection & Use ## Overview NVIDIA Omniverse Kit Application Template collects anonymous usage data to help improve software performance and aid in diagnostic purposes.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 075998
Rest assured, no personal information such as user email, name or any other PII field is collected.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 075999
Purpose Omniverse Kit Application Template starts collecting data when you begin interaction with our provided software.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 076000
After creating an application with the `template new` tooling, go to the `source/apps` directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।
