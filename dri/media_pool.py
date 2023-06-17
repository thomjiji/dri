from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from dri.folder import Folder
from dri.media_pool_item import MediaPoolItem
from dri.timeline import Timeline
from dri.timeline_item import TimelineItem


@dataclass
class ClipInfo:
    """
    Information about a clip for API usage as argument.

    Attributes
    ----------
    mediaPoolItem : MediaPoolItem
        The media pool item associated with the clip.
    startFrame : int
        The starting frame of the clip. Optional. If not specified, using 0.
    endFrame : int
        The ending frame of the clip. Optional. If no specified, using the last frame.
    mediaType : Literal[1, 2]
        The type of media for the clip. Optional.
        -   1: Video only
        -   2: Audio only
    trackIndex : int
        Indicates which track of the timeline the clip will be inserted into. Optional.
        -   If there is only one video track in the timeline: V1, then if trackIndex is
            set to 2, which means the clip will be inserted into the timeline's video
            track V2, then the API will automatically add video track V2 and insert the
            clip into V2.
        -   However, the API does not work if the trackIndex is set to 3 or more when
            only one video track V1 exists. The clip will stil be inserted into V1.
    recordFrame: int
        Indicates where in the timeline the clip will be inserted, in Frames. Optional.

    Examples
    --------
    >>> clip_info = {
    ...     "mediaPoolItem": MediaPoolItem,
    ...     "startFrame": 0,
    ...     "endFrame": 12,
    ...     "mediaType": 1
    ...     "trackIndex": 2,
    ...     "recordFrame": 86400,
    ... }

    """

    mediaPoolItem: MediaPoolItem
    startFrame: int = None
    endFrame: int = None
    mediaType: Literal[1, 2] = None  # 1 - Video only, 2 - Audio only
    recordFrame: int = None
    trackIndex: int = None


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
            2 - Audio only), "trackIndex" (int) and "recordFrame" (int). Returns the
            list of appended timelineItems.

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
            (int), "recordFrame" (int).

            -   ClipInfo that CreateTimelineFromClips accept can't include "trackIndex",
                otherwise DaVinci Resolve will crash.

        """
        ...

    def ImportTimelineFromFile(
        self, file_path: str, import_option: ImportOption
    ) -> Timeline:
        """
        Creates timeline based on parameters within given file
        (AAF/EDL/XML/FCPXML/DRT/ADL) and optional importOptions dict, with support for
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
            DRB (DaVinci Resolve Bin file) file path.
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

    def MoveClips(self, clips: list[MediaPoolItem], target_folder: Folder) -> bool:
        """
        Move specified clips to target folder.

        Parameters
        ----------
        clips
            Clips to be moved. This method don't accept one MediaPoolItem, it only
            accepts a list of MediaPoolItem.
        target_folder
            Moving destination.

        Returns
        -------
        bool
            True if successful, false otherwise.

        """
        ...

    def MoveFolders(self, folders: list[Folder], target_folder: Folder) -> bool:
        """
        Moves specified folders to target folder.

        Parameters
        ----------
        folders
            Folders to be moved. This method don't accept one Folder, it only accepts a
            list of Folder.
        target_folder
            Moving destination.

        Returns
        -------
        bool
            True if successful, false otherwise.

        """
        ...

    def GetClipMatteList(self, media_pool_item: MediaPoolItem) -> list[Path]:
        """
        Get mattes for specified MediaPoolItem, as a list of paths to the matte files.

        Parameters
        ----------
        media_pool_item

        Returns
        -------
        list[Path]
            a list of paths to the matte files.

        """
        ...

    def GetTimelineMatteList(self, folder: Folder) -> list[MediaPoolItem]:
        """
        Get mattes in specified Folder, as list of MediaPoolItems.

        Parameters
        ----------
        folder
            Where to get mattes.

        Returns
        -------
        list[MediaPoolItem]
            Get mattes as list of MediaPoolItems.

        """
        ...

    def DeleteClipMattes(
        self, media_pool_item: MediaPoolItem, paths: list[str]
    ) -> bool:
        """
        Delete mattes based on their file paths, for specified MediaPoolItem. Returns
        True on success.

        Parameters
        ----------
        media_pool_item
            Target
        paths
            Paths of mattes to be deleted

        Returns
        -------
        bool
            True if delete successfully, False otherwise.

        """
        ...

    def RelinkClips(self, clips: list[MediaPoolItem], folder_path: str) -> bool:
        """
        Update the folder location of specified media pool clips with the specified
        folder path.

        Parameters
        ----------
        clips
            Clips to be relinked. Don't accept one clip (MediaPoolItem) as argument, it
            only accepts a list of clips (MediaPoolItem).
        folder_path
            The new path to which clips will be relinked.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def UnlinkClips(self, clips: list[MediaPoolItem]) -> bool:
        """
        Unlink specified media pool clips.

        Parameters
        ----------
        clips
            Clips to be unlinked.

        Returns
        -------
        bool
            True if unlink successful, False otherwise.

        """
        ...

    def ImportMedia(self, paths: list[str]) -> list[MediaPoolItem]:
        """
        Imports specified file/folder paths into current Media Pool folder. Input is
        an array of file/folder paths. Returns a list of the MediaPoolItems created.

        Parameters
        ----------
        paths
            file or folder paths to be imported.

        Returns
        -------
        list[MediaPoolItem]
            Returns a list of MediaPoolItems created. After importing, a list of
            MediaPoolItems will be created.


        """
        ...