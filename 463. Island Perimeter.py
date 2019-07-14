class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])

        def perimeter(i, j, v):
            if i < 0 or i >= h or j < 0 or j >= w: return 1
            if not grid[i][j]: return 1
            if grid[i][j]:
                ans = 0
                if (i, j) not in v:
                    v.add((i, j))
                    ans += perimeter(i + 1, j, v)
                    ans += perimeter(i - 1, j, v)
                    ans += perimeter(i, j + 1, v)
                    ans += perimeter(i, j - 1, v)
            return ans

        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    v = set()
                    return perimeter(i, j, v)


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])

        s = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    s += 4
                    if i > 0 and grid[i - 1][j]: s -= 2
                    if j > 0 and grid[i][j - 1]: s -= 2
        return s