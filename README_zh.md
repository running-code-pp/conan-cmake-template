[English](README.md) | 中文

# Conan CMake 模板

一个使用 Conan 和 CMake 构建的跨平台 C++ 项目模板。

遵循 Google C++ 风格

## 特性

- 现代 CMake (3.22+)
- Conan 包管理
- 跨平台构建支持 (Windows, Linux, macOS)
- Google Test 集成
- Google Benchmark 集成
- 标准项目结构
- 即用型构建配置
- VSCode 自动编译器检测

## 先决条件

- CMake 3.22+
- Conan 2.0+
- 支持 C++20 的编译器
- Python 3.6+ (用于编译器检测脚本)

## 快速开始

1. 安装 Conan 依赖:
   ```bash
   conan install . --build=missing -s build_type=Release
   ```

2. 配置项目:
   ```bash
   cmake . --preset conan-release
   # 或者 Debug 构建
   conan install . --build=missing -s build_type=Debug
   cmake . --preset conan-debug
   ```

3. 构建项目:
   ```bash
   cmake --build --preset conan-release
   # 或
   cmake --build --preset conan-debug
   ```

4. 运行测试:
   ```bash
   ctest --preset conan-release
   ```

5. (可选) 更新 VSCode 编译器配置:
   ```bash
   python scripts/detect.py
   ```

## 项目结构

```
├── CMakeLists.txt          # 主 CMake 配置
├── conanfile.txt           # Conan 依赖
├── README.md
├── README_zh.md            # 中文说明
├── .gitignore
├── scripts/                # 工具脚本
│   └── detect.py           # 编译器检测脚本
├── include/                # 公共头文件
│   └── conan_cmake_template.h
├── src/                    # 源文件
│   ├── main.cc
│   └── conan-cmake-template.cc
├── tests/                  # 单元测试
│   ├── CMakeLists.txt
│   └── test_main.cpp
├── benchmarks/             # 基准测试文件
│   ├── CMakeLists.txt
│   └── string_operations_benchmark.cc
└── .vscode/                # VS Code 设置
    ├── c_cpp_properties.json
    ├── launch.json
    └── tasks.json
```

## Conan 集成

项目使用 Conan 进行依赖管理。依赖项在 `conanfile.txt` 中定义，并通过 `CMakeDeps` 和 `CMakeToolchain` 生成器与 CMake 集成。

## 跨平台支持

CMake 配置包括特定于平台的选项和编译器标志，以在不同操作系统之间实现最大程度的兼容性。

## 编译器检测

`scripts/detect.py` 脚本自动检测系统上可用的最佳编译器，并相应地更新 VSCode 配置。运行此脚本以使用适合您平台的正确编译器路径更新 `.vscode/c_cpp_properties.json` 文件。

使用编译器检测脚本：

1. 确保系统上已安装 Python 3.6+
2. 运行检测脚本：
   ```bash
   python scripts/detect.py
   ```
3. 脚本将扫描可用的编译器（MSVC、GCC、Clang）并显示列表供您选择
4. 脚本将使用您选择的编译器更新 `.vscode/c_cpp_properties.json` 和 `.vscode/settings.json`

这确保了 IntelliSense 和其他 VSCode C++ 功能能与您系统的编译器正常工作。

## 不同配置的构建

对于多配置生成器（如 Windows 上的 Visual Studio），您可以指定构建类型：

```bash
cmake --build . --config Release
# 或
cmake --build . --config Debug
```