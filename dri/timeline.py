from dri.color import MarkerColor


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
        information. 'customData' is optional and helps to attach user specific data
        to the marker.

        Notes
        -----
        -   frameId is not source frame, but a Record Frame minus the first frame
            of the current timeline - 01:00:00:00 (24 fps timeline: 86400, 25 fps
            timeline: 90000).
        -   For example: Here is a marker located at record frame 86607. We know that
            current timeline is 24fps, so the first frame is 86400. Here we can get the
            frameId which is 86607 - 86400 = 207.

        Returns
        -------
        bool
            True if the marker was created successfully.

        """
        ...