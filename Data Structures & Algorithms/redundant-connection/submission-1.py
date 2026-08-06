class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #build graph
        
        n = len(edges)
        # indegrees={}
        G=[[] for _ in range(n+1)]
        for e in edges:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
            # indegrees[e[0]]+=1
            # indegrees[e[1]]+=1
        cycle_start=-1
        visited, all_cycles = set(), set()
        def dfs(vertex, parent=-1):
            nonlocal cycle_start
            #reached a visited node, mark it as a start of the cycle
            if vertex in visited:
                cycle_start=vertex
                return
            visited.add(vertex)
            for neighbor in G[vertex]:
                # if neighbor not in visited:
                    #not visiting parent again
                    if neighbor == parent:
                        continue
                    #if no cycles found continue exploring the Graph
                    if len(all_cycles) == 0:
                        dfs(neighbor, vertex)
                    #cycle detected! keep on adding nodes to the cycle till we get to the start of the cycle,so by adding vertex (the current node), you are safely extracting the exact nodes from the active recursion history (the call stack) that formed the loop, one frame at a time, until you get back to the node where the cycle originally began
                    if cycle_start != -1:
                        all_cycles.add(vertex)
                    #all nodes of the cycle are taken, now return
                    if vertex == cycle_start:
                        cycle_start=-1
                        return

        # for i in range(n):
            # if i not in visited:
        # print(f"our grpah={G}")
        dfs(1)
        
        for i in range(n, -1, -1):
            # print(i)
            if edges[i - 1][0] in all_cycles and edges[i - 1][1] in all_cycles:
                return edges[i - 1]
        return []

