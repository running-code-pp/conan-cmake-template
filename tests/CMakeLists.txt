# Find GTest (required for unit tests)
find_package(GTest REQUIRED)

# Collect all .cc files in the tests directory
file(GLOB TEST_FILES CONFIGURE_DEPENDS "*.cc")

# Combine test files and source files to be tested
set(TEST_SOURCES ${TEST_FILES} ${SOURCE_FILES})

# Create test executable
add_executable(test_runner ${TEST_SOURCES})

# Link against GTest (test_main.cc provides main() function)
target_link_libraries(test_runner PRIVATE
    GTest::GTest
)

# Set output directory (optional, for consistency)
set_target_properties(test_runner PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Register with CTest
add_test(
    NAME test_runner
    COMMAND $<TARGET_FILE:test_runner>
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)