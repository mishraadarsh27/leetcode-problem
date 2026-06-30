class Solution:
    def commonChars(self, A: List[str]) -> List[str]:  
        return [c for c in set(A[0]) for _ in range(min(w.count(c) for w in A))]