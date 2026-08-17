class Solution:
    def rob(self, nums: List[int]):
        def solve(idx):
            #1. At idx == 0: You have one house. Should you rob it or not? You rob it. So return nums[0].
            #2. At idx == 1: You have two houses (indices 0 and 1). You can't rob both (adjacent). So return the maximum of the two—max(nums[0], nums[1]).
            if idx in memo:
                return memo[idx]
            
            if idx == 1:
                memo[1] = max(nums[0], nums[1])
                return memo[1]
            # pick house at idx, so now only grab house at idx-2
            b = solve(idx - 2) + nums[idx]
            # dont pick house at idx, so now get what you have from idx-1
            a = solve(idx - 1)
            memo[idx] = max(a, b)
            
            return max(a, b)

        memo = {0:nums[0]}
        return solve(len(nums) - 1)
        