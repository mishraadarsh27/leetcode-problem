class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        ans = []

        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nbr in adj[node]:
                if not visited[nbr]:
                    dfs(nbr)

        dfs(k)

        for u, v in invocations:
            if (not visited[u] and visited[v]):
                return list(range(n))
            
        for val in range(n):
            if not visited[val]:
                ans.append(val)

        return ans
        