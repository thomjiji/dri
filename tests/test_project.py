class TestProject:
    def test_GetMediaPool(self, project):
        media_pool = project.GetMediaPool()
        assert media_pool is not None

    def test_GetTimelineCount(self, project):
        timeline_count = project.GetTimelineCount()
        assert isinstance(timeline_count, int)

    def test_GetTimelineByIndex(self, project):
        timeline_count = project.GetTimelineCount()

        if timeline_count == 0:
            media_pool = project.GetMediaPool()
            media_pool.CreateEmptyTimeline("test_GetTimelineByIndex")

        tl = project.GetTimelineByIndex(project.GetTimelineCount())
        result = tl.SetStartTimecode("01:00:00:01")
        assert result