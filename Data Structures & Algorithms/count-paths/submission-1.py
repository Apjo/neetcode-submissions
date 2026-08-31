class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # print(dp)
        dp[0][0]=1
        for i in range(1, m + 1):
            # dp[i][0] = dp[i - 1][0] + 1
            dp[i][0] = 1
        for i in range(1, n + 1):
            # dp[0][i] = dp[0][i - 1] + 1
            dp[0][i] = 1
        # print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j] + dp[i][j - 1]
        
        return dp[m -1][n - 1]
