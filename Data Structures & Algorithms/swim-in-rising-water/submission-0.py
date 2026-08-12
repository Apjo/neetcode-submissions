class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # print(f"grid dimensions={m}, {n}")
        min_h = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heapq.heappush(min_h, (grid[0][0], 0, 0))
        visited=[[False for _ in range(n)] for _ in range(m)]
        visited[0][0] = True
    #The reason all rows at column 0 are getting updated is that
    # the multiplication operator * in Python copies object references, not the actual objects.
    #When you write [[False] * n] * m, Python creates one single row in memory
    #and then creates a list of m items that all point to that exact same row.
    # print(visited)
    # timer = 0
        while min_h:
            N = len(min_h)
            # for i in range(N):
            cost, x, y = heapq.heappop(min_h)
            # timer+=1
            # print(f"current cost={cost}, at row={x}, col={y}")
            if x == m - 1 and y == n - 1:
                # print(f"FINAL ANS={cost}")
                return cost
                # return g[x][y]
            visited[x][y] = True
            for dire in directions:
                new_x, new_y = dire[0]+x, dire[1] + y
                #check for valid coordinates
                #check if visited
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or visited[new_x][new_y]:
                    continue
                visited[new_x][new_y] = True
                # print(f"new coordinates to look at:")
                heapq.heappush(min_h, (max(cost, grid[new_x][new_y]), new_x, new_y))
        return -1
        