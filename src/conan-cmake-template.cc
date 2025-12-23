#include <iostream>
#include <string>
#include "conan-cmake-template.h"

namespace conan_cmake_template
{

  App::App() : version_("1.0.0")
  {
  }

  App::~App() = default;

  void App::Run()
  {
    std::cout << "Hello World from Conan CMake Template!" << std::endl;
  }

  std::string App::GetVersion() const
  {
    return version_;
  }

} // namespace conan_cmake_template
