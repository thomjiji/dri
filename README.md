# Quickstart

```py
from dri import Resolve

resolve = Resolve.resolve_init()
project_manager = resolve.GetProjectManager()
project = project_manager.GetCurrentProject()
media_storage = resolve.GetMediaStorage()
media_pool = project.GetMediaPool()
root_folder = media_pool.GetRootFolder()
current_timeline = project.GetCurrentTimeline()
```

# After development using Dri

If your script intends to use outside of DaVinci Resolve (running from terminal), replace the imports below

```python
from dri import Resolve

resolve = Resolve.resolve_init()
```

with:

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
```

If your script intends to use inside DaVinci Resolve, replace it with:

```python
resolve = bmd.scriptapp("Resolve")
```

# Notes

## Headless DaVinci Resolve

`cd` into `/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/MacOS/`, run:

```
./Resolve -nogui
```

It will run in the background without GUI, block current tty (terminal session), output
some logs in the stdout.

# License

[MIT](LICENSE)
