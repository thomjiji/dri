from dataclasses import dataclass
from typing import Literal

from dri.color import MarkerColor
from dri.gallery_still import GalleryStill
from dri.timeline_item import TimelineItem


@dataclass
class ThumbnailData:
    width: int
    height: int
    format: str
    data: str


class ImportOption:
    """
    For :func:`ImportIntoTimeline` use.

    Attributes
    ----------
    autoImportSourceClipsIntoMediaPool
        Specifies if source clips should be imported into media pool, True by default.
    ignoreFileExtensionsWhenMatching
        Specifies if file extensions should be ignored when matching, False by default.
    linkToSourceCameraFiles
        Specifies if link to source camera files should be enabled, False by default.
    useSizingInfo
        Specifies if sizing information should be used, False by default.
    importMultiChannelAudioTracksAsLinkedGroups
        Specifies if multichannel audio tracks should be imported as linked groups,
        False by default
    insertAdditionalTracks
        Specifies if additional tracks should be inserted, True by default.
    insertWithOffset
        specifies insert with offset value in timecode format - defaults to
        "00:00:00:00", applicable if "insertAdditionalTracks" is False.
    sourceClipsPath
        specifies a filesystem path to search for source clips if the media is
        inaccessible in their original path and if "ignoreFileExtensionsWhenMatching"
        is True.
    sourceClipsFolder
        list of Media Pool folder objects to search for source clips if the media is not
        present in current folder.

    """

    autoImportSourceClipsIntoMediaPool: bool = True
    ignoreFileExtensionsWhenMatching: bool = False
    linkToSourceCameraFiles: bool = False
    useSizingInfo: bool = False
    importMultiChannelAudioTracksAsLinkedGroups: bool = False
    insertAdditionalTracks: bool = True
    insertWithOffset: str = "00:00:00:00"
    sourceClipsPath: str = True
    sourceClipsFolder: str


