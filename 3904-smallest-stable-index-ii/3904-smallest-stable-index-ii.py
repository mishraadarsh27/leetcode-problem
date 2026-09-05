class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)              

        pref_max = float('-inf')
        pref_max_list = []
        for i in range(0,n):
            if nums[i] > pref_max : 
                pref_max = nums[i]
            pref_max_list.append(pref_max)

        suff_min = float('inf')
        suff_min_list = []
        for i in range(n-1,-1,-1):
            if nums[i] < suff_min : 
                suff_min = nums[i]
            suff_min_list.append(suff_min)

        suff_min_list.reverse()
        
        idx = []
        for i in range(n):
            instability_score = pref_max_list[i] - suff_min_list[i]
            if instability_score <= k:
                return i
        return -1