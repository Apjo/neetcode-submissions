class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #build the graph
        #init a min cost variable
        #apply prims picking one vertex at a time
        #retun min cost  
        def run_prims(vertex):
            nonlocal total_cost
            # print(f"starting at vertex={vertex}")
            while min_heap:
                cost, curr_point = heapq.heappop(min_heap)
                # print(f"Looking at current point={curr_point}, with cost={cost}")
                if captured[curr_point]:
                    continue
                total_cost += cost
                # print(f"updated cost={total_cost}")
                captured[curr_point] =True
                for point in range(n):
                    if not captured[point]:
                        # print(f"calculating md between point1={curr_point}, point2={point}")
                        md = abs(points[point][0] - points[curr_point][0]) + abs(points[point][1] - points[curr_point][1])
                        # print(f"calcualted md={md} to add to min heap")
                        heapq.heappush(min_heap, (md, point))
                        # captured[]
        n = len(points)

        captured = [False] * (n)
        start_vertex = 0
        # captured[start_vertex]= True
        min_heap = []
        total_cost = 0
        #add first vertex 0 with init cost 0
        heapq.heappush(min_heap, (0, 0))

        run_prims(0)
        return total_cost