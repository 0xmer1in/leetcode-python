from typing import List


# TODO AC the problem
# reference: https://leetcode.com/problems/utf-8-validation/discuss/87478/Simplest-Python-Solution
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0

        for byte in data:
            if byte >= 128 and byte <= 191:
                if not count:
                    return False
                count -= 1
            else:
                if count:
                    return False
                if byte < 128:
                    continue
                elif byte < 224:
                    count = 1
                elif byte < 240:
                    count = 2
                elif byte < 248:
                    count = 3
                else:
                    return False

        return count == 0