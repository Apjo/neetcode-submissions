class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(index):
            if index >= len(s):
                return True
            if index in memo:
                return memo[index]
            for k in range(index, len(s)):
                if s[index : k + 1] in wordDict and solve(k + 1):
                    memo[index] = True
                    return True
            memo[index]=False
            return False
        memo={}
        return solve(0)
        