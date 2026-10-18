class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        furthest = 0
        for i in range(N):
            if furthest < i:
                return False
            furthest = max(furthest, i + nums[i])
        return True