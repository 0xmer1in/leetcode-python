# time : O(n)
# space : O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return s
        _list = [""] * numRows
        for i in range(len(s)):
            index = i % (2 * numRows - 2)
            index = index if index < numRows else 2 * numRows - 2 - index
            _list[index] += s[i]
        return ''.join(_list)