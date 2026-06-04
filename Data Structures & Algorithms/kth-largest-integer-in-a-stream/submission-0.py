class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for i in nums:
            heapq.heappush(self.pq, i)


    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
