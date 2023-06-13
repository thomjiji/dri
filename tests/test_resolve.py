import atexit
import os.path
import unittest
import subprocess
import time

from dri import load_dynamic_lib, Resolve
from tests import skip_if_resolve_none


def close_delete_project_and_quit(r):
    pm = r.GetProjectManager()
    cp = pm.GetCurrentProject()
    print(f"current project is {cp.GetName()}")
    if project_manager.CloseProject(cp):
        print("CloseProject is called")
    if project_manager.DeleteProject("Dri_Tests_Project"):
        print("DeleteProject is called")
    resolve.Quit()


def start_davinci_resolve_app():
    subprocess.run(["open", "-a", "DaVinci Resolve"])
    time.sleep(10)


class TestLoadDynamicLib(unittest.TestCase):
    def test_load_dynamic_lib(self):
        bmd_module = load_dynamic_lib()
        self.assertIsNotNone(bmd_module)


class TestResolve(unittest.TestCase):
    resolve = None

    @classmethod
    def setUpClass(cls) -> None:
        start_davinci_resolve_app()
        resolve = Resolve.resolve_init()
        project_manager = resolve.GetProjectManager()
        if project_manager.CreateProject("Dri_Tests_Project"):
            log.info("Created Dri_test_project")
        cls.resolve = resolve

    @classmethod
    def tearDownClass(cls) -> None:
        # r = Resolve.resolve_init()
        pm = cls.resolve.GetProjectManager()
        cp = pm.GetCurrentProject()
        if pm.CloseProject(cp):
            log.info("CloseProject is called")
        if pm.DeleteProject("Dri_Tests_Project"):
            log.info("DeleteProject is called")
        cls.resolve.Quit()

    def test_resolve_init(self):
        self.assertIsNotNone(self.resolve)

    @skip_if_resolve_none
    def test_Fusion(self):
        fusion = self.resolve.Fusion()
        self.assertIsNotNone(fusion)

    @skip_if_resolve_none
    def test_GetMediaStorage(self):
        media_storage = self.resolve.GetMediaStorage()
        self.assertIsNotNone(media_storage)

    @skip_if_resolve_none
    def test_GetProjectManager(self):
        project_manager = self.resolve.GetProjectManager()
        self.assertIsNotNone(project_manager)

    @skip_if_resolve_none
    def test_OpenPage(self):
        # Precondition and configuration
        current_page = self.resolve.GetCurrentPage()

        # The actual testing
        pages = ["media", "cut", "edit", "fusion", "color", "fairlight", "deliver"]
        result = []
        for page in pages:
            result.append(self.resolve.OpenPage(page))
        self.assertTrue(all(result))

        # Back to the initial state
        self.resolve.OpenPage(current_page)

    @skip_if_resolve_none
    def test_GetCurrentPage(self):
        pages = ["media", "cut", "edit", "fusion", "color", "fairlight", "deliver"]
        self.assertIn(self.resolve.GetCurrentPage(), pages)

    @skip_if_resolve_none
    def test_GetProductName(self):
        product_names = ["DaVinci Resolve Studio", "DaVinci Resolve"]
        self.assertIn(self.resolve.GetProductName(), product_names)

    @skip_if_resolve_none
    def test_GetVersion(self):
        version = self.resolve.GetVersion()
        major = version[0]
        minor = version[1]
        patch = version[2]
        build = version[3]
        suffix = version[4]

        # Firstly, test version should be a list
        self.assertIsInstance(version, list, "version should be a list")

        # Test whether the length of the version list is 5
        self.assertEqual(len(version), 5, "Version should have exactly 5 items")

        # Test individual item's type
        self.assertIsInstance(major, int, "Major version should be an integer")
        self.assertIsInstance(minor, int, "Minor version should be an integer")
        self.assertIsInstance(patch, int, "Patch version should be an integer")
        self.assertIsInstance(build, int, "Build version should be an integer")
        self.assertIsInstance(suffix, str, "Suffix should be a string")

    @skip_if_resolve_none
    def test_GetVersionString(self):
        version = self.resolve.GetVersionString()
        self.assertIsInstance(version, str)

    @skip_if_resolve_none
    def test_LoadLayoutPreset(self):
        # Precondition and configuration
        self.resolve.SaveLayoutPreset("test_LoadLayoutPreset")

        result = self.resolve.LoadLayoutPreset("test_LoadLayoutPreset")
        self.assertTrue(result)

        # Back to the initial state
        self.resolve.DeleteLayoutPreset("test_LoadLayoutPreset")

    @skip_if_resolve_none
    def test_UpdateLayoutPreset(self):
        pass

    @skip_if_resolve_none
    def test_ExportLayoutPreset(self):
        # Precondition and configuration
        self.resolve.SaveLayoutPreset("test_ExportLayoutPreset")
        output_file = "/Users/thom/Desktop/test_ExportLayoutPreset"

        # The actual testing
        result = self.resolve.ExportLayoutPreset(
            "test_ExportLayoutPreset", "/Users/thom/Desktop/test_ExportLayoutPreset"
        )
        self.assertTrue(result)

        # Cleanup
        self.resolve.DeleteLayoutPreset("test_ExportLayoutPreset")
        if os.path.exists(output_file):
            os.remove(output_file)

    @skip_if_resolve_none
    def test_DeleteLayoutPreset(self):
        # Precondition and configuration
        self.resolve.SaveLayoutPreset("test_DeleteLayoutPreset")

        # Testing
        result = self.resolve.DeleteLayoutPreset("test_DeleteLayoutPreset")
        self.assertTrue(result)

    @skip_if_resolve_none
    def test_SaveLayoutPreset(self):
        self.resolve.SaveLayoutPreset("test_SaveLayoutPreset")

        # Cleanup
        self.resolve.DeleteLayoutPreset("test_SaveLayoutPreset")

    @skip_if_resolve_none
    def test_ImportLayoutPreset(self):
        # Precondition and configuration
        self.resolve.SaveLayoutPreset("test_ImportLayoutPreset_EXPORTS")
        self.resolve.ExportLayoutPreset(
            "test_ImportLayoutPreset_EXPORTS",
            "/Users/thom/Desktop/test_ImportLayoutPreset_EXPORTS",
        )

        # Testing
        result = self.resolve.ImportLayoutPreset(
            "/Users/thom/Desktop/test_ImportLayoutPreset_EXPORTS",
            "test_ImportLayoutPreset_IMPORTS",
        )
        self.assertTrue(result)

        # Cleanup
        self.resolve.DeleteLayoutPreset("test_ImportLayoutPreset_EXPORTS")
        self.resolve.DeleteLayoutPreset("test_ImportLayoutPreset_IMPORTS")
        os.remove("/Users/thom/Desktop/test_ImportLayoutPreset_EXPORTS")

    # @skip_if_resolve_none
    # def test_Quit(self):
    #     result = self.resolve.Quit()
    #     self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()