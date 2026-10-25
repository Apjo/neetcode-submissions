"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort by start times
        #iterate over the sorted intervals
        #drop the meeting into a max heap, any meeting thats having an end time > the top of heap, we pop from heap
        #at the end if the heap isn't empty, we return a false
        s_i = sorted(intervals, key=lambda x: x.start)
        N = len(s_i)
        max_h = []
        
        for i in range(N):
            if i + 1 < N and s_i[i].end > s_i[i + 1].start:
                return False

        
        return True