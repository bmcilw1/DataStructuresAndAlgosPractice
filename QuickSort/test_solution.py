#!/usr/bin/env python3

from QuickSort.solution import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


class TestSolution:
    def test_quickSort_singleItem(self, solution):
        assert solution.quickSort([8]) == [8]

    def test_quickSort_duplicateItems(self, solution):
        assert solution.quickSort([8, 0, 8]) == [0, 8, 8]

    def test_quickSort_fewItems(self, solution):
        assert solution.quickSort([8, 0, 3]) == [0, 3, 8]

    def test_quickSort_moreItems(self, solution):
        assert solution.quickSort([8, 7, 0, 2, 3, 4]) == [0, 2, 3, 4, 7, 8]
