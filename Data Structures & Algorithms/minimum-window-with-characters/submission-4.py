class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if t is empty return ""
        if s == t:
            return s
        if t == "":
            return ""
        #build a frequency map of t
        freq_t = {}
        for cc in t:
            freq_t[cc] = freq_t.get(cc, 0) + 1
        #init 2 variables, have=0, and need=len(frequency map for t) to demonstrate how many distinct chars we need from t in s
        have, need, left = 0, len(freq_t), 0
        freq_s = {}
        res_str=[-1,-1]
        res=float("infinity")
        freq_s={}
        #iterate over the string s
        for i in range(len(s)):
            #prepare a frequency map of each character in s
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            #if the character in s is in T, and frequency matches, increment have
            if s[i] in freq_t and freq_s[s[i]] == freq_t[s[i]]:
                have+=1
            #while have == need loop
            while have == need:
                if i - left + 1 < res:
                    res_str=[left, i]
                    res = i - left + 1
                    
                #decrement the frequency of character at left by 1
                freq_s[s[left]]-=1
                #if the character at left is in dictT, and its frequency in s < frequency in T:
                if s[left] in freq_t and freq_s[s[left]] < freq_t[s[left]]:
                    #decrement have by 1 since we got the expected num of this character
                    have-=1
                #increment left pointer by 1
                left+=1
        left, i = res_str
        #return the substring between left and right pointers in s
        return s[left: i + 1] if res != float("infinity") else ""