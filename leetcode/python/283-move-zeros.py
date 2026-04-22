from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        lenNums = len(nums)
        for right in range(lenNums):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
