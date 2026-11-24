fct = [set(),set(),{2},{3},{2},{5},{2,3},{7},{2},{3},{2,5}]

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans,bag,l = min(2, len(nums)), set(), -1
        for r,num in enumerate(nums):
            while l<r and bag & fct[num]: bag -= fct[nums[l:= l+1]]
            bag |= fct[num]
            ans  = max(ans, r-l)
        return ans
        