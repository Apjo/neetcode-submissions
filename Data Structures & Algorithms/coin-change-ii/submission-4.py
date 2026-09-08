class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        ways = [[0] * (amount + 1) for _ in range(N + 1)]
        #there is only 1 ways to make 0 amount with >=0 coins
        for i in range(N + 1):
            ways[i][0] = 1
        #there is no way to make an amount > 0 using 0 coins
        for coin in range(1, N + 1):
            for amt in range(1, amount+1):
                curr_coin_value = coins[coin - 1]
                # print(f"coin num={coin}, current coin value={curr_coin_value}, amount={amt}")
                if amt - coins[coin - 1] >= 0:
                    # print(f"coin num={coin}, current coin value={coins[coin - 1]}, amount={amt}, target={amt - coins[coin - 1]}")
                    ways[coin][amt] = ways[coin][amt - coins[coin - 1]] + ways[coin - 1][amt]
                else:
                    ways[coin][amt] = ways[coin - 1][amt]
        # print(f"final output table={ways}")
        return ways[N][amount]
        