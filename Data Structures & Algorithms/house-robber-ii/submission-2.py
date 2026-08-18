class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        def solve(arr: List[int]) -> int:
            n2 = len(arr)
            dp = [0] * (n2)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n2):
                dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
            return dp[-1]
        
        return max(solve(nums[:-1]), solve(nums[1:]))
        