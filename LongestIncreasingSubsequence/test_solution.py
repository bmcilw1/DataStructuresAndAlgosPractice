from LongestIncreasingSubsequence.solution import Solution

def test_sol_whenPassedOneNumber_returnsOne():
    assert Solution.lengthOfLIS([1]) == 1
