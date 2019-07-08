class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = curr = ListNode(None)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return root.next

# divmod()函数返回一个包含商和余数元组(a // b, a % b)