import importlib.util
import platform
from dataclasses import dataclass
from types import ModuleType
from typing import Optional

from dri.media_storage import MediaStorage
from dri.project_manager import ProjectManager


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


@dataclass
class Resolve:
    # For timeline.Export().
    EXPORT_AAF: str = "AAF"
    EXPORT_DRT: str = "DRT"
    EXPORT_EDL: str = "EDL"
    EXPORT_FCP_7_XML: str = "FCP_7_XML"
    EXPORT_FCPXML_1_8: str = "FCPXML_1_8"
    EXPORT_FCPXML_1_9: str = "FCPXML_1_9"
    EXPORT_FCPXML_1_10: str = "FCPXML_1_10"
    EXPORT_HDR_10_PROFILE_A: str = "HDR_10_PROFILE_A"
    EXPORT_HDR_10_PROFILE_B: str = "HDR_10_PROFILE_B"
    EXPORT_TEXT_CSV: str = "TEXT_CSV"
    EXPORT_TEXT_TAB: str = "TEXT_TAB"
    EXPORT_DOLBY_VISION_VER_2_9: str = "DOLBY_VISION_VER_2_9"
    EXPORT_DOLBY_VISION_VER_4_0: str = "DOLBY_VISION_VER_4_0"
    EXPORT_DOLBY_VISION_VER_5_1: str = "DOLBY_VISION_VER_5_1"
    EXPORT_OTIO: str = "OTIO"

    EXPORT_NONE: str = "NONE"
    EXPORT_AAF_NEW: str = "AAF_NEW"
    EXPORT_AAF_EXISTING: str = "AAF_EXISTING"
    EXPORT_CDL: str = "CDL"
    EXPORT_SDL: str = "SDL"
    EXPORT_MISSING_CLIPS: str = "MISSING_CLIPS"

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

    def GetMediaStorage(self) -> MediaStorage:
        """
        Returns the media storage object to query and act on media locations.

        Returns
        -------
        MediaStorage
            The media storage object to query and act on media locations.

        """
        ...

    def GetProjectManager(self) -> ProjectManager:
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
