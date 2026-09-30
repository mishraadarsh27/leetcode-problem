class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        l = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        return l