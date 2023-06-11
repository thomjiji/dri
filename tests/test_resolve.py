import unittest

from dri import load_dynamic_lib, Resolve


def skip_if_resolve_none(func):
    def wrapper(self, *args, **kwargs):
        if self.resolve is None:
            self.skipTest("resolve object is None, skipping test.")
        else:
            return func(self, *args, **kwargs)

    return wrapper


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
        self.assertIsNotNone(version)


if __name__ == "__main__":
    unittest.main()