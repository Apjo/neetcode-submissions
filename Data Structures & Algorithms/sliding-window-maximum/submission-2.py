class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        buff = deque()
        res=[]
        i,left=0,0
        while i < (len(nums)):
            while buff and nums[buff[-1]] < nums[i]:
                buff.pop()
            buff.append(i)
            if left > buff[0]:
                buff.popleft()
            if i >= k - 1:
                res.append(nums[buff[0]])
                left+=1
            i+=1
        return res