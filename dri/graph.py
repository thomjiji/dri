class Graph:
    def GetNumNodes(self) -> int:
        """
        Returns the number of nodes in the graph.
        """
        ...

    def SetLUT(self, node_index: int, lut_path: str) -> bool:
        """
        Sets LUT on the node mapping the node index provided, 1 <= nodeIndex <=
        self.GetNumNodes().

        The lutPath can be an absolute path, or a relative path (based off custom LUT
        paths or the master LUT path).

        The operation is successful for valid lut paths that Resolve has already
        discovered (see Project.RefreshLUTList).
        """
        ...

    def GetLUT(self, node_index: int) -> str:
        """
        Gets relative LUT path based on the node index provided, 1 <= nodeIndex <= total
        number of nodes.

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
        ...     print(i.GetLUT())
        Arri/ARRI_LogC4_v1_LUT_Package/LUTs/ARRI_LogC4-to-Gamma24_Rec709-D65_v1-65.cube
        Arri/ARRI_LogC4_v1_LUT_Package/LUTs/ARRI_LogC4-to-Gamma24_Rec709-D65_v1-65.cube
        """
        ...

    def GetNodeLabel(self, node_index: int) -> bool:
        """
        Returns the label of the node at nodeIndex.
        """
        ...

    def GetToolsInNode(self, node_index: int) -> list:
        """
        Returns toolsList (list of strings) of the tools used in the node indicated by
        given nodeIndex (int).
        """
        ...
