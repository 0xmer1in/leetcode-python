from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 动态规划DP
        if not triangle: return 0

        res = triangle[-1]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # 这种技术处理，又称状态压缩
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]