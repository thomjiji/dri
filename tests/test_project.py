import unittest

from dri import Resolve


class TestProject(unittest.TestCase):
    def test_GetMediaPool(self):
        resolve = Resolve.resolve_init()
        project_manager = resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()
        self.assertIsNotNone(media_pool)


if __name__ == "__main__":
    unittest.main()