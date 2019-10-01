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


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        # for i in range(len(nums) - 1):
        #     dp[i][i + 1] = nums[i] * nums[i + 1]
        length = len(nums)
        for l in range(3, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                for k in range(i + 1, j):
                    # burst all balloons from i to j, (i, j are kept)
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        print(dp)
        return dp[0][-1]