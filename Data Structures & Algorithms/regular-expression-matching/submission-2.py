class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        memo = {}
        def solve(i, j):
            if i >= M and j >= N:
                return True
            if j >= N:
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]

            is_matching = False

            if i < M: 
                is_matching = s[i] == p[j] or p[j] == '.'
            else:
                is_matching = False

            ans = False

            if j + 1 < N and p[j + 1] == '*':
                memo[(i, j)] = solve(i, j + 2) or (is_matching and solve(i+1, j))
                return memo[(i, j)]

            if is_matching:
                memo[(i, j)] = solve(i + 1, j + 1)
                return memo[(i, j)]
        
            return ans
        
        return solve(0, 0)