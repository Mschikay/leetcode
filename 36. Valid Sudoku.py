
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            col = set()
            cube = set()
            for j in range(len(board[0])):
                # print(i, j)
                if board[i][j] == ".":
                    pass
                else:
                    if board[i][j] in row:
                        return False
                row.add(board[i][j])
                if board[j][i] == ".":
                    pass
                else:
                    if board[j][i] in col:
                        return False
                col.add(board[j][i])

                cubeRow = (i // 3) * 3
                offsetRow = j // 3
                cubeCol = (i % 3) * 3
                offsetCol = j % 3
                t = board[cubeRow + offsetRow][cubeCol + offsetCol]
                if t == ".":
                    pass
                else:
                    if t in cube:
                        return False
                    cube.add(t)

        return True