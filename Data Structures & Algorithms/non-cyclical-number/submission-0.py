class Solution:
    def isHappy(self, n: int) -> bool:
        seen= set()
        '''
        simulate:
        -if after calculating sum of squares is already present in seen,
        or if the final sum is 1 break, else continue
        '''
        seen = {}
        def sum_of_sqrs(x: int) -> int:
            _sum = 0
            while x:
                r  = x % 10
                _sum+=(r ** 2)
                x = x // 10
            return _sum

        while n>=1:
            # print(f"current n={n}")
            if n==1:
                # print("Finally reached a 1")
                return True
                break
            if n in seen and seen[n] > 1:
                # print(f"Found {n} in seen!")
                break
            n = sum_of_sqrs(n)
            # print(f"Adding  N={n} to seen map")
            # seen.add(n)
            seen[n] = seen.get(n, 0) + 1
        return False