from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        rot = l
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            mid = (l + r) // 2
            realmid = (mid + rot) % n
            if nums[realmid] == target: return realmid
            elif nums[realmid] < target: l = mid + 1
            else: r = mid - 1
        return -1