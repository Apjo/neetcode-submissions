class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_h = [-x for x in stones]
        print(max_h)
        heapq.heapify(max_h)
        curr = 0
        
        while max_h:
            x,y=0,0
            
            #if len of heap is > 1 that means we can pop twice
            #else, if len is exactly 1 just pop once, and set curr = curr - value  if curr > value else value - curr
            if len(max_h) > 1:
                x = -1 * heapq.heappop(max_h)
                y = -1 * heapq.heappop(max_h)
                print(f"POPPED x={x}, y={y}")
                curr = x - y if x > y else y - x
                print(f"PUSHING curr={-curr}")
                heapq.heappush(max_h, -curr)
            if len(max_h) == 1:
                x = -1 * heapq.heappop(max_h)
                print(f"ONLY POPPED x={x}")
                curr = x
                break
        return curr