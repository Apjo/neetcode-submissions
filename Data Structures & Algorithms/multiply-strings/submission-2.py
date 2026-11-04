class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #if a 0 is seen in either num1 or num2 immediately return a 0 as the final ans
        #else, we create an intermediate buffer of size len(num1) + len(num2) init to all 0s which will hold the final result of num1*num2
        #iterate both the strings in reverse, and store at locations of their multiplications at locaiton (i + j) i.e. the result of product of num1[i] * num2[j] this will hold all the raw results without handling of carry
        #now, once again iterate over the res array in reverse up until index 0 while handling carry. Carry will always be stored to the left of the index i i.e. at index i - 1. So, we first start by handling the tens value, then keep only the units/ones digit at i, then at i - 1 we add back the carry value
        if "0" in [num1, num2]:
            return "0"
        M,N = len(num1), len(num2)
        res=[0]*(M+N)
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                #why do we store the final result in i + j + 1?
                #ans:
                res[i + j + 1] += int(num1[i]) * int(num2[j])
        for i in range(len(res) - 1, -1, -1):
            carry = res[i] // 10
            res[i] %= 10
            if i > 0:
                res[i-1] += carry
        beg=0
        while beg < len(res) and res[beg] == 0:
            beg+=1
        #now convert all the res array from location at beg to len(res)
        res = map(str, res[beg:])
        return "".join(res)