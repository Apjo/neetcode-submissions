class Solution:
    def numDecodings(self, s: str) -> int:
            def solve(idx):
                if idx == 0:
                    if s[idx] == "0":
                        return 0
                    else:
                        return 1
                if idx < 0:
                    return 1
                # idx is no longer a 0, but we can have a 0 anywhere, and we shouldn't be treating as a valid 1 digit
                one_d = 0
                
                if idx in memo:
                    return memo[idx]
                
                if s[idx] != "0":
                    one_d = solve(idx - 1)

                curr = int(s[idx]) - int("0")
                prev = int(s[idx - 1]) - int("0")
                f_num = int(str(prev) + "" + str(curr))

                two_d = 0
                #the number has to be a valid between 10-26
                if 10 <= f_num <= 26:
                    two_d = solve(idx - 2)

                memo[idx] = one_d + two_d
                
                return memo[idx]
            
            memo={}
            return solve(len(s) - 1)
        