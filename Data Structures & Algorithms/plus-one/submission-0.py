class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        carry = 0
        res=[]
        i = N - 1
        while i >= 0:
            _sum=0
            if i == N - 1:
                _sum = digits[i] + 1
            else:
                _sum = digits[i] + carry
            if _sum >= 10:
                carry=1
                res.append(_sum % 10)
            else:
                carry=0
                res.append(_sum)
            i-=1
        if carry == 1:
            res.append(1)
        res.reverse()
        return res