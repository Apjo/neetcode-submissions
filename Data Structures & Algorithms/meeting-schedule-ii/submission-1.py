"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_int = sorted(intervals, key=lambda x:x.start)
        N = len(intervals)
        ans=0
        min_h=[]
        for i in range(N):
            heapq.heappush(min_h, sorted_int[i].end)
            ans = max(ans, len(min_h))
            while i + 1 < N and min_h and min_h[0] <= sorted_int[i+1].start:
                heapq.heappop(min_h)
        return ans