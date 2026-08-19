class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longest_str_ans = ""
        if N <=1:
            return s
        
        def expand_str(l:int, ri:int):
            while l >=0 and ri < len(s) and s[l] == s[ri]:
                l-=1
                ri+=1
            return s[l + 1 : ri]

        for i in range(N - 1):
            #expand from current char for all odd len strings
            odd_len = expand_str(i, i)
            #expand from current, and current + 1 character for all even len strings
            even_len = expand_str(i, i + 1)
            if len(odd_len) > len(longest_str_ans):
                longest_str_ans = odd_len
            if len(even_len) > len(longest_str_ans):
                longest_str_ans = even_len
        
        return longest_str_ans
        