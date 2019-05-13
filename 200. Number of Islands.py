class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(i, j):
            grid[i][j] = "0"
            for n, m in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= n < len(grid) and 0 <= m < len(grid[0]) and grid[n][m] == "1":
                    dfs(n, m)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res