class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = 0, len(nums) - 1
        def solve(lo, hi):
            if lo > hi:
                return -1
            mid = lo + ((hi  - lo) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return solve(mid + 1, hi)
            else:
                return solve(lo, mid - 1)
        return solve(lo, hi)