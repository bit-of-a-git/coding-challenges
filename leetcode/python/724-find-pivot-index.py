from typing import List


class Solution:
    def pivotIndexNaive(self, nums: List[int]) -> int:
        lenNums = len(nums)
        for i in range(lenNums):
            sumLeft = sum(nums[:i])
            sumRight = sum(nums[i + 1 :])
            if sumLeft == sumRight:
                return i
        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        # We sum once for efficiency
        sumNums = sum(nums)
        # This holds the sum of every number to the left
        leftSum = 0

        for idx, num in enumerate(nums):
            if leftSum == (sumNums - leftSum - num):
                return idx
            leftSum += num
        return -1
