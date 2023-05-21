[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Introduction

Dri is a type system that aims to provide auto-completion, type annotation, and static type checking for developing
scripts using DaVinci Resolve API. It packages all APIs according to the latest README and adds well-formatted
docstrings (using NumPy style, referencing the [Colour](https://github.com/colour-science/colour) project) and detailed type hints to help understand the types of
parameters accepted by each API and their return value types. This is particularly important and useful during
development when there is only one README.txt file as reference.

When developing scripts using DaVinci Resolve API, I often encounter a problem where I don’t know which object a method
belongs to or what the return type of function should be. This requires me to trace back where a value comes from and
then go back to the README.txt to find out what the return value of an API is and what type it is. This process is
cumbersome and does not conform to our usual development habits. In addition, there was no auto-completion for the API.

So I made this repo to overcome. If you don't know what return type of API, just `Cmd+B` (PyCharm) or `F12` (VS Code) to
go to declaration, or hover over the function (API) to see well formatted docstring and type hints.

It has the following characteristics:

- It completely replicates the signature of the original API, and strictly follows the original parameters, function
  overloading, return type, etc. as stated in the DaVinci Resolve API README.
- All docstrings are based on the latest DaVinci Resolve 18.5 Beta 1 README. I will update it regularly.

# Similar Project

- [pybmd](https://github.com/WheheoHu/pybmd)

# Misc

- DaVinci Resolve object (MediaPoolItem, TimelineItem, etc.) type annotation
- API 的 calling 方式与原始完全一样，该接受一个 str 作为 arg 就接受 str。
- 这个库只是达芬奇 API 的一个 interface，所以遇到需要 overload 一个 function 的情况，我们可以直接 pass 掉，直接声明两个同名的
  function，不用去管 overload。达芬奇 API 内部已经处理好了 overload。