class Timeline:
    def GetName(self) -> str:
        """
        Returns the timeline name.

        """
        ...

    def SetName(self, timeline_name) -> bool:
        """
        Sets the timeline name if timelineName (string) is unique. Returns True if
        successful.

        Parameters
        ----------
        timeline_name
            Timeline name to set

        """
        ...

    def GetStartFrame(self) -> int:
        """
        Returns the frame number at the start of timeline.

        """
        ...