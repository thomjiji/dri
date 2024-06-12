from typing import Literal, Optional

from dri.color import LiteralClipColor, LiteralFlagColor, LiteralMarkerColor
from dri.fusion_comp import FusionComp
from dri.graph import Graph
from dri.media_pool_item import MediaPoolItem


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

    def GetFusionCompByIndex(self, comp_index: int) -> FusionComp:
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

    def GetFusionCompByName(self, comp_name: str) -> FusionComp:
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
        >>> from dri.resolve import Resolve
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
        >>> from dri.resolve import Resolve
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

    def AddFusionComp(self) -> FusionComp:
        """
        Adds a new Fusion composition associated with the timeline item.

        Returns
        -------
        FusionComp
            Fusion composition.

        """
        ...

    def ImportFusionComp(self, path: str) -> FusionComp:
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

    def LoadFusionCompByName(self, comp_name: str) -> FusionComp:
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
        >>> from dri.resolve import Resolve
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
        >>> from dri.resolve import Resolve
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
        >>> from dri.resolve import Resolve
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
        >>> from dri.resolve import Resolve
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
        Copies the current grade to all the items in tgtTimelineItems list. Returns True
        on success and False if any error occurred.

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

    def GetNodeGraph(self) -> Graph:
        """
        Returns the clip's node graph object.
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
        >>> from dri.resolve import Resolve
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
