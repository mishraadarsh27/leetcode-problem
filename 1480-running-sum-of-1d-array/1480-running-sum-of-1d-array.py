class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        sum = []
        sum.append(nums[0])
        for i in range(1, n):
            x = sum[i-1] + nums[i]
            sum.append(x)
        return sum

           