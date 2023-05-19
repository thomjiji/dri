from .media_pool_item import MediaPoolItem


class Folder:
    def GetClipList(self) -> list[MediaPoolItem]:
        """
        Returns a list of clips (items) within the folder.

        """
        ...

    def GetName(self) -> str:
        """
        Returns the media folder name.

        """
        ...

    def GetSubFolderList(self) -> list["Folder"]:
        """
        Returns a list of subfolders in the folder.

        """
        ...

    def GetIsFolderStale(self) -> bool:
        """
        Return true if folder is stale in collaboration mode, false otherwise.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the media pool folder.

        """
        ...