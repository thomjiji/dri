from dri.timeline import Timeline
from dri.media_pool import MediaPool


class Project:
    def GetMediaPool(self) -> MediaPool:
        ...

    def GetCurrentTimeline(self) -> Timeline:
        ...