class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        all_sum = sum(nums)
        if all_sum % 2 != 0:
            return False
        all_half = all_sum // 2
        
        dp=[[False] *(all_half + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            #for all i having a sum=0 is possible by not taking any i
            dp[i][0] = True
        # print(dp)
        for i in range(1, N + 1):
            for j in range(1, all_half + 1):
                #take only if sum up until i-1 is <= j 
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[N][all_half]
        