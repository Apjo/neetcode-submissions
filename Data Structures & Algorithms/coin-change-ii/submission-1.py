class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins:
            return 0
        res, buff = [], []
        memo={}
        N = len(coins)
        def solve(T, idx):
            if T == 0:
                memo[(T, idx)] = 1
                return memo[(T, idx)]
            
            if T < 0 or idx >= N:
                return 0

            if (T, idx) in memo:
                return memo[(T, idx)]

            a = solve(T - coins[idx], idx)
            b = solve(T, idx + 1)
            memo[(T, idx)] = a + b

            return memo[(T, idx)]

        return solve(amount, 0)

