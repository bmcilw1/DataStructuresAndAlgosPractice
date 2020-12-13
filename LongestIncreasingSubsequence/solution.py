#!/usr/bin/env python3

class Solution:
    def lengthOfLongestIncreasingSubsequence(self, nums: list[int]) -> int:
        N = len(nums)
        lis = [1] * (N + 1)

        for idx, n in enumerate(nums, start=1):
            subs = []

            for idx_sub in range(0, idx):
                if nums[idx_sub] < n:
                    subs.append(lis[idx_sub])

            lis[idx] = 1 + max(subs, default=0)

        return max(lis, default=0)
