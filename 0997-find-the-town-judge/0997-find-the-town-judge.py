class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        truster = defaultdict(int)
        trusted = defaultdict(int)

        for src, dst in trust:
            truster[src] += 1
            trusted[dst] += 1

        for i in range(1, n + 1):
            if truster[i] == 0 and trusted[i] == n - 1:
                return i

        return -1