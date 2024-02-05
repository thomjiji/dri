from typing import Literal, Optional, TypedDict

from dri.color import LiteralClipColor, LiteralFlagColor, LiteralMarkerColor


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
        information. "customData" is optional and helps to attach user specific data
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
