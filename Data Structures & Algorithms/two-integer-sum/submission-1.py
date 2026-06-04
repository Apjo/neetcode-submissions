class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        res=[]
        sorted(nums)
        for i in range(len(nums)):
            if target - nums[i] in freq:
                res.append(freq[target-nums[i]])
                res.append(i)
            else:
                freq[nums[i]]=i
        return res