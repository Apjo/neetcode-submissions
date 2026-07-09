class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(idx, res, buff):
            if idx == len(nums):
                # res.append(buff[:])
                res.append(buff[:])
                return
            # pick
            buff.append(nums[idx])
            solve(idx + 1, res, buff)
            buff.pop()
            
            # skip duplicates for this nums[idx]
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            # not pick
            solve(idx + 1, res, buff)

        res, buff, idx = [], [], 0

        nums.sort()

        solve(idx, res, buff)

        return res
        