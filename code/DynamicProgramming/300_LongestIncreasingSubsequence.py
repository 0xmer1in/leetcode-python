from typing import List


"""
    @author: Merlin 2019.06.02
    300.Longest Increasing Subsequence
    思路:
    1.tails[i]的作用: 存储所有长度为i+1的递增子序列中，最小的序列尾数
        以nums = [4, 5, 6, 3]为例子:
        length = 1 : [4], [5], [6], [3] => tails[0] = 3
        length = 2 : [4, 5], [5, 6]     => tails[1] = 5
        length = 3 : [4, 5, 6]          => tails[2] = 6
        以这种方式存储的tails是一个递增的数组，因为tails数组是有序的，所以可以用二分查找去找到要更新的元素
    2.更新的情况有两种:
        _1.当前遍历的元素大于tails数组里的所有元素，将该元素append进去并将数组容量加1(这点上Python是自动扩容，也可以像代码里手动创建具体大小的数组)
        _2.如果当前遍历的元素x处于这种情况: tails[i-1] < x <= tails[i]，就要更新tails[i]， 把tails[i]的值改为x
    3.以上述方式维护的tails的数组长度就是最长上升子序列(代码里用size来替代数组大小)
    time: O(nlogn) 遍历nums的每个元素为O(n)，嵌套二分查找去更新元素为O(logn)，所以时间复杂度为O(nlogn)
    space: O(n) 算法里用创建时tails指定了和nums一样的大小，所以空间复杂度为O(n)
    
    https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    test = Solution()
    test.lengthOfLIS(nums)