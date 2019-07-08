from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        size = pre = 0
        cur = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = cur[j]
                if not i or not j or matrix[i][j] == '0':
                    cur[j] = int(matrix[i][j]) - 0
                else:
                    cur[j] = min(pre, min(cur[j], cur[j - 1])) + 1
                size = max(cur[j], size)
                pre = temp
        return size * size