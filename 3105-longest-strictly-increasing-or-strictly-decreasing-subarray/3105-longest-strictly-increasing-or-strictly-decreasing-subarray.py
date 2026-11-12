class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longArrLen = 1
        localLen = 1
        flag = True
        for i in range(0, len(nums)-1):
            if nums[i] < nums[i + 1]:
                if flag == False:
                    localLen = 1
                flag = True
                localLen+=1
            elif nums[i] > nums[i + 1]:
                if flag ==  True:
                    localLen = 1
                flag = False
                localLen += 1
            else:
                localLen = 1
            longArrLen = max(longArrLen, localLen)
        return longArrLen