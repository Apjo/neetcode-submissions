class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_h = [-x for x in stones]
        heapq.heapify(max_h)
        curr = 0
        
        if len(stones) == 1:
            return stones[0]

        while len(max_h) > 1:
            x,y=0,0
            
            #if len of heap is > 1 that means we can pop twice
            #else, if len is exactly 1 just pop once, and set curr = curr - value  if curr > value else value - curr
            # if len(max_h) > 1:
            x = -1 * heapq.heappop(max_h)
            y = -1 * heapq.heappop(max_h)
            
            curr = x - y if x > y else y - x
            
            heapq.heappush(max_h, -curr)
            if len(max_h) == 1:
                curr = -1 * heapq.heappop(max_h)
                break
        return curr