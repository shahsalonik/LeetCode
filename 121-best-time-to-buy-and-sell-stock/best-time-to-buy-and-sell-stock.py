class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_buying = prices[0]

        for sell in prices:
            max_prof = max(max_prof, sell - min_buying)
            min_buying = min(min_buying, sell)
        return max_prof