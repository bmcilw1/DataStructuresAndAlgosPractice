#!/usr/bin/env python3

import copy

class Solution:
    def _partition(self, nums: list[int], start: int, end: int, pivot: int) -> int:
        i = start
        nums[pivot], nums[end] = nums[end], nums[pivot]
        pivot = end

        for j in range (start, end):
            if nums[j] < nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[pivot], nums[i] = nums[i], nums[pivot]

        return i

    def _quickSort(self, nums: list[int], start: int, end: int):
        if (end < start):
            return

        pivot = (end - start) // 2 + start

        pivot_position = self._partition(nums, start, end, pivot)
        self._quickSort(nums, start, pivot_position-1)
        self._quickSort(nums, pivot_position+1, end)

    def quickSort(self, nums: list[int]) -> list[int]:
        copy_nums = copy.deepcopy(nums)
        self._quickSort(copy_nums, 0, len(nums) - 1)
        return copy_nums
