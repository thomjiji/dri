from dri.graph import Graph
from dri.timeline import Timeline
from dri.timeline_item import TimelineItem


class ColorGroup:
    def GetName(self) -> str:
        """
        Returns the name (string) of the ColorGroup.
        """
        ...

    def SetName(self, group_name: str) -> bool:
        """
        Renames ColorGroup to groupName (string).
        """
        ...

    def GetClipsInTimeline(self, timeline: Timeline) -> list[TimelineItem]:
        """
        Returns a list of TimelineItem that are in colorGroup in the given Timeline.
        Timeline is Current Timeline by default.
        """
        ...

    def GetPreClipNodeGraph(self) -> Graph:
        """
        Returns the ColorGroup Pre-clip graph.
        """
        ...

    def GetPostClipNodeGraph(self) -> Graph:
        """
        Returns the ColorGroup Post-clip graph.
        """
        ...
