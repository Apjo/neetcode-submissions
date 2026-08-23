class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        #min number of coins to make amount A from coins 0 to i - 1
        dp=[[float("inf") for _ in range(N + 1)] for _ in range(amount + 1)]
        #for making amount 0 for any coins=0 we need 0 coins
        for i in range(N + 1):
            dp[0][i] = 0
        #for making an amount > 0 from 0 coins there are impossible number of ways i.e. INF
        for i in range(1, amount + 1):
            dp[i][0] = float("inf")
        
        for am in range(1, amount + 1):
            for coin_index in range(1, N + 1):
                # print(f"checking for amount={am}, and coin index={coin_index}")
                if am - coins[coin_index - 1] >= 0:
                    dp[am][coin_index] = min(dp[am][coin_index - 1], dp[am - coins[coin_index - 1]][coin_index] + 1)
                else:
                    dp[am][coin_index] = dp[am][coin_index - 1]
        
        
        return -1 if dp[amount][N] == float("inf") else dp[amount][N]
        