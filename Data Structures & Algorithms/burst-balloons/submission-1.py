class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        #build a new nums arr where we drop 0s and prepend, and append a 1
        nums = [1] + nums + [1]
        # print(nums)
        dp=[[0]*(N + 2) for _ in range(N + 2)]
        #dp[i][j]: the maximum coins we can get from nums[i: j], and we devide it into 3 parts:
        #part 1 burst balloons from index i to k-1
        for k in range(1, N + 1):
            # We define the sub-problem size by the length k, we solve the all the sub-problems M[i][left + k - 1] where left varies with fixed length k, left + k can not larger than N, i.e. left + k - 1 <= N, thus we have left <= N - k + 1
            for left in range(1, N - k + 2):
                right = left + k - 1
                for i in range(left, right + 1):
                    left_num = nums[left - 1] if left - 1 >= 0 else 1
                    right_num = nums[right + 1] if right + 1 <= N else 1
                    coins_earned = left_num * nums[i] * right_num
                    left_sum = dp[left][i - 1]
                    right_sum = dp[i + 1][right]
                    # dp[left][right] = max(dp[left][right], dp[left][i-1] + nums[left - 1] * nums[i] * nums[right + 1] + dp[i + 1][right])
                    dp[left][right] = max(dp[left][right], coins_earned + left_sum + right_sum)
        
        return dp[1][N]
        