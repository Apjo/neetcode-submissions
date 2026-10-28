class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        # queries.sort()
        min_h = []
        N = len(intervals)

        res = []
        hm = {}
        i = 0
        for q in sorted(queries):
            while i < N and intervals[i][0] <= q:
                # keep adding to min heap which is sorted based on interval size until start of interval <= query[i]
                # while :
                st = intervals[i][0]
                end = intervals[i][1]
                interval_size = end - st + 1
                heapq.heappush(min_h, (interval_size, end))
                i += 1
            while min_h and min_h[0][1] < q:
                heapq.heappop(min_h)
            hm[q] = min_h[0][0] if min_h else -1
        return [hm[q] for q in queries]
