class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))

        if min_i > max_i:
            min_i, max_i = max_i, min_i

        left = max_i + 1
        right = n - min_i
        both = (min_i + 1) + (n - 1 - max_i + 1)
        return min(left,right,both)