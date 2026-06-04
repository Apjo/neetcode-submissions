class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        N = len(s)
        ans,max_repeating_char_count,left = 0,0,0
        for i in range(N):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
            max_repeating_char_count = max(max_repeating_char_count, freq[s[i]])
            win_size = i - left + 1
            num_chars_to_keep = win_size - max_repeating_char_count
            if left <= i and num_chars_to_keep > k:
                freq[s[left]]-=1
                left+=1
            ans=max(ans, i - left + 1)
        return ans