import importlib.util
import platform
from dataclasses import dataclass
from enum import Enum, IntEnum
from pathlib import Path
from types import ModuleType
from typing import Literal, Optional, TypedDict, Union


def load_dynamic_lib() -> Optional[ModuleType]:
    try:
        if platform.system() == "Windows":
            path = (
                "C:\\Program Files\\Blackmagic Design\\DaVinci "
                "Resolve\\fusionscript.dll"
            )
        elif platform.system() == "Darwin":
            path = (
                "/Applications/DaVinci Resolve/DaVinci "
                "Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
            )
        elif platform.system() == "Linux":
            path = "/opt/resolve/libs/Fusion/fusionscript.so"
        else:
            raise Exception("Unsupported platform")

        spec = importlib.util.spec_from_file_location("fusionscript", path)
        if spec is None:
            raise ImportError(f"Module not found at {path}")

        bmd_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bmd_module)

    except Exception as e:
        print(f"Failed to load module due to error: {e}")
        bmd_module = None

    return bmd_module


LiteralMarkerColor = Literal[
    "All",
    "Blue",
    "Cyan",
    "Green",
    "Yellow",
    "Red",
    "Pink",
    "Purple",
    "Fuchsia",
    "Rose",
    "Lavender",
    "Sky",
    "Mint",
    "Lemon",
    "Sand",
    "Cocoa",
    "Cream",
]


LiteralFlagColor = Literal[
    "All",
    "Blue",
    "Cyan",
    "Green",
    "Yellow",
    "Red",
    "Pink",
    "Purple",
    "Fuchsia",
    "Rose",
    "Lavender",
    "Sky",
    "Mint",
    "Lemon",
    "Sand",
    "Cocoa",
    "Cream",
]


LiteralClipColor = Literal[
    "Orange",
    "Apricot",
    "Yellow",
    "Lime",
    "Olive",
    "Green",
    "Teal",
    "Navy",
    "Blue",
    "Purple",
    "Violet",
    "Pink",
    "Tan",
    "Beige",
    "Brown",
    "Chocolate",
]


class KeyframeMode(IntEnum):
    """
    'keyframeMode' can be one of the following enums:
        - resolve.KEYFRAME_MODE_ALL     == 0
        - resolve.KEYFRAME_MODE_COLOR   == 1
        - resolve.KEYFRAME_MODE_SIZING  == 2

    Integer values returned by Resolve.GetKeyframeMode() will correspond to the enums
    above.
    """

    ALL = 0
    COLOR = 1
    SIZING = 2


class ExportType(Enum):
    EXPORT_LUT_17PTCUBE = "EXPORT_LUT_17PTCUBE"
    EXPORT_LUT_33PTCUBE = "EXPORT_LUT_33PTCUBE"
    EXPORT_LUT_65PTCUBE = "EXPORT_LUT_65PTCUBE"
    EXPORT_LUT_PANASONICVLUT = "EXPORT_LUT_PANASONICVLUT"


class CloudSync(Enum):
    CLOUD_SYNC_DEFAULT              = -1
    CLOUD_SYNC_DOWNLOAD_IN_QUEUE    = 0
    CLOUD_SYNC_DOWNLOAD_IN_PROGRESS = 1
    CLOUD_SYNC_DOWNLOAD_SUCCESS     = 2
    CLOUD_SYNC_DOWNLOAD_FAIL        = 3
    CLOUD_SYNC_DOWNLOAD_NOT_FOUND   = 4

    CLOUD_SYNC_UPLOAD_IN_QUEUE      = 5
    CLOUD_SYNC_UPLOAD_IN_PROGRESS   = 6
    CLOUD_SYNC_UPLOAD_SUCCESS       = 7
    CLOUD_SYNC_UPLOAD_FAIL          = 8
    CLOUD_SYNC_UPLOAD_NOT_FOUND     = 9
    CLOUD_SYNC_SUCCESS              = 10


class SyncMode(Enum):
    CLOUD_SYNC_NONE           = "CLOUD_SYNC_NONE"
    CLOUD_SYNC_PROXY_ONLY     = "CLOUD_SYNC_PROXY_ONLY"
    CLOUD_SYNC_PROXY_AND_ORIG = "CLOUD_SYNC_PROXY_AND_ORIG"


class RenderSetting(TypedDict):
    SelectAllFrames: bool
    MarkIn: int
    MarkOut: int
    TargetDir: str
    CustomName: str
    UniqueFilenameStyle: Literal[0, 1]  # 0 - Prefix, 1 - Suffix
    ExportVideo: bool
    ExportAudio: bool
    FormatWidth: int
    FormatHeight: int
    FrameRate: float  # Example: 23.976, 24

    # For SD resolution: "16_9" or "4_3", other resolution: "square" or "cinemascope"
    PixelAspectRatio: str

    # "VideoQuality" possible values for current codec (if applicable):
    #  -    0 (int) - will set quality to automatic
    #  -    [1 -> MAX] (int) - will set input bit rate
    #  -    ["Least", "Low", "Medium", "High", "Best"] (string) - will set input
    #       quality level
    VideoQuality: int | str

    AudioCodec: str  # Example: "aac"
    AudioBitDepth: int
    AudioSampleRate: int
    ColorSpaceTag: str  # Example: "Same as Project", "ACES (AP0)"
    GammaTag: str  # Example: "Same as Project", "ACEScct"
    ExportAlpha: bool
    EncodingProfile: str  # Example: "Main10". Can only be set for H.264 and H.265.
    MultiPassEncode: bool  # Can only be set for H.264.

    # 0 - Premultiplied, 1 - Straight. Can only be set for H.264 and H.265.
    AlphaMode: Literal[0, 1]

    NetworkOptimization: bool


@dataclass
class TimelineImportOption:
    """
    For :func:`ImportTimelineFromFile()` use.

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
    sourceClipsFolders: list["Folder"]
    interlaceProcessing: bool
    importSourceClips: bool = True


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

    mediaPoolItem: "MediaPoolItem"
    startFrame: int = 0
    endFrame: int = 0
    mediaType: Literal[1, 2] = 1  # 1 - Video only, 2 - Audio only
    recordFrame: int = 0
    trackIndex: int = 0


# TODO This Metadata class is incomplete
class Metadata(TypedDict):
    """
    For SetMetadata() and GetMetadata() use.

    """

    Description: str
    Comments: str
    Keywords: str
    People: str
    # ClipColor: ClipColor
    Shot: str
    Scene: str
    Take: str
    Angle: str
    Move: str

    # In order to access this field, use "Day / Night" instead of "Day_Night"
    Day_Night: str

    # In order to access this field, use "Good Take" instead of "Good_Take"
    Good_Take: Literal["true", "false"]


@dataclass
class ThumbnailData:
    width: int
    height: int
    format: str
    data: str


class ImportOption:
    """
    For :func:`ImportIntoTimeline` use.

    Attributes
    ----------
    autoImportSourceClipsIntoMediaPool
        Specifies if source clips should be imported into media pool, True by default.
    ignoreFileExtensionsWhenMatching
        Specifies if file extensions should be ignored when matching, False by default.
    linkToSourceCameraFiles
        Specifies if link to source camera files should be enabled, False by default.
    useSizingInfo
        Specifies if sizing information should be used, False by default.
    importMultiChannelAudioTracksAsLinkedGroups
        Specifies if multichannel audio tracks should be imported as linked groups,
        False by default
    insertAdditionalTracks
        Specifies if additional tracks should be inserted, True by default.
    insertWithOffset
        specifies insert with offset value in timecode format - defaults to
        "00:00:00:00", applicable if "insertAdditionalTracks" is False.
    sourceClipsPath
        specifies a filesystem path to search for source clips if the media is
        inaccessible in their original path and if "ignoreFileExtensionsWhenMatching"
        is True.
    sourceClipsFolder
        list of Media Pool folder objects to search for source clips if the media is not
        present in current folder.

    """

    autoImportSourceClipsIntoMediaPool: bool = True
    ignoreFileExtensionsWhenMatching: bool = False
    linkToSourceCameraFiles: bool = False
    useSizingInfo: bool = False
    importMultiChannelAudioTracksAsLinkedGroups: bool = False
    insertAdditionalTracks: bool = True
    insertWithOffset: str = "00:00:00:00"
    sourceClipsPath: str = ""
    sourceClipsFolder: str


class Resolve:
    # fmt: off
    EXPORT_AAF: str                  = "AAF"
    EXPORT_DRT: str                  = "DRT"
    EXPORT_EDL: str                  = "EDL"
    EXPORT_FCP_7_XML: str            = "FCP_7_XML"
    EXPORT_FCPXML_1_8: str           = "FCPXML_1_8"
    EXPORT_FCPXML_1_9: str           = "FCPXML_1_9"
    EXPORT_FCPXML_1_10: str          = "FCPXML_1_10"
    EXPORT_HDR_10_PROFILE_A: str     = "HDR_10_PROFILE_A"
    EXPORT_HDR_10_PROFILE_B: str     = "HDR_10_PROFILE_B"
    EXPORT_TEXT_CSV: str             = "TEXT_CSV"
    EXPORT_TEXT_TAB: str             = "TEXT_TAB"
    EXPORT_DOLBY_VISION_VER_2_9: str = "DOLBY_VISION_VER_2_9"
    EXPORT_DOLBY_VISION_VER_4_0: str = "DOLBY_VISION_VER_4_0"
    EXPORT_DOLBY_VISION_VER_5_1: str = "DOLBY_VISION_VER_5_1"
    EXPORT_OTIO: str                 = "OTIO"
    EXPORT_ALE: str                  = "ALE"
    EXPORT_CDL: str                  = "CDL"

    EXPORT_NONE: str                 = "NONE"
    EXPORT_AAF_NEW: str              = "AAF_NEW"
    EXPORT_AAF_EXISTING: str         = "AAF_EXISTING"
    EXPORT_CDL: str                  = "CDL"
    EXPORT_SDL: str                  = "SDL"
    EXPORT_MISSING_CLIPS: str        = "MISSING_CLIPS"

    KEYFRAME_MODE_ALL: int           = 1
    KEYFRAME_MODE_COLOR: int         = 2
    KEYFRAME_MODE_SIZING: int        = 3

    EXPORT_LUT_17PTCUBE: str         = "EXPORT_LUT_17PTCUBE"
    EXPORT_LUT_33PTCUBE: str         = "EXPORT_LUT_33PTCUBE"
    EXPORT_LUT_65PTCUBE: str         = "EXPORT_LUT_65PTCUBE"
    EXPORT_LUT_PANASONICVLUT: str    = "EXPORT_LUT_PANASONICVLUT"

    CLOUD_SYNC_DEFAULT: int               = -1
    CLOUD_SYNC_DOWNLOAD_IN_QUEUE: int     = 0
    CLOUD_SYNC_DOWNLOAD_IN_PROGRESS: int  = 1
    CLOUD_SYNC_DOWNLOAD_SUCCESS: int      = 2
    CLOUD_SYNC_DOWNLOAD_FAIL: int         = 3
    CLOUD_SYNC_DOWNLOAD_NOT_FOUND: int    = 4
    CLOUD_SYNC_UPLOAD_IN_QUEUE: int       = 5
    CLOUD_SYNC_UPLOAD_IN_PROGRESS: int    = 6
    CLOUD_SYNC_UPLOAD_SUCCESS: int        = 7
    CLOUD_SYNC_UPLOAD_FAIL: int           = 8
    CLOUD_SYNC_UPLOAD_NOT_FOUND: int      = 9
    CLOUD_SYNC_SUCCESS: int               = 10

    CLOUD_SYNC_NONE: str                  = "CLOUD_SYNC_NONE"
    CLOUD_SYNC_PROXY_ONLY: str            = "CLOUD_SYNC_PROXY_ONLY"
    CLOUD_SYNC_PROXY_AND_ORIG: str        = "CLOUD_SYNC_PROXY_AND_ORIG"

    CLOUD_SETTING_PROJECT_NAME: str       = ""
    CLOUD_SETTING_PROJECT_MEDIA_PATH: str = ""
    CLOUD_SETTING_IS_COLLAB: bool         = False
    CLOUD_SETTING_SYNC_MODE: SyncMode     = SyncMode.CLOUD_SYNC_PROXY_ONLY
    CLOUD_SETTING_IS_CAMERA_ACCESS: bool  = False
    # fmt: on

    @staticmethod
    def resolve_init() -> "Resolve":
        bmd_module = load_dynamic_lib()
        resolve = bmd_module.scriptapp("resolve")
        return resolve

    def Fusion(self):
        """
        Returns the Fusion object. Starting point for Fusion scripts.

        """
        ...

    def GetMediaStorage(self) -> "MediaStorage":
        """
        Returns the media storage object to query and act on media locations.

        Returns
        -------
        MediaStorage
            The media storage object to query and act on media locations.

        """
        ...

    def GetProjectManager(self) -> "ProjectManager":
        """
        Returns the project manager object for currently open database.

        Returns
        -------
        ProjectManager
            The project manager object for currently open database.

        """
        ...

    def OpenPage(self, page_name: str) -> bool:
        """
        Switches to indicated page in DaVinci Resolve. Input can be one of ("media",
        "cut", "edit", "fusion", "color", "fairlight", "deliver").

        Parameters
        ----------
        page_name
            The resolve page to switch to. Can be one of the "media", "cut", "edit",
            "fusion", "color", "fairlight", "deliver".

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetCurrentPage(self) -> str:
        """
        Returns the page currently displayed in the main window. Returned value can
        be one of ("media", "cut", "edit", "fusion", "color", "fairlight", "deliver",
        None).

        Returns
        -------
        str
            The page currently displayed in the main window.

        """
        ...

    def GetProductName(self) -> str:
        """
        Returns product name.

        Returns
        -------
        str
            The product name. Such as "DaVinci Resolve Studio".

        """
        ...

    def GetVersion(self) -> list[int | str]:
        """
        Returns list of product version fields in [major, minor, patch, build,
        suffix] format.

        Returns
        -------
        list[str]
            List of product version fields in [major, minor, patch, build,
            suffix] format. Such As [18, 5, 0, 16, 'b'].

        """
        ...

    def GetVersionString(self) -> str:
        """
        Returns product version in "major.minor.patch.build.suffix" format.

        Returns
        -------
        str
            Product version in "major.minor.patch.build.suffix" format.

        """
        ...

    def LoadLayoutPreset(self, preset_name: str) -> bool:
        """
        Loads UI layout from saved preset named "presetName".

        Parameters
        ----------
        preset_name
            The name of the preset to load.

        Returns
        -------
        bool
            True if load successful, False otherwise.

        """
        ...

    def UpdateLayoutPreset(self, preset_name: str) -> bool:
        """
        Overwrites preset named "presetName" with current UI layout.

        Parameters
        ----------
        preset_name
            The name of the preset to update.

        Returns
        -------
        bool
            True if update successful, False otherwise.

        """
        ...

    def ExportLayoutPreset(self, preset_name: str, preset_file_path: str) -> bool:
        """
        Exports preset named "presetName" to path "presetFilePath".

        Parameters
        ----------
        preset_name
            The name of the preset to export.
        preset_file_path
            The path to the preset file to export. For example:
            "/Users/thom/Desktop/my_preset". You should specify the name of the
            preset that you want to export in the preset_file_path argument.

        Returns
        -------
        bool
            True if export successful, False otherwise. If the file exists, it will
            also return True.

        """
        ...

    def DeleteLayoutPreset(self, preset_name: str) -> bool:
        """
        Deletes preset named "presetName".

        Parameters
        ----------
        preset_name
            The name of the preset to delete.

        Returns
        -------
        bool
            True if delete successful, False otherwise.

        """
        ...

    def SaveLayoutPreset(self, preset_name: str) -> bool:
        """
        Saves current UI layout as a preset named 'presetName'.

        Parameters
        ----------
        preset_name
            The name of the preset that will be saved.

        Returns
        -------
        bool
            True if save successful, False otherwise.

        """
        ...

    def ImportLayoutPreset(self, preset_file_path: str, preset_name: str) -> bool:
        """
        Imports preset from path 'presetFilePath'. The optional argument 'presetName'
        specifies how the preset shall be named. If not specified, the preset is
        named based on the filename.

        Parameters
        ----------
        preset_file_path
            The path to the preset file to import.
        preset_name
            The name of the preset to import. If not specified, the preset is named
            based on the filename.

        Returns
        -------
        bool
            True if import successful, False otherwise.

        """
        ...

    def Quit(self):
        """
        Quits the Resolve App.

        """
        ...

    def ImportRenderPreset(self, preset_path: str) -> bool:
        """
        Import a preset from presetPath (string) and set it as current preset for
        rendering.

        Parameters
        ----------
        preset_path
            The path to the preset file to import.

        Returns
        -------
        bool
            True if import successful, False otherwise.

        """
        ...

    def ExportRenderPreset(self, preset_name: str, export_path: str) -> bool:
        """
        Export a preset to a given path (string) if presetName(string) exists.

        Parameters
        ----------
        preset_name
            The name of the preset to import.
        export_path
            The export destination path.

        Returns
        -------
        bool
            True if import successful, False otherwise.

        """
        ...

    def ImportBurnInPreset(self, preset_path: str) -> bool:
        """
        Import a data burn in preset from a given presetPath (string).

        Parameters
        ----------
        preset_path
            The path to the preset file to import.

        Returns
        -------
        bool
            True if import successful, False otherwise.

        """
        ...

    def ExportBurnInPreset(self, preset_name: str, export_path: str) -> bool:
        """
        Export a data burn in preset to a given path (string) if presetName (string)
        exists.

        Parameters
        ----------
        preset_name
            The name of the preset to import.
        export_path
            The export destination path.

        Returns
        -------
        bool
            True if import successful, False otherwise.

        """
        ...

    def GetKeyframeMode(self) -> KeyframeMode:
        """
        Returns the currently set keyframe mode (int). Refer to section 'Keyframe Mode
        information' below for details.

        Notes
        -----
        It's located on Color page > Keyframes panel which next to Scopes.

        Returns
        -------
        KeyframeMode
            Three integers: 0, 1 or 2 correspond to All, Color and Sizing.

        """
        ...

    def SetKeyframeMode(self, keyframe_mode: KeyframeMode) -> bool:
        """
        Returns True when 'keyframeMode'(enum) is successfully set.

        Parameters
        ----------
        keyframe_mode
            Three integers: 0, 1 and 2 correspond to All, Color and Sizing.

        Returns
        -------
            True if successful, False otherwise.

        """
        ...


