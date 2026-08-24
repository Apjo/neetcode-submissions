class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp, res = 1, float("-inf")
        for i in range(len(nums)):
            temp = temp * nums[i]
            res = max(res, temp)
            temp = temp if temp != 0 else 1
        
        temp=1
        for i in range(len(nums) -1, -1, -1):
            temp = temp * nums[i]
            # temp = temp if temp != 0 else 1
            res = max(res, temp)
            temp = temp if temp != 0 else 1

        return int(res)

