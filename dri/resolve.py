import importlib.util

from dri.media_storage import MediaStorage
from dri.project_manager import ProjectManager


def load_dynamic_lib():
    spec = importlib.util.spec_from_file_location(
        "fusionscript",
        "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so",
    )
    bmd_module = importlib.util.module_from_spec(spec)

    return bmd_module


class Resolve:
    def __init__(self):
        self.resolve = self.resolve_init()

    @staticmethod
    def resolve_init():
        bmd_module = load_dynamic_lib()
        resolve = bmd_module.scriptapp("Resolve")
        return resolve

    def Fusion(self):
        """
        Returns the Fusion object. Starting point for Fusion scripts.

        """
        # return self.resolve.Fusion()
        ...

    def GetProjectManager(self) -> ProjectManager:
        ...
        # return ProjectManager(self.resolve)

    def GetMediaStorage(self) -> MediaStorage:
        # return self.resolve.GetMediaStorage()
        ...