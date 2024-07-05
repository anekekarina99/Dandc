import sys
import os
import cProfile
import pstats
import io

# Tambahkan path ke lis_library
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lis_library')))

from lis import LongestIncreasingSubsequence  # Pastikan impor ini benar

def profile_lis():
    # Contoh data
    sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis = LongestIncreasingSubsequence(sequence)
    
    # Profiling metode calculate_lis
    cProfile.runctx('lis.calculate_lis()', globals(), locals(), 'profile_calculate_lis.prof')
    
    # Profiling metode find_lis
    cProfile.runctx('lis.find_lis()', globals(), locals(), 'profile_find_lis.prof')

    # Membaca hasil profiling
    for profile in ['profile_calculate_lis.prof', 'profile_find_lis.prof']:
        s = io.StringIO()
        ps = pstats.Stats(profile, stream=s)
        ps.strip_dirs().sort_stats(pstats.SortKey.TIME).print_stats(10)
        print(s.getvalue())

if __name__ == "__main__":
    profile_lis()