class ProjectManager:
    def ArchiveProject(
        self,
        project_name: str,
        file_path: str,
        is_archive_src_media: bool = True,
        is_archive_render_cache: bool = True,
        is_archive_proxy_media: bool = False,
    ) -> bool:
        """
        Archives project to provided file path with the configuration as provided by the
        optional arguments.

        Parameters
        ----------
        project_name
            Project name
        file_path
            Archive destination
        is_archive_src_media
            Defaults to True
        is_archive_render_cache
            Defaults to True
        is_archive_proxy_media
            Default to False

        Returns
        -------
        bool
            True if successful, False otherwise.

        Notes
        -----
        is_archive_src_media can't be set to False for no reason. It also can't be
        uncheck when using GUI > right click project > Export Project Archive.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project_manager.ArchiveProject(
        ...    "Daily work",
        ...    "/Users/thom/Downloads/Daily work",
        ...    is_archive_src_media=False,
        ...    is_archive_render_cache=False,
        ...    is_archive_proxy_media=False,
        ... )
        True

        """
        ...

    def CreateProject(self, project_name: str) -> Optional[bool]:
        """
        Creates and returns a project if projectName (string) is unique, and None if
        it is not.

        Parameters
        ----------
        project_name
            Project name.

        Returns
        -------
        Optional[bool]
            Project object if project is created, None otherwise.

        """
        ...

    def DeleteProject(self, project_name: str) -> bool:
        """
        Delete project in the current folder if not currently loaded.

        Parameters
        ----------
        project_name
            Project name.

        Returns
        -------
        bool
            True if delete successful, False otherwise.

        """
        ...

    def LoadProject(self, project_name: str) -> Optional["Project"]:
        """
        Loads and returns the project with name = projectName (string) if there is a
        match found, and None if there is no matching Project.

        Parameters
        ----------
        project_name
            Project name.

        Returns
        -------
        Optional[Project]
            Return a Project object if project is loaded, None otherwise.

        """
        ...

    def GetCurrentProject(self) -> "Project":
        """
        Returns the currently loaded Resolve project.

        Returns
        -------
        Project
            The currently loaded Resolve project.

        """
        ...

    def SaveProject(self) -> bool:
        """
        Saves the currently loaded project with its own name. Returns True if
        successful.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def CloseProject(self, project: "Project") -> bool:
        """
        Closes the specified project without saving.

        Parameters
        ----------
        project
            The Project object to close.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def CreateFolder(self, folder_name: str) -> bool:
        """
        Creates a folder if folderName (string) is unique. Return False if it's not.

        Parameters
        ----------
        folder_name
            Folder name.

        Returns
        -------
        bool
            True if successful, False otherwise (maybe folder with that name exists).

        """
        ...

    def DeleteFolder(self, folder_name: str) -> bool:
        """
        Deletes the specified folder if it exists. Returns True in case of success.

        Parameters
        ----------
        folder_name
            Folder name that's going to be deleted.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetProjectListInCurrentFolder(self) -> list[str]:
        """
        Returns a list of project names in current folder.

        Returns
        -------
        list[str]
            List of project names (string) in current folder.

        """
        ...

    def GetFolderListInCurrentFolder(self) -> list[str]:
        """
        Returns a list of folder names in current folder.

        Returns
        -------
        list[str]
            List of folder names (string) in current folder.

        """
        ...

    def GotoRootFolder(self) -> bool:
        """
        Opens root folder in database.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GotoParentFolder(self) -> bool:
        """
        Opens parent folder of current folder in database if current folder has parent.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetCurrentFolder(self) -> str:
        """
        Returns the current folder name.

        Returns
        -------
        str
            The current folder name.

        """
        ...

    def OpenFolder(self, folder_name: str) -> bool:
        """
        Opens folder under given name.

        Parameters
        ----------
        folder_name
            Folder name.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ImportProject(self, file_path: str, project_name: str = None) -> bool:
        """
        Imports a project from the file path provided with given project name,
        if any. Returns True if successful.

        Parameters
        ----------
        file_path
            File path to import project from. Must be an absolute path.
        project_name
            Project name of the project to be imported. If not specified,
            use project path name, such as "/Users/thom/Desktop/my_project.drp" -
            "my_project".

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ExportProject(
        self, project_name: str, file_path: str, with_stills_and_luts: bool = True
    ) -> bool:
        """
        Exports project to provided file path, including stills and LUTs if
        withStillsAndLUTs is True (enabled by default). Returns True in case of success.

        Parameters
        ----------
        project_name
            Project name of the project to be exported.
        file_path
            File path to export project to. Must be an absolute path. Must including the
            exported project name (without extension, Resolve will take care of
            that), see Examples below.
        with_stills_and_luts
            "Export Project with Stills and LUTs...", Defaults to True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project_manager.ExportProject("Daily work", "/Users/thom/Downloads/Daily work")
        True

        """
        ...

    def RestoreProject(self, file_path: str, project_name: str) -> bool:
        """
        Restores a project from the file path provided with given project name,
        if any. Returns True if successful.

        Parameters
        ----------
        file_path
        project_name

        Returns
        -------

        """
        ...

    def GetCurrentDatabase(self) -> dict[str, str]:
        """
        Returns a dictionary (with keys 'DbType', 'DbName' and optional 'IpAddress')
        corresponding to the current database connection.

        Returns
        -------
        dict[str, str]
            Dictionary with keys 'DbType', 'DbName' and optional 'IpAddress'.

        """
        ...

    def GetDatabaseList(self) -> list[dict[str, str]]:
        """
        Returns a list of dictionary items (with keys 'DbType', 'DbName' and optional
        'IpAddress') corresponding to all the databases added to Resolve.

        Returns
        -------
        list[dict[str, str]]
            List of dictionary items (with keys 'DbType', 'DbName' and optional
        'IpAddress').

        """
        ...

    def SetCurrentDatabase(self, db_info: dict) -> bool:
        """
        Switches current database connection to the database specified by the keys
        below, and closes any open project.

        -   'DbType': 'Disk' or 'PostgreSQL' (string)
        -   'DbName': database name (string)
        -   'IpAddress': IP address of the PostgreSQL server (string, optional key -
            defaults to '127.0.0.1')

        Parameters
        ----------
        db_info
            Database info as specified above.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def CreateCloudProject(self) -> "Project":
        """
        Creates and returns a cloud project.

        '{cloudSettings}': Check 'Cloud Projects Settings' subsection below for more
        information.
        """
        ...

    def ImportCloudProject(self, file_path: str, dict) -> bool:
        """
        Returns True if import cloud project is successful; False otherwise

        Parameters
        ----------
        file_path
            filePath of file to import.
        {cloudSettings}
            Check 'Cloud Projects Settings' subsection below for more information.

        """
        ...

    def restoreCloudProject(self, folder_path: str, dict) -> bool:
        """
        Returns True if restore cloud project is successful; False otherwise.

        Parameters
        ----------
        file_path
            filePath of file to restore.
        {cloudSettings}
            Check 'Cloud Projects Settings' subsection below for more information.

        """
        ...


