class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1

        while buy < sell and sell < len(prices):
            # in the case that it's a profitable transaction
            print(prices[buy], prices[sell])
            if prices[buy] <= prices[sell]:
                diff = prices[sell] - prices[buy]
                max_profit = max(diff, max_profit)
            else:
                buy = sell
            sell += 1
            
        return max_profit