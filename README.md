[English](README.md) | [中文](README_zh.md)

# Conan CMake Template

A C++ project template integrating Conan package management and modern CMake.

## Features

- Conan 2.0+
- Modern CMake
- VSCode configuration integration

## Usage

## Prerequisites

- CMake 3.22+
- Conan 2.0+
- VSCode
- VSCode CMake and CMake Tools extensions

## Usage

- Clone the repository
- Modify CMakeUserPresets.json in the root directory and select the corresponding compiler preset from the cmakeuserpresets directory in the include section
- Run the following commands in the terminal:

```bash
cd conan-cmake-template
conan install . --build=missing --output-folder=build --settings=build_type=[Debug|Release]
code .
```

- Select the conan-default preset
