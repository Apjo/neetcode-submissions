class Solution:
    def checkValidString(self, s: str) -> bool:
        o,c,st = 0,0,0
        # if s[0] == ')':
        #     return False
        # for i in s:
        #     if i == "(":
        #         o+=1
        #     if i==")":
        #         c+=1
        #     if i=="*":
        #         st+=1
            
        # if st == 0:
        #     return o == c
        # d = abs(o - c)
        # return st >= d
        open, star = [], []
        for i in range(len(s)):
            if s[i] == '(':
                # o+=1
                open.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while open and star:
            if open[-1] < star[-1]:
                open.pop()
                star.pop()
            else:
                return False
        return not open