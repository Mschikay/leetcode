class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


        def dfs(self, m, n, memo):
            if m == 0 or n == 0:
                return 1
            if memo[m][n]:
                return memo[m][n]
            up = self.dfs(m - 1, n, memo)
            left = self.dfs(m, n - 1, memo)
            memo[m][n] = up + left
            return memo[m][n]
        '''dfs'''
        memo = [[0] * n for _ in range(m)]
        return self.dfs(m - 1, n - 1, memo)

