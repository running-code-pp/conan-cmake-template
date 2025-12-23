#include <iostream>
#include "conan-cmake-template.h"

namespace {

void PrintPlatformInfo() {
#ifdef WIN32
  std::cout << "Running on Windows platform" << std::endl;
#elif defined(LINUX_PLATFORM)
  std::cout << "Running on Linux platform" << std::endl;
#elif defined(APPLE_PLATFORM)
  std::cout << "Running on Apple platform" << std::endl;
#else
  std::cout << "Running on unknown platform" << std::endl;
#endif
}

}  // namespace

int main() {
  conan_cmake_template::App app;
  app.Run();

  std::cout << "Project version: " << app.GetVersion() << std::endl;
  PrintPlatformInfo();

  return 0;
}

