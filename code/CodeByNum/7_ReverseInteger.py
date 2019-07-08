class Solution_1:
    def reverse(self, x: int) -> int:
        temp = x
        x = x if x >= 0 else -x
        x = str(x)
        x = x[::-1]
        x.split('0')
        x = x if temp >= 0 else '-' + x
        x = int(x)
        if x < -2 ** 31 or x > 2 ** 31 - 1: return 0
        return x

import sys

class Solution_2:
    def reverse(self, x: int) -> int:
        res = 0
        while not x == 0:
            res = res * 10 + x % 10
            x = x // 10
            if res > sys.maxsize or res < -sys.maxsize: return 0
        return res
