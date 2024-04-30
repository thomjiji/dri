from dri.media_pool_item import MediaPoolItem


class Folder:
    def GetClipList(self) -> list[MediaPoolItem]:
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
