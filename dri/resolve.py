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
    IP_ADDRESS = "127.0.0.1"
    APP_NAME = "Resolve"

    def __init__(self, resolve_ip=IP_ADDRESS):
        self.resolve = self.resolve_init(resolve_ip)

    def resolve_init(self, ip):
        bmd_module = load_dynamic_lib()
        resolve = bmd_module.scriptapp(self.APP_NAME, ip)
        return resolve

    def Fusion(self):
        """
        Returns the Fusion object. Starting point for Fusion scripts.

        """
        ...

    def GetProjectManager(self) -> ProjectManager:
        ...

    def GetMediaStorage(self) -> MediaStorage:
        ...