class Timeline:
    def GetName(self) -> str:
        """
        Returns the timeline name.

        Returns
        -------
        str
            Timeline name

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

        Returns
        -------
        bool
            True if the timeline name was set successfully, False otherwise.

        """
        ...

    def GetStartFrame(self) -> int:
        """
        Returns the frame number at the start of timeline.

        Returns
        -------
        int
            Frame number at the start of timeline

        """
        ...

    def GetEndFrame(self) -> int:
        """
        Returns the frame number at the end of timeline.

        Returns
        -------
        int
            Frame number at the end of timeline

        """
        ...

    def SetStartTimecode(self, timecode: str) -> bool:
        """
        Set the start timecode of the timeline to the string 'timecode'. Returns true
        when the change is successful, false otherwise.

        Parameters
        ----------
        timecode
            Start timecode of the timeline, such as "01:00:00:00".

        Returns
        -------
        bool
            True if the change was successful, False otherwise.

        Examples
        --------
        >>> current_timeline.SetStartTimecode("00:00:00:00")
        True

        """
        ...

    def GetStartTimecode(self) -> str:
        """
        Returns the start timecode for the timeline.

        Returns
        -------
        str
            Start timecode for the timeline

        Examples
        --------
        >>> current_timeline.GetStartTimecode()
        '01:00:00:00'

        """
        ...

    def GetTrackCount(self, track_type: str) -> int:
        """
        Returns the number of tracks for the given track type ("audio", "video" or
        "subtitle").

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle")

        Returns
        -------
        int
            Number of tracks for the given track type

        """
        ...

    def AddTrack(self, track_type: str, optional_sub_track_type: str = None) -> bool:
        """
        Adds track of trackType ("video", "subtitle", "audio"). Second argument
        optionalSubTrackType is required for "audio".

        optionalSubTrackType can be one of {"mono", "stereo", "5.1", "5.1film",
        "7.1", "7.1film", "adaptive1", ... , "adaptive24"}.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle")
        optional_sub_track_type
            Sub track type ("audio", "video" or "subtitle"). Optional. Can be one of
            "mono", "stereo", "5.1", "5.1film", "7.1", "7.1film", "adaptive1",
            "adaptive2", "adaptive3", ..., "adaptive24".

        Returns
        -------
        bool
            True if the track was added successfully, False otherwise.

        """
        ...

    def DeleteTrack(self, track_type: str, track_index: int) -> bool:
        """
        Deletes track of trackType ("video", "subtitle", "audio") and given
        trackIndex. 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track was deleted successfully, False otherwise.

        """
        ...

    def SetTrackEnable(self, track_type: str, track_index: int, enabled: bool) -> bool:
        """
        Enables/Disables track with given trackType and trackIndex.

        trackType is one of {"audio", "video", "subtitle"}.

        trackIndex is in this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).
        enabled

        Returns
        -------
        bool
            True if the track was enabled/disabled successfully, False otherwise.

        """
        ...

    def GetIsTrackEnabled(self, track_type: str, track_index: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is enabled and False
        otherwise.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track is enabled, False otherwise.

        """
        ...

    def SetTrackLock(self, track_type: str, track_index: int, locked: bool) -> bool:
        """
        Locks/Unlocks track with given trackType and trackIndex.

        trackType is one of {"audio", "video", "subtitle"}.

        trackIndex is in this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).
        locked
            Track locked or not.

        Returns
        -------
        bool
            True if the track was locked/locked successfully, False otherwise.

        """
        ...

    def GetIsTrackLocked(self, track_type: str, track_index: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is locked and False
        otherwise.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track is locked, False otherwise.

        """
        ...

    def DeleteClips(
        self,
        clips: list[TimelineItem],
        ripple_delete: bool = False,
    ) -> bool:
        """
        Deletes specified TimelineItems from the timeline, performing ripple delete
        if the second argument is True. Second argument is optional (The default for
        this is False).

        Parameters
        ----------
        clips
            TimelineItems to delete. Can be
        ripple_delete
            True if the second argument is True.

        Returns
        -------
        bool
            True if the clips were deleted successfully, False otherwise.

        Notes
        -----
        -   If clip have audio, then DeleteClips will only delete the video (which is
            :class:`TimelineItem`), leaving the audio in the timeline.

        """
        ...

    def SetClipsLinked(self, clips: list[TimelineItem], linked: bool) -> bool:
        """
        Links or unlinks the specified TimelineItems depending on second argument.

        Parameters
        ----------
        clips
            TimelineItems to link/unlink.
        linked
            Link or not.

        Returns
        -------
        bool
            True if the clips were linked/unlinked successfully, False otherwise.

        """
        ...

    def GetItemListInTrack(
        self, track_type: str, track_index: int
    ) -> list[TimelineItem]:
        """
        Returns a list of timeline items on that track (based on trackType and
        trackIndex). 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
                Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        list[TimelineItem]
            Returns a list of TimelineItem on that track.

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

        Parameters
        ----------
        frame_id
            Frame id of the marker. Frame id = Record Frame -
            :func:`dri.timeline.GetStartFrame`.
        color
            Marker color.
        name
            Marker name.
        note
            Marker note.
        duration
            Marker duration.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        bool
            True if the marker was created successfully.

        Notes
        -----
        -   frameId is not source frame, but a Record Frame minus the first frame
            of the current timeline (you can get it through
            :func:`dri.timeline.GetStartFrame`) - 01:00:00:00 (24 fps timeline: 86400,
            25 fps timeline: 90000).
        -   For example: Here is a marker located at record frame 86607. We know that
            current timeline is 24fps, so the first frame is 86400. Here we can get the
            frameId which is 86607 - 86400 = 207.

        """
        ...

    def GetMarkers(self) -> dict[int, dict[str, str | int]]:
        """
        Returns a dict (frameId -> {information}) of all markers and dicts with their
        information.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.

        """
        ...

    def GetMarkerByCustomData(
        self, custom_data: str
    ) -> dict[int, dict[str, str | int]]:
        """
        Returns marker {information} for the first matching marker with specified
        customData.

        Parameters
        ----------
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.


        """
        ...

    def UpdateMarkerCustomData(self, frame_id: int, custom_data: str) -> bool:
        """
        Updates customData (string) for the marker at given frameId position.
        CustomData is not exposed via UI and is useful for scripting developer to
        attach any user specific data to markers.

        Parameters
        ----------
        frame_id
            Frame id of the marker.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        bool
            True if the marker was updated successfully.

        """
        ...

    def GetMarkerCustomData(self, frame_id: int) -> str:
        """
        Returns customData string for the marker at given frameId position.

        Parameters
        ----------
        frame_id
            Frame id of the marker.

        Returns
        -------
        str
            Custom data string.

        """
        ...

    def DeleteMarkersByColor(self, color: MarkerColor | str) -> bool:
        """
        Deletes all timeline markers of the specified color. An "All" argument is
        supported and deletes all timeline markers.

        Parameters
        ----------
        color
            Marker color, passing "All" to it will delete all timeline markers.

        Returns
        -------
        bool
            True if the markers were deleted successfully.

        """
        ...

    def DeleteMarkerAtFrame(self, frame_number: int) -> bool:
        """
        Delete marker at frame number from the media pool item.

        Parameters
        ----------
        frame_number
            Frame id, which is Frame id = Record Frame -
            :func:`dri.timeline.GetStartFrame`.

        Returns
        -------
        bool
            True if the marker was deleted successfully.

        """
        ...

    def DeleteMarkerByCustomData(self, custom_data: str) -> bool:
        """
        Delete first matching marker with specified customData.

        Parameters
        ----------
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        bool
            True if the marker was deleted successfully.

        """
        ...

    def ApplyGradeFromDRX(
        self,
        path: str,
        grade_mode: Literal[0, 1, 2],
        item: TimelineItem,
        *items: TimelineItem
    ) -> bool:
        """
        Loads a still from given file path (string) and applies grade to Timeline
        Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode
        aligned", 2 - "Start Frames aligned".

        Parameters
        ----------
        path
            Path to still file.
        grade_mode
            0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames
            aligned".
        item
            :class:`TimelineItem` to apply grade to.

        Other Parameters
        ----------
        *items
            List of :class:`TimelineItem` to apply grade to.

        Returns
        -------
        bool
            True if the grade was applied successfully.

        """
        ...

    def ApplyGradeFromDRX(
        self, path: str, grade_mode: Literal[0, 1, 2], items: list[TimelineItem]
    ) -> bool:
        """
        Loads a still from given file path (string) and applies grade to Timeline
        Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode
        aligned", 2 - "Start Frames aligned".

        Parameters
        ----------
        path
            Path to still file.
        grade_mode
            0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames
            aligned".
        items
            List of :class:`TimelineItem` to apply grade to.

        Returns
        -------
        bool
            True if the grade was applied successfully.

        """
        ...

    def GetCurrentTimecode(self) -> str:
        """
        Returns a string timecode representation for the current playhead position,
        while on Cut, Edit, Color, Fairlight and Deliver pages.

        Returns
        -------
        str
            Timecode in format "HH:MM:SS:FF".

        """
        ...

    def SetCurrentTimecode(self, timecode: str) -> bool:
        """
        Sets current playhead position from input timecode for Cut, Edit, Color,
        Fairlight and Deliver pages.

        Parameters
        ----------
        timecode
            Playhead position in the timeline to set.

        Returns
        -------
        bool
            True if the timecode was set successfully.

        """
        ...

    def GetCurrentVideoItem(self) -> TimelineItem:
        """
        Returns the current video timeline item.

        Returns
        -------
        TimelineItem
            The current video timeline item.

        """
        ...

    def GetCurrentClipThumbnailImage(self) -> ThumbnailData | dict[str, int | str]:
        """
        Returns a dict (keys "width", "height", "format" and "data") with data
        containing raw thumbnail image data (RGB 8-bit image data encoded in base64
        format) for current media in the Color Page.

        An example of how to retrieve and interpret thumbnails is provided in
        6_get_current_media_thumbnail.py in the Examples folder.

        Returns
        -------
        ThumbnailData | dict
            Dict with raw thumbnail data for current media in the Color Page.

        """
        ...

    def GetTrackName(self, track_type: str, track_index: int) -> str:
        """
        Returns the track name for track indicated by trackType ("audio", "video" or
        "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        str
            Track name.

        """
        ...

    def SetTrackName(self, track_type: str, track_index: int) -> bool:
        """
        Sets the track name (string) for track indicated by trackType ("audio",
        "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track name was set successfully.

        """
        ...

    def DuplicateTimeline(self, new_timeline_name: str) -> "Timeline":
        """
        Duplicates the timeline and returns the created timeline, with the (optional)
        timelineName, on success.

        Parameters
        ----------
        new_timeline_name
            Name of the new timeline. If not specified, the new timeline name will
            append a "copy" to its suffix.

        Returns
        -------
        :class:`Timeline`
            The new timeline after duplication.

        """
        ...

    def CreateCompoundClip(
        self, timeline_items: list[TimelineItem], clip_info: dict[str, str] = None
    ) -> TimelineItem:
        """
        Creates a compound clip of input timeline items with an optional clipInfo
        map: {"startTimecode" : "00:00:00:00", "name" : "Compound Clip 1"}. It
        returns the created timeline item.

        Parameters
        ----------
        timeline_items
            List of timeline items to be composed.
        clip_info
            Optional clipInfo.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def CreateFusionClip(self, timeline_items: list[TimelineItem]) -> TimelineItem:
        """
        Creates a Fusion clip of input timeline items. It returns the created timeline
        item.

        Parameters
        ----------
        timeline_items
            List of timeline items to be composed.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def ImportIntoTimeline(
        self, file_path: str, import_option: ImportOption | dict
    ) -> bool:
        """
        Imports timeline items from an AAF file and optional importOptions dict into
        the timeline, with support for the keys:

        -   "autoImportSourceClipsIntoMediaPool": Bool, specifies if source clips
            should be imported into media pool, True by default

        -   "ignoreFileExtensionsWhenMatching": Bool, specifies if file extensions
            should be ignored when matching, False by default

        -   "linkToSourceCameraFiles": Bool, specifies if link to source camera files
            should be enabled, False by default

        -   "useSizingInfo": Bool, specifies if sizing information should be used,
            False by default

        -   "importMultiChannelAudioTracksAsLinkedGroups": Bool, specifies if
            multichannel audio tracks should be imported as linked groups, False by
            default

        -   "insertAdditionalTracks": Bool, specifies if additional tracks should be
            inserted, True by default

        -   "insertWithOffset": string, specifies insert with offset value in timecode
            format - defaults to "00:00:00:00", applicable if "insertAdditionalTracks"
            is False

        -   "sourceClipsPath": string, specifies a filesystem path to search for source
            clips if the media is inaccessible in their original path and if
            "ignoreFileExtensionsWhenMatching" is True

        -   "sourceClipsFolders": string, list of Media Pool folder objects to search
            for source clips if the media is not present in current folder

        Returns
        -------
        bool
            True if the timeline was imported successfully.

        """
        ...

    def Export(self, file_path: str, export_type: str, export_subtype: str) -> bool:
        """
        Exports timeline to 'fileName' as per input exportType & exportSubtype
        format. Refer to section "Looking up timeline export properties" for
        information on the parameters.

        Parameters
        ----------
        file_path
            Exported timeline destination. Should include file name and extension.
            Such as "/Users/thom/Desktop/export_timeline.aaf".
        export_type
            Export type, refer to the :class:`Resolve` for more information.
        export_subtype
            Export subtype, refer to the :class:`Resolve` for more information.

        Returns
        -------
        bool
            True if the timeline was exported successfully.

        # TODO: Does these notes can be expressed using Python's data structure?
        Notes
        -----
        -   Please note that :param:`exportSubType` is a required parameter for
            :py:data:`resolve.EXPORT_AAF` and :py:data:`resolve.EXPORT_EDL`. For rest
            of the :param:`exportType`, :param:`exportSubType` is ignored.

        -   When exportType is resolve.EXPORT_AAF, valid exportSubtype values are
            resolve.EXPORT_AAF_NEW and resolve.EXPORT_AAF_EXISTING.

        -   When exportType is resolve.EXPORT_EDL, valid exportSubtype values are
            resolve.EXPORT_CDL, resolve.EXPORT_SDL, resolve.EXPORT_MISSING_CLIPS and
            resolve.EXPORT_NONE.

        Examples
        --------
        >>> from dri.resolve import Resolve
        ...
        >>> resolve = Resolve.resolve_init()
        >>> project_manager = resolve.GetProjectManager()
        >>> project = project_manager.GetCurrentProject()
        >>> current_timeline = project.GetCurrentTimeline()
        >>> current_timeline.Export(
        ...     "'/Users/thom/Desktop/timeline.aaf', resolve.EXPORT_AAF, "
        ...     "resolve.EXPORT_AAF_NEW"
        ... )
        True

        """
        ...

    def GetSetting(self, setting_name: str = "") -> str | dict[str, str | float]:
        """
        Returns value of timeline setting (indicated by settingName : string). Check
        the section below for more information.

        Parameters
        ----------
        setting_name
            Timeline setting name. Could be None. If not specified, return all settings
            and their value (string).

        Returns
        -------
        str | dict[str, str | float]
            Value of timeline setting. If settingName is not specified, will return
            all settings and their value (string) which is a dict[str, str | float].

        """
        ...

    def SetSetting(self, setting_name: str, setting_value: str) -> bool:
        """
        Sets timeline setting (indicated by settingName : string) to the value (
        settingValue : string). Check the section below for more information.

        Parameters
        ----------
        setting_name
            Timeline setting name.
        setting_value
            Timeline setting name.

        Returns
        -------
        bool
            True if the setting was set successfully.

        """
        ...

    # TODO: Why some of the generator can't be inserted? It returns None.
    def InsertGeneratorIntoTimeline(self, generator_name: str) -> TimelineItem:
        """
        Inserts a generator (indicated by generatorName : string) into the timeline.

        Parameters
        ----------
        generator_name
            Generator name. What's generator? In the Edit page > Effects > Toolbox >
            Generators.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        Notes
        -----
        -   Not work for "BT.2111 Color Bar HLG Narrow", "BT.2111 Color Bar PQ Full",
            "BT.2111 Color Bar PQ Narrow".

        """
        ...

    # TODO: Not work for all Fusion Generators
    def InsertFusionGeneratorIntoTimeline(self, generator_name: str) -> TimelineItem:
        """
        Inserts a Fusion generator (indicated by generatorName : string) into the
        timeline.

        Parameters
        ----------
        generator_name
            Fusion Generator. What's generator? In the Edit page > Effects > Toolbox >
            Generators.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        Notes
        -----
        -   For all Fusion generator, it has no effect. I have no idea.

        """
        ...

    def InsertFusionCompositionIntoTimeline(self) -> TimelineItem:
        """
        Inserts a Fusion composition into the timeline.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def InsertOFXGeneratorIntoTimeline(self, generator_name: str) -> TimelineItem:
        """
        Inserts an OFX generator (indicated by generatorName : string) into the
        timeline.

        Parameters
        ----------
        generator_name
            OFX generator.

        Returns
        -------
        :class:`TimelineItem`
            Timeline item created.

        """
        ...

    def InsertTitleIntoTimeline(self, title_name: str) -> TimelineItem:
        """
        Inserts a title (indicated by titleName : string) into the timeline.

        Parameters
        ----------
        title_name
            Title name.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def InsertFusionTitleIntoTimeline(self, title_name: str) -> TimelineItem:
        """
        Inserts a Fusion title (indicated by titleName : string) into the timeline.

        Parameters
        ----------
        title_name
            Fusion title.

        Returns
        -------
        :class:`TimelineItem`
            The created timeline item.

        """
        ...

    def GrabStill(self) -> GalleryStill:
        """
        Grabs still from the current video clip. Returns a GalleryStill object.

        Returns
        -------
        :class:`GalleryStill`
            The created :class:`GalleryStill` object.

        """
        ...

    def GrabAllStills(self, still_frame_source: Literal[1, 2]) -> list[GalleryStill]:
        """
        Grabs stills from all the clips of the timeline at 'stillFrameSource' (1 -
        First frame, 2 - Middle frame). Returns the list of GalleryStill objects.

        Parameters
        ----------
        still_frame_source
            Choose grab still from first frame (1) or middle frame (2).

        Returns
        -------
        list[GalleryStill]
            The created :class:`GalleryStill` object.

        """
        ...

    def GetUniqueId(self) -> str:
        """
        Returns a unique ID for the timeline.

        Returns
        -------
        str
            Unique ID for the timeline.

        """
        ...

    def CreateSubtitlesFromAudio(self) -> bool:
        """
        Creates subtitles from audio for the timeline. Returns True on success,
        False otherwise.

        Returns
        -------
        bool
            True if subtitles were created successfully.

        """
        ...

    def DetectSceneCuts(self) -> bool:
        """
        Detects and makes scene cuts along the timeline. Returns True if successful,
        False otherwise.

        Returns
        -------
        bool
            True if scene cuts were detected successfully.

        """
        ...