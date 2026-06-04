class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[0]*26
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')]+=1
        for i in range(len(t)):
            arr[ord(t[i]) - ord('a')]-=1
        return all(item == 0 for item in arr)