class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        N,left,ans=len(s),0,0

        for i in range(N):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
            while left < i and freq[s[i]] > 1:
                freq[s[left]]-=1
                left+=1
            ans=max(ans, i-left + 1)
        return ans