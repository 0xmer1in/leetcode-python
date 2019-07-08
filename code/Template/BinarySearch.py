"""
    二分查找的条件(二分查找有局限性)
    1.Sorted(在一个有序的数组里，单调递增或者递减)
    2.Bounded(存在上下界)
    3.Accessible by index(能够通过索引访问)
    通过条件分析得知，链表是非常不适合二分查找而数组非常适合
"""

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            # fine the target!!
            # break or return result
            return
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
"""
    实战题目
    1.https://leetcode.com/problems/sqrtx/
      https://www.beyond3d.com/content/articles/8(拓展阅读)
    2.https://leetcode.com/problems/valid-perfect-square/
"""