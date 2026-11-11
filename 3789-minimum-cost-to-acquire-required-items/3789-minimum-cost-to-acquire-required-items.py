class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 + cost2 <= costBoth:
            return need1*cost1 + need2*cost2
        a = max(0, need2 - need1)*cost2 + need1*costBoth
        b = max(0, need1 - need2)*cost1 + need2*costBoth
        return min(a, b)