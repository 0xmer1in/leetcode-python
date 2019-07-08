from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x not in nums:
                y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
        return best