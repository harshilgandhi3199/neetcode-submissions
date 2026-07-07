class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        n = len(prices)
        for i in range(1, n):
            for j in range(i):
                diff = prices[i] - prices[j]
                profit = max(profit, diff)

        return profit