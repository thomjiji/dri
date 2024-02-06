from dri.media_pool_item import MediaPoolItem
from typing import Literal


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
    ) -> list[MediaPoolItem]:
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

    def AddItemListToMediaPool(self, item_paths: list[str]) -> list[MediaPoolItem]:
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
    ) -> list[MediaPoolItem]:
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
        media_pool_item: MediaPoolItem,
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

    def AddTimelineMattesToMediaPool(self, paths: list[str]) -> list[MediaPoolItem]:
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
