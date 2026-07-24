class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # h = {}
        # for i in nums:
        #     if i in h:
        #         return True
        #     else:
        #         h[i] = 1
        # return False
        
        nums.sort()
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                return True

            left += 1
            right += 1

        return False