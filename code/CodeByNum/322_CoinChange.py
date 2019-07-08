from typing import List


"""
    @author: Merlin 2019.06.02
    322.Coin Change
    思路:
    1.首先声明一个大小为amount+1的数组dp，用dp[i]存储"对于金额i最少用的硬币数"
        _1.首先解释为什么大小是amount+1，比如amount是11块，dp要从0元开始存储到11块，所以数组的大小要amount+1
        _2.对于初始化数组dp的索引i=0的元素值为0，是因为0块要的硬币数为0，所以初始化为0
    2.根据数组dp的定义，得到方程: dp[i] = min(dp[i-coin]+1)
        _1.注意这里的dp[i-coin]的coin是针对每一种硬币(在代码里遍历了coins数组)
    3.返回值的解释
        _1.dp[amount]返回dp数组的最后一个元素，dp[amount] == float("inf")返回dp数组最后的元素是否为inf(无穷大)
        _2.这里用一个例子解释[3, -1][True]返回的是索引为1的元素，[3, -1][False]返回索引为0的元素
        _3.所以dp[amount]不等于inf则返回dp[amount]，等于inf则返回-1，意味着任何一种硬币组合能组成总金额
    time: O(amount*len(coins) 第一层循环遍历了amount次，第二层循环遍历了数组coins的每个元素
    space: O(amount) 算法用一个大小为amount+1的数组来存储值
    
    https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else float("inf") for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == float('inf')]



if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    test = Solution()
    res = test.coinChange(coins, amount)