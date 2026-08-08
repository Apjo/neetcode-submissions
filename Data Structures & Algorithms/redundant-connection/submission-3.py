class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        G = [[] for _ in range(n + 1)]
        indeg = [0]*(n+1)
        # outdeg = [0]*(n)
        for edge in edges:
            G[edge[0]].append(edge[1])
            G[edge[1]].append(edge[0])
            indeg[edge[0]]+=1
            indeg[edge[1]] += 1
        q = deque()
        #add to q all those nodes whose indeg ==1
        for i in range(1, n + 1):
            if indeg[i] == 1:
                q.append(i)
        while q:
            curr = q.popleft()
            #decrement indegree of this node by 1
            indeg[curr]-=1
            for neighbor in G[curr]:
                #decrement indegree of neighbor node by 1
                indeg[neighbor]-=1
                if indeg[neighbor]==1:
                    q.append(neighbor)
        #nodes with degree > 0 are forming a cycle, we traverse our input edge list in reverse, pick the first set of nodes where indeg[u] > 0 and indeg[v] > 0
        print(indeg)
        # print(reversed(edges))
        for u, v in reversed(edges):
            print(f"indeg of u={indeg[u]}, v={indeg[v]}")
            # if indeg[u] == 2 and indeg[v]:
            if indeg[u] > 0 and indeg[v] > 0:
                return [u, v]