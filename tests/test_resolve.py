import unittest

from dri import load_dynamic_lib, Resolve


class TestLoadDynamicLib(unittest.TestCase):
    def test_load_dynamic_lib(self):
        bmd_module = load_dynamic_lib()
        self.assertIsNotNone(bmd_module)


class TestResolve(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resolve = Resolve.resolve_init()
        # print("setup is done")

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("tear down is taking over")

    def test_resolve_init(self):
        self.assertIsNotNone(self.resolve)

    def test_Fusion(self):
        fusion = self.resolve.Fusion()
        self.assertIsNotNone(fusion)

    def test_GetMediaStorage(self):
        media_storage = self.resolve.GetMediaStorage()
        self.assertIsNotNone(media_storage)

    def test_GetProjectManager(self):
        project_manager = self.resolve.GetProjectManager()
        self.assertIsNotNone(project_manager)

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

    def test_GetCurrentPage(self):
        pages = ["media", "cut", "edit", "fusion", "color", "fairlight", "deliver"]
        self.assertIn(self.resolve.GetCurrentPage(), pages)

    def test_GetProductName(self):
        product_names = ["DaVinci Resolve Studio", "DaVinci Resolve"]
        self.assertIn(self.resolve.GetProductName(), product_names)


if __name__ == "__main__":
    unittest.main()