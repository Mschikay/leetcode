class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf") for i in range(n)]
        for i in range(1, len(dp)):
            for j in range(1, int(pow(i, 0.5)) + 1):
                dp[i] = min(dp[i - j ** 2] + 1, dp[i])
        return dp[-1]