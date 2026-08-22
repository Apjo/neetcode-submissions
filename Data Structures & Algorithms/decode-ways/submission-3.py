class Solution:
    def numDecodings(self, s: str) -> int:
        f=[0]*(len(s) + 1)
        f[0] = 1 #there is only 1 way to decode NOTHING.
        f[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            
            second_digit = int(s[i - 1]) - int('0')
            first_digit = int(s[i - 2]) - int("0")
            final_number = int(str(first_digit) + "" + str(second_digit))
            if 10 <= final_number <= 26:
                f[i] += f[i - 2]
        
        return f[len(s)]
        