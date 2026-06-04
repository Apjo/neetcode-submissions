class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                j+=1
        return False