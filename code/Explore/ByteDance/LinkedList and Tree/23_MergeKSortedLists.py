from queue import PriorityQueue
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 这个和下面的解法一样，但这个代码清楚
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        dummy = curr= ListNode(None)
        for list_idx, node in enumerate(lists):
            if node: q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next


# 这种代码更简洁
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(None)
        q = PriorityQueue()
        for idx, node in enumerate(lists):
            if node: q.put((node.val, idx, node))
        while not q.empty():
            _, idx, curr.next = q.get()
            curr = curr.next
            if curr.next: q.put((curr.next.val, idx, curr.next))
        return dummy.next
