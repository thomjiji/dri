import unittest

from dri import load_dynamic_lib, Resolve
from tests import skip_if_resolve_none


class TestLoadDynamicLib(unittest.TestCase):
    def test_load_dynamic_lib(self):
        bmd_module = load_dynamic_lib()
        self.assertIsNotNone(bmd_module)


class TestResolve(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resolve = Resolve.resolve_init()

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


if __name__ == "__main__":
    unittest.main()