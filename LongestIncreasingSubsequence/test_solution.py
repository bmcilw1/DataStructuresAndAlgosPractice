#!/usr/bin/env python3

from LongestIncreasingSubsequence.solution import Solution

class TestSolution:
    def test_lengthOfLIS_whenPassedOneNumber_returnsOne(self):
        solution = Solution()
        assert solution.lengthOfLIS([1]) == 1
