[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

# Introduction

Dri is a type system that aims to provide auto-completion, type annotation, and static type checking for developing
scripts using DaVinci Resolve API. It packages all APIs according to the latest README and adds well-formatted
docstrings (using NumPy style, referencing the [Colour](https://github.com/colour-science/colour) project) and detailed
type hints to help understand the types of parameters accepted by each API and their return value types. This is
particularly important and useful during development when there is only one README file as reference.

If you don't know what return type of API, just `Cmd+B` (PyCharm) or `F12` (VS Code) to go to declaration, or hover
over the function (API) to see well formatted docstring and type hints.

It has the following characteristics:

- It faithfully duplicates the signature of the original API, adhering strictly to the original parameters, function
  overloading, return type, and other specifications outlined in the DaVinci Resolve API README.
- All docstrings are derived from the most recent DaVinci Resolve 18.5 Beta 4 README and will be consistently updated.
- It serves solely as a development dependency or an interface. Once development is complete, you are free to remove it,
  and the code will continue to function seamlessly in DaVinci Resolve since it employs the identical
  signature as the original API.

# Similar Project

- [pybmd](https://github.com/WheheoHu/pybmd)

# Run Tests

```shell
pytest -v
```

By default, pytest captures the output produced by your tests and displays it only if the test fails. However, when you
use `--capture=no` or `-s`, pytest allows the stdout and stderr to be displayed on the console immediately, regardless
of the test result.

```shell
pytest -v -s
```

# After development using Dri

If your script intends to use outside DaVinci Resolve, then replace the import below

```python
from dri import Resolve

resolve = Resolve.resolve_init()
```

with:

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
```

If your script intends to use inside DaVinci Resolve, replace with:

```python
resolve = bmd.scriptapp("Resolve")
```