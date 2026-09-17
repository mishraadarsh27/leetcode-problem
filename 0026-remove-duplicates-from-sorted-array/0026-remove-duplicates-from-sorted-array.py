class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return 1

        curr = 1
        count = 1

        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1]):
                curr += 1
            else:
                nums[count] = nums[curr]
                count += 1
                curr += 1

        return count