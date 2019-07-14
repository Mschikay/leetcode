class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if obstacleGrid[i][j]:
                    continue
                if not i and not j:
                    dp[i][j] = 1
                elif not i:
                    dp[i][j] = dp[i][j - 1]
                elif not j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]