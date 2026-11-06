class Solution:
    def reverseBits(self, n: int) -> int:
        #convert the n into a binary string by padding 0s
        bstr = format(n, '032b')
        #reverse the string
        rev_bstr = bstr[::-1]
        #convert back to int
        return int(rev_bstr, 2)