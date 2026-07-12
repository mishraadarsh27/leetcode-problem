class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sorted_unique = sorted(set(arr))

        rank = {}

        for i, num in enumerate(sorted_unique, start=1):
            rank[num] = i

        return [rank[num] for num in arr]