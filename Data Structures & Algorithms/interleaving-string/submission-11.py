class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        L, M, N = len(s3), len(s1), len(s2)
        
        dp = [[False for _ in range(N + 1)] for _ in range(M + 1)]
        dp[0][0] = True
        # case1: we have non empty s1, and an empty s2, we check if first i characters from s1 match first i chars in s3
        for i in range(1, M +1):
            dp[i][0] = dp[i - 1][0] and s3[i - 1]==s1[i - 1]
        # case2: we have non empty s2, and an empty s1, we check if first j characters from s2 match first j chars in s3
        for j in range(1, N + 1):
            dp[0][j] = dp[0][j-1] and s3[j - 1] == s2[j - 1]
        for i in range(1, M + 1):
            for j in range(1, N+1):
                dp[i][j] = (
                    dp[i][j - 1]
                    and s3[i + j - 1] == s2[j - 1]
                    or dp[i-1][j]
                    and s3[i + j - 1] == s1[i - 1]
                )
        return dp[M][N]
        