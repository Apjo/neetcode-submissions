class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(res, buff, idx):
            if idx == len(nums):
                res.add(tuple(buff[:]))
                return
            #pick
            buff.append(nums[idx])
            solve(res, buff, idx+1)
            buff.pop()
            #dont pick
            solve(res, buff, idx + 1)
        res=set()
        buff=[]
        solve(res, buff, 0)
        # list_of_lists = [list(item) for item in res]
            # return [list(t) 
        return [list(t) for t in res]