from dri.gallery_still_album import GalleryStillAlbum


class Gallery:
    def GetAlbumName(self, gallery_still_album: GalleryStillAlbum) -> str:
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

        """
        ...

    def SetAlbumName(
        self, gallery_still_album: GalleryStillAlbum, album_name: str
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

        """
        ...

    def GetCurrentStillAlbum(self) -> GalleryStillAlbum:
        """
        Returns current album as a GalleryStillAlbum object.
        """
        ...

    def SetCurrentStillAlbum(self, gallery_still_album: GalleryStillAlbum) -> bool:
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

        """
        ...

    def GetGalleryStillAlbums(self) -> list[GalleryStillAlbum]:
        """
        Returns the gallery albums as a list of GalleryStillAlbum objects.

        Returns
        -------
        list[GalleryStillAlbum]
            A list of :class:`dri.GalleryStillAlbum` object.
        """
        ...
