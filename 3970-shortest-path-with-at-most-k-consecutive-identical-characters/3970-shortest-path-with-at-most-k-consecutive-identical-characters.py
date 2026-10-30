import heapq
from typing import List


class Solution:
    def shortestPath(
        self,
        n: int,
        edges: List[List[int]],
        labels: str,
        k: int,
    ) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        heap = [(0, 0, 1)]  

        while heap:
            d, u, run = heapq.heappop(heap)

            if d > dist[u][run]:
                continue

            if u == n - 1:
                return d

            for v, w in graph[u]:
                next_run = run + 1 if labels[u] == labels[v] else 1

                if next_run > k:
                    continue

                new_distance = d + w
                if new_distance < dist[v][next_run]:
                    dist[v][next_run] = new_distance
                    heapq.heappush(heap, (new_distance, v, next_run))

        return -1