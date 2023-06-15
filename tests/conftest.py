import pytest

from dri import Resolve
from tests import log, start_davinci_resolve_app


@pytest.fixture(scope="class")
def resolve_init(request):
    resolve = Resolve.resolve_init()
    log.info("resolve object initialized")
    request.cls.resolve = resolve
    yield resolve


@pytest.fixture(scope="session", autouse=True)
def setup_teardown_session():
    if start_davinci_resolve_app():
        log.info("Successfully launched the Resolve app")
    resolve = Resolve.resolve_init()
    project_manager = resolve.GetProjectManager()
    if project_manager.CreateProject("Dri_Tests_Project"):
        log.info("Created Dri_test_project (from setUpModule)")

    yield resolve, project_manager  # Execute the tests

    pm = resolve.GetProjectManager()
    cp = pm.GetCurrentProject()
    if pm.CloseProject(cp):
        log.info("Closed project (from tearDownModule)")
    if pm.DeleteProject("Dri_Tests_Project"):
        log.info("Deleted project (from tearDownModule)")
    resolve.Quit()