class Project:
    def GetMediaPool(self) -> "MediaPool":
        """
        Returns the Media Pool object.

        Returns
        -------
        :class:`dri.MediaPool`
            The Media Pool object.

        """
        ...

    def GetTimelineCount(self) -> int:
        """
        Returns the number of timelines currently present in the project.

        Returns
        -------
        int
            The number of timelines currently present in the project.

        """
        ...

    def GetTimelineByIndex(self, idx: int) -> "Timeline":
        """
        Returns timeline at the give index, 1 <= idx <= project.GetTimelineCount().

        Parameters
        ----------
        idx
            The index of Timeline that's going to return.

        Returns
        -------
        :class:`dri.Timeline`
            The Timeline object at the give index.

        """
        ...

    def GetCurrentTimeline(self) -> "Timeline":
        """
        Returns the currently loaded timeline.

        Returns
        -------
        :class:`Timeline`
            The currently loaded timeline.

        """
        ...

    def SetCurrentTimeline(self, timeline: "Timeline") -> bool:
        """
        Sets given timeline as current timeline for the project. Returns True if
        successful.

        Parameters
        ----------
        timeline
            The Timeline object to set as current timeline.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetGallery(self) -> "Gallery":
        """
        Returns the Gallery object.

        Returns
        -------
        Gallery
            The Gallery object.

        """
        ...

    def GetName(self) -> str:
        """
        Returns the project name.

        Returns
        -------
        str
            The project name.

        """
        ...

    def SetName(self, project_name: str) -> bool:
        """
        Sets project name if given projectName (string) is unique.

        Parameters
        ----------
        project_name
            The project name to set.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetPresetList(self) -> list[dict[str, str]]:
        """
        Returns a list of presets and their information.

        Returns
        -------
        list[dict[str, str]]
            List of presets and their information.

        Examples
        --------
        >>> project.GetPresetList()
        [{'Name': 'Current Project', 'Width': 1920, 'Height': 1080},
         {'Name': 'System Config', 'Width': 1920, 'Height': 1080},
         {'Name': 'guest default config', 'Width': 1920, 'Height': 1080}]

        """
        ...

    def SetPreset(self, preset_name: str) -> bool:
        """
        Sets preset by given presetName (string) into project.

        Parameters
        ----------
        preset_name
            The preset name to set.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def AddRenderJob(self) -> str:
        """
        Adds a render job based on current render settings to the render queue.
        Returns a unique job id (string) for the new render job.

        Returns
        -------
        str
            Unique job id (string) for the new render job.

        Notes
        -----
        -   If there is no clip in current timeline, or you don't set render target
            directory, AddRenderJob will return '', which is False.
        -   If there is no timeline, AddRenderJob will return None.

        """
        ...

    def DeleteRenderJob(self, job_id: str) -> bool:
        """
        Deletes render job for input job id (string).

        Parameters
        ----------
        job_id
            Render job's ID (string)

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def DeleteAllRenderJobs(self) -> bool:
        """
        Deletes all render jobs in the queue.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetRenderJobList(self) -> list[dict[str, str | int | float | bool]]:
        """
        Returns a list of render jobs and their information.

        Returns
        -------
        list[dict[str | int | float]]
            List of render jobs and their information.

        """
        ...

    def GetRenderPresetList(self) -> list[str]:
        """
        Returns a list of render presets and their information.

        Returns
        -------
        list[str]
            List of render presets and their information.

        """
        ...

    def StartRendering(self, *job_ids: str, is_interactive_mode: bool = False) -> bool:
        """
        Starts rendering jobs indicated by the input job ids. If not specified, it will
        start all queued jobs one by one. The optional "isInteractiveMode", when set,
        enables error feedback in the UI during rendering.

        Parameters
        ----------
        job_ids
            Render job's ID (string). Can be empty.
        is_interactive_mode
            When set, enables error feedback in the UI during rendering.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def StartRendering(
        self, job_ids: list[str], is_interactive_mode: bool = False
    ) -> bool:
        """
        Starts rendering jobs indicated by the input job ids. The optional
        "isInteractiveMode", when set, enables error feedback in the UI during
        rendering.

        Parameters
        ----------
        job_ids
            A list of job ids to start rendering.
        is_interactive_mode
            When set, enables error feedback in the UI during rendering.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def StopRendering(self):
        """
        Stops any current render processes.

        """
        ...

    def IsRenderingInProgress(self) -> bool:
        """
        Returns True if rendering is in progress.

        Returns
        -------
        bool
            True if rendering is in progress, False otherwise.

        """
        ...

    def LoadRenderPreset(self, preset_name: str) -> bool:
        """
        Sets a preset as current preset for rendering if presetName (string) exists.

        Parameters
        ----------
        preset_name
            The preset name.

        Returns
        -------
        bool
            True if load successful, False otherwise.

        """
        ...

    def SaveAsNewRenderPreset(self, preset_name: str) -> bool:
        """
        Creates new render preset by given name if presetName (string) is unique.

        Parameters
        ----------
        preset_name
            The preset name.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def SetRenderSettings(
        self, settings: RenderSetting | dict[str, int | float | str | bool]
    ) -> bool:
        """
        Sets given settings for rendering. Settings is a dict, with support for the
        keys: Refer to "Looking up render settings" section for information for
        supported settings.

        Parameters
        ----------
        settings
            A dict with settings (specified in RenderSetting class).

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetRenderJobStatus(self, job_id: str) -> dict[str, str | int]:
        """
        Returns a dict with job status and completion percentage of the job by given
        jobId (string).

        Parameters
        ----------
        job_id
            Render job's ID (string).

        Returns
        -------
        dict[str, str | int]
            A dict with job status and completion percentage of the job by given
            jobId (string).

        """
        ...

    def GetSetting(self, setting_name: str = "") -> str | dict[str, str | float]:
        """
        Returns value of project setting (indicated by settingName, string). Check the
        section below for more information.

        Parameters
        ----------
        setting_name
            Project setting name. Could be None. If not specified, return all settings
            and their value (string).

        Returns
        -------
        str | dict[str, str | float]
            Value of project setting. If settingName is not specified, will return
            all settings and their value (string) which is a dict[str, str | float].
            "timelineFrameRate" could be of float, see example below.

        """
        ...

    def SetSetting(self, setting_name: str, setting_value: str) -> bool:
        """
        Sets the project setting (indicated by settingName, string) to the value (
        settingValue, string). Check the section below for more information.

        Parameters
        ----------
        setting_name
            Project setting name.
        setting_value
            Project setting value.

        Returns
        -------
        bool
            True if set successful, False otherwise.

        """
        ...

    def GetRenderFormats(self) -> dict[str, str]:
        """
        Returns a dict (format -> file extension) of available render formats.

        Returns
        -------
        dict
            A dict (format -> file extension) of available render formats.

        Examples
        --------
        >>> project.GetRenderFormats()
        {'AVI': 'avi',
         'BRAW': 'braw',
         'Cineon': 'cin',
         'DCP': 'dcp',
         'DPX': 'dpx',
         'EXR': 'exr',
         'GIF': 'gif',
         'HLS': 'm3u8',
         'IMF': 'imf',
         'JPEG 2000': 'j2c',
         'MJ2': 'mj2',
         'MKV': 'mkv',
         'MP4': 'mp4',
         'MTS': 'mts',
         'MXF OP-Atom': 'mxf',
         'MXF OP1A': 'mxf_op1a',
         'Panasonic AVC': 'pavc',
         'QuickTime': 'mov',
         'TIFF': 'tif',
         'Wave': 'wav'}

        """
        ...

    def GetRenderCodecs(self, render_format: str) -> dict[str, str]:
        """
        Returns a dict (codec description -> codec name) of available codecs for
        given render format (string).

        Parameters
        ----------
        render_format
            Render format (string). Such as "MP4", "mp4", "MKV", "mov",
            case-insensitive. Also note that you cannot use "QuickTime" to retrieve the
            codec, only "mov" in this case.

        Returns
        -------
        dict
            A dict (codec description -> codec name) of available codecs for
            given render format (string).

        """
        ...

    def GetCurrentRenderFormatAndCodec(self) -> dict[str, str]:
        """
        Returns a dict with currently selected format 'format' and render codec 'codec'.

        Returns
        -------
        dict[str, str]
            A dict with currently selected format and codec.

        Examples
        --------
        >>> project.GetCurrentRenderFormatAndCodec()
        {'format': 'mov', 'codec': 'H265'}

        """
        ...

    def SetCurrentRenderFormatAndCodec(self, render_format: str, codec: str) -> bool:
        """
        Sets given render format (string) and render codec (string) as options for
        rendering.

        Parameters
        ----------
        render_format
            Render format (string). Such as "mov", "mp4", "mkv". You can use
            *GetRenderFormats()* to retrieve all available formats. Note that you can
            only use the **file extension** ("mov", "mp4", not "QuickTime", "MP4") as
            arg passed to *SetCurrentRenderFormatAndCodec()*.
        codec
            Render codec (string). Such as "H265". You can use *GetRenderCodecs(
            render_format: str)* to retrieve all available codecs under the given
            render formats. Note that you can only use the **codec name** not the
            **codec description** as arg passed to *SetCurrentRenderFormatAndCodec()*.

        Returns
        -------
        bool
            True if set successful, False otherwise.

        """
        ...

    def GetCurrentRenderMode(self) -> int:
        """
        Returns the render mode: 0 - Individual clips, 1 - Single clip.

        Returns
        -------
        int
            Render mode (0 - Individual clips, 1 - Single clip).

        """
        ...

    def SetCurrentRenderMode(self, render_mode: int) -> bool:
        """
        Sets the render mode. Specify renderMode = 0 for Individual clips,
        1 for Single clip.

        Parameters
        ----------
        render_mode
            0 for Individual Clips, 1 for Single Clip.

        Returns
        -------
        bool
            True if set successful, False otherwise.

        """
        ...

    def GetRenderResolutions(
        self, render_format: str, codec: str
    ) -> list[dict[str, int]]:
        """
        Returns list of resolutions applicable for the given render format (string)
        and render codec (string). Returns full list of resolutions if no argument is
        provided. Each element in the list is a dictionary with 2 keys "Width" and
        "Height".

        Parameters
        ----------
        render_format
            Render format (string).
        codec
            Render codec (string).

        Returns
        -------
        list[dict[str, int]]
            List of resolutions applicable for the given render format (string)
            and render codec (string).

        """
        ...

    def RefreshLUTList(self) -> bool:
        """
        Refreshes LUT list.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the project item.

        Returns
        -------
        str
            A unique ID for the project item.

        """
        ...

    def InsertAudioToCurrentTrackAtPlayhead(
        self, media_path: str, start_offset_in_samples: int, duration_in_samples: int
    ) -> bool:
        """
        Inserts the media specified by mediaPath (string) with startOffsetInSamples (
        int) and durationInSamples (int) at the playhead on a selected track on the
        Fairlight page. Returns True if successful, otherwise False.

        Parameters
        ----------
        media_path
            Path to the media file (string) that's going to be inserted.
        start_offset_in_samples
            Start offset
        duration_in_samples
            Duration

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def LoadBurnInPreset(self, preset_name: str) -> bool:
        """
        Loads user defined data burn in preset for project when supplied presetName (
        string). Returns true if successful.

        Parameters
        ----------
        preset_name
            Burn-in preset name

        Returns
        -------
        bool
            True if load successful, False otherwise.

        """
        ...

    def ExportCurrentFrameAsStill(self, file_path: str) -> bool:
        """
        Exports current frame as still to supplied filePath. filePath must end in
        valid export file format. Returns True if successful, False otherwise.

        Parameters
        ----------
        file_path
            Still export destination.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Examples
        --------
        >>> project.ExportCurrentFrameAsStill("/Users/thom/Desktop/arriraw.jpg")
        True

        """
        ...

    def GetColorGroupsList(self) -> list["ColorGroup"]:
        """
        Returns a list of all group objects in the timeline.
        """
        ...

    def AddColorGroup(self, group_name: str) -> "ColorGroup":
        """
        Creates a new ColorGroup. groupName must be a unique string.
        """
        ...

    def DeleteColorGroup(self, color_group: "ColorGroup") -> bool:
        """
        Deletes the given color group and sets clips to ungrouped.
        """
        ...


