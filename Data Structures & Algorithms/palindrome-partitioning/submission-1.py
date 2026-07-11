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
        
        def solve(input_s, buff, res):
            if not input_s:
                # print(f"Appending to final res...")
                res.append(buff[:])
                # print(f"Currently final res={res}")
                return
            for i in range(1, len(input_s) + 1):
                curr_substr = input_s[0 : i]
                # print(f"At i={i}, curr substr={curr_substr}")
                if not is_palindrome(curr_substr):
                    continue
                buff.append(curr_substr)
                # print(f"curr buff={buff}")
                solve(input_s[i : ], buff, res)
                buff.pop()
        res,buff = [], []
        solve(s, buff, res)
        return res