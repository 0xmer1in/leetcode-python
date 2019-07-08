# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# reference: https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation
# time: O(n) space: O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow, fast = head, head.next
            while fast is not slow:
                slow = slow.next
                fast = fast.next
        except:
            return None

        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        return head