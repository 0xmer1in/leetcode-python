from typing import List

class Solution_1:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        # 用字典来存储次数，time:O(n), space:O(n)
        dic = {}
        max = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            if dic[num] > max:
                max = dic[num]
                res = num
        return res


class Solution_2:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        # 用快排解决
        list = nums
        list.sort()
        return list[len(nums) // 2]
