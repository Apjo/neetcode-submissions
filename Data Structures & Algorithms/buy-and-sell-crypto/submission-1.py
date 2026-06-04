class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,prev = 0,prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prev:
                profit = max(prices[i] - prev, profit)
            else:
                # prev=prices[]
            
                prev = prices[i]
        return profit