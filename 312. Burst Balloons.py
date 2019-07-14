class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for i in range(len(nums))]

        def helper(i, j):
            if dp[i][j] or j == i + 1:
                return dp[i][j]

            coins = 0
            for k in range(i + 1, j):
                coins = max(coins, nums[i] * nums[j] * nums[k] + helper(i, k) + helper(k, j))
            dp[i][j] = coins
            return dp[i][j]

        return helper(0, len(nums) - 1)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for i in range(len(nums))]

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][len(nums) - 1]