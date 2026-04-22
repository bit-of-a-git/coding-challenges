from typing import List


class Solution:
    def minStartValueNaive(self, nums: List[int]) -> int:
        prefixSum = []
        runningTotal = 0
        for i in nums:
            runningTotal += i
            prefixSum.append(runningTotal)
        minPrefix = min(prefixSum)
        if minPrefix <= 0:
            return 1 + abs(minPrefix)
        else:
            return 1

    def minStartValue(self, nums: List[int]) -> int:
        minVal = 0
        runningTotal = 0
        for i in nums:
            runningTotal += i
            minVal = min(minVal, runningTotal)
        return 1 + abs(minVal)
