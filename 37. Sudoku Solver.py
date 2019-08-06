class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def legal(i, j, x):
            for y in range(9):
                if board[y][j] == x:
                    return False
                if board[i][y] == x:
                    return False
            r = (i // 3) * 3
            c = (j // 3) * 3
            for a in range(r, r + 3):
                for b in range(c, c + 3):
                    if board[a][b] == x:
                        return False
            return True

        def dfs(i, j):
            if i > 8: return True

            if board[i][j] == ".":
                for x in "123456789":
                    if legal(i, j, x):
                        board[i][j] = x
                        if j < 8:
                            if dfs(i, j + 1): return True
                        else:
                            if dfs(i + 1, 0): return True
                        board[i][j] = "."
                return False
            else:
                if j < 8:
                    if dfs(i, j + 1): return True
                else:
                    if dfs(i + 1, 0): return True

        dfs(0, 0)