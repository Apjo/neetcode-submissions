import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #maintain a freq map
        freq=Counter(nums)
        min_heap=[]
        for val, frequency in freq.items():
            heapq.heappush(min_heap, [frequency, val])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        ans = []
        while min_heap:
            frequency, value = heapq.heappop(min_heap)
            ans.append(value)
        return ans
        #maintain a pq starting with a min heap of size k which is sorted based on freq of element
            #keep on dumping elements into this heap as long as heap.size <k
            #once heap size reaches >=k:
                #poll from the heap
            #once iteration over the input is done, the heap should contain all the most frequently occuring elements