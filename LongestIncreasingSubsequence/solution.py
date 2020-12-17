#!/usr/bin/env python3

class Solution:
    def lengthOfLongestIncreasingSubsequence(self, nums: list[int]) -> int:
        return self.lengthOfLongestIncreasingSubsequence_n_squared(nums)

    def lengthOfLongestIncreasingSubsequence_n_squared(self, nums: list[int]) -> int:
        lis = [1] * len(nums)

        for i in range(1, len(nums)):
            prior_LIS_with_num_less_than_i = [
                lis[j] for j in range(i) if nums[j] < nums[i]]
            lis[i] = 1 + max(prior_LIS_with_num_less_than_i, default=0)

        return lis[-1]