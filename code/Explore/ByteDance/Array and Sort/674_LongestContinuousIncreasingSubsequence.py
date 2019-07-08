from typing import List


# Author: Merlin
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        count, max = 1, 0
        n = len(nums)
        for i in range(n):
            if 0 < i < n and nums[i - 1] < nums[i]:
                count += 1
            else:
                count = 1
            if max < count: max = count
        return max