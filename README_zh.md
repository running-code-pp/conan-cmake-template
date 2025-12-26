[English](README.md) | 中文

# Conan CMake Template

一个集成conan包管理 和 现代cmake 的 C++项目模板

# 特性
- conan2
- morden cmake
- vscode 配置集成

# 使用

## 先决条件

- cmake 3.22+
- conan 2.0+
- vscode
- vscode cmake cmake tools 插件

## 使用

- 克隆代码
- 修改根目录下的CMakeUserPresets.json 在include中选择cmakeuserpresets目录下对应编译器的预设
- 在终端运行以下命令
```bash
cd conan-cmake-template
conan install . --build=missing --output-folder=build --settings=build_type=[Debug|Release]
code .
```
-  选择conan-defaul预设

# 待做
- 集成 github actions 实现CICD模板
- 兼容多种生成模板:执行文件/动态库/静态库
- 给代码自动添加开源许可证的脚本