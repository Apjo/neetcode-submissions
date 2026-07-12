class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #maintain the map of what each digit represents
        #for each digit:
            #grab its corresponding string
            #and then simply perform cross product between each digit's string with the next digit's str
        def solve(idx, buff, res):
            if idx == len(digits):
                # res.append(buff[:])
                res.append(buff)
                return
            curr_digit = int(digits[idx])
            for curr_char in d_to_l[curr_digit]:
                # buff.append(curr_char)
                buff+=curr_char
                solve(idx + 1, buff, res)
                buff = buff[:-1]
        
        if not digits:
            return []
        d_to_l = {0:(), 1:(), 2:('a', 'b', 'c'), 3:('d', 'e', 'f'), 4:('g', 'h', 'i'), 5:('j', 'k', 'l'), 6:('m', 'n', 'o'), 7:('p', 'q', 'r', 's'), 8:('t', 'u', 'v'), 9:('w', 'x', 'y', 'z')}
        
        idx, res, buff = 0, [],""
        solve(idx, buff, res)
        print(res)
        return res
        