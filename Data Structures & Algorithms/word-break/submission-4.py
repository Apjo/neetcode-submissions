class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp =[False]*(len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            "k asks: Can I find a valid previous boundary such that the piece from k to i is a dictionary word?"
            for k in range(i):
                if s[k : i] in wordDict and dp[k]:
                    dp[i] = True
        return dp[len(s)]
        