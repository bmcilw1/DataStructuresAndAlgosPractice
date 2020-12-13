#!/usr/bin/env python3

from LongestIncreasingSubsequence.solution import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


class TestSolution:
    def test_lengthOfLIS_whenPassedOneNumber_returnsOne(self, solution):
        assert solution.lengthOfLIS([8]) == 1

    def test_lengthOfLIS_exampleOne(self, solution):
        assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_lengthOfLIS_exampleTwo(self, solution):
        assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4

    def test_lengthOfLIS_exampleThree(self, solution):
        assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
