class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return (p:=sorted(points)) and max(b-a for (a,_),(b,_) in zip(p, p[1:]))