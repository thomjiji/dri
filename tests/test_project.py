class TestProject:
    def test_GetMediaPool(self, resolve_init):
        resolve = resolve_init
        project_manager = resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()
        assert media_pool is not None