import os
from pathlib import Path

from dri import load_dynamic_lib


class TestLoadDynamicLib:
    def test_load_dynamic_lib(self):
        bmd_module = load_dynamic_lib()
        assert bmd_module is not None


class TestResolve:
    def test_resolve_init(self, resolve):
        assert resolve is not None

    def test_Fusion(self, resolve):
        fusion = resolve.Fusion()
        assert fusion is not None

    def test_GetMediaStorage(self, resolve):
        media_storage = resolve.GetMediaStorage()
        assert media_storage is not None

    def test_GetProjectManager(self, resolve):
        project_manager = resolve.GetProjectManager()
        assert project_manager is not None

    def test_OpenPage(self, resolve):
        # Configuration
        current_page = resolve.GetCurrentPage()

        # Testing
        pages = ["media", "cut", "edit", "fusion", "color", "fairlight", "deliver"]
        result = []
        for page in pages:
            result.append(resolve.OpenPage(page))
        assert all(result) is True

        # Cleanup
        resolve.OpenPage(current_page)

    def test_GetCurrentPage(self, resolve):
        pages = ["media", "cut", "edit", "fusion", "color", "fairlight", "deliver"]
        assert resolve.GetCurrentPage() in pages

    def test_GetProductName(self, resolve):
        product_names = ["DaVinci Resolve Studio", "DaVinci Resolve"]
        assert resolve.GetProductName() in product_names

    def test_GetVersion(self, resolve):
        version = resolve.GetVersion()
        major = version[0]
        minor = version[1]
        patch = version[2]
        build = version[3]
        suffix = version[4]

        # Firstly, test version should be a list
        assert isinstance(version, list), "version should be a list"

        # Test whether the length of the version list is 5
        assert len(version) == 5, "Version should have exactly 5 items"

        # Test individual item's type
        assert isinstance(major, int), "Major version should be an integer"
        assert isinstance(minor, int), "Minor version should be an integer"
        assert isinstance(patch, int), "Patch version should be an integer"
        assert isinstance(build, int), "Build version should be an integer"
        assert isinstance(suffix, str), "Suffix should be a string"

    def test_GetVersionString(self, resolve):
        version = resolve.GetVersionString()
        assert isinstance(version, str)

    def test_LoadLayoutPreset(self, resolve):
        # Configuration
        resolve.SaveLayoutPreset("test_LoadLayoutPreset")

        # Testing
        result = resolve.LoadLayoutPreset("test_LoadLayoutPreset")
        assert result

        # Cleanup
        resolve.DeleteLayoutPreset("test_LoadLayoutPreset")

    def test_UpdateLayoutPreset(self, resolve):
        # Configuration
        resolve.SaveLayoutPreset("test_UpdateLayoutPreset")

        # Testing
        result = resolve.UpdateLayoutPreset("test_UpdateLayoutPreset")
        assert result

        # Cleanup
        resolve.DeleteLayoutPreset("test_UpdateLayoutPreset")

    def test_ExportLayoutPreset(self, resolve):
        # Configuration
        resolve.SaveLayoutPreset("test_ExportLayoutPreset")
        output_file = Path.home() / "Desktop" / "test_ExportLayoutPreset"

        # Testing
        result = resolve.ExportLayoutPreset("test_ExportLayoutPreset", f"{output_file}")
        assert result

        # Cleanup
        resolve.DeleteLayoutPreset("test_ExportLayoutPreset")
        if os.path.exists(output_file):
            os.remove(output_file)

    def test_DeleteLayoutPreset(self, resolve):
        # Configuration
        resolve.SaveLayoutPreset("test_DeleteLayoutPreset")

        # Testing
        result = resolve.DeleteLayoutPreset("test_DeleteLayoutPreset")
        assert result

    def test_SaveLayoutPreset(self, resolve):
        # Testing
        result = resolve.SaveLayoutPreset("test_SaveLayoutPreset")
        assert result

        # Cleanup
        resolve.DeleteLayoutPreset("test_SaveLayoutPreset")

    def test_ImportLayoutPreset(self, resolve):
        # Configuration
        resolve.SaveLayoutPreset("test_ImportLayoutPreset_EXPORTS")
        resolve.ExportLayoutPreset(
            "test_ImportLayoutPreset_EXPORTS",
            f"{Path.home()}/Desktop/test_ImportLayoutPreset_EXPORTS",
        )

        # Testing
        result = resolve.ImportLayoutPreset(
            f"{Path.home()}/Desktop/test_ImportLayoutPreset_EXPORTS",
            "test_ImportLayoutPreset_EXPORTS_ImportBack",
        )
        assert result

        # Cleanup
        resolve.DeleteLayoutPreset("test_ImportLayoutPreset_EXPORTS")
        resolve.DeleteLayoutPreset("test_ImportLayoutPreset_EXPORTS_ImportBack")
        os.remove(f"{Path.home()}/Desktop/test_ImportLayoutPreset_EXPORTS")

    # def test_Quit(self, resolve):
    #     result = self.resolve.Quit()
    #     self.assertIsNone(result)