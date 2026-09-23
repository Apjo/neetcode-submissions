class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        ans=[[0] *(N + 1) for _ in range(M + 1)]
        #to go from an empty word to an non-empty word
        for i in range(1, M+1):
            ans[i][0] = i

        #to go from an non-empty word to an empty word
        for i in range(1, N+1):
            ans[0][i] = i

        for i in range(1, M+1):
            for j in range(1, N+1):
                ans[i][j] = min(ans[i-1][j] + 1,
                                ans[i][j-1] + 1,
                                ans[i-1][j-1] + (0 if word1[i-1]==word2[j-1] else 1))
        return ans[M][N]