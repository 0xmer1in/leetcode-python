from typing import List


class Solution_1:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[count] = nums[i]
                if count != i:
                    nums[i] = 0
                count += 1


class Solution_2:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for i, n in enumerate(filter(lambda x: x, nums)):
            nums[i] = n
        for i in range(i + 1, len(nums)):
            nums[i] = 0


class Solution_3:
    def moveZeroes(self, nums: List[int]) -> None:
        def gen(nums):
            """手动实现上面解法的filter"""
            for x in nums:
                if x:
                    yield x

        i = 0
        for i, n in enumerate(gen(nums)):
            nums[i] = n
        for i in range(i + 1, len(nums)):
            nums[i] = 0


class Solution_4:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=bool, reverse=True)