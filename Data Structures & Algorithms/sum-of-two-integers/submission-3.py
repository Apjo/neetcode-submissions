class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFF
        for _ in range(32):
            if not b:
                break
            partial_sum = a ^ b
            carry = (a & b) << 1
            a=partial_sum
            b=carry
        if b:
            return a & MASK
        return a
