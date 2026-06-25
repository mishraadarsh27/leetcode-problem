class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        i = 0
        my_set = set()
        while i < len(nums):
            k = 0
            for k in nums[i]:
                count[k] += 1
            i += 1
        for key, value in count.items():
            if value == len(nums):
                my_set.add(key)
        ans = sorted(my_set)
        return ans
        