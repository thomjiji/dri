from dri.gallery import Gallery
from dri.timeline import Timeline
from dri.media_pool import MediaPool


class Project:
    def GetMediaPool(self) -> MediaPool:
        ...

    def GetTimelineCount(self) -> int:
        """
        Returns the number of timelines currently present in the project.

        Returns
        -------
        int
            The number of timelines currently present in the project.

        """
        ...

    def GetTimelineByIndex(self, idx: int) -> Timeline:
        """
        Returns timeline at the give index, 1 <= idx <= project.GetTimelineCount().

        Parameters
        ----------
        idx
            Index of the timeline to get.

        Returns
        -------

        """
        ...

    def GetCurrentTimeline(self) -> Timeline:
        """
        Returns the currently loaded timeline.

        Returns
        -------
        Timeline
            The currently loaded timeline.

        """
        ...

    def SetCurrentTimeline(self, timeline: Timeline) -> bool:
        """
        Sets given timeline as current timeline for the project. Returns True if
        successful.

        Parameters
        ----------
        timeline
            The Timeline object to set as current timeline.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetGallery(self) -> Gallery:
        """
        Returns the Gallery object.

        Returns
        -------
        Gallery
            The Gallery object.

        """
        ...

    def GetName(self) -> str:
        """
        Returns the project name.

        Returns
        -------
        str
            The project name.

        """
        ...

    def SetName(self, project_name: str) -> bool:
        """
        Sets project name if given projectName (string) is unique.

        Parameters
        ----------
        project_name
            The project name to set.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetPresetList(self) -> list[dict[str, str]]:
        """
        Returns a list of presets and their information.

        Returns
        -------
        list[dict[str, str]]
            List of presets and their information.

        Examples
        --------
        >>> project.GetPresetList()
        [{'Name': 'Current Project', 'Width': 1920, 'Height': 1080},
         {'Name': 'System Config', 'Width': 1920, 'Height': 1080},
         {'Name': 'guest default config', 'Width': 1920, 'Height': 1080}]

        """
        ...

    def SetPreset(self, preset_name: str) -> bool:
        """
        Sets preset by given presetName (string) into project.

        Parameters
        ----------
        preset_name
            The preset name to set.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def AddRenderJob(self) -> str:
        """
        Adds a render job based on current render settings to the render queue.
        Returns a unique job id (string) for the new render job.

        Returns
        -------
        str
            Unique job id (string) for the new render job.

        """
        ...

    def DeleteRenderJob(self, job_id: str) -> bool:
        """
        Deletes render job for input job id (string).

        Parameters
        ----------
        job_id
            Render job's ID (string)

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def DeleteAllRenderJobs(self) -> bool:
        """
        Deletes all render jobs in the queue.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetRenderJobList(self) -> list[dict[str | int | float]]:
        """
        Returns a list of render jobs and their information.

        Returns
        -------
        list[dict[str | int | float]]
            List of render jobs and their information.

        """
        ...

    def StartRendering(self, *job_ids: str, is_interactive_mode: bool = False) -> bool:
        """
        Starts rendering jobs indicated by the input job ids. If not specified,
        it will start all queued jobs one by one. The optional "isInteractiveMode",
        when set, enables error feedback in the UI during rendering.

        Parameters
        ----------
        job_ids
            Render job's ID (string). Can be empty.
        is_interactive_mode
            When set, enables error feedback in the UI during rendering.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def StartRendering(
        self, job_ids: list[str], is_interactive_mode: bool = False
    ) -> bool:
        """
        Starts rendering jobs indicated by the input job ids. The optional
        "isInteractiveMode", when set, enables error feedback in the UI during
        rendering.

        Parameters
        ----------
        job_ids
            A list of job ids to start rendering.
        is_interactive_mode
            When set, enables error feedback in the UI during rendering.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def StopRendering(self):
        """
        Stops any current render processes.

        """
        ...

    def GetCurrentTimeline(self) -> Timeline:
        ...