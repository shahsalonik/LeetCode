class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_prof = max(max_prof, profit)
            else:
                left = right
            right += 1

        return max_prof