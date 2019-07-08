# 状态转移方程 dp[m][i] = dp[m - 1][i - 1] + dp[m - 1][i] + 1
# m代表可扔的次数，i代表鸡蛋数

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0, 0]
        m = 0
        while dp[-1] < N:
            for i in range(len(dp)-1, 0, -1):
                dp[i] += dp[i - 1] + 1
            if len(dp) < K + 1:
                dp.append(dp[-1])
            m += 1
        return m

# time: O(m * k)
# space: O(K)