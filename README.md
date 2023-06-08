[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Introduction

Dri is a type system that aims to provide auto-completion, type annotation, and static type checking for developing
scripts using DaVinci Resolve API. It packages all APIs according to the latest README and adds well-formatted
docstrings (using NumPy style, referencing the [Colour](https://github.com/colour-science/colour) project) and detailed
type hints to help understand the types of parameters accepted by each API and their return value types. This is
particularly important and useful during development when there is only one README file as reference.

If you don't know what return type of API, just `Cmd+B` (PyCharm) or `F12` (VS Code) to go to declaration, or hover
over the function (API) to see well formatted docstring and type hints.

It has the following characteristics:

- It completely replicates the signature of the original API, and strictly follows the original parameters, function
  overloading, return type, etc. as stated in the DaVinci Resolve API README.
- All docstrings are based on the latest DaVinci Resolve 18.5 Beta 1 README. I will update it regularly.
- It's just a dev dependency, or you can think of it as an interface. When you're done with the dev, you can delete it
  and the code will work fine in DaVinci Resolve. Because it uses the exact same signature as the original API.

# Similar Project

- [pybmd](https://github.com/WheheoHu/pybmd)