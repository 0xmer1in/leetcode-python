from typing import List


"""
    Dynamic Programming
    @author: Merlin 2019.05.05
    53.Maximum Subarray
    思路: 定义以第i个元素作为结尾的最大子数组和为dp[i]，从状态转移方程可以得出以第i+1个元素作为结尾的最大子数组和
    1.如果dp[i-1]大于0，那么加上nums[i]肯定大于nums[i]，这里用dp[i-1] + nums[i]
    2.如果dp[i-1]小于0，加上nums[i]会使子数组小于nums[i]自身，所以这里直接用0 + nums[i]
    3.状态转移方程: dp[i] = dp[i - 1] > 0 ? dp[i - 1] : 0 + nums[i];(三元表达式)
    time: O(n) space: O(n)
    reference: https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        _max = dp[0]
        for i in range(1, len(nums)):
            temp = dp[i-1] if dp[i-1] > 0 else 0
            dp.append(nums[i] + temp)
            _max = max(_max, dp[i])
        return _max

"""
    更简洁的写法
    time: O(n) space: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum = _max = nums[0]
        for i in range(1, len(nums)):
            _sum = nums[i] if _sum < 0 else _sum + nums[i]
            if _sum > _max: _max = _sum
        return _max