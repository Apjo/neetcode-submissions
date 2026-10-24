class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        N = len(intervals)
        # res.append(intervals[0])
        # flag = False
        # seen=-1
        for i in range(N):
            '''
            if new interval[1] < current interval[0]
                append newinterval to res
                return final result by appending to it everything after this index
            else if new interval[0] > current interval[1]
                append current interval to res
            else
                update newinterval's start and end
            add newinterval to res
            return res
            '''
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res
        