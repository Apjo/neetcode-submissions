class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort intervals based on start times
        #iterate over each and we try to create a new list of only non overlapping intervals
        ans=0
        si = sorted(intervals, key=lambda x: x[0])
        N = len(intervals)
        # res =[]
        prev_end = si[0][1]
        for i in range(1, N):
            if si[i][0] >= prev_end:
                prev_end=si[i][1]
            else:
                ans+=1
                prev_end = min(prev_end, si[i][1])
        return ans