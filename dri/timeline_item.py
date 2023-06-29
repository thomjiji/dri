from typing import Optional

from dri.color import MarkerColor
from dri.fusion_comp import FusionComp


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
            True if successful.

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
        color: MarkerColor,
        name: str,
        note: Optional[str],
        duration: int,
        custom_data: Optional[str],
    ) -> bool:
        """
        Creates a new marker at given frameId position and with given marker
        information. 'customData' is optional and helps to attach user specific data
        to the marker.

        Parameters
        ----------
        frame_id
            Frame number. Which is "Source Frame".
        color
            Marker color.
        name
            Marker name.
        note
            Marker note. Optional.
        duration
            Marker duration.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI. Optional.

        Returns
        -------
        bool
            True if successful, False otherwise.

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