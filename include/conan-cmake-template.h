#ifndef INCLUDE_CONAN_CMAKE_TEMPLATE_H_
#define INCLUDE_CONAN_CMAKE_TEMPLATE_H_

#include <string>

namespace conan_cmake_template
{

  // This class represents the main application
  class App
  {
  public:
    App();
    ~App();

    // Runs the application
    void Run();

    // Returns the current version of the application
    std::string GetVersion() const;

  private:
    std::string version_;
  };

} // namespace conan_cmake_template

#endif // INCLUDE_CONAN_CMAKE_TEMPLATE_H_
