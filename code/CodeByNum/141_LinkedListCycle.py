# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# HashMap
# time: O(n) space: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashMap = {}
        while head:
            if head in hashMap:
                return True
            else:
                hashMap[head] = 1
        return False


# fast and slow pointers
# time: O(n) space: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False