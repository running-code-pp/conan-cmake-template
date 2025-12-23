[English](README.md) | [中文](README_zh.md)

# Conan CMake Template

A cross-platform C++ project template built with Conan and CMake.

fllow google c++ style

## Features

- Modern CMake (3.22+)
- Conan package management
- Cross-platform build support (Windows, Linux, macOS)
- Google Test integration
- Google Benchmark integration
- Standard project structure
- Ready-to-use build configuration
- Automatic compiler detection for VSCode

## Prerequisites

- CMake 3.22+
- Conan 2.0+
- C++20 compatible compiler
- Python 3.6+ (for compiler detection script)

## Getting Started

1. Install Conan dependencies:
   ```bash
   conan install . --build=missing -s build_type=Release
   ```

2. Configure the project:
   ```bash
   cmake . --preset conan-release
   # or for Debug build
   conan install . --build=missing -s build_type=Debug
   cmake . --preset conan-debug
   ```

3. Build the project:
   ```bash
   cmake --build --preset conan-release
   # or
   cmake --build --preset conan-debug
   ```

4. Run tests:
   ```bash
   ctest --preset conan-release
   ```

5. (Optional) Update VSCode compiler configuration:
   ```bash
   python scripts/detect.py
   ```

## Project Structure

```
├── CMakeLists.txt          # Main CMake configuration
├── conanfile.txt           # Conan dependencies
├── README.md
├── .gitignore
├── scripts/                # Utility scripts
│   └── detect.py           # Compiler detection script
├── include/                # Public headers
│   └── conan_cmake_template.h
├── src/                    # Source files
│   ├── main.cc
│   └── conan-cmake-template.cc
├── tests/                  # Unit tests
│   ├── CMakeLists.txt
│   └── test_main.cpp
├── benchmarks/             # Benchmark files
│   ├── CMakeLists.txt
│   └── string_operations_benchmark.cc
└── .vscode/                # VS Code settings
    ├── c_cpp_properties.json
    ├── launch.json
    └── tasks.json
```

## Conan Integration

The project uses Conan for dependency management. Dependencies are defined in `conanfile.txt` and integrated with CMake through the `CMakeDeps` and `CMakeToolchain` generators.

## Cross-Platform Support

The CMake configuration includes platform-specific options and compiler flags for maximum compatibility across different operating systems.

## Compiler Detection

The `scripts/detect.py` script automatically detects the best available compiler on your system and updates the VSCode configuration accordingly. Run this script to update your `.vscode/c_cpp_properties.json` file with the correct compiler path for your platform.

To use the compiler detection script:

1. Make sure Python 3.6+ is installed on your system
2. Run the detection script:
   ```bash
   python scripts/detect.py
   ```
3. The script will scan for available compilers (MSVC, GCC, Clang) and present a list for you to choose from
4. The script will update both `.vscode/c_cpp_properties.json` and `.vscode/settings.json` with your selected compiler

This ensures that IntelliSense and other VSCode C++ features work properly with your system's compiler.

## Building with Different Configurations

For multi-configuration generators (like Visual Studio on Windows), you can specify the build type:

```bash
cmake --build . --config Release
# or
cmake --build . --config Debug
```

