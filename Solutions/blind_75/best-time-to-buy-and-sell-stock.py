# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Brute force
# O(n^2) time --> (n-2)/2 | O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

# Sliding Windows
# O(n) time | O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left == buy, right == sell
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # new lowest "buy"
                left = right
            right += 1
        return max_profit