class Solution:
    def f(self, n, nums, target, dp):
        if target == 0:
            return 1
        if target < 0:
            return 0

        if dp[target] != -1:
            return dp[target]

        take = 0

        for j in range(n):
            take += self.f(n, nums, target - nums[j], dp)

        dp[target] = take
        return take

    def combinationSum4(self, nums, target):
        dp = [-1] * (target + 1)
        return self.f(len(nums), nums, target, dp)

# Example usage:
solution = Solution()
nums = [1, 2, 3]
target = 4
result = solution.combinationSum4(nums, target)
print("Number of combinations:", result)