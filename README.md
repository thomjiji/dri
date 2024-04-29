[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

# Quickstart

```py
from dri.resolve import Resolve

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

# Run Tests

```shell
pytest -v
```

By default, pytest captures the output produced by your tests and displays it only if
the test fails. However, when you use `--capture=no` or `-s`, pytest allows the stdout
and stderr to be displayed on the console immediately, regardless of the test result.

```shell
pytest -v -s
```

# License

[LGPLv3](LICENSE)
