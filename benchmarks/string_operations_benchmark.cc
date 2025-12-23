#include <benchmark/benchmark.h>
#include <string>
#include <sstream>

// Simple benchmark to test string concatenation performance
static void BM_StringConcatenation(benchmark::State &state)
{
  for (auto _ : state)
  {
    std::string result;
    for (int i = 0; i < state.range(0); ++i)
    {
      result += "test";
    }
    benchmark::DoNotOptimize(result);
  }
}
BENCHMARK(BM_StringConcatenation)->Range(1, 1024);

// Benchmark for string stream operations
static void BM_StringStream(benchmark::State &state)
{
  for (auto _ : state)
  {
    std::ostringstream oss;
    for (int i = 0; i < state.range(0); ++i)
    {
      oss << "test" << i;
    }
    std::string result = oss.str();
    benchmark::DoNotOptimize(result);
  }
}
BENCHMARK(BM_StringStream)->Range(1, 1024);

BENCHMARK_MAIN();