class MediaStorage:
    def GetMountedVolumeList(self) -> list[str]:
        """
        Returns list of folder paths corresponding to mounted volumes displayed in
        Resolve’s Media Storage.

        Returns
        -------
        list[str]
            List of folder paths corresponding to mounted volumes displayed in
            Resolve’s Media Storage.

        """
        ...

    def GetSubFolderList(self, folder_path: str) -> list[str]:
        """
        Returns list of folder paths in the given absolute folder path.

        Parameters
        ----------
        folder_path
            The given absolute folder path, used to retrieve the subfolder paths list.

        Returns
        -------
        list[str]
            List of folder paths (absolute path) under the given absolute folder path.

        """
        ...

    def GetFileList(self, folder_path: str) -> list[str]:
        """
        Returns list of media and file listings in the given absolute folder path. Note
        that media listings may be logically consolidated entries.

        Parameters
        ----------
        folder_path
            The given absolute folder path, used to retrieve media list.

        Returns
        -------
        list[str]
            List of media and file listings in the given absolute folder path.

        """
        ...

    def RevealInStorage(self, path: str) -> bool:
        """
        Expands and displays given file/folder path in Resolve’s Media Storage.

        Parameters
        ----------
        path
            The given absolute file/folder path, used to reveal in Resolve’s Media
            Storage.

        Returns
        -------
        bool
            True if file/folder path was successfully revealed in Resolve’s Media
            Storage, False otherwise.

        """
        ...

    def AddItemListToMediaPool(
        self, item_path: str, *item_paths: str
    ) -> list["MediaPoolItem"]:
        """
        Adds specified file/folder paths from Media Storage into current Media Pool
        folder. Input is one or more file/folder paths. Returns a list of the
        MediaPoolItems created.

        Parameters
        ----------
        item_path
            The path of the first item to add.
        *item_paths
            The paths of additional items to add.

        Returns
        -------
        list[MediaPoolItem]
            List of MediaPoolItems created.

        """
        ...

    def AddItemListToMediaPool(self, item_paths: list[str]) -> list["MediaPoolItem"]:
        """
        Adds specified file/folder paths from Media Storage into current Media Pool
        folder. Input is an array of file/folder paths. Returns a list of the
        MediaPoolItems created.

        Parameters
        ----------
        item_paths
            The paths of items to add.

        Returns
        -------
        list[MediaPoolItem]
            List of MediaPoolItems created.

        """
        ...

    def AddItemListToMediaPool(
        self, item_info: list[dict[str, str | int]]
    ) -> list["MediaPoolItem"]:
        """
        Adds list of itemInfos specified as dict of "media" (string), "startFrame"
        (int), "endFrame" (int) from Media Storage into current Media Pool folder.
        Returns a list of the MediaPoolItems created.

        Parameters
        ----------
        item_info
            List of dicts of "media" (string), "startFrame" (int), "endFrame" (int)
            from Media Storage. The key of dict must be "media", "startFrame" and
            "endFrame". The last two can be emitted (optional).

        Returns
        -------
        list[MediaPoolItem]
            List of :class:`MediaPoolItem` created.

        Examples
        --------
        >>> item_1 = {
        ...     "media": "/Users/thom/Desktop/A010C0037_220622_005G.MOV",
        ...     "startFrame": 0,
        ...     "endFrame": 3182,
        ... }
        >>> item_2 = {
        ...     "media": "/Users/thom/Desktop/A010C0038_220622_005G.MOV",
        ...     # "startFrame": 1392,  # Can be emitted
        ...     # "endFrame": 3182,  # Can be emitted
        ... }
        >>> media_storage.AddItemListToMediaPool([item_1, item_2])
        [<BlackmagicFusion.PyRemoteObject at 0x1064d2ff0>,
         <BlackmagicFusion.PyRemoteObject at 0x1064d2690>]

        """
        ...

    def AddClipMattesToMediaPool(
        self,
        media_pool_item: "MediaPoolItem",
        paths: list[str],
        stereo_eye: Literal["left", "right"] = "",
    ) -> bool:
        """
        Adds specified media files as mattes for the specified MediaPoolItem.
        StereoEye is an optional argument for specifying which eye to add the matte
        to for stereo clips ("left" or "right"). Returns True if successful.

        Parameters
        ----------
        media_pool_item
            The MediaPoolItem to add the clips as mattes to.
        paths
            The paths of the media files to add as mattes.
        stereo_eye
            Specify which eye to add the matte to for stereo clips ("left" or "right").
            Defaults to "". It's optional.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def AddTimelineMattesToMediaPool(self, paths: list[str]) -> list["MediaPoolItem"]:
        """
        Adds specified media files as timeline mattes in current media pool folder.
        Returns a list of created MediaPoolItems.

        Parameters
        ----------
        paths
            The paths of the media files to add as timeline mattes.

        Returns
        -------
        list[MediaPoolItem]
            List of created :class:`MediaPoolItem`.

        """
        ...


class MediaPool:
    def GetRootFolder(self) -> "Folder":
        """
        Returns root Folder of Media Pool.

        Returns
        -------
        Folder
            Root Folder of Media Pool.

        """
        ...

    def AddSubFolder(self, folder: "Folder", name: str) -> "Folder":
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

    def CreateEmptyTimeline(self, name: str) -> "Timeline":
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
        self, clip: "MediaPoolItem", *clips: "MediaPoolItem"
    ) -> list["TimelineItem"]:
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
        self,
        clips: list[
            Union["MediaPoolItem", ClipInfo, dict[str, Union["MediaPoolItem", int]]]
        ],
    ) -> list["TimelineItem"]:
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
        self, timeline_name: str, clip: "MediaPoolItem", *clips: "MediaPoolItem"
    ) -> "Timeline":
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
        self, timeline_name: str, clips: list[Union["MediaPoolItem", "ClipInfo"]]
    ) -> "Timeline":
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
        self,
        file_path: str,
        import_option: TimelineImportOption | dict[str, str | list | bool],
    ) -> "Timeline":
        """
        Creates timeline based on parameters within given file
        (AAF/EDL/XML/FCPXML/DRT/ADL/OTIO) and optional importOptions dict, with support
        for the keys:

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

    def DeleteTimelines(self, timeline: Union["Timeline", list["Timeline"]]) -> bool:
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

    def GetCurrentFolder(self) -> "Folder":
        """
        Returns currently selected Folder.

        Returns
        -------
        Folder
            :class:`Folder` object of currently selected folder.

        """
        ...

    def SetCurrentFolder(self, folder: "Folder") -> bool:
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

    def DeleteClips(self, clip: "MediaPoolItem", *clips: "MediaPoolItem") -> bool:
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

    def DeleteClips(self, clips: list["MediaPoolItem"]) -> bool:
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

    def DeleteFolders(self, subfolder: "Folder", *subfolders: "Folder") -> bool:
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

    def DeleteFolders(self, subfolders: list["Folder"]) -> bool:
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

    def MoveClips(self, clips: list["MediaPoolItem"], target_folder: "Folder") -> bool:
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

    def MoveFolders(self, folders: list["Folder"], target_folder: "Folder") -> bool:
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

    def GetClipMatteList(self, media_pool_item: "MediaPoolItem") -> list[Path]:
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

    def GetTimelineMatteList(self, folder: "Folder") -> list["MediaPoolItem"]:
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
        self, media_pool_item: "MediaPoolItem", paths: list[str]
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

    def RelinkClips(self, clips: list["MediaPoolItem"], folder_path: str) -> bool:
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

    def UnlinkClips(self, clips: list["MediaPoolItem"]) -> bool:
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

    def ImportMedia(self, paths: list[str]) -> list["MediaPoolItem"]:
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
        self, paths: list[ClipInfo | dict[str, Union["MediaPoolItem", int]]]
    ) -> list["MediaPoolItem"]:
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

    def ExportMetadata(self, file_name: str, clips: list["MediaPoolItem"] = []) -> bool:
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

    def CreateStereoClip(
        self, left_media_pool_item: MediaPoolItem, right_media_pool_item: MediaPoolItem
    ) -> "MediaPoolItem":
        """
        Takes in two existing media pool items and creates a new 3D stereoscopic media
        pool entry replacing the input media in the media pool.
        """
        ...


class Folder:
    def GetClipList(self) -> list["MediaPoolItem"]:
        """
        Returns a list of clips (items) within the folder.

        Returns
        -------
        list[MediaPoolItem]
            A list of :class:`MediaPoolItem` within the folder.

        """
        ...

    def GetName(self) -> str:
        """
        Returns the media folder name.

        Returns
        -------
        str
            The media folder name.

        """
        ...

    def GetSubFolderList(self) -> list["Folder"]:
        """
        Returns a list of subfolders in the folder.

        Returns
        -------
        list[Folder]
            A list of :class:`Folder` within the current folder.

        """
        ...

    def GetIsFolderStale(self) -> bool:
        """
        Return true if folder is stale in collaboration mode, false otherwise.

        Returns
        -------
        bool
            True if folder is stale in collaboration mode, false otherwise.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the media pool folder.

        Returns
        -------
        str
            A unique ID for the media pool folder.

        """
        ...

    def Export(self, file_path: str) -> bool:
        """
        Returns true if export of DRB folder to filePath is successful, false otherwise

        Parameters
        ----------
        file_path
            The export file destination.

        Returns
        -------
        bool
            True if export is successful, false otherwise.

        """
        ...


class MediaPoolItem:
    def GetName(self) -> str:
        """
        Returns the clip name.

        Returns
        -------
        str
            Clip name.

        """
        ...

    def GetMetadata(self, metadata_type: str = None) -> str | Metadata:
        """
        Returns the metadata value for the key "metadataType". If no argument is
        specified, a dict of all set metadata properties is returned.

        Parameters
        ----------
        metadata_type
            Metadata type to get.

        Returns
        -------
        str | Metadata
            Metadata value for the key "metadataType".

        Notes
        -----
        -   You can access all the items in DaVinci Resolve Metadata tab through this
            API, except for "Clip Color" (see "GetClipColor()"), "Flags" (see
            "AddFlag(color)") and items that cannot be modified in the UI.

        """
        ...

    def SetMetadata(self, metadata_type: str, metadata_value: str) -> bool:
        """
        Sets the given metadata to metadataValue (string). Returns True if successfully.

        Parameters
        ----------
        metadata_type
            Metadata type to set.
        metadata_value
            Metadata value to set.

        Returns
        -------
        bool
            True if successful.

        Notes
        -----
        -   You can set all the items in DaVinci Resolve Metadata tab through this
            API, except for "Clip Color" (see :func:`dri.media_pool_item.GetClipColor`),
            "Flags" (see :func:`dri.media_pool_item.AddFlag`) and items that cannot be
            modified in the UI.

        """
        ...

    def SetMetadata(self, metadata: Metadata | dict[str, str]) -> bool:
        """
        Sets the item metadata with specified "metadata" dict. Returns True if
        successful.

        Parameters
        ----------
        metadata
            Metadata to set.

        Returns
        -------
        bool
            True if successful.

        Notes
        -----
        -   You can set all the items in DaVinci Resolve Metadata tab through this
            API, except for "Clip Color" (see :func:`dri.media_pool_item.GetClipColor`),
            "Flags" (see :func:`dri.media_pool_item.AddFlag`) and items that cannot be
            modified in the UI.

        """
        ...

    def GetMediaId(self) -> bool:
        """
        Returns the unique ID for the MediaPoolItem.

        Returns
        -------
        str
            Unique ID for the MediaPoolItem.

        """
        ...

    def AddMarker(
        self,
        frame_id: int,
        color: LiteralMarkerColor,
        name: str,
        note: Optional[str],
        duration: int,
        custom_data: Optional[str],
    ) -> bool:
        """
        Creates a new marker at given frameId position and with given marker
        information. "customData" is optional and helps to attach user specific data to
        the marker.

        Parameters
        ----------
        frame_id
            Frame number. Which is "Source Frame" located in the UI.
        color
            Marker color.
        name
            Marker name.
        note
            Marker note. Optional.
        duration
            Marker duration.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible in
            the UI. Optional.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Notes
        -----
        -   :func:`dri.timeline.AddMarker` only accepts positional arguments like in the
            example below. If you pass keyword arguments (kwarg=value) to it, it will
            always return False.
        -   The parameters `note` and `custom_data` are optional, which means: when
            calling this function, you should at least give it a null value `""` instead
            of omitting this parameter completely.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for i in current_timeline.GetItemListInTrack("video", 1):
        >>>     i.AddMarker(20, "Blue", "name", "", 1, "")

        """
        ...

    def GetMarkers(self) -> dict[int, dict[str, str | int]]:
        """
        Returns a dict of all markers and dicts with their information.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.

        Examples
        --------
        In the below example, there is one "Green" marker at offset 96 (position of the
        marker):

        >>> from resolve_init import GetResolve
        >>> resolve = GetResolve()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> for clip in root_folder.GetClipList():
        ...     print(clip.GetMarkers())
        {96: {'color': 'Green', 'duration': 1, 'note': '', 'name': 'Marker 1',
        'customData': ''}, ...}

        """
        ...

    def GetMarkerByCustomData(self, custom_data: str) -> dict[str, int]:
        """
        Returns marker {information} for the first matching marker with specified
        customData.

        Parameters
        ----------
        custom_data
            Custom data to search for.

        Returns
        -------
        dict[str, int]
            Marker information for the first matching marker with specified customData.

        Examples
        --------
        >>> from resolve_init import GetResolve
        >>> resolve = GetResolve()
        >>> project_manager.py = resolve.GetProjectManager()
        >>> project = project_manager.py.GetCurrentProject()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> for clip in root_folder.GetClipList():
        ...     print(clip.GetMarkerByCustomData("Hi"))
        {'color': 'Sky',
         'duration': 1,
         'note': '',
         'name': 'Marker 5',
         'customData': 'Hi'}

        """
        ...

    def UpdateMarkerCustomData(self, frame_id: int, custom_data: str) -> bool:
        """
        Updates the customData (string) for the marker at given frameId position.

        Parameters
        ----------
        frame_id
            Frame number. On the Resolve UI it's called "Source Frame".
        custom_data
            Custom data to update.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetMarkerCustomData(self, frame_id: int) -> str:
        """
        Returns customData string for the marker at given frameId position.

        Parameters
        ----------
        frame_id
            Frame number. On the Resolve UI it's called "Source Frame".

        Returns
        -------
        str
            Custom data string for the marker at given frameId position.

        """
        ...

    def DeleteMarkersByColor(self, color: LiteralMarkerColor) -> bool:
        """
        Delete all markers of the specified color from the media pool item. **"All"** as
        argument deletes all markers.

        Parameters
        ----------
        color
            Marker color.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def DeleteMarkerAtFrame(self, frame_num: int) -> bool:
        """
        Delete marker at frame number from the media pool item.

        Parameters
        ----------
        frame_num
            Frame number. On the Resolve UI it's called "Source Frame".

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def DeleteMarkerByCustomData(self, custom_data: str) -> bool:
        """
        Delete first matching marker with specified customData.

        Parameters
        ----------
        custom_data
            Custom data to search for.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def AddFlag(self, color: LiteralFlagColor) -> bool:
        """
        Adds a flag with given color (string).

        Parameters
        ----------
        color
            Flag color.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetFlagList(self) -> list[LiteralFlagColor]:
        """
        Returns a list of flag colors assigned to the item.

        Returns
        -------
        list[LiteralFlagColor | str]
            List of flag colors assigned to the item.

        """
        ...

    def ClearFlags(self, color: LiteralFlagColor) -> bool:
        """
        Clears the flag of the given color if one exists. An "All" argument is supported
        and clears all flags.

        Parameters
        ----------
        color
            Flag color.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetClipColor(self) -> LiteralClipColor:
        """
        Returns the item color as a string.

        Returns
        -------
        LiteralClipColor | str
            Return Clip color as a string.

        """
        ...

    def SetClipColor(self, color_name: LiteralClipColor) -> bool:
        """
        Sets the item color based on the colorName (string).

        Parameters
        ----------
        color_name
            Clip color name.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ClearClipColor(self) -> bool:
        """
        Clear the item color.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetClipProperty(self, property_name: str = None) -> str | dict[str, str]:
        """
        Returns the property value for the key "propertyName". If no argument is
        specified, a dict of all clip properties is returned. Check the section below
        for more information.

        Parameters
        ----------
        property_name
            Property name.

        Returns
        -------
        str | dict[str, str]
            Return property value or dict of properties.

        Examples
        --------
        >>> from resolve_init import GetResolve
        >>> resolve = GetResolve()
        >>> project_manager.py = resolve.GetProjectManager()
        >>> project = project_manager.py.GetCurrentProject()
        >>> media_pool = project.GetMediaPool
        >>> root_folder = media_pool.GetRootFolder()
        >>> root_folder.GetClipList()[0].GetClipProperty()
         {'Alpha mode': 'None',
          'Angle': '',
          'Audio Bit Depth': '32',
          'Audio Ch': '1',
          'Audio Codec': 'AAC',
          'Audio Offset': '',
          'Bit Depth': '8',
          'Camera #': '',
          'Clip Color': 'Teal',
          'Clip Name': 'video.mov',
          'Comments': '',
          'Data Level': 'Auto',
          'Date Added': 'Fri May 19 2023 19:37:03',
          'Date Created': 'Sat Nov 5 2022 20:16:20',
          'Date Modified': 'Sat Nov 5 20:16:44 2022',
          'Description': '',
          'Drop frame': '0',
          'Duration': '00:00:24:05',
          'Enable Deinterlacing': '0',
          'End': '1204',
          'End TC': '00:00:24:05',
          'FPS': 50.0,
          'Field Dominance': 'Auto',
          'File Name': 'video.mov',
          'File Path': '/Users/resolve/Desktop/video.mov',
          'Flags': '',
          'Format': 'QuickTime',
          'Frames': '1205',
          'Good Take': '',
          'H-FLIP': 'Off',
          'IDT': '',
          'In': '',
          'Input Color Space': 'Rec.709-A',
          'Input LUT': '',
          'Input Sizing Preset': 'None',
          'Keyword': '',
          'Noise Reduction': '',
          'Offline Reference': '',
          'Online Status': 'Online',
          'Out': '',
          'PAR': 'Square',
          'Proxy': 'None',
          'Proxy Media Path': '',
          'Reel Name': '',
          'Resolution': '1920x1080',
          'Roll/Card': '',
          'S3D Sync': '',
          'Sample Rate': '48000',
          'Scene': '',
          'Sharpness': '',
          'Shot': '',
          'Slate TC': '00:00:00:00',
          'Start': '0',
          'Start KeyKode': '',
          'Start TC': '00:00:00:00',
          'SuperScale Noise Reduction': '0.5',
          'SuperScale Sharpness': '0.5',
          'Synced Audio': '',
          'Take': '',
          'Type': 'Video + Audio',
          'Usage': '2',
          'V-FLIP': 'Off',
          'Video Codec': 'H.264 Main L5.1',
          'Super Scale': 1}

        """
        ...

    def SetClipProperty(self, property_name: str, property_value: str) -> bool:
        """
        Sets the given property to propertyValue (string). Check the section below
        for more information.

        Parameters
        ----------
        property_name
            Property name.
        property_value
            Property value.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def LinkProxyMedia(self, proxy_media_file_path: str) -> bool:
        """
        Links proxy media located at path specified by arg "proxyMediaFilePath" with
        the current clip. "proxyMediaFilePath" should be absolute clip path.

        Parameters
        ----------
        proxy_media_file_path
            Path to proxy media file.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Notes
        -----
        -   Proxy files must have identical timecode to the source file.
        -   Proxy files must have the same file name as the source file (excluding
            extensions).
        -   Proxy files must have the same frame rate as the source file.
        -   The format and codec used for proxy files must be supported in DaVinci
            Resolve.

        """
        ...

    def UnlinkProxyMedia(self) -> bool:
        """
        Unlinks any proxy media associated with clip.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ReplaceClip(self, file_path: str) -> bool:
        """
        Replaces the underlying asset and metadata of MediaPoolItem with the
        specified absolute clip path.

        Parameters
        ----------
        file_path
            Absolute clip path.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the media pool item.

        Returns
        -------
        str
            Unique ID.

        """
        ...

    def TranscribeAudio(self) -> bool:
        """
        Transcribes audio of the MediaPoolItem. Returns True if successful; False
        otherwise.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ClearTranscription(self) -> bool:
        """
        Clears audio transcription of the MediaPoolItem. Returns True if successful;
        False otherwise.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetAudioMapping(self) -> dict:
        """
        Returns a string with MediaPoolItem's audio mapping information. Check 'Audio
        Mapping' section below for more information.

        Returns
        -------
        dict
            json formatted string.

        """
        ...


