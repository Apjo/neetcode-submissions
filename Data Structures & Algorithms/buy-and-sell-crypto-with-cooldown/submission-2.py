class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        ans = float("-inf")
        #at each index i we decide to buy or not buy.
        #But, if you buy at i - 1 cannot buy at i, but can buy at i + 1
        def solve(idx, buying):
            if idx >= N:
                return 0
            if (idx, buying) in memo:
                return memo[(idx, buying)]
            #always compute "cooldown" effect
            cooldown = solve(idx + 1, buying)
            # memo[(idx, buying)] = cooldown
            if buying:
                #buy this at i, and then move to i+2
                a = solve(idx+1, not buying) - prices[idx]
                memo[(idx, buying)] = max(a, cooldown)
                return max(a, cooldown)
            else:
                #sell this at i with a profit!
                b = solve(idx + 2, not buying) + prices[idx]
                memo[(idx, buying)] = max(b, cooldown)
                return max(b, cooldown)
            
        memo={}
        return solve(0, True)
        # return ans