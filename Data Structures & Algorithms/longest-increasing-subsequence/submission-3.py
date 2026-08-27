class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        ans = [1]*(N)
        for i in range(N):
            for k in range(i):
                # print(f"At k={k}, i={i} nums[i]={nums[i]}, nums[k]={nums[k]}, ans[i]={ans[i]} ans[k]={ans[k]}")
                if nums[k] < nums[i]:
                    #if we find a number > the one at k, do we stay with what we have up until now that is ans[i], or we add 1 and see which one is max?
                    ans[i] = max(ans[i], ans[k] + 1)
        return max(ans)