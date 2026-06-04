class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_h = []
        for num in nums:
            heapq.heappush(min_h, num)
            if len(min_h) > k:
                heapq.heappop(min_h)
        return min_h[0]