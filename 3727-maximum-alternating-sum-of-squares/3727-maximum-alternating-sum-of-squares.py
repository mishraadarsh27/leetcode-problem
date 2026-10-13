class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        vals = sorted((x * x for x in nums), reverse=True)
        pos = (len(vals) + 1) // 2
        return sum(vals[:pos]) - sum(vals[pos:])