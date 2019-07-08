class Solution_1:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = a + b, a
        return a


class Solution_2:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        nums = [0] * (n + 1)
        nums[1] = 1
        nums[2] = 2
        for i in range(3, n + 1):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n]


class Solution_3(object):
    def climbStairs(self, n):
        if n == 1: return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]


"""
    对于改版题的思考: 能走1步，2步，3步，不能连续走同样的步数 nums[n][m] 表示走到n阶，
    nums[0][0] = 1
    nums[1][1] = 1
    nums[2][2] = 2
    nums[3] = 能走1/2 2/1 不能走1/1/1 dp方程为 nums[n][m] = nums[n-3][!m] + nums[n-2][!m] + nums[n-1][!m]
    dp[3][2] = dp[3-1]
    
    dp[i]= max(dp[i-1], dp[i-2]+nums[i]) + max(dp[i-1], dp[i-3]+nums[i] )+max(dp[i-2],dp[i-3]+nums[i])+1
"""