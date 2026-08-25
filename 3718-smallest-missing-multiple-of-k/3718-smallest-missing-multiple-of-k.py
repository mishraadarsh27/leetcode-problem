class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ks=k
        i=1
        while k in nums:
            k=ks*i
            i+=1
        return k