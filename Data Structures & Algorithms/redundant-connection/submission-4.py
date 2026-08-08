class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        #each node first is the parent of itself
        parent = [i for i in range(n + 1)]
        #initiall rank of all nodes is 1
        rank = [1]*(n + 1)
        
        def find(node):
            if node == parent[node]:
                return node
            node_to_ret = find(parent[node])
            return node_to_ret
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []