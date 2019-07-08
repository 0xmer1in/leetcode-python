'''template of dynamic programming'''
# 状态定义
# dp = new int [m + 1][n + 1];

# 初始状态
# dp[0][0] = x;
# dp[0][1] = y;
# ...

# DP状态的推导
'''
for  i = 0; i <= n; ++i {
    for j = 0; j <= m; ++j {
        ...

        dp[i][j] = min {dp[i - 1][j], dp[i][j - 1], etc.}
    }
}
'''

# return dp[m][n]; 最优解