cmake_minimum_required(VERSION 3.22)
project(conan-cmake-template)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Conan integration
include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake OPTIONAL)


# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Find Conan packages
find_package(benchmark REQUIRED)
find_package(GTest REQUIRED)

# Define library source files (excluding main.cpp)
set(LIB_SOURCES
    src/conan-cmake-template.cpp
)

# Define source files
set(SOURCES
    src/main.cc
    src/conan-cmake-template.cc
)


# Define the main executable
add_executable(${PROJECT_NAME} ${SOURCES})

# Link libraries to the executable
if(TARGET benchmark::benchmark)
    target_link_libraries(${PROJECT_NAME} PRIVATE benchmark::benchmark)
endif()

if(TARGET GTest::GTest)
    target_link_libraries(${PROJECT_NAME} PRIVATE GTest::GTest GTest::Main)
endif()



# Set include directories
target_include_directories(${PROJECT_NAME}
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${CMAKE_CURRENT_SOURCE_DIR}/include
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# Platform-specific configurations
if(WIN32)
    # Windows-specific settings
    target_compile_definitions(${PROJECT_NAME} PRIVATE WIN32_LEAN_AND_MEAN NOMINMAX)
    if(MSVC)
        target_compile_options(${PROJECT_NAME} PRIVATE /W4)
    endif()
elseif(UNIX)
    # Unix-like systems (Linux, macOS)
    if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
        target_compile_options(${PROJECT_NAME} PRIVATE -Wall -Wextra -Wpedantic)
        
        # Platform-specific definitions
        if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
            target_compile_definitions(${PROJECT_NAME} PRIVATE LINUX_PLATFORM)
        elseif(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
            target_compile_definitions(${PROJECT_NAME} PRIVATE APPLE_PLATFORM)
        endif()
    endif()
endif()

# Create an install target
install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Enable testing if GTest is available
enable_testing()
add_subdirectory(tests)

# Add benchmarks if in development mode
option(BUILD_BENCHMARKS "Build benchmark executables" ON)
if(BUILD_BENCHMARKS)
    add_subdirectory(benchmarks)
endif()

