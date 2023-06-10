from typing import Optional

from dri.project import Project


class ProjectManager:
    def ArchiveProject(
        self,
        project_name: str,
        file_path: str,
        is_archive_src_media: bool = True,
        is_archive_render_cache: bool = True,
        is_archive_proxy_media: bool = False,
    ) -> bool:
        """
        Archives project to provided file path with the configuration as provided by
        the optional arguments

        Parameters
        ----------
        project_name
            Project name
        file_path
            Archive destination
        is_archive_src_media
            Defaults to True
        is_archive_render_cache
            Defaults to True
        is_archive_proxy_media
            Default to False

        Returns
        -------
        bool
            True if successful, False otherwise

        """
        ...

    def CreateProject(self, project_name: str) -> Optional[bool]:
        """
        Creates and returns a project if projectName (string) is unique, and None if
        it is not.

        Parameters
        ----------
        project_name
            Project name.

        Returns
        -------
        Optional[bool]
            Project object if project is created, None otherwise.

        """
        ...

    def DeleteProject(self, project_name: str) -> bool:
        """
        Delete project in the current folder if not currently loaded.

        Parameters
        ----------
        project_name
            Project name.

        Returns
        -------
        bool
            True if delete successful, False otherwise.

        """
        ...

    def LoadProject(self, project_name: str) -> Optional[Project]:
        """
        Loads and returns the project with name = projectName (string) if there is a
        match found, and None if there is no matching Project.

        Parameters
        ----------
        project_name
            Project name.

        Returns
        -------
        Optional[Project]
            Return a Project object if project is loaded, None otherwise.

        """
        ...

    def GetCurrentProject(self) -> Project:
        """
        Returns the currently loaded Resolve project.

        Returns
        -------
        Project
            The currently loaded Resolve project.

        """
        ...

    def SaveProject(self) -> bool:
        """
        Saves the currently loaded project with its own name. Returns True if
        successful.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def CloseProject(self, project: Project) -> bool:
        """
        Closes the specified project without saving.

        Parameters
        ----------
        project
            The Project object to close.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def CreateFolder(self, folder_name: str) -> bool:
        """
        Creates a folder if folderName (string) is unique. Return False if it's not.

        Parameters
        ----------
        folder_name
            Folder name.

        Returns
        -------
        bool
            True if successful, False otherwise (maybe folder with that name exists).

        """
        ...

    def DeleteFolder(self, folder_name: str) -> bool:
        """
        Deletes the specified folder if it exists. Returns True in case of success.

        Parameters
        ----------
        folder_name
            Folder name that's going to be deleted.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetProjectListInCurrentFolder(self) -> list[str]:
        """
        Returns a list of project names in current folder.

        Returns
        -------
        list[str]
            List of project names (string) in current folder.

        """
        ...

    def GetFolderListInCurrentFolder(self) -> list[str]:
        """
        Returns a list of folder names in current folder.

        Returns
        -------
        list[str]
            List of folder names (string) in current folder.

        """
        ...

    def GotoRootFolder(self) -> bool:
        """
        Opens root folder in database.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GotoParentFolder(self) -> bool:
        """
        Opens parent folder of current folder in database if current folder has parent.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetCurrentFolder(self) -> str:
        """
        Returns the current folder name.

        Returns
        -------
        str
            The current folder name.

        """
        ...

    def OpenFolder(self, folder_name: str) -> bool:
        """
        Opens folder under given name.

        Parameters
        ----------
        folder_name
            Folder name.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ImportProject(self, file_path: str, project_name: str = None) -> bool:
        """
        Imports a project from the file path provided with given project name,
        if any. Returns True if successful.

        Parameters
        ----------
        file_path
            File path to import project from. Must be an absolute path.
        project_name
            Project name of the project to be imported. If not specified,
            use project path name, such as "/Users/thom/Desktop/my_project.drp" -
            "my_project".

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def ExportProject(
        self, project_name: str, file_path: str, with_stills_and_luts: bool = True
    ) -> bool:
        """
        Exports project to provided file path, including stills and LUTs if
        withStillsAndLUTs is True (enabled by default). Returns True in case of success.

        Parameters
        ----------
        project_name
            Project name of the project to be exported.
        file_path
            File path to export project to. Must be an absolute path.
        with_stills_and_luts
            "Export Project with Stills and LUTs...", Defaults to True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def RestoreProject(self, file_path: str, project_name: str) -> bool:
        """
        Restores a project from the file path provided with given project name,
        if any. Returns True if successful.

        Parameters
        ----------
        file_path
        project_name

        Returns
        -------

        """
        ...

    def GetCurrentDatabase(self) -> dict[str, str]:
        """
        Returns a dictionary (with keys 'DbType', 'DbName' and optional 'IpAddress')
        corresponding to the current database connection.

        Returns
        -------
        dict[str, str]
            Dictionary with keys 'DbType', 'DbName' and optional 'IpAddress'.

        """
        ...

    def GetDatabaseList(self) -> list[dict[str, str]]:
        """
        Returns a list of dictionary items (with keys 'DbType', 'DbName' and optional
        'IpAddress') corresponding to all the databases added to Resolve.

        Returns
        -------
        list[dict[str, str]]
            List of dictionary items (with keys 'DbType', 'DbName' and optional
        'IpAddress').

        """
        ...

    def SetCurrentDatabase(self, db_info: dict) -> bool:
        """
        Switches current database connection to the database specified by the keys
        below, and closes any open project.

        -   'DbType': 'Disk' or 'PostgreSQL' (string)
        -   'DbName': database name (string)
        -   'IpAddress': IP address of the PostgreSQL server (string, optional key -
            defaults to '127.0.0.1')

        Parameters
        ----------
        db_info
            Database info as specified above.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...