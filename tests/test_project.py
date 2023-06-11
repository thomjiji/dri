import unittest

from dri import Resolve
from tests.test_resolve import skip_if_resolve_none


class TestProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resolve = Resolve.resolve_init()

    @skip_if_resolve_none
    def test_GetMediaPool(self):
        project_manager = self.resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()
        self.assertIsNotNone(media_pool)


if __name__ == "__main__":
    unittest.main()