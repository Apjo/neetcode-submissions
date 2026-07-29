class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # def run_dijk():
        #     #dist, and parent map will be fed into
        #     #captured will be init to False to keep track of which vertices have been visited
        #     #a PQ min heap will be instantiated here? or passed in? lets pass in
        #     while min_heap:
        #         curr_min_dist, row_i, col_j = heapq.heappop(min_heap)
        #         if captured[row_i][col_j]:
        #             continue
        #         captured[row_i][col_j] = True
        #         if curr_min_dist == INF:
        #             curr_min_dist=0
        #         for direction in directions:
        #             new_r, new_c = direction[0] + row_i, direction[1] + col_j
        #             #skip captured, and walls,and invalid grid locations
        #             if new_r < 0 or new_c < 0 or new_r >= M or new_c >= N or captured[new_r][new_c] or grid[new_r][new_c]==-1:
        #                 continue
        #             # if grid[new_r][new_c] == INF:
        #             if distance[(new_r, new_c)] > 1 + curr_min_dist:
        #                 distance[(new_r, new_c)] = 1 + curr_min_dist
        #                 heapq.heappush(min_heap, (distance[(new_r, new_c)], new_r, new_c))
        
        if not grid:
            return
        INF, M, N = 2147483647, len(grid), len(grid[0])
        # captured = [[False for _ in range(N)] for _ in range(M)]
        # distance={(r, c): INF for r in range(M) for c in range(N)}
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # min_heap = deque()
        bfs_q = deque()
        #add all open cells to a queue
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    bfs_q.append((i, j))
        #run bfs at each cell and keep on updating min distances to that cell          
        while bfs_q:
            r, c = bfs_q.popleft()
            curr_dist = grid[r][c]
            for direction in directions:
                new_r, new_c = direction[0] + r, direction[1] + c
                #skip captured, and walls,and invalid grid locations
                # if new_r < 0 or new_c < 0 or new_r >= M or new_c >= N or grid[new_r][new_c]==-1:
                #     continue
                if new_r >= 0 and new_c >= 0 and new_r < M and new_c < N and grid[new_r][new_c]==INF:
                    # continue
                    new_dist = 1 + curr_dist
                    if new_dist < 0:
                        new_dist = 0
                    grid[new_r][new_c] = new_dist
                    bfs_q.append((new_r, new_c))
                    # captured[new_r][new_c] = True


        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j] == INF:
        #             distance[(i, j)] = 0
        #             heapq.heappush(min_heap, (grid[i][j], i, j))
        #             run_dijk()
        
        # for k, v in distance.items():
        #     r, c = k
        #     grid[r][c] = v
        # return grid
