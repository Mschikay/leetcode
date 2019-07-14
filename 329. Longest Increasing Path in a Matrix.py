# 时间和空间复杂度mn
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        h = len(matrix)
        w = len(matrix[0])
        longest = [[0 for i in range(w)] for j in range(h)]

        def dfs(i, j):
            if longest[i][j]:
                return longest[i][j]
            else:
                res = 1
                t = matrix[i][j]
                if 0 <= j - 1 < w and matrix[i][j - 1] > t:
                    res = max(res, 1 + dfs(i, j - 1))
                if 0 <= j + 1 < w and matrix[i][j + 1] > t:
                    res = max(res, 1 + dfs(i, j + 1))
                if 0 <= i - 1 < h and matrix[i - 1][j] > t:
                    res = max(res, 1 + dfs(i - 1, j))
                if 0 <= i + 1 < h and matrix[i + 1][j] > t:
                    res = max(res, 1 + dfs(i + 1, j))

            longest[i][j] = res
            return longest[i][j]

        ans = float("-inf")
        for i in range(h):
            for j in range(w):
                ans = max(ans, dfs(i, j))

        return ans


def __init__(self):
    self.max_len = 0
    self.table = {}


def longestIncreasingPath(self, matrix):
    def dfs(x, y, prev):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= prev:
            return 0

        if (x, y) in self.table:
            return self.table[(x, y)]

        path = 1 + max(dfs(x + 1, y, matrix[x][y]), dfs(x - 1, y, matrix[x][y]), dfs(x, y + 1, matrix[x][y]),
                       dfs(x, y - 1, matrix[x][y]))

        self.max_len = max(self.max_len, path)
        self.table[(x, y)] = path

        return path

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dfs(i, j, -sys.maxint)

    return self.max_len