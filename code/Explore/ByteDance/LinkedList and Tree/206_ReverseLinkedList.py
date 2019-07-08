# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# iterative
# time: O(n) space: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next  # 正确
            # cur.next, cur, prev = prev, cur.next, cur  正确
            # prev, cur, cur.next = cur, cur.next, prev  报错
            # cur, cur.next, prev = cur.next, prev, cur  报错
        return prev

# recursive
# time: O(n) space: O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)