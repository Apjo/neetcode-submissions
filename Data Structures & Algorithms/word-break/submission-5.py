class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp =[False]*(len(s) + 1)
        dp[0] = True
        '''
        i: where we're currently ending the string we're trying to build.
        k: where the last word starts.
        s[k:i] = the last word we're considering
        and, dp[k] = can everything before that last word be broken into valid words?
        So when you're calculating dp[i], you're basically asking:
"Can I find a place k where the last word starts, such that everything before k works AND s[k:i] is a word?"
    leet | code
         ↑     ↑
         k     i
         4     8
         k = 4 → "code" starts here
         i = 8 → "code" ends here
         s[4:8] → "code"
         dp[4] → tells you whether "leet" can be broken successfully
        '''
        for i in range(len(s) + 1):
            "k asks: Can I find a valid previous boundary such that the piece from k to i is a dictionary word?"
            for k in range(i):
                if s[k : i] in wordDict and dp[k]:
                    dp[i] = True
        return dp[len(s)]
        