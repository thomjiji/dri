from pathlib import Path


class TestProject:
    def test_GetMediaPool(self, project):
        media_pool = project.GetMediaPool()
        assert media_pool is not None

    def test_GetTimelineCount(self, project):
        timeline_count = project.GetTimelineCount()
        assert isinstance(timeline_count, int)

    def test_GetTimelineByIndex(self, project, media_pool):
        # Configuration
        timeline_count = project.GetTimelineCount()

        # If there is no timeline yet, create it.
        if timeline_count == 0:
            media_pool.CreateEmptyTimeline("test_GetTimelineByIndex")

        timeline = None
        try:
            # Testing
            timeline = project.GetTimelineByIndex(project.GetTimelineCount())
            assert timeline
        finally:
            # Cleanup
            media_pool.DeleteTimelines(timeline)

    def test_GetCurrentTimeline(self, project, media_pool):
        if not project.GetCurrentTimeline():
            media_pool.CreateEmptyTimeline("test_GetCurrentTimeline")

        current_timeline = None
        try:
            # Testing
            current_timeline = project.GetCurrentTimeline()
            assert current_timeline
        finally:
            # Cleanup
            media_pool.DeleteTimelines(current_timeline)

    def test_SetCurrentTimeline(self, project, media_pool):
        timeline_1 = media_pool.CreateEmptyTimeline("test_SetCurrentTimeline_1")
        timeline_2 = media_pool.CreateEmptyTimeline("test_SetCurrentTimeline_2")

        try:
            result = project.SetCurrentTimeline(timeline_1)
            assert result
        finally:
            media_pool.DeleteTimelines([timeline_1, timeline_2])

    def test_GetGallery(self, project):
        result = project.GetGallery()
        assert result

    def test_GetName(self, project):
        result = project.GetName()
        assert isinstance(result, str)

    def test_SetName(self, project):
        try:
            # If the new name differs from the old name, the project is renamed
            # successfully. It will return True.
            result = project.SetName("Dri_Tests_Project_renamedBy_SetName")
            assert result is True

            # If the new name is the same as the old name, it will return False.
            result = project.SetName("Dri_Tests_Project_renamedBy_SetName")
            assert result is False
        finally:
            project.SetName("Dri_Tests_Project")

    def test_GetPresetList(self, project):
        preset_list = project.GetPresetList()
        # Preset list need to be a list
        assert isinstance(preset_list, list)

        for preset in preset_list:
            # Inside preset list, there are dictionaries
            assert isinstance(preset, dict)
            for k, v in preset.items():
                # The key of the dictionaries is str, the value of the dictionaries
                # is str or int
                assert isinstance(k, str)
                assert isinstance(v, str | int)

    def test_SetPreset(self, project):
        # Now really sure how to handle this setting
        pass

    def test_AddRenderJob(self, project, media_pool):
        helen_john_file_path = (
            f"{Path(__file__).parent.parent}/static"
            f"/ARRI_Helen_John_ALEXA_35_ARRIRAW.jpg"
        )
        helen_john_mediaPoolItem = media_pool.ImportMedia([helen_john_file_path])
        media_pool.CreateTimelineFromClips(
            "test_AddRenderJob", helen_john_mediaPoolItem
        )

        job_id = None
        try:
            job_id = project.AddRenderJob()
            assert isinstance(job_id, str)
        finally:
            current_timeline = project.GetCurrentTimeline()
            media_pool.DeleteTimelines(current_timeline)
            media_pool.DeleteClips(helen_john_mediaPoolItem)
            project.DeleteRenderJob(job_id)