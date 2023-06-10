import unittest

from dri import load_dynamic_lib, Resolve


class TestLoadDynamicLib(unittest.TestCase):
    def test_load_dynamic_lib(self):
        bmd_module = load_dynamic_lib()
        self.assertIsNotNone(bmd_module)


class TestResolve(unittest.TestCase):
    def test_resolve_init(self):
        resolve = Resolve.resolve_init()
        self.assertIsNotNone(resolve)

    def test_Fusion(self):
        resolve = Resolve.resolve_init()
        fusion = resolve.Fusion()
        self.assertIsNotNone(fusion)

    def test_GetMediaStorage(self):
        resolve = Resolve.resolve_init()
        media_storage = resolve.GetMediaStorage()
        self.assertIsNotNone(media_storage)


if __name__ == "__main__":
    unittest.main()