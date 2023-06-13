import unittest

from dri import Resolve
from tests import skip_if_resolve_none, start_davinci_resolve_app
from tests import log


def setUpModule():
    if start_davinci_resolve_app():
        log.info("Successfully launched the Resolve app")
    resolve = Resolve.resolve_init()
    project_manager = resolve.GetProjectManager()
    if project_manager.CreateProject("Dri_Tests_Project"):
        log.info("Created Dri_test_project (from setUpModule)")


def tearDownModule():
    resolve = Resolve.resolve_init()
    pm = resolve.GetProjectManager()
    cp = pm.GetCurrentProject()
    if pm.CloseProject(cp):
        log.info("Closed project (from tearDownModule)")
    if pm.DeleteProject("Dri_Tests_Project"):
        log.info("Deleted project (from tearDownModule)")
    resolve.Quit()


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
    # unittest.main()
    # Create test loader to load tests
    loader = unittest.TestLoader()
    # Create test suite to group tests (In this test module, It's not necessary to)
    suite = unittest.TestSuite()

    # Add tests to test suite
    suite.addTest(loader.loadTestsFromTestCase(TestProject))

    # Create a test runner
    runner = unittest.TextTestRunner(verbosity=2)

    # Run the tests using the test runner and suite
    result = runner.run(suite)