#!/usr/bin/env python3

class Solution:
    def lengthOfLongestIncreasingSubsequence(self, nums: list[int]) -> int:
        lis = [1] * len(nums) 

        for idx in range(0, len(nums)):
            subs = []

            for idx_sub in range(0, idx):
                if nums[idx_sub] < nums[idx]:
                    subs.append(lis[idx_sub])

            lis[idx] = 1 + max(subs, default=0)

        return max(lis, default=0)
