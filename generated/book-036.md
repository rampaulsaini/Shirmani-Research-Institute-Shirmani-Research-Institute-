# डिजिटल महाग्रंथ 036

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 035001
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035002
Select desired template with arrow keys ↑↓:** Basic C++ Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035003
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035004
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035005
Enter version:** [set extension version] #### Build and Launch While C++ extensions do require compilation this is typically not done in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035006
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035007
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035008
Customization Customization of a C++ Extension might involve writing new C++ classes or functions, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035009
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035010
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035011
It should be noted that a limited number of registry extensions expose a C++ API**.
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035012
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`).
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035013
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_cpp/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035014
USD Viewer Setup Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Setup Extension Template is specifically designed to configure the USD Viewer Template application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035015
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Viewer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035016
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Viewer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035017
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035018
Key Features - Custom configurations tailored to the USD Viewer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035019
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035020
This extension does provide a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035021
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035022
Basic Python Extension Template ## Overview The Basic Python Extension Template is a starting point for developers looking to build Python-based extensions within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035023
This template offers a best practices foundation and structure to easily integrate with the broader capabilities of the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035024
Use Cases This template is ideal for developers looking to build: - A reusable Python extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035025
Key Features - Structure well suited for the build, test and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035026
All required setup code for use with the Omniverse Kit SDK.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035027
Usage This section provides instructions for the setup and use of the Basic Python Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035028
Getting Started To get started with the Basic Python Extension, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035029
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035030
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035031
Select desired template with arrow keys ↑↓:**: Basic Python Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035032
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035033
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035034
Enter version:** [set extension version] #### Build and Launch While Python extensions typically do not require a build step in isolation, this template is structured to properly interact with the Omniverse Kit SDK application build and packaging tooling.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035035
Launching the extension typically requires that they be a part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035036
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035037
Customization Customization of a Python Extension might involve writing new Python modules, or integrating existing libraries.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035038
As is the case with Applications, extensions can also depend on and be depended on by other extensions.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035039
These can be custom developed extensions or those provided by the NVIDIA managed extension registry.
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035040
A view of available registry extensions can be found within the Extension Manager accessible via the developer bundle (select `Developer` > `Utilities` > `Extensions`) ## Additional Learning - [Kit Manual Extension Docs]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/basic_python/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035041
C++ with Python Bindings Extension Template ## Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035042
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035043
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035044
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035045
For more details, see the [Windows Developer Configuration guide](../../../readme-assets/additional-docs/windows_developer_configuration.md).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035046
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035047
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035048
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035049
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035050
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035051
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035052
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035053
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035054
Usage This section details how to set up and use the C++ with Python Bindings Extension Template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035055
Getting Started Before you begin, ensure your development environment meets the prerequisites outlined in the [top-level README](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035056
Cloning the Repository Use the following steps to clone the repository locally: ```bash git clone cd kit-app-template ``` #### Create New Extension Use the provided script (either shell or PowerShell) to start a new extension from the template.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035057
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompts in your terminal: - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035058
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035059
Select desired template with arrow keys ↑↓:** Basic C++ w/ Python Binding Extension - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035060
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035061
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035062
Enter version:** [set extension version] #### Build and Launch While C++ extensions require a build step, this template is structured so that the build, test, and packaging processes are conveniently handled through the Omniverse Kit SDK’s application tooling.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035063
Python developers can then import the resulting module for a seamless C++-backed Python experience.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035064
Launching an extension typically requires that it be part of an Omniverse [Service](../../apps/kit_service/README.md) or [Editor](../../apps/kit_base_editor/README.md) application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035065
Adding an Extension to an Application** To add your extension to an application, declare it in the dependencies section of the application's `.kit` file: ```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After adding your new extension, re-run the build process for the application.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035066
This ensures your compiled C++ code and Python bindings are included in the final build artifacts.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035067
Customization Customization of this C++/Python Binding Extension may involve: - Extending or altering the C++ source files to incorporate new functionalities.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035068
Adjusting the Pybind11 binding code to expose additional methods, classes, or data structures to Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035069
Integrating other C++ or Python libraries as needed.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035070
As with any extension, dependencies can be declared on other custom or registry-based extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035071
Whether you need more specialized C++ libraries or Python packages, you can add them to your extension as desired.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035072
Note that only a limited number of registry extensions expose a C++ API, so validate your dependencies accordingly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035073
Additional Learning - [Kit Manual Extension Docs]( - [C++ Extension Examples]( - [Kit SDK Companion Tutorial]( - [Pybind11 Documentation](
स्रोत: kit-app-template/templates/extensions/basic_python_binding/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035074
USD Viewer Messaging Extension Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer Messaging Extension Template is specifically designed for the USD Viewer Application, a Viewport-only application that cleanly displays USD content with in-scene functionality.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035075
This messaging extension allows remote communication with the underlying Kit application to perform actions typically driven by in-app UI and menus found in other applications.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035076
:warning: Important:** While this extension exists alongside general extension templates, it is specifically tailored for the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035077
Use Cases This messaging extension is particularly useful for: - Remotely loading scenes in the USD Viewer Application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035078
Managing the state for selecting objects within the scene.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035079
Performing actions without traditional in-app UI and menus.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035080
Key Features - Remote communication with the Kit application.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035081
Scene loading capabilities.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035082
State management for object selection within the USD Viewer.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035083
Usage This extension is automatically created and configured when you generate a new application based on the [USD Viewer Template Application](../../apps/usd_viewer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035084
This extension serves as an example for developers to understand how remote communication and scene management can be implemented in applications using the Kit SDK.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035085
Additional Learning - [Kit Manual - Advanced Extensions](
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035086
USD Composer Setup Extension Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer Setup Extension Template is specifically designed to configure the USD Composer Template application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035087
This setup extension ensures the proper integration and configuration of specific components and extensions required for the USD Composer Template application to function as intended.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035088
Use Cases This setup extension is particularly useful for: - Customizing the setup and configuration of the USD Composer Application Template.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035089
Learning more (by example) about advanced usage of the Kit SDK and Omniverse Extensions.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035090
Key Features - Custom configurations tailored to the USD Composer Template Application.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035091
Usage This extension is automatically created and configured when you generate a new application based on the [USD Composer Template Application](../../apps/usd_composer/README.md).
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035092
This extension provides a learning opportunity for developers to understand how applications can be extensively customized and configured using a setup extension.
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035093
Additional Learning - [Kit Manual - Advanced Extensions]( - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/extensions/usd_composer.setup/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035094
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - 2024-03-13 - Initial version based on kit service extension template
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035095
{{ extension_display_name }} [{{ extension_name }}] This is an example of a simple Kit Service extension.
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035096
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/service.setup/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035097
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035098
{{ extension_display_name }} [{{ extension_name }}] A simple python UI extension example.
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035099
Use it as a starting point for your extensions.
स्रोत: kit-app-template/templates/extensions/python_ui/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035100
Changelog The format is based on [Keep a Changelog]( ## [1.0.32] - 2023-11-02 ### Changed - OMFP-3224: Added regression test - Added unit tests for state manager ## [1.0.31] - 2023-10-25 ### Changed - OMFP-3094: Restored Window/Viewport menu ## [1.0.30] - 2023-10-26 ### Changed - OMFP-2904: Show "Examples" by default in Layout mode ## [1.0.29] - 2023-10-25 ### Changed - OMFP-3224: Fix stage template light directions.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035101
[1.0.28] - 2023-10-23 ### Changed - OMFP-2654: Upgraded carb.imgui with omni.kit.imgui ## [1.0.27] - 2023-10-20 ### Changed - OMFP-2649: Missed the Layout item, it is now hidden as requested.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035102
[1.0.26] - 2023-10-20 ### Changed - Update embedded light rigs and textures ## [1.0.25] - 2023-10-19 ### Changed - Added regression test for OMFP-2304 ## [1.0.24] - 2023-10-19 ### Changed - OMFP-1981: always load the default layout when startup the app ## [1.0.23] - 2023-10-18 ### Changed - OMFP-2649: Hiding menu entries.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035103
[1.0.22] - 2023-10-18 ### Changed - Updated About dialog PNG to match the new application icon.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035104
[1.0.21] - 2023-10-18 ### Changed - OMFP-2737: Do no rebuild menu (change menu layout) if layout is same ## [1.0.20] - 2023-10-18 ### Changed - make windows invisible which are not desired to be in Review mode, OMFP-2252 activity progress window and OMFP-1981 scene optimizer window.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035105
OMFP-1981: when user switch between modes, make sure the user defined layout in Layout mode is kept.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035106
[1.0.13] - 2023-10-11 ### Changed - OMFP-2328: Fix "Sunnysky" oriented incorrectly ## [1.0.12] - 2023-10-10 ### Changed - OMFP-2226 - Remove second Viewport menu item from layouts.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035107
[1.0.11] - 2023-10-11 ### Changed - Added UI state manager.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035108
[1.0.10] - 2023-10-10 ### Changed - Deactivate tools when app mode is changed.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035109
[1.0.9] - 2023-10-09 ### Changed - OMFP-2200 - Disabling the viewport expansion, this should keep us locked to a 16:9 aspect ratio.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035110
[1.0.8] - 2023-10-06 ### Changed - Added a new stage template and made it default ## [1.0.7] - 2023-10-06 ### Changed - Enable UI aware "expand_viewport" mode rather than lower-level fill_viewport mode ## [1.0.6] - 2023-10-05 ### Changed - Used allowlists for building main menu entries to guard against unexpected menus.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035111
[1.0.5] - 2023-10-05 ### Fixed - Regression in hiding viewport toolbar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035112
[1.0.4] - 2023-10-04 ### Changed - Modify mode now shows selected menus on main menubar.
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035113
[1.0.3] - 2023-10-04 - Hide Viewport top toolbar in Comment Mode ## [1.0.2] - 2023-10-03 - Navigation Toolbar hidden by default in Modify Mode ## [1.0.1] - 2023-09-27 - Renamed to omni.usd_explorer.setup ## [1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/usd_explorer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035114
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{ current_date }} - Initial version of basic C++ extension template
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035115
{{ extension_display_name }} [{{ extension_name }}] Simple example of an extension that loads a C++ plugin.
स्रोत: kit-app-template/templates/extensions/basic_cpp/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035116
[ { "children": [ { "children": [ { "children": [ { "children": [ { "dock_id": 5, "dock_tab_bar_enabled": false, "dock_tab_bar_visible": false, "height": 500.0, "position_x": 0.0, "position_y": 26.0, "selected_in_dock": true, "title": "Viewport", "visible": true, "width": 727.0 } ], "dock_id": 5, "position": "LEFT" } ], "dock_id": 3, "position": "TOP" } ], "dock_id": 1, "position": "LEFT" } ], "dock_id": 3358485147 } ]
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/layouts/default.json · स्वतंत्र परीक्षण अपेक्षित।

## 035117
Changelog The format is based on [Keep a Changelog]( ## [1.0.4] - 2024-04-15 - Rename USD Player -> USD Viewer ## [1.0.3] - 2023-12-08 - Fixed deprecation warnings ## [1.0.2] - 2023-12-07 - Renamed to omni.app.usd_player.setup ## [1.0.1] - 2023-12-04 - Updated runtime profiling setings and precache of required extensions.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035118
Added proper handling of no stage loading mode in splash creen stage state monitoring.
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035119
[1.0.0] - 2021-04-26 - Initial version of extension UI template with a window
स्रोत: kit-app-template/templates/extensions/usd_viewer.setup/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035120
Changelog The format is based on [Keep a Changelog]( ## [{{ version }}] - {{current_date}} - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035121
{{ extension_display_name }} [{{ extension_name }}] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035122
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/basic_python/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035123
Overview An example C++ extension that can be used as a reference/template for creating new extensions.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035124
Demonstrates how to reflect C++ code using pybind11 so that it can be called from Python code.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035125
The {{ interface_name }} located in `include/{{ python_module_path }}/{{ interface_name }}.h` is: - Implemented in `plugins/{{ extension_name }}/ExamplePybindExtension.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035126
Reflected in `bindings/python/{{ extension_name }}/ExamplePybindBindings.cpp`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035127
Accessed from Python in `python/tests/test_pybind_example.py` via `python/impl/example_pybind_extension.py`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035128
C++ Usage Examples ## Defining Pybind Module ``` PYBIND11_MODULE({{ library_name }}, m) { using namespace {{ extension_namespace }} ; m.doc() = "pybind11 {{ extension_name }} bindings"; carb::defineInterfaceClass ( m, "{{ interface_name }}", "acquire_bound_interface", "release_bound_interface") .def("register_bound_object", &{{ interface_name }}::register{{object_name}}, R"( Register a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035129
Args: object: The bound object to register.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035130
)", py::arg("object")) .def("deregister_bound_object", &{{ interface_name }}::deregister{{object_name}}, R"( Deregister a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035131
Args: object: The bound object to deregister.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035132
)", py::arg("object")) .def("find_bound_object", &{{ interface_name }}::find{{object_name}}, py::return_value_policy::reference, R"( Find a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035133
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035134
Return: The bound object if it exists, an empty object otherwise.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035135
)", py::arg("id")) /**/; py::class_ >(m, "{{ object_interface_name }}") .def_property_readonly("id", &{{ object_interface_name }}::getId, py::return_value_policy::reference, R"( Get the id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035136
Return: The id of this bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035137
)") /**/; py::class_ >(m, "{{object_name}}") .def(py::init([](const char* id) { return Python{{object_name}}::create(id); }), R"( Create a bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035138
Args: id: Id of the bound object.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035139
Return: The bound object that was created.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035140
)", py::arg("id")) .def_readwrite("property_int", &Python{{object_name}}::m_memberInt, R"( Int property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035141
)") .def_readwrite("property_bool", &Python{{object_name}}::m_memberBool, R"( Bool property bound directly.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035142
)") .def_property("property_string", &Python{{object_name}}::getMemberString, &Python{{object_name}}::setMemberString, py::return_value_policy::reference, R"( String property bound using accessors.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035143
)") .def("multiply_int_property", &Python{{object_name}}::multiplyIntProperty, R"( Bound fuction that accepts an argument.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035144
Args: value_to_multiply: The value to multiply by.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035145
)", py::arg("value_to_multiply")) .def("toggle_bool_property", &Python{{object_name}}::toggleBoolProperty, R"( Bound fuction that returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035146
Return: The toggled bool value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035147
)") .def("append_string_property", &Python{{object_name}}::appendStringProperty, py::return_value_policy::reference, R"( Bound fuction that accepts an argument and returns a value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035148
Args: value_to_append: The value to append.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035149
Return: The new string value.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035150
)", py::arg("value_to_append")) /**/; } ```
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Overview.md · स्वतंत्र परीक्षण अपेक्षित।

## 035151
Changelog ## [1.0.1] - 2023-04-27 ### Updated - Build against Kit 105.0 ## [1.0.0] - 2022-06-30 ### Added - Initial implementation.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035152
Overview The C++ with Python Bindings Extension Template is a starting point for developers who need the performance benefits of C++ while offering a Python-friendly interface through Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035153
Designed for the NVIDIA Omniverse ecosystem, this template provides a best-practices structure to seamlessly integrate with the Omniverse Kit SDK and enable easy consumption of extension features from Python.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035154
Note for Windows C++ Developers**: This template requires that Visual Studio be installed on the host.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035155
Additionally, `"platform:windows-x86_64".enabled` and `link_host_toolchain` within the `repo.toml` file must be set to `true`.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035156
Use Cases This template is ideal for developers looking to build: - A reusable C++ extension that can be easily integrated with Omniverse Kit SDK applications.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035157
Performance-sensitive extensions that leverage C++ while still exposing a Python interface.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035158
Extensions that require direct access to the Omniverse Kit or Carbonite SDK C++ API, with the added ability for Python scripting.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035159
Integrations with existing C++ libraries or codebases while offering Python-friendly APIs for broader adoption.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035160
Key Features - Structure well suited for the build, test, and packaging tooling within this repository.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035161
All required setup code for bridging C++ logic with Python using Pybind11.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035162
Best practices for organizing C++ source and Python binding code into a single extension.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035163
Smooth integration with the Omniverse Kit SDK for application deployment.
स्रोत: kit-app-template/templates/extensions/basic_python_binding/template/docs/Readme.md · स्वतंत्र परीक्षण अपेक्षित।

## 035164
Changelog The format is based on [Keep a Changelog]( ## [0.1.2] - 2026-05-11 ### Fixed - `makePrimsPickable` handler raised `UnboundLocalError` when the WebSocket payload was empty or missing the `paths` key, and the broad `except` then leaked the raw Python exception message (including internal variable names) to the streaming client.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035165
The handler now initializes `paths` to an empty list before the conditional so an empty payload is a clean no-op, and unexpected exceptions are logged server-side via `carb.log_error` while only a generic error string is returned to the client (OMPE-90584, NVBug 6100326).
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035166
Added - Regression test `test_make_prims_pickable_empty_payload` covering empty payload, missing-`paths` key, and explicit-empty-list cases.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035167
[0.1.1] - 2025-02-13 ### Removed - Redundant openedStageResult event dispatch ## [0.1.0] - 2024-04-26 - Initial version of basic python extension template
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/CHANGELOG.md · स्वतंत्र परीक्षण अपेक्षित।

## 035168
USD Viewer Messaging Extension [omni.usd_viewer.messaging] This is an example of pure python Kit extension.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035169
It is intended to be copied and to serve as a template to create new ones.
स्रोत: kit-app-template/templates/extensions/usd_viewer.messaging/template/docs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035170
USD Explorer App Template ![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg) ## Overview The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035171
This template showcases high-performance rendering, scene optimization, live collaboration, and more.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035172
It is a great fit for interacting with large or complex 3D scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035173
By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035174
It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035175
Use Cases The USD Explorer Template is perfectly suited for: - Visualizing complex industrial environments for planning and review.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035176
Collaborating on large-scale design projects in real-time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035177
Building digital twins for industries to simulate and analyze real-world performance.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035178
This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035179
Key Features - **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035180
Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035181
Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035182
Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035183
Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035184
CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035185
Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035186
Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035187
Usage ### Getting Started To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035188
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035189
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Explorer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035190
In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035191
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035192
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035193
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035194
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035195
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035196
Select desired template with arrow keys ↑↓:** USD Explorer - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035197
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035198
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035199
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035200
Setup Extension -> omni_usd_explorer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035201
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035202
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035203
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035204
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035205
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035206
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035207
Select with arrow keys which App would you like to launch:** [Select the desired explorer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035208
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035209
![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png) ### Where to Go From Here For more guidance on modifying the USD Explorer Template, visit the [Kit SDK Companion Tutorial - Extending Reference Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035210
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035211
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035212
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035213
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035214
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035215
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035216
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035217
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035218
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035219
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035220
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035221
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035222
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035223
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035224
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035225
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035226
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035227
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035228
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035229
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035230
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035231
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035232
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035233
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035234
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035235
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035236
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035237
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035238
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035239
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035240
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035241
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035242
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035243
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035244
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035245
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035246
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035247
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containeri
स्रोत: kit-app-template/templates/apps/usd_explorer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035248
Streaming Configuration Layers These `.kit` files, known as `ApplicationLayerTemplates`, are used to define additional functionality added to the base application.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035249
For streaming configuration layers, these templates define and configure the required streaming extensions.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035250
:warning: **Important**: These layers are not standalone application templates.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035251
They must be used in conjunction with a base application template.
स्रोत: kit-app-template/templates/apps/streaming_configs/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035252
USD Composer App Template ![USD Composer Hero Image](../../../readme-assets/usd_composer.jpg) ## Overview The USD Composer App Template provides a streamlined starting point for developers aiming to create complex OpenUSD scenes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035253
This template is tailored for configurator applications, featuring enhanced performance through the Fabric Scene Delegate, improved support for AXF sourced MDLs, and robust Variant Tools.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035254
To better serve complex scene editing use cases, USD Composer has been optimized to include a refined set of extensions, focusing on the most essential components.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035255
This template simplifies the creation and manipulation of detailed 3D scenes, making it easier to customize and extend functionalities to meet your team's and customer's needs.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035256
Use Cases The USD Composer Template is perfectly suited for: - **Configurators** - USD Composer is targeted at authoring for Configurators.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035257
Developers can leverage, asset layout, materials, lighting, rendering, and variant tools to bring their configurator projects to final quality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035258
The resulting USD asset can then be packaged and deployed to end users using the USD Viewer kit-app-template - **Design Review** - The exact same asset that is authored for configurators can also be used for Design Review.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035259
Stakeholders can walk through the options of a product that the design team has authored and decide what works best for their final product offering ### Key Features - **OpenUSD File Aggregation:** Seamlessly combine and manage multiple USD files in a unified scene.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035260
Variant Tools:** View, edit, and interact with USD Variants throughout USD Composer.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035261
Scene Optimizer and Validation:** Validate and modify your USD based on your custom pipeline.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035262
Asset Packaging:** Collect and prepare your final content for deployment to your end user experiences.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035263
Built in Importers:** Directly import and convert files into the OpenUSD format.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035264
Material Library:** library of materials to seed your imagination and use on your assets.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035265
Live Collaboration:** Real-time collaboration tools allowing multiple users to view and edit scenes concurrently ## Usage ### Getting Started To get started with the USD Composer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035266
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035267
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Composer** : Some applications require setup extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035268
In the case of USD Composer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035269
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035270
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035271
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035272
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035273
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035274
Select desired template with arrow keys ↑↓:** USD Composer - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035275
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035276
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035277
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035278
Setup Extension -> omni_usd_composer_setup* - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035279
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035280
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035281
Enter version:** [set extension version] ### Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035282
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035283
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035284
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035285
Select with arrow keys which App would you like to launch:** [Select the desired composer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035286
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035287
Select **Window > Browsers > Configurator Samples** - to open configuration sample browser ![Launched USD Composer](../../../readme-assets/usd_composer_default_launch.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035288
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035289
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035290
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035291
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035292
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035293
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035294
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035295
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035296
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035297
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035298
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035299
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035300
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035301
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035302
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035303
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035304
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035305
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035306
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035307
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035308
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035309
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035310
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035311
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035312
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035313
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035314
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035315
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035316
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035317
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035318
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035319
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035320
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035321
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035322
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035323
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035324
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035325
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035326
If multiple container images exist, you will be
स्रोत: kit-app-template/templates/apps/usd_composer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035327
Kit Service App Template ![Kit Service Image](../../../readme-assets/kit_service.png) ## Overview The Kit Service App Template offers a starting point for creating headless services within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035328
Designed to leverage the capabilities of the Omniverse Kit SDK, this template enables developers to build solutions that operate without a graphical user interface, ideal for background processes or server-side applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035329
Use Cases The Kit Service Template is particularly well-suited for: - Automation services that perform tasks in the background.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035330
Headless batch processing of 3D content for optimization, conversion, or analysis.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035331
Integrations with other software ecosystems that require 3D data processing without direct user interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035332
Key Features - **Headless Operation**: Runs without a graphical user interface for efficient background processing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035333
Fully Extensible**: Leverage and extend the existing functionalities of Omniverse Kit SDK.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035334
Usage This section provides comprehensive instructions to leverage the Kit Service App Template effectively.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035335
Getting Started To get started with the Kit Service Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035336
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035337
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for Kit Service Template** : Some applications require a setup extension to function as intended.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035338
During Application configuration, you will be prompted for information about this extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035339
This extension will be created alongside the application and automatically added to your .kit file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035340
Subsequent extensions can be added to the .kit file manually.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035341
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035342
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035343
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035344
Select desired template with arrow keys ↑↓:** Kit Service - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035345
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035346
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035347
Enter version:** [set application version] *The application template you have selected requires a setup extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035348
Setup Extension -> kit_service_setup* - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035349
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035350
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035351
Enter version:** [set extension version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035352
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035353
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035354
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035355
Select with arrow keys which App would you like to launch:** [Select the desired service application] #### View your running Service: - Visit ` in your web browser to view the interactive documentation for the running service.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035356
By default the service will have a POST endpoint which will prompt you for input to generate a simple USD scene.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035357
![Launched Service](../../../readme-assets/kit_service.png) ### Where to Go From Here For more guidance on extending the Kit Service Template, visit the [Kit SDK Companion Tutorial - Extending Services]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035358
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035359
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035360
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035361
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization You can customize your Service Setup extension by adding new endpoints to, modifying existing ones, or adding new functionality to `service.py` or `extension.py`.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035362
If you would like to create a reusable component that might be used in other Omniverse services or applications, it is recommended that you create a new extension.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035363
When adapting an existing extension for a headless service, keep the service execution path limited to the dependencies it requires.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035364
Prefer separating reusable headless logic from UI, viewport, rendering, and other application-specific functionality.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035365
If separation is impractical, dependencies that the service can operate without may be declared optional, provided their imports and initialization are also guarded.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035366
See [Adapting Existing Extensions for Headless Services]( for guidance and examples.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035367
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035368
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035369
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035370
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035371
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035372
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension (beyond the initial setup extension) to become a persistent part of an application, the extension will need to be added to the application `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035373
```toml [dependencies] "my_company.my_extension" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035374
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035375
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035376
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035377
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035378
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035379
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035380
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035381
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035382
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035383
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035384
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035385
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035386
For example, if you are containerizing a headless Kit Service, select the `{your-service-name}.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035387
> **NOTE:** Default Kit Services do not enable UI based interaction.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035388
As such, containerization of these services do not require a streaming Application Layer.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035389
The base application `.kit` file should be used for containerization.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035390
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035391
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035392
Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_service/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035393
Kit Base Editor App Template ![Kit Base Editor Image](../../../readme-assets/kit_base_editor.png) ## Overview The Kit Base Editor App Template provides a minimal starting point for developers aiming to create interactive 3D applications within the NVIDIA Omniverse ecosystem.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035394
This template simplifies the process of crafting applications capable of loading, manipulating, and rendering Open Universal Scene Description (OpenUSD) content via a graphical user interface.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035395
Use Cases Kit Base Editor Template is ideal for developers looking to build: - High fidelity OpenUSD editing applications and tools from a functional, minimal starting point.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035396
Key Features - Scene loading - RTX Renderer - Basic UI for manipulating and exploring 3D scenes.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035397
Usage This section provides instructions for the setup and use of the Kit Base Editor Application Template.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035398
Getting Started To get started with the Kit Base Editor template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035399
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035400
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035401
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035402
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035403
Select desired template with arrow keys ↑↓:** Kit Base Editor - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035404
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035405
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035406
Enter version:** [set application version] ### Build and Launch #### Build your application using the provided build scripts: Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035407
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035408
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035409
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035410
Select with arrow keys which App would you like to launch:** [Select the desired editor application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035411
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035412
![Launched Kit Base Editor](../../../readme-assets/kit_base_editor.png) ### Where to Go From Here For more guidance on extending the Kit Base Editor Template, visit the [Kit SDK Companion Tutorial - Extending Editor Applications]( This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035413
Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035414
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035415
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035416
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ### Customization #### Enable Extension - From the running application select `Developer` > `Extensions` - Browse and enable extensions of interest from the Extension Manager.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035417
Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035418
To permanently add the extension to the application, you will need to add the extension to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035419
For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035420
For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035421
Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035422
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035423
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035424
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035425
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035426
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035427
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035428
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035429
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035430
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035431
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035432
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035433
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035434
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035435
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035436
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035437
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035438
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035439
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035440
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035441
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035442
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035443
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035444
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035445
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035446
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035447
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035448
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035449
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035450
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035451
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035452
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035453
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035454
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**stream only no UI overlay**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035455
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035456
![Streaming Base Editor Image](../../../readme-assets/streaming_base_editor.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Kit SDK Companion Tutorial](
स्रोत: kit-app-template/templates/apps/kit_base_editor/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035457
USD Viewer App Template ![USD Viewer Hero Image](../../../readme-assets/usd_viewer.jpg) ## Overview The USD Viewer App Template is designed to provide a robust starting point for developers looking to create streaming Omniverse Applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035458
This template showcases an RTX viewport, app streaming, and messaging support.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035459
Use Cases The USD Viewer Template is perfectly suited for streaming into a front end client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035460
Usage ### Getting Started To get started with the USD Viewer template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035461
> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035462
Cloning the Repository ```bash git clone cd kit-app-template ``` #### Create New Application **Note for USD Viewer** : This application requires `extra` and `setup` extensions to function as intended.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035463
These extensions handle the configuration within application, communication, layout, and other settings.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035464
During Application configuration, you will be prompted for information about these extensions.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035465
> **NOTE:** Feel free to use default values for testing purposes.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035466
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` > **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035467
Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035468
Select what you want to create with arrow keys ↑↓:** Application - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035469
Select desired template with arrow keys ↑↓:** USD Viewer - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035470
Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035471
Enter application_display_name:** [set application display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035472
Enter version:** [set application version] *For each required extension you will be prompted [display name] -> [extension name]:* - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035473
Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035474
Enter extension_display_name:** [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035475
Enter version:** [set extension version] > **NOTE:** You will need to repeat above steps for each extension.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035476
Build and Launch Note that the build step will build all applications contained in the `source` directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035477
Outside of initial experimentation, it is recommended that you build only the application you are actively developing.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035478
Build your application using the provided build scripts: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` If you experience issues related to build, please see the [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035479
Launch your application: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035480
Select with arrow keys which App would you like to launch:** [Select the desired viewer application] > **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035481
After initial shader compilation, startup time will reduce dramatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035482
Default Launch State By default, the USD Viewer template application opens with an empty viewport.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035483
![USD Viewer Default Launch](../../../readme-assets/usd_viewer_default_launch.png) This is the intended behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035484
The USD Viewer template application is designed as a base for displaying content either locally or over a streaming connection (See the [Local Streaming](#local-streaming) section below).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035485
To display content in the desktop application, you can pass an argument to the `repo launch` command to load content on startup.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035486
The USD Viewer template includes sample assets for this purpose.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035487
Let's load the `stage01.usd` sample asset by providing the full path to the `/app/auto_load_usd` argument.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035488
Linux:** ```bash ./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` **Windows:** ```powershell .\repo.bat launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd' ``` ![USD Viewer Asset Launch](../../../readme-assets/usd_viewer_load_asset_desktop.png) ### Testing Applications and their associated extensions can be tested using the `repo test` tooling provided.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035489
Each application template includes an initial test suite that can be run to verify the application's functionality.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035490
> **NOTE:** Testing will only be run on applications and extensions within the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035491
A successful build is required before testing.** **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` #### Create Custom Extension **Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` Follow the prompt instructions: - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035492
Select what you want to create with arrow keys ↑↓:** Extension - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035493
Select desired template with arrow keys ↑↓:**: [choose extension template] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035494
Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035495
Enter extension_display_name:**: [set extension display name] - **?
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035496
Enter version:** [set extension version] #### Adding Extension to .kit File **Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035497
```toml [dependencies] "extension.name" = {} ``` #### Build with New Extensions After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035498
Packaging and Deployment For deploying your application, create a deployable package using the `package` command: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` By default, the `package` command will name the package based on the `name` value contained in the `repo.toml` file at the root of the repository.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035499
By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035500
Alternatively, you can specify a package name using the `--name` flag: **Linux:** ```bash ./repo.sh package --name ``` **Windows:** ```powershell .\repo.bat package --name ``` This will bundle your application into a distributable format, ready for deployment on compatible platforms.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035501
:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035502
The version is set within the `tools/VERSION.md` file.** #### Launching a Package > :warning: **Deprecated:** `launch --package` is deprecated and will be removed in a future release.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035503
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035504
See [Packaging An Application]( for details.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035505
Applications packaged using the `package` command can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --package ``` **Windows:** ```powershell .\repo.bat launch --package ``` > **NOTE:** This behavior is not supported when packaging with the `--thin` flag.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035506
Containerization (Linux Only) **Requires:** `Docker` and `NVIDIA Container Toolkit` The packaging tooling provided by the Kit App Template also supports containerization of applications.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035507
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035508
To package your application as a container image, use the `--container` flag: **Linux:** ```bash ./repo.sh package --container ``` You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035509
This will dictate the behavior of your containerized application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035510
For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035511
> **NOTE:** If creating a container for a NVIDIA Cloud Functions (NVCF) based deployment, select the `{your-app-name}_nvcf.kit` file to ensure the proper settings are used for that platform.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035512
Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image: **Linux:** ```bash ./repo.sh package --container --name [container_image_name] ``` #### Launching a Container Applications packaged as container images can be launched using the `launch` command: **Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035513
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035514
Local Streaming During the creation of a new application, you can enable streaming by selecting the desired streaming layer(s) for your application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035515
Selecting the **Omniverse Kit App Streaming (Default)** layer will create a `{your-app-name}_streaming.kit` which we will use for local streaming.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035516
This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035517
To try local streaming, you need a web client to connect to the streaming server.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035518
Clone Web Viewer Sample The web viewer sample can be found [here]( ```base git clone ``` Follow the [Quick Start instructions in the README]( to install the necessary dependencies.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035519
Start the streaming Kit Application :warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035520
Launch and stream a desktop application:** **Linux:** ```bash ./repo.sh launch -- --no-window ``` **Windows:** ```powershell .\repo.bat launch -- --no-window ``` Select the `{your-app-name}_streaming.kit` and wait for the application to start **Launch and stream a containerized application:** When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035521
Linux:** ```bash ./repo.sh launch --container ``` If only a single container image exists, it will launch automatically.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035522
If multiple container images exist, you will be prompted to select the desired container image to launch.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035523
> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035524
Start the Streaming Client Follow the [Quick Start instructions in the web-viewer-sample README]( to start the streaming client (**with Web UI overlay for messaging**) and connect via a Chromium-based browser.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035525
You should see the streaming client connect to the running Kit application.
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035526
![Streaming Viewer Image](../../../readme-assets/streaming_viewer.png) ## Additional Learning - [Usage and Troubleshooting](../../../readme-assets/additional-docs/usage_and_troubleshooting.md) - [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) - [Omniverse Kit SDK Manual](
स्रोत: kit-app-template/templates/apps/usd_viewer/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035527
name: kit-upgrade description: "Scan and upgrade Omniverse Kit SDK projects between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035528
Analyzes project files, identifies breaking changes, deprecated APIs, and removed extensions specific to the customer's code.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035529
Provides a personalized upgrade plan with file:line references and auto-fix suggestions.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035530
Covers Kit 106→107→108→109→110." --- # Kit SDK Upgrade Skill Guide a developer through upgrading their Omniverse Kit project from one version to another.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035531
This skill is a lean workflow router.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035532
Steps 1 and 2 (detect the project, decide the migration path) are inline below** — they are always needed.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035533
The detail for the remaining steps (2.5–6) lives in `procedures/`, and the structured change data in `references/`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035534
Read each procedure file when the workflow sends you to it** — do not try to hold them all in context at once.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035535
When to Use - User asks to upgrade their Kit project/app/extension - User asks about Kit breaking changes or migration - User is hitting errors after changing their Kit SDK version - User has a broken build or runtime failure after a version bump --- ## Quick Orientation Pick the entry point that matches the request: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035536
First-time upgrade scan** → start at Step 1 below and follow the workflow in order.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035537
Already upgraded, now has a build/runtime error** → go straight to `procedures/failure-modes.md`, diagnose, then apply the relevant Stage's fixes from `procedures/stage-notes.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035538
Just wants a list of breaking changes** → do Step 1, then run the scans in `procedures/scan.md` for their migration path and present the report from `procedures/report.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035539
The `# Kit SDK Version:` comment in `.kit` files reflects the last lock-file regeneration and may differ from the pin during an in-progress upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035540
Version string format: `110.1.0+feature.${platform_target_abi}.${config}` - First number (110) = major Kit version **If no version pin is found:** Check git history (`git log --oneline -20 -- tools/deps/ deps/`) or ask the user what Kit version they are currently running.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035541
(Layout detection below has not run yet, so scope the log to both candidate deps locations.) ### Detect project layout and build system Kit projects do **not** all use the SDK template layout, and the layout can differ between releases and project types — for example, `deps/` may sit at the project **root** in one release and under **`tools/`** in another (even between two point releases of the same major line).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035542
Projects also frequently **wrap or integrate the Kit build system into their own tooling**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035543
Detect the layout and build entrypoint **once**, then reuse them everywhere below — **never assume `tools/deps/` or `./repo.sh`**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035544
deps directory (holds kit-sdk.packman.xml + repo-deps.packman.xml) if [ -f tools/deps/kit-sdk.packman.xml ]; then DEPS_DIR=tools/deps elif [ -f deps/kit-sdk.packman.xml ]; then DEPS_DIR=deps else f=$(find .
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035545
name kit-sdk.packman.xml -not -path './_*' | head -1); DEPS_DIR=${f:+$(dirname "$f")}; fi echo "DEPS_DIR=${DEPS_DIR:- }" # 2.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035546
build entrypoint — the standard repo wrapper, if present if [ -f ./repo.sh ]; then BUILD='./repo.sh' elif [ -f ./repo.bat ]; then BUILD='repo.bat' else BUILD=''; fi # empty => custom / integrated build (see below) echo "BUILD=${BUILD:- }" ``` **If `BUILD` is empty, the project uses a custom or integrated build system** (common — many customers embed the Kit build inside their own).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035547
Do **not** fabricate `./repo.sh` calls.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035548
Find the real build command (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or the project README) or ask the user how they build.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035549
The upgrade work below (kernel pin bump, **toolchain update**, lock regeneration) still applies — you just invoke it through the project's own entrypoint.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035550
Record it as `$BUILD`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035551
> **From here on (and in every procedure file), use `$DEPS_DIR` and `$BUILD` in every command.** Where a document still shows a literal `tools/deps/` or `./repo.sh`, substitute the detected values.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035552
> > **These are not guaranteed to persist across shells.** If you run each fenced block in a fresh subshell, `$DEPS_DIR`/`$BUILD` will be unset.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035553
So do **one** of: (a) textually replace `$DEPS_DIR` and `$BUILD` with the literal detected paths (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035554
`tools/deps`, `./repo.sh`) in every command you run, or (b) re-run the two detection blocks above at the top of each new shell session.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035555
Do **not** run a later block assuming the variables are still set.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035556
Step 2: Determine Migration Path Kit versions must be upgraded **in sequence**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035557
Kit 108 was never publicly released** — its changes are folded into the 107→109 path.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035558
When upgrading 107→109 you must still address Stage 2 (107→108) changes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035559
A **within-major** bump (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035560
`110.0 → 110.1`, `110.1.0 → 110.1.2`) or a **feature → production** branch transition is a *different, lighter* job — and it is the most common upgrade performed in practice.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035561
These rarely need the Stage code/API changes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035562
The real work is almost entirely **tooling and layout**: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035563
Update the build toolchain** (repo tools, packman, repo scripts) — see Step 2.5 (`procedures/toolchain.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035564
This is usually the substantive part.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035565
Re-detect the deps directory** — its location can differ between releases, even within the same major line (Step 1 already sets `$DEPS_DIR`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035566
Bump the kit-kernel pin** in `$DEPS_DIR/kit-sdk.packman.xml` (Step 5, item 2 — `procedures/apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035567
For a feature ↔ production transition only:** check the extension **registry URL** in the `.kit` files — the feature and production lines use different registries, so a feature→production move may need a registry swap (Step 5, item 3).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035568
A plain within-major bump on the same line usually does **not**.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035569
Regenerate the extension version-lock** and do a **clean rebuild** (Step 5 items 1 & 8, then Step 6).
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035570
> **⚠️ Do NOT run the whole of Step 5 for a within-major bump.** Step 5 (`procedures/apply-fixes.md`) is written for **major-boundary** crossings.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035571
Running them on a 110.1.0→110.1.2 bump would wrongly strip extensions or rewrite APIs that are perfectly valid on 110.1.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035572
Only run the Step 3 code scans if the upgrade crosses a major boundary.** For a pure within-major or feature→production move, skip Step 3's per-stage API scans and go straight to Step 2.5 → Step 5 (items 1–3 & 8 only, as above) → Step 6.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035573
If you cross one or more major boundaries on the way, run Step 3 for each major boundary passed and the full Step 5.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035574
Steps 2.5–6: Execute the Upgrade Once the path is known, work through these in order.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035575
Read the linked procedure file and follow it**; each assumes Step 1 detection has run.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035576
Step 2.5 — Update the build toolchain** → `procedures/toolchain.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035577
Highest-impact step; run it **first**, before touching source.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035578
For a within-major bump this is usually the only substantive work.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035579
Step 3 — Scan the project** → `procedures/scan.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035580
Run only the stage scans for the major boundaries you cross.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035581
Skip entirely for a pure within-major bump.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035582
Step 4 — Generate the upgrade report** → `procedures/report.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035583
Present findings by severity with exact `file:line` references.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035584
Step 5 — Apply fixes** → `procedures/apply-fixes.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035585
Get user approval before modifying files.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035586
(Within-major: items 1, 2, 8 only — see Step 2 above.) - **Step 6 — Validate** → `procedures/validate.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035587
Clean rebuild, regenerate the version lock, run tests.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035588
Already upgraded and hitting a specific error?** Go to `procedures/failure-modes.md` — it maps common symptoms (exit-55, ABI undefined symbols, render diffs, build loops, custom-build/layout issues) to fixes.
स्रोत: kit-app-template/.skills/kit-upgrade/SKILL.md · स्वतंत्र परीक्षण अपेक्षित।

## 035589
Kit SDK Upgrade Skill ## What This Is This repository contains an AI agent skill for upgrading Omniverse Kit SDK projects between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035590
The skill encodes the complete breaking-change catalog for the Kit 106→107→108→109→110 migration path — including removed extensions, deprecated APIs, C++ ABI breaks, Python runtime changes, and configuration updates — into a structured set of instructions and reference data that an AI agent can execute against a live project.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035591
The agent scans the project, produces a categorized report with exact `file:line` references, and suggests targeted fixes, including auto-fixable regex replacements where safe.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035592
Who It's For Kit extension and application developers who need to upgrade a project from one Kit SDK version to another.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035593
This includes developers working on kit-app-template-based applications, standalone extensions, and Isaac Sim integrations.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035594
The skill is particularly useful when upgrading across multiple versions at once (e.g., 107→110), where the number of breaking changes makes manual triage error-prone.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035595
What It Contains | File | Description | |------|-------------| | `SKILL.md` | Lean workflow router — loaded by the AI agent.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035596
Holds version/layout/build detection (Step 1) and the migration-path decision (Step 2), and points to the procedure files for everything else.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035597
| | `procedures/toolchain.md` | Step 2.5 — update the `repo_*` build toolchain (the highest-impact part of most upgrades).
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035598
| | `procedures/scan.md` | Step 3 — the full per-stage `grep` scan catalog for breaking changes, removed extensions, and config.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035599
| | `procedures/report.md` | Step 4 — the upgrade-report template.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035600
| | `procedures/apply-fixes.md` | Step 5 — ordered fix list, auto-fixable regex patterns, and manual-only changes.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035601
| | `procedures/validate.md` | Step 6 — clean-rebuild and validation commands.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035602
| | `procedures/failure-modes.md` | Symptom→fix diagnosis for projects that already upgraded and are erroring.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035603
| | `procedures/stage-notes.md` | Per-stage (106→107→…→110) breaking-change reference.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035604
| | `references/breaking_changes.json` | 80+ breaking changes with search patterns, affected versions, and recommended fixes.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035605
| | `references/removed_extensions.json` | Extensions removed or deprecated by Kit version, with replacement guidance and search targets.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035606
| | `references/api_replacements.json` | 1:1 API replacements that are safe to apply with regex find/replace.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035607
| | `references/config_changes.json` | Settings keys, registry URLs, and build config changes between versions.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035608
| | `references/toolchain.json` | The build-toolchain file/package set (`repo_*` tools, packman, repo scripts) and how to find the correct target versions for a given Kit line.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035609
| | `install.sh` / `install.bat` | Copies the skill (SKILL.md + `procedures/` + `references/`) into an existing Kit project so it travels with the repo.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035610
| The skill uses **progressive disclosure**: `SKILL.md` stays small (a router the agent always loads) and each step's detail lives in a `procedures/*.md` file the agent reads only when the workflow sends it there.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035611
This keeps the entry file well under length limits and keeps irrelevant detail out of context.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035612
How to Use **Install into an existing project** (so the skill travels with the repo): ```bash ./install.sh /path/to/your-kit-project # copies into /.skills/kit-upgrade/ ./install.sh /path/to/your-kit-project .claude/skills # or the Claude Code skills layout ``` On Windows: `install.bat C:\path\to\your-kit-project`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035613
Then load the skill into any AI coding assistant that can read files and run shell commands, and point it at the project you want to upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035614
Claude Code:** ``` Read the skill at /path/to/kit-upgrade-skill/SKILL.md and the reference files in references/.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035615
Then scan /path/to/my-kit-project and generate an upgrade report for Kit 109 → 110.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035616
``` **Cursor / VS Code Copilot / other MCP clients:** Add `kit-upgrade-skill/` as a context directory or attach `SKILL.md` as a system prompt, then ask the agent to scan your project.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035617
Detect the current Kit SDK version, the deps-directory location (`tools/deps/` vs root `deps/`), and the build entrypoint (`./repo.sh` / `repo.bat` or a custom/integrated build) — never assuming the SDK template layout 2.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035618
Determine the migration path — including within-major (minor/patch) and feature↔production transitions, not just major-version stages 3.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035619
Update the build toolchain (`repo_*` tools, packman, repo scripts) to match the target Kit line — often the substantive part of an upgrade 4.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035620
Run targeted `grep` scans across the full project root (including `templates/`, launcher configs, and ETM lock files) for any major boundaries crossed 5.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035621
Generate a categorized report: breaking changes, behavioral changes, deprecated usage, and a "not affected" checklist 6.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035622
Suggest fixes — both auto-applicable regex replacements and manual changes requiring human judgment 7.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035623
Its changes are folded into the 107→109 path — Stage 2 must still be addressed when upgrading 107→109.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035624
Multi-version upgrades (e.g., 107→110) apply all intervening stages in sequence.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035625
How to Contribute **Add a new breaking change:** Add an entry to `references/breaking_changes.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035626
Each entry needs an `id`, `title`, `stage`, `search_pattern` (grep-compatible regex), `affected_files` (glob patterns), and `fix` description.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035627
If the fix is a safe 1:1 substitution, also add it to `references/api_replacements.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035628
Add a removed or deprecated extension:** Add an entry to `references/removed_extensions.json` with `extension`, `status` (`removed` or `deprecated`), `version`, `replacement` (or `null`), `search_in` (list of file extensions to scan), and `notes`.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035629
Include any known failure mode (e.g., exit-55) and whether the extension appears in non-obvious locations like `templates/` or ETM lock files.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035630
Add a new Kit version (release):** edit the files that own each piece — the skill is split by concern: - `SKILL.md` — add the new row/stage to the **Step 2 migration-path table and Stage summary** (these stay in the router).
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035631
`procedures/scan.md` — add the new `# === Stage N ===` scan blocks.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035632
`procedures/stage-notes.md` — add the new per-stage breaking-change section.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035633
`procedures/apply-fixes.md` — add any new auto-fix regex patterns or fix-list items.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035634
`references/*.json` — add the corresponding structured entries.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035635
Follow the existing section structure in each file for consistency.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035636
Keep `SKILL.md` lean — detailed scan commands and stage notes belong in `procedures/`, not the router.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035637
Test your additions:** Apply the skill to a real project that exercises the new patterns.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035638
If the scan misses something or the fix guidance is wrong, document it and open a PR with both the issue description and the corresponding fix in the relevant `procedures/` or `references/` file.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035639
This skill was developed and validated against [kit-extension-explorer]( a Kit 110 application based on kit-app-template.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035640
See `test-report.md` for the full upgrade report from that validation run.
स्रोत: kit-app-template/.skills/kit-upgrade/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 035641
{ "description": "The build toolchain a Kit project must keep in sync with its kit-kernel pin.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035642
SKILL.md Step 2.5 makes updating it a first-class step.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035643
Do NOT hardcode versions here — they move per branch; read the target branch's actual pins at upgrade time.", "toolchain_files": [ {"file": " /kit-sdk.packman.xml", "holds": "kit-kernel pin (the Kit SDK itself)", "notes": "DEPS_DIR is tools/deps/ or root deps/ — detect it (SKILL.md Step 1)."}, {"file": " /repo-deps.packman.xml", "holds": "the repo_* build tools + template-content packages", "notes": "The main toolchain file.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035644
Add or remove packages that appear/disappear between lines (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035645
repo_nspect is present on feature/main but not on production/110.1 or feature/110.3).", "reference_source": "omniverse/kit-apps/kit-sdk-public (and/or omniverse/kit-github/kit-app-template) on the matching branch.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035646
Prefer production/ over feature/ for a stable upgrade.", "critical_note": "Toolchain versions track the BRANCH's maintenance cadence, NOT the kernel line number.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035647
A newer kernel line can carry an OLDER toolchain.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035648
Never infer tool versions from the Kit version — read the actual target-branch pins.", "example_only_do_not_copy": { "note": "Illustrative snapshot read from kit-sdk-public in 2026 — WILL go stale.
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035649
Always re-read the target branch at upgrade time.", "feature/main": {"kit-kernel": "110.4.0+feature", "repo_man": "2.6.4", "repo_build": "1.30.0", "repo_kit_tools": "1.20.3"}, "production/110.1": {"kit-kernel": "110.1.3+production", "repo_man": "2.9.3", "repo_build": "1.34.3", "repo_kit_tools": "1.21.2"} } } }
स्रोत: kit-app-template/.skills/kit-upgrade/references/toolchain.json · स्वतंत्र परीक्षण अपेक्षित।

## 035650
[ {"setting":"packman XML ABI token","versions":{"from":"106","to":"107"},"old_value":"${platform_target}","new_value":"${platform_target_abi}","file":"*.packman.xml","path":"package name attributes","notes":"Native packages now use ABI-variant package names.
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035651
The deps directory location varies by release and project type (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035652
deps/ at the project root in one release, under tools/ in another, even between point releases of the same major line).
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035653
Do NOT assume tools/deps/ and do NOT rewrite paths from old_value to new_value -- detect the actual location (SKILL.md Step 1, $DEPS_DIR)."} ]
स्रोत: kit-app-template/.skills/kit-upgrade/references/config_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035654
[ { "extension": "omni.kvdb", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035655
Causes exit code 55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035656
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.localcache", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035657
Same failure class as omni.kvdb.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035658
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.genproc.core", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035659
Migrate procedural generation workflows.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035660
Search the entire project root including templates/ and launcher-configs/ directories." }, { "extension": "omni.kit.extpath.git", "status": "removed", "version": "108", "replacement": null, "search_in": [ "extension.toml" ], "notes": "Git URL extension search path.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035661
Was deprecated in 107." }, { "extension": "omni.hydra.iray.shadercache.d3d12", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035662
No explicit removal notice." }, { "extension": "omni.hydra.iray.shadercache.vulkan", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Silently removed alongside Iray deprecation.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035663
No explicit removal notice." }, { "extension": "omni.kit.viewport.iray", "status": "removed", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Was Sample in Kit 107.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035664
No version recorded in official docs." }, { "extension": "omni.hydra.scene_api", "status": "deprecated", "version": "108", "replacement": null, "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated since Kit 108.0.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035665
Removal pending." }, { "extension": "omni.surface_instancer", "status": "deprecated", "version": "pre-106", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Confirmed deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035666
Active customer confusion." }, { "extension": "omni.renderer_capture", "status": "deprecated", "version": "110", "replacement": "omni.kit.capture", "search_in": [ "extension.toml", ".kit", ".py" ], "notes": "Deprecated in Kit 110." }, { "extension": "omni.kit.widget.nucleus_connector", "status": "deprecated", "version": "110", "replacement": "omni.kit.widget.connection_manager", "search_in": [ "extension.toml", ".kit" ], "notes": "Compatibility shim.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035667
Will be removed." }, { "extension": "omni.kit.viewport.legacy_gizmos", "status": "deprecated", "version": "110", "replacement": null, "search_in": [ "extension.toml", ".kit" ], "notes": "Deprecated in Kit 110.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035668
Still operational but emits deprecation warnings.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035669
Commonly appears in both source/apps/ and templates/ .kit files — scan the full project root.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035670
No direct replacement announced; plan migration away from legacy gizmos rendering path." }, { "extension": "omni.kit.livestream", "status": "removed", "version": "108", "replacement": "omni.kit.livestream.app + omni.kit.livestream.aov + omni.kit.livestream.core", "search_in": [ "extension.toml", ".kit" ], "notes": "Monolithic livestream extension split into focused modules in Kit 108.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035671
Replace with the three new extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035672
Settings paths also changed \u2014 see config_changes.json." }, { "extension": "omni.services.livestream.nvcf", "status": "removed", "version": "108", "replacement": "omni.services.livestream.session", "search_in": [ "extension.toml", ".kit" ], "notes": "Session management extension renamed in Kit 108.
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035673
Replace dependency declaration and update any code referencing the old extension name." } ]
स्रोत: kit-app-template/.skills/kit-upgrade/references/removed_extensions.json · स्वतंत्र परीक्षण अपेक्षित।

## 035674
[ {"id":"py-omniclient","versions":{"from":"106","to":"107"},"category":"Python API","severity":"breaking","title":"omni.client._omniclient removed","description":"Private internal API removed.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035675
Use public omni.client API.","search_patterns":["omni\\.client\\._omniclient"],"file_types":[".py"],"fix":{"type":"regex_replace","description":"Replace import","from_pattern":"import omni\\.client\\._omniclient","to_pattern":"import omni.client"}}, {"id":"py-311","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"Python 3.10 → 3.11","description":"Python upgraded.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035676
Audit f-strings, typing module usage, and third-party packages for 3.11 compatibility.","search_patterns":["python3\\.10","python310"],"file_types":[".toml",".py",".sh",".bat",".lua"],"fix":{"type":"manual","description":"Update Python references to 3.11"}}, {"id":"cpp-abi-cxx11","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Linux: _GLIBCXX_USE_CXX11_ABI=1","description":"Native packages now use new C++ ABI.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035677
Rebuild all .so plugins.","search_patterns":["_GLIBCXX_USE_CXX11_ABI"],"file_types":[".cpp",".cmake",".toml"],"fix":{"type":"manual","description":"Rebuild all native plugins against new ABI"}}, {"id":"packman-abi-token","versions":{"from":"106","to":"107"},"category":"Build","severity":"breaking","title":"packman XML: ${platform_target} → ${platform_target_abi}","description":"Native packages now use ABI-variant tokens.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035678
Python payload access changed from e.payload['key'] to e['key'].
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035679
Subscribe via carb.eventdispatcher.get_eventdispatcher().observe_event().
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035680
C++: update to carb::eventdispatcher.","search_patterns":["e\\.payload\\[","carb\\.events\\.acquire_event_queue","create_subscription_to_pop"],"file_types":[".py",".cpp",".h"],"fix":{"type":"manual","description":"Update event subscriptions and payload access to Events 2.0 pattern.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035681
Remove explicit event pump calls."}}, {"id":"fabric-pathc-tokenc-intro","versions":{"from":"106","to":"107"},"category":"C++ ABI","severity":"breaking","title":"Fabric PathC/TokenC introduced (removed in 109)","description":"Kit 107 introduced PathC/TokenC.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035682
Kit 109 removes them.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035683
Update Premake configs, CI, and build scripts.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035684
Audit all third-party packages for 3.12 compatibility.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035685
Use getCachedInterface.","search_patterns":["acquireInterface"],"file_types":[".cpp",".h"],"fix":{"type":"regex_replace","from_pattern":"carb::Framework::acquireInterface","to_pattern":"carb::getCachedInterface"}}, {"id":"omnigraph-3.0","versions":{"from":"107","to":"108"},"category":"C++ ABI","severity":"breaking","title":"omni.graph.core 3.0.0 ABI break","description":"Binary incompatible with 2.x.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035686
Recompile all OmniGraph nodes.","search_patterns":["omni\\.graph\\.core","omni\\.graph\\.nodes"],"file_types":[".toml"],"fix":{"type":"manual","description":"Recompile against omni.graph.core 3.0.0.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035687
Align omni.graph.nodes version."}}, {"id":"parallel-node-reg","versions":{"from":"107","to":"108"},"category":"Extension","severity":"breaking","title":"Parallel OmniGraph node registration removed","description":"Extension manager is not thread-safe.
स्रोत: kit-app-template/.skills/kit-upgrade/references/breaking_changes.json · स्वतंत्र परीक्षण अपेक्षित।

## 035688
Step 6: Validate > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 035689
Assumes Step 1 detection has run (`$BUILD` is set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 035690
```bash # After a kit-kernel pin bump, do a CLEAN rebuild so the kernel symlinks refresh, # then regenerate the version lock against the new kernel.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 035691
$BUILD is the entrypoint detected in Step 1 (./repo.sh, repo.bat, or the project's own build wrapper).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 035692
`No versions of > omni.anim.curve.core … = `).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 035693
Use **`$BUILD build --clean`** (removes the build-time `_*` > folders so the next `build -r` refreshes the symlinks) or **`$BUILD build --rebuild -r`** (clean + > release build in one command), then regenerate the lock with `build -u`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 035694
The generated `[settings.app.exts] > enabled = [...]` block in each `.kit` is what must be regenerated — it carries exact old-version pins that > `extscache` clearing does not touch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/validate.md · स्वतंत्र परीक्षण अपेक्षित।

## 035695
Failure Mode Diagnosis > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035696
Use this when the user has **already** upgraded and has a specific error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035697
`$DEPS_DIR` / `$BUILD` refer to the values detected in Step 1 (in `../SKILL.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035698
Exit Code 55 (Dependency Solver Failure) **Cause:** Removed extension still declared as a dependency, or stale extscache.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035699
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035700
Search for removed extension names in `.kit` and `extension.toml` files (see `../references/removed_extensions.json`) 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035701
For Kit 110: check for `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.*`, `omni.kit.viewport.iray` 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035702
Re-run `precache_exts` ### Build Fails with Undefined Symbol / Missing Method **Cause:** ABI break — extension was compiled against an older version.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035703
Fix:** Recompile the extension against the current Kit SDK.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035704
Every stage has at least one ABI break.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035705
Runtime Crash on DLL Load (Windows) **Cause after Stage 3:** mimalloc cross-DLL heap mismatch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035706
Memory allocated on one side of a DLL boundary freed on the other.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035707
Fix:** Audit allocation ownership.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035708
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035709
Python TypeError: unexpected keyword argument 'menu_compatibility' **Cause (Stage 4):** `menu_compatibility` parameter removed from `ui.Menu` and `ui.Separator`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035710
Fix:** Remove the `menu_compatibility=` argument from all call sites.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035711
Extension Loads But APIs Return None / AttributeError **Cause:** Transitive loading of `omni.kit.ui`, `omni.resourcemonitor`, or `omni.kit.manipulator.prim.fabric` was removed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035712
Fix:** Add explicit dependency in `extension.toml`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035713
Render Output Differs (No Code Changes) **Cause after Stage 3:** DomeLight orientation changed (USD 25.05), FSD enabled by default, or `mergeMaterials` default changed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035714
Diagnosis:** - Check for DomeLights in the scene: `grep -rn "DomeLight" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035715
include="*.usd" --include="*.usda"` - Check FSD setting: `grep -rn "FabricSceneDelegate\|fsd" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035716
include="*.kit" --include="*.toml"` - Check `mergeMaterials`: `grep -rn "mergeMaterials" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035717
include="*.kit" --include="*.toml"` ### if (optional_bool) No Longer Works (C++) **Cause (Stage 4):** `optional ` / `expected ` now tests for *presence* in an if-condition, not the stored value.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035718
Fix:** Replace `if (b)` with `if (b.has_value() && b.value())` ### Build Fails in a Loop / the Same Error Repeats **Cause:** Almost always a **stale toolchain** (Step 2.5 not applied — see `toolchain.md`) or a wrong assumption about the project's layout/build system — *not* the source code.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035719
Rule — do not keep editing source and rebuilding.** If the same build error recurs after **2 attempts**, STOP and re-check the fundamentals before changing any more code: 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035720
Is the **toolchain** aligned to the target Kit line?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035721
(Step 2.5, `toolchain.md` — the #1 cause of build loops.) 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035722
Is `$DEPS_DIR` the **actual** deps location and `$BUILD` the project's **actual** build entrypoint?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035723
(Step 1 in `../SKILL.md`.) 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035724
Did you do a **clean** rebuild (`$BUILD build --rebuild -r`), not just clear extscache?
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035725
(Step 6, `validate.md`.) Surface the exact error and these three checks to the user rather than looping — repeated speculative edits burn tokens and rarely fix a toolchain/layout problem.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035726
Project Uses a Custom / Integrated Build System **Cause:** The project wraps or embeds the Kit build system in its own tooling, so `./repo.sh` / `repo.bat` don't exist or aren't the real entrypoint (common for customer integrations).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035727
Fix:** Do **not** fabricate `./repo.sh` commands.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035728
Use the `$BUILD` detected in Step 1 (check `repo.toml`, `Makefile`/`CMakeLists.txt`, `package.json` scripts, CI config, or ask the user).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035729
The upgrade steps (kernel pin, **toolchain update**, lock regen) still apply — invoke them through `$BUILD`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035730
deps Directory Not Where Expected **Cause:** The project layout differs from the SDK template, or the deps directory moved between releases (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035731
`deps/` at the project root vs under `tools/`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035732
Fix:** Re-run the Step 1 detection (in `../SKILL.md`) to set `$DEPS_DIR`, then use it everywhere.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035733
Never hardcode `tools/deps/`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/failure-modes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035734
Step 3: Scan the Project > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035735
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035736
Only run this step for major-version boundaries you cross** — a pure within-major / feature→production bump skips it.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035737
Run these commands from the project root.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035738
Only run scans for the stages that apply to this upgrade.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035739
Collect all matches before generating the report.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035740
> **⚠️ Scan scope:** Use `.` (project root) as the search root, not just `source/`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035741
Many projects have `templates/`, `launcher-configs/`, or other directories containing `.kit` files and `extension.toml` files with real dependency declarations.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035742
Scanning only `source/` will miss these.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035743
> > **Windows note:** Commands below use bash syntax.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035744
On Windows, replace `for` loops with individual `findstr` or PowerShell `Select-String` commands, or run inside WSL/Git Bash.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035745
Python / Extension Dependencies ```bash # === Stage 1 (106→107) === # Python 3.10 references (now 3.11) grep -rn "python3\.10\|python310\|boost_python310" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035746
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" --include="*.toml" # Private omni.client API grep -rn "omni\.client\._omniclient" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035747
include="*.py" # carb.imgui (removed — use omni.kit.imgui) grep -rn "carb\.imgui" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035748
include="*.py" # Events 1.0 patterns (payload access, subscription style) grep -rn "e\.payload\[" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035749
include="*.py" grep -rn "create_subscription_to_pop" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035750
include="*.py" # nv_usd references in build files grep -rn "nv_usd" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035751
premake5.lua repo.toml --include="*.lua" --include="*.toml" # packman XML using a pre-ABI token (should be ${platform_target_abi}).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035752
NOTE: match BOTH the old ${platform} form (Kit 106) and the intermediate ${platform_target} form — # the narrower 'platform_target[^_]' pattern misses ${platform}, which is what 106.5 actually uses and # is a build-verified hard failure on 106->107 (kit-kernel pull: "Package not found ...gl.linux-x86_64").
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035753
grep -rnE '\$\{platform(_target)?\}' "$DEPS_DIR" --include="*.xml" # Toolbar deprecated APIs grep -rn "omni\.kit\.widget\.toolbar\|omni\.kit\.window\.toolbar" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035754
include="*.py" --include="*.toml" # === Stage 2 (107→108) === # Python 3.11 references (now 3.12) grep -rn "python3\.11\|python311\|boost_python311" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035755
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" # get_custom_glyph_code (moved to omni.ui) grep -rn "omni\.kit\.ui.*get_custom_glyph_code" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035756
include="*.py" # WindowHandle deprecated usage grep -rn "WindowHandle" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035757
include="*.py" # menu_compatibility (deprecated in 108, removed in 110) grep -rn "menu_compatibility" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035758
include="*.py" # Layer events (Events 1.0 style) grep -rn "get_event_stream\|create_subscription_to_pop\|carb\.events" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035759
include="*.py" # Livestream extension (monolithic — should be split) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035760
include="*.kit" --include="*.toml" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035761
include="*.kit" --include="*.toml" # Livestream settings (old path) grep -rn "app/livestream\|app\.livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035762
include="*.kit" --include="*.toml" # Old omni.kit.ui transitive usage (no longer loaded transitively) grep -rn "omni\.kit\.ui[^.]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035763
include="*.py" # === Stage 3 (108→109) === # NumPy 1.x type aliases (removed in 2.0) grep -rn "np\.bool[^_]\|np\.int[^0-9_]\|np\.float[^0-9_]\|np\.complex[^0-9_]\|np\.object[^_]\|np\.str[^_]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035764
include="*.py" # === Stage 4 (109→110) === # menu_compatibility (now raises TypeError — must remove entirely) grep -rn "menu_compatibility=" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035765
include="*.py" # omni.usd layers deprecated API grep -rn "get_context()\.get_layers()\|context\.get_layers()" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035766
include="*.py" # omni.renderer_capture (deprecated → omni.kit.capture) grep -rn "omni\.renderer_capture" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035767
include="*.py" # USD displayName/displayGroup/hidden deprecated metadata grep -rn "GetMetadata.*displayName\|SetMetadata.*displayName\|GetMetadata.*hidden\|SetMetadata.*hidden\|GetMetadata.*displayGroup\|SetMetadata.*displayGroup" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035768
include="*.py" ``` ### C++ / Native Code ```bash # === Stage 1 (106→107) === # C++ ABI — check for _GLIBCXX_USE_CXX11_ABI overrides (must be =1) grep -rn "_GLIBCXX_USE_CXX11_ABI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035769
include="*.cpp" --include="*.h" --include="*.cmake" # === Stage 2 (107→108) === # ITokens::setValue (renamed to setValueS) grep -rn "->setValue(" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035770
include="*.cpp" --include="*.h" # carb::detail::defineTupleCommon grep -rn "carb::detail::defineTupleCommon" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035771
include="*.cpp" --include="*.h" # PyObjectVTable::get()->typeName grep -rn "PyObjectVTable" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035772
include="*.cpp" --include="*.h" # acquireInterface (prefer getCachedInterface) grep -rn "acquireInterface" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035773
include="*.cpp" --include="*.h" # carb::extras::Path implicit conversion grep -rn "carb::extras::Path\|carb::fs::Path" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035774
include="*.cpp" --include="*.h" # Assert macros (may need explicit carb/Assert.h now) grep -rn "CARB_ASSERT\|CARB_FATAL_UNLESS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035775
include="*.cpp" --include="*.h" # Library.h removed functions grep -rn "getDefaultLibraryPrefix\|getDefaultLibraryExtension" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035776
include="*.cpp" --include="*.h" # GfMatrix usage (imprecise overloads removed) grep -rn "GfMatrix" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035777
include="*.cpp" --include="*.h" # ILayers.h inclusion (ABI 1.0 → 1.1 recompile required) grep -rn "ILayers\.h\|omni/kit/usd/layers" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035778
include="*.cpp" --include="*.h" # carb.events const char* usage (deprecated — prefer string_view) grep -rn "carb::events::\|IEventQueue\|IEvents" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035779
include="*.cpp" --include="*.h" # Scalar xform ops — code that iterates over xform ops assuming vector types grep -rn "GetOrderedXformOps\|xformOp:translate\|xformOp:scale\|xformOp:rotate" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035780
include="*.cpp" --include="*.h" --include="*.py" # === Stage 3 (108→109) === # Fabric TokenC/PathC (removed; also kUninitializedToken/Path) grep -rn "TokenC\|PathC\|TokenId\|PathId\|kUninitializedToken\|kUninitializedPath" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035781
include="*.cpp" --include="*.h" # carb::cpp17 / carb::cpp20 (merged to carb::cpp) grep -rn "carb::cpp17\|carb::cpp20" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035782
include="*.cpp" --include="*.h" # carb::thread::shared_lock (removed) grep -rn "carb::thread::shared_lock" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035783
include="*.cpp" --include="*.h" # IDictionary::MakeAtPathS (renamed to MakeAtPath) grep -rn "MakeAtPathS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035784
include="*.cpp" --include="*.h" # compareStringsNoCase (renamed) grep -rn "compareStringsNoCase" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035785
include="*.cpp" --include="*.h" # Logger (superseded by Logger2) grep -rn "carb::logging::Logger[^2]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035786
include="*.cpp" --include="*.h" # MDL/Neuray usage (ABI 56 → 57 recompile required) grep -rn "omni\.mdl\|Neuray\|MDL.*SDK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035787
include="*.cpp" --include="*.h" --include="*.toml" # CloudXR / XRCloudXRBindings grep -rn "CloudXR\|XRCloudXRBindings\|IOpenXRRuntime" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035788
include="*.cpp" --include="*.h" # === Stage 4 (109→110) === # CARB_CHECK (replaced by CARB_RELEASE_ASSERT) grep -rn "CARB_CHECK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035789
include="*.cpp" --include="*.h" # carb/Defines.h (split into sub-headers) grep -rn '#include.*carb/Defines\.h' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035790
include="*.cpp" --include="*.h" # IFileSystem raw char* methods grep -rn "IFileSystem" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035791
include="*.cpp" --include="*.h" # ITokens (unsafe methods removed; ITokens 2.0 available) grep -rn "ITokens\|->resolveString\|->setValue" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035792
include="*.cpp" --include="*.h" # optional / expected — semantics changed (if(b) now tests presence) grep -rn "optional \|expected **Important:** Also scan `templates/`, `launcher-configs/`, and any ETM lock files (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035793
`omni.all.template.extensions.kit`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035794
These contain real dependency declarations and will cause test or runtime failures if they reference removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035795
```bash # === All stages — removed/deprecated extensions === # Kit 108 removals grep -rn "omni\.kit\.extpath\.git" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035796
include="*.toml" --include="*.kit" # Kit 108 — monolithic livestream (split into modules) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035797
include="*.toml" --include="*.kit" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035798
include="*.toml" --include="*.kit" # Kit 110 removals (cause cryptic exit-55 dependency solver failures) for ext in omni.kvdb omni.localcache omni.genproc.core; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035799
include="*.kit" --include="*.toml" done # Kit 110 silently removed (no deprecation notice) for ext in "omni.hydra.iray.shadercache.d3d12" "omni.hydra.iray.shadercache.vulkan" "omni.kit.viewport.iray"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035800
include="*.kit" --include="*.toml" done # Deprecated (not yet removed — still operational but plan migration) for ext in "omni.command.usd" "omni.debugdraw" "omni.hydra.iray" "omni.iray.settings.core" \ "omni.kit.autocapture" "omni.kit.manipulator.viewport" "omni.hydra.scene_api" \ "omni.renderer_capture" "omni.surface_instancer" "omni.kit.viewport.legacy_gizmos" \ "omni.kit.widget.nucleus_connector"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035801
include="*.kit" --include="*.toml" done # Extensions that need explicit declaration (no longer loaded transitively) grep -rn "omni\.kit\.manipulator\.prim\.fabric\|omni\.resourcemonitor\|omni\.kit\.ui" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035802
\ --include="*.py" --include="*.toml" ``` ### Config Files ```bash # Extension registry URLs (must update for Kit 110) grep -rn "kit-extensions\.ov\.nvidia\.com\|omniverse://" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035803
include="*.kit" # Build system (VS version) — also check CI-scoped token overrides # (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035804
"token:in_ci==true".vs_version may override the default even when the top-level is correct) grep -rn "vs_version\|vs2019\|vs2017\|v142" repo.toml # Livestream settings (old path style) grep -rn "app/livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035805
include="*.kit" --include="*.toml" # Kit SDK version pin (use the $DEPS_DIR detected in Step 1) cat "$DEPS_DIR/kit-sdk.packman.xml" # mergeMaterials (behavioral default change in 109) grep -rn "mergeMaterials" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035806
include="*.kit" --include="*.toml" # FSD / Fabric Scene Delegate settings grep -rn "FabricSceneDelegate\|fsd\b" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035807
include="*.kit" --include="*.toml" ``` ### OmniGraph ```bash # === Stage 2 (107→108) — OmniGraph 3.0 ABI === grep -rn "omni\.graph\.core\|omni\.graph\.nodes" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035808
include="*.toml" # === Stage 4 (109→110) — deprecated/removed OmniGraph nodes === # DeformedPointsToHydra — removed (was part of OmniHydra) grep -rn "DeformedPointsToHydra" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035809
include="*.py" --include="*.usd" --include="*.usda" # OnCustomEvent bundle attributes deprecated grep -rn "OnCustomEvent" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035810
include="*.py" --include="*.usd" --include="*.usda" # Bundle/attribute manipulation nodes deprecated grep -rn "ArrayGetSize\|AttributeType\|BundleConstructor\|CopyAttribute\|ExtractPrim\|GetAttributeNames\|HasAttribute\|InsertAttribute\|RemoveAttribute\|RenameAttribute" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035811
include="*.py" --include="*.usd" --include="*.usda" # Event/render pipeline nodes deprecated grep -rn "UpdateTickEvent\|GpuInteropCudaEntry\|RenderPreprocessEntry\|RpResourceExample" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035812
include="*.py" --include="*.usd" --include="*.usda" ``` ### Isaac Sim Projects If the project uses Isaac Sim extensions, scan for the `omni.isaac.*` namespace migration (applies Kit 107+): ```bash # omni.isaac.* imports (deprecated → isaacsim.*) grep -rn "omni\.isaac\." .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035813
include="*.py" --include="*.toml" --include="*.kit" # omni.replicator.isaac (→ isaacsim.replicator.*) grep -rn "omni\.replicator\.isaac" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035814
include="*.py" --include="*.toml" # Dynamic Control Toolbox (removed as compile-time dep) grep -rn "dynamic_control\|DynamicControl" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035815
include="*.py" --include="*.cpp" --include="*.h" # SemanticsAPI (→ UsdSemantics.LabelsAPI) grep -rn "add_update_semantics\|SemanticsAPI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 035816
Step 5: Apply Fixes > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035817
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035818
> **Within-major / feature→production upgrade?** Run **only items 1, 2, 8** below (plus item 3 *if* a feature↔production registry swap is needed), then Step 6 (`validate.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035819
Skip items 4–7** — they apply only when a major boundary is crossed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035820
See "Within-major upgrades" under Step 2 in `../SKILL.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035821
Get user approval before modifying files.** Then apply in this order (a full major-boundary upgrade runs all eight): 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035822
Clear extscache** first: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035823
Update version pin** in `$DEPS_DIR/kit-sdk.packman.xml` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035824
Update registry URLs** in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035825
Replace deprecated APIs** using patterns in `../references/api_replacements.json` — these are safe regex replacements 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035826
Remove deprecated extension deps** from `extension.toml` and `.kit` files (see `../references/removed_extensions.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035827
For 109→110 specifically:** the following six extensions are removed with **no deprecation notice**, and any lingering reference causes a cryptic `exit code 55` dependency-solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035828
They MUST be removed from every `.kit` (and `extension.toml`) file: - `omni.kvdb` - `omni.localcache` - `omni.genproc.core` - `omni.hydra.iray.shadercache.d3d12` - `omni.hydra.iray.shadercache.vulkan` - `omni.kit.viewport.iray` ⚠️ **Check the generated version-lock block, not just `[dependencies]`.** In application `.kit` files these names almost always appear in the auto-generated `[settings.app.exts] enabled = [...]` lock (pinned at the old version, e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035829
`omni.kvdb-109.0.10`), **not** the hand-authored dependency list.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035830
Clearing extscache (step 1) does NOT remove them** — you must regenerate the lock: delete the `# BEGIN GENERATED PART` … `# END GENERATED PART` block (the `.kit` says "Remove from 'BEGIN' to 'END' to regenerate") and run `$BUILD precache_exts -c release` so it is rebuilt without the removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035831
Then confirm a clean rebuild (the version stamp should advance to 110 and the six names should be gone).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035832
(If you are working in an internal `kit-app-template` checkout, the ETM lock file `templates/omni.all.template.extensions.kit` and any internal-registry entries are KAT-internal — wrapped in `# AUTOREMOVE` and stripped from external releases by `repo stage_for_github` — so external customer projects will not contain them.) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035833
Add explicit deps** where transitive loading was removed: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035834
Update build config** in `repo.toml` (VS version, MSVC version, Windows SDK — see `../references/config_changes.json`) 8.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035835
Step 2.5: Update the Build Toolchain (highest-impact — often the real work) > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035836
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035837
Run this **before** touching source code — for a within-major / feature→production bump it is usually the *only* substantive work.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035838
> **Key principle:** the most valuable part of an upgrade is usually **not** the code changes — it is making sure the project's **tooling** is correctly updated (repo scripts, `repo_man`/repoman, dependency versions).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035839
This step is therefore **first-class for every upgrade**, and the *primary* step for within-major / branch-transition bumps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035840
Run it **before** touching source code.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035841
Why it matters:** the Kit kernel pin and the repo toolchain are coupled.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035842
Bumping `kit-sdk.packman.xml` alone frequently fails because packman tokens (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035843
`${platform_target_abi}`) only resolve under the matching `repo_man`, and newer kernels expect newer `repo_build` / `repo_kit_tools`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035844
A pin bump *without* a toolchain bump produces cryptic pull/resolve failures — e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035845
`Package not found ...gl.linux-x86_64` or `No versions of … = `.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035846
The toolchain = these files** (see `../references/toolchain.json`): - `$DEPS_DIR/repo-deps.packman.xml` — the `repo_*` tools: `repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_tools_internal`, `repo_kit_template`, `repo_usd`, `repo_format`, `repo_test`, `repo_package`, `repo_ci`, etc.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035847
`$DEPS_DIR/kit-sdk.packman.xml` — the kit-kernel pin (updated in Step 5, item 2 — see `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035848
`tools/packman/` — the packman bootstrap (`packman`, `packman.cmd`, `bootstrap/`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035849
`repo.sh` / `repo.bat` — the repo wrappers (may need regenerating under a newer `repo_man`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035850
`repo.toml` — build config (VS/MSVC/WinSDK for Stage 4; see `../references/config_changes.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035851
How to find the correct target versions — do NOT guess:** 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035852
Get a **reference project already on the target Kit version** — the matching `kit-app-template` or `kit-sdk-public` branch for that Kit line, or the target Kit SDK release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035853
Read its `repo-deps.packman.xml`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035854
Prefer the `production/ ` branch** — it carries the vetted, most-current toolchain for that release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035855
⚠️ **Toolchain versions track the branch's maintenance cadence, not the kernel number** — a newer kernel line can ship an *older* toolchain (in kit-sdk-public, `feature/main` pins kernel 110.4 with `repo_man` 2.6.4, while the maintained `production/110.1` pins kernel 110.1.3 with a *newer* `repo_man` 2.9.3).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035856
Always read the target branch's **actual** pins; never assume "newer Kit = newer tools".
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035857
(Those version numbers are an illustrative snapshot read in 2026 — they **will** go stale; verify against the live branch, do not copy them.)* 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035858
Diff** the project's `$DEPS_DIR/repo-deps.packman.xml` against the reference and align each `repo_*` tool `version=` to the reference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035859
Do the same for `tools/packman/` if it differs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035860
Apply the versions, then do a **clean rebuild** (Step 6 — see `validate.md`) — the toolchain bump must land before the kernel pin resolves cleanly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035861
> This step is safe to run and validate (Step 6) **on its own, first**.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035862
Many "the upgrade won't build" error loops are nothing more than a stale toolchain — fixing it up front avoids chasing phantom code errors.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 035863
Step 4: Generate Upgrade Report > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035864
Run after the Step 3 scans (`scan.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035865
Present findings organized by severity.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035866
Use exact `file:line` references from scan output.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035867
``` ## Upgrade Report: Kit [FROM] → [TO] Project: [path] Migration stages applied: [e.g., Stage 2 + 3 + 4] ### ❌ Breaking Changes (must fix — build or load will fail) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035868
[file:line] — [description] → [exact fix] ### ⚠️ Behavioral Changes (no error, but may affect output or performance) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035869
[file:line] — [description] → [fix or test required] ### 🔔 Deprecated Usage (should fix — will break in next version) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035870
[file:line] — [description] → [fix] ### ✅ Not Affected - [List the `id` or `title` from `breaking_changes.json` for each pattern that was scanned and returned no matches.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035871
This serves as a record that the check was performed, not just skipped.] ### 📋 Required Steps Regardless of Code Changes 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035872
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035873
Update `kit-sdk.packman.xml`: change version pin to `[TO].x.y+feature.${platform_target_abi}.${config}` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035874
Update extension registry URLs in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035875
Rebuild all C++ extensions (ABI break at every stage — required even with no source changes) 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035876
Regenerate version lock blocks in `.kit` files: `$BUILD precache_exts -c release` (substitute the build entrypoint detected in Step 1 — `./repo.sh` may not exist on a custom/integrated build) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035877
If project has an ETM lock file (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035878
`omni.all.template.extensions.kit`), regenerate it or manually remove entries for removed extensions 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035879
[stage-specific items, e.g., VS2022 for Stage 4] ### 🧪 Behavioral Tests Required 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035880
[scenes with DomeLights — orientation regression (Stage 3, but inherited in all later stages)] 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035881
[load performance with mergeMaterials setting (Stage 3)] 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035882
[render output with FSD enabled (Stage 3)] 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035883
[MaterialX materials (Stage 4)] 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035884
[transform-heavy workflows after scalar xform ops change (Stage 2)] ``` **Prioritize for the user:** Extension removal errors and ABI rebuild requirements are the most common causes of project failures after a version bump.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 035885
Important Notes by Stage > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035886
Per-stage reference for the breaking changes summarized in the Step 2 migration table.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035887
Read the stages that apply to the boundaries you cross.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035888
Stage 1: 106 → 107 - **Rebuild required** — Linux ABI changed (`_GLIBCXX_USE_CXX11_ABI=0` → `=1`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035889
All prebuilt `.so` files will fail to load.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035890
packman XML token**: Update the kit-kernel pin token to `${platform_target_abi}` in all `.packman.xml` files.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035891
Kit 106 uses the **`${platform}`** form (not `${platform_target}`); both must become `${platform_target_abi}`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035892
Build-verified:* leaving the old token makes the kit-kernel pull fail immediately with `Package not found on specified remote servers (…gl.linux-x86_64.release)`, because Kit 107's kernel is published only under the ABI string (`manylinux_2_35_x86_64`), not `linux-x86_64`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035893
Bump the repo toolchain too (required, easy to miss)** — see **Step 2.5** (`toolchain.md`): the token fix alone is **insufficient** — `${platform_target_abi}` only resolves to the ABI string under the newer `repo_man`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035894
Update `$DEPS_DIR/repo-deps.packman.xml` to the 107-era tooling (`repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_template`, `repo_usd`) and the packman bootstrap.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035895
Build-verified:* under 106.5's `repo_man` 1.86.0 the token still resolves to `linux-x86_64`; after the toolchain bump it resolves to `manylinux_2_35_x86_64` and the pull succeeds.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035896
Carbonite Events 2.0**: The event system changed from push/pump to dispatch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035897
No explicit pump calls needed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035898
Python payload access changed from `e.payload['key']` to `e['key']`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035899
C++17 is now available** explicitly in Premake via `cppdialect = "C++17"`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035900
Stage 2: 107 → 108 - **Kit 108 was never publicly released.** These changes still apply when upgrading 107→109.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035901
Python 3.12** replaces 3.11.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035902
Update all Premake configs, CI configs, and boost_python links.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035903
OpenUSD 25.02**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035904
GfMatrix imprecise overloads removed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035905
Livestream modularization**: `omni.kit.livestream` (monolithic) → `omni.kit.livestream.app` + `.aov` + `.core`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035906
`omni.services.livestream.nvcf` → `omni.services.livestream.session`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035907
Settings paths changed — see `../references/config_changes.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035908
Transitive deps removed**: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` must now be declared explicitly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035909
ILayers ABI 1.0 → 1.1**: Recompile all extensions including `ILayers.h`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035910
USD scalar xform ops**: OpenUSD now supports scalar ops (e.g., `xformOp:translateX`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035911
Code iterating over xform ops that assumes all are vector types may behave incorrectly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035912
Stage 3: 108 → 109 - **CUDA 12.4.1 driver requirement**: Linux minimum 550.54.15, Windows minimum 551.78.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035913
Apps fail to start with older drivers.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035914
NumPy 2.x**: Many breaking changes.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035915
On Windows, the default integer type changed from `int32` to `int64` — can cause silent correctness issues.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035916
Fabric ABI break**: Even if no source changes needed (no TokenC/PathC usage), all extensions including Fabric headers must recompile — `Token`/`Path` became trivially copyable, which is a binary ABI change.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035917
Use `token.isNull()` instead of `kUninitializedToken`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035918
mimalloc (Windows)**: Cross-DLL allocation/free pairs that cross a DLL boundary may now crash.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035919
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035920
mergeMaterials**: Default changed — can cause significant load time regression with no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035921
FSD default on**: If previously disabled FSD, test render output carefully.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035922
DomeLight orientation**: USD 25.05 changed the default orientation.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035923
Visual change only — no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035924
Use `UpgradeUsdLuxLightsCommand` for assisted migration.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035925
Stage 4: 109 → 110 - **Clear extscache first** — stale Kit 109 entries cause exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035926
Silent extension removals**: `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.d3d12`, `omni.hydra.iray.shadercache.vulkan`, `omni.kit.viewport.iray` — all removed with no deprecation notice.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035927
First symptom is a cryptic exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035928
Remove every reference from `.kit`/`extension.toml` files — including the auto-generated `[settings.app.exts] enabled = [...]` version-lock block, where they usually hide pinned at the old version (clearing extscache alone won't drop them; regenerate the lock with `precache_exts` — see Step 5, item 5 in `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035929
Also scan `templates/` and ETM lock files** — these are easily missed by `source/`-only scans.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035930
DomeLight orientation (inherited from Stage 3)**: If the project contains DomeLights and was not verified during a previous Stage 3 upgrade, the USD 25.05 orientation change is a permanent behavioral difference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035931
Search with `grep -rn 'DomeLight' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035932
include='*.py' --include='*.usd'` and use `UpgradeUsdLuxLightsCommand` if scenes were not migrated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035933
`optional ` semantics**: `if(b)` now tests *presence*, not *value*.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035934
Code that previously worked may now be wrong silently.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035935
`g_carbClientName`**: Type changed to `zstring_view`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035936
Any direct string assignment or comparison breaks.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035937
Hydra 2 removed**: No migration path.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035938
Hydra 1 (Storm) and RTX remain.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035939
OmniGraph bundle nodes**: Large set of bundle/attribute manipulation nodes deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035940
Deprecation warnings visible in editor from Kit 110.1+.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035941
`AttributeType` → `GetAttributeType`, `ArrayGetSize` → `ArrayLength`, `ExtractPrim` → `ReadPrim`, `GetAttributeNames` → `ReadPrimAttributes`, `InsertAttribute` → `WritePrimAttribute`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035942
`BundleConstructor`, `RemoveAttribute`, `RenameAttribute` have no direct replacement — redesign graphs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035943
OpenUSD 25.11**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035944
Ndr/Sdr libraries consolidated — update include paths.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035945
VS2022 required** on Windows (was VS2019).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035946
New extensions in Kit 110**: `omni.grpc.lib`, `omni.protobuf.lib`, `omni.sensors.nv.*` (camera/lidar/radar/ultrasonic/ids/wpm), `omni.kit.xr.core` — available for use in Kit 110 apps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 035947
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035948
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035949
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035950
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035951
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035952
Select the desired UI based application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035953
The developer bundle is not currently suitable for headless services.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035954
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035955
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035956
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035957
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035958
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035959
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035960
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035961
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035962
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035963
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035964
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035965
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035966
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035967
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035968
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035969
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035970
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035971
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035972
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035973
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035974
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035975
What Are Application Layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035976
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035977
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035978
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035979
``` Answer `yes` to enable streaming for your application.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035980
You can then pick from the following streaming layers: ```bash ?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035981
Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035982
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035983
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035984
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035985
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035986
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035987
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035988
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035989
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035990
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035991
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035992
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035993
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035994
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 035995
Testing Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is an extension — including the `.kit` files that define applications.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035996
The `test` tool (`repo_test`) reflects this: it validates that your applications start up and shut down cleanly, and it runs the automated tests defined within your extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035997
Each extension template provided by the `kit-app-template` repository ships with sample tests that you can expand to grow your coverage.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035998
This document covers running tests, understanding what is tested, and adding your own tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 035999
Prerequisites: Build Before You Test The test tool runs against the contents of the `_build` directory, so a successful build must precede any test run.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 036000
If you have changed source since your last build, rebuild first.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।
