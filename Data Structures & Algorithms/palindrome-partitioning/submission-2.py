class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s) -> bool:
            lo, hi = 0, len(s) - 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo+=1
                hi-=1
            return True
        
        def solve(idx, input_s, buff, res):
            if idx >= len(input_s):
                # print(f"Appending to final res...")
                res.append(buff[:])
                # print(f"Currently final res={res}")
                return
            for i in range(idx, len(input_s)):
                #we try every possible end index=idx from i to end:
                curr_substr = input_s[idx : i+1]
                print(f"At i={i}, curr substr={curr_substr}")
                if not is_palindrome(curr_substr):
                    continue
                buff.append(curr_substr)
                print(f"curr buff={buff}")
                solve(i+1, input_s, buff, res)
                buff.pop()
        res,buff = [], []
        solve(0, s, buff, res)
        return res