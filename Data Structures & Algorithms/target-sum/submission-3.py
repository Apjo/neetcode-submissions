class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        N = len(nums)
        memo={}
        def solve(idx, T):
            if idx >= N :
                if T == target:
                    # print(f"YAY! reached target at idx={idx}")
                    return 1
                # print(f":( did not reach target at idx={idx}")
                return 0
            if (idx, T) in memo:
                return memo[(idx, T)]
            # print(f"pos:At index={idx}, nums[idx]={nums[idx]}, with curr sum={T}")
            a = solve(idx + 1, T + nums[idx])
            # print(f"neg:At index={idx}, nums[idx]={nums[idx]}, with curr sum={T}")
            b = solve(idx + 1, T + -1 * nums[idx])
            memo[(idx, T)] = a+b
            return a + b
        
        return solve(0, 0)