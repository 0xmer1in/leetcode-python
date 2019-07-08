# Author: Merlin

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'

        num1 = [ord(item) - ord('0') for item in num1]
        num2 = [ord(item) - ord('0') for item in num2]
        l1, l2 = len(num1), len(num2)
        n1, n2 = 0, 0

        for item in num1:
            n1 += item * 10 ** (l1 - 1)
            l1 -= 1

        for item in num2:
            n2 += item * 10 ** (l2 - 1)
            l2 -= 1

        return str(n2 * n1)