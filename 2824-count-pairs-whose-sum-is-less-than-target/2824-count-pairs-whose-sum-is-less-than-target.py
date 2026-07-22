class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        res = 0

        while left < right:

            current_sum = nums[left] + nums[right]

            if current_sum >= target:
                right -= 1
            else:
                res += (right - left)
                left += 1
        return res