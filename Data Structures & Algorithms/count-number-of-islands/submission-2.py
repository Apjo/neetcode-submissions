class Solution:
    class DSU:
        def __init__(self, size):
            self.size = [1]*(size+1)
            self.parent = [0]*(size + 1)
            for i in range(size + 1):
                self.parent[i]=i

        def find(self, node):
            while self.parent[node] != node:
                node = self.find(self.parent[node])
            return self.parent[node]
        
        def union(self, n1, n2):
            p1 = self.find(n1)
            p2 = self.find(n2)
            if p1 == p2:
                return False
            #if parents are not same, think of merging
            if p1 != p2:
                #if the sizes of p1 >= p2, make p1 parent of p2, and increment size of p1 by size of p2
                if self.size[p1] >= self.size[p2]:
                    self.parent[p2] = p1
                    self.size[p1]+=self.size[p2]
                
                else:
                    #elif the sizes of p2 > p1, or if sizes of p1 and p2 are the same then:
                    # 1. make p2 parent of p1
                    # 2. increment size of p2 by size of p1
                    self.parent[p1] = p2
                    self.size[p2]+=self.size[p1]
            return True
    
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands, M, N = 0, len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1, 0]]
        
        dsu = self.DSU(M*N)
        
        def calc_index(row_num, col_num):
            return row_num * N + col_num
        
        for i in range(M):
            for j in range(N):
                if grid[i][j]=="1":
                    num_islands+=1
                    for dir in directions:
                        new_i = dir[0] + i
                        new_c = dir[1] + j
                        if new_i < 0 or new_c < 0 or new_i >= M or new_c >= N or grid[new_i][new_c] == "0":
                            continue
                        if dsu.union(calc_index(i, j), calc_index(new_i, new_c)):
                            num_islands-=1

        return num_islands
        