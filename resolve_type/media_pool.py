from dataclasses import dataclass
from typing import Literal

from resolve_type.folder import Folder
from resolve_type.media_pool_item import MediaPoolItem
from resolve_type.timeline import Timeline
from resolve_type.timeline_item import TimelineItem


@dataclass
class ClipInfo:
    """
    Information about a clip for API usage as argument.

    Attributes
    ----------
    mediaPoolItem : MediaPoolItem
        The media pool item associated with the clip.
    startFrame : int
        The starting frame of the clip.
    endFrame : int
        The ending frame of the clip.
    mediaType : Literal[1, 2]
        The type of media for the clip. Optional.
        - 1: Video only
        - 2: Audio only

    Examples
    --------
    >>> clip_info = {
    ...     "mediaPoolItem": MediaPoolItem,
    ...     "startFrame": 0,
    ...     "endFrame": 12,
    ...     "mediaType": 1
    ... }

    """

    mediaPoolItem: MediaPoolItem
    startFrame: int
    endFrame: int
    mediaType: Literal[1, 2] = None  # 1 - Video only, 2 - Audio only


@dataclass
class ImportOption:
    """
    For `ImportTimelineFromFile()` use.

    Attributes
    ----------
    timelineName : str
        Specifies the name of the timeline to be created. Not valid for DRT import.
    sourceClipsPath : str
        Specifies a filesystem path to search for source clips if the media is
        inaccessible in their original path and if "importSourceClips" is True.
    sourceClipsFolders : list[Folder]
        List of Media Pool folder objects to search for source clips if the media is not
        present in the current folder and if "importSourceClips" is False. Not valid for
        DRT import.
    interlaceProcessing : bool
        Specifies whether to enable interlace processing on the imported timeline being
        created. Valid only for AAF import.
    importSourceClips : bool, optional
        Specifies whether source clips should be imported. True by default. Not valid
        for DRT import.

    """

    timelineName: str
    sourceClipsPath: str
    sourceClipsFolders: list[Folder]
    interlaceProcessing: bool
    importSourceClips: bool = True


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

    def AppendToTimeline(
        self, clip: MediaPoolItem, *clips: MediaPoolItem
    ) -> list[TimelineItem]:
        """
        Appends specified MediaPoolItem objects in the current timeline. Returns the
        list of appended timelineItems.

        """
        ...

    def AppendToTimeline(
        self, clips: list[MediaPoolItem | ClipInfo]
    ) -> list[TimelineItem]:
        """
        Notes
        -----

        -   If input is list of *MediaPoolItem*:

        Appends specified MediaPoolItem objects in the current timeline. Returns the
        list of appended timelineItems.

        -   If input is list of *ClipInfos*:

        Appends list of clipInfos specified as dict of "mediaPoolItem", "startFrame"
        (int), "endFrame" (int), (optional) "mediaType" (int; 1 - Video only,
        2 - Audio only). Returns the list of appended timelineItems.

        """
        ...

    def CreateTimelineFromClips(
        self, timeline_name: str, *clips: MediaPoolItem
    ) -> Timeline:
        """
        Creates new timeline with specified name, and appends the specified
        MediaPoolItem objects.

        """
        ...

    def CreateTimelineFromClips(
        self, timeline_name: str, clips: list[MediaPoolItem | ClipInfo]
    ) -> Timeline:
        """
        Notes
        -----

        -   If input is list of *MediaPoolItem*:
            Creates new timeline with specified name, and appends the specified
            MediaPoolItem objects.

        -   If input is list of *ClipInfos*:
            Creates new timeline with specified name, appending the list of clipInfos
            specified as a dict of "mediaPoolItem", "startFrame" (int), "endFrame"
            (int).

        """
        ...

    def ImportTimelineFromFile(
        self, file_path: str, import_option: ImportOption
    ) -> Timeline:
        """
        Creates timeline based on parameters within given file (
        AAF/EDL/XML/FCPXML/DRT/ADL) and optional importOptions dict, with support for
        the keys:

        -   timelineName: string, specifies the name of the timeline to be created. Not
            valid for DRT import.

        -   importSourceClips: Bool, specifies whether source clips should be imported.
            True by default. Not valid for DRT import.

        -   sourceClipsPath: string, Specifies a filesystem path to search for source
            clips if the media is inaccessible in their original path and if
            "importSourceClips" is True.

        -   sourceClipsFolders: List of Media Pool folder objects to search for source
            clips if the media is not present in the current folder and if
            "importSourceClips" is False. Not valid for DRT import.

        -   interlaceProcessing: Bool, specifies whether to enable interlace processing
            on the imported timeline being created. Valid only for AAF import.

        """
        ...

    def DeleteTimelines(self, timeline: Timeline | list[Timeline]) -> bool:
        """
        Deletes specified timelines in the media pool.

        """
        ...

    def GetCurrentFolder(self) -> Folder:
        """
        Returns currently selected Folder.

        """
        ...

    def SetCurentFolder(self, folder: Folder) -> bool:
        """
        Sets current folder by given Folder

        """
        ...

    def DeleteClips(self, clips: MediaPoolItem | list[MediaPoolItem]) -> bool:
        """
        Deletes specified clips or timeline mattes in the media pool.

        """
        ...

    def ImportFolderFromFile(self, file_path: str, source_clips_path: str = "") -> bool:
        """
        Returns true if import from given DRB filePath is successful, false otherwise.

        Parameters
        ----------
        file_path
            DRB file path.
        source_clips_path
            sourceClipsPath is a string that specifies a filesystem path to search for
            source clips if the media is inaccessible in their original path, empty by
            default.

        """
        ...

    def DeleteFolders(self, subfolders: Folder | list[Folder]) -> bool:
        """
        Deletes specified subfolders in the media pool.

        """
        ...