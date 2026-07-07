class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # curr is smaller than min -> update min
        # curr is greater than min -> update profit
        profit = 0
        minPrice = float('inf')

        for price in prices:
            minPrice = min(price, minPrice)
            profit = max(profit, price - minPrice)

        return profit
