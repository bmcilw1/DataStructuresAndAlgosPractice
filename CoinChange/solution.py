#!/usr/bin/env python3

class Solution:
    coins = set()
    past_change = dict()

    def coinChange(self, coins: list[int], amount: int) -> int:
        self.coins = set(coins)
        return self.change(amount)

    def change(self, amount: int) -> int:
        if amount in self.past_change:
            return self.past_change[amount]

        if amount == 0:
            self.past_change[amount] = 0
        elif amount in self.coins:
            self.past_change[amount] = 1
        else:
            self.past_change[amount] = -1

        return self.past_change[amount]
