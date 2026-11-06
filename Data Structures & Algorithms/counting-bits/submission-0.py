class Solution:
    def countBits(self, n: int) -> List[int]:
        def countSetBits(n) -> int:
            ctr = 0
            while n > 0:
                #if n has a set bit at the ith position the result is positive, else its a 0. We increment ctr if result is positive
                if (n & 1):
                    ctr+=1
                #shifting n by 1 to right moves us to next bit
                n >>= 1
                # ctr+=1
            return ctr
        res = []
        for i in range(n + 1):
            res.append(countSetBits(i))
        
        return res
