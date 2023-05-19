from dataclasses import dataclass
from multipledispatch import dispatch

from .media_pool_item import MediaPoolItem
from .timeline import Timeline
from .timeline_item import TimelineItem
from .folder import Folder


@dataclass
class ClipInfo:
    mediaPoolItem: MediaPoolItem
    startFrame: int
    endFrame: int
    mediaType: int  # 1 - Video only, 2 - Audio only


class MediaPool:
    def GetRootFolder(self) -> Folder:
        """
        Returns root Folder of Media Pool.

        """
        ...

    def AddSubFolder(self, folder: Folder, name: str) -> Folder:
        """
        Adds new subfolder under specified Folder object with the given name.

        """
        ...

    def RefreshFolders(self) -> bool:
        """
        Updates the folders in collaboration mode.

        """
        ...

    def CreateEmptyTimeline(self, name: str) -> Timeline:
        """
        Adds new timeline with given name.

        """
        ...

    @dispatch(MediaPoolItem, MediaPoolItem)
    def AppendToTimeline(self, clip, *args) -> list[TimelineItem]:
        """
        Appends specified MediaPoolItem objects in the current timeline. Returns the
        list of appended timelineItems.

        """
        ...

    @dispatch(list[MediaPoolItem | ClipInfo])
    def AppendToTimeline(self, clips) -> list[TimelineItem]:
        """
        Notes
        -----

        - if input is list of *MediaPoolItem*:

        Appends specified MediaPoolItem objects in the current timeline. Returns the
        list of appended timelineItems.

        - if input is list of *ClipInfos*:

        Appends list of clipInfos specified as dict of "mediaPoolItem", "startFrame"
        (int), "endFrame" (int), (optional) "mediaType" (int; 1 - Video only,
        2 - Audio only). Returns the list of appended timelineItems.

        - Even if it needs to accept a list as an argument, but you pass it an item,
        it will work fine.

        """
        ...