class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        for c in range(1, n):
            val = grid[0][c]
            dp[c] = {x ^ val for x in dp[c - 1]}
        for r in range(1, m):
            val = grid[r][0]
            dp[0] = {x ^ val for x in dp[0]}
            for c in range(1, n):
                val = grid[r][c]
                combined_prev_xors = dp[c] | dp[c - 1]
                dp[c] = {x ^ val for x in combined_prev_xors}
        return min(dp[n - 1])