class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        L, M, N = len(s3), len(s1), len(s2)

        ans: bool = False
        memo = {}
        def solve(idx1, idx2):
            nonlocal ans
            if idx1 == M and idx2 == N:
                return True

            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            if idx1 + idx2 < L and idx1 < M and s1[idx1] == s3[idx1 + idx2]:
                r1 = solve(idx1 + 1, idx2)
                ans |= r1
                # memo[(idx1, idx2)] = ans
            if idx1 + idx2 < L and idx2 < N and s2[idx2] == s3[idx1 + idx2]:
                r2 = solve(idx1, idx2 + 1)
                ans |= r2
                # memo[(idx1, idx2)] = ans
            memo[(idx1, idx2)] = ans

            return ans

        return solve(0, 0)
        