from dri.gallery_still import GalleryStill


class GalleryStillAlbum:
    def GetStills(self) -> list[GalleryStill]:
        """
        Returns the list of GalleryStill objects in the album.

        Returns
        -------
        list[GalleryStill]
            A list of GalleryStill objects in the album.

        """
        ...

    def GetLabel(self, gallery_still: GalleryStill) -> str:
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

        """
        ...

    def SetLabel(self, gallery_still: GalleryStill, label: str) -> bool:
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

        """
        ...

    def ImportStills(self, file_paths: list[str]) -> bool:
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

        """
        ...

    def ExportStills(
        self,
        gallery_still: list[GalleryStill],
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

        """
        ...

    def DeleteStills(self, gallery_still: list[GalleryStill]) -> bool:
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

        """
        ...
