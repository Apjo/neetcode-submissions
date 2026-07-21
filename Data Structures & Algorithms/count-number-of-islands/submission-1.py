class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate over the grid, and if you see a 1, perform a dfs to count the islands
        #after finishing the search then only increment the count
        ans, M, N = 0, len(grid), len(grid[0])
        def solve(r, c):
            if r < 0 or c < 0 or r >=M or c >= N or grid[r][c]=="#" or grid[r][c]=="0":
                return

            #Basically, here is where ideally we could have just marked the land cell as water 
            #since Whenever we find a land cell that hasn’t been visited, we start a DFS to sink the entire island by marking all its connected land as water.
            #in our case a # means this cell is visited
            grid[r][c]="#"
            solve(r+1, c)
            solve(r-1, c)
            solve(r, c+1)
            solve(r, c-1)

        for r in range(M):
            for c in range(N):
                if grid[r][c]=="1":
                    ctr=0
                    solve(r, c)
                    ans+=1
        return ans