class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                dest_idx = nums[i]
                if dest_idx < len(nums) and nums[i] != nums[dest_idx]:
                    nums[i], nums[dest_idx] = nums[dest_idx], nums[i]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
