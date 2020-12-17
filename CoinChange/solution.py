#!/usr/bin/env python3

class Solution:
    coins = set()

    def coinChange(self, coins: list[int], amount: int) -> int:
        self.coins = set(coins)
        return self.change(amount)

    def change(self, amount: int) -> int:
        if amount == 0:
            return 0
        elif amount in self.coins:
            return 1
        return -1
