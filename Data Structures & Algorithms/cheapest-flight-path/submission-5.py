class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # build graph of {from : (to, cost)}
        G = defaultdict(list)
        for flight in flights:
            G[flight[0]].append((flight[1], flight[2]))
        # set distance matrix for source to find destination
        dist = [float("inf")] * (n)
        dist[src] = 0
        bfs_q = deque()
        bfs_q.append((0, src, k + 1))

        while bfs_q:
            N = len(bfs_q)
            for i in range(N):
                curr_cost, curr_node, curr_stop_num = bfs_q.popleft()

                if curr_stop_num <= 0:
                    continue

                for neighbor, neighbor_cost in G[curr_node]:
                    new_cost = curr_cost + neighbor_cost
                    if new_cost < dist[neighbor]:
                        dist[neighbor] = new_cost
                        bfs_q.append((new_cost, neighbor, curr_stop_num - 1))

        return dist[dst] if dist[dst] != float("inf") else -1
        