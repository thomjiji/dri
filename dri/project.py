from dataclasses import dataclass
from typing import Literal, TypedDict

from dri.gallery import Gallery
from dri.media_pool import MediaPool
from dri.timeline import Timeline


@dataclass
class RenderSetting(TypedDict):
    SelectAllFrames: bool
    MarkIn: int
    MarkOut: int
    TargetDir: str
    CustomName: str
    UniqueFilenameStyle: Literal[0, 1]  # 0 - Prefix, 1 - Suffix
    ExportVideo: bool
    ExportAudio: bool
    FormatWidth: int
    FormatHeight: int
    FrameRate: float  # Example: 23.976, 24

    # For SD resolution: "16_9" or "4_3", other resolution: "square" or "cinemascope"
    PixelAspectRatio: str

    # "VideoQuality" possible values for current codec (if applicable):
    #  -    0 (int) - will set quality to automatic
    #  -    [1 -> MAX] (int) - will set input bit rate
    #  -    ["Least", "Low", "Medium", "High", "Best"] (string) - will set input
    #       quality level
    VideoQuality: int | str

    AudioCodec: str  # Example: "aac"
    AudioBitDepth: int
    AudioSampleRate: int
    ColorSpaceTag: str  # Example: "Same as Project", "AstroDesign"
    GammaTag: str  # Example: "Same as Project", "ACEScct"
    ExportAlpha: bool
    EncodingProfile: str  # Example: "Main10". Can only be set for H.264 and H.265.
    MultiPassEncode: bool  # Can only be set for H.264.

    # 0 - Premultiplied, 1 - Straight. Can only be set for H.264 and H.265.
    AlphaMode: Literal[0, 1]

    NetworkOptimization: bool  # Only supported by QuickTime and MP4 formats.


