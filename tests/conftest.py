import pytest

from dri import Resolve
from tests import log, start_davinci_resolve_app


@pytest.fixture(scope="module")
def resolve():
    r = Resolve.resolve_init()
    log.info("resolve object initialized")
    yield r


@pytest.fixture(scope="class")
def project(resolve):
    pm = resolve.GetProjectManager()
    cp = pm.GetCurrentProject()
    log.info(f"Current project: {cp.GetName()}")
    yield cp


@pytest.fixture(scope="class")
def media_pool(resolve, project):
    mp = project.GetMediaPool()
    yield mp


@pytest.fixture(scope="session", autouse=True)
def setup_teardown_session():
    if start_davinci_resolve_app():
        log.info("Successfully launched the Resolve app (from setUp)")
    r = Resolve.resolve_init()
    pm = r.GetProjectManager()
    if pm.CreateProject("Dri_Tests_Project"):
        log.info("Created Dri_test_project (from setUp)")

    yield r, pm  # Execute the tests

    cp = pm.GetCurrentProject()
    if pm.CloseProject(cp):
        log.info("Closed project (from tearDown)")
    if pm.DeleteProject("Dri_Tests_Project"):
        log.info("Deleted project (from tearDown)")
    r.Quit()