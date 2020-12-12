#!/usr/bin/env python3

from LongestIncreasingSubsequence.solution import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


class TestSolution:
    def test_lengthOfLIS_whenPassedOneNumber_returnsOne(self, solution):
        assert solution.lengthOfLIS([8]) == 1
