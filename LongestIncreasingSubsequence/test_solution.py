#!/usr/bin/env python3

from solution import Solution

@pytest.fixture()
def solution():
    yield Solution()

class TestSolution:
    def test_lengthOfLIS_whenPassedOneNumber_returnsOne(self, solution):
        assert solution.lengthOfLIS([1]) == 1
