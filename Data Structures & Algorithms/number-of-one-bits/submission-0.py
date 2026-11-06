class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr = 0
        while n > 0:
            if (n & 1):
                ctr+=1
            n >>= 1
            # ctr+=1
        return ctr