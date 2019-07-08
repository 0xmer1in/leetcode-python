class Solution:
    def threeSum(self, nums):
        # 第一种解法，利用c = -(a+b)
        if len(nums): return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]: continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x)) # 此处可以改成 res.add([v, -v-x, x]) , 对应下面也要修改
        return list(map(list, res)) # 此处对应上面应修改成 return list(res)


        # 第二种解法，左边和右边同时向内移动
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1; r -= 1
        return res
