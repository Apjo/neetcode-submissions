class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #using kadanes algo
        curr_sum = 0
        ans = float("-inf")
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            ans = max(ans, curr_sum)
        return ans