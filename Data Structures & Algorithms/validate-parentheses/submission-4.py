class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for cc in s:
            if cc in ['(', '[', '{']:
                print("pushing to stk")
                stk.append(cc)
                print(stk)
            else:
                if stk:
                    curr = stk[-1]
                    if (cc == ')' and curr == '(') or (cc == ']' and curr == '[') or (cc == '}' and curr == '{'):
                        stk.pop()
                    else:
                        return False
                else:
                    return False
        return len(stk)==0