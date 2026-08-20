class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                #len == 1
                if i == j:
                    dp[i][j] = True
                #len==2
                elif j == i + 1:
                    dp[i][j] = s[i] == s[j]
                #len > 2
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j]:
                    ans+=1

        return ans