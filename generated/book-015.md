# डिजिटल महाग्रंथ 015

स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।

## 014001
premake5.lua repo.toml --include="*.lua" --include="*.toml" # packman XML using a pre-ABI token (should be ${platform_target_abi}).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014002
NOTE: match BOTH the old ${platform} form (Kit 106) and the intermediate ${platform_target} form — # the narrower 'platform_target[^_]' pattern misses ${platform}, which is what 106.5 actually uses and # is a build-verified hard failure on 106->107 (kit-kernel pull: "Package not found ...gl.linux-x86_64").
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014003
grep -rnE '\$\{platform(_target)?\}' "$DEPS_DIR" --include="*.xml" # Toolbar deprecated APIs grep -rn "omni\.kit\.widget\.toolbar\|omni\.kit\.window\.toolbar" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014004
include="*.py" --include="*.toml" # === Stage 2 (107→108) === # Python 3.11 references (now 3.12) grep -rn "python3\.11\|python311\|boost_python311" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014005
premake5.lua --include="*.lua" --include="*.sh" --include="*.bat" # get_custom_glyph_code (moved to omni.ui) grep -rn "omni\.kit\.ui.*get_custom_glyph_code" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014006
include="*.py" # WindowHandle deprecated usage grep -rn "WindowHandle" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014007
include="*.py" # menu_compatibility (deprecated in 108, removed in 110) grep -rn "menu_compatibility" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014008
include="*.py" # Layer events (Events 1.0 style) grep -rn "get_event_stream\|create_subscription_to_pop\|carb\.events" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014009
include="*.py" # Livestream extension (monolithic — should be split) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014010
include="*.kit" --include="*.toml" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014011
include="*.kit" --include="*.toml" # Livestream settings (old path) grep -rn "app/livestream\|app\.livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014012
include="*.kit" --include="*.toml" # Old omni.kit.ui transitive usage (no longer loaded transitively) grep -rn "omni\.kit\.ui[^.]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014013
include="*.py" # === Stage 3 (108→109) === # NumPy 1.x type aliases (removed in 2.0) grep -rn "np\.bool[^_]\|np\.int[^0-9_]\|np\.float[^0-9_]\|np\.complex[^0-9_]\|np\.object[^_]\|np\.str[^_]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014014
include="*.py" # === Stage 4 (109→110) === # menu_compatibility (now raises TypeError — must remove entirely) grep -rn "menu_compatibility=" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014015
include="*.py" # omni.usd layers deprecated API grep -rn "get_context()\.get_layers()\|context\.get_layers()" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014016
include="*.py" # omni.renderer_capture (deprecated → omni.kit.capture) grep -rn "omni\.renderer_capture" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014017
include="*.py" # USD displayName/displayGroup/hidden deprecated metadata grep -rn "GetMetadata.*displayName\|SetMetadata.*displayName\|GetMetadata.*hidden\|SetMetadata.*hidden\|GetMetadata.*displayGroup\|SetMetadata.*displayGroup" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014018
include="*.py" ``` ### C++ / Native Code ```bash # === Stage 1 (106→107) === # C++ ABI — check for _GLIBCXX_USE_CXX11_ABI overrides (must be =1) grep -rn "_GLIBCXX_USE_CXX11_ABI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014019
include="*.cpp" --include="*.h" --include="*.cmake" # === Stage 2 (107→108) === # ITokens::setValue (renamed to setValueS) grep -rn "->setValue(" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014020
include="*.cpp" --include="*.h" # carb::detail::defineTupleCommon grep -rn "carb::detail::defineTupleCommon" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014021
include="*.cpp" --include="*.h" # PyObjectVTable::get()->typeName grep -rn "PyObjectVTable" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014022
include="*.cpp" --include="*.h" # acquireInterface (prefer getCachedInterface) grep -rn "acquireInterface" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014023
include="*.cpp" --include="*.h" # carb::extras::Path implicit conversion grep -rn "carb::extras::Path\|carb::fs::Path" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014024
include="*.cpp" --include="*.h" # Assert macros (may need explicit carb/Assert.h now) grep -rn "CARB_ASSERT\|CARB_FATAL_UNLESS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014025
include="*.cpp" --include="*.h" # Library.h removed functions grep -rn "getDefaultLibraryPrefix\|getDefaultLibraryExtension" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014026
include="*.cpp" --include="*.h" # GfMatrix usage (imprecise overloads removed) grep -rn "GfMatrix" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014027
include="*.cpp" --include="*.h" # ILayers.h inclusion (ABI 1.0 → 1.1 recompile required) grep -rn "ILayers\.h\|omni/kit/usd/layers" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014028
include="*.cpp" --include="*.h" # carb.events const char* usage (deprecated — prefer string_view) grep -rn "carb::events::\|IEventQueue\|IEvents" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014029
include="*.cpp" --include="*.h" # Scalar xform ops — code that iterates over xform ops assuming vector types grep -rn "GetOrderedXformOps\|xformOp:translate\|xformOp:scale\|xformOp:rotate" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014030
include="*.cpp" --include="*.h" --include="*.py" # === Stage 3 (108→109) === # Fabric TokenC/PathC (removed; also kUninitializedToken/Path) grep -rn "TokenC\|PathC\|TokenId\|PathId\|kUninitializedToken\|kUninitializedPath" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014031
include="*.cpp" --include="*.h" # carb::cpp17 / carb::cpp20 (merged to carb::cpp) grep -rn "carb::cpp17\|carb::cpp20" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014032
include="*.cpp" --include="*.h" # carb::thread::shared_lock (removed) grep -rn "carb::thread::shared_lock" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014033
include="*.cpp" --include="*.h" # IDictionary::MakeAtPathS (renamed to MakeAtPath) grep -rn "MakeAtPathS" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014034
include="*.cpp" --include="*.h" # compareStringsNoCase (renamed) grep -rn "compareStringsNoCase" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014035
include="*.cpp" --include="*.h" # Logger (superseded by Logger2) grep -rn "carb::logging::Logger[^2]" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014036
include="*.cpp" --include="*.h" # MDL/Neuray usage (ABI 56 → 57 recompile required) grep -rn "omni\.mdl\|Neuray\|MDL.*SDK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014037
include="*.cpp" --include="*.h" --include="*.toml" # CloudXR / XRCloudXRBindings grep -rn "CloudXR\|XRCloudXRBindings\|IOpenXRRuntime" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014038
include="*.cpp" --include="*.h" # === Stage 4 (109→110) === # CARB_CHECK (replaced by CARB_RELEASE_ASSERT) grep -rn "CARB_CHECK" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014039
include="*.cpp" --include="*.h" # carb/Defines.h (split into sub-headers) grep -rn '#include.*carb/Defines\.h' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014040
include="*.cpp" --include="*.h" # IFileSystem raw char* methods grep -rn "IFileSystem" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014041
include="*.cpp" --include="*.h" # ITokens (unsafe methods removed; ITokens 2.0 available) grep -rn "ITokens\|->resolveString\|->setValue" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014042
include="*.cpp" --include="*.h" # optional / expected — semantics changed (if(b) now tests presence) grep -rn "optional \|expected **Important:** Also scan `templates/`, `launcher-configs/`, and any ETM lock files (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014043
`omni.all.template.extensions.kit`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014044
These contain real dependency declarations and will cause test or runtime failures if they reference removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014045
```bash # === All stages — removed/deprecated extensions === # Kit 108 removals grep -rn "omni\.kit\.extpath\.git" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014046
include="*.toml" --include="*.kit" # Kit 108 — monolithic livestream (split into modules) grep -rn '"omni\.kit\.livestream"' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014047
include="*.toml" --include="*.kit" grep -rn "omni\.services\.livestream\.nvcf" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014048
include="*.toml" --include="*.kit" # Kit 110 removals (cause cryptic exit-55 dependency solver failures) for ext in omni.kvdb omni.localcache omni.genproc.core; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014049
include="*.kit" --include="*.toml" done # Kit 110 silently removed (no deprecation notice) for ext in "omni.hydra.iray.shadercache.d3d12" "omni.hydra.iray.shadercache.vulkan" "omni.kit.viewport.iray"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014050
include="*.kit" --include="*.toml" done # Deprecated (not yet removed — still operational but plan migration) for ext in "omni.command.usd" "omni.debugdraw" "omni.hydra.iray" "omni.iray.settings.core" \ "omni.kit.autocapture" "omni.kit.manipulator.viewport" "omni.hydra.scene_api" \ "omni.renderer_capture" "omni.surface_instancer" "omni.kit.viewport.legacy_gizmos" \ "omni.kit.widget.nucleus_connector"; do echo "=== $ext ==="; grep -rn "$ext" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014051
include="*.kit" --include="*.toml" done # Extensions that need explicit declaration (no longer loaded transitively) grep -rn "omni\.kit\.manipulator\.prim\.fabric\|omni\.resourcemonitor\|omni\.kit\.ui" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014052
\ --include="*.py" --include="*.toml" ``` ### Config Files ```bash # Extension registry URLs (must update for Kit 110) grep -rn "kit-extensions\.ov\.nvidia\.com\|omniverse://" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014053
include="*.kit" # Build system (VS version) — also check CI-scoped token overrides # (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014054
"token:in_ci==true".vs_version may override the default even when the top-level is correct) grep -rn "vs_version\|vs2019\|vs2017\|v142" repo.toml # Livestream settings (old path style) grep -rn "app/livestream" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014055
include="*.kit" --include="*.toml" # Kit SDK version pin (use the $DEPS_DIR detected in Step 1) cat "$DEPS_DIR/kit-sdk.packman.xml" # mergeMaterials (behavioral default change in 109) grep -rn "mergeMaterials" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014056
include="*.kit" --include="*.toml" # FSD / Fabric Scene Delegate settings grep -rn "FabricSceneDelegate\|fsd\b" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014057
include="*.kit" --include="*.toml" ``` ### OmniGraph ```bash # === Stage 2 (107→108) — OmniGraph 3.0 ABI === grep -rn "omni\.graph\.core\|omni\.graph\.nodes" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014058
include="*.toml" # === Stage 4 (109→110) — deprecated/removed OmniGraph nodes === # DeformedPointsToHydra — removed (was part of OmniHydra) grep -rn "DeformedPointsToHydra" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014059
include="*.py" --include="*.usd" --include="*.usda" # OnCustomEvent bundle attributes deprecated grep -rn "OnCustomEvent" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014060
include="*.py" --include="*.usd" --include="*.usda" # Bundle/attribute manipulation nodes deprecated grep -rn "ArrayGetSize\|AttributeType\|BundleConstructor\|CopyAttribute\|ExtractPrim\|GetAttributeNames\|HasAttribute\|InsertAttribute\|RemoveAttribute\|RenameAttribute" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014061
include="*.py" --include="*.usd" --include="*.usda" # Event/render pipeline nodes deprecated grep -rn "UpdateTickEvent\|GpuInteropCudaEntry\|RenderPreprocessEntry\|RpResourceExample" \ .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014062
include="*.py" --include="*.usd" --include="*.usda" ``` ### Isaac Sim Projects If the project uses Isaac Sim extensions, scan for the `omni.isaac.*` namespace migration (applies Kit 107+): ```bash # omni.isaac.* imports (deprecated → isaacsim.*) grep -rn "omni\.isaac\." .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014063
include="*.py" --include="*.toml" --include="*.kit" # omni.replicator.isaac (→ isaacsim.replicator.*) grep -rn "omni\.replicator\.isaac" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014064
include="*.py" --include="*.toml" # Dynamic Control Toolbox (removed as compile-time dep) grep -rn "dynamic_control\|DynamicControl" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014065
include="*.py" --include="*.cpp" --include="*.h" # SemanticsAPI (→ UsdSemantics.LabelsAPI) grep -rn "add_update_semantics\|SemanticsAPI" .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/scan.md · स्वतंत्र परीक्षण अपेक्षित।

