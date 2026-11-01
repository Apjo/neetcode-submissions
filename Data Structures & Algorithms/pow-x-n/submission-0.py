class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(a, b):
            if a == 0:
                return 0
            if b == 0:
                return 1
            
            if b % 2 == 0:
                res = solve(a, b // 2)
                return res * res
            
            return a * solve(a, b - 1)
            
        fp = solve(x, abs(n))
        return fp if n >= 0 else 1/fp
