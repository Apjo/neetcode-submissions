class Solution:
    def reverseBits(self, n: int) -> int:
        #init res to 0
        res=0
        #for each bit position i from 0 to 31
        for i in range(32):
            #extract the ith bit in n
            extracted_bit = (n >> i) & 1
            #shift this bit to position 31 - i
            shifted_bit = extracted_bit << (31 - i)
            #add it to final result res
            res+=shifted_bit
        #finally return re after processing all 32 bits
        return res
        