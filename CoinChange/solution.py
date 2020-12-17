#!/usr/bin/env python3

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        self.coins = set(coins)
        self.min_coin = min(coins)
        self.calculated_change = {}
        self.calculated_change[0] = 0
        return self.change(amount)

    def change(self, amount: int) -> int:
        if amount in self.calculated_change:
            pass
        elif amount < self.min_coin:
            self.calculated_change[amount] = -1
        else:
            min_change = float('inf')
            for coin in self.coins:
                change_less_coin = 1 + self.change(amount - coin)
                if change_less_coin > 0 and change_less_coin < min_change:
                    min_change = change_less_coin

            self.calculated_change[amount] = -1 if min_change == float('inf') else min_change

        return self.calculated_change[amount]
