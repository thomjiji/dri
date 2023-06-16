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