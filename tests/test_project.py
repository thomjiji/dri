import unittest

from dri import Resolve
from tests import skip_if_resolve_none
from tests import log


class TestProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resolve = Resolve.resolve_init()
        log.info("TestProject additional setUp operation")

    @skip_if_resolve_none
    def test_GetMediaPool(self):
        project_manager = self.resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()
        self.assertIsNotNone(media_pool)


if __name__ == "__main__":
    unittest.main()