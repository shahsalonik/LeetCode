class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        smallest = 0
        largest = 1
        while largest < len(prices):
            diff = prices[largest] - prices[smallest]
            if diff > 0:
                max_diff = max(diff, max_diff)
            else:
                smallest = largest
            largest += 1
        return max_diff