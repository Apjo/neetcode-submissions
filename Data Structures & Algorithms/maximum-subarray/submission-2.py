class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [*nums]
        for i in range(1, N):
            dp[i] = max(nums[i] + dp[i - 1], nums[i])
        return max(dp)
        