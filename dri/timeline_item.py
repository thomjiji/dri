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