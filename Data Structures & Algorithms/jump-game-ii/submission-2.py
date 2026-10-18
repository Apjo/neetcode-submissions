class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        memo={}
        def solve(idx):
            if idx in memo:
                return memo[idx]
            if idx == N - 1:
                return 0
            if nums[idx] == 0:
                return 100000
            
            end = min(N - 1, idx + nums[idx])
            res = 100000
            for i in range(idx + 1, end + 1):
                res = min(res, 1 + solve(i))
            memo[idx] = res
            return res
        temp = solve(0)

        return temp