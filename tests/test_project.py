import pytest


@pytest.mark.usefixtures("resolve_init")
class TestProject:
    def test_GetMediaPool(self):
        project_manager = self.resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()
        assert media_pool is not None