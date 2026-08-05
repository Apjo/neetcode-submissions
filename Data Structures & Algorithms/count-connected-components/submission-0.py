class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt=0
        G=[[] for _ in range(n)]
        for e in edges:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
        
        visited=set()
        def solve(vertex):
            visited.add(vertex)
            for neighbor in G[vertex]:
                if neighbor not in visited:
                    solve(neighbor)
        for i in range(n):
            if i not in visited:
                cnt+=1
                solve(i)
        return cnt