class Project:
    def GetMediaPool(self) -> MediaPool:
        """
        Returns the Media Pool object.

        Returns
        -------
        :class:`dri.MediaPool`
            The Media Pool object.

        """
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
            The index of Timeline that's going to return.

        Returns
        -------
        :class:`dri.Timeline`
            The Timeline object at the give index.

        """
        ...

    def GetCurrentTimeline(self) -> Timeline:
        """
        Returns the currently loaded timeline.

        Returns
        -------
        :class:`Timeline`
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

    def GetRenderJobList(self) -> list[dict[str, str | int | float | bool]]:
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

    def IsRenderingInProgress(self) -> bool:
        """
        Returns True if rendering is in progress.

        Returns
        -------
        bool
            True if rendering is in progress, False otherwise.

        """
        ...

    def LoadRenderPreset(self, preset_name: str) -> bool:
        """
        Sets a preset as current preset for rendering if presetName (string) exists.

        Parameters
        ----------
        preset_name
            The preset name.

        Returns
        -------
        bool
            True if load successful, False otherwise.

        """
        ...

    def SaveAsNewRenderPreset(self, preset_name: str) -> bool:
        """
        Creates new render preset by given name if presetName (string) is unique.

        Parameters
        ----------
        preset_name
            The preset name.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def SetRenderSettings(
        self, settings: RenderSetting | dict[str, int | float | str | bool]
    ) -> bool:
        """
        Sets given settings for rendering. Settings is a dict, with support for the
        keys: Refer to "Looking up render settings" section for information for
        supported settings.

        Parameters
        ----------
        settings
            A dict with settings (specified in RenderSetting class).

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetRenderJobStatus(self, job_id: str) -> dict[str, str | int]:
        """
        Returns a dict with job status and completion percentage of the job by given
        jobId (string).

        Parameters
        ----------
        job_id
            Render job's ID (string).

        Returns
        -------
        dict[str, str | int]
            A dict with job status and completion percentage of the job by given
            jobId (string).

        """
        ...

    def GetSetting(self, setting_name: str = None) -> str | dict[str, str | float]:
        """
        Returns value of project setting (indicated by settingName, string). Check
        the section below for more information.

        Parameters
        ----------
        setting_name
            Project setting name. Could be None. If not specified, return all
            settings and their value (string).

        Returns
        -------
        str | dict[str, str | float]
            Value of project setting (indicated by settingName, string). If settingName
            is not specified, will return dict[str, str | float]. "timelineFrameRate"
            could be of float, see example below.

        Examples
        --------
        >>> project.GetSetting("timelineFrameRate")
        "24.0"


        """
        ...

    def SetSetting(self, setting_name: str, setting_value: str) -> bool:
        """
        Sets the project setting (indicated by settingName, string) to the value (
        settingValue, string). Check the section below for more information.

        Parameters
        ----------
        setting_name
            Project setting name.
        setting_value
            Project setting value.

        Returns
        -------
        bool
            True if set successful, False otherwise.

        """
        ...

    def GetRenderFormats(self) -> dict[str, str]:
        """
        Returns a dict (format -> file extension) of available render formats.

        Returns
        -------
        dict
            A dict (format -> file extension) of available render formats.

        Examples
        --------
        >>> project.GetRenderFormats()
        {'AVI': 'avi',
         'BRAW': 'braw',
         'Cineon': 'cin',
         'DCP': 'dcp',
         'DPX': 'dpx',
         'EXR': 'exr',
         'GIF': 'gif',
         'HLS': 'm3u8',
         'IMF': 'imf',
         'JPEG 2000': 'j2c',
         'MJ2': 'mj2',
         'MKV': 'mkv',
         'MP4': 'mp4',
         'MTS': 'mts',
         'MXF OP-Atom': 'mxf',
         'MXF OP1A': 'mxf_op1a',
         'Panasonic AVC': 'pavc',
         'QuickTime': 'mov',
         'TIFF': 'tif',
         'Wave': 'wav'}

        """
        ...

    def GetRenderCodecs(self, render_format: str) -> dict[str, str]:
        """
        Returns a dict (codec description -> codec name) of available codecs for
        given render format (string).

        Parameters
        ----------
        render_format
            Render format (string). Such as "MP4", "mp4", "MKV", "mov",
            case-insensitive. Also note that you cannot use "QuickTime" to retrieve the
            codec, only "mov" in this case.

        Returns
        -------
        dict
            A dict (codec description -> codec name) of available codecs for
            given render format (string).

        """
        ...

    def GetCurrentRenderFormatAndCodec(self) -> dict[str, str]:
        """
        Returns a dict with currently selected format 'format' and render codec 'codec'.

        Returns
        -------
        dict[str, str]
            A dict with currently selected format and codec.

        Examples
        --------
        >>> project.GetCurrentRenderFormatAndCodec()
        {'format': 'mov', 'codec': 'H265'}

        """
        ...

    def SetCurrentRenderFormatAndCodec(self, render_format: str, codec: str) -> bool:
        """
        Sets given render format (string) and render codec (string) as options for
        rendering.

        Parameters
        ----------
        render_format
            Render format (string). Such as "mov", "mp4", "mkv". You can use
            *GetRenderFormats()* to retrieve all available formats. Note that you can
            only use the **file extension** ("mov", "mp4", not "QuickTime", "MP4") as
            arg passed to *SetCurrentRenderFormatAndCodec()*.
        codec
            Render codec (string). Such as "H265". You can use *GetRenderCodecs(
            render_format: str)* to retrieve all available codecs under the given
            render formats. Note that you can only use the **codec name** not the
            **codec description** as arg passed to *SetCurrentRenderFormatAndCodec()*.

        Returns
        -------
        bool
            True if set successful, False otherwise.

        """
        ...

    def GetCurrentRenderMode(self) -> int:
        """
        Returns the render mode: 0 - Individual clips, 1 - Single clip.

        Returns
        -------
        int
            Render mode (0 - Individual clips, 1 - Single clip).

        """
        ...

    def SetCurrentRenderMode(self, render_mode: int) -> bool:
        """
        Sets the render mode. Specify renderMode = 0 for Individual clips,
        1 for Single clip.

        Parameters
        ----------
        render_mode
            0 for Individual Clips, 1 for Single Clip.

        Returns
        -------
        bool
            True if set successful, False otherwise.

        """
        ...

    def GetRenderResolutions(
        self, render_format: str, codec: str
    ) -> list[dict[str, int]]:
        """
        Returns list of resolutions applicable for the given render format (string)
        and render codec (string). Returns full list of resolutions if no argument is
        provided. Each element in the list is a dictionary with 2 keys "Width" and
        "Height".

        Parameters
        ----------
        render_format
            Render format (string).
        codec
            Render codec (string).

        Returns
        -------
        list[dict[str, int]]
            List of resolutions applicable for the given render format (string)
            and render codec (string).

        """
        ...

    def RefreshLUTList(self) -> bool:
        """
        Refreshes LUT list.

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the project item.

        Returns
        -------
        str
            A unique ID for the project item.

        """
        ...

    def InsertAudioToCurrentTrackAtPlayhead(
        self, media_path: str, start_offset_in_samples: int, duration_in_samples: int
    ) -> bool:
        """
        Inserts the media specified by mediaPath (string) with startOffsetInSamples (
        int) and durationInSamples (int) at the playhead on a selected track on the
        Fairlight page. Returns True if successful, otherwise False.

        Parameters
        ----------
        media_path
            Path to the media file (string) that's going to be inserted.
        start_offset_in_samples
            Start offset
        duration_in_samples
            Duration

        Returns
        -------
        bool
            True if successful, False otherwise.

        """
        ...

    def LoadBurnInPreset(self, preset_name: str) -> bool:
        """
        Loads user defined data burn in preset for project when supplied presetName (
        string). Returns true if successful.

        Parameters
        ----------
        preset_name
            Burn-in preset name

        Returns
        -------
        bool
            True if load successful, False otherwise.

        """
        ...