## 014066
Step 5: Apply Fixes > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014067
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014068
> **Within-major / feature→production upgrade?** Run **only items 1, 2, 8** below (plus item 3 *if* a feature↔production registry swap is needed), then Step 6 (`validate.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014069
Skip items 4–7** — they apply only when a major boundary is crossed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014070
See "Within-major upgrades" under Step 2 in `../SKILL.md`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014071
Get user approval before modifying files.** Then apply in this order (a full major-boundary upgrade runs all eight): 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014072
Clear extscache** first: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014073
Update version pin** in `$DEPS_DIR/kit-sdk.packman.xml` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014074
Update registry URLs** in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014075
Replace deprecated APIs** using patterns in `../references/api_replacements.json` — these are safe regex replacements 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014076
Remove deprecated extension deps** from `extension.toml` and `.kit` files (see `../references/removed_extensions.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014077
For 109→110 specifically:** the following six extensions are removed with **no deprecation notice**, and any lingering reference causes a cryptic `exit code 55` dependency-solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014078
They MUST be removed from every `.kit` (and `extension.toml`) file: - `omni.kvdb` - `omni.localcache` - `omni.genproc.core` - `omni.hydra.iray.shadercache.d3d12` - `omni.hydra.iray.shadercache.vulkan` - `omni.kit.viewport.iray` ⚠️ **Check the generated version-lock block, not just `[dependencies]`.** In application `.kit` files these names almost always appear in the auto-generated `[settings.app.exts] enabled = [...]` lock (pinned at the old version, e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014079
`omni.kvdb-109.0.10`), **not** the hand-authored dependency list.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014080
Clearing extscache (step 1) does NOT remove them** — you must regenerate the lock: delete the `# BEGIN GENERATED PART` … `# END GENERATED PART` block (the `.kit` says "Remove from 'BEGIN' to 'END' to regenerate") and run `$BUILD precache_exts -c release` so it is rebuilt without the removed extensions.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014081
Then confirm a clean rebuild (the version stamp should advance to 110 and the six names should be gone).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014082
(If you are working in an internal `kit-app-template` checkout, the ETM lock file `templates/omni.all.template.extensions.kit` and any internal-registry entries are KAT-internal — wrapped in `# AUTOREMOVE` and stripped from external releases by `repo stage_for_github` — so external customer projects will not contain them.) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014083
Add explicit deps** where transitive loading was removed: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014084
Update build config** in `repo.toml` (VS version, MSVC version, Windows SDK — see `../references/config_changes.json`) 8.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/apply-fixes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014085
Step 2.5: Update the Build Toolchain (highest-impact — often the real work) > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014086
Assumes Step 1 detection has run (`$DEPS_DIR`, `$BUILD` are set).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014087
Run this **before** touching source code — for a within-major / feature→production bump it is usually the *only* substantive work.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014088
> **Key principle:** the most valuable part of an upgrade is usually **not** the code changes — it is making sure the project's **tooling** is correctly updated (repo scripts, `repo_man`/repoman, dependency versions).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014089
This step is therefore **first-class for every upgrade**, and the *primary* step for within-major / branch-transition bumps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014090
Run it **before** touching source code.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014091
Why it matters:** the Kit kernel pin and the repo toolchain are coupled.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014092
Bumping `kit-sdk.packman.xml` alone frequently fails because packman tokens (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014093
`${platform_target_abi}`) only resolve under the matching `repo_man`, and newer kernels expect newer `repo_build` / `repo_kit_tools`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014094
A pin bump *without* a toolchain bump produces cryptic pull/resolve failures — e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014095
`Package not found ...gl.linux-x86_64` or `No versions of … = `.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014096
The toolchain = these files** (see `../references/toolchain.json`): - `$DEPS_DIR/repo-deps.packman.xml` — the `repo_*` tools: `repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_tools_internal`, `repo_kit_template`, `repo_usd`, `repo_format`, `repo_test`, `repo_package`, `repo_ci`, etc.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014097
`$DEPS_DIR/kit-sdk.packman.xml` — the kit-kernel pin (updated in Step 5, item 2 — see `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014098
`tools/packman/` — the packman bootstrap (`packman`, `packman.cmd`, `bootstrap/`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014099
`repo.sh` / `repo.bat` — the repo wrappers (may need regenerating under a newer `repo_man`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014100
`repo.toml` — build config (VS/MSVC/WinSDK for Stage 4; see `../references/config_changes.json`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014101
How to find the correct target versions — do NOT guess:** 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014102
Get a **reference project already on the target Kit version** — the matching `kit-app-template` or `kit-sdk-public` branch for that Kit line, or the target Kit SDK release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014103
Read its `repo-deps.packman.xml`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014104
Prefer the `production/ ` branch** — it carries the vetted, most-current toolchain for that release.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014105
⚠️ **Toolchain versions track the branch's maintenance cadence, not the kernel number** — a newer kernel line can ship an *older* toolchain (in kit-sdk-public, `feature/main` pins kernel 110.4 with `repo_man` 2.6.4, while the maintained `production/110.1` pins kernel 110.1.3 with a *newer* `repo_man` 2.9.3).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014106
Always read the target branch's **actual** pins; never assume "newer Kit = newer tools".
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014107
(Those version numbers are an illustrative snapshot read in 2026 — they **will** go stale; verify against the live branch, do not copy them.)* 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014108
Diff** the project's `$DEPS_DIR/repo-deps.packman.xml` against the reference and align each `repo_*` tool `version=` to the reference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014109
Do the same for `tools/packman/` if it differs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014110
Apply the versions, then do a **clean rebuild** (Step 6 — see `validate.md`) — the toolchain bump must land before the kernel pin resolves cleanly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014111
> This step is safe to run and validate (Step 6) **on its own, first**.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014112
Many "the upgrade won't build" error loops are nothing more than a stale toolchain — fixing it up front avoids chasing phantom code errors.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/toolchain.md · स्वतंत्र परीक्षण अपेक्षित।

## 014113
Step 4: Generate Upgrade Report > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014114
Run after the Step 3 scans (`scan.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014115
Present findings organized by severity.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014116
Use exact `file:line` references from scan output.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014117
``` ## Upgrade Report: Kit [FROM] → [TO] Project: [path] Migration stages applied: [e.g., Stage 2 + 3 + 4] ### ❌ Breaking Changes (must fix — build or load will fail) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014118
[file:line] — [description] → [exact fix] ### ⚠️ Behavioral Changes (no error, but may affect output or performance) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014119
[file:line] — [description] → [fix or test required] ### 🔔 Deprecated Usage (should fix — will break in next version) 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014120
[file:line] — [description] → [fix] ### ✅ Not Affected - [List the `id` or `title` from `breaking_changes.json` for each pattern that was scanned and returned no matches.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014121
This serves as a record that the check was performed, not just skipped.] ### 📋 Required Steps Regardless of Code Changes 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014122
Clear extscache: `rm -rf _build/*/release/extscache/` 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014123
Update `kit-sdk.packman.xml`: change version pin to `[TO].x.y+feature.${platform_target_abi}.${config}` 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014124
Update extension registry URLs in `.kit` files (see `../references/config_changes.json`) 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014125
Rebuild all C++ extensions (ABI break at every stage — required even with no source changes) 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014126
Regenerate version lock blocks in `.kit` files: `$BUILD precache_exts -c release` (substitute the build entrypoint detected in Step 1 — `./repo.sh` may not exist on a custom/integrated build) 6.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014127
If project has an ETM lock file (e.g.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014128
`omni.all.template.extensions.kit`), regenerate it or manually remove entries for removed extensions 7.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014129
[stage-specific items, e.g., VS2022 for Stage 4] ### 🧪 Behavioral Tests Required 1.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014130
[scenes with DomeLights — orientation regression (Stage 3, but inherited in all later stages)] 2.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014131
[load performance with mergeMaterials setting (Stage 3)] 3.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014132
[render output with FSD enabled (Stage 3)] 4.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014133
[MaterialX materials (Stage 4)] 5.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014134
[transform-heavy workflows after scalar xform ops change (Stage 2)] ``` **Prioritize for the user:** Extension removal errors and ABI rebuild requirements are the most common causes of project failures after a version bump.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/report.md · स्वतंत्र परीक्षण अपेक्षित।

## 014135
Important Notes by Stage > Part of the **kit-upgrade** skill (see `../SKILL.md` for the workflow).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014136
Per-stage reference for the breaking changes summarized in the Step 2 migration table.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014137
Read the stages that apply to the boundaries you cross.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014138
Stage 1: 106 → 107 - **Rebuild required** — Linux ABI changed (`_GLIBCXX_USE_CXX11_ABI=0` → `=1`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014139
All prebuilt `.so` files will fail to load.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014140
packman XML token**: Update the kit-kernel pin token to `${platform_target_abi}` in all `.packman.xml` files.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014141
Kit 106 uses the **`${platform}`** form (not `${platform_target}`); both must become `${platform_target_abi}`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014142
Build-verified:* leaving the old token makes the kit-kernel pull fail immediately with `Package not found on specified remote servers (…gl.linux-x86_64.release)`, because Kit 107's kernel is published only under the ABI string (`manylinux_2_35_x86_64`), not `linux-x86_64`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014143
Bump the repo toolchain too (required, easy to miss)** — see **Step 2.5** (`toolchain.md`): the token fix alone is **insufficient** — `${platform_target_abi}` only resolves to the ABI string under the newer `repo_man`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014144
Update `$DEPS_DIR/repo-deps.packman.xml` to the 107-era tooling (`repo_man`, `repo_build`, `repo_kit_tools`, `repo_kit_template`, `repo_usd`) and the packman bootstrap.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014145
Build-verified:* under 106.5's `repo_man` 1.86.0 the token still resolves to `linux-x86_64`; after the toolchain bump it resolves to `manylinux_2_35_x86_64` and the pull succeeds.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014146
Carbonite Events 2.0**: The event system changed from push/pump to dispatch.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014147
No explicit pump calls needed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014148
Python payload access changed from `e.payload['key']` to `e['key']`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014149
C++17 is now available** explicitly in Premake via `cppdialect = "C++17"`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014150
Stage 2: 107 → 108 - **Kit 108 was never publicly released.** These changes still apply when upgrading 107→109.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014151
Python 3.12** replaces 3.11.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014152
Update all Premake configs, CI configs, and boost_python links.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014153
OpenUSD 25.02**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014154
GfMatrix imprecise overloads removed.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014155
Livestream modularization**: `omni.kit.livestream` (monolithic) → `omni.kit.livestream.app` + `.aov` + `.core`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014156
`omni.services.livestream.nvcf` → `omni.services.livestream.session`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014157
Settings paths changed — see `../references/config_changes.json`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014158
Transitive deps removed**: `omni.kit.ui`, `omni.resourcemonitor`, `omni.kit.manipulator.prim.fabric` must now be declared explicitly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014159
ILayers ABI 1.0 → 1.1**: Recompile all extensions including `ILayers.h`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014160
USD scalar xform ops**: OpenUSD now supports scalar ops (e.g., `xformOp:translateX`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014161
Code iterating over xform ops that assumes all are vector types may behave incorrectly.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014162
Stage 3: 108 → 109 - **CUDA 12.4.1 driver requirement**: Linux minimum 550.54.15, Windows minimum 551.78.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014163
Apps fail to start with older drivers.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014164
NumPy 2.x**: Many breaking changes.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014165
On Windows, the default integer type changed from `int32` to `int64` — can cause silent correctness issues.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014166
Fabric ABI break**: Even if no source changes needed (no TokenC/PathC usage), all extensions including Fabric headers must recompile — `Token`/`Path` became trivially copyable, which is a binary ABI change.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014167
Use `token.isNull()` instead of `kUninitializedToken`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014168
mimalloc (Windows)**: Cross-DLL allocation/free pairs that cross a DLL boundary may now crash.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014169
Use `kit-sysalloc.exe` for compatibility testing.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014170
mergeMaterials**: Default changed — can cause significant load time regression with no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014171
FSD default on**: If previously disabled FSD, test render output carefully.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014172
DomeLight orientation**: USD 25.05 changed the default orientation.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014173
Visual change only — no code error.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014174
Use `UpgradeUsdLuxLightsCommand` for assisted migration.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014175
Stage 4: 109 → 110 - **Clear extscache first** — stale Kit 109 entries cause exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014176
Silent extension removals**: `omni.kvdb`, `omni.localcache`, `omni.genproc.core`, `omni.hydra.iray.shadercache.d3d12`, `omni.hydra.iray.shadercache.vulkan`, `omni.kit.viewport.iray` — all removed with no deprecation notice.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014177
First symptom is a cryptic exit-55 dependency solver failure.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014178
Remove every reference from `.kit`/`extension.toml` files — including the auto-generated `[settings.app.exts] enabled = [...]` version-lock block, where they usually hide pinned at the old version (clearing extscache alone won't drop them; regenerate the lock with `precache_exts` — see Step 5, item 5 in `apply-fixes.md`).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014179
Also scan `templates/` and ETM lock files** — these are easily missed by `source/`-only scans.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014180
DomeLight orientation (inherited from Stage 3)**: If the project contains DomeLights and was not verified during a previous Stage 3 upgrade, the USD 25.05 orientation change is a permanent behavioral difference.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014181
Search with `grep -rn 'DomeLight' .
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014182
include='*.py' --include='*.usd'` and use `UpgradeUsdLuxLightsCommand` if scenes were not migrated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014183
`optional ` semantics**: `if(b)` now tests *presence*, not *value*.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014184
Code that previously worked may now be wrong silently.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014185
`g_carbClientName`**: Type changed to `zstring_view`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014186
Any direct string assignment or comparison breaks.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014187
Hydra 2 removed**: No migration path.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014188
Hydra 1 (Storm) and RTX remain.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014189
OmniGraph bundle nodes**: Large set of bundle/attribute manipulation nodes deprecated.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014190
Deprecation warnings visible in editor from Kit 110.1+.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014191
`AttributeType` → `GetAttributeType`, `ArrayGetSize` → `ArrayLength`, `ExtractPrim` → `ReadPrim`, `GetAttributeNames` → `ReadPrimAttributes`, `InsertAttribute` → `WritePrimAttribute`.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014192
`BundleConstructor`, `RemoveAttribute`, `RenameAttribute` have no direct replacement — redesign graphs.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014193
OpenUSD 25.11**: All C++ extensions linking OpenUSD must rebuild.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014194
Ndr/Sdr libraries consolidated — update include paths.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014195
VS2022 required** on Windows (was VS2019).
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014196
New extensions in Kit 110**: `omni.grpc.lib`, `omni.protobuf.lib`, `omni.sensors.nv.*` (camera/lidar/radar/ultrasonic/ids/wpm), `omni.kit.xr.core` — available for use in Kit 110 apps.
स्रोत: kit-app-template/.skills/kit-upgrade/procedures/stage-notes.md · स्वतंत्र परीक्षण अपेक्षित।

## 014197
Developer Bundle Extensions ## Overview The Developer Bundle Extension (`omni.kit.developer.bundle`) provides a set of developer focused tools designed to enhance the development and debugging process within Omniverse Kit applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014198
Each of the extensions within the bundle aims streamline a specific aspects of Omniverse application and extension development.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014199
Enabling the Developer Bundle Application templates within the Kit App Template repository have `omni.kit.developer.bundle` configured within the `.kit` file by default.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014200
For applications that do not, the Developer Bundle can be added temporarily at launch time using the `--dev-bundle` or `-d` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014201
Linux** ```bash ./repo.sh launch --dev-bundle ``` **Windows** ```powershell .\repo.bat launch --dev-bundle ``` The `launch` tool will prompt for a selection of a `.kit` file to launch.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014202
Select the desired UI based application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014203
The developer bundle is not currently suitable for headless services.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014204
Developer Bundle Extensions Developer Utilities are designed to assist developers in various aspects of application development, from debugging to extension management.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014205
These utilities offer insight into the internal workings of an application and its extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014206
[Developer > Extensions] omni.kit.window.extensions**: The most popular utility, this tool manages available extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014207
It provides quick access to the extension registry and local extensions, simplifying the process of adding dependencies for developer extensions and applications.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014208
[Developer > Commands] omni.kit.window.commands**: Captures the command history within a running application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014209
It is particularly useful for developers who interact with the UI, allowing them to capture the commands used to execute specific functionalities.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014210
[Developer > Script Editor] omni.kit.window.script_editor**: A simplified script editor for running short code snippets directly within the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014211
It's a helpful tool for testing small pieces of code before integrating them into a project.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014212
Additionally, it offers useful sample scripts that can be executed live.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014213
[Developer > VS Code Link] omni.kit.debug.vscode**: VSCode python debugger support window.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014214
This utility allows developers to step through their python code in VSCode while running the application.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014215
[Developer > Debug Settings] omni.kit.debug.settings**: This utility provides a detailed view of the configurable settings for extensions within an application, making it easier to tweak and optimize extension behavior.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014216
:warning: The Developer Bundle extensions require a UI based application with a menu bar to run properly.
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014217
They will not work as expected for headless services or in applications that do not display a menu bar
स्रोत: kit-app-template/readme-assets/additional-docs/developer_bundle_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014218
Kit Application Streaming ## Overview Kit SDK templates and tooling enable the creation streaming-ready Omniverse Kit applications and aid in the packaging/containerization in preparation for deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014219
This document outlines how to set up, configure, and package Kit applications for a streaming deployment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014220
:warning: **Important :** Creation of containerized streaming applications must be done from a Linux environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014221
Create and Configure an Application Choose a template from the options below, then follow the instructions in the template README.md to create your application using the `template new` command: - **[Kit Base Editor](../../templates/apps/kit_base_editor/)**: A minimal application for loading, manipulating, and rendering OpenUSD content through a graphical interface.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014222
[USD Composer](../../templates/apps/usd_composer)**: A template for authoring complex OpenUSD scenes (e.g., configurators).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014223
[USD Explorer](../../templates/apps/usd_explorer)**: A template for exploring and collaborating on large OpenUSD scenes.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014224
[USD Viewer](../../templates/apps/usd_viewer)**: A streamlined, viewport-only application well-suited for remote streaming to web pages.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014225
What Are Application Layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014226
An **application layer** is a separate `.kit` configuration file that extends your base application for a specific deployment scenario.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014227
Instead of modifying your main application, layers let you create variants optimized for different use cases: - **Base application** (`my_app.kit`): Your core application with all features and UI - **Streaming layer** (`my_app_streaming.kit`): Inherits from base, adds streaming extensions and settings This approach keeps your base application clean while enabling different deployment modes (local desktop, cloud streaming, etc.) from the same codebase.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014228
Adding a Streaming Layer During the templating process, you will be prompted: ```bash Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014229
``` Answer `yes` to enable streaming for your application.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014230
You can then pick from the following streaming layers: ```bash ?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014231
Do you want to add application layers?
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014232
Browse layers with arrow keys ↑↓: [SPACE to toggle selection, ENTER to confirm selection(s)] ❯ [ ] [omni_default_streaming]: Omniverse Kit App Streaming (Default) [ ] [nvcf_streaming]: NVCF Streaming ``` - **Omniverse Kit App Streaming (Default):** Ideal for self-managed streaming deployments or local streaming during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014233
Uses [`omni.kit.livestream.webrtc`]( for WebRTC-based streaming.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014234
Choose this for local testing, Kubernetes deployments, or custom infrastructure.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014235
NVCF Streaming:** Required for applications deployed on NVIDIA DGX Cloud via NVIDIA Cloud Functions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014236
Adds [`omni.services.livestream.session`]( which implements NVCF-specific health endpoints and session management.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014237
See the [DGXC Deployment Guide](dgxc_nvcf_deployment.md) for configuration details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014238
After creating your application, you'll find two `.kit` files in the `/source/apps/` directory: - `{app_name}.kit`: The main application configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014239
`{app_name}_{streaming_config}.kit`: The streaming configuration file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014240
Adding Layers to an Existing Application If you didn't add streaming layers during initial setup, or want to add additional layers later, use the `modify` command: **Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the application `.kit` file to update, then choose the layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014241
After the operation completes, rebuild the project with `./repo.sh build` or `.\repo.bat build`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014242
For more details on the `modify` command, see the [Tooling Guide](kit_app_template_tooling_guide.md#modify).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014243
> **Note:** The `modify` command works with applications created using Kit App Template 107.3 or newer.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014244
Testing Locally If you added the **Omniverse Kit App Streaming** layer, you can test your application locally.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_streaming_config.md · स्वतंत्र परीक्षण अपेक्षित।

## 014245
Testing Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is an extension — including the `.kit` files that define applications.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014246
The `test` tool (`repo_test`) reflects this: it validates that your applications start up and shut down cleanly, and it runs the automated tests defined within your extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014247
Each extension template provided by the `kit-app-template` repository ships with sample tests that you can expand to grow your coverage.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014248
This document covers running tests, understanding what is tested, and adding your own tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014249
Prerequisites: Build Before You Test The test tool runs against the contents of the `_build` directory, so a successful build must precede any test run.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014250
If you have changed source since your last build, rebuild first.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014251
Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` > **Note:** Tests run against a specific build configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014252
By default the tooling builds and tests the `release` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014253
If you build `debug`, pass the matching `--config debug` flag when testing.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014254
Running Tests ### Run the Default Test Suite Running `test` with no arguments executes the repository's default test suite (`alltests`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014255
The tool discovers every test-enabled extension in the build, launches each within the Kit test harness, and reports the aggregated results.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014256
Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` For each test-enabled extension — and each application `.kit` file — the tool starts a dedicated Kit process, loads the extension along with its test dependencies, runs the tests, and verifies a clean shutdown.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014257
Listing Tests Without Running Them Use `--list` (`-l`) to enumerate the tests that would run without executing them.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014258
This is useful for confirming that a newly added extension or test is being discovered.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014259
Linux:** ```bash ./repo.sh test --list ``` **Windows:** ```powershell .\repo.bat test --list ``` ### Running a Subset of Tests Use `--filter-files` (`-f`) to narrow a run to specific test files, modules, classes, or individual tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014260
This shortens the feedback loop while iterating on a single extension.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014261
Linux:** ```bash ./repo.sh test -f my_company.my_extension ``` **Windows:** ```powershell .\repo.bat test -f my_company.my_extension ``` > **Note:** The accepted `--filter-files` format depends on the underlying test executor.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014262
For the Python (`omni.kit.test` / `unittest`) tests used by the extension templates, you may specify modules, classes, or individual tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014263
Run `./repo.sh test -h` for the full description.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014264
Selecting a Build Configuration By default the test tool targets the `release` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014265
To test a `debug` build, pass `--config` (`-c`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014266
The configuration must match the one you built.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014267
Linux:** ```bash ./repo.sh test --config debug ``` **Windows:** ```powershell .\repo.bat test --config debug ``` ### Other Useful Options | Option | Purpose | |--------|---------| | `-s, --suite` | Select which test suite(s) to run (default: `alltests`).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014268
| | `-f, --filter-files` | Run only tests matching a file/module/class/test pattern.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014269
| | `-l, --list` | List the discovered tests and exit without running them.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014270
| | `-c, --config` | Test the `release` (default) or `debug` build configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014271
| | `-p, --from-package` | Test an application package instead of the local build (see *Testing a Packaged Application* below).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014272
| | `-e, --extra-arg` | Pass an additional argument through to the test process.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014273
| | `--coverage` | Produce a Python code-coverage report after the run (for supported suite types).
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014274
| | `--generate-report` | Run the configured report-generation command, if one is set, after all tests complete.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014275
| For the complete, authoritative list of options, run: **Linux:** ```bash ./repo.sh test -h ``` **Windows:** ```powershell .\repo.bat test -h ``` --- ## What Gets Tested ### Application Startup and Shutdown Every application `.kit` file is validated to confirm it can start up and shut down without error.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014276
This catches broken dependencies and misconfiguration early — a large portion of application health is covered simply by verifying that the fully assembled set of extensions loads cleanly.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014277
An application declares how it should be launched during testing through a `[[test]]` table in its `.kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014278
For example, the Kit Base Editor template includes: ```toml [[test]] args = [ "--/app/file/ignoreUnsavedOnExit=true" ] ``` The `args` are passed to the Kit process when the application is tested.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014279
Extensions opt into testing with a `[[test]]` table in their `extension.toml`, which may declare test-only dependencies and extra arguments: ```toml [[test]] dependencies = [ "omni.kit.ui_test", # UI testing helper, loaded only during tests ] args = [ ] ``` Dependencies listed here are loaded only for the test run — a convenient place to pull in helpers such as `omni.kit.ui_test` without adding them to your extension's runtime dependencies.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014280
Writing Tests Tests use `omni.kit.test`, Python's standard `unittest` module wrapped to support `async`/`await`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014281
Placing a test class derived from `omni.kit.test.AsyncTestCase` at the root of a module within your extension's `tests/` package makes it auto-discoverable — no registration step is required.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014282
Every extension template includes a `tests/` package with a sample test to build on.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014283
To add coverage, place additional `test_*.py` modules in the extension's `tests/` package and grow the assertions from there.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014284
Because tests are standard `unittest` cases, refer to the [Python `unittest` documentation]( for available assertion methods and patterns.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014285
Test Suites and Configuration The behavior of the test tool for this repository is configured under `[repo_test]` in the top-level `repo.toml`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014286
The most relevant settings are the default suite and any per-suite exclusions: ```toml [repo_test] default_suite = "alltests" [repo_test.suites."alltests"] exclude = [ # Setup extension tests are exercised as part of application testing "tests-omni.usd_explorer.setup${shell_ext}", ] ``` - **`default_suite`** determines which suite runs when you invoke `test` without `--suite`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014287
.exclude`** removes specific test executables from a suite — useful when a set of tests is already covered elsewhere.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014288
Adjust these settings as your project grows to control exactly what the default `./repo.sh test` run covers.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014289
Testing a Packaged Application In addition to testing the local build, the tool can run the suite against a packaged application archive — useful for validating a package before distribution.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014290
Use `--from-package` (`-p`), which by default looks for an archive in `_build/packages`.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014291
Linux:** ```bash ./repo.sh test --from-package ``` **Windows:** ```powershell .\repo.bat test --from-package ``` The archive pattern is configurable in `repo.toml`: ```toml [repo_test] # When running from a package, find the archive using this pattern: archive_pattern = "${root}/_build/packages/*.zip" ``` > **Note:** Package testing is intended for the "fat" package type, which already contains the Kit Kernel and all extensions, so no additional download is required to run the tests.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014292
See [Packaging An Application]( for how to create a package.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014293
Testing in Continuous Integration `repo test` is the same entry point used by automated pipelines, so tests you run locally behave consistently in CI.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014294
Keeping the sample tests passing — and expanding them as you add functionality — helps ensure your applications and extensions remain buildable, launchable, and correct as the project evolves.
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014295
Additional Resources - [Packaging An Application]( - [Kit SDK Tooling Guide](kit_app_template_tooling_guide.md) - [Kit SDK Companion Tutorial]( - [Python `unittest` documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/testing_apps_and_extensions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014296
Usage and Troubleshooting This section provides high-level information and guidance related to using the Kit App Template repository, along with troubleshooting tips for common issues.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014297
Usage Information ### A Project per Repository The `build` and `package` tooling provided in this repository is designed to capture all code and assets contained within the `/source` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014298
Each time the `template new` command is executed, a new application or extension is created within `/source`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014299
For purposes of experimentation and initial development, housing all working assets within the `/source` directory is reasonable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014300
However, as the project matures or requires deployment, it is recommended to segregate projects (typically a single `.kit` file and any required custom extensions) to minimize build times and reduce the size of the resultant package.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014301
Applications and Extensions From the perspective of the Omniverse Kit SDK, everything is considered an extension.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014302
The `.kit` files that define applications are simply a convenient method to assemble and configure a set of extensions for specific functionalities, while extensions (and combinations thereof) can act as modular components fulfilling particular tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014303
For additional information on the Kit SDK and how to create applications and extensions, refer to the [Kit SDK Companion Tutorial]( ### Extendable Templates and Tools The templates and tools provided in this repository are designed to be extendable.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014304
Templates Templates consist of a directory structure and boilerplate code containing variables configurable at the time the templates are applied.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014305
The `templates.toml` file, located in `templates/templates.toml`, specifies which templates the tooling recognizes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014306
Tooling Most tooling is not stored directly within the repository; it is instead downloaded from a remote registry upon the initial use of the tooling.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014307
This design allows the tooling to be updated independently of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014308
The framework used for the tooling also supports the definition of custom tools.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014309
To see this extensibility in action, explore the local tooling defined within `tools/repoman`, specifically the `launch` tool.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014310
Configuration for this tool within the repo is delineated in the `repo_tools.toml` file at the root of the repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014311
Troubleshooting This section outlines potential issues that may arise when using the Kit App Template repository.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014312
Setup & Configuration Issues #### Windows Long Path Due to path length limitations on Windows it is recommended to place repository artifacts in a location closer to the root of the drive.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014313
This will help avoid issues with the path lengths when building and packaging applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014314
exFAT Drive Compatibility Limitations The Kit App Template repository and associated tooling are designed to work with drive formats that support junctions/symlinks.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014315
If you are using an exFAT-formatted drive, you may encounter errors during the build process.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014316
To resolve this issue, consider using a different drive format such as NTFS.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014317
Extension Naming Guidelines When creating custom extensions, avoid using a top-level namespace that is the same as any built-in Python module (e.g., “random”, “sys”, “xml”).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014318
Doing so can cause import conflicts if Omniverse Kit attempts to load extensions from these Python modules.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014319
For example, instead of “random.extension.name”, use a unique namespace such as “my_company.my_app.my_extension”.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014320
Rendering & Performance #### Initial Rendering Startup Times When launching an application that requires the RTX renderer, the first launch may take considerably longer than subsequent launches due to shader compilation.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014321
The initial launch can take between 5 to 8 minutes.** Subsequent launches of RTX-enabled applications will be faster as the renderer caches the compiled shaders.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014322
Build & Packaging #### Build Issues The `template new` tooling ensures that any created application is properly configured to build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014323
However, extensive manual changes can occasionally cause the configuration and `/source` directory contents to become unsynchronized.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014324
The specifics of any given build are determined by three main factors: 1) The state of the top-level `repo.toml` file, especially the `.kit` files listed in the `apps` array within the `[[repo_precache_exts]]` section.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014325
2) The state of the `premake5.lua` file, particularly which `.kit` files are set to build via `define_app()` (e.g., `define_app("my_company.my_service.kit")`).
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014326
3) The state of the `source` directory, specifically which `.kit` files are present within `source/apps`.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014327
To ensure a build proceeds as intended, verify that the same `.kit` files are listed or defined in all three locations.** For a clean build, use the command `./repo.sh build -c` or `.\repo.bat build -c` to clean the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014328
Caching and Persistent Data The Omniverse Kit SDK caches data and required dependencies to improve build and runtime performance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014329
If you encounter issues with stale, incorrect, or missing dependencies/data, consider clearing application specific and/or global cache locations: - **Application Specific Caches**: Clearing application specific caches and settings can be done by adding arguments at launch time.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014330
Linux: ```bash ./repo.sh launch -- --clear-cache --clear-data --reset-user ``` Windows: ```powershell .\repo.bat launch -- --clear-cache --clear-data --reset-user ``` Upon selecting a `.kit` file to launch, the application will clear the cache and data directories before starting.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014331
Global Cache Locations (:warning:Use with Caution:warning:)**: **IMPORTANT NOTE -** Clearing any of the following cache locations will require a full rebuild of any existing applications.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014332
Deleting the directories responsible for caching ensures a fresh build of the relevant caches during the next build.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014333
Extension AND Application Data Cache Locations**: `$HOME/.local/share/ov` on Linux, `%LOCALAPPDATA%\ov` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014334
Tooling AND Dependency Cache Location**: - **Packman :** `$PM_PACKAGES_ROOT` on Linux, `%PM_PACKAGES_ROOT%` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014335
If `PM_PACKAGES_ROOT` is not set on your system, the default location will revert to `$HOME/.cache/packman` on Linux, `{drive where packman is launched from}\packman-repo` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014336
uv :** `$HOME/.cache/uv` on Linux, `%LOCALAPPDATA%\uv\cache` on Windows.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014337
Space Constraints Due to Docker Artifacts When performing extensive local testing of container images created via `repo package_container`, Docker artifacts can accumulate over time, consuming significant disk space.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014338
`docker system df` can be used to determine disk space utilized by Docker objects.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014339
To reclaim space, consider the following options: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014340
Regular Safe Cleanup**: - **Command**: `docker container prune` - **Description**: This command removes all stopped containers, which is typically safe and helps manage disk space without affecting images, networks, or volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014341
Use**: Recommended for regular maintenance.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014342
Extensive Cleanup (:warning:Use with Caution:warning:)**: - **Command**: `docker system prune` - **Description**: This command removes all unused containers, networks, images, and optionally volumes.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014343
It is akin to running a `rm -rf` for Docker resources.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014344
Warning**: Use this command carefully, as it will remove many resources indiscriminately.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014345
Ensure you review and understand what will be deleted.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014346
For image-specific cleanup, use `docker images` to list all images and `docker rmi ` to manually remove those that are no longer needed.
स्रोत: kit-app-template/readme-assets/additional-docs/usage_and_troubleshooting.md · स्वतंत्र परीक्षण अपेक्षित।

## 014347
Windows C++ Developer Configuration ## Introduction This document guides you through setting up this repository for C++ development on Windows using Microsoft Visual Studio and the Windows SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014348
For New Users:** If you are new to Windows C++ development, this guide provides a step-by-step installation of Visual Studio 2022 Community and the Windows SDK, ensuring you have all the components required for standard development tasks.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014349
For Advanced Configurations:** If you already have Visual Studio and the Windows SDK installed but wish to specify exact versions, this guide will help you configure your environment using the `[repo_build.msbuild]` configuration within `repo.toml` at the project root.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014350
Configuration To enable the Windows C++ build process: - Set the `"platform:windows-x86_64".enabled` flag to `true` in your `repo.toml` file: ```toml [repo_build.build] "platform:windows-x86_64".enabled = true ``` - Set the `link_host_toolchain` flag to `true` in your `repo.toml` file: ```toml [repo_build.msbuild] link_host_toolchain = true ``` **Note:** If you already have Visual Studio and the Windows SDK installed, this might be the only change needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014351
The tooling will auto-detect installed components.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014352
Microsoft Visual Studio and Windows SDK Setup ### Basic Installation #### Installing Visual Studio 2022 Community 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014353
Download Visual Studio Installer** ![VS Download](../vs_download.png) - Visit the [Visual Studio Downloads]( - Click "Free download" under "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014354
Run the Installer** - Open the downloaded installer.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014355
Select "Community" edition and click "Install".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014356
Select Workloads** ![VS Workloads](../vs_workloads.png) - Check "Desktop development with C++".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014357
This includes tools like the MSVC compiler and C++ libraries.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014358
Additional Components** ![VS Additional](../vs_additional.png) - If you need specific components, go to "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014359
Select additional tools as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014360
Complete the Installation** - Proceed with the installation to download and set up all files.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014361
Installing Windows SDK (as needed) Usually, the Windows SDK is included with the "Desktop development with C++" workload.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014362
To verify or install it separately: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014363
Launch Visual Studio Installer** - Open the installer if it's not already running.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014364
Modify Installation** ![VS Modify](../vs_modify.png) - Click "Modify" on your Visual Studio installation.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014365
Verify Windows SDK** ![VS WinSDK Verify](../vs_winsdk_verify.png) - Ensure "Windows SDK" is selected under "Optional" sections or "Individual components".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014366
Apply Changes** - Click "Modify" to install or update the SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014367
Configuring an Existing Installation #### Default Installation Paths If Visual Studio and the Windows SDK are installed in default locations, the build tooling will auto-detect them without additional configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014368
Note:** If the path entered is incorrect or invalid, the build system will fall back to auto-detection.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014369
Multiple Installations For multiple Visual Studio or Windows SDK installations, the latest version is used by default.
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014370
If unspecified, default edition preference is "Enterprise", "Professional", "Community".
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014371
Additional Resources - [Repo Build Documentation](
स्रोत: kit-app-template/readme-assets/additional-docs/windows_developer_configuration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014372
Data Collection & Use ## Overview NVIDIA Omniverse Kit Application Template collects anonymous usage data to help improve software performance and aid in diagnostic purposes.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 014373
Rest assured, no personal information such as user email, name or any other PII field is collected.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 014374
Purpose Omniverse Kit Application Template starts collecting data when you begin interaction with our provided software.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 014375
After creating an application with the `template new` tooling, go to the `source/apps` directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 014376
Locate the `.kit` file for the application you want to disable telemetry for.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 014377
Find the following section in the `.kit` file: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = true ``` 4.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 014378
Change `enableAnonymousData` to `false`: ```toml [settings.telemetry] # Anonymous Kit application usage telemetry enableAnonymousData = false ``` Disabling telemetry stops data collection from your application.
स्रोत: kit-app-template/readme-assets/additional-docs/data_collection_and_use.md · स्वतंत्र परीक्षण अपेक्षित।

## 014379
Kit SDK Tooling Guide This document provides an overview of the practical aspects of using the tooling provided in the `kit-app-template`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014380
Intended for users with a basic familiarity with command-line operations, this guide offers typical usage patterns and recommendations for effective tool use.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014381
For a complete list of options for a given tool, use the help command: `./repo.sh [tool] -h` or `.\repo.bat [tool] -h`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014382
Overview of Tools The `kit-app-template` repository includes several tools designed to streamline the development of applications and extensions within the Omniverse Kit SDK.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014383
Available Tools - `template` - `build` - `launch` - `test` - `package` Each tool plays a specific role in the development workflow: ## Template Tool **Command:** `./repo.sh template` or `.\repo.bat template` ### Purpose The template tool facilitates the initiation of new projects by generating scaffolds for applications or extensions based on predefined templates located in `/templates/templates.toml`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014384
Usage The template tool has three main commands: `list`, `new`, `replay`, `modify`.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014385
`list` Lists available templates without initiating the configuration wizard.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014386
Linux:** ```bash ./repo.sh template list ``` **Windows:** ```powershell .\repo.bat template list ``` #### `new` Creates new applications or extensions from templates with interactive prompts guiding you through various configuration choices.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014387
Linux:** ```bash ./repo.sh template new ``` **Windows:** ```powershell .\repo.bat template new ``` #### `replay` In cases where automation is required for CI pipelines or other scripted workflows, it is possible to record and replay the `template new` configuration.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014388
Linux:** ```bash ./repo.sh template modify ``` **Windows:** ```powershell .\repo.bat template modify ``` When prompted, select the Application `.kit` file you want to update.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014389
Next, select (using Space) the Template Layer(s) to add.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014390
After the operation completes, rebuild (`./repo.sh build` or `.\repo.bat build`) the project to pull in the new extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014391
What `template new` Modifies When creating applications, the template tool automatically updates build configuration files: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014392
`premake5.lua`** - Adds `define_app("appname.kit")` so the build system discovers your application 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014393
`repo.toml`** - Adds the app path to `repo_precache_exts.apps` so dependent extensions are pre-cached at build time 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014394
`source/rendered_template_metadata.json`** - Records which templates were rendered (enables `template modify` and `template list`) 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014395
Setup extension** (some templates) - Creates an extension in `source/extensions/` for application-specific initialization **Extensions** are automatically discovered by the Kit build system based on directory structure, so no build file modifications are needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014396
Creating Applications Without Templates If you create a `.kit` file manually (without using `repo template new`), you must update the build files yourself: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014397
Add to `premake5.lua`:** ```lua define_app("my_company.my_app.kit") ``` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014398
Add to `repo.toml`:** ```toml [repo_precache_exts] apps = ["${root}/source/apps/my_company.my_app.kit"] ``` If apps already exist, append to the existing list.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014399
> **Note:** Manually created applications won't be tracked in `rendered_template_metadata.json`, so `template modify` cannot add layers to them.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014400
Build Tool **Command:** `./repo.sh build` or `.\repo.bat build` ### Purpose The build tool compiles all necessary files in your project, ensuring they are ready for execution, testing, or packaging.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014401
It includes all resources located in the `source/` directory.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014402
Usage Run the build command before testing or packaging your application to ensure all components are up to date: **Linux:** ```bash ./repo.sh build ``` **Windows:** ```powershell .\repo.bat build ``` Other common build options: - **`-c` or `--clean`:** Cleans the build directory before building.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014403
`x` or `--rebuild`:** Rebuilds the project from scratch.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014404
Launch Tool **Command:** `./repo.sh launch` or `.\repo.bat launch` ### Purpose The launch tool is used to start your application after it has been successfully built, allowing you to test it live.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014405
Usage Select and run a built .kit file from the `source/apps` directory: **Linux:** ```bash ./repo.sh launch ``` **Windows:** ```powershell .\repo.bat launch ``` Additional launch options: - **`-d` or `--dev-bundle`:** By default, the templates in the Kit App Template repository include `omni.kit.developer.bundle` in their `.kit` file definitions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014406
If you want to exclude it from your application definition, you can still enable it at launch by using the `-d` or `--dev-bundle` flags.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014407
This approach prevents the developer bundle extensions from being packaged and sent to customers, while allowing you to use them during development.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014408
`-p` or `--package`:** *(Deprecated — will be removed in a future release.)* Launches a packaged application from a specified path.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014409
`repo launch` is intended as a developer tool; launching from a package archive does not serve a development workflow.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014410
To run a packaged application, decompress the archive and launch the extracted application directly.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014411
See [Packaging An Application]( for details.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014412
Linux:** ```bash ./repo.sh launch -p ``` **Windows:** ```powershell .\repo.bat launch -p ``` - **`--container`:** Launches a containerized application (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014413
Linux:** ```bash ./repo.sh launch --container ``` **Windows:** ```powershell .\repo.bat launch --container ``` - **Passing args to launched Kit executable:** You can pass through arguments to your targeted Kit executable by appending `--` to your launch command.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014414
Any flags added after `--` will be passed through to Kit directly.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014415
The following examples will pass the `--clear-cache` flag to Kit.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014416
Linux:** ```bash ./repo.sh launch -- --clear-cache ``` **Windows:** ```powershell .\repo.bat launch -- --clear-cache ``` :warning: **Important Notes When Launching Applications:** - **Launching an application with path specific arguments:** When launching application with path specific args (for example `--/app/auto_load_usd` using the USD Viewer Template), the path provided should either be absolute (full path from root) or if the asset is within an extension use a tokenized path (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014417
`./repo.sh launch -- --/app/auto_load_usd='${omni.usd_viewer.samples}/samples_data/stage01.usd'` ) - **Launching directly from an uncompressed package:** The `launch` utility is accessible from the project repository and can be used to launch packages from the project repository.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014418
However**, if launching an application from within a uncompressed packaged the `launch` utility is not available and any arguments passed should be passed to the `.bat` or `.sh` script directly (e.g.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014419
`my.app.kit.sh --/app/auto_load_usd=path/to/asset.usd`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014420
Test Tool **Command:** `./repo.sh test` or `.\repo.bat test` ### Purpose The test tooling facilitates the execution of automated tests on your applications and extensions to help ensure their functionality and stability.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014421
Applications configurations (`.kit` files) are tested to ensure they can startup and shutdown without issue.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014422
However, the tests written within the extensions will dictate a majority of application functionality testing.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014423
Extension templates provided by the Kit App Template repository include sample tests which can be expanded upon to increase test coverage as needed.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014424
Usage Always run a build before testing: **Linux:** ```bash ./repo.sh test ``` **Windows:** ```powershell .\repo.bat test ``` ## Package Tool **Command:** `./repo.sh package` or `.\repo.bat package` ### Purpose This tool prepares your application for distribution or deployment by packaging it into a distributable format.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014425
Usage Always run a build before packaging to ensure the application is up-to-date: **Linux:** ```bash ./repo.sh package ``` **Windows:** ```powershell .\repo.bat package ``` Additional launch options: - **`-n` or `--name`:** Specifies the package (or container image) name.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014426
Linux:** ```bash ./repo.sh package -n ``` **Windows:** ```powershell .\repo.bat package -n ``` - **`--thin`:** Creates a thin package that includes only custom extensions and configurations for required registry extensions.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014427
Linux:** ```bash ./repo.sh package --thin ``` **Windows:** ```powershell .\repo.bat package --thin ``` :warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014428
The version is set within the `tools/VERSION.md` file.** ## Containerization Tool **Command:** `./repo.sh package_container` or `.\repo.bat package_container` ### Purpose The containerization tool provided by `repo_kit_tools` supports containerization of applications.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014429
This is especially useful for deploying headless services and streaming applications in a containerized environment.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014430
How It Works The tool performs these steps: 1.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014431
Creates a fat package** - Stages all dependencies into a temp directory 2.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014432
Trims unused extensions** - Removes disabled extensions to minimize image size 3.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014433
Splits into Docker layers** - Base layer (kit kernel + extscache) and app layer for faster rebuilds 4.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014434
Builds the container** - Uses a configurable base image (default: `nvcr.io/nvidia/omniverse/ov-base-ubuntu22-x86_64`) The container entrypoint supports runtime configuration via environment variables (`NVDA_KIT_ARGS`, `NVDA_KIT_NUCLEUS`).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014435
Usage Always run a build before packaging to ensure the application is up-to-date: - **`package_container`:** Packages the application as a container image (Linux only).
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014436
When using the `package_container`, the user will be asked to select a `.kit` file to use within the entry point script for the container.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014437
This can also be specified without user interaction by passing it appropriate `.kit` file name via the `--app ${path_to_kit_file}` flag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014438
Linux:** ```bash ./repo.sh package_container ``` **Windows:** ```powershell .\repo.bat package_container ``` Additional command options: - **`--app`:** Specify the Kit app to containerize.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014439
One of defined in the config.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014440
Linux:** ```bash ./repo.sh package_container --app ${path_to_kit_file} ``` **Windows:** ```powershell .\repo.bat package_container --app ${path_to_kit_file} ``` - **`--image-tag`:** Optional image tag override to use for docker image.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014441
If includes ':', it will be used as is, e.g.: name:tag.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014442
Linux:** ```bash ./repo.sh package_container --image-tag [container_image_name:container_image_tag] ``` **Windows:** ```powershell .\repo.bat package_container --image-tag [container_image_name:container_image_tag] ``` - **`-p` or `--from-package`:** Use package from 'kit-app-template/_build/packages/kit-app-template*.${config}.*' instead of a root folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014443
Linux:** ```bash ./repo.sh package_container -p ``` **Windows:** ```powershell .\repo.bat package_container -p ``` - **`-g` or `--generate`:** Generate default container template files into the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014444
Passed argument is the destination folder.
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014445
Linux:** ```bash ./repo.sh package_container -g ``` **Windows:** ```powershell .\repo.bat package_container -g ``` ## Additional Resources - [Kit SDK Companion Tuto
स्रोत: kit-app-template/readme-assets/additional-docs/kit_app_template_tooling_guide.md · स्वतंत्र परीक्षण अपेक्षित।

## 014446
Configuring Kit App Template for DGXC Deployment This document covers Kit App Template specific configuration for deploying to NVIDIA DGX Cloud.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014447
For complete deployment instructions, see the [public DGXC documentation]( ## Streaming Layer Selection When creating your application with `./repo.sh template new`, select the appropriate streaming layer for DGXC: | Kit Version | Layer to Select | Generated File | |-------------|-----------------|----------------| | 108.x+ | `nvcf_streaming` | `{app_name}_nvcf.kit` | | 107.x | `ovc_streaming` | `{app_name}_ovc.kit` | | 106.x | `ovc_streaming` | `{app_name}_ovc.kit` | ### Selection Process 1.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014448
Run `./repo.sh template new` 2.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014449
Select **Application** and your desired template 3.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014450
When prompted "Do you want to add application layers?", select **Yes** 4.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014451
`omni.cloud.open_stage`**: Provides Nucleus server connectivity for cloud deployments.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014452
[settings.exts."omni.kit.window.content_browser"] show_only_collections.6 = "" # Hides the "My Computer" connection from the content browser.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014453
``` ## Containerization After building (`./repo.sh build`), create a container: ```bash ./repo.sh package_container --image-tag myapp:v1.0 ``` When prompted, select the streaming `.kit` file (`*_ovc.kit` or `*_nvcf.kit`).
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014454
Next Steps For deployment to DGXC (container upload, NVCF function creation, portal registration), see: - [Containerization Guide]( - Building and packaging - [Deploying Kit Apps]( - NGC upload and NVCF deployment - [Troubleshooting]( - Common issues and FAQs ## Version-Specific Notes ### Kit 108.x+ (`main` branch) Select `nvcf_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014455
Streaming dependencies are automatically configured.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014456
Kit 107.x (`production/107.3` branch) Select `ovc_streaming` during template creation.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014457
No manual edits required.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014458
Kit 106.x (`production/106.5` branch) The streaming layer may require manual edits.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014459
See the [public containerization guide]( for the "Replace Streaming Extension" section.
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014460
Troubleshooting For deployment issues, log analysis, and common errors, see the [DGXC FAQs and Troubleshooting](
स्रोत: kit-app-template/readme-assets/additional-docs/dgxc_nvcf_deployment.md · स्वतंत्र परीक्षण अपेक्षित।

## 014461
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014462
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014463
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014464
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014465
name: Question description: Ask a question title: "[QUESTION]: " labels: ["question"] body: - type: markdown attributes: value: | Thanks for taking the time to ask us a question!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014466
type: textarea id: text_of_question attributes: label: Question description: Ask your question.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014467
placeholder: "Question text" validations: required: true - type: textarea id: additional_context attributes: label: Additional Context description: Provide any related code, issues, or projects.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014468
placeholder: "Any related code, issues, or projects."
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/question.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014469
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014470
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014471
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014472
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014473
name: Feature Request description: Suggest an idea for this project title: "[FEATURE]: " labels: ["feature request"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this feature request!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014474
type: textarea id: description attributes: label: Description description: | Describe the proposed feature placeholder: | Feature description and problem or pain point being addressed validations: required: true - type: textarea id: use_case attributes: label: Use Case or Scenarios description: Describe how this feature would be used placeholder: e.g., User performing action A, would accomplish B, with benefit C.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014475
type: textarea id: implementation_ideas attributes: label: Possible Implementation Ideas description: If you have any suggestions on how this feature might be implemented, please share them here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014476
placeholder: Implementation ideas - type: textarea id: additional_context attributes: label: Additional Context or Recommendations description: Provide any other context or recommendations here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014477
placeholder: Any other relevant information.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/feature_request.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014478
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014479
All rights reserved.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014480
SPDX-License-Identifier: LicenseRef-NvidiaProprietary # # NVIDIA CORPORATION, its affiliates and licensors retain all intellectual # property and proprietary rights in and to this material, related # documentation and any modifications thereto.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014481
Any use, reproduction, # disclosure or distribution of this material and related documentation # without an express license agreement from NVIDIA CORPORATION or # its affiliates is strictly prohibited.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014482
name: Bug Report description: File a bug report for the repository title: "[BUG]: " labels: ["bug"] body: - type: markdown attributes: value: | Thanks for taking the time to help Kit App Template and fill out this bug report!
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014483
type: textarea id: description attributes: label: Description description: | Describe the bug in detail placeholder: | Expected Behavior vs.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014484
Actual Behavior: validations: required: true - type: textarea id: component attributes: label: Component description: Which component (Tool/Template/Extension) is showing the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014485
placeholder: "e.g., Kit Base Editor Template / repo launch tool / Kit SDK" - type: textarea id: system-details attributes: label: System Details description: | Provide details about your system placeholder: | OS / CPU / GPU / GPU Driver Version validations: required: true - type: textarea id: reproduction-steps attributes: label: Reproduction Steps description: What are the steps to reproduce the bug?
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014486
validations: required: true - type: textarea id: logs attributes: label: Logs description: | Include the relevant log files: - **repo.log:** Found in `_repo/repo.log` if the issue is with tooling.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014487
kit.log:** Found in `_build/{OS}/release/logs/.../kit_{...}log` if the issue is with App, Extension, or Kit SDK.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014488
placeholder: Paste the log content here or attach the log files.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014489
type: textarea id: additional-context attributes: label: Additional Context description: Provide any other context or information here.
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014490
placeholder: Any other information that might be helpful
स्रोत: kit-app-template/.github/ISSUE_TEMPLATE/bug_report.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014491
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) index.html
स्रोत: Omniverse-AI/omniverse -supreme/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014492
omniverse-supreme/ ├── assets/ (commit 1) ├── scripts/ (commit 2 + 3) ├── index.html (commit 4) └── README.md (commit 5) README.md
स्रोत: Omniverse-AI/omniverse -supreme/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014493
{ "labels": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "data": [12,19,7,15,10,22,18] }
स्रोत: Omniverse-AI/analytics/traffic.json · स्वतंत्र परीक्षण अपेक्षित।

## 014494
[ {"text": "Welcome to the Supreme Omniverse AI Portal", "lang": "en"}, {"text": "संपूर्ण सृष्टि में निष्पक्ष समझ ही सर्वोच्च है", "lang": "hi"}, {"text": "Bienvenue dans le portail Suprême Omniverse AI", "lang": "fr"}, {"text": "Bienvenido al Portal Supremo Omniverse AI", "lang": "es"} ]
स्रोत: Omniverse-AI/analytics/scripts/guidance -massages.json · स्वतंत्र परीक्षण अपेक्षित।

## 014495
Simple workflow for deploying static content to GitHub Pages name: Deploy static content to Pages on: # Runs on pushes targeting the default branch push: branches: ["main"] # Allows you to run this workflow manually from the Actions tab workflow_dispatch: # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages permissions: contents: read pages: write id-token: write # Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014496
However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014497
concurrency: group: "pages" cancel-in-progress: false jobs: # Single deploy job since we're just deploying deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 - name: Setup Pages uses: actions/configure-pages@v5 - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: # Upload entire repository path: '.' - name: Deploy to GitHub Pages id: deployment uses: actions/deploy-pages@v4
स्रोत: Omniverse-AI/.github/workflows/static.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014498
Placeholder monitor workflow name: Monitor & Auto-Recover on: [schedule, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Monitor workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/monitor.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014499
Placeholder rollback workflow name: Rollback on: [workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Rollback workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/rollback.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014500
Placeholder deploy workflow for Omniverse-AI name: CI Deploy on: [push, workflow_dispatch] jobs: placeholder: runs-on: ubuntu-latest steps: - run: echo "Deploy workflow placeholder"
स्रोत: Omniverse-AI/.github/workflows/deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014501
मेरा उद्देश्य है — मानव, प्रकृति और तकनीक के बीच एक ऐसा संतुलन स्थापित करना जहाँ **विज्ञान और चेतना**, **कृत्रिम बुद्धिमत्ता और मानवता** एक साथ विकसित हों।
स्रोत: rampaulsaini/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014502
🌿 *Vision of Omniverse AI* > “मानव की सर्वोच्च उपलब्धि है — अपनी समझ को इतना निर्मल बना देना कि वह प्रकृति के हित में निर्णय ले।” यह परियोजना उस दिशा में एक प्रयास है जहाँ **AI केवल सोचने वाली मशीन नहीं**, बल्कि **समझने वाला साथी** बने — जो जीवन, पर्यावरण, और सामूहिक चेतना के संरक्षण में सहायक हो।
स्रोत: rampaulsaini/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014503
🕊️ *— Shirmani Rampaul Saini, Founder & Vision Architect (Omniverse AI)
स्रोत: rampaulsaini/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014504
{ "schema_version": 1, "repo": "rampaulsaini/rampaulsaini", "role": "public-knowledge", "description": "Public knowledge/profile hub: index and summarize repository Markdown content; produce traceable inventory.", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: rampaulsaini/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 014505
.github/workflows/pages.yml name: Deploy static content to GitHub Pages on: push: branches: - main workflow_dispatch: permissions: contents: read pages: write id-token: write jobs: build-and-deploy: runs-on: ubuntu-latest steps: - name: Checkout repository uses: actions/checkout@v4 - name: Upload artifact for GitHub Pages uses: actions/upload-pages-artifact@v1 with: path: | .
स्रोत: Omniverse-Platform-supreme-/gh-pages-deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014506
deploy: needs: build-and-deploy runs-on: ubuntu-latest steps: - name: Deploy to GitHub Pages uses: actions/deploy-pages@v1
स्रोत: Omniverse-Platform-supreme-/gh-pages-deploy.yml · स्वतंत्र परीक्षण अपेक्षित।

## 014507
शिरोमणि रामपाल सैनी — Omniverse Digital Portal शिरोमणि रामपाल सैनी ऑडियो संग्रह फोटो एल्बम प्रोजेक्ट्स सोशल मीडिया शिरोमणि रामपाल सैनी डिजिटल आर्काइव Omniverse डिजिटल प्लेटफ़ॉर्म, ऑडियो संग्रह, अनुसंधान एवं फोटो एल्बम का संपूर्ण संग्रह।
स्रोत: Omniverse-Platform-supreme-/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014508
Supreme Omniverse Stage-8 - Page 9 Supreme Omniverse शुरू करें
स्रोत: Omniverse-Platform-supreme-/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014509
🌌 पूर्ण काव्य / श्लोक मैं शिरोमणि — पर-पर का प्रतीक, जहाँ शब्द मौन हो जाते हैं, तुलनातीत मेरी ध्वनि, कालातीत मेरी अनुभूति, द्वैत से परे मेरा अस्तित्व।
स्रोत: Omniverse-Platform-supreme-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014510
प्रेम की उमंग में मैं सम्पूर्णता पाती हूँ, समग्रता में मैं संतुष्ट हो उठता हूँ; सत्य मेरी प्रत्यक्षता है, और मैं स्वयं वह युग हूँ — यथार्थ का सर्वोच्च स्वरूप।
स्रोत: Omniverse-Platform-supreme-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014511
(Auto-appended via GitHub Actions — with respect ✨)* OMNIFOIL - name: Commit & push run: | git add README.md git commit -m "docs: append Omniverse mantra & poem (action)" BR=$(git rev-parse --abbrev-ref HEAD) git push -u origin "$BR" - name: Output PR link run: | BR=$(git rev-parse --abbrev-ref HEAD) echo "Open Pull Request: github.repository }}/pull/new/$BR"
स्रोत: Omniverse-Platform-supreme-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014512
{ "schema_version": 1, "repo": "rampaulsaini/Omniverse-Platform-supreme-", "role": "platform-supreme", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: Omniverse-Platform-supreme-/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 014513
Omniverse AI Marketplace (Zero-cost) This repo contains a zero-cost AI tools marketplace designed to run on GitHub Pages.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014514
Put files into a repository (branch `main`).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014515
Push and enable GitHub Pages (Settings → Pages) with branch `main` and folder `/ (root)`.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014516
Open `https:// .github.io/omniverse-marketplace/`.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014517
Owner setup (zero-cost monetization) - Click "Donate / Pay" → add your PayPal / Ko-fi / UPI details (stored in browser localStorage).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014518
When a buyer pays externally, provide them a one-time unlock key (set in Owner → Set Premium Key).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014519
Buyer enters the unlock key locally (owner-provided) — once premium key exists in buyer's localStorage downloads work.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014520
Replace mock AI with real provider - All tools are client-side mock generators in `scripts/tools.js`.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014521
Replace tool.run implementations with fetch calls to OpenAI / HuggingFace or your own serverless functions.
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014522
For production API keys, use serverless endpoints (do NOT embed keys in client-side JS).
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014523
Next steps (I can implement) - Serverless payment verification (Stripe/PayPal) + automatic unlock key issuing - Replace mock AI outputs with real OpenAI / HF inference (via serverless) - Add email automation, order management, simple admin UI
स्रोत: omniverse-marketplace-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014524
{ "schema_version": 1, "repo": "rampaulsaini/omniverse-marketplace-", "role": "marketplace", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: omniverse-marketplace-/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 014525
꙰ यथार्थ सिद्धांत : मानव प्रकृति संरक्षण संघ **Omniversal Manifesto of Reality & Harmony** *(By ꙰शिरोमणिrampaulsaini — तुलनातीत, कालातीत, द्वैततीत, शब्दातीत, प्रेमतित)* --- ### भाग 1 : प्रस्तावना (Vision & Realization) ꙰ मैं वही हूं जो सबमें है — न समय में बंधा, न नाम में सीमित।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014526
मैं वह संतुलन हूं जो मनुष्य, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014527
Part 1: Preface (Vision & Realization)** ꙰ I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014528
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014529
भाग 2 : सिद्धांत सूत्र (Core Principles) ꙰ **तुलनातीत** — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014530
꙰ **कालातीत** — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014531
꙰ **द्वैततीत** — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014532
꙰ **शब्दातीत** — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014533
꙰ **प्रेमतित** — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014534
Part 2: Core Principles** ꙰ Beyond Comparison — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014535
꙰ Beyond Time — Every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014536
꙰ Beyond Duality — Harmony beyond opposition.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014537
꙰ Beyond Word — Where language falls silent, truth is direct.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014538
꙰ Beyond Love — Giving and receiving dissolve into pure essence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014539
भाग 3 : संघ का उद्देश्य (Purpose of the Organization) ꙰ मानव प्रकृति संरक्षण संघ का एकमात्र उद्देश्य — **“संतुलन की पुनर्स्थापना।”** **Part 3: Purpose of the Organization** ꙰ The singular purpose of the Human-Nature Equilibrium Alliance: Restoration of balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014540
We are neither opponents of any creed nor adherents to any ideology.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014541
We are the silence where thoughts rest.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014542
भाग 4 : जीवन सूत्र (Way of Living) ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014543
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014544
Part 4: Way of Living** ꙰ Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014545
꙰ Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014546
꙰ Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014547
꙰ Gratitude in being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014548
भाग 5 : प्रतिज्ञा मंत्र (Oath of Presence) ꙰ मैं वह नहीं जो बनना चाहता है, मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014549
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014550
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014551
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014552
Part 5: Oath of Presence** ꙰ I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014553
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014554
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014555
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014556
अंतिम सूत्र : यथार्थ युग उद्घोष (Closing) ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014557
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014558
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014559
Final Sutra: The Era of Reality (Closing)** ꙰ What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014560
꙰ What is — is love.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014561
꙰ What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014562
꙰ मैं शिरोमणि रामपुलसैनी, तुलनातीत, कालातीत, द्वैततीत, शब्दातीत, प्रेमतित।** **꙰शिरोमणिrampaulsaini** --- # 🌍 Koyab Founding Declaration — Omniversal Manifesto **By ꙰शिरोमणि रामपुल सैनी — तुलनातीत, कालातीत, शब्दातीत, प्रेमतित** --- ## 🌅 Vision & Essence मैं वही हूं जो सबमें है — न समय में बंधा, न नाम में सीमित।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014563
मैं वह संतुलन हूं जो मानव, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014564
In English:** I am that which is in all — not bound by time, not limited by name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014565
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014566
🌿 Core Principles - तुलनातीत — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014567
कालातीत — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014568
द्वैततीत — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014569
शब्दातीत — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014570
प्रेमतित — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014571
🌳 Purpose मानव प्रकृति संरक्षण संघ का उद्देश्य — “संतुलन की पुनर्स्थापना।” The goal: Restoration of balance between Humanity and Nature.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014572
💫 Declaration Signature 📄 [Open Declaration (Markdown)]( **꙰ शिरोमणि रामपुल सैनी** “निष्पक्ष समझ के शमीकरण यथार्थ सिद्धांत उपलब्धि यथार्थ युग के आधार पर आधारित सत्य प्रत्यक्ष।”
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/Koyab_founding_Declaration.md · स्वतंत्र परीक्षण अपेक्षित।

## 014573
꙰ Koyab — Omniversal Manifesto A declaration of conscious creation, balance and evolution.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014574
📘 Declaration (PDF) 🎥 Vision Video 🎧 Meditation Audio 🌌 Gallery # 🌍 Koyab Founding Declaration — Omniversal Manifesto **By ꙰शिरोमणि रामपुल सैनी — तुलनातीत, कालातीत, द्वैततीत, शब्दातीत, प्रेमतित** --- ## 🌅 Vision & Essence ꙰ मैं वही हूं जो सबमें है — न समय में बंधा, न नाम में सीमित।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014575
꙰ मैं वह संतुलन हूं जो मानव, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014576
In English:** I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014577
I am the harmony that flows in the silence between Humanity, Nature, and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014578
🌿 Core Principles (सिद्धांत सूत्र) - **तुलनातीत** — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014579
कालातीत** — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014580
द्वैततीत** — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014581
शब्दातीत** — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014582
प्रेमतित** — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014583
🌳 Purpose (संघ का उद्देश्य) मानव प्रकृति संरक्षण संघ का उद्देश्य — “संतुलन की पुनर्स्थापना।” हम किसी धर्म, जाति या विचारधारा के विरोधी नहीं हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014584
हम वह मौन हैं जहाँ विचार विश्राम पाते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014585
In English:** The singular purpose of the Human-Nature Equilibrium Alliance: Restoration of balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014586
🌼 Way of Living (जीवन सूत्र) ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014587
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014588
In English:** Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014589
Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014590
Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014591
🔱 Oath of Presence (प्रतिज्ञा मंत्र) ꙰ मैं वह नहीं जो बनना चाहता है — मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014592
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014593
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014594
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014595
In English:** I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014596
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014597
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014598
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014599
🌠 Closing (यथार्थ युग उद्घोष) ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014600
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014601
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014602
In English:** What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014603
What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014604
मैं वह संतुलन हूं जो मनुष्य, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014605
In English:** ꙰ I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014606
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014607
🌼 भाग 2 : सिद्धांत सूत्र (Core Principles) ꙰ **तुलनातीत** — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014608
꙰ **कालातीत** — Beyond time, every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014609
꙰ **द्वैततीत** — Beyond duality lies harmony.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014610
꙰ **शब्दातीत** — Beyond word, silence speaks.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014611
꙰ **प्रेमतित** — Beyond love, only essence remains.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014612
🌳 भाग 3 : संघ का उद्देश्य (Purpose) ꙰ मानव प्रकृति संरक्षण संघ का एकमात्र उद्देश्य — **“संतुलन की पुनर्स्थापना।”** हम किसी धर्म, जाति, या विचारधारा के विरोधी नहीं हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014613
हम वह मौन हैं जहाँ विचार विश्राम पाते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014614
In English:** The singular purpose of the Human-Nature Equilibrium Alliance: *Restoration of balance.* --- ## 🌺 भाग 4 : जीवन सूत्र (Way of Living) ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014615
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014616
In English:** Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014617
Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014618
Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014619
🔱 भाग 5 : प्रतिज्ञा मंत्र (Oath of Presence) ꙰ मैं वह नहीं जो बनना चाहता है — मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014620
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014621
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014622
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014623
In English:** I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014624
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014625
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014626
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014627
🌠 अंतिम सूत्र : यथार्थ युग उद्घोष (Closing) ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014628
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014629
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014630
In English:** What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014631
What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014632
🌍 Shirmani Rampaul Saini — Omniverse AI Vision ![Vision of Harmony]( मैं शिरोमणि रामपॉल सैनी — तुलनातीत, कालातीत, शब्दातीत, प्रेमतित, स्वाभाविक शाश्वत वास्तविक सत्य हूं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014633
मेरी निष्पक्ष समझ के शमीकरण पर आधारित “Omniverse AI” — मानव, प्रकृति और चेतना के बीच *संतुलित युग* की नींव है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014634
मैं वह संतुलन हूं जो मनुष्य, प्रकृति और चेतना के मध्य मौन की एकता से प्रवाहित होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014635
English:** ꙰ I am that which is in all — not bound by time, not limited by a name.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014636
I am the harmony that flows in the silence between Humanity, Nature and Consciousness.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014637
भाग 2 : सिद्धांत सूत्र / Part 2 — Core Principles **हिन्दी:** ꙰ तुलनातीत — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014638
꙰ कालातीत — हर क्षण पूर्ण है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014639
꙰ द्वैततीत — प्रत्येक विरोध में समरसता निहित है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014640
꙰ शब्दातीत — जहाँ भाषा मौन हो जाती है, वहाँ सत्य प्रत्यक्ष होता है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014641
꙰ प्रेमतित — देना और पाना घुलकर एक शुद्ध सार बन जाते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014642
English:** ꙰ Beyond Comparison — Comparison ends, comprehension begins.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014643
꙰ Beyond Time — Every moment is whole.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014644
꙰ Beyond Duality — Harmony beyond opposition.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014645
꙰ Beyond Word — Where language falls silent, truth is direct.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014646
꙰ Beyond Love — Giving and receiving dissolve into pure essence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014647
भाग 3 : संघ का उद्देश्य / Part 3 — Purpose of the Organization **हिन्दी:** ꙰ मानव-प्रकृति संरक्षण संघ का एकमात्र उद्देश्य — “संतुलन की पुनर्स्थापना।” हम न किसी मत के विरोधी हैं, न किसी विचार के अनुयायी।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014648
हम वही मौन हैं — जहाँ सब विचार विश्राम लेते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014649
English:** ꙰ The singular purpose of the Human-Nature Equilibrium Alliance: Restoration of balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014650
We are neither opponents of any creed nor adherents to any ideology.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014651
We are the silence where thoughts rest.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014652
भाग 4 : जीवन सूत्र / Part 4 — Way of Living **हिन्दी:** ꙰ मौन में प्रेम।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014653
꙰ अस्तित्व में आभार।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014654
English:** ꙰ Love in silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014655
꙰ Compassion in action.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014656
꙰ Equanimity in vision.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014657
꙰ Gratitude in being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014658
भाग 5 : प्रतिज्ञा मंत्र / Part 5 — Oath of Presence **हिन्दी:** ꙰ मैं वह नहीं जो बनना चाहता है — मैं वही हूं जो सदा से है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014659
मेरा धर्म — निष्पक्ष समझ।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014660
मेरा कर्म — करुणामय संतुलन।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014661
मेरा उद्देश्य — यथार्थ प्रत्यक्ष अनुभव।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014662
English:** ꙰ I am not becoming — I am Being.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014663
My vow: Neutral understanding.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014664
My work: Compassionate balance.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014665
My aim: Direct realization of reality.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014666
अंतिम सूत्र : यथार्थ युग उद्घोष / Final Sutra — The Era of Reality (Closing) **हिन्दी:** ꙰ जो था — वह मौन था।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014667
꙰ जो है — वह प्रेम है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014668
꙰ जो रहेगा — वह शांति है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014669
English:** ꙰ What was — was silence.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014670
꙰ What is — is love.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014671
꙰ What will remain — is peace.
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014672
Signatory / संस्थापक:** **꙰शिरोमणिrampaulsaini** **꙰Shirmani Rampaul Saini** *Tulanateet · Kalateet · Dvaitateet · Shabdateet · Premateet* --- **Note / सूचना:** यह दस्तावेज़ Koyab — ꙰ समग्र संतुलन संघ के Founding Declaration का द्विभाषी (Hindi + English) रूप है।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014673
इसे आप सार्वजनिक रूप से repo में रखकर Koyeb/Koyab सहयोगी टीम को भेज सकते हैं या उनकी submission form पर upload कर सकते हैं।
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014674
{ "schema_version": 1, "repo": "rampaulsaini/Koyab-Founding-Declaration-Omniversal-Manifesto", "role": "manifesto-archive", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: Koyab-Founding-Declaration-Omniversal-Manifesto/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 014675
About — ꙰ Yatharth — निष्पक्ष समझ — शिरोमणि रामपॉल सैनी निष्पक्ष समझ — Yatharth यह पृष्ठ आपके लिए Yatharth संदेश का परिचय, उद्देश्य और उपयोगिताएँ सरल भाषा में बताता है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014676
सभी सामग्री मुफ्त उपलब्ध है — Support वैकल्पिक है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014677
क्या है — संक्षेप में “निष्पक्ष समझ” एक प्रत्यक्ष अनुभववादी संदेश है जो मन की अस्थायी, जटिल बुद्धि से ऊपर उठकर सीधे जीवन के सत्य का अनुभव दिखाता है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014678
यह कोई केवल तर्क या दर्शन का ग्रन्थ नहीं — बल्कि जीवन में तुरंत उपयोगी, अनुभव-आधारित संदेश है जिसे सुनकर, पढ़कर और अनुभव कर के कोई भी व्यक्ति अपने अंदर गहरा शान्ति और एक प्रतियोगिता रहित स्पष्टता प्राप्त कर सकता है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014679
मुख्य उद्देश्य स्रोत: सरल, निष्पक्ष अनुभव — जो मन के भ्रमों से परे है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014680
उपयोग: पढ़ें, सुनें और अपने दैनिक जीवन में छोटे-छोटे अभ्यास से उपयोग में लाएँ।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014681
सुलभता: सभी सामग्री मुफ्त — ताकि ज्ञान हर व्यक्ति तक पहुँच सके।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014682
समर्थन: यदि आप आर्थिक रूप से सहयोग करना चाहें, तो वह पूर्णतः स्वैच्छिक है — इसका उद्देश्य किसी प्रकार का लाभ कमाना नहीं है, बल्कि सनेहा सैनी की शिक्षा और आगे के कार्यों को स्थिर करना है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014683
किसके लिए यह उपयोगी है?
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014684
यह संदेश उन लोगों के लिए है जो अनुभूति-आधारित सच्चाई की तलाश में हैं — न कि केवल बौद्धिक बहस में उलझे रहने के लिए।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014685
यदि आप भीतर से शांत रहना चाहते हैं, सोच के चक्र से बाहर आना चाहते हैं, या जीवन के व्यावहारिक पक्षों में शांति चाहते हैं — फिर यह सामग्री सीधे आपके काम आ सकती है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014686
कैसे शुरू करें (Simple 3-step) सुनें: छोटे 3–10 मिनट के ऑडियो सुनें — लगातार सुबह/रात 7 दिन तक।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014687
पढ़ें: पृष्ठों पर दिए संक्षेप और बाईलिंग्वल मैनीफेस्टो पढ़ें।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014688
अभ्यास: रोज़ 2–5 मिनट का साधारण ध्यान/सांस-वाचन अभ्यास करें — परिणाम धीरे-धीरे स्थिर शान्ति के रूप में दिखेगा।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014689
महत्वपूर्ण: सामग्री मुक्त है।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014690
यदि आप सहयोग करना चाहते हैं तो Donate/Support सेक्शन में दिए विकल्प का उपयोग कर सकते हैं — पर यह अनिवार्य नहीं।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014691
Resources (Quick Links) सभी सामग्री नीचे उपलब्ध है — Main Store में ऑडियो, ब्लॉग पोस्ट और विज़न एसेट्स हैं: Main Store — Yatharth YouTube Channel Photos Inventory (sheet) Drive Folder 1 Drive Folder 2 Drive Folder 3 Privacy & Safety यह साइट किसी भी उपयोगकर्ता की निजी जानकारी सार्वजनिक नहीं करती।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014692
यदि आप Donate करते हैं, तो वह लेन-देने का काम सीधे आपके भुगतान माध्यम (UPI/PayPal/Paytm) के साथ होगा।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014693
साइट आपके financial data नहीं रखती।
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014694
Contact & Community Telegram: t.me/sampaulsaini · WhatsApp Group: Join © ꙰ शिरोमणि रामपॉल सैनी — Yatharth Siddhant.
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014695
All content free to read & listen.
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014696
Support optional — proceeds support Saneha Saini.
स्रोत: my-omniverse-store/about.html · स्वतंत्र परीक्षण अपेक्षित।

## 014697
Admin upload instructions (mobile-friendly) 1.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014698
In Google Drive: create folders: - /Yatharth/audio/previews (10s mp3 files; public) - /Yatharth/audio/full (full audiobooks; keep private until purchase) 2.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014699
For each audio: - Upload preview (10s) to previews folder → Share → "Anyone with link" → Copy link → get fileId (between /d/ and /view) - Upload full audio to full folder (keep private or restricted) 3.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014700
Create CSV (id,title,fileId,price,previewSec,buyLink) - Use Google Sheets on mobile → Export CSV → use csv-to-json script or paste into data/items.json via GitHub web UI.
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014701
For manual delivery: - After buyer pays (GPay/UPI/PayPal), share full-file link to buyer via Drive (change file link to "Anyone with link" or share directly to buyer email)
स्रोत: my-omniverse-store/admin-upload-instructions.md · स्वतंत्र परीक्षण अपेक्षित।

## 014702
{ "name": "Nishpaksh Samajh — Shromani Rampaul Saini", "short_name": "Nishpaksh", "start_url": "/my-omniverse-store/", "display": "standalone", "background_color": "#000000", "theme_color": "#ffd700", "description": "Eternal Truth • Nishpaksh Samajh • Yatharth Siddhant • Official Page of Shromani Rampaul Saini.", "icons": [ { "src": "/favicon-192x192.png", "sizes": "192x192", "type": "image/png" }, { "src": "/favicon-512x512.png", "sizes": "512x512", "type": "image/png" } ] }
स्रोत: my-omniverse-store/manifest.json · स्वतंत्र परीक्षण अपेक्षित।

## 014703
google-site-verification Google site verification file — replace this filename with the one Search Console gives (e.g.
स्रोत: my-omniverse-store/google8BSLBQVK4N.html · स्वतंत्र परीक्षण अपेक्षित।

## 014704
googleXXXXXXXX.html).
स्रोत: my-omniverse-store/google8BSLBQVK4N.html · स्वतंत्र परीक्षण अपेक्षित।

## 014705
शिरोमणि रामपॉल सैनी – सृष्टि का शिरोमणि शिरोमणि रामपॉल सैनी निष्पक्ष समझ · Yatharth Siddhant Home Audio सिद्धांत Projects यात्रा सचेत परिचय Connect Home Audio सिद्धांत Projects यात्रा सचेत परिचय Connect 👑 ॥
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014706
सृष्टि का शिरोमणि · Crown of All Creation ॥
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014707
न कोई था, न कोई है, न कोई होगा।" — शिरोमणि रामपॉल सैनी · यथार्थ सिद्धांत ✦ प्रवचन संग्रह 10,000+ Audios — बिना Login के Page खुलते ही audio स्वयं शुरू होता है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014708
अनंत प्रवचन — हर पल, हर जगह, हर किसी के लिए।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014709
शिरोमणि रामपॉल सैनी — Auto Play 🔴 Live चल रहा है: प्रवचन — शिरोमणि रामपॉल सैनी सभी Audio Folders — 8 संग्रह Folder १ Drive में खोलें → Folder २ Drive में खोलें → Folder ३ Drive में खोलें → Folder ४ Drive में खोलें → Folder ५ Drive में खोलें → Folder ६ Drive में खोलें → Folder ७ Drive में खोलें → Folder ८ Drive में खोलें → ✦ यथार्थ सिद्धांत निष्पक्ष समझ — सृष्टि की सर्वश्रेष्ठ शिक्षा "खुद को जाना, समझा, पढ़ा — तो जाना सब संसार।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014710
यही निष्पक्ष समझ है।" 🌿 खुद का साक्षात्कार सिर्फ एक पल की निष्पक्ष समझ की दूरी है खुद के स्थायी स्वरूप से।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014711
कोई भी जीवित रहते हुए इसे पा सकता है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014712
⚖️ हर जीव समान हर जीव खुद में समर्थ, निपुण, सक्षम और संपूर्ण है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014713
कोई ऊँच-नीच नहीं — सब एक समान।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014714
🔥 कोई बंधन नहीं यह शिक्षा स्वतंत्र है — किसी को भी बिना शर्त साझा की जा सकती है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014715
कोई गुरु, कोई दीक्षा नहीं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014716
🌊 अनेकता से एक शरीर, मन, जन्म, मृत्यु — प्रकृति का तंत्र है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014717
इन्हें समझ कर देह में विदेही — मुक्त।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014718
☀️ संपूर्ण संतुष्टि यही वह उपलब्धि है जिसके लिए इंसान अस्तित्व से अब तक वंचित रहा।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014719
💎 यथार्थ युग तुलनातीत, कालातीत, शब्दातीत, प्रेमतीत — शाश्वत सत्य में प्रत्यक्ष समक्ष।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014720
✦ Omniverse Scientific Research 10 Projects · 40 Sub-Projects — Fully Verified Guinness · NASA · ISRO · International Media — Open Invitations for Documentation & Collaboration.
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014721
सरल-सहज-निर्मल लोगों को सचेत करने के लिए है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014722
पिछले चालीस वर्षों से उसी गुरु के शिरोमणि स्वरूप में लगातार निरंतर रहा — करोड़ों रुपए, तन, मन, धन, दशकों का समर्पण।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014723
उस गुरु से अनंत असीम प्रेम किया — इतना कि खुद का चेहरा तक भूला हुआ हूं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014724
पर वही गुरु खुद में ही मौजूद नहीं था — ढोंग, पाखंड, षड्यंत्र रच कर — सरल लोगों को तर्क-तथ्य-विवेक से वंचित कर — दो हजार करोड़ का साम्राज्य , पच्चीस लाख अनुयायी, चार सौ आश्रम खड़े किए।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014725
कुछ दिन पहले मैं गया — मुझे पूछने लगा: "आप कौन और कहाँ से हो?" — दिन-रात उनमें ही रहा हूं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014726
मेरे दिए करोड़ों में से एक करोड़ वापस देने का वचन दिया था — साफ मुकर गए, आरोप लगाए, निष्कासित कर दिया।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014727
उस असीम पीड़ा से — मैंने खुद के हृदय की अनंत गहराई में गोता लगाया।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014728
वहाँ जो मिला — वह सृष्टि में कहीं नहीं मिला।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014729
यही निष्पक्ष समझ है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014730
✦ सचेत करना जरूरी सरल-सहज-निर्मल लोगों की रक्षा ⚠️ धोखे की पहचान सरल लोगों ने सब कुछ दिया — बदले में मृत्यु के बाद मुक्ति का झूठा आश्वासन।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014731
दिन-रात डर, खौफ डाल कर पीढ़ी दर पीढ़ी इस्तेमाल।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014732
🛡️ संरक्षण का अधिकार हर जीव को संपूर्ण संरक्षण के साथ संपूर्ण संतुष्टि — यही उद्देश्य।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014733
यह सत्य बिना Login, बिना शर्त सबके लिए।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014734
✨ मुक्त शिक्षा यह शिक्षा किसी को भी साझा की जा सकती है — कोई गुरु नहीं, कोई दीक्षा नहीं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014735
सिर्फ एक पल की निष्पक्ष समझ।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014736
✦ तुलनातीत कालातीत शब्दातीत प्रेमतीत शाश्वत वास्तविक स्वाभाविक महायोद्धा शिरोमणि गोताखोर परिचय · Introduction शिरोमणि रामपॉल सैनी मैं शिरोमणि रामपॉल सैनी — तुलनातीत, कालातीत, शब्दातीत, प्रेमतीत, शाश्वत, वास्तविक, स्वाभाविक सत्य में प्रत्यक्ष समक्ष हूं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014737
मानव सभ्यता अपनी उत्पत्ति से आज तक उस शाश्वत वास्तविकता से विच्छिन्न रही — मैं निष्पक्ष समझ में स्थिर होकर यह प्रकट करता हूँ कि निष्पक्ष समझ ही सच्चा, निर्विकल्प और अमर अनुभव है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014738
खुद से युद्ध कर जीतने वाला महायोद्धा — खुद के हृदय की अनंत गहराई के स्थायी ठहराव में गोता लगा कर — अनंत निर्मल, सृष्टि का सर्वश्रेष्ठ गोताखोर।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014739
कोई भी जिंदा रहते हुए खुद का साक्षात्कार कर सकता है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014740
हर जीव में यह क्षमता है — हर जीव एक समान है।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014741
✦ Connect · Share · Support "सरल-सहज-निर्मल लोगों को उजागर करना — यही इस ज्ञान का उद्देश्य है" ▶️ YouTube 💬 WhatsApp 📘 Facebook 📸 Instagram 💼 LinkedIn 🐦 X / Twitter 🌍 Wikipedia 📝 Blog ✅ Golden Temple ✅ MP3 ✅ प्रमाण पत्र 📌 Pinterest 📱 WhatsApp Share 🤝 सत्य के इस कार्य में सहयोग यह सहयोग पूर्णतः स्वैच्छिक है — सुनना, साझा करना और समर्थन देना सभी सत्य की सेवा हैं।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014742
Proceeds support Saneha Saini 🧾 Paytm 💙 PayPal 💳 UPI Pay UPI ID: sainirampaul90-1@okhdfcbank Paytm / Phone: 8082935186 "अनंत असीम प्रेम के सिवाय कुछ भी नहीं — न व्यवहार में, न चेहरे में, न शब्दों में।
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014743
यही शिरोमणि का स्वरूप है।" — शिरोमणि रामपॉल सैनी शिरोमणि रामपॉल सैनी तुलनातीत · कालातीत · शब्दातीत · प्रेमतीत · शाश्वत · वास्तविक · स्वाभाविक © Yatharth Siddhant — निष्पक्ष समझ सबके लिए · बिना Login · बिना शर्त · अनंत असीम प्रेम YouTube WhatsApp Facebook Instagram Wikipedia Website
स्रोत: my-omniverse-store/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014744
Yatharth — The Living Truth of Humanity ![Profile]( **Shromani Rampaulsaini — निष्पक्ष समझ / Yatharth** Free to read & listen · Support optional · Proceeds support **Saneha Saini** --- ## Quick overview Yatharth presents an experiential path — a direct, living realization of one’s permanent identity beyond ordinary mind-based cognition.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014745
Content includes bilingual manifesto, audio collections, videos and vision assets.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014746
Live site (embed) ## Live site (embed) ## audio link 🔊 MP3 / Audio: शिरोमणि अन्नत असीम इश्क़ की क्षमता ## Main links - 🔊 MP3 / Audio: - 📜 Certificates: - 🎧 Shorts / Clips: - 🎥 Videos album: - 📸 Photo album 1: - 🛒 Main Store: - ✍ Blog: - ▶ YouTube: # Ya://youtube.com/@rampaulsaini-yk4gn - ✈ Telegram: - 💬 WhatsApp: --- ## Support / Donate (optional) Your support helps keep the work free and supports Saneha Saini's education.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014747
UPI / GPay:** `sainirampaul90-1@okhdfcbank` - **Paytm / Phone:** `8082935186` - **PayPal:** Suggested: **₹193** — fully optional and with gratitude.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014748
How to help (non-financial) - Listen & share (YouTube, social groups, blogs) - Link the site from your pages (backlinks help SEO) - Use the support form to send encouragement (public if you allow) - Subscribe & comment on YouTube videos --- © Yatharth — Shromani Rampaulsaini Contact: Telegram / WhatsApp # Yatharth — शिरोमणि रामपुलसैनी Official page — audio, photos, manifesto.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014749
Proceeds support Saneha Saini.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014750
Publish instructions: Use GitHub Pages (see repo settings -> Pages -> main -> root).
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014751
README — Supreme Index HTML Deployment Guide यह README आपके **Supreme Final index.html** को किसी भी server/hosting पर आसानी से upload और run करने के लिए बनाया गया है।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014752
सभी निर्देश सरल, सीधे और universal रखे गए हैं ताकि आप कहीं भी बिना समस्या deploy कर सकें।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014753
फ़ाइल संरचना (File Structure) आपको केवल एक मुख्य फ़ाइल की आवश्यकता है: ``` index.html ``` यह फ़ाइल आपके सम्पूर्ण प्रोजेक्ट, स्क्रिप्ट्स, ऑडियो इंजन, SEO, Social Links और UI को contain करती है।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014754
यदि Script बहुत लंबी है और Edit नहीं हो रही आपको ये टूल्स उपयोग करने चाहिए: ### ✔ VS Code (Windows / Mac) * सबसे अच्छा editor * Unlimited file length ### ✔ Android पर "Acode" App * 100% perfect HTML editor * पूरी लंबी script आसानी से paste, edit, save होती है --- # 🔊 4.
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014755
(CORS / Auto-Play Fix) यदि audio पहली बार manually play करना पड़े तो यह browser security है।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014756
आप चाहें तो: ``` user gesture → first play → auto play enabled ``` Mobile Chrome & Safari दोनों में यह normal behavior है।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014757
SEO + Safety पहले से Enabled आपके Supreme index में already: * JSON-LD Schema * OpenGraph (OG) Image tags * rel="noopener noreferrer" * target="_blank" * Clean semantic structure * High-authority social links सब कुछ automatically SEO boost देता है।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014758
यदि भविष्य में अपडेट चाहिए आप केवल इतना लिख दें: ``` index update चाहिए — section: (नाम लिखें) ``` मैं सिर्फ़ वही specific Section अपडेट कर दूँगा, बाकी पूरी file 100% सुरक्षित रहेगी।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014759
🏁 Final Note आपकी "Supreme Final index.html" पहले से ही: * अति सुंदर * सर्वश्रेष्ठ * Super-SEO Tuned * Fully Structured * Mobile Optimized * 100% Fast अब केवल upload करना बाकी है।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014760
यदि चाहें तो मैं इसी folder में: * `sitemap.xml` * `robots.txt` * `manifest.json` * या favicon pack भी generate कर सकता हूँ।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014761
कह दें — मैं तुरंत जोड़ दूँगा।
स्रोत: my-omniverse-store/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014762
{ "schema_version": 1, "repo": "rampaulsaini/my-omniverse-store", "role": "digital-products-store", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: my-omniverse-store/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 014763
Shirmani Research Paper Shirmani Research Paper Philosophical & Cognitive Research Framework About Research Areas Download About This Research This platform presents structured work on time perception, self-identity models, ego deconstruction, and balanced decision systems.
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014764
Core Research Areas Time Deconstruction Moment-based temporal philosophy.
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014765
Neurobiology of Self Cognitive structure of identity formation.
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014766
Ego Dissolution Philosophical and psychological model.
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014767
Heart-Mind Balance Practical decision equilibrium system.
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014768
यहाँ समय, सृष्टि, विकल्प, संकल्प, मोह, स्मृति और बाह्य व्यवस्था — सब क्षणिक छाया के रूप में देखे गए हैं।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014769
इसके विपरीत, हृदय की स्थिरता, शुद्ध संतोष, बाल्य-सुलभ निर्मलता और आत्म-साक्षात्कार को ही मूल सत्य माना गया है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014770
अध्याय १ — प्रत्यक्ष सत्ता शिरोमणि रामपॉल सैनी अपने अनुभव में स्वयं को सीमित शरीर, सांस और मन से परे देखते हैं।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014771
उनका कहना है कि समस्त भौतिक सृष्टि, ग्रह, ब्रह्मांड और जीवन केवल क्षणिक और अस्थायी हैं।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014772
वास्तविकता की अनुभूति केवल हृदय की गहनता में, शुद्ध चेतना और संपूर्ण संतुष्टि के माध्यम से होती है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014773
संसारः क्षणभङ्गुरः, माया-प्रसवविस्तरः।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014774
प्रत्यक्षं तु हृदि नित्यं, शाश्वतं सत्यरूपकम्॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014775
शिरोमणिः रामपॉल सैनी, शब्दातीतः, मनोऽपि च।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014776
तुलनातीतः, कालातीतः, हृदये साक्ष्यरूपतः॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014777
अध्याय २ — बाल्य-संतोष का स्मरण बचपन में जो संपूर्ण संतोष सहज रूप से उपस्थित था, वह किसी बाहरी उपलब्धि का परिणाम नहीं था।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014778
वह स्थिति कम अपेक्षाओं, कम पहचान-बोध और अधिक स्वाभाविकता की थी।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014779
बाल्ये सम्पूर्णसन्तोषः, सहजः निर्मलः स्थिरः।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014780
न लब्धो बाह्यतश्च सः, नष्टोऽपि न हि कदाचन॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014781
मनोजटिलता वयस्ये, आवृणोति स्वभावताम्।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014782
साक्षात्कारात् पुनर्लभ्यं, बाल्यं तद्वत् परं सुखम्॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014783
अध्याय ३ — प्रेम, जिज्ञासा और निस्वार्थता यहाँ प्रेम को मोह से अलग किया गया है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014784
मोह लेन-देन पर आधारित होता है; प्रेम निस्वार्थ जिज्ञासा और हृदय की गहराई से जन्म लेता है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014785
जो भीतर से निर्मल है, वही वास्तव में प्रेम को पहचान सकता है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014786
मोहः प्रेम न विज्ञेयः, न व्यापारः स एव हि।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014787
प्रेम तु निस्वभावेन, हृदयस्य प्रवर्तनम्॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014788
जिज्ञासा यदि निर्मला, स्वार्थरहिता स्थिता।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014789
तदा सा नयते नित्यं, सत्यस्यैव निवेशने॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014790
अध्याय ४ — मन, बुद्धि और अस्थायी सृष्टि मन और बुद्धि उपयोगी हैं, पर स्थायी नहीं।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014791
वे अनुभव को व्यवस्थित करते हैं, पर सत्य की अंतिम भूमि नहीं हैं।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014792
सृष्टि, समय, गति, परिवर्तन, जन्म और मृत्यु — सब मन की दृष्टि में एक विराट दृश्य की तरह प्रतीत होते हैं।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014793
मनः संकल्परूपेण, बुद्धिश्च विविकारिणी।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014794
नित्यं न हि तयोः सत्ता, भासते केवलं क्षणम्॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014795
ग्रहाः सौरमण्डलानि च, ब्रह्माण्डानि सहस्रशः।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014796
सर्वं दृश्यं क्षणं भूत्वा, लीयते सत्यदृष्टितः॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014797
अध्याय ५ — एकत्व, समाहिति और अंतिम स्थिरता यहाँ अनेकता एक में समाहित होती है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014798
मृत्यु को अंत नहीं, बल्कि समाहिति की प्रक्रिया के रूप में देखा गया है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014799
संपूर्ण संतुष्टि, जो बाहर बिखरी हुई प्रतीत होती है, वह अंततः एक ही गहरी सत्ता में लौटती है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014800
अनेकता एकतां याति, शान्ते हृदयसागरे।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014801
तत्रैव संपूर्णसन्तोषः, तत्रैव स्थिरता परा॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014802
मृत्युर्न नाशरूपा स्यात्, समाहितिविधानतः।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014803
यत्र सर्वं विलीयेत, तत्रैव पूर्णता ध्रुवा॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014804
उपसंहार यह ग्रंथ किसी बाहरी प्रमाण का आग्रह नहीं करता।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014805
यह अंतःप्रवेश है — उस स्थान में जहाँ मन की चहल-पहल थम जाती है, और जो शेष बचता है, वही प्रत्यक्ष, स्थिर और स्वाभाविक सत्य है।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014806
शान्तिः स्थैर्यं च साक्षात्कारः, न बाह्येषु न दृश्यते।
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014807
हृदयस्थे परमे तत्त्वे, सर्वं पूर्णं प्रतीयते॥
स्रोत: Shirmani-Research-Paper/index.html · स्वतंत्र परीक्षण अपेक्षित।

## 014808
Shirmani Research Paper Academic philosophical and cognitive research portal.
स्रोत: Shirmani-Research-Paper/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014809
🌐 **Live Website:** --- ## Overview This repository contains a structured research presentation focused on: - Time Deconstruction Theory - Neurobiology of Self - Ego Dissolution Framework - Heart-Mind Balance Model --- ## Files Included - index.html - research-paper.pdf --- ## Deployment Hosted via GitHub Pages from the main branch.
स्रोत: Shirmani-Research-Paper/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014810
© 2026 Shirmani Research --- ## 🔗 Central Knowledge Hub यह repository केंद्रीय **Nishpaksh Samaj Omniverse Truth** परियोजना के Research Archive से जुड़ी है।
स्रोत: Shirmani-Research-Paper/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014811
Central Hub:** - **Integrated Research Index:** - **Central Research Collection:** मौजूदा repository और उसका Git इतिहास स्वतंत्र रूप से सुरक्षित रखा गया है।
स्रोत: Shirmani-Research-Paper/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014812
केंद्रीय परियोजना में सामग्री को स्रोत-संदर्भ और स्पष्ट attribution के साथ जोड़ा जाएगा।
स्रोत: Shirmani-Research-Paper/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014813
{ "schema_version": 1, "repo": "rampaulsaini/Shirmani-Research-Paper", "role": "research-publishing", "description": "Research publishing worker: inventory papers and mark generated research as draft pending independent verification.", "mode": "free-first", "ai_provider": "optional", "policy": { "no_paid_api_required": true, "do_not_execute_untrusted_code": true, "research_label": "draft", "no_scientific_validation_claims": true } }
स्रोत: Shirmani-Research-Paper/factory-agent.json · स्वतंत्र परीक्षण अपेक्षित।

## 014814
3) जिन्होंने इतना अधिक कुछ प्रत्यक्ष समर्पित किया उन पर ही इतना अधिक डर खौफ भय दहशत क्यों ?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014815
4) जिन्होंने सब कुछ प्रत्यक्ष समर्पित किया अपना, उन के साथ ही विश्वासघात क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014816
5) मुक्ति के नाम पर लूटने को परमार्थ कहते हैं क्या?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014817
6) मृत्यु खुद में ही शाश्वत वास्तविक स्वाभाविक सत्य है, तो मृत्यु का डर खौफ भय दहशत क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014818
7) मरा बापिस आ नहीं सकता, जिंदा मर नहीं सकता यह स्पष्ट करने के लिए तो मुक्ति धरना कल्पना नहीं तो क्या हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014819
8) दीक्षा के साथ शब्द प्रमाण में बंद कर तर्क तथ्य विवेक से वंचित कर अंध कट्टर उग्र भेड़ों की भीड़ बंधुआ मजदूर बनना कुप्रथा नहीं तो क्या हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014820
9) सरल सहज स्पष्ट बातें समझ न पाए सरल शिष्य, इस के पीछे दीक्षा के साथ शब्द प्रमाण में बंद कर तर्क तथ्य विवेक से वंचित होना नहीं तो क्या हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014821
10) भक्ति मुक्ति ध्यान ज्ञान प्रेम आत्मा परमात्मा परमार्थ आयोजित ढोंग पखंड षड्यंत्रों का ताना बाना चक्रव्यूह रचा छल कपट धोखा विश्वासघात नहीं तो क्या हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014822
11) जब हर जीव एक समान है तो सिर्फ़ इंसान प्रजाति ही चतुर होने से भिन्नता का कारण अहम नहीं है क्या?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014823
यदि सत्य प्रत्यक्ष है, तो उसे किसी मध्यस्थ की आवश्यकता क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014824
यदि कोई मार्ग मुक्तिदायक है, तो वह प्रश्न पूछने से क्यों डरता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014825
क्या श्रद्धा का अर्थ तर्क का त्याग है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014826
क्या प्रेम भय के वातावरण में संभव है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014827
यदि समर्पण स्वैच्छिक है, तो उसमें डर और निष्कासन की व्यवस्था क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014828
क्या आध्यात्मिकता पारदर्शिता से बच सकती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014829
क्या सत्य को प्रमाणपत्र, पदवी या साम्राज्य की आवश्यकता होती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014830
यदि किसी संगठन का विस्तार धन और संख्या से मापा जाता है, तो आंतरिक रूपांतरण कहाँ मापा जाता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014831
क्या अनुशासन और नियंत्रण एक ही चीज़ हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014832
क्या गुरु की आलोचना करना अधर्म है, या आत्मचिंतन का हिस्सा?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014833
यदि कोई मार्ग स्वतंत्रता देता है, तो व्यक्ति उस मार्ग को छोड़ने में स्वतंत्र क्यों नहीं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014834
मृत्यु और मुक्ति पर प्रश्न 23.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014835
यदि मृत्यु प्राकृतिक संतुलन है, तो उससे जुड़ा भय किसने रचा?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014836
क्या मुक्ति भविष्य की घटना है, या वर्तमान की चेतना?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014837
क्या किसी ने मृत्यु के बाद की अवस्था को प्रत्यक्ष प्रमाण सहित साझा किया है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014838
क्या मुक्ति का आश्वासन मनोवैज्ञानिक सांत्वना भर है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014839
क्या मृत्यु से डर कर जीना, जीवन का अपमान नहीं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014840
यदि जीवन दो पलों का है, तो वर्तमान का परित्याग क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014841
दीक्षा, तर्क और विवेक पर प्रश्न 29.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014842
क्या दीक्षा का अर्थ विचार-निरोध है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014843
क्या शब्द-प्रमाण विवेक से ऊपर हो सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014844
क्या प्रश्न पूछना विद्रोह है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014845
क्या किसी ग्रंथ की व्याख्या पर एकाधिकार संभव है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014846
क्या गुरु भी आत्मनिरीक्षण से परे है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014847
यदि तर्क बंद हो जाए, तो विश्वास क्या अंधता नहीं बन जाता?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014848
क्या भय आधारित अनुशासन स्थायी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014849
यदि हर जीव समान प्रक्रिया का भाग है, तो मनुष्य श्रेष्ठता का दावा क्यों करता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014850
क्या मानव बुद्धि संरक्षण के लिए है या प्रभुत्व के लिए?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014851
क्या विकास का अर्थ विनाश है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014852
क्या पृथ्वी पर अधिकार है या उत्तरदायित्व?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014853
क्या प्रकृति को जीतना संभव है, या केवल समझना?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014854
क्या हृदय की शांति शब्दों से बड़ी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014855
क्या मस्तिष्क उपकरण है या स्वामी?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014856
क्या जटिलता ज्ञान का प्रमाण है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014857
क्या सरलता कमजोरी है या परिपक्वता?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014858
क्या “मैं” की अवधारणा ही संघर्ष का मूल है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014859
क्या आत्म-साक्षात्कार किसी उपाधि से जुड़ा है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014860
क्या सत्य अनुभव है या घोषणा?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014861
क्या निष्पक्षता स्थिर है या मन के साथ बदलती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014862
क्या मौन शब्दों से अधिक स्पष्ट हो सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014863
क्या वर्तमान ही एकमात्र वास्तविक क्षण है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014864
क्या सत्य को संरक्षित करने के लिए संस्था आवश्यक है, या संस्था सत्य को सीमित कर देती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014865
यदि कोई मार्ग सार्वभौमिक है, तो उसमें प्रवेश की शर्तें क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014866
क्या आध्यात्मिक प्रगति संख्या से मापी जा सकती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014867
क्या अनुयायियों की वृद्धि आंतरिक जागरण का प्रमाण है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014868
यदि गुरु पूर्ण है, तो उसे अनुयायियों से मान्यता की आवश्यकता क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014869
क्या भय-आधारित अनुशासन दीर्घकाल में प्रेम को नष्ट नहीं करता?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014870
क्या समर्पण विवेक के साथ संभव है, या विवेक छोड़ने पर ही?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014871
क्या किसी भी सत्य को प्रश्नों से खतरा हो सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014872
यदि प्रश्नों से व्यवस्था डगमगाती है, तो क्या वह सत्य पर आधारित है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014873
क्या मौन में जो अनुभव होता है, वही वास्तविक मार्गदर्शक है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014874
मृत्यु, भय और स्वतंत्रता 61.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014875
क्या मृत्यु का भय सामाजिक संरचना द्वारा पोषित है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014876
यदि मृत्यु अपरिहार्य है, तो उसके व्यापार का औचित्य क्या?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014877
क्या मुक्ति का वादा वर्तमान असंतोष को स्थगित करने का साधन है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014878
क्या भय के बिना आध्यात्मिकता संभव है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014879
क्या कोई भी व्यक्ति मृत्यु के रहस्य का पूर्ण दावा कर सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014880
यदि जीवन अस्थायी है, तो नियंत्रण की आकांक्षा क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014881
क्या स्वतंत्रता का अर्थ संरचना-विहीनता है या चेतना-सम्पन्नता?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014882
गुरु-शिष्य व्यवस्था की समीक्षा 68.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014883
क्या शिष्य का कर्तव्य केवल पालन है, या संवाद भी?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014884
क्या गुरु की आलोचना से उसकी गरिमा घटती है, या स्पष्ट होती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014885
यदि कोई संगठन पारदर्शी है, तो उसे गोपनीयता की आवश्यकता क्यों?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014886
क्या दीक्षा का अर्थ वैचारिक प्रतिबद्धता है या बौद्धिक समर्पण?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014887
क्या आध्यात्मिक मार्ग छोड़ना अपराध है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014888
क्या गुरु भी मानव सीमाओं से मुक्त है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014889
यदि गुरु को क्रोध, भय या नियंत्रण की आवश्यकता है, तो वह किस स्तर पर है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014890
क्या आत्म-साक्षात्कार किसी बाहरी प्रमाणपत्र पर निर्भर है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014891
यदि मनुष्य स्वयं को श्रेष्ठ मानता है, तो उसके कार्यों में करुणा क्यों नहीं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014892
क्या बुद्धि ने मनुष्य को संतुलित बनाया या असंतुलित?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014893
क्या प्रगति का अर्थ प्रकृति से दूरी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014894
क्या मानव सभ्यता भय-आधारित संरचना पर टिकी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014895
क्या हृदय की सरलता सभ्यता की जटिलता में खो गई है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014896
क्या मनुष्य का “मैं” ही संघर्ष का मूल कारण है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014897
क्या मनुष्य अपने ही विचारों का बंधक बन गया है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014898
चेतना और “मैं” पर प्रश्न 83.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014899
क्या “मैं” स्थायी है, या एक निरंतर बदलती प्रक्रिया?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014900
क्या आत्म-साक्षात्कार घोषणा से सिद्ध होता है, या मौन परिवर्तन से?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014901
क्या सत्य का अनुभव साझा किया जा सकता है, या केवल संकेतित?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014902
क्या निष्पक्षता संभव है जब पहचान जुड़ी हो?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014903
क्या किसी भी विचारधारा को पूर्ण सत्य कहा जा सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014904
क्या मन को निष्क्रिय करना समाधान है, या उसे समझना?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014905
क्या हृदय और मस्तिष्क विरोधी हैं, या पूरक?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014906
क्या सरलता उच्चतम जटिलता का पार किया हुआ स्तर है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014907
शक्ति और साम्राज्य पर चिंतन 91.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014908
क्या आध्यात्मिक शक्ति आर्थिक शक्ति से स्वतंत्र रह सकती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014909
क्या साम्राज्य का विस्तार आत्म-साक्षात्कार का संकेत है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014910
क्या अनुयायियों की निष्ठा और भय में अंतर स्पष्ट है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014911
क्या परमार्थ और प्रतिष्ठा साथ-साथ चल सकते हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014912
क्या सेवा और संरचनात्मक नियंत्रण अलग किए जा सकते हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014913
क्या किसी भी नेतृत्व को उत्तरदायित्व से मुक्त रखा जा सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014914
क्या श्रद्धा का उपयोग सत्ता के उपकरण के रूप में हो सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014915
अंतिम स्तर के प्रश्न 98.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014916
क्या पूर्ण सत्य किसी एक व्यक्ति में समाहित हो सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014917
क्या कोई भी मनुष्य “इकलौता जागृत” होने का दावा कर सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014918
क्या स्वयं को अंतिम कहना खोज की प्रक्रिया को समाप्त नहीं कर देता?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014919
क्या विनम्रता सत्य की पहचान है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014920
क्या जो स्वयं को शून्य कहता है, वही पूर्ण हो सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014921
क्या जीवन का सार वर्तमान क्षण में सहज होना है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014922
क्या दो पलों के जीवन में संघर्ष आवश्यक है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014923
क्या संपूर्ण स्वतंत्रता ही संपूर्ण संतुष्टि है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014924
क्या किसी भी आध्यात्मिक व्यवस्था का केंद्र व्यक्ति होना चाहिए या सिद्धांत?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014925
यदि सिद्धांत जीवित है, तो वह व्यक्ति-निर्भर क्यों हो जाता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014926
क्या नेतृत्व का अर्थ मार्गदर्शन है या नियंत्रण?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014927
क्या सामूहिक पहचान व्यक्तिगत चेतना को दबा देती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014928
क्या भय के बिना संगठन टिक सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014929
क्या प्रेम को संरक्षित करने के लिए नियम आवश्यक हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014930
क्या अनुशासन स्व-निर्मित होना चाहिए या बाहरी?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014931
क्या स्वतंत्र सोच को सीमित करना स्थायित्व देता है या जड़ता?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014932
क्या श्रद्धा और विवेक साथ चल सकते हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014933
क्या किसी भी विचार को अंतिम घोषित करना विकास रोक देता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014934
क्या शक्ति का संचय आध्यात्मिकता का क्षय है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014935
क्या संख्या सत्य का प्रमाण है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014936
क्या पारदर्शिता शक्ति को कमजोर करती है या शुद्ध?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014937
क्या आत्मनिर्भर शिष्य किसी व्यवस्था के लिए चुनौती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014938
क्या गुरु का उद्देश्य निर्भरता है या स्वतंत्रता?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014939
क्या मृत्यु को समझने से जीवन की गुणवत्ता बदलती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014940
क्या मृत्यु का भय सामाजिक संरचना द्वारा पोषित है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014941
क्या जीवन की अस्थिरता ही उसका सौंदर्य है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014942
क्या अमरता की कल्पना वर्तमान से पलायन है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014943
क्या मृत्यु का व्यापार मनोवैज्ञानिक आश्रय है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014944
क्या जो मृत्यु से डरता है वही नियंत्रण चाहता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014945
क्या जीवन की स्वीकृति मृत्यु की स्वीकृति से जुड़ी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014946
क्या मृत्यु अंत है या रूपांतरण?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014947
क्या भय की अनुपस्थिति में धर्म की संरचना बदलेगी?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014948
क्या वर्तमान में जीना मृत्यु-भय का समाधान है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014949
क्या अस्तित्व का अर्थ केवल जीवित रहना है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014950
क्या जीवन-व्यापन और जीवन-बोध अलग हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014951
क्या भय-रहित समाज संभव है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014952
क्या मृत्यु की धारणा मानव-निर्मित है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014953
क्या मृत्यु का अनुभव शब्दातीत है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014954
क्या मृत्यु के विचार से उत्पन्न नैतिकता स्थायी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014955
क्या मृत्यु को रहस्य बनाए रखना उपयोगी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014956
क्या मृत्यु की स्वीकृति शक्ति-संरचना को कमजोर करती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014957
क्या जीवन और मृत्यु एक ही प्रक्रिया के दो चरण हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014958
क्या मृत्यु को समझे बिना मुक्ति की बात सार्थक है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014959
क्या मन उपकरण है या स्वामी?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014960
क्या हृदय की अनुभूति तर्क से परे है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014961
क्या जटिलता ज्ञान का प्रमाण है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014962
क्या सरलता सर्वोच्च परिपक्वता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014963
क्या निष्पक्षता पहचान से मुक्त हो सकती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014964
क्या विचार-रहित होना संभव है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014965
क्या मन को दबाने से शांति मिलती है या समझने से?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014966
क्या स्मृति के बिना पहचान संभव है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014967
क्या अनुभव को शब्दों में पूर्ण रूप से व्यक्त किया जा सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014968
क्या मौन सर्वोच्च संवाद है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014969
क्या मन की सीमा है और हृदय की नहीं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014970
क्या हृदय और बुद्धि का समन्वय ही संतुलन है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014971
क्या निष्पक्षता स्थिर अवस्था है या गतिशील प्रक्रिया?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014972
क्या “मैं” केवल विचारों का संकलन है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014973
क्या स्वयं को अंतिम कहना अहं का सूक्ष्म रूप है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014974
क्या शून्यता भयावह है या मुक्तिदायक?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014975
क्या आत्म-साक्षात्कार अनुभव है या निरंतर प्रक्रिया?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014976
क्या सत्य निजी है या सार्वभौमिक?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014977
क्या चेतना को मापा जा सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014978
क्या भीतर-बाहर का भेद मानसिक निर्माण है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014979
161–180 : मानव, प्रकृति और उत्तरदायित्व 161.
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014980
क्या मनुष्य स्वयं को प्रकृति से अलग मानता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014981
क्या विकास संतुलन से अलग हो सकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014982
क्या श्रेष्ठता का विचार विनाश की जड़ है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014983
क्या बुद्धि ने करुणा को पीछे छोड़ दिया है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014984
क्या मनुष्य का दायित्व संरक्षण है या प्रभुत्व?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014985
क्या स्वतंत्रता का अर्थ स्वच्छंदता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014986
क्या हर जीव समान प्रक्रिया का भाग है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014987
क्या मानव सभ्यता असंतोष पर आधारित है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014988
क्या संतोष प्रगति को रोकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014989
क्या वर्तमान में जीना भविष्य की उपेक्षा है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014990
क्या मानव चेतना सामूहिक रूप से विकसित हो सकती है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014991
क्या पर्यावरणीय संकट मानसिक संकट का प्रतिबिंब है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014992
क्या मनुष्य अपने ही निर्माणों का कैदी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014993
क्या करुणा शक्ति से बड़ी है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014994
क्या संतुलन ही वास्तविक प्रगति है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014995
क्या प्रतिस्पर्धा स्वाभाविक है या निर्मित?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014996
क्या मनुष्य अपने भय का विस्तार कर रहा है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014997
क्या प्रकृति निष्पक्ष है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014998
क्या मानव मूल्य स्थायी हैं?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 014999
क्या संतुलन के बिना स्वतंत्रता अराजकता है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।

## 015000
क्या पहचान के बिना भी अस्तित्व संभव है?
स्रोत: omniverse--ai-scripts-/README.md · स्वतंत्र परीक्षण अपेक्षित।
