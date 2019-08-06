class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        res = 0
        for i in range(len(nums) - 1):
            m = 0
            for j in range(i - 1):
                m = max(m, dp[j])
            dp[i] = m + nums[i]
            res = max(res, dp[i])

        dp1 = [0] * len(nums)
        res1 = 0
        for i in range(1, len(nums)):
            m = 0
            for j in range(i - 1):
                m = max(m, dp1[j])
            dp1[i] = m + nums[i]
            res1 = max(res1, dp1[i])

        return max(res, res1)