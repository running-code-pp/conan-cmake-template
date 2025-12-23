#!/usr/bin/env python3
#
# Conan CMake Template - Compiler Detection Script
#
# This script detects available compilers on the system and updates VSCode configuration
# to use the appropriate compiler for the current platform.
#
import os
import sys
import json
import subprocess
import platform
from pathlib import Path


def find_all_compilers():
    """Find all available compilers on the system"""
    compilers = []

    # Find MSVC on Windows
    if platform.system() == "Windows":
        msvc_path = find_msvc()
        if msvc_path:
            compilers.append((msvc_path, "windows-msvc-x64", "MSVC Compiler"))

    # Find GCC
    gcc_path = find_gcc()
    if gcc_path:
        if platform.system() == "Windows":
            compilers.append((gcc_path, "windows-gcc-x64", "GCC Compiler"))
        elif platform.system() == "Darwin":
            compilers.append((gcc_path, "macos-gcc-x64", "GCC Compiler"))
        else:  # Linux
            compilers.append((gcc_path, "linux-gcc-x64", "GCC Compiler"))

    # Find Clang
    clang_path = find_clang()
    if clang_path:
        if platform.system() == "Windows":
            compilers.append(
                (clang_path, "windows-clang-x64", "Clang Compiler"))
        elif platform.system() == "Darwin":
            compilers.append((clang_path, "macos-clang-x64", "Clang Compiler"))
        else:  # Linux
            compilers.append((clang_path, "linux-clang-x64", "Clang Compiler"))

    # Add default paths if no compilers found
    if not compilers:
        if platform.system() == "Windows":
            compilers.append(
                ("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe", "windows-msvc-x64", "Default MSVC"))
        elif platform.system() == "Darwin":
            compilers.append(
                ("/usr/bin/clang++", "macos-clang-x64", "Default Clang"))
        else:  # Linux
            compilers.append(("/usr/bin/g++", "linux-gcc-x64", "Default GCC"))

    return compilers


def select_compiler():
    """Allow user to select a compiler from available options"""
    compilers = find_all_compilers()

    if len(compilers) == 1:
        print(f"Found one compiler: {compilers[0][2]} at {compilers[0][0]}")
        return compilers[0][0], compilers[0][1]

    print("Available compilers:")
    for i, (path, mode, name) in enumerate(compilers):
        print(f"{i+1}. {name}: {path}")

    while True:
        try:
            choice = input(f"Select a compiler (1-{len(compilers)}): ")
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(compilers):
                return compilers[choice_idx][0], compilers[choice_idx][1]
            else:
                print(f"Please enter a number between 1 and {len(compilers)}")
        except (ValueError, IndexError):
            print(
                f"Please enter a valid number between 1 and {len(compilers)}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            sys.exit(1)


def find_msvc():
    """Find MSVC compiler on Windows"""
    if platform.system() != "Windows":
        return None

    # Try to find MSVC via common paths
    import glob
    common_paths = [
        "C:/Program Files/Microsoft Visual Studio/*/Community/VC/Tools/MSVC/*/bin/Hostx64/x64/cl.exe",
        "C:/Program Files (x86)/Microsoft Visual Studio/*/Community/VC/Tools/MSVC/*/bin/Hostx64/x64/cl.exe",
        "C:/Program Files/Microsoft Visual Studio/*/Professional/VC/Tools/MSVC/*/bin/Hostx64/x64/cl.exe",
        "C:/Program Files (x86)/Microsoft Visual Studio/*/Professional/VC/Tools/MSVC/*/bin/Hostx64/x64/cl.exe",
        "C:/Program Files/Microsoft Visual Studio/*/Enterprise/VC/Tools/MSVC/*/bin/Hostx64/x64/cl.exe",
        "C:/Program Files (x86)/Microsoft Visual Studio/*/Enterprise/VC/Tools/MSVC/*/bin/Hostx64/x64/cl.exe",
    ]

    for pattern in common_paths:
        matches = glob.glob(pattern)
        if matches:
            # Return the most recent version
            return sorted(matches, key=os.path.getctime)[-1]

    return None


def find_gcc():
    """Find GCC compiler"""
    possible_names = ["g++", "g++-11", "g++-10",
                      "g++-9", "g++-8", "gcc", "g++"]
    for name in possible_names:
        try:
            result = subprocess.run(
                [name, "--version"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                # Verify it's actually GCC
                if "Free Software" in result.stdout or "gcc" in result.stdout.lower():
                    return name
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            continue
    return None


def find_clang():
    """Find Clang compiler"""
    possible_names = ["clang++", "clang++-14",
                      "clang++-13", "clang++-12", "clang++-11", "clang"]
    for name in possible_names:
        try:
            result = subprocess.run(
                [name, "--version"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                # Verify it's actually Clang
                if "clang" in result.stdout.lower():
                    return name
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            continue
    return None


def update_vscode_config():
    """Update the VSCode configuration with selected compiler"""
    # Get project root (parent of scripts directory)
    project_root = Path(__file__).parent.parent
    c_cpp_properties_path = project_root / ".vscode" / "c_cpp_properties.json"
    settings_path = project_root / ".vscode" / "settings.json"

    # Select compiler
    compiler_path, intelli_sense_mode = select_compiler()

    # Determine configuration name based on platform
    system = platform.system()
    if system == "Windows":
        name = "Windows"
    elif system == "Darwin":
        name = "macOS"
    else:
        name = "Linux"

    # Create c_cpp_properties.json configuration
    c_cpp_config = {
        "configurations": [
            {
                "name": name,
                "includePath": [
                    "${workspaceFolder}/**",
                    "${workspaceFolder}/include",
                    "${workspaceFolder}/src",
                    "${command:cmake.getLaunchTargetDirectory}"
                ],
                "defines": [],
                "intelliSenseMode": intelli_sense_mode,
                "compilerPath": compiler_path,
                "cStandard": "c17",
                "cppStandard": "c++20"
            }
        ],
        "version": 4
    }

    # Read existing settings.json if it exists, otherwise create default
    if settings_path.exists():
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings_config = json.load(f)
    else:
        settings_config = {
            "files.associations": {},
            "C_Cpp.intelliSenseEngine": "default",
            "C_Cpp.default.cppStandard": "c++20",
            "C_Cpp.errorSquiggles": "enabled",
            "C_Cpp.dimInactiveRegions": false,
            "C_Cpp.intelliSense.maxMemory": 4096,
            "C_Cpp.exclusionPolicy": "checkFolders",
            "C_Cpp.default.compilerArgs": [
                "/std:c++20",
                "/await",
                "/permissive-"
            ],
            "cmake.buildDirectory": "${workspaceFolder}/build"
        }

    # Update the compiler path in settings.json
    settings_config["C_Cpp.default.compilerPath"] = compiler_path

    # Ensure .vscode directory exists
    c_cpp_properties_path.parent.mkdir(exist_ok=True)

    # Write the configurations
    with open(c_cpp_properties_path, 'w', encoding='utf-8') as f:
        json.dump(c_cpp_config, f, indent=4)

    with open(settings_path, 'w', encoding='utf-8') as f:
        json.dump(settings_config, f, indent=4)

    print(f"VSCode configurations updated for {system}")
    print(f"Compiler selected: {compiler_path}")
    print(f"IntelliSense mode: {intelli_sense_mode}")
    print(f"Updated both c_cpp_properties.json and settings.json")


def main():
    """Main function to run the detection and update process"""
    print("Detecting compilers and updating VSCode configuration...")

    try:
        update_vscode_config()
        print("Configuration updated successfully!")
    except Exception as e:
        print(f"Error updating configuration: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
