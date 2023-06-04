import importlib.util

from .folder import Folder
from .media_pool_item import MediaPoolItem
from .media_pool import MediaPool


def load_dynamic_lib():
    spec = importlib.util.spec_from_file_location(
        "fusionscript",
        "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so",
    )
    bmd_module = importlib.util.module_from_spec(spec)

    return bmd_module


def resolve_init():
    bmd_module = load_dynamic_lib()
    resolve = bmd_module.scriptapp("Resolve")
    return resolve