class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort()
        l = []
        while sum(l) <= sum(nums):
            l.append(nums.pop())
        return l