class Timeline:
    def GetName(self) -> str:
        """
        Returns the timeline name.

        Returns
        -------
        str
            Timeline name

        """
        ...

    def SetName(self, timeline_name) -> bool:
        """
        Sets the timeline name if timelineName (string) is unique. Returns True if
        successful.

        Parameters
        ----------
        timeline_name
            Timeline name to set

        Returns
        -------
        bool
            True if the timeline name was set successfully, False otherwise.

        """
        ...

    def GetStartFrame(self) -> int:
        """
        Returns the frame number at the start of timeline.

        Returns
        -------
        int
            Frame number at the start of timeline

        """
        ...

    def GetEndFrame(self) -> int:
        """
        Returns the frame number at the end of timeline.

        Returns
        -------
        int
            Frame number at the end of timeline

        """
        ...

    def SetStartTimecode(self, timecode: str) -> bool:
        """
        Set the start timecode of the timeline to the string 'timecode'. Returns true
        when the change is successful, false otherwise.

        Parameters
        ----------
        timecode
            Start timecode of the timeline, such as "01:00:00:00".

        Returns
        -------
        bool
            True if the change was successful, False otherwise.

        Examples
        --------
        >>> current_timeline.SetStartTimecode("00:00:00:00")
        True

        """
        ...

    def GetStartTimecode(self) -> str:
        """
        Returns the start timecode for the timeline.

        Returns
        -------
        str
            Start timecode for the timeline

        Examples
        --------
        >>> current_timeline.GetStartTimecode()
        '01:00:00:00'

        """
        ...

    def GetTrackCount(self, track_type: str) -> int:
        """
        Returns the number of tracks for the given track type ("audio", "video" or
        "subtitle").

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle")

        Returns
        -------
        int
            Number of tracks for the given track type

        """
        ...

    def AddTrack(self, track_type: str, sub_track_type: str = "") -> bool:
        """
        Adds track of trackType ("video", "subtitle", "audio"). Optional argument
        subTrackType is used for "audio" trackType.

        subTrackType can be one of {"mono", "stereo", "5.1", "5.1film",
        "7.1", "7.1film", "adaptive1", ... , "adaptive24"}.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle")
        sub_track_type
            Sub track type ("audio", "video" or "subtitle"). Optional. Can be one of
            "mono", "stereo", "5.1", "5.1film", "7.1", "7.1film", "adaptive1",
            "adaptive2", "adaptive3", ..., "adaptive24".

        Returns
        -------
        bool
            True if the track was added successfully, False otherwise.

        Examples
        -------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> current_timeline.AddTrack("audio", "7.1")
        True

        """
        ...

    def AddTrack(
        self, track_type: str, new_track_options: dict[str, str | int]
    ) -> bool:
        """
        Adds track of trackType ("video", "subtitle", "audio"). Optional newTrackOptions
        = {'audioType': same as subTrackType above, 'index': 1 <= index <=
        GetTrackCount(trackType)}

        'audiotype' defaults to 'mono' if arg skipped and
        track type is ‘audio’.

        'index' if skipped (or if value not in bounds) appends
        track.

        Returns
        -------
        bool
            True if the track was added successfully, False otherwise.

        Examples
        -------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> new_track_option = {'audioType': "5.1", 'index': 3}
        >>> current_timeline.AddTrack("audio", new_track_option)
        True

        """
        ...

    def DeleteTrack(self, track_type: str, track_index: int) -> bool:
        """
        Deletes track of trackType ("video", "subtitle", "audio") and given
        trackIndex. 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track was deleted successfully, False otherwise.

        """
        ...

    def GetTrackSubType(self, track_type: str, track_index: str) -> str:
        """
        Returns an audio track's format. The return value is one of {"mono", "stereo",
        "5.1", "5.1film", "7.1", "7.1film", "adaptive1", ... , "adaptive24"} and matches
        the parameters 'subTrackType' and 'audioType' in timeline.AddTrack.

        Returns a blank string for non audio tracks.
        """
        ...

    def SetTrackEnable(self, track_type: str, track_index: int, enabled: bool) -> bool:
        """
        Enables/Disables track with given trackType and trackIndex.

        trackType is one of {"audio", "video", "subtitle"}.

        trackIndex is in this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).
        enabled

        Returns
        -------
        bool
            True if the track was enabled/disabled successfully, False otherwise.

        """
        ...

    def GetIsTrackEnabled(self, track_type: str, track_index: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is enabled and False
        otherwise.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track is enabled, False otherwise.

        """
        ...

    def SetTrackLock(self, track_type: str, track_index: int, locked: bool) -> bool:
        """
        Locks/Unlocks track with given trackType and trackIndex.

        trackType is one of {"audio", "video", "subtitle"}.

        trackIndex is in this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).
        locked
            Track locked or not.

        Returns
        -------
        bool
            True if the track was locked/locked successfully, False otherwise.

        """
        ...

    def GetIsTrackLocked(self, track_type: str, track_index: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is locked and False
        otherwise.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track is locked, False otherwise.

        """
        ...

    def DeleteClips(
        self,
        clips: list["TimelineItem"],
        ripple_delete: bool = False,
    ) -> bool:
        """
        Deletes specified TimelineItems from the timeline, performing ripple delete
        if the second argument is True. Second argument is optional (The default for
        this is False).

        Parameters
        ----------
        clips
            TimelineItems to delete. Can be
        ripple_delete
            True if the second argument is True.

        Returns
        -------
        bool
            True if the clips were deleted successfully, False otherwise.

        Notes
        -----
        -   If clip have audio, then DeleteClips will only delete the video (which is
            :class:`TimelineItem`), leaving the audio in the timeline.

        """
        ...

    def SetClipsLinked(self, clips: list["TimelineItem"], linked: bool) -> bool:
        """
        Links or unlinks the specified TimelineItems depending on second argument.

        Parameters
        ----------
        clips
            TimelineItems to link/unlink.
        linked
            Link or not.

        Returns
        -------
        bool
            True if the clips were linked/unlinked successfully, False otherwise.

        """
        ...

    def GetItemListInTrack(
        self, track_type: str, track_index: int
    ) -> list["TimelineItem"]:
        """
        Returns a list of timeline items on that track (based on trackType and
        trackIndex). 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        list[TimelineItem]
            Returns a list of TimelineItem on that track.

        """
        ...

    def AddMarker(
        self,
        frame_id: int,
        color: LiteralMarkerColor,
        name: str,
        note: Optional[str],
        duration: int,
        custom_data: Optional[str],
    ) -> bool:
        """
        Creates a new marker at given frameId position and with given marker
        information. 'customData' is optional and helps to attach user specific data to
        the marker.

        Parameters
        ----------
        frame_id
            Frame id of the marker. Frame id = Record Frame -
            :func:`dri.timeline.GetStartFrame`.
        color
            Marker color.
        name
            Marker name.
        note
            Marker note. Optional.
        duration
            Marker duration.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible in
            the UI. Optional.

        Returns
        -------
        bool
            True if the marker was created successfully.

        Notes
        -----
        -   frameId is not source frame, but a Record Frame minus the first frame of the
            current timeline (you can get it through :func:`dri.timeline.GetStartFrame`)
            — 01:00:00:00 on 24 fps timeline: 86400, on 25 fps timeline: 90000).
        -   For instance, consider a marker positioned at record frame 86607 in a 24 fps
            timeline, where the initial frame is 86400. To calculate the frameId for
            this marker, subtract the first frame from its record frame: 86607 - 86400,
            resulting in a frameId of 207.
        -   :func:`dri.timeline.AddMarker` only accepts positional arguments like in the
            example below. If you pass keyword arguments (kwarg=value) to it, it will
            always return False.
        -   The parameters `note` and `custom_data` are optional, which means: when
            calling this function, you should at least give it a null value `""` instead
            of omitting this parameter completely.
        -   If there is already a marker at the position of frameId, it will return
            False.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> current_timeline.AddMarker(171, "Blue", "name", "note", 1, "custom_data")
        True

        """
        ...

    def GetMarkers(self) -> dict[int, dict[str, str | int]]:
        """
        Returns a dict (frameId -> {information}) of all markers and dicts with their
        information.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.

        """
        ...

    def GetMarkerByCustomData(
        self, custom_data: str
    ) -> dict[int, dict[str, str | int]]:
        """
        Returns marker {information} for the first matching marker with specified
        customData.

        Parameters
        ----------
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.


        """
        ...

    def UpdateMarkerCustomData(self, frame_id: int, custom_data: str) -> bool:
        """
        Updates customData (string) for the marker at given frameId position.
        CustomData is not exposed via UI and is useful for scripting developer to
        attach any user specific data to markers.

        Parameters
        ----------
        frame_id
            Frame id of the marker.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        bool
            True if the marker was updated successfully.

        """
        ...

    def GetMarkerCustomData(self, frame_id: int) -> str:
        """
        Returns customData string for the marker at given frameId position.

        Parameters
        ----------
        frame_id
            Frame id of the marker.

        Returns
        -------
        str
            Custom data string.

        """
        ...

    def DeleteMarkersByColor(self, color: LiteralMarkerColor) -> bool:
        """
        Deletes all timeline markers of the specified color. An "All" argument is
        supported and deletes all timeline markers.

        Parameters
        ----------
        color
            Marker color, passing "All" to it will delete all timeline markers.

        Returns
        -------
        bool
            True if the markers were deleted successfully.

        """
        ...

    def DeleteMarkerAtFrame(self, frame_number: int) -> bool:
        """
        Delete marker at frame number from the media pool item.

        Parameters
        ----------
        frame_number
            Frame id, which is Frame id = Record Frame -
            :func:`dri.timeline.GetStartFrame`.

        Returns
        -------
        bool
            True if the marker was deleted successfully.

        """
        ...

    def DeleteMarkerByCustomData(self, custom_data: str) -> bool:
        """
        Delete first matching marker with specified customData.

        Parameters
        ----------
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        bool
            True if the marker was deleted successfully.

        """
        ...

    def ApplyGradeFromDRX(
        self,
        path: str,
        grade_mode: Literal[0, 1, 2],
        item: "TimelineItem",
        *items: "TimelineItem",
    ) -> bool:
        """
        Loads a still from given file path (string) and applies grade to Timeline
        Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode
        aligned", 2 - "Start Frames aligned".

        Parameters
        ----------
        path
            Path to still file.
        grade_mode
            0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames
            aligned".
        item
            :class:`TimelineItem` to apply grade to.

        Other Parameters
        ----------
        *items
            List of :class:`TimelineItem` to apply grade to.

        Returns
        -------
        bool
            True if the grade was applied successfully.

        """
        ...

    def ApplyGradeFromDRX(
        self, path: str, grade_mode: Literal[0, 1, 2], items: list["TimelineItem"]
    ) -> bool:
        """
        Loads a still from given file path (string) and applies grade to Timeline
        Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode
        aligned", 2 - "Start Frames aligned".

        Parameters
        ----------
        path
            Path to still file.
        grade_mode
            0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames
            aligned".
        items
            List of :class:`TimelineItem` to apply grade to.

        Returns
        -------
        bool
            True if the grade was applied successfully.

        """
        ...

    def GetCurrentTimecode(self) -> str:
        """
        Returns a string timecode representation for the current playhead position,
        while on Cut, Edit, Color, Fairlight and Deliver pages.

        Returns
        -------
        str
            Timecode in format "HH:MM:SS:FF".

        """
        ...

    def SetCurrentTimecode(self, timecode: str) -> bool:
        """
        Sets current playhead position from input timecode for Cut, Edit, Color,
        Fairlight and Deliver pages.

        Parameters
        ----------
        timecode
            Playhead position in the timeline to set.

        Returns
        -------
        bool
            True if the timecode was set successfully.

        """
        ...

    def GetCurrentVideoItem(self) -> "TimelineItem":
        """
        Returns the current video timeline item.

        Returns
        -------
        TimelineItem
            The current video timeline item.

        """
        ...

    def GetCurrentClipThumbnailImage(self) -> ThumbnailData | dict[str, int | str]:
        """
        Returns a dict (keys "width", "height", "format" and "data") with data
        containing raw thumbnail image data (RGB 8-bit image data encoded in base64
        format) for current media in the Color Page.

        An example of how to retrieve and interpret thumbnails is provided in
        6_get_current_media_thumbnail.py in the Examples folder.

        Returns
        -------
        ThumbnailData | dict
            Dict with raw thumbnail data for current media in the Color Page.

        """
        ...

    def GetTrackName(self, track_type: str, track_index: int) -> str:
        """
        Returns the track name for track indicated by trackType ("audio", "video" or
        "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        str
            Track name.

        """
        ...

    def SetTrackName(self, track_type: str, track_index: int) -> bool:
        """
        Sets the track name (string) for track indicated by trackType ("audio",
        "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track name was set successfully.

        """
        ...

    def DuplicateTimeline(self, new_timeline_name: str) -> "Timeline":
        """
        Duplicates the timeline and returns the created timeline, with the (optional)
        timelineName, on success.

        Parameters
        ----------
        new_timeline_name
            Name of the new timeline. If not specified, the new timeline name will
            append a "copy" to its suffix.

        Returns
        -------
        :class:`Timeline`
            The new timeline after duplication.

        """
        ...

    def CreateCompoundClip(
        self, timeline_items: list["TimelineItem"], clip_info: dict[str, str] = None
    ) -> "TimelineItem":
        """
        Creates a compound clip of input timeline items with an optional clipInfo
        map: {"startTimecode" : "00:00:00:00", "name" : "Compound Clip 1"}. It
        returns the created timeline item.

        Parameters
        ----------
        timeline_items
            List of timeline items to be composed.
        clip_info
            Optional clipInfo.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def CreateFusionClip(self, timeline_items: list["TimelineItem"]) -> "TimelineItem":
        """
        Creates a Fusion clip of input timeline items. It returns the created timeline
        item.

        Parameters
        ----------
        timeline_items
            List of timeline items to be composed.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def ImportIntoTimeline(
        self, file_path: str, import_option: ImportOption | dict
    ) -> bool:
        """
        Imports timeline items from an AAF file and optional importOptions dict into
        the timeline, with support for the keys:

        -   "autoImportSourceClipsIntoMediaPool": Bool, specifies if source clips
            should be imported into media pool, True by default

        -   "ignoreFileExtensionsWhenMatching": Bool, specifies if file extensions
            should be ignored when matching, False by default

        -   "linkToSourceCameraFiles": Bool, specifies if link to source camera files
            should be enabled, False by default

        -   "useSizingInfo": Bool, specifies if sizing information should be used,
            False by default

        -   "importMultiChannelAudioTracksAsLinkedGroups": Bool, specifies if
            multichannel audio tracks should be imported as linked groups, False by
            default

        -   "insertAdditionalTracks": Bool, specifies if additional tracks should be
            inserted, True by default

        -   "insertWithOffset": string, specifies insert with offset value in timecode
            format - defaults to "00:00:00:00", applicable if "insertAdditionalTracks"
            is False

        -   "sourceClipsPath": string, specifies a filesystem path to search for source
            clips if the media is inaccessible in their original path and if
            "ignoreFileExtensionsWhenMatching" is True

        -   "sourceClipsFolders": string, list of Media Pool folder objects to search
            for source clips if the media is not present in current folder

        Returns
        -------
        bool
            True if the timeline was imported successfully.

        """
        ...

    def Export(self, file_path: str, export_type: str, export_subtype: str) -> bool:
        """
        Exports timeline to 'fileName' as per input exportType & exportSubtype
        format. Refer to section "Looking up timeline export properties" for
        information on the parameters.

        Parameters
        ----------
        file_path
            Exported timeline destination. Should include file name and extension.
            Such as "/Users/thom/Desktop/export_timeline.aaf".
        export_type
            Export type, refer to the :class:`Resolve` for more information.
        export_subtype
            Export subtype, refer to the :class:`Resolve` for more information.

        Returns
        -------
        bool
            True if the timeline was exported successfully.

        # TODO: Does these notes can be expressed using Python's data structure?
        Notes
        -----
        -   Please note that :param:`exportSubType` is a required parameter for
            :py:data:`resolve.EXPORT_AAF` and :py:data:`resolve.EXPORT_EDL`. For rest
            of the :param:`exportType`, :param:`exportSubType` is ignored.

        -   When exportType is resolve.EXPORT_AAF, valid exportSubtype values are
            resolve.EXPORT_AAF_NEW and resolve.EXPORT_AAF_EXISTING.

        -   When exportType is resolve.EXPORT_EDL, valid exportSubtype values are
            resolve.EXPORT_CDL, resolve.EXPORT_SDL, resolve.EXPORT_MISSING_CLIPS and
            resolve.EXPORT_NONE.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> current_timeline = project.GetCurrentTimeline()
        >>> current_timeline.Export(
        ...     "'/Users/thom/Desktop/timeline.aaf', resolve.EXPORT_AAF, "
        ...     "resolve.EXPORT_AAF_NEW"
        ... )
        True

        """
        ...

    def GetSetting(self, setting_name: str = "") -> str | dict[str, str | float]:
        """
        Returns value of timeline setting (indicated by settingName : string). Check
        the section below for more information.

        Parameters
        ----------
        setting_name
            Timeline setting name. Could be None. If not specified, return all settings
            and their value (string).

        Returns
        -------
        str | dict[str, str | float]
            Value of timeline setting. If settingName is not specified, will return
            all settings and their value (string) which is a dict[str, str | float].

        """
        ...

    def SetSetting(self, setting_name: str, setting_value: str) -> bool:
        """
        Sets timeline setting (indicated by settingName : string) to the value (
        settingValue : string). Check the section below for more information.

        Parameters
        ----------
        setting_name
            Timeline setting name.
        setting_value
            Timeline setting name.

        Returns
        -------
        bool
            True if the setting was set successfully.

        """
        ...

    # TODO: Why some of the generator can't be inserted? It returns None.
    def InsertGeneratorIntoTimeline(self, generator_name: str) -> "TimelineItem":
        """
        Inserts a generator (indicated by generatorName : string) into the timeline.

        Parameters
        ----------
        generator_name
            Generator name. What's generator? In the Edit page > Effects > Toolbox >
            Generators.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        Notes
        -----
        -   Not work for "BT.2111 Color Bar HLG Narrow", "BT.2111 Color Bar PQ Full",
            "BT.2111 Color Bar PQ Narrow".

        """
        ...

    # TODO: Not work for all Fusion Generators
    def InsertFusionGeneratorIntoTimeline(self, generator_name: str) -> "TimelineItem":
        """
        Inserts a Fusion generator (indicated by generatorName : string) into the
        timeline.

        Parameters
        ----------
        generator_name
            Fusion Generator. What's generator? In the Edit page > Effects > Toolbox >
            Generators.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        Notes
        -----
        -   For all Fusion generator, it has no effect. I have no idea.

        """
        ...

    def InsertFusionCompositionIntoTimeline(self) -> "TimelineItem":
        """
        Inserts a Fusion composition into the timeline.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def InsertOFXGeneratorIntoTimeline(self, generator_name: str) -> "TimelineItem":
        """
        Inserts an OFX generator (indicated by generatorName : string) into the
        timeline.

        Parameters
        ----------
        generator_name
            OFX generator.

        Returns
        -------
        :class:`TimelineItem`
            Timeline item created.

        """
        ...

    def InsertTitleIntoTimeline(self, title_name: str) -> "TimelineItem":
        """
        Inserts a title (indicated by titleName : string) into the timeline.

        Parameters
        ----------
        title_name
            Title name.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def InsertFusionTitleIntoTimeline(self, title_name: str) -> "TimelineItem":
        """
        Inserts a Fusion title (indicated by titleName : string) into the timeline.

        Parameters
        ----------
        title_name
            Fusion title.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def GrabStill(self) -> "GalleryStill":
        """
        Grabs still from the current video clip. Returns a GalleryStill object.

        Returns
        -------
        :class:`GalleryStill`
            The created :class:`GalleryStill` object.

        """
        ...

    def GrabAllStills(self, still_frame_source: Literal[1, 2]) -> list["GalleryStill"]:
        """
        Grabs stills from all the clips of the timeline at 'stillFrameSource' (1 -
        First frame, 2 - Middle frame). Returns the list of GalleryStill objects.

        Parameters
        ----------
        still_frame_source
            Choose grab still from first frame (1) or middle frame (2).

        Returns
        -------
        list[GalleryStill]
            The created :class:`GalleryStill` object.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the timeline.

        Returns
        -------
        str
            Unique ID for the timeline.

        """
        ...

    def CreateSubtitlesFromAudio(self, auto_caption_settings: Optional[dict]) -> bool:
        """
        Creates subtitles from audio for the timeline. Takes in optional dictionary
        {autoCaptionSettings}. Check 'Auto Caption Settings' subsection below for more
        information.

        Returns
        -------
        bool
            True if subtitles were created successfully.

        """
        ...

    def DetectSceneCuts(self) -> bool:
        """
        Detects and makes scene cuts along the timeline. Returns True if successful,
        False otherwise.

        Returns
        -------
        bool
            True if scene cuts were detected successfully.

        """
        ...

    def ConvertTimelineToStereo() -> bool:
        """
        Converts timeline to stereo. Returns True if successful; False otherwise.
        """
        ...

    def GetNodeGraph(self) -> "Graph":
        """
        Returns the timeline's node graph object.

        """
        ...

    def AnalyzeDolbyVision(
        self, timeline_item: list["TimelineItem"] = [], analysis_type=None
    ) -> bool:
        """
        Analyzes Dolby Vision on clips present on the timeline. Returns True if analysis
        start is successful; False otherwise. if [timelineItems] is empty, analysis
        performed on all items. Else, analysis performed on [timelineItems] only. set
        analysisType to resolve.DLB_BLEND_SHOTS for blend setting.

        """
        ...


class TimelineItem:
    def GetName(self) -> str:
        """
        Returns the item name.

        Returns
        -------
        str
            The timeline item name.

        """
        ...

    def GetDuration(self) -> int:
        """
        Returns the item duration.

        Returns
        -------
        int
            The timeline item duration.

        """
        ...

    def GetEnd(self) -> int:
        """
        Returns the end frame position on the timeline.

        Returns
        -------
        int
            The end frame position of that timeline item on the timeline.
        """
        ...

    def GetFusionCompCount(self) -> int:
        """
        Returns number of Fusion compositions associated with the timeline item.

        Returns
        -------
        int
            Number of Fusion compositions associated with the timeline item.

        """
        ...

    def GetFusionCompByIndex(self, comp_index: int) -> "FusionComp":
        """
        Returns the Fusion composition object based on given index. 1 <= compIndex <=
        timelineItem.GetFusionCompCount()

        Parameters
        ----------
        comp_index
            Index of the Fusion composition.

        Returns
        -------
        FusionComp
            The Fusion composition object.

        """
        ...

    def GetFusionCompNameList(self) -> list[str]:
        """
        Returns a list of Fusion composition names associated with the timeline item.

        Returns
        -------
        list[str]
            List of Fusion composition names associated with the timeline item.

        """
        ...

    def GetFusionCompByName(self, comp_name: str) -> "FusionComp":
        """
        Returns the Fusion composition object based on given name.

        Parameters
        ----------
        comp_name
            Name of the Fusion composition.

        Returns
        -------
        FusionComp
            The Fusion composition object.

        """
        ...

    def GetLeftOffset(self) -> int:
        """
        Returns the maximum extension by frame for clip from left side.

        Returns
        -------
        int
            Maximum extension by frame for clip from left side.

        """
        ...

    def GetRightOffset(self) -> int:
        """
        Returns the maximum extension by frame for clip from right side.

        Returns
        -------
        int
            Maximum extension by frame for clip from right side.

        """
        ...

    def GetStart(self) -> int:
        """
        Returns the start frame position on the timeline.

        Returns
        -------
        int
            The start frame position of that timeline item on the timeline.

        """
        ...

    def SetProperty(self, property_key: str, property_value: str) -> bool:
        """
        Sets the value of property "propertyKey" to value "propertyValue"

        Refer to "Looking up Timeline item properties" for more information.

        Parameters
        ----------
        property_key
        property_value

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetProperty(
        self, property_key: str
    ) -> int | list[dict[str, float | bool | int]]:
        """
        Returns the value of the specified key. If no key is specified, the method
        returns a dictionary (python) or table (lua) for all supported keys.

        Parameters
        ----------
        property_key

        Returns
        -------
        int | list[dict[str, float | bool | int]]
            The value of the specified key. If no key is specified, the method returns
            a dictionary (python) or table (lua) for all supported keys.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for timeline_item in current_timeline.GetItemListInTrack("video", 1):
        ...     print(timeline_item.GetProperty())
        ...     break
        {'AnchorPointX': 0.0,
         'AnchorPointY': 0.0,
         'CompositeMode': 0,
         'CropBottom': 0.0,
         'CropLeft': 0.0,
         'CropRetain': False,
         'CropRight': 0.0,
         'CropSoftness': 0.0,
         'CropTop': 0.0,
         'Distortion': 0.0,
         'DynamicZoomEase': 0,
         'FlipX': False,
         'FlipY': False,
         'MotionEstimation': 0,
         'Opacity': 100.0,
         'Pan': 0.0,
         'Pitch': 0.0,
         'ResizeFilter': 0,
         'RetimeProcess': 0,
         'RotationAngle': 0.0,
         'Scaling': 0,
         'Tilt': 0.0,
         'Yaw': 0.0,
         'ZoomGang': True,
         'ZoomX': 1.0,
         'ZoomY': 1.0}

        """
        ...

    def AddMarker(
        self,
        frame_id: int,
        color: LiteralMarkerColor,
        name: str,
        note: Optional[str],
        duration: int,
        custom_data: Optional[str],
    ) -> bool:
        """
        Creates a new marker at given frameId position and with given marker
        information. 'customData' is optional and helps to attach user specific data to
        the marker.

        Parameters
        ----------
        frame_id
            Frame number. Which is "Source Frame" located in the UI.
        color
            Marker color.
        name
            Marker name.
        note
            Marker note. Optional.
        duration
            Marker duration.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible in
            the UI. Optional.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Notes
        -----
        -   :func:`dri.timeline.AddMarker` only accepts positional arguments like in the
            example below. If you pass keyword arguments (kwarg=value) to it, it will
            always return False.
        -   The parameters `note` and `custom_data` are optional, which means: when
            calling this function, you should at least give it a null value `""` instead
            of omitting this parameter completely.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for i in current_timeline.GetItemListInTrack("video", 1):
        >>>     i.AddMarker(20, "Blue", "name", "", 1, "")

        """
        ...

    def GetMarkers(self) -> dict[int, dict[str, str | int]]:
        """
        Returns a dict (frameId -> {information}) of all markers and dicts with their
        information.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.
        """
        ...

    def GetMarkerByCustomData(self, custom_data: str) -> dict[str, int]:
        """
        Returns marker {information} for the first matching marker with specified
        customData.

        Parameters
        ----------
        custom_data

        Returns
        -------
        dict[str, int]
            Dict of all markers and dicts with their information.

        """
        ...

    def UpdateMarkerCustomData(self, frame_id: int, custom_data: str) -> bool:
        """
        Updates customData (string) for the marker at given frameId position.
        CustomData is not exposed via UI and is useful for scripting developer to
        attach any user specific data to markers.

        Parameters
        ----------
        frame_id
        custom_data

        Returns
        -------

        """
        ...

    def GetMarkerCustomData(self, frame_id: int) -> str:
        """
        Returns customData string for the marker at given frameId position.

        Parameters
        ----------
        frame_id
            Frame number. On the Resolve UI it's called "Source Frame".

        Returns
        -------
        str
            CustomData string.

        """
        ...

    def DeleteMarkersByColor(self, color: LiteralMarkerColor) -> bool:
        """
        Delete all markers of the specified color from the timeline item. "All" as
        argument deletes all color markers.

        Parameters
        ----------
        color
            Marker color

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def DeleteMarkerAtFrame(self, frame_num: int) -> bool:
        """
        Delete marker at frame number from the timeline item.

        Parameters
        ----------
        frame_num
            Frame number. On the Resolve UI it's called "Source Frame".

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def DeleteMarkerByCustomData(self, custom_data: str) -> bool:
        """
        Delete first matching marker with specified customData.

        Parameters
        ----------
        custom_data
            Custom data to search for.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def AddFlag(self, color: LiteralFlagColor) -> bool:
        """
        Adds a flag with given color (string).

        Parameters
        ----------
        color
            Flag color.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetFlagList(self) -> list[LiteralFlagColor]:
        """
        Returns a list of flag colors assigned to the item.

        Returns
        -------
        list[LiteralFlagColor]
            List of flag colors assigned to the item.

        """
        ...

    def ClearFlags(self, color: LiteralFlagColor) -> bool:
        """
        Clear flags of the specified color. An "All" argument is supported to clear
        all flags.

        Parameters
        ----------
        color
            Flag color.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetClipColor(self) -> str:
        """
        Returns the item color as a string.

        Returns
        -------
        str
            Timeline item color.

        """
        ...

    def SetClipColor(self, color_name: LiteralClipColor) -> bool:
        """
        Sets the item color based on the colorName (string).

        Parameters
        ----------
        color_name
            Clip color name.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ClearClipColor(self) -> bool:
        """
        Clears the item color.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def AddFusionComp(self) -> "FusionComp":
        """
        Adds a new Fusion composition associated with the timeline item.

        Returns
        -------
        FusionComp
            Fusion composition.

        """
        ...

    def ImportFusionComp(self, path: str) -> "FusionComp":
        """
        Imports a Fusion composition from given file path by creating and adding a
        new composition for the item.

        Parameters
        ----------
        path
            Path to the Fusion composition.

        Returns
        -------
        FusionComp
            Fusion composition created after importing.

        """
        ...

    def ExportFusionComp(self, path: list, comp_index: int) -> bool:
        """
        Exports the Fusion composition based on given index to the path provided.

        Parameters
        ----------
        path
            Path to the Fusion composition exporting destination.
        comp_index
            Index of the Fusion composition to export.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def DeleteFusionCompByName(self, comp_name: str) -> bool:
        """
        Deletes the named Fusion composition.


        Parameters
        ----------
        comp_name
            Name of the Fusion composition.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def LoadFusionCompByName(self, comp_name: str) -> "FusionComp":
        """
        Loads the named Fusion composition as the active composition.

        Parameters
        ----------
        comp_name
            Name of the Fusion composition.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def RenameFusionCompByName(self, old_name: str, new_name: str) -> bool:
        """
        Renames the Fusion composition identified by oldName.

        Parameters
        ----------
        old_name
        new_name

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def AddVersion(self, version_name: str, version_type: int) -> bool:
        """
        Add a new color version for a video clip based on versionType (0 - local, 1 -
        remote).

        Parameters
        ----------
        version_name
            Any str you want to name the color version.
        version_type
            0 for local version, 1 for remote version.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetCurrentVersion(self) -> dict:
        """
        Return the current version of the video clip. The returned value will have the
        keys versionName and versionType (0 - local, 1 - remote).

        Returns
        -------
        dict

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for i in current_timeline.GetItemListInTrack("video", 1):
        ...     print(i.GetCurrentVersion())
        {'versionName': 'Version 1', 'versionType': 0}
        {'versionName': 'Version 1', 'versionType': 0}

        """
        ...

    def DeleteVersionByName(self, version_name: str, version_type: int) -> bool:
        """
        Deletes a color version by name and versionType (0 - local, 1 - remote).

        Parameters
        ----------
        version_name
            Any str you want to name the color version.
        version_type
            0 for local version, 1 for remote version.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def LoadVersionByName(self, version_name: str, version_type: int) -> bool:
        """
        Loads a named color version as the active version. versionType: 0 - local,
        1 - remote.

        Parameters
        ----------
        version_name
            Any str you want to name the color version.
        version_type
            0 for local version, 1 for remote version.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def RenameVersionByName(
        self, old_name: str, new_name: str, version_type: int
    ) -> bool:
        """
        Renames the color version identified by oldName and versionType (0 - local,
        1 - remote).

        Parameters
        ----------
        old_name
        new_name
        version_type
            0 for local version, 1 for remote version.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetVersionNameList(self, version_type: int) -> list[str]:
        """
        Returns a list of all color versions for the given versionType (0 - local, 1 -
        remote).

        Parameters
        ----------
        version_type
            0 for local version, 1 for remote version.

        Returns
        -------
        list
            A list contains all the version names.

        """
        ...

    def GetMediaPoolItem(self) -> MediaPoolItem:
        """
        Returns the media pool item corresponding to the timeline item if one exists.

        Returns
        -------
        MediaPoolItem

        """
        ...

    def GetStereoConvergenceValues(self) -> dict:
        """
        Returns a dict (offset -> value) of keyframe offsets and respective convergence
        values.

        Returns
        -------
        dict

        """
        ...

    def GetStereoLeftFloatingWindowParams(self) -> dict:
        """
        For the LEFT eye -> returns a dict (offset -> dict) of keyframe offsets and
        respective floating window params. Value at particular offset includes the left,
        right, top and bottom floating window values.

        Returns
        -------
        dict

        """
        ...

    def GetStereoRightFloatingWindowParams(self) -> dict:
        """
        For the RIGHT eye -> returns a dict (offset -> dict) of keyframe offsets and
        respective floating window params. Value at particular offset includes the left,
        right, top and bottom floating window values.

        Returns
        -------
        dict

        """
        ...

    def ApplyArriCdlLut(self) -> bool:
        """
        Applies ARRI CDL and LUT. Returns True if successful, False otherwise.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def SetCDL(self, CDL_map: dict) -> bool:
        """
        Keys of map are: "NodeIndex", "Slope", "Offset", "Power", "Saturation", where 1
        <= NodeIndex <= total number of nodes. Example python code - SetCDL({"NodeIndex"
        : "1", "Slope" : "0.5 0.4 0.2", "Offset" : "0.4 0.3 0.2", "Power" : "0.6 0.7
        0.8", "Saturation" : "0.65"})

        Parameters
        ----------
        CDL_map
            A dict with keys "NodeIndex", "Slope", "Offset", "Power", and "Saturation".

        Returns
        -------
        bool
            True if successful, False otherwise.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for i in current_timeline.GetItemListInTrack("video", 1):
        ...     print(
        ...         i.SetCDL(
        ...             {
        ...                 "NodeIndex": "1",
        ...                 "Slope": "0.5 0.4 0.2",
        ...                 "Offset": "0.4 0.3 0.2",
        ...                 "Power": "0.6 0.7 0.8",
        ...                 "Saturation": "0.65",
        ...             }
        ...         )
        ...     )
        True

        """
        ...

    def AddTake(
        self,
        media_pool_item: MediaPoolItem,
        start_frame: Optional[int] = None,
        end_frame: Optional[int] = None,
    ) -> bool:
        """
        Adds mediaPoolItem as a new take. Initializes a take selector for the timeline
        item if needed. By default, the full clip extents is added. startFrame (int) and
        endFrame (int) are optional arguments used to specify the extents.

        Parameters
        ----------
        media_pool_item
        start_frame
            Start frame
        end_frame
            End frame

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetSelectedTakeIndex(self) -> int:
        """
        Returns the index of the currently selected take, or 0 if the clip is not a take
        selector.

        Returns
        -------
        int
            The index of the currently selected take. 0 if current
            :class:`dri.TimelineItem` is not a take selector.

        Notes
        -----
        -   "take selector" is in Edit page > Timeline > right click any clip in
            timeline, and then your will see "Take Selector" in the menu.

        """
        ...

    def GetTakesCount(self) -> int:
        """
        Returns the number of takes in take selector, or 0 if the clip is not a take
        selector.

        Returns
        -------
        int
            The number of takes in take selector.

        Notes
        -----
        -   "take selector" is in Edit page > Timeline > right click any clip in
            timeline, and then your will see "Take Selector" in the menu.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for i in current_timeline.GetItemListInTrack("video", 1):
        ...     print(i.GetTakesCount())
        3

        """
        ...

    def GetTakeByIndex(self, idx: int) -> dict:
        """
        Returns a dict (keys "startFrame", "endFrame" and "mediaPoolItem") with take
        info for specified index.

        Parameters
        ----------
        idx
            Take index.

        Returns
        -------
        dict
            A dict with keys "startFrame", "endFrame", and "mediaPoolitem".

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for i in current_timeline.GetItemListInTrack("video", 1):
        >>>     print(i.GetTakeByIndex(1))
        {'mediaPoolItem': <BlackmagicFusion.PyRemoteObject object at 0x10677acf0>,
        'startFrame': 0, 'endFrame': 415}

        """
        ...

    def DeleteTakeByIndex(self, idx: int) -> bool:
        """
        Deletes a take by index, 1 <= idx <= number of takes.

        Parameters
        ----------
        idx
            Take index.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def SelectTakeByIndex(self, idx: int) -> bool:
        """
        Selects a take by index, 1 <= idx <= number of takes.

        Parameters
        ----------
        idx
            Take index.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def FinalizeTake(self) -> bool:
        """
        Finalizes take selection.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def CopyGrades(self, target_timemline_items: list["TimelineItem"]) -> bool:
        """
        Copies the current node stack layer grade to the same layer for each
        item in tgtTimelineItems. Returns True if successful.

        Parameters
        ----------
        target_timeline_items
            Target :class:`dri.TimelineItems` list.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def SetClipEnabled(self, enabled: bool) -> bool:
        """
        Sets clip enabled based on argument.

        Parameters
        ----------
        enabled
            Clip enable or disable.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetClipEnabled(self) -> bool:
        """
        Gets clip enabled status.

        Returns
        -------
        bool
            True if clip is already enabled, False otherwise.

        """
        ...

    def UpdateSidecar(self) -> bool:
        """
        Updates sidecar file for BRAW clips or RMD file for R3D clips.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the timeline item

        Returns
        -------
        str
            Unique ID for the timeline item.
        """
        ...

    def LoadBurnInPreset(self, preset_name: str) -> bool:
        """
        Loads user defined data burn in preset for clip when supplied presetName
        (string). Returns true if successful.

        Parameters
        ----------
        preset_name
            User defined data burn-in preset name.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def CreateMagicMask(self, mode: Literal["F", "B", "BI"]) -> bool:
        """
        Returns True if magic mask was created successfully, False otherwise. mode can
        "F" (forward), "B" (backward), or "BI" (bidirection).

        Parameters
        ----------
        mode
            Can be "F" (forward), "B" (backward), or "BI" (bidirection).

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def RegenerateMagicMask(self) -> bool:
        """
        Returns True if magic mask was regenerated successfully, False otherwise.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def Stabilize(self) -> bool:
        """
        Returns True if stabilization was successful, False otherwise

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def SmartReframe(self) -> bool:
        """
        Performs Smart Reframe. Returns True if successful, False otherwise.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetNodeGraph(self, layer_index: int = 1) -> "Graph":
        """
        Returns the clip's node graph object at layerIdx (int, optional). Returns the
        first layer if layerIdx is skipped. 1 <= layerIdx <=
        project.GetSetting("nodeStackLayers").

        Parameters
        ----------
        layer_index
            Defaults to 1 as it's at less 1 layer in the node graph - The clip level
            node graph (There is also Timeline level node graph). Maximum is 4. 1 <=
            layerIdx <= project.GetSetting("nodeStackLayers").

        """
        ...

    def GetColorGroup(self):
        """
        Returns the clip's color group if one exists.
        """
        ...

    def AssignToColorGroup(self, color_group) -> bool:
        """
        Returns True if TiItem to successfully assigned to given ColorGroup. ColorGroup
        must be an existing group in the current project.
        """
        ...

    def RemoveFromColorGroup(self) -> bool:
        """
        Returns True if the TiItem is successfully removed from the ColorGroup it is in.
        """
        ...

    def ExportLUT(self, export_type, path: str) -> bool:
        """
        Exports LUTs from tiItem referring to value passed in 'exportType' (enum) for
        LUT size. Refer to. 'ExportLUT notes' section for possible values.

        Saves generated LUT in the provided 'path' (string). 'path' should include the
        intended file name.

        If an empty or incorrect extension is provided, the appropriate extension
        (.cube/.vlt) will be appended at the end of the path.

        Examples
        -------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> media_storage = resolve.GetMediaStorage()
        >>> media_pool = project.GetMediaPool()
        >>> root_folder = media_pool.GetRootFolder()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for timeline_item in current_timeline.GetItemListInTrack("video", 1):
        ...     timeline_item.ExportLUT(resolve.EXPORT_LUT_33PTCUBE, '/Users/thom/Desktop/sample_lut.cube')

        """
        ...

    def GetLinkedItems(self) -> list["TimelineItem"]:
        """
        Returns a list of linked timeline items.
        """
        ...

    def GetTrackTypeAndIndex(self) -> list[tuple[str, int]]:
        """
        Returns a list of two values that correspond to the TimelineItem's trackType
        (string) and trackIndex (int) respectively.

        trackType is one of {"audio", "video", "subtitle"}.

        trackIndex is in this range: 1 <= trackIndex <= GetTrackCount(trackType).
        """
        ...

    def GetSourceAudioChannelMapping(self) -> str:
        """
        Returns a string with TimelineItem's audio mapping information. Check 'Audio
        Mapping' section below for more information.
        """
        ...


class Gallery:
    def GetAlbumName(self, gallery_still_album: "GalleryStillAlbum") -> str:
        """
        Returns the name of the :class:`dri.GalleryStillAlbum` object
        "galleryStillAlbum".

        Parameters
        ----------
        gallery_still_album
            :class:`dri.GalleryStillAlbum` object

        Returns
        -------
        str
            Album name.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> galley.GetAlbumName(current_gallery_still_ablum)
        Stills 1

        """
        ...

    def SetAlbumName(
        self, gallery_still_album: "GalleryStillAlbum", album_name: str
    ) -> bool:
        """
        Sets the name of the GalleryStillAlbum object "galleryStillAlbum" to "albumName".

        Parameters
        ----------
        gallery_still_album
            :class:`dri.GalleryStillAlbum` object
        album_name
            Album name to set.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> galley.SetAlbumName(current_gallery_still_ablum, "New Album Name")
        True

        """
        ...

    def GetCurrentStillAlbum(self) -> "GalleryStillAlbum":
        """
        Returns current album as a GalleryStillAlbum object.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()

        """
        ...

    def SetCurrentStillAlbum(self, gallery_still_album: "GalleryStillAlbum") -> bool:
        """
        Sets current album to GalleryStillAlbum object "galleryStillAlbum".

        Parameters
        ----------
        gallery_still_album
            :class:`dri.GalleryStillAlbum` object

        Returns
        -------
        bool
            True if successful, False otherwise.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> gallery_still_ablums: list[GalleryStillAlbum] = galley.GetGalleryStillAlbums()
        >>> galley.SetCurrentStillAlbum(gallery_still_ablums[0])
        True

        """
        ...

    def GetGalleryStillAlbums(self) -> list["GalleryStillAlbum"]:
        """
        Returns the gallery albums as a list of GalleryStillAlbum objects.

        Returns
        -------
        list[GalleryStillAlbum]
            A list of :class:`dri.GalleryStillAlbum` object.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> gallery_still_albums: list[GalleryStillAlbum] = galley.GetGalleryStillAlbums()

        """
        ...


class GalleryStillAlbum:
    def GetStills(self) -> list["GalleryStill"]:
        """
        Returns the list of GalleryStill objects in the album.

        Returns
        -------
        list[GalleryStill]
            A list of GalleryStill objects in the album.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> current_gallery_still_ablum.GetStills()
        [<BlackmagicFusion.PyRemoteObject object at 0x102f72070>, <BlackmagicFusion.PyRemoteObject object at 0x102f70ff0>]

        """
        ...

    def GetLabel(self, gallery_still: "GalleryStill") -> str:
        """
        Returns the label of the galleryStill.

        Parameters
        ----------
        gallery_still
            Get label from this :class:`GallerySill` object.

        Returns
        -------
        str
            The Label of this :class:`GalleryStill` object.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> for still in current_gallery_still_ablum.GetStills():
        ...     current_gallery_still_ablum.GetLabel(still)

        """
        ...

    def SetLabel(self, gallery_still: "GalleryStill", label: str) -> bool:
        """
        Sets the new 'label' to GalleryStill object 'galleryStill'.

        Parameters
        ----------
        gallery_still
            Target of setting new label to.
        label
            New label.

        Returns
        -------
        bool
            True if successful, false otherwise.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> for still in current_gallery_still_ablum.GetStills():
        ...     current_gallery_still_ablum.SetLabel(still, "Label Name")

        """
        ...

    def ImportStills(self, file_paths: str | list[str]) -> bool:
        """
        Imports GalleryStill from each filePath in [filePaths] list. True if at least
        one still is imported successfully. False otherwise.

        Parameters
        ----------
        file_path
           File paths that store GalleryStills.

        Returns
        -------
        bool
            True if at least one still is imported successfully, false otherwise.

        Notes
        -----
        It can also take a single file path, not limited to only accept a list of file
        paths.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> current_gallery_still_ablum.ImportStills("~/Downloads/Still_1.1.1.drx")

        """
        ...

    def ExportStills(
        self,
        gallery_still: list["GalleryStill"],
        folder_path: str,
        file_prefix: str,
        format: str,
    ) -> bool:
        """
        Exports list of GalleryStill objects '[galleryStill]' to directory 'folderPath',
        with filename prefix 'filePrefix', using file format 'format' (supported
        formats: dpx, cin, tif, jpg, png, ppm, bmp, xpm, drx).

        Parameters
        ----------
        gallery_still
            The list of `GalleryStill` objects to be exported.
        folder_path
            The path of the folder where the stills will be exported to.
        file_prefix
            The prefix that will be added to the filenames of all exported stills.
        format
            The format of the exported stills. Supported formats are: dpx, cin, tif,
            jpg, png, ppm, bmp, xpm, and drx.

        Returns
        -------
        bool
            Return `True` if all the stills are successfully exported, `False`
            otherwise.

        Notes
        -----
        folder_path must be absolute path, abbreviation like `~/Downloads/` will not
        work.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> gallery_stills_to_export = current_gallery_still_ablum.GetStills()
        >>> current_gallery_still_ablum.ExportStills(
        ...     gallery_stills_to_export, "/Users/thom/Downloads/", "prefix", "png"
        ... )

        """
        ...

    def DeleteStills(self, gallery_still: list["GalleryStill"]) -> bool:
        """
        Deletes specified list of GalleryStill objects '[galleryStill]'.

        Parameters
        ----------
        gallery_still
            The list of `GalleryStill` objects that are to be deleted.

        Returns
        -------
        bool
            Return `True` if all objects were successfully deleted, `False` otherwise.

        Examples
        --------
        >>> from dri import GalleryStillAlbum, Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        ...
        >>> galley = project.GetGallery()
        >>> current_gallery_still_ablum: GalleryStillAlbum = galley.GetCurrentStillAlbum()
        >>> gallery_stills_to_export = current_gallery_still_ablum.GetStills()
        >>> current_gallery_still_ablum.DeleteStills(gallery_stills_to_export)

        """
        ...


class GalleryStill:
    """
    This class does not provide any API functions but the object type is used by
    functions in other classes.
    """

    ...


class Graph:
    def GetNumNodes(self) -> int:
        """
        Returns the number of nodes in the graph.
        """
        ...

    def SetLUT(self, node_index: int, lut_path: str) -> bool:
        """
        Sets LUT on the node mapping the node index provided, 1 <= nodeIndex <=
        self.GetNumNodes().

        The lutPath can be an absolute path, or a relative path (based off custom LUT
        paths or the master LUT path).

        The operation is successful for valid lut paths that Resolve has already
        discovered (see Project.RefreshLUTList).
        """
        ...

    def GetLUT(self, node_index: int) -> str:
        """
        Gets relative LUT path based on the node index provided, 1 <= nodeIndex <= total
        number of nodes.

        Examples
        --------
        >>> from dri import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> current_timeline = project.GetCurrentTimeline()
        ...
        >>> for i in current_timeline.GetItemListInTrack("video", 1):
        ...     print(i.GetNodeGraph().GetLUT(1))
        Arri/ARRI_LogC4_v1_LUT_Package/LUTs/ARRI_LogC4-to-Gamma24_Rec709-D65_v1-65.cube
        Arri/ARRI_LogC4_v1_LUT_Package/LUTs/ARRI_LogC4-to-Gamma24_Rec709-D65_v1-65.cube
        """
        ...

    def GetNodeLabel(self, node_index: int) -> bool:
        """
        Returns the label of the node at nodeIndex.
        """
        ...

    def GetToolsInNode(self, node_index: int) -> list:
        """
        Returns toolsList (list of strings) of the tools used in the node indicated by
        given nodeIndex (int).
        """
        ...

    def SetNodeEnabled(self, node_index: int, is_enabled: bool) -> bool:
        """
        Sets the node at the given nodeIndex (int) to isEnabled (bool). 1 <= nodeIndex
        <= self.GetNumNodes().

        """
        ...


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


class FusionComp: ...
