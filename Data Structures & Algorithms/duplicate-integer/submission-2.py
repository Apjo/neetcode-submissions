class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for i in range(len(nums)):
            if nums[i] in hs:
                return True
            else:
                hs.add(nums[i])
        return False