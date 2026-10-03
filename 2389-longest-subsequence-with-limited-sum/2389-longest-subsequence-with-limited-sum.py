class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        k = len(queries)

        res = []
        
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in queries:
            l , r = 0 , len(prefix) -1 
            while l <= r:
                mid = (l + r) // 2

                if prefix[mid] <= i:
                    l = mid + 1
                else:
                    r = mid - 1

            res.append(r)

        return res