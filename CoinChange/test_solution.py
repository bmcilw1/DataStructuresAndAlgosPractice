#!/usr/bin/env python3

from CoinChange.solution import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


class TestSolution:
    def test_coinChange_noSolution(self, solution):
        assert solution.coinChange([2], 3) == -1

    def test_coinChange_zeroChange(self, solution):
        assert solution.coinChange([2], 0) == 0

    def test_coinChange_exactChange(self, solution):
        assert solution.coinChange([2], 2) == 1

    def test_coinChange_onesOnly(self, solution):
        assert solution.coinChange([1], 2) == 2

    def test_coinChange_mixedBag(self, solution):
        assert solution.coinChange([1,2,5], 11) == 3