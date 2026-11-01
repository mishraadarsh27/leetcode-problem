class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def incresing(lst):
            for i in range(len(lst)-1):
                if(lst[i]>=lst[i+1]):
                    return False
            return True
        ans=0
        n=len(nums)
        for i in range(0,n):
            for j in range(i,n):
                remaining=incresing(nums[:i]+nums[j+1:])
                if(remaining==True):
                    ans+=1
        return ans