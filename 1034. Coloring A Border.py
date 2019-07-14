class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        h, w = len(grid), len(grid[0])
        target = grid[r0][c0]

        def colorij(i, j, v, ans):
            if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] != target: return True
            if (i, j) not in v:
                v.add((i, j))
                p1, p2, p3, p4 = colorij(i + 1, j, v, ans), colorij(i - 1, j, v, ans), colorij(i, j + 1, v,
                                                                                               ans), colorij(i, j - 1,
                                                                                                             v, ans)
                if p1 or p2 or p3 or p4:
                    ans.append((i, j))  # 不可以在递归时修改grid
            return False

        v = set()
        ans = []
        colorij(r0, c0, v, ans)
        for i, j in ans:
            grid[i][j] = color
        return grid