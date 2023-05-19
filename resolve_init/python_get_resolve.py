#!/usr/bin/env python

"""
This file serves to return a DaVinci Resolve object
"""
import importlib.util
import sys
import os


def GetResolve():
    try:
        # The PYTHONPATH needs to be set correctly for this import statement to work.
        # An alternative is to import the DaVinciResolveScript by specifying absolute
        # path (see ExceptionHandler logic)
        from resolve_init import DaVinciResolveScript as bmd
    except ImportError:
        if sys.platform.startswith("darwin"):
            expected_path = (
                "/Library/Application Support/Blackmagic Design/DaVinci "
                "Resolve/Developer/Scripting/Modules/"
            )
        elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
            expected_path = (
                os.getenv("PROGRAMDATA") + "\\Blackmagic Design\\DaVinci "
                "Resolve\\Support\\Developer\\Scripting\\Modules\\"
            )
        elif sys.platform.startswith("linux"):
            expected_path = "/opt/resolve/libs/Fusion/Modules/"

        # check if the default path has it...
        print(
            "Unable to find module DaVinciResolveScript from $PYTHONPATH - trying "
            "default locations"
        )
        try:
            spec = importlib.util.spec_from_file_location(
                "DaVinciResolveScript", f"{expected_path}DaVinciResolveScript.py"
            )
            bmd = importlib.util.module_from_spec(spec)
        except ImportError:
            # No fallbacks ... report error:
            print(
                "Unable to find module DaVinciResolveScript - please ensure that the "
                "module DaVinciResolveScript is discoverable by python"
            )
            print(
                f"For a default DaVinci Resolve installation, the module is expected "
                f"to be located in: {expected_path}"
            )
            sys.exit()

    return bmd.scriptapp("Resolve")