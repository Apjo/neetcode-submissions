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
        # min_h = []
        # q will hold (curr cost, curr node, curr stop num)
        bfs_q.append((0, src, k + 1))
        # heapq.heappush(min_h, (0, src, k + 1))
        # stop_count = 0
        # heapq.heappush(min_h, (0, src, starting_stop))
        # apply dijkstra!
        while bfs_q:
            N = len(bfs_q)
            for i in range(N):
                curr_cost, curr_node, curr_stop_num = bfs_q.popleft()
                # curr_cost, curr_node, _ = heapq.heappop(min_h)
                # print(f"curr_cost={curr_cost}, curr_node={curr_node}, curr_stop_num={curr_stop_num}")
                if curr_stop_num <= 0:
                    continue
                # why not check if we have already seen this node?
                # if dist[curr_node] != float("inf"):
                #     continue
                # dist[curr_node] = curr_cost
                # print(f"setting distance of curr_node={curr_node} to be={dist[curr_node]}")
                for neighbor, neighbor_cost in G[curr_node]:
                    # print(f"looking at neighbor={neighbor}, with cost={neighbor_cost}")
                    new_cost = curr_cost + neighbor_cost
                    # print(f"new cost={new_cost}")
                    if new_cost < dist[neighbor]:
                        # print("updating neighbor's cost, and reducing stop by 1")
                        dist[neighbor] = new_cost
                        bfs_q.append((new_cost, neighbor, curr_stop_num - 1))
                        # heapq.heappush(min_h, (new_cost, neighbor, _))
            # starting_stop += 1

        return dist[dst] if dist[dst] != float("inf") else -1
        