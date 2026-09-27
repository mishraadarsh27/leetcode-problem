class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        equal = 0
        hashmap = defaultdict(int)
        for index in range(length - 1):
            if nums[index] == nums[index + 1]:
                equal = equal + 1
            else:
                a , b = nums[index] , nums[index + 1]
                if a > b:
                    a , b = b , a
                hashmap[(a , b)] = hashmap[(a , b)] + 1
        if hashmap :
            return equal + max(hashmap.values()) 
        else:
            return equal     