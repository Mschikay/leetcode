class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if not i and not j:
                    dp[i][j] = grid[i][j]
                elif not i:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif not j:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

        return dp[-1][-1]