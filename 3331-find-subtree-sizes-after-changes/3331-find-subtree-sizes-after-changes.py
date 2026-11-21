class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        new_parent = parent[:]
        last = [-1] * 26
        def dfs1(u):
            c = ord(s[u]) - ord('a')
            prev = last[c]
            if prev != -1:
                new_parent[u] = prev
            last[c] = u
            for v in children[u]:
                dfs1(v)
            last[c] = prev
        dfs1(0)
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        ans = [1] * n
        def dfs2(u):
            for v in new_children[u]:
                dfs2(v)
                ans[u] += ans[v]
        dfs2(0)

        return ans