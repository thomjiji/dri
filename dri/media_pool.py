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
        The type of media for the clip. Optional. 1: Video only, 2: Audio only.
    trackIndex : int
        Indicates which track of the timeline the clip will be inserted into. Optional.
    recordFrame: int
        Indicates where in the timeline the clip will be inserted, in Frames. Optional.

    Notes
    -----
    trackIndex

    -   If there is only one video track in the timeline: V1, then if trackIndex is
        set to 2, which means the clip will be inserted into the timeline's video
        track 2, then the API will automatically add video track V2 and insert the
        clip into V2.

    -   However, the API does not work if the trackIndex is set to 3 or more when
        only one video track V1 exists. The clip will still be inserted into V1.

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

        Returns
        -------
        Folder
            Root Folder of Media Pool.

        """
        ...

    def AddSubFolder(self, folder: Folder, name: str) -> Folder:
        """
        Adds new subfolder under specified Folder object with the given name.

        Parameters
        ----------
        folder
            Folder to add subfolder under.
        name
            Name of the subfolder to add.

        Returns
        -------
        Folder
            Subfolder added under specified Folder object.

        """
        ...

    def RefreshFolders(self) -> bool:
        """
        Updates the folders in collaboration mode.

        Returns
        -------
        bool
            True if folders were updated, False otherwise.

        """
        ...

    def CreateEmptyTimeline(self, name: str) -> Timeline:
        """
        Adds new timeline with given name.

        Parameters
        ----------
        name
            Name of the timeline to add.

        Returns
        -------
        Timeline
            Timeline object added.

        """
        ...

    def AppendToTimeline(
        self, clip: MediaPoolItem, *clips: MediaPoolItem
    ) -> list[TimelineItem]:
        """
        Appends specified MediaPoolItem objects in the current timeline. Returns the
        list of appended timelineItems.

        Parameters
        ----------
        clip
            :class:`MediaPoolItem` to be appended. Required.
        *clips
            :class:`MediaPoolItem` to be appended.

        Returns
        -------
        list[TimelineItem]
            List of :class:`TimelineItem` appended.

        """
        ...

    def AppendToTimeline(
        self, clips: list[MediaPoolItem | ClipInfo | dict[str, MediaPoolItem | int]]
    ) -> list[TimelineItem]:
        """
        Notes
        -----
        -   If input is list of :class:`MediaPoolItem`:
            Appends specified :class:`MediaPoolItem` objects in the current timeline.
            Returns the list of appended timelineItems.

        -   If input is list of :class:`ClipInfos`:
            Appends list of clipInfos specified as dict of "mediaPoolItem", "startFrame"
            (int), "endFrame" (int), (optional) "mediaType" (int; 1 - Video only, 2 -
            Audio only), "trackIndex" (int) and "recordFrame" (int). Returns the list of
            appended timelineItems.

        Parameters
        ----------
        clips
            List of MediaPoolItems to be appended. It can be a list of multiple
            :class:`MediaPoolItem`, or a list of multiple :class:`ClipInfo` (which is a
            dict). The specific fields accepted by ClipInfo, please see
            :class:`ClipInfo`.

        Returns
        -------
        list[TimelineItem]
            List of :class:`TimelineItem` appended.

        """
        ...

    def CreateTimelineFromClips(
        self, timeline_name: str, clip: MediaPoolItem, *clips: MediaPoolItem
    ) -> Timeline:
        """
        Creates new timeline with specified name, and appends the specified
        MediaPoolItem objects.

        Parameters
        ----------
        timeline_name
            Name of the timeline to be created.
        clip
            MediaPoolItem to be appended.
        *clips
            MediaPoolItems to be appended.

        Returns
        -------
        Timeline
            :class:`Timeline` object created.

        """
        ...

    def CreateTimelineFromClips(
        self, timeline_name: str, clips: list[MediaPoolItem | ClipInfo]
    ) -> Timeline:
        """
        If input is list of :class:`MediaPoolItem`:
        Creates new timeline with specified name, and appends the specified
        MediaPoolItem objects.

        If input is list of :class:`ClipInfo`:
        Creates new timeline with specified name, appending the list of clipInfos
        specified as a dict of "mediaPoolItem", "startFrame" (int), "endFrame" (int),
        "recordFrame" (int).

        Notes
        -----
        -   :class:`ClipInfo` that CreateTimelineFromClips accept can't include
            "trackIndex", otherwise DaVinci Resolve will crash.

        Returns
        -------
        Timeline
            :class:`Timeline` object created.

        """
        ...

    def ImportTimelineFromFile(
        self, file_path: str, import_option: ImportOption | dict[str, str | list | bool]
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

        Returns
        -------
        Timeline
            :class:`Timeline` object created.

        """
        ...

    def DeleteTimelines(self, timeline: Timeline | list[Timeline]) -> bool:
        """
        Deletes specified timelines in the media pool.

        Parameters
        ----------
        timeline
            Timeline(s) to be deleted.

        Returns
        -------
        bool
            True if successful, false otherwise.

        """
        ...

    def GetCurrentFolder(self) -> Folder:
        """
        Returns currently selected Folder.

        Returns
        -------
        Folder
            :class:`Folder` object of currently selected folder.

        """
        ...

    def SetCurentFolder(self, folder: Folder) -> bool:
        """
        Sets current folder by given Folder

        Parameters
        ----------
        folder
            Folder to be set as the current folder.

        Returns
        -------
        bool
            True if successful, false otherwise.

        """
        ...

    def DeleteClips(self, clip: MediaPoolItem, *clips: MediaPoolItem) -> bool:
        """
        Deletes specified clips or timeline mattes in the media pool. It needs to
        accept as least one MediaPoolItem, or it will return False.

        Parameters
        ----------
        clip
            Clip to be deleted. Required.
        *clips
            Clips to be deleted. It can accept more than one MediaPoolItem.

        Returns
        -------
        bool
            True if successful, false otherwise.

        Examples
        --------
        >>> clip_1 = root_folder.GetClipList()[0]
        >>> clip_2 = root_folder.GetClipList()[1]
        >>> clip_3 = root_folder.GetClipList()[2]
        >>> clip_4 = root_folder.GetClipList()[3]
        >>> clip_5 = root_folder.GetClipList()[4]
        ...
        >>> media_pool.DeleteClips(clip_1, clip_2, clip_3, clip_4, clip_5)
        True

        """
        ...

    def DeleteClips(self, clips: list[MediaPoolItem]) -> bool:
        """
        Deletes specified clips or timeline mattes in the media pool.

        Parameters
        ----------
        clips
            Clips to be deleted.

        Returns
        -------
        bool
            True if successful, false otherwise.

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

        Returns
        -------
        bool
            True if successful, false otherwise.

        """
        ...

    def DeleteFolders(self, subfolder: Folder, *subfolders: Folder) -> bool:
        """
        Deletes specified subfolders in the media pool recursively.

        Parameters
        ----------
        subfolder
            Folder to be deleted. Required.
        *subfolders
            Subfolders to be deleted. Optional.

        Returns
        -------
        bool
            True if successful, false otherwise.

        """
        ...

    def DeleteFolders(self, subfolders: list[Folder]) -> bool:
        """
        Deletes specified subfolders in the media pool recursively.

        Parameters
        ----------
        subfolders
            Subfolders to be deleted.

        Returns
        -------
        bool
            True if successful, false otherwise.

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
            MediaPoolItem to get mattes for.

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

    # TODO: what fields does ClipInfo accept? I have no idea.
    def ImportMedia(
        self, paths: list[ClipInfo | dict[str, MediaPoolItem | int]]
    ) -> list[MediaPoolItem]:
        """
        Imports file path(s) into current Media Pool folder as specified in list of
        clipInfo dict. Returns a list of the MediaPoolItems created.

        Notes
        -----
        -   Each clipInfo gets imported as one :class:`MediaPoolItem` unless 'Show
            Individual Frames' is turned on.
        -   Example: ImportMedia([{"FilePath":"file_%03d.dpx", "StartIndex":1,
            "EndIndex":100}]) would import clip "file_[001-100].dpx".

        Parameters
        ----------
        paths

        Returns
        -------
        list[MediaPoolItem]
            A list of MediaPoolItems created after importing.

        """
        ...

    def ExportMetadata(self, file_name: str, clips: list[MediaPoolItem] = []) -> bool:
        """
        Exports metadata of specified clips to 'fileName' in CSV format. If no clips
        are specified, all clips from media pool will be used.

        Parameters
        ----------
        file_name
            The name of the metadata file to export. Adding or not adding csv suffix
            to it is fine.
        clips
            :class:`MediaPoolItem` to export metadata in media pool.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the media pool.

        Returns
        -------
        str
            Unique ID for the media pool.

        """
        ...