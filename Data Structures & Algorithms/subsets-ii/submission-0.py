class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(idx, res, buff):
            if idx == len(nums):
                # res.append(buff[:])
                res.add(tuple(buff[:]))
                return
            #pick
            buff.append(nums[idx])
            solve(idx+1, res, buff)
            buff.pop()
            #not pick
            solve(idx+1, res, buff)
        res, buff, idx = set(), [], 0
        nums.sort()
        solve(idx, res, buff)
        return [list(t) for t in res]