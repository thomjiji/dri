import os
from pathlib import Path

import pytest

from tests import log


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

    @pytest.fixture
    def import_helen_john_to_media_pool(self, project, media_pool):
        helen_john_file_path = (
            f"{Path(__file__).parent.parent}/static"
            f"/ARRI_Helen_John_ALEXA_35_ARRIRAW.jpg"
        )
        helen_john_media_pool_item = media_pool.ImportMedia([helen_john_file_path])
        media_pool.CreateTimelineFromClips(
            "test_AddRenderJob", helen_john_media_pool_item
        )

        yield helen_john_media_pool_item

        current_timeline = project.GetCurrentTimeline()
        media_pool.DeleteTimelines(current_timeline)
        media_pool.DeleteClips(helen_john_media_pool_item)

    def test_AddRenderJob(
        self, project, project_manager, import_helen_john_to_media_pool
    ):
        if project_manager.SaveProject():
            log.info("Save project")
        render_target_dir = f"{Path.home()}/Desktop/"
        project.SetRenderSettings({"TargetDir": render_target_dir})
        job_id = project.AddRenderJob()
        log.info(f"test_AddRenderJob job id: {job_id}")
        log.info(f"test_AddRenderJob render queue: {project.GetRenderJobList()}")
        assert job_id
        assert isinstance(job_id, str)
        project.DeleteRenderJob(job_id)

    def test_DeleteRenderJob(self, project, import_helen_john_to_media_pool):
        render_target_dir = f"{Path.home()}/Desktop/"
        project.SetRenderSettings({"TargetDir": render_target_dir})
        job_id = project.AddRenderJob()
        log.info(f"test_DeleteRenderJob job id: {job_id}")
        log.info(f"test_DeleteRenderJob render queue: {project.GetRenderJobList()}")
        result = project.DeleteRenderJob(job_id)
        assert result

    def test_DeleteAllRenderJobs(self, project, import_helen_john_to_media_pool):
        render_target_dir = f"{Path.home()}/Desktop/"
        project.SetRenderSettings({"TargetDir": render_target_dir})
        job_id_1 = project.AddRenderJob()
        job_id_2 = project.AddRenderJob()
        log.info(f"test_DeleteRenderJob job id 1: {job_id_1}, job id 2: {job_id_2}")
        result = project.DeleteAllRenderJobs()
        assert result

    def test_GetRenderJobList(self, project, import_helen_john_to_media_pool):
        render_target_dir = f"{Path.home()}/Desktop/"
        project.SetRenderSettings({"TargetDir": render_target_dir})
        project.AddRenderJob()
        project.AddRenderJob()
        result = project.GetRenderJobList()
        assert result
        project.DeleteAllRenderJobs()

    @pytest.mark.skip("skipped due to AddRenderJob() bug")
    def test_StartRendering(self, project, import_helen_john_to_media_pool):
        render_target_dir = f"{Path.home()}/Desktop/"
        project.SetRenderSettings(
            {"TargetDir": render_target_dir, "CustomName": "test_StartRendering_1"}
        )
        job_id_1 = project.AddRenderJob()

        project.SetRenderSettings(
            {"TargetDir": render_target_dir, "CustomName": "test_startRendering_2"}
        )
        job_id_2 = project.AddRenderJob()

        result = project.StartRendering(job_id_1, job_id_2)
        assert result

        project.StopRendering()
        project.DeleteRenderJob(job_id_1, job_id_2)
        os.remove(f"{Path.home()}/Desktop/test_StartRendering_1")
        # os.remove(f"{Path.home()}/Desktop/test_StartRendering_2")