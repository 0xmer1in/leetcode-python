from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, x in enumerate(prices):
            if i == len(prices) - 1: return profit
            if x < prices[i+1]:
                profit += prices[i+1] - x
        return profit