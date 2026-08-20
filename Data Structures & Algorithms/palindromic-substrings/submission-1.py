class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def expand(le, ri):
            nonlocal ans
            while le >= 0 and ri < len(s) and s[le] == s[ri]:
                ans+=1
                le-=1
                ri+=1

        for i in range(len(s)):
            #for odd len strings expand from center i.e. i
            expand(i, i)
            # for even len strings expand from i, and i + 1
            expand(i, i + 1)
        
        return ans
        