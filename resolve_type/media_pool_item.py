from .marker_color import MarkerColor


class MediaPoolItem:
    def GetName(self) -> str:
        """
        Returns the clip name.

        """
        pass

    def GetMetadata(self, metadata_type=None) -> str | dict[str, str]:
        """
        Returns the metadata value for the key "metadataType". If no argument is
        specified, a dict of all set metadata properties is returned.

        """
        pass

    def SetMetadata(self, metadata_type: str, metadata_value: str) -> bool:
        """
        Sets the given metadata to metadataValue (string). Returns True if successfully.

        """
        pass

    # TODO
    def SetMetadata(self, metadata: dict) -> bool:
        """
        Sets the item metadata with specified "metadata" dict. Returns True if
        successful.

        """
        pass

    def GetClipProperty(self, property_name=None):
        pass

    def GetMediaId(self) -> bool:
        """
        Returns the unique ID for the MediaPoolItem.

        """
        pass

    def AddMarker(
        self,
        frame_id: int,
        color: MarkerColor,
        name: str,
        note: str,
        duration: int,
        custom_data: str,
    ) -> bool:
        """
        Creates a new marker at given frameId position and with given marker
        information. "customData" is optional and helps to attach user specific data
        to the marker.

        Parameters
        ----------
        frame_id
        color
        name
        note
        duration
        custom_data

        Returns
        -------

        """

        pass

    def GetMarkers(self) -> dict[int, dict[str, str | int]]:
        """
        Returns a dict of all markers and dicts with their information.

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
        pass

    def GetMarkerByCustomData(self, custom_data: str) -> dict[str, int]:
        """
        Returns marker {information} for the first matching marker with specified
        customData.

        Examples
        --------
        >>> from resolve_init import GetResolve
        >>> resolve = GetResolve()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
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
        pass