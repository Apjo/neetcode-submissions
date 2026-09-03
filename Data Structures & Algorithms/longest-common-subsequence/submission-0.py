class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Follow edit distance trick
        if s[i]!=t[j]
            mismatch, or deletion, or replacement we incur 0 cost
        else:
            since there is a match we add +1 to this case
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + X)
        '''
        if text1 == text2:
            return len(text1)
        M, N = len(text1), len(text2)
        dp=[[0 for _ in range(N + 1)] for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
                else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[M][N]    

