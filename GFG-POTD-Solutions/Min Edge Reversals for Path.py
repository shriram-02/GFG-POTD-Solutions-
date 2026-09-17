from collections import deque

class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))

        dist = [float('inf')] * (n + 1)
        dist[src] = 0

        dq = deque([src])

        while dq:
            u = dq.popleft()

            for v, cost in adj[u]:
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost

                    if cost == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)

        return -1 if dist[dst] == float('inf') else dist[dst]