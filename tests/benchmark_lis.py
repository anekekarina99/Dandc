import sys
import os
import timeit

# Tambahkan path ke lis_library
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lis_library')))

from lis import LongestIncreasingSubsequence  # Pastikan impor ini benar

# Fungsi wrapper untuk metode calculate_lis
def benchmark_calculate_lis():
    sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis = LongestIncreasingSubsequence(sequence)
    lis.calculate_lis()

# Fungsi wrapper untuk metode find_lis
def benchmark_find_lis():
    sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis = LongestIncreasingSubsequence(sequence)
    lis.find_lis()

if __name__ == "__main__":
    # Benchmarking calculate_lis
    calculate_lis_time = timeit.timeit(benchmark_calculate_lis, number=100)
    print(f"calculate_lis: {calculate_lis_time:.5f} seconds")

    # Benchmarking find_lis
    find_lis_time = timeit.timeit(benchmark_find_lis, number=100)
    print(f"find_lis: {find_lis_time:.5f} seconds")
