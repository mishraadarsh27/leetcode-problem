class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            distinct = set(nums)
            for num in distinct:
                nums.remove(num)
            ans += sorted(distinct)
        return ans 