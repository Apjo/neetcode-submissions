class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            dd = point[0] ** 2 + point[1] ** 2
            rec = (-dd, point[0], point[1])
            heapq.heappush(min_heap,rec)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = []
        while min_heap:
            # temp_l = [x,y for x, y in ]
            _, second, third = heapq.heappop(min_heap)
            res.append([second, third])
        return res