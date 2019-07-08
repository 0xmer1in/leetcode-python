"""
    deque 双边队列
    @author: Merlin
    思路: 利用双边队列可以先进先出也可以先进后出的特点，当i大于等于k时，每次遍历都要检查边界
    1.下一个元素比窗口中最大的元素大时，pop出所有元素并append这个元素
    2.每次append进window的是下标，最后append进res的是值即可
    time: O(n) space: O(1)
"""
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res