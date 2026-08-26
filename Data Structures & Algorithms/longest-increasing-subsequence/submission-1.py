class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        ans=[1]*(N)
        for i in range(N):
            for k in range(i):
                if nums[i] > nums[k]:
                    ans[i] = max(ans[i], ans[k] + 1)
        # print(ans)
        return max(ans)