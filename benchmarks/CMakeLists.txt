# Benchmark executable
find_package(benchmark REQUIRED)

# Define benchmark source files
set(BENCHMARK_SOURCES
    string_operations_benchmark.cc
)

add_executable(benchmark_runner ${BENCHMARK_SOURCES})

# Link libraries to benchmark executable
target_link_libraries(benchmark_runner PRIVATE 
    benchmark::benchmark
    benchmark::benchmark_main
)
