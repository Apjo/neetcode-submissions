class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = float("inf")
        memo={}
        def solve(T, idx):
            if idx >= len(coins):
                if T != 0:
                    memo[(T, idx)] = float("inf")
                    return memo[(T, idx)]
                if T == 0:
                    memo[(T, idx)] = 0
                    return memo[(T, idx)]
            
            if T < 0:
                memo[(T, idx)] = float("inf")
                return memo[(T, idx)]

            if T == 0:
                #0 num coins required to reach from idx to T since we acheived the target
                memo[(T, idx)] = 0
                return memo[(T, idx)]
            
            if (T, idx) in memo:
                return memo[(T, idx)]
            else:
                memo[(T, idx)] = float("inf")
            # if you pick this coin, since there are infinite denominations, we can just stay here, and continue down this path where we keep on picking this coin at idx itself, and decrementing T by coins[idx] value, till we either reach a 0 where we found the min number of coins required, or we reach a -1 where we would never be able to reach the target.
            a = solve(T - coins[idx], idx) + 1
            b = solve(T, idx + 1)
            if a and b:
                #min number of coins required from idx to reach T
                memo[(T, idx)] = min(a, b)
                
            return memo[(T, idx)]
        
        val = solve(amount, 0)
        
        return val if val != float("inf") else -1
        
        