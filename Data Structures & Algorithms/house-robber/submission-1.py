class Solution:
    def rob(self, nums: List[int]) -> int:
        #if im planning to rob house at index i, then i need to rob i-2, else i need to work with what i have from i-1, and pick the max out of them
        #i.e. dp[i] <- max(dp[i - 2] + cost[i], dp[i - 1])
        n = len(nums)
        print(f"got total houses={n}")
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp=[0]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]